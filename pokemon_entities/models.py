from django.db import models  # noqa F401

# your models here
class Pokemon (models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='pokemons', blank=True)
    def __str__(self):
        return f'{self.title}'

class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()