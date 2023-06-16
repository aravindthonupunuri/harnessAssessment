from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import LikeDislikeSerializer
from base.models import LikeDislike

@api_view(['GET'])
def getLikes(request):
    likes = LikeDislike.objects.all()
    serializer = LikeDislikeSerializer(likes, many=True)
    return Response(serializer.data) 

@api_view(['DELETE'])
def deleteLike(request, id):
    try:
        post = LikeDislike.objects.get(id=id)
    except LikeDislike.DoesNotExist:
        return Response("LikeDislike not found", status=status.HTTP_404_NOT_FOUND)

    post.delete()
    return Response("LikeDislike deleted successfully", status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addLikeDislike(request):
    serializer = LikeDislikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      