from rest_framework.permissions import AllowAny
from rest_framework import generics
from users.models import Profile
from .serializers import UserSerializer

# Vista para listar todos los usuarios
class UserList(generics.ListAPIView):
    permission_classes = [AllowAny]  # Permite acceso a todos

    queryset = Profile.objects.all()
    serializer_class = UserSerializer

# Vista para ver los detalles de un usuario específico
class UserDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer