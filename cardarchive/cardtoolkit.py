from .models import PokemonCard, PokemonCardSet
from pokemontcgsdk import Card
from pokemontcgsdk import Set

def insert_cards(set_name):
    cards = Card.where(q='set.name:{}'.format(set_name))
    sets = Set.all()

    sets_to_save = []
    for set in sets:
        sets_to_save.append(
            PokemonCardSet(
                id=set.id,
                name=set.name
            )
        )

    overlap, inserted = _dedupe_and_insert(PokemonCardSet, sets_to_save)

    cards_to_save = []
    for card in cards:
        cards_to_save.append(
            PokemonCard(
                id=card.id,
                name=card.name,
                set=PokemonCardSet.objects.get(id=card.set.id)
            )
        )


    overlap, inserted = _dedupe_and_insert(PokemonCard, cards_to_save)

    return overlap, inserted


def _dedupe_and_insert(model, items_to_insert):
    # We don't want to backup if we have the card already stored
    saved_item_ids = model.objects.all().values_list('id', flat=True)

    overlap = [item for item in items_to_insert if item.id in saved_item_ids]
    items_to_insert = [item for item in items_to_insert if item.id not in saved_item_ids]

    print(items_to_insert)
    print(overlap)

    if items_to_insert:
        model.objects.bulk_create(items_to_insert)

    return overlap, items_to_insert

def purge_cards():
    # We use list() to force evaluation before we delete the cards
    cards = list(PokemonCard.objects.all())
    PokemonCard.objects.all().delete()
    return cards
