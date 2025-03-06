from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    slug = serializers.SlugField()
    description = serializers.CharField()
    posts_count = serializers.SerializerMethodField()

    def get_posts_count(self, obj):
        return obj.posts.count()
