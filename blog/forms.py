from django import forms
from google.appengine.ext import db

from models import Article

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
    is_published = forms.BooleanField(required=False)
    
    def is_valid(self, edit=False):
        valid = super(ArticleForm, self).is_valid()
        if not valid:
            return valid
        if not edit and db.Query(Article).filter("title =", self.cleaned_data['title']).get():
        
            self.errors['title'] = 'Article with this title exist'
            print self.errors
            return False
        return True
