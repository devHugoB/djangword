from django.contrib.auth.decorators import login_required
from app.models import Credential
from django.shortcuts import render
import base64


@login_required
def listItems(request):
    user_credentials = Credential.objects.filter(user=request.user)
    for item in user_credentials:
        item.login = base64.b64decode(item.login).decode()
        item.password = base64.b64decode(item.password).decode()
        item.url = base64.b64decode(item.url).decode()
    context = {"items": user_credentials}

    return render(
        request,
        "items/items_list.html",
        context=context
    )
