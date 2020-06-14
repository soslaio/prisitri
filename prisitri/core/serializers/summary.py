
from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Company, ResourceType, ExtendedUser, ApprovalGroup, ScheduleType, Resource


class UserSummarySerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'email')

    def get_full_name(self, obj):
        return obj.get_full_name()


class CompanySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'url')


class ExtendedUserSummarySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    user = UserSummarySerializer()

    class Meta:
        model = ExtendedUser
        fields = ('id', 'user', 'url')


class ResourceTypeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceType
        fields = ('id', 'name', 'url')


class ScheduleTypeSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleType
        fields = ('id', 'name', 'time', 'unit', 'url')


class ApprovalGroupSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalGroup
        fields = ('id', 'name', 'url')


class ResourceSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'name', 'url')
