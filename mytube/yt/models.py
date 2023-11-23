from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/avatar')
    backphoto = models.ImageField(upload_to='uploads/background')
    uploaded_videos = models.ManyToManyField('Videos', related_name='profile_uploads', blank=True)

    def __str__(self):
        return f'profile: {self.user.username}'

    class Meta:
        verbose_name = "Profile"

class Videos(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_upload = models.DateTimeField(auto_now_add=True)
    video = models.FileField(blank=True, null=True, upload_to="uploads/video")
    uploaders = models.ManyToManyField(Profile, related_name='video_uploads', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
