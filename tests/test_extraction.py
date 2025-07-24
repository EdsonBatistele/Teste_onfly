import pytest
from src.extraction import get_pokemons, get_details_pokemon


def test_get_pokemons():
    pokemons = get_pokemons(limit=5)
    assert isinstance(pokemons, list)
    assert len(pokemons) == 5
    assert "name" in pokemons[0]
    assert "url" in pokemons[0]


def test_get_details_pokemon():
    bulbasaur_url = "https://pokeapi.co/api/v2/pokemon/1/"
    details = get_details_pokemon(bulbasaur_url)
    assert isinstance(details, dict)
    assert details["name"] == "bulbasaur"
    assert "stats" in details
