from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница Django')


def group_posts(request, slug):
    return HttpResponse(f'И зачем эта страница {slug}?')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
# def ice_cream_detail(request, pk):
#    return HttpResponse(f'Мороженое номер {pk}')
