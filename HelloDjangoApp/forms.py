from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class GitHubCreds(forms.Form):
   username = forms.CharField(max_length=254,label=_("Git Hub Username"),
                               widget=forms.TextInput({
                                   'class': 'form-control pb-3',
                                   'placeholder': 'Enter Username'}))
   password = forms.CharField(label=_("Git Hub Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control pb-3',
                                   'placeholder':'Enter Password'}))

   def clean(self):
        cleaned_data = super(GitHubCreds, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')      
        if not username and not password:
            raise forms.ValidationError('You have to write something!')