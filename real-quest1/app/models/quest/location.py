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


class Location(models.Model):

    """ """

    gps_long = models.DecimalField(max_digits=9, decimal_places=6)
    gps_lat = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.TextField(null=True, blank=True)
    building = models.CharField(max_length=30, null=True, blank=True)
    floor = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    ##



    ## FUNCTIONS 

    def gps(self):

        """Returns a GPS location."""

        pass