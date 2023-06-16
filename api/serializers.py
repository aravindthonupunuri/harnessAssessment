from rest_framework import serializers
from base.models import User
from base.models import Post
from base.models import LikeDislike

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'   

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  

class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = '__all__'  