from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

GENDER = 'MALE'
WEIGHT_KG = 90
HEIGHT_CM = 176.00
AGE = 35

API_KEY = os.environ.get('API_KEY')
APP_ID = os.environ.get('APP_ID')
EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = 'https://api.sheety.co/de9862cff422df325716dc388558dc1d/workoutTracking/workouts'

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

response = requests.post(url=EXERCISE_URL, json=parameters, headers=header)
result = response.json()['exercises']
# print(result)



today = datetime.now()
date = today.strftime('%d/%m/%Y')
hour = f'{today.hour}:{today.minute}:{today.second}'

for index in range(len(result)):
    training_parameters = {
        'workout': {
            'date': date,
            'time': hour,
            'exercise': result[index]['name'].title(),
            'duration': result[index]['duration_min'],
            'calories': result[index]['nf_calories'],
        }
    }
    requests.post(SHEET_URL,json=training_parameters)