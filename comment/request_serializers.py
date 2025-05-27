from rest_framework import serializers

from account.request_serializers import SignInRequestSerializer


class CommentListRequestSerializer(serializers.Serializer):
    post = serializers.IntegerField()
    content = serializers.CharField()


class CommentDetailRequestSerializer(serializers.Serializer):
    content = serializers.CharField()
