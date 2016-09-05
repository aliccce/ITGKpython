while True:
    try:
        lønn = float(input("Hvor mye har du tjent?\n>>> "))
        dager = int(input("Hvor mange dager har du jobbet?\n>>> "))
        print("Gjennomsnittslønnen er", lønn/dager, "kroner per dag.")    
    
    except ValueError:
        print("Du må skrive et tall.")

    except ZeroDivisionError:
        print("Du kan ikke skrive 0 dager.")

    else:
        print("Takk for at du brukte programmet.")

    finally:
        svar = input("Vil du avslutte? Ja/nei\n>>> ").lower().strip()
        if svar == "ja":
            break



"""
Ved å bare skrive

except:

uten å spesifisere hvilken feilmelding jeg forventer, vil jeg fange alle feilmeldinger.
"""

