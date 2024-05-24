from rest_framework import serializers
from announcements.models import Announcement, Manager, Score
from accounts.serializers import UserSerializer

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['value']
        
class ManagerSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    average_score = serializers.SerializerMethodField()
    user = UserSerializer
    class Meta:
        model = Manager
        fields = ['name', 'scores', 'average_score', 'user']

    def get_average_score(self, obj):
        scores = obj.scores.all()
        if scores:
            return sum(score.value for score in scores) / len(scores)
        return 0


class AnnouncementSerializer(serializers.ModelSerializer):
    manager =  ManagerSerializer
    class Meta:
        model = Announcement
        fields = "__all__"




