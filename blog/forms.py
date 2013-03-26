from django import forms
from google.appengine.ext import db

from models import Article

class ArticleForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(label="", help_text="", widget=forms.Textarea)
    is_published = forms.BooleanField(required=False)
    
    def is_valid(self, edit=False):
        valid = super(ArticleForm, self).is_valid()
        if not valid:
            return valid
            
        if not edit and db.Query(Article).filter("title =", self.cleaned_data['title']).get():
            self._errors['title'] = 'Article with this title exist'
            return False
        return True
