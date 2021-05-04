from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from .cardtoolkit import insert_cards, purge_cards
from .models import PokemonCard

def index(request):
    return render(request, "cardarchive/index.html")


def create_backup(request):
    overlap, new_cards = insert_cards(set_name='detective.pikachu')
    context = {"overlap": overlap,"cards": new_cards}
    return render(request, "cardarchive/backup.html", context)


def purge(request):
    purged = purge_cards()
    context = {"cards": purged}
    return render(request, "cardarchive/purge.html", context)

def search(request):
    search_method = request.POST.get('searchby')
    search_text = request.POST.get('searchterm')
    if search_method == 'name':
        matches = PokemonCard.objects.filter(name__icontains=search_text).all()
    else:
        return HttpResponseBadRequest('{} not a valid search method'.format(search_method))

    context = {"search_method":search_method, "search_text":search_text, "matches":matches}
    return render(request, "cardarchive/searchresult.html", context)

