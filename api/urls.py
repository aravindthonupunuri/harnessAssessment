from django.urls import path
from . import userViews
from . import postViews
from . import likesViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('alluser/', userViews.getUsers),
    path('user/<str:email>', userViews.getUser),
    path('addPost/', postViews.addPost),    
    path('posts/<int:id>/', postViews.getPostById),
    path('change/posts/<int:id>/', postViews.updatePost),
    path('delete/posts/<int:id>/', postViews.deletePost),
    path('email/posts/<str:email>/', postViews.getPostByEmail),
    path('posts/', postViews.getPosts),
    path('addLikedislike/', likesViews.addLikeDislike),
    path('likes/', likesViews.getLikes),
    path('delete/likedislike/<int:id>/', likesViews.deleteLike),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('addUser/', userViews.addUser),
]