import json
import os
import random

SCORE_BORD_FILE = "scorebord.json"
VRAGEN_FILE = "vragen.json"

def quiz_spelen():
    if not os.path.exists(VRAGEN_FILE):
        print("Er zijn geen vragen beschikbaar. Voeg eerst vragen toe.")
        return

    with open(VRAGEN_FILE, "r") as file:
        try:
            vragen = json.load(file)
            if not vragen:
                print("Er zijn geen vragen beschikbaar.")
                return
        except json.JSONDecodeError:
            print("Fout: JSON-bestand is corrupt.")
            return

    random.shuffle(vragen)
    
    naam = input("Voer je naam in: ")
    score = 0

    for vraag in vragen:
        print(f"\n{vraag['vraag']}")
        
        opties = []
        for i in range(1, 5):
            key = f"Antwoord_{i}"
            if key in vraag and vraag[key]:  
                opties.append((i, vraag[key]))

        for nummer, antwoord in opties:
            print(f"{nummer}. {antwoord}")

        beschikbare_nummers = [nummer for nummer, _ in opties]
        while True:
            try:
                antwoord = int(input(f"Jouw antwoord ({'/'.join(map(str, beschikbare_nummers))}): "))
                if antwoord in beschikbare_nummers:
                    break
                else:
                    print(f"Ongeldige keuze, kies een nummer uit: {', '.join(map(str, beschikbare_nummers))}")
            except ValueError:
                print("Voer een geldig nummer in.")

        if str(antwoord) == vraag["Het_antwoord"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Fout! Het juiste antwoord was {vraag['Het_antwoord']}.")

    print(f"\n🎉 {naam}, je hebt {score} van de {len(vragen)} vragen goed!")
    
    score_opslaan(naam, score)

def score_opslaan(naam, score):
    if os.path.exists(SCORE_BORD_FILE):
        with open(SCORE_BORD_FILE, "r") as file:
            try:
                score_data = json.load(file)
            except json.JSONDecodeError:
                score_data = []
    else:
        score_data = []

    score_data.append({"naam": naam, "score": score})

    with open(SCORE_BORD_FILE, "w") as file:
        json.dump(score_data, file, indent=4)

    print("✅ Score opgeslagen!")

def scorebord_tonen():
    if not os.path.exists(SCORE_BORD_FILE):
        print("Nog geen scores opgeslagen.")
        return

    with open(SCORE_BORD_FILE, "r") as file:
        try:
            score_data = json.load(file)
            if not score_data:
                print("Nog geen scores opgeslagen.")
                return
        except json.JSONDecodeError:
            print("Fout: JSON-bestand is corrupt.")
            return

    print("\n📊 Scorebord:")
    for score in sorted(score_data, key=lambda x: x["score"], reverse=True):
        print(f"{score['naam']}: {score['score']} punten")

print("Type (1) om de quiz te spelen")
print("Type (2) om het scorebord te bekijken")

while True:
    start_input = input(" : ")
    if start_input == "1":
        quiz_spelen()
    elif start_input == "2":
        scorebord_tonen()
    else:
        print("Ongeldige invoer.")
