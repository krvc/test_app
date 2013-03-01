from django import forms


class ClientForm(forms.Form):
    client_id = forms.CharField(max_length=124)
    client_secret = forms.CharField(max_length=124)
