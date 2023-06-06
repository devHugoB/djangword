from django.db import models
from django.conf import settings


class Credential(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    deleted = models.BooleanField()
    security_index = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
