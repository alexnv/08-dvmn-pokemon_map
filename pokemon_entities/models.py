from django.db import models  # noqa F401

# your models here
class Pokemon (models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='pokemons', null=True, blank=True)
    description = models.TextField(blank=True)
    title_en = models.TextField(blank=True)
    title_jp = models.TextField(blank=True)
    def __str__(self):
        return f'{self.title}'

    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        else:
            return None

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
