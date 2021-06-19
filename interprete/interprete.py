from model.pokemons.pokemon import Pokemon


def title() -> str:
    return ' __   __        ___        __\n|__) /  \ |__/ |__   |\/| /  \ |\ |\n|    \__/ |  \ |___  |  | \__/ | \|\n'


def principal_menu() -> str:
    return '[1]\tJugar\n[2]\tInstrucciones\n[3]\tSobre mí\n[4]\tSalir\n'


def principal_menu_eng() -> str:
    return '[1]\tPlay\n[2]\tInstructions\n[3]\tAbout me\n[4]\tExit\n'


def exit_msg() -> str:
    return 'Gracias por jugar'


def instructions() -> str:
    return 'El juego consiste en un combate pokemon contra otro entrenador. Los entrenadores dispondrán de turnos\n' \
           'alternos donde podrán realizar sus ataques, utilizar elementos de la mochila o cambiar el pokemon del\n' \
           'campo de batalla\n'


def about_me() -> str:
    return "Juego creado por David Villamil Fernández - UO244801\n"


def invalid_command(entrada_del_usuario: str) -> str:
    return f'La opción [{entrada_del_usuario}] no es válida\n'


def show_menu_combate() -> str:
    return '[1]\tLuchar\n[2]\tMochila\n[3]\tCambiar pokemon\n[4]\tInformación\n[5]\tHuir'


def show_pokemons(pokemon_from_user: Pokemon, player_name: str, pokemon_from_cpu: Pokemon) -> str:
    return f'El rival ha utilizado ha {pokemon_from_cpu.name}. {player_name} ha utilizado a {pokemon_from_user.name}.\n'


def show_ganador() -> str:
    return '  _   _                                         _       \n | | | | __ _ ___    __ _  __ _ _ __   __ _  ' \
           '__| | ___  \n | |_| |/ _` / __|  / _` |/ _` | \'_ \ / _` |/ _` |/ _ \ \n |  _  | (_| \__ \ | (_| | (_| |' \
           ' | | | (_| | (_| | (_) |\n |_| |_|\__,_|___/  \__, |\__,_|_| |_|\__,_|\__,_|\___/ \n                  ' \
           '  |___/                               '


def show_perdedor() -> str:
    return '  _   _                                _ _     _       \n | | | | __ _ ___   _ __   ___ _ __ __| (_)' \
           ' __| | ___  \n | |_| |/ _` / __| | \'_ \ / _ \ \'__/ _` | |/ _` |/ _ \ \n |  _  | (_| \__ \ | |_) |  __/ ' \
           '| | (_| | | (_| | (_) |\n |_| |_|\__,_|___/ | .__/ \___|_|  \__,_|_|\__,_|\___/\n                   ' \
           '|_|                                 '
