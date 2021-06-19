from model.estados.estados import *


class Bicho:

    @staticmethod
    def aguijon(pokemon_que_realiza_el_ataque, pokemon_que_recibe_el_ataque):
        print("{0} usa 'aguijón'.\n".format(pokemon_que_realiza_el_ataque.name))
        print("{0} ha perdido 15 puntos de vida.".format(pokemon_que_recibe_el_ataque.name))
        if pokemon_que_recibe_el_ataque.has_effect():
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 15
        elif pokemon_que_recibe_el_ataque.had_state:
            print("{0} ya ha cambiado el estado una vez, no puede volver a ser afectado.".format(
                pokemon_que_recibe_el_ataque.name))
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 15
        else:
            print("{0} ha sido 'Envenenado'.".format(pokemon_que_recibe_el_ataque.name))
            pokemon_que_recibe_el_ataque.state = Envenenado
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 15
        print("")


class Fuego:

    @staticmethod
    def quemadura(pokemon_que_realiza_el_ataque, pokemon_que_recibe_el_ataque):
        print("{0} usa 'quemadura'.\n".format(pokemon_que_realiza_el_ataque.name))
        print("{0} ha perdido 10 puntos de vida.".format(pokemon_que_recibe_el_ataque.name))
        pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 10

    @staticmethod
    def llamarada(pokemon_que_realiza_el_ataque, pokemon_que_recibe_el_ataque):
        print("{0} usa 'llamarada'.\n".format(pokemon_que_realiza_el_ataque.name))
        print("{0} ha perdido 30 puntos de vida.".format(pokemon_que_recibe_el_ataque.name))
        if pokemon_que_recibe_el_ataque.has_effect():
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 30
        elif pokemon_que_recibe_el_ataque.had_state:
            print("{0} ya ha cambiado el estado una vez, no puede volver a ser afectado.".format(
                pokemon_que_recibe_el_ataque.name))
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 30
        else:
            print("{0} ha sido 'Quemado'.".format(pokemon_que_recibe_el_ataque.name))
            pokemon_que_recibe_el_ataque.state = Quemado
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 30
        print("")


class Tierra:

    @staticmethod
    def bomba_lodo(pokemon_que_realiza_el_ataque, pokemon_que_recibe_el_ataque):
        print("{0} usa 'bomba_lodo'.\n".format(pokemon_que_realiza_el_ataque.name))
        print("{0} ha perdido 40 puntos de vida.".format(pokemon_que_recibe_el_ataque.name))
        if pokemon_que_recibe_el_ataque.has_effect():
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 40
        elif pokemon_que_recibe_el_ataque.had_state:
            print("{0} ya ha cambiado el estado una vez, no puede volver a ser afectado.".format(
                pokemon_que_recibe_el_ataque.name))
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 40
        else:
            print("{0} ha sido 'Enterrado'.".format(pokemon_que_recibe_el_ataque.name))
            pokemon_que_recibe_el_ataque.state = Enterrado
            pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 40
        print("")


class Agua:

    @staticmethod
    def pistola_agua(pokemon_que_realiza_el_ataque, pokemon_que_recibe_el_ataque):
        print("{0} usa 'pistola_agua'.\n".format(pokemon_que_realiza_el_ataque.name))
        print("{0} ha perdido 15 puntos de vida.".format(pokemon_que_recibe_el_ataque.name))
        pokemon_que_recibe_el_ataque.life = pokemon_que_recibe_el_ataque.life - 25
        print("")
