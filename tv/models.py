from django.db import models
from django.contrib.auth.models import User
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/tv', filename)

class Shows(models.Model):

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
    show_title = models.CharField(max_length=50)
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
    watching =  models.BooleanField(default=False)
    started_watching_on = models.DateTimeField(
        blank=True,
        null=True,
    )
    completed_watching_on = models.DateTimeField(
        blank=True,
        null=True,
    )
    seasons_watched = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='tv')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shows'
        verbose_name = "Show"
        verbose_name_plural = "Shows"
        ordering = ['-updated_at']

    def __str__(self):
        return self.show_title
