i = 0

while i <= 10:
    i += 1
    print "Vuelta numero %d" % i
    if i % 2 == 0: 
        print i
    if i == 6:
        continue
    print "Este es el final del bloque..."
   
