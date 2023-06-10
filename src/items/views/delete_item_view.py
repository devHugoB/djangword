from django.shortcuts import render
from ..forms import DeleteItemForm
from app.models import Credential
from django.http import HttpResponseRedirect
from datetime import datetime


def deleteItem(request, item_id):

    item = Credential.objects.get(id=item_id)

    if request.method == 'POST':
        form = DeleteItemForm(request.POST, credential=item)
        if form.is_valid():
            form.delete_credential()
            print(
                f"[{datetime.now()}] [{request.user}] DEBUG - Suppression d'un item")
            return HttpResponseRedirect("/items/items_list/")
    else:
        print(
            f"[{datetime.now()}] [{request.user}] DEBUG - Affichage de la page de suppression d'item")
        form = DeleteItemForm(credential=item)

    return render(
        request,
        "items/delete_item.html", {'form': form}
    )
