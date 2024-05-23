from rest_framework import serializers
from announcements.models import Announcement, AnnouncementJoinRequest


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"

class AnnouncementJoinRequestSerializer(serializers.ModelSerializer):
    announcement_title = serializers.CharField(source='announcement.title', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = AnnouncementJoinRequest
        fields = ('id', 'user', 'announcement', 'status', 'created_at', 'announcement_title', 'user_username')


