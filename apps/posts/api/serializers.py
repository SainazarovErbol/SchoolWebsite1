from rest_framework import serializers
from apps.posts.models import Post, PostImage


class PostCreateSerializer(serializers.ModelSerializer):
    # create post serializer
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
        ]


class PostListSerializer(serializers.ModelSerializer):
    # List Post serializer
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'created_at',
        ]


class PostDeleteSerializer(serializers.ModelSerializer):
    # Delete Post serializer
    class Meta:
        model = Post


class PostImageCreateSerializer(serializers.ModelSerializer):
    # Create PostImage serializer
    class Meta:
        model = PostImage
        fields = [
            'post',
            'image',
        ]


class PostImageListSerializer(serializers.ModelSerializer):
    # List PostImage serializer
    class Meta:
        model = PostImage
        fields = [
            'id',
            'post',
            'image',
        ]


class PostImageSerializer(serializers.ModelSerializer):
    # Detail PostImage serializer
    class Meta:
        model = PostImage
        fields = [
            'id',
            'post',
            'image',
        ]


class PostImageUpdateSerializer(serializers.ModelSerializer):
    # Update PostImage serializer
    class Meta:
        model = PostImage
        fields = [
            'image',
        ]


class PostImageDeleteSerializer(serializers.ModelSerializer):
    # Delete PostImage serializer
    class Meta:
        model = PostImage
        fields = []  # No fields required