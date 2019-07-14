from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse

from garden.models import Vegetable

name = 'ウメ'
sub_titles = ['美味しいよ！', 'お買い得！', '産地直送！', 'とれたてをお届け！']


def index(request):
    """メイン画面."""
    title = name + 'の野菜販売'
    vegetables = Vegetable.objects.all()
    return TemplateResponse(request, 'garden/index.html',
                            {'title': title,
                             'vegetables': vegetables})
