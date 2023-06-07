from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Credential, History


@login_required
def history(request):
    user_credentials = Credential.objects.all().filter(user=request.user.id).order_by("-created_at")

    credentials_history = []
    for credential in user_credentials:
        credential_history = History.objects.get(credential=credential.id)
        credentials_history.append(credential_history)

    context = {"history": credentials_history}

    return render(
        request,
        "history/index.html",
        context=context
    )