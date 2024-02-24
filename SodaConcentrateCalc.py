import math

try:
    soda = int(input("Paljonko haluat valmista juotavaa (dl)? "))
    tiivisteosuus = int(input("Anna tiivisteen sekoitus suhteen tiiviste osuus: "))
    vesiosuus = int(input("Anna tiivisteen sekoitus suhteen vesi osuus: "))

    if tiivisteosuus + vesiosuus == 0:
        raise ValueError("Tiiviste- ja vesi-osuuksien summa ei voi olla nolla.")

    tiiviste_dl = (tiivisteosuus / (tiivisteosuus + vesiosuus)) * soda
    vesi_dl = (vesiosuus / (tiivisteosuus + vesiosuus)) * soda

    # Muunnetaan desimaaliluvut haluttuun muotoon (0.5 dl = 50 ml, 1 dl = 100 ml)
    tiiviste_ml = tiiviste_dl * 100
    vesi_ml = vesi_dl * 100

    # Pyöristetään tiivisteen määrä ylöspäin lähimpään kokonaislukuun
    tiiviste_ml_pyoristetty = math.ceil(tiiviste_ml)

    # Muunnetaan vesi litroiksi ja millilitroiksi
    vesi_dl_kokonaisluku = int(vesi_dl)
    vesi_ml_jaljella = int((vesi_dl - vesi_dl_kokonaisluku) * 100)

    # Tulostetaan tulokset halutussa muodossa
    print(f"Tarvitset {tiiviste_ml_pyoristetty} ml tiivistettä ja {vesi_dl_kokonaisluku} dl ja {vesi_ml_jaljella} ml vettä")
except ValueError as ve:
    print("Virheellinen syöte:", ve)
except Exception as e:
    print("Jokin meni pieleen:", e)
    
input("Paina Enter sulkeaksesi ohjelma...")