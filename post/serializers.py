from rest_framework.serializers import ModelSerializer
from .models import Post
from tag.serializers import TagSerializer
from account.serializers import UserIdUsernameSerializer
from .models import Like
from rest_framework import serializers


class PostSerializer(ModelSerializer):
    author = UserIdUsernameSerializer(read_only=True)
    like_users = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = "__all__"
        
    def get_like_users(self, post):
        # post.like_set을 통해 Like 인스턴스들을 가져와
        # user PK 리스트로 반환
        return [ like.user.id for like in post.like_set.all() ]
