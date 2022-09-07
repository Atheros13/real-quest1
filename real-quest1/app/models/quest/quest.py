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

class Quest(models.Model):

    """ """

    name = models.CharField(max_length=50)