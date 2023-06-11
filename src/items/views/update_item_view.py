from django.shortcuts import render, get_object_or_404
from ..forms.create_item_form import CreateItemForm
from app.models import Credential, History
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .create_item_view import test_password_strength
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse
import base64


@login_required
@require_http_methods(["GET", "POST"])
def updateItem(request, item_id):
    item = get_object_or_404(Credential, pk=item_id)
    if not item.can_read_password(request.user):
        return JsonResponse({"error": "You can not access to this password"}, status=403)
    
    if request.method == 'POST':
        form = CreateItemForm(request.POST, instance=item)
        if form.is_valid():
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
            print(
                f"[{datetime.now()}] [{request.user}] DEBUG - Modification d'un item")
            return HttpResponseRedirect("/items/items_list/")
    else:
        print(
            f"[{datetime.now()}] [{request.user}] DEBUG - Affichage de la page de modification d'item")
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
