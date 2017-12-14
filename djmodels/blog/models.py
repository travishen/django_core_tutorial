from django.db import models
from django.db.models import (CharField, TextField,
                              IntegerField, DateField,
                              SlugField, DateTimeField,
                              BooleanField)
from django.utils.encoding import smart_text
from .validators import validate_author_email
from django.utils.text import slugify

from django.db.models.signals import post_save, pre_save

from django.utils.timesince import timesince
from datetime import datetime, timedelta

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)


class PostModelManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(PostModelManager, self).all(*args, **kwargs).filter(active=True)
        return qs


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
    publish = CharField(max_length=120, default='draft', choices=PUBLISH_CHOICES)
    view_count = IntegerField(default=0)
    publish_date = DateField(auto_now=False, auto_now_add=False)
    author_email = CharField(max_length=240,
                             validators=[validate_author_email],
                             null=True,
                             blank=True)
    slug = SlugField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    other = PostModelManager()

    class Meta:
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        # if not self.slug:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    @property
    def age(self):
        if self.publish != 'publish':
            return 'Not published!'

        now = datetime.now()
        publish_time = datetime.combine(self.publish_date, now.min.time())

        try:
            diff = now - publish_time
        except:
            return 'Not published'

        if diff <= timedelta(minutes=1):
            return 'just now'
        return timesince(self.publish_date)

    def __unicode__(self):
        return smart_text(self.title)

    def __str__(self):
        return smart_text(self.title)


def post_model_save_receiver(sender, instance, created, *args, **kwargs):
    print('call post_model_save_receiver')
    print(created)
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()


post_save.connect(post_model_save_receiver, sender=PostModel)


def post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)


# pre_save.connect(post_model_pre_save_receiver, sender=PostModel)


