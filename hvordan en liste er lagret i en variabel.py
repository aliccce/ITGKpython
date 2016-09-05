
def doble_innhold_i_ny_liste(li):
    # Vi oppretter en tom liste, og legger til endringene i denne.
    ny_li = []
    for element in li:
        ny_li.append(element * 2)
    return ny_li

def halvere_innhold_i_ny_liste(li):
    # Vi kopierer lista vi får som argument, og endrer på den kopierte lista.
    kopiert_liste = li[:]
    for i in range(len(kopiert_liste)):
        kopiert_liste[i] = kopiert_liste[i] // 2
    return kopiert_liste

def gjør_til_toere(li):
    for i in range(len(li)):
        li[i] = 2


# Eksempel der samme liste blir endret på
liste = [4, 2, 5, 1]

print("Før funksjon:   ", liste)
gjør_til_toere(liste)
print("Etter funksjon: ", liste, "\n")


# Eksempel der vi passer på at endringene kommer i en ny liste
gammel_liste = [2, 4, 6, 8]

ny_liste_1 = halvere_innhold_i_ny_liste(gammel_liste)
ny_liste_2 = doble_innhold_i_ny_liste(gammel_liste)

print("Gammel:  ", gammel_liste)
print("Ny1:     ", ny_liste_2)
print("Ny2:     ", ny_liste_2)
