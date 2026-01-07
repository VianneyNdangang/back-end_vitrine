from rest_framework import serializers

from .models import Project, Service, Reviews


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "image", "date"]
        read_only_fields = ["date", "id"]

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "image"]
        read_only_fields = ["id"]

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ["id", "username", "company", "notation", "message", "created_at"]
        read_only_fields = ["id", "created_at"]