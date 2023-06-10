from django.contrib.auth.decorators import login_required
from app.models import Credential, SharedCredential
from django.shortcuts import render
from .update_item_view import decode_item
from django.http import JsonResponse
from datetime import datetime


@login_required
def listItems(request):
    user_credentials = Credential.objects.filter(user=request.user)
    user_shared_credentials = SharedCredential.objects.filter(
        user_to=request.user)

    for item in user_credentials:
        item = decode_item(item)

    for item in user_shared_credentials:
        item.credential = decode_item(item.credential)

    context = {"credentials": user_credentials,
               "shared_credentials": user_shared_credentials}

    print(f"[{datetime.now()}] [{request.user}] DEBUG - Affichage des items")

    return render(
        request,
        "items/items_list.html",
        context=context
    )


def showPassword(request, item_id):
    user_credential = Credential.objects.get(pk=item_id)
    user_credential = decode_item(user_credential)
    return JsonResponse({"item_password": user_credential.password})
