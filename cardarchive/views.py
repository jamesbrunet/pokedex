from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from .savecards import insert_cards


def index(request):
    return render(request, "cardarchive/index.html")


def create_backup(request):
    cards = Card.where(set='Detective Pikachu')
    insert_cards(cards)
    context = {"cards": cards}
    return render(request, "cardarchive/backup.html", context)
