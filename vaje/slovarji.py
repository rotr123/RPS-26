
#mini vaja 1
avto = {
    "znamka": "BMW",
    "model": 540,
    "letnik": "2023"
}

avto["barva"]="črna"
# print(f"znamka:{avto["znamka"]}")
# print(f"model:{avto["model"]}")
# print(f"letnik:{avto["letnik"]}")

#mini vaja 2
sola = {
    "ime": "ŠC Kranj",
    "naslov": {
        "ulica": "Kidričeva cesta 55",
        "posta": 4000,
        "kraj": "Kranj"
    },
    "smeri": ["računalništvo", "elektrotehnika", "mehatronika"]
}

for vrednost in sola["smeri"]:
    print(vrednost)



#mini vaja 3
import requests

url = "https://api.open-meteo.com/v1/forecast"
parametri = {
    "latitude": 500,
    "longitude": 14.5058,
    "current": "temperature_2m,wind_speed_10m"
}

odgovor = requests.get(url, params=parametri)

print(odgovor.status_code)
podatki = odgovor.json()     


temperatura = podatki["current"]["temperature_2m"]
enota = podatki["current_units"]["temperature_2m"]
hitrost = podatki["current"]["wind_speed_10m"]
enota1 = podatki["current_units"]["wind_speed_10m"]
print(f"Temperatura v Ljubljani je trenutno {temperatura} {enota},hitrost vetra pa {hitrost}{enota1} ")

#mini vaja 4
def trenutna_temperatura(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    parametri = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    odgovor = requests.get(url, params=parametri)
    podatki = odgovor.json()
    return podatki["current"]["temperature_2m"]


kraji = {
    "Ljubljana": (46.0569, 14.5058),
    "Maribor": (46.5547, 15.6459),
}

for ime, (lat, lon) in kraji.items():
    t = trenutna_temperatura(lat, lon)
    print(f"{ime}: {t} °C")
