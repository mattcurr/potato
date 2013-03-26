from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.template.context import RequestContext
from google.appengine.ext import db
from google.appengine.api import users

from models import Article
from forms import ArticleForm


def home(request):
    articles = db.Query(Article)
    if not users.is_current_user_admin():
        articles = articles.filter('is_published =', True)
        
    context = RequestContext(request)
    context['articles'] = articles.order('-created_at')
    return render_to_response("home.html", context)

def article(request, slug):
    context = RequestContext(request)
    article = db.Query(Article).filter("slug =", slug).get()
    if not article:
        raise Http404()
    context['article'] = article

    return render_to_response("article.html", context)

def article_edit(request, slug):
    context = RequestContext(request)
    article = db.Query(Article).filter("slug =", slug).get()
    if not article:
        raise Http404()
        
    if request.method == 'POST':
        if 'delete' in request.POST:
            article.delete()
            return redirect('/')
        else:
            article_form = ArticleForm(request.POST)
            if article_form.is_valid(edit=True):
                article.title = article_form.cleaned_data['title']
                article.body = article_form.cleaned_data['body']
                article.is_published = article_form.cleaned_data['is_published']
                article.save()
                return redirect(article.get_absolute_url())
    else:
        article_form = ArticleForm({'title':article.title, 'body': article.body,  \
                                    'is_published': article.is_published})
    context['form'] = article_form
    context['article'] = article
    return render_to_response("submit.html", context)
    
def submit(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)

        if article_form.is_valid():
            title = article_form.cleaned_data['title']
            body = article_form.cleaned_data['body']
            is_published = article_form.cleaned_data['is_published']
            
            article = Article(title=title, body=body, is_published=is_published)
            article.put()
            return redirect('/')
    else:
        article_form = ArticleForm()
    
    context['form'] = article_form 
    
    return render_to_response("submit.html", context)

