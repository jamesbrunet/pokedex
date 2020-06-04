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

    # We don't want to backup if we already have any of these cards stored
    saved_card_ids = PokemonCard.objects.all().values_list('id', flat=True)
    cards_to_save_ids = [card.id for card in cards]
    overlap = [value for value in saved_card_ids if value in cards_to_save_ids]
    print(overlap)

    if overlap:
        return True
    else:
        PokemonCard.objects.bulk_create(cards_to_save)
        return False


def purge_cards():
    # We use list() to force evaluation before we delete the cards
    cards = list(PokemonCard.objects.all())
    PokemonCard.objects.all().delete()
    return cards
