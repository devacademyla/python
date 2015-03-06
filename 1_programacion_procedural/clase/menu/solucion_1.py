# -*- coding: utf-8 -*-

opcion_elegida = False
opciones_validas = range(1, 4 + 1) # [1, 2, 3, 4]

while not opcion_elegida:
    print u"Elija una de las siguientes opciones:\n"
    print u"1.- Python"
    print u"2.- Javascript"
    print u"3.- Java"
    print u"4.- Ruby"
    print u"\nElija una opción:",
    opcion = raw_input()
    try:
        opcion = int(opcion)
        if opcion in opciones_validas:
            opcion_elegida = True
    except ValueError:
        pass

    if not opcion_elegida:
        print u"\nERROR: No ingresó una opción válida\n"

print u"La opción elegida fué: %d" % opcion
