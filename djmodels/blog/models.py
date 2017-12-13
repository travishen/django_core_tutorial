from django.db import models
from django.db.models import (CharField, TextField,
                              IntegerField, DateField,
                              SlugField)
from django.utils.encoding import smart_text
from .validators import validate_author_email
from django.utils.text import slugify

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)


class PostModel(models.Model):
    title = CharField(max_length=20, default='', unique=True)
    content = TextField(null=True, blank=True)
    publish = CharField(max_length=120, default='draft', choices=PUBLISH_CHOICES)
    view_count = IntegerField(default=0)
    publish_date = DateField(auto_now=False, auto_now_add=False)
    author_email = CharField(max_length=240,
                             validators=[validate_author_email],
                             null=True,
                             blank=True)
    slug = SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_text(self.title)

    def __str__(self):
        return smart_text(self.title)


