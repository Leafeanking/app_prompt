from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import math
import random

def get_random_item(model, max_id=None):
    '''
    Credit for this function to Mikhail Korobov:
        http://stackoverflow.com/a/971671
    '''
    if max_id is None:
        max_id = model.objects.aggregate(models.Max('id')).values()[0]
    min_id = math.ceil(max_id*random.random())
    return model.objects.filter(id__gte=min_id).first()


class Prompt(models.Model):
    name = models.CharField(
        max_length=100,
        default='',
    )
    description = models.TextField(
        blank=True,
        default='',
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        default=None,
    )
    creator = models.ForeignKey(
        User,
        default=None,
        null=True,
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        default='',
    )

    def __str__(self):
        return self.name


class Feature(models.Model):
    prompt = models.ForeignKey(
        Prompt,
    )
    name = models.CharField(
        max_length=100,
        default=''
    )
    description = models.TextField(
        blank=True,
        default='',
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name
