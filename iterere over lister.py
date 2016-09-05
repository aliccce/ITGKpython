
liste = ['tomat', 'agurk', 'gulrot', 'squash',\
         'aubergine', 'salat', 'paprika']




# iterere over elementer

for grønnsak in liste:
    print(grønnsak)
    """ Denne måten å iterere på er bra, hvis vi
    bare skal printe elementene eller bruke de til noe,
    og vi ikke trenger å endre på lista.

    Passende variabelnavn:
    item, element, eller noe som beskriver hva som
    er i lista. """



# iterere over indekser

for i in range(len(liste)):
    print("indeks: ", i)
    print("element: ", liste[i])

    """
    Passende variabelnavn:
    i, j, k, x, y
    index

    """



# For å endre på elementer i lista,
# itererer vi over indekser

for i in range(len(liste)):
    
    liste[i] = 0
    
    print(liste)
    print()

""" Dette fungerer ikke:

for grønnsak in liste:
    grønnsak = 0
    # Lista blir /ikke/ endret,
    # kun variabelen "grønnsak" blir endret.

"""


# Hvis vi trenger påfølgende eller etterfølgende
# elementer i lista, itererer vi over indekser

for i in range(0, len(liste), 2):
    if i == len(liste) - 1:
        print(liste[i])
        """Hvis i er indeks til siste element i lista,
        kan vi bare printe dette elementet.
        liste[i + 1] vil gi feilmeldingen IndexError."""
        
    else:
        print(liste[i], liste[i + 1])
    




















