# -*- coding: utf-8 -*-
numeros = range(6, 16)

listado = ['par:{}'.format(num) if num % 2 == 0 else 'impar:{}'.format(num) for num in numeros]
print listado
