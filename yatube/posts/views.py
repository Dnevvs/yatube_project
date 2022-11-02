from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    template = 'index.html'
    title = 'Главня страница'
    text = 'Это главная страница проекта Yatube',
    # Словарь с данными принято называть context
    context = {
        'title': title,
        'text': text
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


def group_list(request, template):
    template = 'posts/group_list.html'
    title = 'Группы'
    text = 'Здесь будет информация о группах проекта Yatube',
    # Словарь с данными принято называть context
    context = {
        'title': title,
        'text': text
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
