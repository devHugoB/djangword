from django.urls import path

from .views import history

app_name = "history"

urlpatterns = [
    path("", history, name="history")
]
