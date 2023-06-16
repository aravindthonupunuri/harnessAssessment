from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PostSerializer
from base.models import Post

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def getPostByEmail(request, email):
    try:
        posts = Post.objects.filter(email=email)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response("Post not found", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getPostById(request, id):
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response("Post not found", status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updatePost(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response("Post not found", status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletePost(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response("Post not found", status=status.HTTP_404_NOT_FOUND)

    post.delete()
    return Response("Post deleted successfully", status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      