from django.db import models
from django.contrib.auth.models import User
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/comics', filename)

class ComicBooks(models.Model):

    STATUS = [
        ('READING', 'Reading'),
        ('COMPLETED', 'Completed'),
        ('TO-READ', 'To-Read'),
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
    reading =  models.BooleanField(default=False)
    completed_reading =  models.BooleanField(default=False)
    started_reading_on = models.DateTimeField(
        blank=True,
        null=True,
    )
    completed_reading_on = models.DateTimeField(
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='comics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comicbooks'
        verbose_name = "ComicBook"
        verbose_name_plural = "ComicBooks"
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
