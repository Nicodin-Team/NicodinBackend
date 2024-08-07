from rest_framework import serializers
from .models import CustomUser, Skill
from django.contrib.auth.hashers import make_password

class UserRegistrationSerializer(serializers.ModelSerializer):     
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'username', 'first_name', 'last_name', 'gender', 'age', 'country', 'city']
        extra_kwargs = {
            'email': {'required': True,},
            'username': {'required': True},
            'password': {'required': True, 'write_only': True}
        }
        
    def create(self, validated_data):        
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ['id', 'photo', 'bio', 'username', 'first_name', 'last_name', 'created_at', 'gender', 'age', 'country', 'city']
        read_only_fields = ['id']
    

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'level']


class PasswordRecoverySerializer(serializers.Serializer):
    token = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)
    confirm_password = serializers.CharField(required = True)

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')
        
        if new_password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

        





