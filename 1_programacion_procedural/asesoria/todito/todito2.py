# -*- coding: utf-8 -*-
import random

dado = random.randrange(1, 7)
print 'Resultado:', dado
if dado == 1 or dado == 5:
    print "Toman todos"
elif dado == 2 or dado == 6:
    print "Toma otro"
elif dado == 3:
    print "Toma el de la derecha"
elif dado == 4:
    print "Toma el de la izquierda"
else:
    print 'El numero no se encuentra'
