from rest_framework import serializers
from .models import Post, PostImage


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'name',
            'age',
            'species',
            'breed',
            'color',
            'contact',
            'city',
            'state',
            'address',
            'post_type',
            'is_resolved',
            'author',
        ]


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = [
            'id',
            'image',
            'post',
        ]


class CreatedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = [
            'id',
        ]


class PostSerializerWithImages(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'name',
            'age',
            'species',
            'breed',
            'color',
            'contact',
            'city',
            'state',
            'address',
            'post_type',
            'images',
            'is_resolved',
            'author',
        ]
