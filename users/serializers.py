from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from users.models import CustomUser


class UserUpdateListDetailSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateTimeField(
        required=False,
        format="%d/%m/%Y",
        input_formats=["%d/%m/%Y", "%d-%m-%Y"]
    )

    class Meta():
        model = CustomUser
        fields = ['id', 'email', 'username', 
                  'name', 'date_joined', 'description',
                  'birth_date', ]
        
        read_only_fields = ['id', 'date_joined']


class UserCreateSerializer(serializers.ModelSerializer):

    birth_date = serializers.DateTimeField(
        required=False,
        format="%d/%m/%Y",
        input_formats=["%d/%m/%Y", "%d-%m-%Y"]
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'},
        label='Password'
    )

    confirm_password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'},
        label='Confirm Password'
    )


    class Meta():
        model = CustomUser
        fields = ['id', 'email', 'username', 
                  'name', 'password', 'confirm_password',
                  'description', 'birth_date']
        read_only_fields = ['id']


    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("The passwords must be equal!!!")
        validate_password(attrs['password'])
        return attrs
    

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


