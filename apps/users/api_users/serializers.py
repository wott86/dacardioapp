from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    EmailField,
    ModelSerializer,
    CharField,
    ValidationError
)

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    email = EmailField()
    first_name = CharField()
    last_name = CharField()
    confirm_password = CharField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
        )
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return validated_data


    def validate_confirm_password(self, value):
        password = self.get_initial().get('password')
        print password, value
        if password != value:
            raise ValidationError('Confirm password do not match.')
        return value


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )
