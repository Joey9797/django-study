from django.db import models
from django.conf import settings

# Create your models here.
class Diary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='diaries')
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
    content = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=255)