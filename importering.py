
# Importere hele biblioteket.

import math
print(math.sin(0))


# Importere hele biblioteket med as

import math as m
print(m.sin(0))


# Importere visse funksjoner fra et bibliotek

from math import sin, cos
print(sin(0), cos(0))


# Importere alle funksjoner fra et bibliotek
# Merk at funksjonsnavn kan kollidere!

from math import *
print(pi, tan(0))

