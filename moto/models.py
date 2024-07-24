from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    zipcode = models.IntegerField()  # Changed from FloatField to IntegerField
    photo = models.ImageField(upload_to='photos/', default='default_photo.jpg')

    def __str__(self):
        return str(self.username)
    
class ForumPost(models.Model):
    title = models.CharField(max_length=75)
    tags = models.CharField(max_length=200)
    body = models.CharField(max_length=2500)
    images = models.TextField()
    links = models.CharField(max_length=2500)
    category = models.CharField(max_length=500)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='forum_posts')
    first_choice = models.CharField(max_length=150, blank=True, null=True)
    second_choice = models.CharField(max_length=150, blank=True, null=True)
    votes1 = models.FloatField(default=0, blank=True, null=True)
    votes2 = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.title)
    
class MeetUpEvent(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=2500)
    invite_only = models.BooleanField()
    main_image = models.TextField()
    images = models.TextField()
    category = models.CharField(max_length=500)
    skill_level = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
    type = models.CharField(max_length=30)
    tags = models.CharField(max_length=200)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='meetup_events')

    def __str__(self):
        return str(self.name)
    
class Messages(models.Model):
    outgoing = models.BooleanField()
    incoming = models.BooleanField()
    body = models.CharField(max_length=2500)
    from_profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
    to_profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages')

    def __str__(self):
        return str(self.from_profile_id)
    
class Comment(models.Model):
    body = models.CharField(max_length=2500)
    image = models.TextField()
    post_id = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return str(self.body)
