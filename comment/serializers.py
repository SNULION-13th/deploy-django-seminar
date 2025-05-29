from rest_framework.serializers import ModelSerializer
from .models import Comment
from account.serializers import UserIdUsernameSerializer

class CommentSerializer(ModelSerializer):
    # author를 사용자 객체로 직렬화하여 .id, .username 사용 가능
    author = UserIdUsernameSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
