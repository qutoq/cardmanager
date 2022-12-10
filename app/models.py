from django.db import models


CHOICE = [('a', 'активирована'), ('n', 'не активирована'), ('p', 'просрочена')]


class Card(models.Model):
    series = models.CharField(max_length=25, null=False, verbose_name='Cерия')
    number = models.IntegerField(null=False, verbose_name='Номер')
    start = models.DateTimeField(null=False, verbose_name='Дата выпуска')
    end = models.DateTimeField(null=False, verbose_name='Дата окончания')
    status = models.CharField(max_length=1, default='n', choices=CHOICE, verbose_name='Статус')

    class Meta:
        unique_together = ('series', 'number')

    def __str__(self):
        return str(self.series) + str(self.number)


class Operation(models.Model):
    card = models.ForeignKey('card', related_name='purchases', on_delete=models.CASCADE, verbose_name='Карта')
    name = models.CharField(max_length=100, verbose_name='Описание')
    cost = models.FloatField(verbose_name='Сумма')
    date = models.DateTimeField(editable=True, verbose_name='Дата')

    class Meta:
        ordering = ['date']
