from django.shortcuts import render, get_object_or_404
from ..forms.create_item_form import CreateItemForm
from app.models.credential import Credential
from app.models.history import History
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .create_item_view import test_password_strength
from django.http import HttpResponseRedirect
import base64

@login_required
@require_http_methods(["GET", "POST"])
def updateItem(request, item_id):
    item = get_object_or_404(Credential, pk=item_id)
    if request.method == 'POST':
        form = CreateItemForm(request.POST, instance=item)
        print("ici")
        if form.is_valid():
            print(form)
            item.security_index = test_password_strength(
                form.cleaned_data["password"])
            item.login = base64.b64encode(
                form.cleaned_data["login"].encode())
            item.login = item.login.decode()
            item.password = base64.b64encode(
                form.cleaned_data["password"].encode())
            item.password = item.password.decode()
            item.url = base64.b64encode(
                form.cleaned_data["url"].encode())
            item.url = item.url.decode()
            item.save()

            history = {"credential": item,
                       "login": item.login,
                       "password": item.password,
                       "url": item.url,
                       "security_index": item.security_index,
                       "operation": "UPDATE"}
            hist_inst = History.objects.create(**history)
            hist_inst.save()
            return HttpResponseRedirect(f"/items/items_list/")
    else:
        item = decode_item(item)
        form = CreateItemForm(instance=item)

    return render(
        request,
        "items/update_item.html",
        context={"form": form}
    )

def decode_item(item):
    item.login = base64.b64decode(item.login).decode()
    item.password = base64.b64decode(item.password).decode()
    item.url = base64.b64decode(item.url).decode()
    return item