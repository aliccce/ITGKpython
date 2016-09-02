
# Vi oppretter en matrise med gangetabellen for tallene 1 til 10.

matrise = []

for i in range(1, 11):
    rad = []
    for j in range(1, 11):
        rad.append(i * j)
    matrise.append(rad)


# Fin printing av matrisa, der vi benytter streng.rjust()-funksjonen

for rad in matrise:
    for tall in rad:
        print(str(tall).rjust(5), end="")
    print()


# Deretter sletter vi elementer og rader fra matrisa

del matrise[0][1]
del matrise[0][8]
del matrise[2] # Legg merke til at her slettes faktisk en hel rad
del matrise[4][2]
del matrise[3][2]
del matrise[8][9]


# Nå vil vi endre alle tall i matrisa til 0 istedet, men nå er det
# ikke lenger sånn at alle rader har lengde 10. Derfor passer vi på
# å bruke len(matrise) og len(rad) [samme som len(matrise[i])] i
# for-løkkene.

for i in range(len(matrise)):
    rad = matrise[i]
    for j in range(len(rad)):
        rad[j] = 0
        # Merk at her vil matrise[i][j] = 0 gi akkurat samme resultat!


# Til slutt printer vi matrisa igjen - dette er samme kode som tidligere!
print("\n")

for rad in matrise:
    for tall in rad:
        print(str(tall).rjust(5), end="")
    print()
