# -*- coding: utf-8 -*-

resultado = 2 ** 100

print reduce(lambda a,b: a + b, [int(d) for d in str(resultado)])
