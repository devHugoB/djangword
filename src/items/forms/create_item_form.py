from django import forms
from app.models.credential import Credential


class CreateItemForm(forms.ModelForm):
    url = forms.URLField(label='URL')
    login = forms.CharField(label="Login", max_length=255)
    password = forms.CharField(label="Password", max_length=255, widget=forms.PasswordInput(render_value=True))

    def clean_password(self):
        new_password = self.cleaned_data.get('password')
        instance = self.instance

        if instance:
            instance.validate_password(new_password)

        return new_password

    class Meta:
        model = Credential
        fields = ['url', 'login', 'password']
