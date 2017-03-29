from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.permissions import (
    IsAdminUser,
)

from .serializers import (
    UserSerializer,
    UsersSerializer,
)

from .permissions import isStaffOrOwner

User = get_user_model()


class UserView(RetrieveUpdateDestroyAPIView):
    permission_classes = (isStaffOrOwner,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersView(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    