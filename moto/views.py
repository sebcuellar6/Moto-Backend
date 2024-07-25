from rest_framework import generics
from .serializers import ProfileSerializer, CommentSerializer, MeetUpEventSerializer, ForumPostSerializer, MessagesSerializer, CategorySerializer
from .models import Profile, Comment, MeetUpEvent, ForumPost, Messages, Category

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class MeetUpEventList(generics.ListCreateAPIView):
    queryset = MeetUpEvent.objects.all()
    serializer_class = MeetUpEventSerializer

class MeetUpEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeetUpEvent.objects.all()
    serializer_class = MeetUpEventSerializer

class ForumPostList(generics.ListCreateAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer

class ForumPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer

class MessagesList(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

class MessagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Create your views here.
