try:
    with open("SodaConcentrateCalc.py", "r", encoding="iso-8859-1") as file:
        code = file.read()

    exec(code)
except Exception as e:
    print("Virhe:", e)
