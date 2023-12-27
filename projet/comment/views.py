from django.shortcuts import render
from .models import Comment
from .forms import CommentForm 
from django.contrib import messages
from django.shortcuts import redirect

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            date = form.cleaned_data['date']
            author = form.cleaned_data['author']
            article = form.cleaned_data['article']

            comment = Comment(content=content, author=author, date=date, article=article)
            comment.save()
    else:
        form = CommentForm()

    return render(request, 'comment/application.html', {'form': form})



def clear_comments(request):
    if Comment.objects.count() != 0:
        try:
            deleted_count, _ = Comment.objects.all().delete()
            print("Deleted count:", deleted_count)
            deleted_count = int(deleted_count)
            messages.success(request, f'Tous les commentaires ont été supprimés avec succès. Nombre de commentaires supprimés : {deleted_count}')
        except Exception as e:
            print(f"Error: {str(e)}")
            messages.error(request, 'Une erreur s\'est produite lors de la suppression des commentaires.')
    return redirect('list_article')