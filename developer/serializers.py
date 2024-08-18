from rest_framework import permissions, serializers
from .models import Developer, Team, Skill


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        extra_kwargs = {
            "team_leader": {"read_only": True},
        }


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
