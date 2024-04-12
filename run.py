import json
import getpass
import os
import time


def cadastro_usuario():
    """
    Function to register a user in the system and save it in the file
    usuarios.json with the name and password of the user.
    """
    senha = ""

    while True:
        name = input("How you want to be called?\n")

        try:
            with open('usuarios.json', 'r') as arquivo:
                usuarios = json.load(arquivo)
        except json.decoder.JSONDecodeError:
            usuarios = []

        name_registered = False
        for user in usuarios:
            if user["name"] == name:
                print("Name already registered")
                name_registered = True
                break

        if not name_registered:
            senha = getpass.getpass("Choose a password with 6 digits:\n")
            if (name == senha or name == "" or len(senha) != 6 or
                    senha.strip() == ""):
                print("Invalid name or password")
            else:
                clear()
                print(f"Thank you {name}! " +
                      "Registration successfully Completed!")
                usuarios.append({"name": name, "password": senha})
                with open('usuarios.json', 'w') as arquivo:
                    json.dump(usuarios, arquivo)
                return_menu()
                break


def return_menu():
    """
    Function to return to the main menu, login or exit the system.
    """
    print("1 - Return to the menu")
    print("2 - Login")
    print("3 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        main()
    elif option == "2":
        login()
    elif option == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid option")
        return_menu()


def login():
    """
    Function to login the user in the system and
    check if the name and password are correct.
    """
    with open('usuarios.json', 'r') as arquivo:
        try:
            usuario = json.load(arquivo)
        except json.decoder.JSONDecodeError:
            print("No user registered yet")
            return
    name = input("Enter your name: ")
    password = getpass.getpass("Enter your password: ")
    for user in usuario:
        if user["name"] == name and user["password"] == password:
            print("Login successfully completed!")
            import weather
            weather.main()
            return
    print("Invalid name or password")
    login()


def clear():
    """
    Function to clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Function to show the main menu of the system and
    call the functions to register, login or exit the system.
    """
    clear()
    print("Welcome to Real-Time Weather Forecast")
    print("1 - Register")
    print("2 - Login")
    print("3 - Exit")
    input_user = input("Choose an option: ")
    if input_user == "1":
        cadastro_usuario()
    elif input_user == "2":
        login()
    elif input_user == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid option")
        time.sleep(1)
        main()


main()
