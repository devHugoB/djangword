from django.contrib.auth.decorators import login_required
from app.models import SharedCredential
from django.shortcuts import render
from .update_item_view import decode_item


@login_required
def sharedItems(request):
    shared_items = SharedCredential.objects.filter(user_from=request.user)

    for item in shared_items:
        item.credential = decode_item(item.credential)
        print(item.credential.url)

    return render(
        request,
        "items/shared_items.html",
        context={"items": shared_items}
    )
