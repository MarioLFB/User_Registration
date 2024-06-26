import requests
import datetime
import os
import time

API_KEY = "ea0e21b47d3e60fce3ad43dc7ae01db5"


def options():
    """
    Display the options to the user and call the
    functions to check the weather, temperature,
    sunrise and sunset times or exit the program.
    """
    time.sleep(1)
    clear_terminal()
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
        print("Goodbye!")
        exit()
    else:
        print("Invalid option")
        options()


def get_weather_data(city):
    """
    Function to get the weather data from the city entered by the user.
    """
    link = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&"
        f"appid={API_KEY}"
    )
    requisicao = requests.get(link)
    if requisicao.status_code != 200:
        print("City not found")
        options()
    return requisicao.json()


def format_unix_time(unix_time):
    """
    Function to format the time in unix
    format to a more readable format.
    """
    return datetime.datetime.fromtimestamp(unix_time).strftime('%H:%M')


def sunrise_sunset(data):
    """
    Function to show the sunrise and sunset
    times of the city entered by the user.
    """
    city = data['name']
    sunrise_time = format_unix_time(data['sys']['sunrise'])
    sunset_time = format_unix_time(data['sys']['sunset'])
    print(f"In {city}, the sunrise time is {sunrise_time} " +
          f"and the sunset time is {sunset_time}.")
    return_menu()


def weather(data):
    """
    Function to show the weather of the city entered by the user.
    """
    city = data['name']
    print(f"The sky in {city} is all like "
          f"{data['weather'][0]['description']}")
    return_menu()


def temperature(data):
    """
    Function to show the temperature of the city entered by the user.
    """
    city = data['name']
    print(f"Dude, it's like {data['main']['temp'] - 273.15:.0f}°C " +
          f"in {city} right now.")
    print(f"It's hitting up to {data['main']['temp_max'] - 273.15:.0f}°C and "
          f"falling to {data['main']['temp_min'] - 273.15:.0f}°C in {city}.")
    print(f"It feels like {data['main']['feels_like'] - 273.15:.0f}°C " +
          f"in {city}.")
    return_menu()


def return_menu():
    """
    Function to return to the main menu or exit the system.
    """
    print("1 - Return to the menu")
    print("2 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        options()
    elif option == "2":
        print("Goodbye!")
        exit()
    else:
        print("Invalid option")
        return_menu()


def clear_terminal():
    """
    Function to clear the terminal screen.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Function to call the options function.
    """
    options()
