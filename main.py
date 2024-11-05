print("""Autores:

Jônatas da Silva Gonçalves.
Wallace dos Santos Izidoro.
Pedro Henrique da Fonseca do Nascimento.
Vinícius do Nascimento Generoso.\n""")

print("Calculadora Ótica-python\n")

print("Caso deseje entrar com valores em notação científica, utilize o formato abaixo:")
print("1.23 x 10^4 --> 1.23e4\n")


while True:
    print("Menu: ")
    print("1 - Dados com duas entradas: ")
    print("2 - Dados com três entradas: ")
    print("0 - Sair")
    print()

    opcao = str(input("Digite o número da opção desejada: "))
    print()
    
    if(opcao == "1"):
        posInicial = int(input("Digite o valor da posicão inicial: "))
        intensidade = float(input("Digite a intencidade: "))
        ang1 = float(input("Digite o primeiro ângulo: "))
        ang2 = float(input("Digite o segundo ângulo: "))
        print()

    elif(opcao == "2"):
        posInicial = int(input("Digite o valor da posicão inicial: "))
        intensidade = float(input("Digite a intencidade: "))
        ang1 = float(input("Digite o primeiro ângulo: "))
        ang2 = float(input("Digite o segundo ângulo: "))
        ang3 = float(input("Digite o terceiro ângulo: "))
        print()

    elif(opcao == "0"):
        print("Saindo...")
        break

