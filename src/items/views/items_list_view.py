from django.contrib.auth.decorators import login_required
from app.models import Credential
from django.shortcuts import render
from .update_item_view import decode_item
import base64


@login_required
def listItems(request):
    user_credentials = Credential.objects.filter(user=request.user)
    for item in user_credentials:
        item = decode_item(item)
    context = {"items": user_credentials}

    return render(
        request,
        "items/items_list.html",
        context=context
    )
