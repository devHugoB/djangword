from django import forms


class ShareItemForm(forms.Form):
    username = forms.CharField(
        label="Partager à l'utilisateur", max_length=255)
