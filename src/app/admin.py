from django.contrib import admin
from .models.credential import Credential
from .models.history import History
from .models.shared_credential import SharedCredential


class SharedCredentialAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "credential",
        "user_from",
        "user_to",
        "created_at",
    )

    readonly_fields = (
        "credential",
        "user_from",
        "user_to",
        "created_at",
    )


class CredentialAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "login",
        "password",
        "url",
        "deleted",
        "security_index",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "user",
        "login",
        "password",
        "url",
        "deleted",
        "security_index",
        "created_at",
    )


class HistoryAdmin(admin.ModelAdmin):
    list_display = (
        "credential",
        "login",
        "password",
        "url",
        "security_index",
        "created_at",
        "operation",
    )

    readonly_fields = (
        "credential",
        "login",
        "password",
        "url",
        "security_index",
        "created_at",
        "operation",
    )


# Register your models here.
admin.site.register(Credential, CredentialAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(SharedCredential, SharedCredentialAdmin)
