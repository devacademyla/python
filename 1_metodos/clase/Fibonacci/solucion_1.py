# -*- coding: utf-8 -*-
fib = 1
fib2 = 2
acarr = 0
suma = 0

while acarr <=4000000:
    acarr = fib2
    if acarr % 2 == 0:
        suma += acarr
    acarr = fib + fib2
    fib = fib2
    fib2 = acarr

print suma 

