from django.db import models
from django.contrib.auth.models import User
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/games', filename)

class Games(models.Model):

    STATUS = [
        ('PLAYING', 'Playing'),
        ('COMPLETED', 'Completed'),
        ('TO-PLAY', 'To-Play'),
    ]

    COLLECTION_TYPE = [
        ('PHYSICAL', 'Own Physically'),
        ('DIGITAL', 'Own Digitally'),
    ]

    PLATFORM = [
        ('PC', 'PC'),
        ('PLAYSTATION', 'Playstation'),
        ('XBOBX', 'Xbox'),
        ('SWITCH', 'Nintendo Switch'),
    ]

    cover_image = models.FileField(upload_to=get_file_path,
                        null=True,
                        blank=True,
                    )
    title = models.CharField(max_length=50)
    review = models.CharField(max_length=200)
    status = models.CharField(
        max_length=50,
        choices=STATUS,
        default=STATUS[0][0],
    )
    collected_on = models.CharField(
        max_length=50,
        choices=COLLECTION_TYPE,
        default=COLLECTION_TYPE[0][0],
    )
    platform = models.CharField(
        max_length=50,
        choices=PLATFORM,
        default=PLATFORM[0][0],
    )
    completed =  models.BooleanField(default=False)
    started_playing_on = models.DateTimeField(
        blank=True,
        null=True,
    )
    completed_playing_on = models.DateTimeField(
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='games')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'games'
        verbose_name = "Game"
        verbose_name_plural = "Games"
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
