from django.db import models
from django.db.models import (CharField, TextField,
                              IntegerField, DateField,
                              SlugField, BooleanField)


class PostModel(models.Model):
    title = CharField(max_length=20,
                      default='',
                      unique=True,
                      error_messages={
                          'unique': 'this title is not unique, please try again!',
                          'blank': 'this title is blank, please try again!'
                      },
                      help_text='must be an unique title')
    active = BooleanField(default=False)
    content = TextField(null=True, blank=True)
    view_count = IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Posts'

# Create your models here.
