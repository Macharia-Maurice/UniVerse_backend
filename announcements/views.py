from .models import Announcement
from accounts.models import UserProfile
from .serializers import AnnouncementSerializer
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.permissions import IsOwnerOrReadOnly
from django.db.models import Q
from support.permissions import IsAdminOrReadOnly
from django.utils.translation import gettext_lazy as _

# Create your views here.
class ListCreateAnnouncement(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user

        # Ensure the user has a related UserProfile
        try:
            user_profile = user.user_profile
        except UserProfile.DoesNotExist:
            raise NotFound("UserProfile matching query does not exist.")

        # Check if the user is a superuser (admin)
        if not user.is_superuser:
            raise ValidationError(_("Only admins can create announcements."))

        serializer.save(creator=user_profile)


class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsOwnerOrReadOnly]


class AnnouncementSearchView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q', '')

        if not query:
            return Response({'error': _('Query parameter "q" is required.')}, status=status.HTTP_400_BAD_REQUEST)

        announcement_results = Announcement.objects.filter(
            Q(title__icontains=query) |
            Q(creator__user__email__icontains=query) |
            Q(creator__user__first_name__icontains=query) |
            Q(content__icontains=query)
        ).order_by('-created_at')
        
        if not announcement_results.exists():
            raise NotFound("No announcements match the search query.")
        
        announcement_serializer = self.get_serializer(announcement_results, many=True)

        return Response({'Announcements': announcement_serializer.data})
    
