import json
import os

def vragen_aanmaken():
    if os.path.exists("vragen.json"):
        with open("vragen.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    vraag = input("Typ een vraag: ")
    antwoord1 = input("Tpye hier antwoord 1: ")
    antwoord2 = input("Tpye hier antwoord 2: ")
    antwoord3 = input("Tpye hier antwoord 3: ")
    antwoord4 = input("Tpye hier antwoord 4: ")
    het_antwoord = input("Type hier HET antwoord (1,2,3,4): ")
    

    vraag_id = len(data) + 1

    nieuwe_vraag = {
        "vraag": vraag,
        "Antwoord_1": antwoord1,
        "Antwoord_2": antwoord2,
        "Antwoord_3": antwoord3,
        "Antwoord_4": antwoord4,
        "Het_antwoord": het_antwoord,
        "id": vraag_id,
    }

    data.append(nieuwe_vraag)

    with open("vragen.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Vraag met ID {vraag_id} opgeslagen!")

def vragen_tonen():
    if os.path.exists("vragen.json"):
        with open("vragen.json", "r") as file:
            try:
                data = json.load(file)
                if not data:
                    print("Er zijn nog geen vragen opgeslagen.")
                    return
            except json.JSONDecodeError:
                print("Fout: JSON-bestand is corrupt.")
                return
    else:
        print("Er zijn nog geen vragen opgeslagen.")
        return

    print("\n📌 Opgeslagen vragen:")
    for vraag in data:
        print(f"ID {vraag['id']}: {vraag['vraag']}")

print("Type (1) om een nieuwe vraag toe te voegen")
print("Type (2) om alle vragen te bekijken")

while True:
    start_input = input(" : ")
    if start_input == "1":
        vragen_aanmaken()
    elif start_input == "2":
        vragen_tonen()
    else:
        print("Invalid input")
