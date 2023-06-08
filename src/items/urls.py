from django.urls import path

from .views.create_item_view import createItem
from .views.items_list_view import listItems

urlpatterns = [
    path("create_item/", createItem, name="create_item"),
    path("items_list/", listItems, name="items_list")
]
