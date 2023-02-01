import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_entities = PokemonEntity.objects.filter(disappeared_at__gte=localtime(), appeared_at__lte=localtime())
    for pokemon_entity in pokemons_entities:
        add_pokemon(
                    folium_map, pokemon_entity.lat,
                    pokemon_entity.lon,
                    request.build_absolute_uri(pokemon_entity.pokemon.get_photo_url())
                )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append(make_pokemon_data(pokemon, request))

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemons_entities = PokemonEntity.objects.filter(disappeared_at__gte=localtime(), appeared_at__lte=localtime(), pokemon=pokemon)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.get_photo_url())
        )


    pokemon_on_page = make_pokemon_data(pokemon, request)
    if pokemon.previous_evolution:
        pokemon_on_page["previous_evolution"] = make_pokemon_data(pokemon.previous_evolution, request)
    if pokemon.next_evolution.all():
        pokemon_on_page["next_evolution"] = make_pokemon_data(pokemon.next_evolution.first(), request)

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_on_page
    })


def make_pokemon_data(pokemon, request):
    return {
        'pokemon_id': pokemon.id,
        'img_url': request.build_absolute_uri(pokemon.get_photo_url()),
        'title_ru': pokemon.title,
        'description': pokemon.description,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
    }
