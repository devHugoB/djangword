from django import forms


class ChangeUsernameForm(forms.Form):
    username = forms.CharField(label="Username", max_length=255)
