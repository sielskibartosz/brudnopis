import json

# Przykładowy słownik
slownik = {
    "imie": True,
    "wiek": None,
    "miasto": "Warszawa",
    "zainteresowania": ["programowanie", "muzyka", "sport"]
}

# Zapis do pliku JSON
with open("dane.json", "w", encoding="utf-8") as plik:
    json.dump(slownik, plik, ensure_ascii=False, indent=4)
    # json.dump(slownik, plik,indent=4)

with open("dane.json", "r") as file:
    data = json.load(file)

print(data)