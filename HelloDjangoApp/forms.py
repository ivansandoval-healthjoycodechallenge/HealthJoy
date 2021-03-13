from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class GitHubCreds(forms.Form):

   token = forms.CharField(label=_("Git Hub Personal Access Token"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control pb-3',
                                   'placeholder':'Enter Personal Access Token'}))

   def clean(self):
        cleaned_data = super(GitHubCreds, self).clean()       
        token = cleaned_data.get('token')      
   