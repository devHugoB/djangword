from django.urls import path

from .views import RegisterView, changeUsername

app_name = 'accounts'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("changedmymind/", changeUsername, name="changedmymind")
]
