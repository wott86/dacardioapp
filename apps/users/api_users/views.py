from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status, permissions

from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

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
    filter_backends = (SearchFilter,)
    search_fields = ('username', 'email', 'first_name', 'last_name')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer

class UserUpdatePasswordView(UpdateAPIView):
    permission_classes = (isOwner,)
    queryset = User.objects.all()
    serializer_class = UserUpdatePasswordSerializer

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'user': self.request.user,
            'format': self.format_kwarg,
            'view': self
        }

