from django.urls import path

from .views.create_item_view import createItem
from .views.show_item_view import showItem

urlpatterns = [
    path("create_item/", createItem, name="create_item"),
    path("show_item/", showItem, name="show_item")
]