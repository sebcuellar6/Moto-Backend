from rest_framework import serializers
from .models import Comment, Messages, MeetUpEvent, ForumPost, Profile

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'

class MeetUpEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeetUpEvent
        fields = '__all__'

class ForumPostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = ForumPost
        fields = '__all__'

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    forum_posts = ForumPostSerializer(
        many=True,
        read_only=True
    )
    meetup_events = MeetUpEventSerializer(
        many=True,
        read_only=True
    )
    sent_messages = MessagesSerializer(
        many=True,
        read_only=True
    )
    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Profile
        fields = '__all__'

