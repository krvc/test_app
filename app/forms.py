from django import forms


class ClientForm(forms.Form):
    client_id = forms.CharField(max_length=124)
    client_secret = forms.CharField(max_length=124)


class ResumeUploadForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    projects_url = forms.URLField()
    code_url = forms.URLField()
    resume = forms.FileField()
