import json

# Przykładowy słownik
slownik = {
    "imie": "Jan",
    "wiek": 30,
    "miasto": "Warszawa",
    "zainteresowania": ["programowanie", "muzyka", "sport"]
}

# Zapis do pliku JSON
with open("dane.json", "w", encoding="utf-8") as plik:
    json.dump(slownik, plik, ensure_ascii=False, indent=4)
    # json.dump(slownik, plik,indent=4)

