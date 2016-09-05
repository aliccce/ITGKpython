



def binærsøk(liste, verdi, start, slutt):
    # Vi finner indeksen til elementet i midten av søkeområdet vårt
    # Søkeområde: Fra start og til men ikke med slutt
    midten = start + (slutt - start) // 2

    if verdi == liste[midten]:
        # Funnet elementet, og finner indeks til første forekomst
        return find_first_index(liste, midten)

    elif slutt - start > 1:
        if verdi < liste[midten]:
            # Elementet kan ligge til venstre i lista
            return binærsøk(liste, verdi, start, midten)
        else:
            # Elementet kan ligge til høyre i lista
            return binærsøk(liste, verdi, midten, slutt)
        
    else:
        # Kun ett element igjen i søkeområdet, og det var ikke det vi leita etter.
        # Elementet finnes derfor ikke i lista.
        return -1
    

def find_first_index(liste, index):
    while liste[index] == liste[index - 1]:
        index -= 1
    return index


li = [1, 2, 2, 2, 3, 4, 5, 7, 7, 7, 8, 34, 76, 456, 3453]

print(li)

# Vi søker gjennom hele lista.
# Du kan dobbeltsjekke at alle indekser den returnerer er riktige!
for ele in li:
    print(binærsøk(li, ele, 0, len(li)))

# Vi prøver å søke etter et element som ikke finnes i lista.
print(binærsøk(li, 2309842, 0, len(li)))
