from django.urls import path

from .views import createItem, listItems, updateItem, deleteItem

app_name = "items"

urlpatterns = [
    path("create_item/", createItem, name="create_item"),
    path("items_list/", listItems, name="items_list"),
    path("update_item/<int:item_id>", updateItem, name="update_item"),
    path("delete_item/<int:item_id>", deleteItem, name="delete_item")
]
