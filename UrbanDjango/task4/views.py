from django.shortcuts import render

# Create your views here.
def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'platform.html', context)

def games(request):
    title = 'Игры'
    games = ['Red Dead Redemption 2', 'God of War: Ragnarok', 'Horizon Zero Dawn']
    main_page = 'http://127.0.0.1:8000/platform/'

    context = {
        'games': games,
        'mp': main_page,
        'title': title
    }
    return render(request, 'games.html', context)

def cart(request):
    title = 'Корзина'
    main_page = 'http://127.0.0.1:8000/platform/'
    game_page = 'http://127.0.0.1:8000/platform/games/'

    context = {
        'mp': main_page,
        'gp': game_page,
        'title': title
    }
    return render(request, 'cart.html', context)

