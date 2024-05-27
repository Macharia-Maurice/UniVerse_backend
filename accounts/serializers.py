from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import UserProfile, MyUser, Address, Education

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

#AddressModel Serializer
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


# EducationModel Serializer
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    user = MyUserSerializer()
    address = AddressSerializer()
    education = EducationSerializer()

    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'address', 'education', 'profile_picture', 'is_student', 
            'is_alumni', 'is_lecturer', 'isAdmin', 'created_at', 'updated_at', 
            'phone_number', 'bio', 'linked_in_url', 'x_in_url'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        address_data = validated_data.pop('address')
        education_data = validated_data.pop('education')

        user = MyUserSerializer.create(MyUserSerializer(), validated_data=user_data)
        address = AddressSerializer.create(AddressSerializer(), validated_data=address_data)
        education = EducationSerializer.create(EducationSerializer(), validated_data=education_data)

        user_profile = UserProfile.objects.create(user=user, address=address, education=education, **validated_data)
        return user_profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        address_data = validated_data.pop('address')
        education_data = validated_data.pop('education')

        user = instance.user
        address = instance.address
        education = instance.education

        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.is_student = validated_data.get('is_student', instance.is_student)
        instance.is_alumni = validated_data.get('is_alumni', instance.is_alumni)
        instance.is_lecturer = validated_data.get('is_lecturer', instance.is_lecturer)
        instance.isAdmin = validated_data.get('isAdmin', instance.isAdmin)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.linked_in_url = validated_data.get('linked_in_url', instance.linked_in_url)
        instance.x_in_url = validated_data.get('x_in_url', instance.x_in_url)
        instance.save()

        MyUserSerializer.update(MyUserSerializer(), instance=user, validated_data=user_data)
        AddressSerializer.update(AddressSerializer(), instance=address, validated_data=address_data)
        EducationSerializer.update(EducationSerializer(), instance=education, validated_data=education_data)

        return instance
