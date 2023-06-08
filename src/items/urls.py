from django.urls import path

from .views.create_item_view import createItem
from .views.items_list_view import listItems
from .views.update_item_view import updateItem

app_name = "items"

urlpatterns = [
    path("create_item/", createItem, name="create_item"),
    path("items_list/", listItems, name="items_list"),
    path("update_item/<int:item_id>", updateItem, name="update_item")
]
