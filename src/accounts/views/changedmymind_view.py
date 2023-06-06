from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from accounts.forms import ChangeUsernameForm


@login_required
@require_http_methods(["GET", "POST"])
def changeUsername(request):
    if request.method == "POST":
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            user = request.user
            user.username = form.cleaned_data["username"]
            user.save()

            return HttpResponseRedirect("/")
    else:
        form = ChangeUsernameForm()

    return render(
            request,
            "registration/changedmymind.html",
            context={"form": form}
    )
