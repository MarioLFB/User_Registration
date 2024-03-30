import json
import getpass

def cadastro_usuario():
    senha = "" # Cria a variável senha com conteúdo vazio
    while True: # Loop infinito
        name = input("How you want to be called?\n")

        try:
            with open('usuarios.json', 'r') as arquivo: # Abre o arquivo no modo leitura R de read e salva na variável arquivo
                usuarios = json.load(arquivo) # Cria a variavel Usuarios, que recebe o conteúdo do da variavel arquivo, usando o método json.load
        except json.decoder.JSONDecodeError: # O erro json.decoder.JSONDecodeError: ocorre quando o arquivo está vazio ou nao esta no formato json valido.
            usuarios = [] # Caso ocorra o erro, a variável usuarios recebe uma lista vazia

        name_registered = False # Cria a variável name_registered com conteúdo False a ser usado mais tarde
        for user in usuarios: #loop para percorrer todos os usuários cadastrados
            if user["name"] == name: # se o user dentro do arquivo usuarios for igual ao nome digitado segue o bloco de código
                print("Name already registered") # apresenta a mensagem "Name already registered"
                name_registered = True # seguindo o bloco de código, a variável name_registered recebe True
                break
        
        if not name_registered: # se a variável name_registered for False, segue o bloco de código
            senha = getpass.getpass("Choose a password with 6 digits:\n") # Pede para o usuário digitar a senha e salva na variável senha
            if name == senha or name == "" or len(senha) != 6 or senha.strip() == "": # Cria a condicional para verificar se o nome é igual a senha, se o nome é vazio, se o tamanho da senha é diferente de 6 ou se a senha é vazia
                print("Invalid name or password")
            else:
                print(f"Thank you {name}! Registration successfully Completed!")
                usuarios.append({"name": name, "password": senha}) # Adiciona a variavel usuarios o dicionário com o nome e senha do usuário
                with open('usuarios.json', 'w') as arquivo: # Abre o arquivo no modo escrita W de write e salva na variável arquivo
                    json.dump(usuarios, arquivo) # 1 usuarios é a variavel de usuários que você que teve append a lista. 2 arquivo representa o arquivo "usuarios.json" dentro dele.
                return_menu() # Chama a função return_menu
                break

def return_menu(): # funcao criada para retornar ao menu principal ou sair do programa
    print("1 - Return to the menu")
    print("2 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        main()
    elif option == "2":
        exit()
    else:
        print("Invalid option")
        return_menu()

def login():
    with open('usuarios.json', 'r') as arquivo: # Abre o arquivo no modo leitura R de read e salva na variável arquivo
        try: #metodo try para tentar executar o código e posteriormente o metodo except para tratar caso ocorra um erro
            usuario = json.load(arquivo) # Cria a variavel usuario, e da load do objeto arquivo para dentro  da variavel usuario.
        except json.decoder.JSONDecodeError: # O erro json.decoder.JSONDecodeError: ocorre quando o arquivo está vazio ou nao esta no formato json valido.
            print("No user registered yet") # Caso ocorra o erro, apresenta a mensagem "No user registered yet"
            return # Retorna para a função login
    name = input("Enter your name: ") # Pede para o usuário digitar o nome e salva na variável name
    password = getpass.getpass("Enter your password: ") # Pede para o usuário digitar a senha e salva na variável senha
    for user in usuario: #O loop 'e necessario para poder checkar TODOS os usuarios cadastrados, sem isso ele nao percorrera todos os usuarios.
        if user["name"] == name and user["password"] == password: # cria a condicional para verificar se o nome e senha digitados pelo usuario sao iguais ao nome e senha cadastrados
            print("Login successfully completed!") # Caso a condicional seja verdadeira, apresenta a mensagem "Login successfully completed!"
            return # Retorna para a função login
    print("Invalid name or password") # Caso a condicional seja falsa, apresenta a mensagem "Invalid name or password"


def main():
    print("Welcome to the system!")
    print("1 - Register")
    print("2 - Login")
    input_user = input("Choose an option: ")
    if input_user == "1":
        cadastro_usuario()
    elif input_user == "2":
        login()
    else:
        print("Invalid option")
        main()

main()