#!/usr/bin/env python

def num_prim(num):
	div = 2
	while div < num:
		if num % div == 0:
			num = num / div
		div = div + 1
	print div

if __name__ == '__main__':
    num_prim(600851475143)
