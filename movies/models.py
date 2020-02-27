from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'movies'
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
