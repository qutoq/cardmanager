from django import forms

CHOICE_BLANK = [('-', '---------'), ('a', 'активирована'), ('n', 'не активирована'), ('p', 'просрочена')]
TIME = [('31', '1 месяц'), ('183', '6 месяцев'), ('365', '1 год')]


class GenerateForm(forms.Form):
    series = forms.CharField(max_length=25, label='Серия')
    cnt = forms.IntegerField(min_value=1, label='Количество')
    time = forms.ChoiceField(choices=TIME, label='Срок действия')


class SearchForm(forms.Form):
    series = forms.CharField(max_length=25, label='Серия', required=False)
    number = forms.IntegerField(label='Номер', required=False)
    status = forms.ChoiceField(choices=CHOICE_BLANK, label='Статус', required=False)

