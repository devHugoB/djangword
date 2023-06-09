from ..forms.share_item_form import ShareItemForm
from app.models import Credential, SharedCredential
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
import base64


@login_required
@require_http_methods(["GET", "POST"])
def shareItem(request, item_id):
    item = Credential.objects.get(pk=item_id)
    error = ""

    item.login = base64.b64decode(item.login.encode()).decode()
    item.url = base64.b64decode(item.url.encode()).decode()

    if request.method == 'POST':
        form = ShareItemForm(request.POST)
        if form.is_valid():
            try:
                user_to = User.objects.get(
                    username=form.cleaned_data["username"])

                shared_item = {
                    "credential": item,
                    "user_from": request.user,
                    "user_to": user_to,
                }

                shared_item = SharedCredential.objects.create(**shared_item)
                shared_item.save()

            except User.DoesNotExist:
                error = "L'utilisateur n'existe pas"
                print(f"ERROR: {error}")

            except Exception:
                error = "Mot de passe déjà partagé à cet utilisateur"
                print(f"ERROR: {error}")

            else:
                return HttpResponseRedirect("/items/items_list/")
    else:
        form = ShareItemForm()

    return render(
        request,
        "items/share_item.html",
        context={"form": form, "item": item, "error": error}
    )
