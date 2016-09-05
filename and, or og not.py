
alder = int(input("Hvor gammel er du? "))
høyde = int(input("Hvor høy er du? "))
hjerteproblemer = False



# Man kan ta berg-og-dal-banen hvis man er eldre enn 18 år,
# eller 13 år og høyere enn 140 cm:

if alder >= 18 or (alder >= 13 and høyde >= 140):
    print("Du får ta berg-og-dalbanen")

""" Dette vil gi samme resultat, men vi har overflødig kode: """
if alder >= 18:
    print("Du får ta berg-og-dalbanen") # samme her
elif  alder >= 13 and høyde >= 140:
    print("Du får ta berg-og-dalbanen") # som her!



# Man må være eldre enn 18 år, og man kan ikke ha hjerteproblemer:

if alder >= 18 and not hjerteproblemer:
    print("Du får ta berg-og-dal-banen")



# Man må være eldre enn 18 år, eller 13 år og minst 140 cm,
# men man kan ikke ha hjerteproblemer:

""" En måte å løse det på: """
if (alder >= 18 or (alder >= 13 and høyde >= 140)) and not hjerteproblemer:
    print("Du får ta berg-og-dalbanen")

""" En annen måte å løse det på, som er lettere å lese / mer oversiktlig: """
if not hjerteproblemer:
    if alder >= 18 or (alder >= 13 and høyde >= 140):
        print("Du får ta berg-og-dalbanen")


