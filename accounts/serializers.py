from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import UserProfile, MyUser, Address, Education, Follower

# customUser Serializer
class MyUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
        
# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()


    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'profile_picture', 'is_student',
            'is_alumni', 'is_lecturer', 'isAdmin', 'is_verified', 'created_at', 'updated_at',
            'phone_number', 'bio', 'linked_in_url', 'x_in_url','followers_count', 'following_count',
        ]
        read_only_fields = ('created_at', 'updated_at', 'followers_count', 'following_count')
    
    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()


class AddressSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    class Meta:
        model = Address
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.user_profile)

# EducationModel Serializer
class EducationSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    class Meta:
        model = Education
        fields = '__all__'


#AddressModel Serializer

class FollowerSerializer(serializers.ModelSerializer):
    follower_name = serializers.SerializerMethodField()
    followed_name = serializers.SerializerMethodField()

    class Meta:
        model = Follower
        fields = ['id','follower_name','followed_name','created_at']

    def get_follower_name(self, obj):
        return f"{obj.follower.user.first_name} {obj.follower.user.last_name}"

    def get_followed_name(self, obj):
        return f"{obj.followed.user.first_name} {obj.followed.user.last_name}"
    
    
    
    # user serializer with fewer fields
class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name']

    # userprofile serializer with fewer fields
class UserProfileSimpleSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='userprofile-detail',lookup_field='pk')
    class Meta:
        model = UserProfile
        fields = ['id', 'url', 'user', 'profile_picture', 'is_verified']
        read_only_fields = ['profile_picture', "is_verified"]
