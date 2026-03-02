import requests
from datetime import date

url = "http://127.0.0.1:5000/add"

my_session_daa = {
    "date": str(date.today()),
    "duration_minutes": 120,
    "energy_level": 9
}

response = requests.post(url, json=my_session_daa)
print(response.json())