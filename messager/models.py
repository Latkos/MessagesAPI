from django.core.validators import MinValueValidator
from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=160)
    view_counter = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __init__(self, *args, **kwargs): # we need to store the earlier title and content to see if it changed
        super(Message, self).__init__(*args, **kwargs)
        self.__original_title = self.title
        self.__original_content = self.content

    def save(self, **kwargs):
        if self.title != self.__original_title or self.content != self.__original_content: # if we changed the message
            # we need to reset the view counter
            self.view_counter = 0
        self.full_clean() # to enforce the character limit even in SQLite
        super().save(**kwargs)
