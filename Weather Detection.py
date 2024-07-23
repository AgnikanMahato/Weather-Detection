import requests, json

def weather_report(city_name):
    api_key = "a8d9c2b3fa11c2ea2735ac6090943d30"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    complete_url = f"{base_url}?q={city_name}&appid={api_key}"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_desc = data["weather"][0]["description"]

        print("Temperature : " +
              str(temperature) +
              "\nHumidity : " +
              str(humidity) +
              "\nDescription : " +
              str(weather_desc))
    else:
        print("City Not Found!")

city_name = input("Enter city name : ")
weather_report(city_name)