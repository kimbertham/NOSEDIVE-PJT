# pylint: disable=arguments-differ
from rest_framework import serializers
from django.contrib.auth import get_user_model
# import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from photos.serializers import PhotoSerializer


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)


    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'does not match'})
        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise serializers.ValidationError({'password': err.messages})
        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = '__all__'

class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('first_name','last_name','description','tagline','career','location','age','relationship','profile_image','id','username' )

class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('first_name','last_name','id','profile_image','id','username' )


