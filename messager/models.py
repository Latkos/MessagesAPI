from django.core.validators import MinValueValidator
from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=160)
    view_counter = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    # every time message is updated, reset the view counter
    def save(self, **kwargs):
        self.view_counter = 0
        self.full_clean()
        super().save(**kwargs)
