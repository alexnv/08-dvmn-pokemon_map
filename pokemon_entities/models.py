from django.db import models  # noqa F401


# your models here
class Pokemon(models.Model):
    """Модель покемона"""
    title = models.CharField ('Название (ru)', max_length=200)
    photo = models.ImageField('Изображение', upload_to='pokemons', null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    title_en = models.CharField ('Название (en)', null=True, blank=True, max_length=200)
    title_jp = models.CharField ('Название (jp)', null=True, blank=True, max_length=200)
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Из кого эволюционировал',
        related_name='next_evolutions',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )


    def __str__(self):
        return self.title

    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        else:
            return None


class PokemonEntity(models.Model):
    """Появление покемона на карте"""
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE, null=True, )
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Появляется', null=True)
    disappeared_at = models.DateTimeField('Исчезает', null=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    attack = models.IntegerField('Атака', null=True, blank=True)
    protection = models.IntegerField('Защита', null=True, blank=True)
    endurance = models.IntegerField('Выносливость', null=True, blank=True)

    def __str__(self):
        return f'{self.pokemon.title} lvl {self.level} at {self.lat}:{self.lon}'