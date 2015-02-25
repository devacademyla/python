# -*- coding: utf-8 -*-

def rimar(a, b):
    if len(a) < 3 or len(b) < 3:
        print "Las dos palabras tienen que tener al menos 3 letras."
    elif a[-3:] == b[-3:]:
        print "Las palabras \"%s\" y \"%s\" riman." % (a, b)
    elif a[-2:] == b[-2:]:
        print "Las palabras \"%s\" y \"%s\" riman un poco." % (a, b)
    else:
        print "Las palabras \"%s\" y \"%s\" NO riman." % (a, b)

if __name__ == '__main__':
    palabras = [
        (u"fragmento", u"fundamento"),
        (u"avión", u"canción"),
        (u"presidente", u"ministerio"),
        (u"ab", "ac"),
        (u"zapato", u"rata"),
        (u"hermano", u"fulano")
    ]

    for p1, p2 in palabras:
        rimar(p1, p2)
