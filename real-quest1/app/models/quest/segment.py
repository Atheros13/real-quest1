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
from django.db.models.fields.related import ForeignKey

from .location import Location
from .quest import Quest
from .story import StoryPassage

class Segment(models.Model):

    """ """

    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name="segments")

    previous_segment = models.ForeignKey("self", on_delete=models.CASCADE, related_name="next_segment")
    # <<< next_segment

    location_start = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL, related_name="segment_starts")
    location_others = models.ManyToManyField(Location, related_name="segment_others")
    location_finish = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL, related_name="segment_finishes")

    story_passage = models.OneToOneField(StoryPassage, null=True, on_delete=models.SET_NULL, related_name="segment")

    clue = models.TextField()    
    solution = models.TextField()
    # <<< hints 
    answer = models.CharField(max_length=20)

    ## META

    def __str__(self):

        pass

    ## FUNCTIONS

    def filter_answers(self, answer):

        """This filters answers so that spelling and close enough answers are
        accepted. This may require further class attributes in order 
        to work correctly."""

        pass
