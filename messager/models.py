from django.core.validators import MinValueValidator
from django.db import models


class Message(models.Model):
    title=models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    view_counter = models.IntegerField(default=0, validators=[MinValueValidator(0)])
