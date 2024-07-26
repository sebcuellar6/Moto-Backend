from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)