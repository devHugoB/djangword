from django import forms

class DeleteItemForm(forms.Form):
    confirm_deletion = forms.BooleanField(label="Confirmer la suppression ? :", required=True, initial=False)

    def __init__(self, *args, **kwargs):
        self.credential = kwargs.pop('credential')
        super().__init__(*args, **kwargs)

    def clean_confirm_deletion(self):
        confirm_deletion = self.cleaned_data.get('confirm_deletion')
        if not confirm_deletion:
            raise forms.ValidationError("Vous devez confirmer la suppression.")
        return confirm_deletion

    def delete_credential(self):
        self.credential.delete()