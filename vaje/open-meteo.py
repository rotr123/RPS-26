import requests
url="https://api.open-meteo.com/v1/forecast?latitude=46.0511&longitude=14.5051&current=temperature_2m&forecast_days=1"

klic=requests.get(url)

klicJSON=klic.json()

print(klicJSON["latitude"])