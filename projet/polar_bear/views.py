from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.forms import Form, CharField

from .models import Article
from comment.models import Comment

class search_article(Form):
    search = CharField(max_length=100, required=False)

def list_article(request):
    articles = Article.objects.all()

    if request.method == 'POST':
        form = search_article(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            articles = Article.objects.filter(title__contains=search)
    else:
        form = search_article()
        tile_form = request.GET.get('title', '')
        if tile_form != '':
            articles = Article.objects.filter(title__contains=tile_form)
            form.fields['title'].initial = tile_form

    return render(request, 'polar_bear/list_articles.html', {'search_form': form, 'articles': articles, 'title': 'Liste des articles'})


def article(request, id):
    article = get_object_or_404(Article, id=id)
    comment = Comment.objects.filter(article=article)
    return render(request, 'polar_bear/article.html', {'article': article, 'comment': comment})
