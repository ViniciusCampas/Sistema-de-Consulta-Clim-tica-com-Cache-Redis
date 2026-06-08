import requests
import redis
import json
import os

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

cidade = "Sao Paulo"

API_KEY = ''

cache = r.get(cidade)

if cache:
    print("Dados vindos do Redis")
    print(json.loads(cache))

else:
    try:
        print("Consultando API...")

        url = (
            f"https://weather.visualcrossing.com/"
            f"VisualCrossingWebServices/rest/services/"
            f"timeline/{cidade}?key={API_KEY}"
        )

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Erro ao consultar API")
            exit()

        clima = response.json()

        temperatura = {
            "cidade": cidade,
            "dia": clima["days"][0]["datetime"],
            "tempMax": clima["days"][0]["tempmax"],
            "tempMin": clima["days"][0]["tempmin"],
            "temperatura": clima["days"][0]["temp"],
            "umidade": clima["days"][0]["humidity"],
            "condicao": clima["days"][0]["conditions"]
        }

        r.set(
            cidade,
            json.dumps(temperatura),
            ex=43200
        )

        print(temperatura)

    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")