# -*- coding: utf-8 -*-
num = 600851475143
div = 2
while div < num:
	if num % div == 0:
		num = num / div
	div = div + 1
print div