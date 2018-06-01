from django.db import models



class CountryManager(models.query.QuerySet):
    def with_num_cities(self):
        return self.annotate(num_cities=models.Count('cities'))
    def with_biggest_city_size(self):
        return self.annotate(biggest_city_size=models.Max('cities__area'))


class CityManager(models.query.QuerySet):
    def with_dencity(self):
        return self.annotate(dencity=models.F('population')/models.F('area'))


class Country(models.Model):
    name = models.CharField(
        'Название',
        max_length=255
    )
    objects = CountryManager.as_manager()

class City(models.Model):
    country = models.ForeignKey(
        Country,
        verbose_name='Страна',
        related_name='cities',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Название',
        max_length=255
    )
    population = models.FloatField(
        'Население'
    )
    area = models.FloatField(
        'Площадь'
    )
    objects = CityManager.as_manager()
