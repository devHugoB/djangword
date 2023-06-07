from django.urls import path

from .views.create_item_view import createItem

urlpatterns = [
    path("create_item/", createItem, name="create_item")
]