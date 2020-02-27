from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comicbooks'
        verbose_name = "ComicBook"
        verbose_name_plural = "ComicBooks"
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
