from django.shortcuts import render
from django.http import HttpResponse
import a2s


def index(request):
    address = ("188.127.241.8", 27173)
    player_list = a2s.players(address)
    server_info = a2s.info(address)
    map = server_info.map_name
    online = server_info.player_count
    cap = server_info.max_players

    context = {'map': map, 'online': online, 'cap': cap}
    return render(request, 'core/index.html', context)