from rest_framework import generics, status, permissions, views

from rest_framework.response import Response

from django.contrib.auth import login

from users.models import CustomUser
from users.serializers import UsersSerializer, UserRegistrationSerializer, UserLoginSerializer, UserUpdateSerializer

from users.permissions import IsOwnerOrReadOnly

class UsersListAPI(generics.ListCreateAPIView):
    serializer_class = UsersSerializer
    queryset = CustomUser.objects.all()


class RegisterAPI(generics.ListCreateAPIView):
    """
    This view provides 'list' for all users and 'create' new users.
    """
    serializer_class = UserRegistrationSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(generics.GenericAPIView):
    """
    This view provides 'login' functionality for users.
    """
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):        
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            if user:
                login(request, user)
                data = {
                    'user_id': user.id,
                    'username': user.username,
                    'message': 'Logged in successfully'
                }
                return Response(data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     


class UsersDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    This view provides 'retrieve', 'update', 'destroy' actions to appropriate users.
    """
    serializer_class = UserUpdateSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'username'


class LogoutAPI(views.APIView):
    def get(self, request, format=None):
        request.session.flush() # Removes Session from Storage
        try:
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
