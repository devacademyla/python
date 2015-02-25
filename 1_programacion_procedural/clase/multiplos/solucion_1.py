#!/usr/bin/env python

suma = 0
i = 1

while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        suma += i
    i += 1

print suma
