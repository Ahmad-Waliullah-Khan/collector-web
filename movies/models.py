from django.db import models
from django.contrib.auth.models import User
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/games', filename)

class Movies(models.Model):

    STATUS = [
        ('WATCHING', 'Watching'),
        ('COMPLETED', 'Completed'),
        ('TO-WATCH', 'To-Watch'),
    ]

    COLLECTION_TYPE = [
        ('PHYSICAL', 'Own Physically'),
        ('DIGITAL', 'Own Digitally'),
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
    watched =  models.BooleanField(default=False)
    started_watching_on = models.DateTimeField(
        blank=True,
        null=True,
    )
    completed_watching_on = models.DateTimeField(
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='movies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'movies'
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ['-completed_watching_on']

    def __str__(self):
        return self.title
