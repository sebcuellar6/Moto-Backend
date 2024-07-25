from rest_framework import serializers
from .models import Comment, Messages, MeetUpEvent, ForumPost, Profile, Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=ForumPost.objects.all()
    )
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = Comment
        fields = ['id', 'body', 'image', 'post_id', 'profile_id']

class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    from_profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )
    to_profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = Messages
        fields = ['id', 'outgoing', 'incoming', 'body', 'from_profile_id', 'to_profile_id']

class MeetUpEventSerializer(serializers.HyperlinkedModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )
    category = CategorySerializer(many=True, read_only=True)
    

    class Meta:
        model = MeetUpEvent
        fields = ['id', 'name', 'category', 'description', 'invite_only', 'main_image', 'images', 'skill_level', 'location', 'type', 'tags', 'profile_id']


class ForumPostSerializer(serializers.HyperlinkedModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )
    category = CategorySerializer(many=True, read_only=True)
    username = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = ForumPost
        fields = ['id', 'title', 'tags', 'category', 'body', 'images', 'links', 'profile_id', 'username', 'first_choice', 'second_choice', 'votes1', 'votes2', 'comments']

    def get_username(self, obj):
        return obj.profile_id.username

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    forum_posts = ForumPostSerializer(many=True, read_only=True)
    meetup_events = MeetUpEventSerializer(many=True, read_only=True)
    messages = MessagesSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'city', 'state', 'zipcode', 'photo', 'forum_posts', 'meetup_events', 'messages', 'comments']
