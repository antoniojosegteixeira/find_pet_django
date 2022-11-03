from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['uuid', 'name', 'age', 'species', 'breed', 'color',
                  'contact', 'city', 'state', 'address', 'post_type', 'is_found', 'author']
