from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


# Create your models here.
class UserExtend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expire = models.DateTimeField(default=None, null=True, blank=True)


class TempGuest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expire = models.DateTimeField(default=None, null=True, blank=True)


class TestUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expire = models.DateTimeField(default=None, null=True, blank=True)


class VirtualKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fk_user')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fk_created_by')
    active_from = models.DateTimeField(default=None, null=True, blank=True)
    active_to = models.DateTimeField(default=None, null=True, blank=True)


# Super user - Full access (only dev)
# Staff - Residents
# Active - User can be used

# Maybe change_password = True by default
