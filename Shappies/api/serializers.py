from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
        # pw is write only so you can't see it and required if want to post and not get
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    #  override the create method but use the validated data to create user
    # needed to hash the password sent from client so we don't store passwords
    def create(self, validated_data):  # validated data is data being sent by the request
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)  # create a token for the newly created user
        return user

