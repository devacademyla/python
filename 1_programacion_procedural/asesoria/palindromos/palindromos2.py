import string

cadena_original = raw_input("Ingrese una cadena: ")

cadena2 = ''

# Copia todos los caracteres que sean letras
# y no copia los otros

for c in cadena_original.lower():
	if c in string.ascii_lowercase:
		cadena2 += c

palindromo = True
for i in range(len(cadena2) // 2):
	if cadena2[i] != cadena2[-1*(i+1)]:
		palindromo = False
		break

if palindromo:
	print "La cadena '%s' es palindroma" % cadena_original
else:
	print "La cadena '%s' NO es palindroma" % cadena_original
