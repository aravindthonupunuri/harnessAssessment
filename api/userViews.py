from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User
from .serializers import UserSerializer
from requests.exceptions import RequestException
import requests
from datetime import date
import time
import hashlib

MAX_RETRIES = 3
RETRY_DELAY = 2

def make_request(url):
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except (RequestException, ValueError) as e:
            print(f"Request failed. Retrying in {RETRY_DELAY} seconds... (Attempt {attempt+1}/{MAX_RETRIES})")
            time.sleep(RETRY_DELAY)
    return None

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def getUser(request, email):
    try:
        user = User.objects.get(email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response("Post not found", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        useremail = serializer.data.get('email')
        try:
            emailResponse = make_request('https://emailvalidation.abstractapi.com/v1/?api_key=91818e66dbed4a9db23e14cff9017bb6&email=' + useremail)
            if emailResponse.get('deliverability') == "UNDELIVERABLE":
                return Response("Invalid email id")
            else:
                locationResponse = make_request('https://ipgeolocation.abstractapi.com/v1/?api_key=90d4d84f09c9457e90b10ba1b8cf7afb')
                serializer.validated_data['city'] = locationResponse.get('city')
                
                password = serializer.data.get('password')
                hash_object = hashlib.sha256()
                hash_object.update(password.encode("utf-8"))
                serializer.validated_data['password'] = hash_object.hexdigest()

                serializer.validated_data['isHoliday'] = False 
                today = date.today()                
                str_today = today.strftime("%Y-%m-%d")
                date_parts = str_today.split("-")                
                holidayResponse = make_request('https://holidays.abstractapi.com/v1/?api_key=070fb22fcf1d4533b4077776ac461182&country=US&year=' + date_parts[0] + '&month=' + date_parts[1] + '&day=' + date_parts[2])
                if holidayResponse:
                   serializer.validated_data['isHoliday'] = True

                # Create a new User object with the validated data
                user_object = User(**serializer.validated_data)
                user_object.save()

                serialized_user = UserSerializer(user_object)
                response_data = serialized_user.data

                return Response(response_data)

        except RequestException as e:
            return Response("Error occurred while making a request to the API")

    return Response(serializer.errors)