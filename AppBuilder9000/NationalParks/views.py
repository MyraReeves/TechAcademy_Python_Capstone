from django.shortcuts import render, get_object_or_404, redirect
from .models import VisitorComment
from .forms import CommentForm


def states(request):
    return render(request, 'National_Parks.html')


def comments(request):
    comments_data = VisitorComment.object.all()
    return render(request, 'park_comments.html', {'comments': comments_data})


def create_comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('comments')
    else:
        print(form.errors)
        form = CommentForm()
        context = {'form': form, }
        return render(request, 'park_comment_NEW.html', context)
