from django.shortcuts import render
from ..forms.create_item_form import CreateItemForm
from app.models.credential import Credential
from app.models.history import History
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from string import punctuation
from datetime import datetime
import base64


@login_required
@require_http_methods(["GET", "POST"])
def createItem(request):
    if request.method == "POST":
        form = CreateItemForm(request.POST)
        if form.is_valid():
            form.cleaned_data["user_id"] = request.user.id
            form.cleaned_data["security_index"] = test_password_strength(
                form.cleaned_data["password"])

            form.cleaned_data["login"] = base64.b64encode(
                form.cleaned_data["login"].encode())
            form.cleaned_data["login"] = form.cleaned_data["login"].decode()
            form.cleaned_data["password"] = base64.b64encode(
                form.cleaned_data["password"].encode())
            form.cleaned_data["password"] = form.cleaned_data["password"].decode()
            form.cleaned_data["url"] = base64.b64encode(
                form.cleaned_data["url"].encode())
            form.cleaned_data["url"] = form.cleaned_data["url"].decode()

            credential_inst = Credential.objects.create(**form.cleaned_data)
            credential_inst.save()

            history = {"credential": credential_inst,
                       "login": credential_inst.login,
                       "password": credential_inst.password,
                       "url": credential_inst.url,
                       "security_index": credential_inst.security_index,
                       "operation": "CREATE"}
            hist_inst = History.objects.create(**history)
            hist_inst.save()

            print(f"[{datetime.now()}] [{request.user}] DEBUG - Création d'un item")

            return HttpResponseRedirect("/items/create_item")
    else:
        print(
            f"[{datetime.now()}] [{request.user}] DEBUG - Affichage de la page de création d'item")
        form = CreateItemForm()

    return render(
        request,
        "items/create_item.html",
        context={"form": form}
    )


def test_password_strength(password: str) -> int:
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in punctuation for c in password)

    number_different_characters = sum(
        (has_upper, has_lower, has_digit, has_special))
    score = min(number_different_characters * 2, 5)

    if len(password) < 10:
        return 1

    if len(password) <= 13:
        return max(score - 1, 2)

    if len(password) <= 15:
        return score

    if len(password) <= 17:
        return min(score + 1, 5)

    return 5
