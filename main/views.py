from django.shortcuts import render


def index(request):
    data = {'title': 'Главная страница',
            'values': ['some', 'hello', 'hii'],
            'obj': {
                'car': 'bmw',
                'age': 12,
                'hobby': 'foll'
            }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')