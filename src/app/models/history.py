from django.db import models
from .credential import Credential


class History(models.Model):
    OPERATIONS = [
        ("DELETE", "DELETE"),
        ("UPDATE", "UPDATE"),
        ("CREATE", "CREATE")
    ]
    credential = models.ForeignKey(Credential, on_delete=models.CASCADE)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    security_index = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    operation = models.CharField(max_length=6, choices=OPERATIONS)
    