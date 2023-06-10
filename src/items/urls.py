from django.urls import path

from .views import createItem, listItems, updateItem, deleteItem, showPassword, shareItem, sharedItems

app_name = "items"

urlpatterns = [
    path("create_item/", createItem, name="create_item"),
    path("items_list/", listItems, name="items_list"),
    path("share_item/<int:item_id>", shareItem, name="share_item"),
    path("update_item/<int:item_id>", updateItem, name="update_item"),
    path("delete_item/<int:item_id>", deleteItem, name="delete_item"),
    path("show_password/<int:item_id>", showPassword, name="show_password"),
    path("shared_items", sharedItems, name="shared_items")
]
