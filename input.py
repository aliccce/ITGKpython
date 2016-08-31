

# Enkelt eksempel på bruk av input-funksjon:

navn = input("Hva er navnet ditt?")
print("Hei", navn)


# Gjøre om input til et tall:

alder = int(input("Hvor gammel er du?"))
årstall = 2016 - alder


# sette sammen flere strenger til en streng:

født_i_årstall = input("Ble du født i " + str(årstall) + "?")
print("Du svarte:", født_i_årstall)
