import json
import random

quiz_data = {
    "Kubuś Puchatek": [
        {"pytanie": "Jak nazywa się przyjaciel Kubusia z długimi uszami?",
         "odpowiedzi": ["Tygrysek", "Kłapouchy", "Prosiaczek", "Krzyś"],
         "poprawna": "Kłapouchy"},
        {"pytanie": "Czego najbardziej lubi Kubuś?",
         "odpowiedzi": ["Miodu", "Mleka", "Marchewek", "Soku"],
         "poprawna": "Miodu"},
        {"pytanie": "Jak nazywa się człowiek w Stumilowym Lesie?",
         "odpowiedzi": ["Krzyś", "Krystian", "Krystek", "Karol"],
         "poprawna": "Krzyś"},
        {"pytanie": "Jakim zwierzęciem jest Tygrysek?",
         "odpowiedzi": ["Niedźwiadkiem", "Kangurem", "Tygrysem", "Osiołkiem"],
         "poprawna": "Tygrysem"},
        {"pytanie": "Kto ciągle się smuci?",
         "odpowiedzi": ["Prosiaczek", "Królik", "Kłapouchy", "Tygrysek"],
         "poprawna": "Kłapouchy"}
    ],
    "Czerwony Kapturek": [
        {"pytanie": "Kogo odwiedzała Czerwony Kapturek?",
         "odpowiedzi": ["Mamę", "Siostrę", "Babcię", "Kuzynkę"],
         "poprawna": "Babcię"},
        {"pytanie": "Kto chciał zjeść Kapturka?",
         "odpowiedzi": ["Niedźwiadek", "Wilk", "Lis", "Smok"],
         "poprawna": "Wilk"},
        {"pytanie": "Jakiego koloru był Kapturek?",
         "odpowiedzi": ["Zielony", "Różowy", "Czerwony", "Niebieski"],
         "poprawna": "Czerwony"},
        {"pytanie": "Co przynosiła babci?",
         "odpowiedzi": ["Ciasto", "Kwiaty", "Lekarstwa", "Mleko"],
         "poprawna": "Lekarstwa"},
        {"pytanie": "Kto uratował babcię i Kapturka?",
         "odpowiedzi": ["Myśliwy", "Tata", "Książę", "Wilk zmienił zdanie"],
         "poprawna": "Myśliwy"}
    ],
    "Król Lew": [
        {"pytanie": "Jak nazywa się główny bohater filmu Król Lew?",
         "odpowiedzi": ["Mufasa", "Skaza", "Simba", "Rafiki"],
         "poprawna": "Simba"},
        {"pytanie": "Kim był Mufasa dla Simby?",
         "odpowiedzi": ["Wujkiem", "Ojcem", "Dziadkiem", "Bratem"],
         "poprawna": "Ojcem"},
        {"pytanie": "Jak nazywa się zły brat Mufasy?",
         "odpowiedzi": ["Zazu", "Timon", "Skaza", "Nala"],
         "poprawna": "Skaza"},
        {"pytanie": "Jakie zwierzę to Timon?",
         "odpowiedzi": ["Lew", "Hiena", "Świnia", "Surykatka"],
         "poprawna": "Surykatka"},
        {"pytanie": "Co oznacza 'Hakuna Matata'?",
         "odpowiedzi": ["Walcz", "Nie martw się", "Ruszaj", "Król"],
         "poprawna": "Nie martw się"}
    ]
}

def zapisz_wyniki(wyniki):
    try:
        with open("quiz.json", "w") as f:
            json.dump(wyniki, f)
        print("😄Wyniki zapisane!😃")
    except:
        print("😐Błąd zapisu pliku.😬")

def wczytaj_wyniki():
    try:
        with open("quiz.json", "r") as f:
            return json.load(f)
    except:
        return {}

def pomieszaj_odpowiedzi(pytanie):
    odp = pytanie["odpowiedzi"][:]
    random.shuffle(odp)
    return {litera: odp[i] for i, litera in enumerate(["A", "B", "C", "D"])}

def uruchom_quiz(nazwa_bajki):
    pytania = quiz_data[nazwa_bajki][:]
    random.shuffle(pytania)
    wynik = 0
    for p in pytania:
        print("\n" + p["pytanie"])
        odp_dict = pomieszaj_odpowiedzi(p)
        for litera in sorted(odp_dict.keys()):
            print(f"{litera}) {odp_dict[litera]}")
        wybór = input("Wybierz A/B/C/D: ").upper()
        if wybór in odp_dict and odp_dict[wybór] == p["poprawna"]:
            print("🤪Dobrze!")
            wynik += 1
        else:
            print("😧Źle! Poprawna to:", p["poprawna"])
    print(f"\nTwój wynik: {wynik}/5")
    return wynik

wyniki = wczytaj_wyniki()

while True:
    print("\n--- Witaj w quizie! Wybierz bajkę: ---")
    print("1. Kubuś Puchatek")
    print("2. Czerwony Kapturek")
    print("3. Król Lew")
    print("4. Zapisz i zakończ")
    print("5. Usuń wyniki i zacznij od nowa")

    wybór = input("Wybór (1-5): ")

    if wybór == "1":
        wynik = uruchom_quiz("Kubuś Puchatek")
        wyniki["Kubuś Puchatek"] = wynik
    elif wybór == "2":
        wynik = uruchom_quiz("Czerwony Kapturek")
        wyniki["Czerwony Kapturek"] = wynik
    elif wybór == "3":
        wynik = uruchom_quiz("Król Lew")
        wyniki["Król Lew"] = wynik
    elif wybór == "4":
        zapisz_wyniki(wyniki)
        break
    elif wybór == "5":
        wyniki = {}
        print("🧹 Wyniki usunięte.🧹")
    else:
        print("🙄Nieprawidłowy wybór.😕")
