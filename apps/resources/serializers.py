from rest_framework.serializers import ModelSerializer
from apps.resources.models import Resource

class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'link', 'description']
        read_only_fields = ['id']
