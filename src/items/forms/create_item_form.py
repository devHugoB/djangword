from django import forms


class CreateItemForm(forms.Form):
    url = forms.CharField(label="URL", max_length=255)
    login = forms.CharField(label="Login", max_length=255)
    password = forms.CharField(label="Password", max_length=255)
