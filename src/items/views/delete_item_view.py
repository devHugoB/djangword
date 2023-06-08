from django.shortcuts import render
from ..forms import DeleteItemForm
from app.models import Credential
from django.http import HttpResponseRedirect

def deleteItem(request, item_id):

    item = Credential.objects.get(id=item_id)

    if request.method == 'POST':
        form = DeleteItemForm(request.POST, credential=item)
        if form.is_valid():
            print("valisé")
            form.delete_credential()
            return HttpResponseRedirect(f"/items/items_list/")
    else:
        form = DeleteItemForm(credential=item)

    return render(
        request,
        "items/delete_item.html", {'form': form}
    )