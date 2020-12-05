from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)
    thumbnail = models.CharField(max_length=500)
    
    class Meta:
        indexes = [
            models.Index(fields=['-published_at']),
        ]
