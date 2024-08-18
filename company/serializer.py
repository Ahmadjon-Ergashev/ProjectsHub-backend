from rest_framework import permissions, serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }
