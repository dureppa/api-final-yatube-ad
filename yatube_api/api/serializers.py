from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.models import Comment, Post, Group, Follow
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', 'author')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = '__all__'
        read_only_fields = ('user',)

    def validate_following(self, value):
        request = self.context['request']
        if request.user == value:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!")
        if Follow.objects.filter(user=request.user, following=value).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого пользователя!")
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
