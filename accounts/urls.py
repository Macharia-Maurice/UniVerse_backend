
from django.urls import path, re_path,include
from .views import (CustomProviderAuthView,
                    CustomTokenObtainPairView,
                    CustomTokenRefreshView,
                    CustomTokenVerifyView,
                    LogoutView,
                    ProfileDetail,
                    SearchView,
                    FollowToggleView,
                    FollowerList,
                    FollowingList,

                    UserProfileDetail,
                    UserAddressDetail,
                    UserEducationDetail,

                    AddressDetail,
                    EducationProfile,
                    EducationDetail,
                    
                    StudentList,
                    AlumniList,
                    LecturerList,
                    VerifiedList,
                    )

urlpatterns = [
    # Include the URLs from the 'djoser' app
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/o/(?P<provider>\S+)/$', CustomProviderAuthView.as_view(), name='provider-auth'),

    # Custom JWT token endpoints
    path('auth/jwt/create/', CustomTokenObtainPairView.as_view()),  # Endpoint to obtain JWT token pair
    path('auth/jwt/refresh/', CustomTokenRefreshView.as_view()),  # Endpoint to refresh JWT token
    path('auth/jwt/verify/', CustomTokenVerifyView.as_view()),  # Endpoint to verify JWT token


    path('auth/logout/', LogoutView.as_view()),  # Endpoint to log out user
    path('accounts/search/', SearchView.as_view() ), # Searching for Accounts

    # follow Urls
    path('follow-toggle/', FollowToggleView.as_view(), name='follow-toggle'), #Endpoint for following and un-follow users
    path('followers/', FollowerList.as_view(), name='follower-list'), # Endpoint to list followers
    path('following/', FollowingList.as_view(), name='following-list'), # Endpoint to list following


        # LoggedInUser URLs
    path('profile/', ProfileDetail.as_view(),name='profile-detail'),  # Read, Update and Delete(RUD) the logged-in user's profile
    path('address/', AddressDetail.as_view(), name='address-detail'),  # Retrieve, update a specific address for the logged-in user
    path('education/create/', EducationProfile.as_view(), name='education-create'),  # Create and list education details for the logged-in user
    path('education/<int:pk>/', EducationDetail.as_view(), name='education-detail'),  # Retrieve, update, or delete a specific education detail for the logged-in user
    
    # Normal User URLs
    path('user/profiles/<int:pk>/', UserProfileDetail.as_view(), name="userprofile-detail"),  # View the profile of a normal user
    path('user/addresses/<int:pk>/', UserAddressDetail.as_view(), name='address-create'),  # View the addresses of a normal user
    path('user/educations/<int:pk>/', UserEducationDetail.as_view(), name='user-education-detail'),  # View the education details of a normal user
    
    path('profile/student/', StudentList.as_view(), name="student-list"),
    path('profile/alumni/', AlumniList.as_view(), name="alumni-list"),
    path('profile/lecturer/', LecturerList.as_view(), name="lecturer-list"),
    path('profile/verified/', VerifiedList.as_view(), name="verified-list"),

]