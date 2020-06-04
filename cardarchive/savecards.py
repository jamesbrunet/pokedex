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