from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import ProfilUser, PostUserMedia, PostUserVente
from .serializers import UserSerializer, ProfilUserSerializer, PostUserMediaSerializer, PostUserVenteSerializer


def index(request):
    return render(request, 'index.html')


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        ProfilUser.objects.create(user=user, bio='')

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfilUserView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profil


class PostUserMediaListCreateView(generics.ListCreateAPIView):
    serializer_class = PostUserMediaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return PostUserMedia.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUserVenteListCreateView(generics.ListCreateAPIView):
    serializer_class = PostUserVenteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return PostUserVente.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserPostsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        media_posts = PostUserMedia.objects.filter(
            user=request.user).order_by('-created_at')
        vente_posts = PostUserVente.objects.filter(
            user=request.user).order_by('-created_at')

        return Response({
            'media':
            PostUserMediaSerializer(media_posts, many=True).data,
            'vente':
            PostUserVenteSerializer(vente_posts, many=True).data,
        })
