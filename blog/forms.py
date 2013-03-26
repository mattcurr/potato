from django import forms
from models import Article

class ArticleForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    is_published = forms.BooleanField(required=False)
    
