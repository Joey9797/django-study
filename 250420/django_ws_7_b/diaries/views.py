from django.shortcuts import render, redirect
from .models import Diary, Comment
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    context = {
        'diaries': diaries,
    }
    return render(request, 'diaries/index.html', context)


def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)


def detail(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    comment_form = CommentForm()
    context = {
        'diary': diary,
        'comment_form': comment_form,
    }
    return render(request, 'diaries:index', context)


def comments_create(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.diary = diary
        comment.save()
        return redirect('diaries:detail', diary.pk)
    context = {
        'form': form,
    }
    return render(request, 'diaries/detail.html', context)


def comments_delete(request, diary_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return render(request, 'diaries:detail', diary_pk)
