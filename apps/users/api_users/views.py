from django.contrib.auth import get_user_model

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView
)
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import (
    UserCreateSerializer,
    UserSerializer,
    UserUpdatePasswordSerializer
)

from .permissions import (
    isStaffOrOwner,
    isOwner
)

User = get_user_model()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (isStaffOrOwner,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer

class UserUpdatePasswordView(UpdateAPIView):
    permission_classes = (isOwner,)
    queryset = User.objects.all()
    serializer_class = UserUpdatePasswordSerializer
