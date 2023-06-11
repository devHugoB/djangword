from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import base64

class Credential(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    url = models.URLField()
    deleted = models.BooleanField(default=False)
    security_index = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def validate_password(self, new_password):
        new_password = base64.b64encode(new_password.encode())
        new_password = new_password.decode()
        if self.password == new_password:
            raise ValidationError(
                "You can not use your old password !"
            )

    def can_read_password(self, user):
        if user.has_perm('app.view_credential_password') == True:
            return True
        else:
            return self.sharedcredential_set.filter(user_to=user).exists()
    