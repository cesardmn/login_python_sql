from Controller import ControllerCadastro, ControllerLogin


def cadastrar():
    nome = input("\nDigite seu nome\n")
    email = input("\nDigite seu email\n")
    senha = input("\nDigite sua senha\n")
    try:
        ControllerCadastro.cadastrar(nome, email, senha)
        print("\nCadastro realizado com sucesso\n")
    except ValueError as e:
        print("\nErro:", e)


def logar():
    email = input("\nDigite seu email\n")
    senha = input("\nDigite sua senha\n")
    resultado = ControllerLogin.login(email, senha)
    if not resultado:
        print("\nEmail ou senha inválidos\n")
    else:
        print(resultado)


if __name__ == "__main__":
    while True:
        print("\n========== [MENU] ==========")
        decidir = int(
            input("Digite 1 para cadastrar\nDigite 2 para Logar\nDigite 3 para sair\n")
        )

        if decidir == 1:
            cadastrar()
        elif decidir == 2:
            logar()
        else:
            break
