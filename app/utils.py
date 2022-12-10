from .models import Card
from datetime import datetime, timedelta


def generat(series, cnt, days):
    cards = Card.objects.filter(series=series)
    number_busy = set()
    for card in cards:
        number_busy.add(card.number)
    number_i = 1
    for i in range(cnt):
        while number_i in number_busy:
            number_i += 1
        card = Card()
        card.series = series
        card.number = number_i
        card.start = datetime.now()
        card.end = datetime.now() + timedelta(days=days)
        card.save()
        number_i += 1