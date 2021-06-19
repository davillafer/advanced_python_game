from model.pokemons.pokemon import Pokemon


class Envenenado:

    @staticmethod
    def effect(pokemon_que_recibe_el_ataque: Pokemon) -> None:
        if pokemon_que_recibe_el_ataque.life > 0:
            print("{} se ha envenenado y ha perdido 5 puntos de vida".format(pokemon_que_recibe_el_ataque.name))
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 5


class Quemado:

    @staticmethod
    def effect(pokemon_que_recibe_el_ataque: Pokemon) -> None:
        if pokemon_que_recibe_el_ataque.life > 0:
            print("{} se ha quemado y ha perdido 3 puntos de vida".format(pokemon_que_recibe_el_ataque.name))
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 3


class Enterrado:

    @staticmethod
    def effect(pokemon_que_recibe_el_ataque: Pokemon) -> None:
        if pokemon_que_recibe_el_ataque.life > 0:
            print("{} se ha enterrado y ha perdido 10 puntos de vida".format(pokemon_que_recibe_el_ataque.name))
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 10
