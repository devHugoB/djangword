from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Credential, History
from items.views.update_item_view import decode_item
from django.http import JsonResponse


@login_required
def history(request):
    user = request.user
    histories = History.objects.filter(credential__user=user)

    for item in histories:
        item = decode_item(item)
        
    context = {"history": histories}

    return render(
        request,
        "history/index.html",
        context=context
    )

def showPassword(request, item_id):
    user_credential = Credential.objects.get(pk=item_id)
    user_credential = decode_item(user_credential)
    return JsonResponse({"item_password": user_credential.password})