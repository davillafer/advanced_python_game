import unittest

from model.bag.bag import *
from model.estados.estados import *
from model.game import *
from model.pokemons.pokemon import Pokemon
from model.tipos.tipos import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_game = Game("usuario_de_prueba")
        self.test_game.equipo_del_usuario = [
            Pokemon("Weedle", [Bicho, Tierra], 105),
            Pokemon("Charmander", [Fuego], 85),
            Pokemon("Blastoise", [Tierra, Agua], 65),
            Pokemon("Magikarp", [Agua], 35)
        ]
        self.test_game_2 = Game("otro_usuario_de_prueba")
        self.test_game_2.equipo_del_usuario = [
            Pokemon("Weedle", [Bicho, Tierra, Agua], 105),
            Pokemon("Charmander", [Tierra], 85),
            Pokemon("Blastoise", [Tierra, Bicho], 65)
        ]

    def test_ataques_segun_tipos(self):
        """
        Bicho - aguijón
        Fuego - quemadura, llamarada
        Tierra - bomba_lodo
        Agua - pistola_agua
        """
        ataques = []
        for pokemon in self.test_game.equipo_del_usuario:
            for tipo in pokemon.types:
                ataques = ataques + ([f for f in dir(tipo) if not f.startswith("__")])
        self.assertEqual(['aguijon', 'bomba_lodo', 'llamarada', 'quemadura', 'bomba_lodo', 'pistola_agua',
                          'pistola_agua'], ataques)
        ataques = []
        for pokemon in self.test_game_2.equipo_del_usuario:
            for tipo in pokemon.types:
                ataques = ataques + ([f for f in dir(tipo) if not f.startswith("__")])
        self.assertEqual(['aguijon', 'bomba_lodo', 'pistola_agua', 'bomba_lodo', 'bomba_lodo', 'aguijon'], ataques)

    def test_llenar_mochila(self):
        """
        add_to_bag(item)
        add_to_bag_list([items])
        """
        mochila = Bag()
        mochila.add_to_bag(Pocion())
        mochila.add_to_bag(AntiQuemar())
        self.assertEqual(len(mochila.items), 2)
        mochila.add_to_bag(AntiEnvenenar())
        mochila.add_to_bag(AntiEnterrar())
        self.assertEqual(len(mochila.items), 4)
        mochila.add_to_bag(AntiEnvenenar())
        mochila.add_to_bag(AntiEnterrar())
        self.assertEqual(len(mochila.items), 6)
        mochila_2 = Bag()
        mochila_2.add_to_bag_list([Pocion(), AntiQuemar(), AntiEnvenenar(), AntiEnterrar()])
        self.assertEqual(len(mochila_2.items), 4)

    def test_efectos_en_estado_pokemons(self):
        """
        __setattr__()
        has_effect()
        apply_effect()
        """
        self.test_game.equipo_del_usuario[0].state = Envenenado
        self.assertEqual(self.test_game.equipo_del_usuario[0].has_effect(), True)
        self.assertEqual(self.test_game.equipo_del_usuario[0].state.__name__, 'Envenenado')
        self.test_game.equipo_del_usuario[0].state = None
        self.assertEqual(self.test_game.equipo_del_usuario[0].has_effect(), False)
        self.test_game.equipo_del_usuario[0].state = Enterrado
        self.assertEqual(self.test_game.equipo_del_usuario[0].has_effect(), False)

        p = Pokemon("Weedle", [Bicho, Tierra, Agua], 100)
        p.state = Enterrado
        self.assertEqual(p.has_effect(), True)
        self.assertEqual(p.state.__name__, 'Enterrado')
        self.assertEqual(p.life, 100)
        p.apply_effect()
        self.assertEqual(p.life, 90)

        p = Pokemon("Weedle", [Bicho, Tierra, Agua], 100)
        p.state = Envenenado
        self.assertEqual(p.has_effect(), True)
        self.assertEqual(p.state.__name__, 'Envenenado')
        self.assertEqual(p.life, 100)
        p.apply_effect()
        self.assertEqual(p.life, 95)

        p = Pokemon("Weedle", [Bicho, Tierra, Agua], 100)
        p.state = Quemado
        self.assertEqual(p.has_effect(), True)
        self.assertEqual(p.state.__name__, 'Quemado')
        self.assertEqual(p.life, 100)
        p.apply_effect()
        self.assertEqual(p.life, 97)

    def test_efectos_de_mochila_a_pokemons(self):
        """
        effect(Pokemon)
        """
        p = Pokemon("Weedle", [Bicho, Tierra, Agua], 100)
        p.state = Enterrado
        self.assertEqual(p.has_effect(), True)
        self.assertEqual(p.state.__name__, 'Enterrado')
        self.assertEqual(p.life, 100)
        Pocion.effect(p)
        self.assertEqual(p.life, 125)

        p = Pokemon("Weedle", [Bicho, Tierra, Agua], 100)
        p.state = Enterrado
        self.assertEqual(p.has_effect(), True)
        AntiEnterrar.effect(p)
        self.assertEqual(p.has_effect(), False)

        p = Pokemon("Weedle", [Bicho, Tierra, Agua], 100)
        p.state = Envenenado
        self.assertEqual(p.has_effect(), True)
        AntiEnvenenar.effect(p)
        self.assertEqual(p.has_effect(), False)

        p = Pokemon("Weedle", [Bicho, Tierra, Agua], 100)
        p.state = Quemado
        self.assertEqual(p.has_effect(), True)
        AntiQuemar.effect(p)
        self.assertEqual(p.has_effect(), False)


if __name__ == '__main__':
    unittest.main()
