from django.db import models
from django.db.models import CharField, TextField, IntegerField, DateField
from django.utils.encoding import smart_text

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

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __unicode__(self):
        return smart_text(self.title)

    def __str__(self):
        return smart_text(self.title)

