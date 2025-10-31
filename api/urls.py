from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    LogoutView,
    ProfilUserView,
    PostUserMediaListCreateView,
    PostUserVenteListCreateView,
    UserPostsView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profil/', ProfilUserView.as_view(), name='profil'),
    path('posts/media/', PostUserMediaListCreateView.as_view(), name='media-posts'),
    path('posts/vente/', PostUserVenteListCreateView.as_view(), name='vente-posts'),
    path('my-posts/', UserPostsView.as_view(), name='user-posts'),
]
