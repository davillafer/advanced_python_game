from typing import List, Union

from model.estados.estados import *
from model.pokemons.pokemon import Pokemon


class Pocion:

    @staticmethod
    def effect(pokemon_que_recibe_el_item: Pokemon) -> None:
        if pokemon_que_recibe_el_item.life <= 0:
            print("La 'Poción' no funciona con un pokemon debilitado")
        else:
            print("Se ha aplicado una Poción al pokemon {}".format(pokemon_que_recibe_el_item.name))
            prev_life = pokemon_que_recibe_el_item.life
            pokemon_que_recibe_el_item.life = pokemon_que_recibe_el_item.life + 25
            print("Su vida ha pasado de {0} a {1}".format(prev_life, pokemon_que_recibe_el_item.life))


class AntiQuemar(object):

    @staticmethod
    def effect(pokemon_que_recibe_el_item: Pokemon) -> None:
        if pokemon_que_recibe_el_item.state == Quemado:
            print("Se ha aplicado un AntiQuemar al pokemon {}".format(pokemon_que_recibe_el_item.name))
            pokemon_que_recibe_el_item.state = None
        else:
            if not pokemon_que_recibe_el_item.has_effect():
                print("El 'AntiQuemar' no funciona contra un pokemon en estado normal")
            else:
                print("El 'AntiQuemar' no funciona contra un pokemon en estado '{}'".format(
                    pokemon_que_recibe_el_item.state.__name__))


class AntiEnvenenar(object):

    @staticmethod
    def effect(pokemon_que_recibe_el_item: Pokemon) -> None:
        if pokemon_que_recibe_el_item.state == Envenenado:
            print("Se ha aplicado un AntiEnvenenar al pokemon {}".format(pokemon_que_recibe_el_item.name))
            pokemon_que_recibe_el_item.state = None
        else:
            if not pokemon_que_recibe_el_item.has_effect():
                print("El 'AntiQuemar' no funciona contra un pokemon en estado normal")
            else:
                print("El 'AntiEnvenenar' no funciona contra un pokemon en estado '{}'".format(
                    pokemon_que_recibe_el_item.state.__name__))


class AntiEnterrar(object):

    @staticmethod
    def effect(pokemon_que_recibe_el_item: Pokemon) -> None:
        if pokemon_que_recibe_el_item.state == Enterrado:
            print("Se ha aplicado un AntiEnterrar al pokemon {}".format(pokemon_que_recibe_el_item.name))
            pokemon_que_recibe_el_item.state = None
        else:
            if not pokemon_que_recibe_el_item.has_effect():
                print("El 'AntiQuemar' no funciona contra un pokemon en estado normal")
            else:
                print("El 'AntiEnterrar' no funciona contra un pokemon en estado '{}'".format(
                    pokemon_que_recibe_el_item.state.__name__))


class Bag:

    def __init__(self) -> None:
        self.items: List[Union[Pocion, AntiQuemar, AntiEnvenenar, AntiEnterrar]] = []

    def add_to_bag(self, item: Union[Pocion, AntiQuemar, AntiEnvenenar, AntiEnterrar]) -> None:
        self.items.append(item)

    def add_to_bag_list(self, items: List[Union[Pocion, AntiQuemar, AntiEnvenenar, AntiEnterrar]]) -> None:
        self.items = self.items + items
