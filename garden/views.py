from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse

from garden.forms import CommentForm
from garden.models import Vegetable, Comment

name = 'ウメ'
sub_titles = ['美味しいよ！', 'お買い得！', '産地直送！', 'とれたてをお届け！']


def index(request):
    """メイン画面."""
    if request.method == 'POST':
        form = CommentForm(request.POST)  # request.POSTの戻り値は django.http.request.QueryDict型だが、普通のdictと似たようなもんらしい
        print(type(request.POST))
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()

    title = name + 'の野菜販売'
    vegetables = Vegetable.objects.all()

    comments = Comment.objects.order_by('-created_at')[:3]
    return TemplateResponse(request, 'garden/index.html',
                            {'title': title,
                             'vegetables': vegetables,
                             'form': form,
                             'comments': comments})
