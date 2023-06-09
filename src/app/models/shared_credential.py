from django.db import models
from django.conf import settings
from .credential import Credential


class SharedCredential(models.Model):
    credential = models.ForeignKey(Credential, on_delete=models.CASCADE)
    user_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="shared_credentials"
    )
    user_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_credentials"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('credential', 'user_to'),)
