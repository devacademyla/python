# -*- coding: utf-8 -*-
def rimar(a,b):
	if len(a) <3 or len(b) < 3:
		print "Las palabras tienen menos de 3 letras"
	elif a[-3:] == b[-3:]:
		print "Las palabras", a, "y", b, "riman"
	elif a[-2:] == b[-2:]:
		print "Las palabras", a, "y", b, "riman un poco"
	else:
		print "No riman"
	
rimar("fragmento","fundamento")