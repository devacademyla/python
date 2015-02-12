# -*- coding: utf-8 -*-
import math


def primo(num):
    i = 2
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return num
    else:
        return False
lista = range(1, 1000)
print sum(filter(primo, lista))
