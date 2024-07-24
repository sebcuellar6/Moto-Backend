from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('forumposts/', views.ForumPostList.as_view(), name='forumpost_list'),
    path('forumposts/<int:pk>/', views.ForumPostDetail.as_view(), name='forumpost_detail'),
    path('meetups/', views.MeetUpEventList.as_view(), name='meetup_list'),
    path('meetups/<int:pk>/', views.MeetUpEventDetail.as_view(), name='meetup_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    path('messages/', views.MessagesList.as_view(), name='message_list'),
    path('messages/<int:pk>/', views.MessagesDetail.as_view(), name='message_detail'),
]
