from django.db import models  # noqa F401

# your models here
class Pokemon (models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='pokemons', blank=True)
    def __str__(self):
        return f'{self.title}'

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()
