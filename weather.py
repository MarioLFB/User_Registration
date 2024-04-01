import requests
import datetime

API_KEY = "ea0e21b47d3e60fce3ad43dc7ae01db5"

def options():
    print("1 - Check the weather")
    print("2 - Check the temperature")
    print("3 - Check the sunrise and sunset times")
    print("4 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        city = input("Enter the city: ")
        weather(get_weather_data(city))
    elif option == "2":
        city = input("Enter the city: ")
        temperature(get_weather_data(city))
    elif option == "3":
        city = input("Enter the city: ")
        sunrise_sunset(get_weather_data(city))
    elif option == "4":
        exit()
    else:
        print("Invalid option")
        options()

def get_weather_data(city):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    requisicao = requests.get(link)
    if requisicao.status_code != 200:
        print("City not found")
        options()
    return requisicao.json()


def format_unix_time(unix_time): # Função para formatar o tempo unix
    return datetime.datetime.fromtimestamp(unix_time).strftime('%H:%M')

def sunrise_sunset(data):
    city = data['name']
    sunrise_time = format_unix_time(data['sys']['sunrise'])
    sunset_time = format_unix_time(data['sys']['sunset'])
    print(f"In {city}, the sunrise time is {sunrise_time} and the sunset time is {sunset_time}.")
    return_menu()
    
def weather(data):
    city = data['name']
    print(f"The sky in {city}  is all like {data['weather'][0]['description']}")
    return_menu()

def temperature(data):
    city = data['name']
    print(f"Dude, it's like {data['main']['temp'] - 273.15:.0f}°C in {city} right now.")
    print(f"Yo, it's hitting up to {data['main']['temp_max'] - 273.15:.0f}°C as high and dipping down to {data['main']['temp_min'] - 273.15:.0f}°C as low in {city} right now.")
    print(f"And guess what? It feels like {data['main']['feels_like'] - 273.15:.0f}°C in {city}, man.")
    return_menu()




def return_menu(): # funcao criada para retornar ao menu principal ou sair do programa
    print("1 - Return to the menu")
    print("2 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        options()
    elif option == "2":
        exit()
    else:
        print("Invalid option")
        return_menu()


def main():
    options()

