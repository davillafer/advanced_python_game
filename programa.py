from interprete.interprete import *
from model.game import *


def method_that_asks_for_the_user_name_esp(con_fichero, lector) -> str:
    while True:
        print("Introduzca su nombre de usuario")
        nombre_usuario = obtain_input(con_fichero, lector)
        print("")
        print("Está seguro de que quiere el nombre [{}] (s/n)".format(nombre_usuario))
        seguro = obtain_input(con_fichero, lector)
        print("")
        if seguro.lower() == 's':
            return nombre_usuario
        elif seguro.lower() == 'n':
            pass
        else:
            print(invalid_command(seguro))


def method_that_asks_for_the_user_name_eng(con_fichero, lector) -> str:
    while True:
        print('Introduce your user name')
        nombre_usuario = obtain_input(con_fichero, lector)
        print("")
        print(f'Are you sure? [{nombre_usuario}] (s/n)')
        seguro = obtain_input(con_fichero, lector)
        print("")
        if seguro.lower() == 's':
            return nombre_usuario
        elif seguro.lower() == 'n':
            pass
        else:
            print(f'The option [{seguro}] is not valid\n')


def language(lenguaje_seleccionado):
    if lenguaje_seleccionado == 'eng':
        return principal_menu_eng, method_that_asks_for_the_user_name_eng
    else:
        return principal_menu, method_that_asks_for_the_user_name_esp


def obtain_input(con_fichero, lector):
    if con_fichero:
        result = lector.obtain_order()
        if result != '-1':
            return result
        else:
            return input()
    else:
        return input()


if __name__ == '__main__':
    lector = Lector()
    # Mensaje de bienvenida
    print("Desea leer el fichero? s/n")
    leer_fichero = input()
    con_fichero = False
    if leer_fichero == 's':
        con_fichero = True
        lector.read_file()
    print(title())
    print("Select language (eng/esp)")
    menu, ask = language(obtain_input(con_fichero, lector))
    # Menu principal del juego
    while True:
        print(menu())
        entrada_del_usuario = obtain_input(con_fichero, lector)
        print("")
        # Opción de salida
        if entrada_del_usuario == '1':
            nombre_usuario = ask(con_fichero, lector)
            game = Game(nombre_usuario)
            game.start(con_fichero, lector)
        elif entrada_del_usuario == '2':
            print(instructions())
        elif entrada_del_usuario == '3':
            print(about_me())
        elif entrada_del_usuario == '4':
            break
        else:
            print(invalid_command(entrada_del_usuario))
    # Cierre del juego
    print(exit_msg())
