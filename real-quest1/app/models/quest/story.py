from __future__ import unicode_literals
from typing import Union

from django.db import models
from django.conf import settings 
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail, BadHeaderError

from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import EmailField

from .quest import Quest

class Story(models.Model):

    """ """

    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name="story")

    title = models.CharField(max_length=50)
    synopsis = models.TextField()


class StoryAct(models.Model):

    """ """

    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="acts")
    
    sequence = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    synopsis = models.TextField()


class StoryPassage(models.Model):

    """ """

    act = models.ForeignKey(StoryAct, on_delete=models.CASCADE, related_name="passages")

    title = models.CharField(max_length=30)
    passage = models.TextField()