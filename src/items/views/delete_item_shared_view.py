from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from app.models import SharedCredential

@login_required
def delete_item_shared(request, shared_item_id):
    shared_item = get_object_or_404(SharedCredential, pk=shared_item_id)

    # Vérifiez que l'utilisateur actuel est bien l'utilisateur qui a partagé l'élément
    if shared_item.user_from == request.user:
        shared_item.delete()  # Supprime l'élément partagé

    return redirect(f'/items/shared_items')
