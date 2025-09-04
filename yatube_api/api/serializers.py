from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("post",)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",
    )

    class Meta:
        model = Follow
        fields = ("user", "following")

    def validate_following(self, value):
        user = self.context["request"].user
        if user == value:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя.")
        if Follow.objects.filter(user=user, following=value).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого пользователя.")
        return value
