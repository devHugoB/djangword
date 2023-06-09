from django.urls import path

from .views import history, showPassword

app_name = "history"

urlpatterns = [
    path("", history, name="history"),
    path("show_password/<int:item_id>", showPassword, name="show_password")
]
