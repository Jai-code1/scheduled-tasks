import requests, os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

OWP_API_KEY = os.environ.get("OWP_API_KEY")
OWP_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = -8.761070
MY_LONG = -63.885979

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=OWP_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

# print(data)

data_list = data["list"]

will_rain = False
for hour_data in data_list:
    weather_code = hour_data["weather"][0]["id"]
    print(weather_code)
    if int(weather_code) < 700:
        # print("umbrella needed")
        will_rain = True

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
    body="It's going to rain today, bring an ☔️",
    from_="whatsapp:+14155238886",
    to="whatsapp:+14435672035",
    )

    print(message.status)
