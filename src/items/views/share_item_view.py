from ..forms.share_item_form import ShareItemForm
from app.models import Credential, SharedCredential
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
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

                if user_to.id == request.user.id:
                    raise PermissionDenied

                shared_item = {
                    "credential": item,
                    "user_from": request.user,
                    "user_to": user_to,
                }

                shared_item = SharedCredential.objects.create(**shared_item)
                shared_item.save()

            except PermissionDenied:
                error = "Vous ne pouvez pas partager un item à vous même"
                print(f"[{datetime.now()}] [{request.user}] ERROR - {error}")

            except User.DoesNotExist:
                error = "L'utilisateur n'existe pas"
                print(f"[{datetime.now()}] [{request.user}] ERROR - {error}")

            except Exception:
                error = "Mot de passe déjà partagé à cet utilisateur"
                print(f"[{datetime.now()}] [{request.user}] ERROR - {error}")

            else:
                print(
                    f"[{datetime.now()}] [{request.user}] DEBUG - Partage d'un mot de passe de l'utilisateur {request.user.username} à {user_to.username}")
                return HttpResponseRedirect("/items/items_list/")
    else:
        print(
            f"[{datetime.now()}] [{request.user}] DEBUG - Affichage de la page de partage de mot de passe")
        form = ShareItemForm()

    return render(
        request,
        "items/share_item.html",
        context={"form": form, "item": item, "error": error}
    )
