from django.db import models
from django.contrib.auth.models import User


class Notice(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
