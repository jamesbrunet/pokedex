from .models import PokemonCard


def insert_cards(cards):
    cards_to_save = []
    for card in cards:
        cards_to_save.append(
            PokemonCard(
                id=card.id,
                name=card.name
            )
        )

    PokemonCard.objects.bulk_create(cards_to_save)


def purge_cards():
    # We use list() to force evaluation before we delete the cards
    cards = list(PokemonCard.objects.all())
    PokemonCard.objects.all().delete()
    return cards
