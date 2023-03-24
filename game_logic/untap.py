def untap(card):
    # untaps a card
    if card.tapped:
        card.tapped = False
        print(f"{card.name} untapped.")
        