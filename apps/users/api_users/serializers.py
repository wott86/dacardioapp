from django.contrib.auth import get_user_model
from rest_framework.fields import CurrentUserDefault

from rest_framework.serializers import (
    EmailField,
    ModelSerializer,
    CharField,
    Serializer,
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

class UserUpdatePasswordSerializer(Serializer):

    old_password = CharField()
    new_password = CharField()
    confirm_new_password = CharField()

    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password',
            'confirm_new_password',
        )

    def validate_confirm_new_password(self, value):
        confirm_new_password = self.get_initial().get('new_password')
        if confirm_new_password != value:
            raise ValidationError('Confirm password do not match.')
        return value

    def validate_old_password(self, value):
        user = self.context.get("user")
        if user.check_password(value) is False:
            raise ValidationError('Wrong password.')

        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance

    def to_representation(self, obj):
        return {}
