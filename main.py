from dotenv import load_dotenv
import os
import requests

load_dotenv()

GENDER = 'MALE'
WEIGHT_KG = 90
HEIGHT_CM = 176.00
AGE = 35

API_KEY = os.environ.get('API_KEY')
APP_ID = os.environ.get('APP_ID')
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input('What exercises have you done today?: ')

header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}


parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=URL, json=parameters, headers=header)
result = response.json()
print(result)