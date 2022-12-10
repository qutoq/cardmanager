from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import *
from .forms import *
from .utils import generat


def main_view(request, search=None):
    if search is None:
        search = []
    cards = Card.objects.all().order_by('series', 'number')
    for card in cards.order_by('end'):
        if card.end <= timezone.now():
            card.status = 'p'
            card.save()
            continue
        break
    if search != []:
        series, number, status = search
        if series != '':
            cards = cards.filter(series=series)
        if number != '':
            cards = cards.filter(number=number)
        if status != '-':
            cards = cards.filter(status=status)
        cnt = len(cards)
        return render(request, 'app/main.html', {'cards': cards, "cnt": cnt, "text": "Результаты поиска"})
    else:
        cnt = len(cards)
        return render(request, 'app/main.html', {'cards': cards, "cnt": cnt, "text": "Список карт"})


def card_view(request, id):
    card = get_object_or_404(Card, id=id)
    operations = Operation.objects.filter(card=card)
    if card.end <= timezone.now():
        card.status = 'p'
        card.save()
    return render(request, 'app/card.html', {'card': card, "operations": operations})


def status_change(request, id):
    card = get_object_or_404(Card, id=id)
    if card.status == 'n':
        card.status = 'a'
    elif card.status == 'a':
        card.status = 'n'
    card.save()
    return redirect('/card/' + str(id))


def delete_view(request, id):
    card = Card.objects.get(id=id)
    operations = Operation.objects.filter(card=card)
    for operation in operations:
        operation.delete()
    card.delete()
    return redirect('app:main')


def search_view(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            series = request.POST.get('series')
            number = request.POST.get('number')
            status = request.POST.get('status')
            return main_view(request, [series, number, status])
    form = SearchForm()
    return render(request, 'app/search.html', {'form': form})


def generate_view(request):
    if request.method == "POST":
        form = GenerateForm(request.POST)
        if form.is_valid():
            series = request.POST.get('series')
            cnt = request.POST.get('cnt')
            time = request.POST.get('time')
            generat(series, int(cnt), int(time))
            return redirect('app:main')
    form = GenerateForm()
    return render(request, 'app/generate.html', {"form": form})
