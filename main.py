import requests
import os
from twilio.rest import Client

my_api_key = os.environ.get("OWN_API_KEY")
angela_api_key = "69f04e4613056b159c2761a9d9e664d2"

account_sid = "AC33e1e91b517d52e3b77854647666493e"
auth_token = os.environ.get("YOUR_AUTH_TOKEN")

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 20.959470,
    "lon": 105.605495,
    "appid": angela_api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# weather_hourly = weather_data["hourly"][0]["weather"][0]["id"]
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.☔",
        from_='+12409085743',
        to='+84961902036')
    print(message.status)
else:
    message = client.messages \
        .create(
        body="It's not rain today. Remember to you 😊😒😁",
        from_='+12409085743',
        to='+84961902036')
    print(message.status)
