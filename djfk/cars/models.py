from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = settings.AUTH_USER_MODEL


def set_delete_user():
    User = get_user_model()
    return User.objects.get_or_create(username='deleted')[0]


def limit_car_choices():
    Q = models.Q
    return Q(username__iexact='travishen')


class Car(models.Model):
    owner = models.ForeignKey(User,
                              # SET_NULL # SET_DEFAULT # CASCADE
                              on_delete=models.SET(set_delete_user),
                              null=True,
                              limit_choices_to=limit_car_choices,
                              related_name='cars')
    first_owner = models.OneToOneField(User,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       related_name='first_owned_car')
    drivers = models.ManyToManyField(User,
                                     blank=True,
                                     related_name='drives_cars')
    name = models.CharField(max_length=15)

    update_by = models.ForeignKey(User,
                                  null=True, blank=True,
                                  related_name='updated_cars')

    def __str__(self):
        return self.name



