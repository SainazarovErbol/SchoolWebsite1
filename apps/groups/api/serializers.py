from rest_framework import serializers

from apps.groups.models import Group


class GroupCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'name'
        ]


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name'
        ]


class GroupDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'teacher',
            'students',
        ]


class GroupDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

