from django.contrib import admin
from .models.credential import Credential
from .models.history import History

class CredentialAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "login",
        "password",
        "url",
        "deleted",
        "security_index",
        "created_at",
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