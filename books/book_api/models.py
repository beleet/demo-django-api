from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    published_date = models.DateTimeField(default=datetime.now)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
