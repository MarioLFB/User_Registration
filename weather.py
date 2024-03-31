import requests

API_KEY = "ea0e21b47d3e60fce3ad43dc7ae01db5"

def options():
    print("1 - Check the weather")
    print("2 - Check the temperature")
    print("3 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        city = input("Enter the city: ")
        weather(get_weather_data(city))
    elif option == "2":
        city = input("Enter the city: ")
        temperature(get_weather_data(city))
    elif option == "3":
        exit()
    else:
        print("Invalid option")
        options()

def get_weather_data(city):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    requisicao = requests.get(link)
    if requisicao.status_code != 200:
        print("City not found")
        return None
    return requisicao.json()

def weather(data):
    city = data['name']
    print(f"The sky in {city} is {data['weather'][0]['description']}")

def temperature(data):
    city = data['name']
    print(f"The temperature in {city} is {data['main']['temp'] - 273.15:.0f}°C")
    print(f"The feels Like in {city} is {data['main']['feels_like'] - 273.15:.0f}°C")


def main():
    print("Welcome to the weather system!")
    options()

main()

