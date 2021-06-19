import random

from model.pokemons.pokemon import Pokemon
from programa import obtain_input
from interprete.interprete import show_menu_combate, invalid_command, show_pokemons, show_ganador, show_perdedor
from interprete.lector import Lector
from model.bag.bag import *
from model.tipos.tipos import *


class Game:

    def __init__(self, player_name: str) -> None:
        self.player_name = player_name
        self.pokemon_usuario = None
        self.pokemon_pc = None
        self.equipo_del_usuario = None
        self.equipo_del_pc = None
        self.mochila = Bag()
        self.mochila.add_to_bag_list([Pocion(), AntiQuemar(), AntiEnvenenar(), AntiEnterrar()])

    def start(self, con_fichero: bool, lector: Lector) -> None:
        print("Hola {}. El combate contra el entrenador Brock ha comenzado.".format(self.player_name))
        self.equipo_del_usuario = [
            Pokemon("Weedle", [Bicho, Tierra], 105),
            Pokemon("Charmander", [Fuego], 85)
        ]
        self.equipo_del_pc = [
            Pokemon("Blastoise", [Tierra, Agua], 65),
            Pokemon("Magikarp", [Agua], 35)
        ]
        self.pokemon_usuario = self.equipo_del_usuario[0]
        self.pokemon_pc = self.equipo_del_pc[0]
        print(show_pokemons(self.pokemon_usuario, self.player_name, self.pokemon_pc))
        while True:
            if self.all_debilitados(self.equipo_del_usuario):
                print("Fin de la partida.\n")
                print(show_perdedor())
                break
            elif self.all_debilitados(self.equipo_del_pc):
                print("Fin de la partida.\n")
                print(show_ganador())
                break
            else:
                print(show_menu_combate())
                entrada_usuario = obtain_input(con_fichero, lector)
                print("")
                if entrada_usuario == '1':
                    self.fight(con_fichero, lector)
                elif entrada_usuario == '2':
                    self.bag(con_fichero, lector)
                elif entrada_usuario == '3':
                    self.change_pokemon(self.equipo_del_usuario, con_fichero, lector)
                elif entrada_usuario == '4':
                    self.information(self.player_name, self.pokemon_usuario, self.pokemon_pc)
                elif entrada_usuario == '5':
                    break
                else:
                    print(invalid_command(entrada_usuario))

    def fight_pc(self):
        if self.pokemon_pc.life <= 0:
            print("El pokemon del rival ha sido debilitado.")
            for p in self.equipo_del_pc:
                if p.life > 0:
                    self.pokemon_pc = p
                    print("El rival ha sacado a {}".format(p.name))
        else:
            ataque = self.ataque_random()
            for t in self.pokemon_pc.types:
                if ataque in dir(t):
                    getattr(t, ataque)(self.pokemon_pc, self.pokemon_usuario)

    def fight(self, con_fichero, lector):
        if self.pokemon_usuario.life <= 0:
            print("Tu pokemon ha sido debilitado, debes cambiar de pokemon.")
        elif self.pokemon_usuario.has_effect():
            print("Tu pokemon se encuentra {}. Debes curarle.".format(self.pokemon_usuario.state.__name__))
        else:
            change = False
            while True:
                print("Seleccione el ataque que desea realizar:")
                ataques = []
                for t in self.pokemon_usuario.types:
                    ataques = ataques + ([f for f in dir(t) if not f.startswith("__")])
                ataques_temp = self.ataques(ataques)
                entrada_usuario = obtain_input(con_fichero, lector)
                print("")
                if int(entrada_usuario) == len(ataques_temp):
                    change = True
                    break
                elif int(entrada_usuario) > len(ataques_temp) or int(entrada_usuario) <= 0:
                    print(invalid_command(entrada_usuario))
                else:
                    aux = ataques_temp[int(entrada_usuario) - 1][1]
                    for t in self.pokemon_usuario.types:
                        if aux in dir(t):
                            getattr(t, aux)(self.pokemon_usuario, self.pokemon_pc)
                    break
            if not change:
                self.change_turn()

    def ataque_random(self):
        lista = []
        for t in self.pokemon_pc.types:
            lista.append(random.choice([f for f in dir(t) if not f.startswith("__")]))
        item = random.choice(lista)
        return item

    def bag(self, con_fichero, lector):
        print("Utensilios en la mochila:")
        print("\t{}".format([type(f).__name__ for f in self.mochila.items]))
        aux = False
        while True:
            print("Seleccione el utensilio a utilizar:")
            utensilios_temp = self.utensilios(self.mochila.items)
            entrada_usuario = obtain_input(con_fichero, lector)
            print("")
            if int(entrada_usuario) == len(utensilios_temp):
                aux = True
                break
            elif int(entrada_usuario) > len(utensilios_temp) or int(entrada_usuario) <= 0:
                print(invalid_command(entrada_usuario))
            else:
                utensilios_temp[int(entrada_usuario) - 1][1].effect(self.pokemon_usuario)
                break
        if not aux:
            self.change_turn()

    def change_pokemon(self, equipo_del_usuario, con_fichero, lector):
        print("Equipo pokemon:")
        print("\tDisponibles:")
        print("\t{}".format(
            [("{0} ({1} puntos de vida)".format(f.name, f.life)) for f in equipo_del_usuario if f.life > 0])
        )
        print("\tDebilitados:")
        print("\t{}".format([f.name for f in equipo_del_usuario if f.life <= 0]))
        print("")
        aux = False
        while True:
            print("Seleccione el pokemon a sacar:")
            equipo_temp = self.equipo(equipo_del_usuario)
            entrada_usuario = obtain_input(con_fichero, lector)
            print("")
            if int(entrada_usuario) == len(equipo_temp):
                aux = True
                break
            elif int(entrada_usuario) > len(equipo_temp) or int(entrada_usuario) <= 0:
                print(invalid_command(entrada_usuario))
            else:
                if equipo_temp[int(entrada_usuario) - 1][1].name == self.pokemon_usuario.name:
                    print("El pokemon seleccionado ya está en el campo de batalla")
                elif equipo_temp[int(entrada_usuario) - 1][1].life <= 0:
                    print("El pokemon seleccionado está debilitado")
                else:
                    print("Vuelve {}".format(self.pokemon_usuario.name))
                    self.pokemon_usuario = equipo_temp[int(entrada_usuario) - 1][1]
                    print("Adelante {}".format(self.pokemon_usuario.name))
                    break
        if not aux:
            self.change_turn()

    def information(self, player_name, pokemon_from_user, pokemon_from_cpu):
        print("Información sobre los pokemons en el campo de batalla:")
        print("{0} tiene sobre el campo a {1} y sus ataques son".format(player_name, pokemon_from_user.name))
        for t in pokemon_from_user.types:
            print("\t{}".format([f for f in dir(t) if not f.startswith("__")]))
        print("El rival tiene sobre el campo a {} y sus ataques son".format(pokemon_from_cpu.name))
        for t in pokemon_from_cpu.types:
            print("\t{}".format([f for f in dir(t) if not f.startswith("__")]))
        print("")

    def equipo(self, team_from_user):
        back_counter = 1
        result = []
        for p in team_from_user:
            if p.life > 0:
                print("[{0}]\t{1}".format(back_counter, p.name))
                result.append((back_counter, p))
                back_counter = back_counter + 1
        print("[{}]\tAtrás".format(back_counter))
        result.append((back_counter, "Atrás"))
        return result

    def utensilios(self, utensilios):
        result = []
        back_counter = 1
        for p in utensilios:
            print("[{0}]\t{1}".format(back_counter, type(p).__name__))
            result.append((back_counter, p))
            back_counter = back_counter + 1
        print("[{}]\tAtrás".format(back_counter))
        result.append((back_counter, "Atrás"))
        return result

    def ataques(self, ataques):
        result = []
        back_counter = 1
        for p in ataques:
            print("[{0}]\t{1}".format(back_counter, p))
            result.append((back_counter, p))
            back_counter = back_counter + 1
        print("[{}]\tAtrás".format(back_counter))
        result.append((back_counter, "Atrás"))
        return result

    def change_turn(self):
        print("Turno del rival: ")
        self.apply_effect(self.pokemon_pc)
        self.fight_pc()
        self.status()
        print("Turno de {}:\n".format(self.player_name))
        self.apply_effect(self.pokemon_usuario)

    def all_debilitados(self, equipo):
        for p in equipo:
            if p.life > 0:
                return False
        return True

    def status(self):
        if self.pokemon_usuario.has_effect():
            print("[{0} / puntos de vida: {1} / estado: {2}]".format(self.pokemon_usuario.name,
                                                                     self.pokemon_usuario.life,
                                                                     self.pokemon_usuario.state.__name__))
        else:
            print("[{0} / puntos de vida: {1} / sin estado]".format(self.pokemon_usuario.name,
                                                                    self.pokemon_usuario.life))
        if self.pokemon_pc.has_effect():
            print("[{0} / puntos de vida: {1} / estado: {2}]".format(self.pokemon_pc.name, self.pokemon_pc.life,
                                                                     self.pokemon_pc.state.__name__))
        else:
            print("[{0} / puntos de vida: {1} / sin estado]".format(self.pokemon_pc.name, self.pokemon_pc.life))

    def apply_effect(self, pokemon):
        if pokemon.has_effect():
            pokemon.state.effect(pokemon)
