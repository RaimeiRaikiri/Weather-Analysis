import requests
import keys
import json
import datetime
import sqlite3

def fetch_data() -> dict | None:
    url = "https://api.openweathermap.org/data/2.5/weather"
    payload = {
        "appid": keys.weather_api,
        "units": "metric",
        "lat": "51.3637768",
        "lon": "0.6122424"
    }
    
    response = requests.get(url, params=payload)
    
    if response.status_code == 200:
        json_response = json.loads(response.content)

        return json_response
    
    else:
        return None
    
def parse_data_for_temperature(data: dict) -> float:
    return float(data["main"]["temp"])

def get_current_date() -> str:
    date = datetime.datetime.now()
    
    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")
    
    return year + "-" + month + "-" + day

def export_data_to_database(parsed_data: float, date: str) -> None:
    connection = sqlite3.connect("/Users/michael/Python/Weather-Analysis/rainham_weather.db")
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO rainham_weather (temperature  ,date) VALUES (?, ?)", (parsed_data, date))
    connection.commit()

data = fetch_data()
parsed_data = parse_data_for_temperature(data)
export_data_to_database(parsed_data ,get_current_date()) 
