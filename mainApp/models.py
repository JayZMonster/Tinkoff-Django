from django.db import models

# Create your models here.


class Setting(models.Model):
    """
    General settings
    """
    id = models.AutoField(primary_key=True)
    api_key = models.CharField(max_length=255)
    fee = models.FloatField()

    class Meta:
        verbose_name_plural = 'Настройки'
        verbose_name = 'Настройка'


class Summary(models.Model):
    """
    Summary allover the deals
    """
    id = models.AutoField(primary_key=True)
    deals = models.IntegerField()
    profit = models.FloatField()
    fees = models.FloatField()

    class Meta:
        verbose_name_plural = 'Сводки'
        verbose_name = 'Сводка'


class Deal(models.Model):
    """
    Each deal(buy&sell)
    """
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    stock = models.CharField(max_length=255)
    start_volume = models.FloatField(verbose_name='Начальный объем')
    end_volume = models.FloatField(verbose_name='Конечный объем')
    fee = models.FloatField()
    profit = models.FloatField(null=True)

    class Meta:
        verbose_name_plural = 'Сделки'
        verbose_name = 'Сделка'





