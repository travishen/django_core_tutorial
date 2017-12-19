from django.db import models
from django.db.models import ForeignKey, CharField, TextField, SlugField, DateTimeField
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
# Create your models here.


class Book(models.Model):
    added_by = ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='book_add')
    last_edited_by = ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='book_edit')
    title = CharField(max_length=120)
    description = TextField(null=True, blank=True)
    slug = SlugField(unique=True)
    updated = DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cbv:book_detail', kwargs={'slug': self.slug})


def pre_save_book(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slug


pre_save.connect(pre_save_book, sender=Book)
