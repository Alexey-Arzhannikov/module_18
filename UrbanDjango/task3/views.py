from django.shortcuts import render

# Create your views here.
def platform(request):
    img_back = 'https://mollielpatterson.com/wp-content/uploads/2020/11/astro-00-1.jpg'
    context = {
        'i_back': img_back
    }
    return render(request, 'platform.html', context)

def games(request):
    img_RDR = 'https://g.foolcdn.com/editorial/images/515221/take-two-game-art-for-rdr-2.jpg'
    img_GoW = 'https://digiseller.mycdn.ink/preview/354824/p1_3542703_c0c39de8.jpeg'
    img_HZD = 'https://digiseller.mycdn.ink/preview/730077/p1_3266335_ed30dc7b.jpg'
    img_back = 'https://cdn.mos.cms.futurecdn.net/XhWVzWQqziAF2i9nGiZhTo-1200-80.jpg'

    point_RDR = 'Red Dead Redemption 2'
    point_GoW = 'God of War: Ragnarok'
    point_HZD = 'Horizon Zero Dawn'

    # link_RDR = 'https://steamcommunity.com/sharedfiles/filedetails/?id=2511120791&ysclid=m20fimh1jr646606560'
    # link_GoW = 'https://store.steampowered.com/app/2322010/God_of_War_Ragnark/'
    # link_HZD = 'https://store.steampowered.com/app/1151640/Horizon_Zero_Dawn_Complete_Edition/'
    main_page = 'http://127.0.0.1:8000/platform/'

    context = {
        'i_rdr': img_RDR,
        'i_gow': img_GoW,
        'i_hzd': img_HZD,
        'i_back': img_back,
        'p_rdr': point_RDR,
        'p_gow': point_GoW,
        'p_hzd': point_HZD,
        # 'l_gow': link_GoW,
        # 'l_rdr': link_RDR,
        # 'l_hzd': link_HZD,
        'mp': main_page,
    }
    return render(request, 'games.html', context)

def cart(request):
    main_page = 'http://127.0.0.1:8000/platform/'
    game_page = 'http://127.0.0.1:8000/platform/games/'
    link_img = 'https://overclockers.ru/st/legacy/blog/363664/119828_O.jpg'
    img_back = 'https://i.ytimg.com/vi/ibCLRoBTjn0/maxresdefault.jpg'

    context = {
        'mp': main_page,
        'gp': game_page,
        'l_img': link_img,
        'i_back': img_back
    }
    return render(request, 'cart.html', context)