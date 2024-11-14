from funcoes import *

print("""Autores:

Jônatas da Silva Gonçalves.
Wallace dos Santos Izidoro.
Pedro Henrique da Fonseca do Nascimento.
Vinícius do Nascimento Generoso.\n""")

print("Calculadora Ótica-python\n")
print()
print("Caso deseje entrar com valores em notação científica, utilize o formato abaixo:")
print("1.23 x 10^4 --> 1.23e4\n")
print()

print("Atenção para posição inicial.")
print("Digite 0 -> caso não tenha incidido nenhum polarizador")
print("Digite 1. Se incidiu apenas 1 polarizador")
print("Digite 2. Caso tenha incindido em 2 polarizadores")
print("Assim, sucessivamente.")


while True:
    print("Menu: ")
    print("1 - Dados com duas entradas: ")
    print("2 - Dados com três entradas: ")
    print("0 - Sair")
    print()

    opcao = str(input("Digite o número da opção desejada: "))
    print()
    
    if(opcao == "1"):
        posInicial = int(input("Qual a posicão inicial? (I0, I1 ou I2 - Digite somento o número): "))
        intensidade = float(input("Digite a intensidade: "))
        ang1 = float(input("Digite o primeiro ângulo em graus: "))
        ang2 = float(input("Digite o segundo ângulo em graus: "))

        if(posInicial != 1 or posInicial != 2 or posInicial != 3):
            saida1, saida2 = doisPolarizadores(posInicial, intensidade, ang1, ang2)
        else:
            print("Entrada inválida.")
            print()
            continue
        print()

        if(posInicial == 0):
            print("Intensidade no momento 0 (I0) = ", intensidade)
            print("Intensidade no momento 1 (I1) = ", saida1)
            print("Intensidade no momento 2 (I2) = ", saida2)
        elif(posInicial == 1):
            print("Intensidade no momento 0 (I0) = ", saida1)
            print("Intensidade no momento 1 (I1) = ", intensidade)
            print("Intensidade no momento 3 (I2) = ", saida2)
        elif(posInicial == 2):
            print("Intensidade no momento 0 (I0) = ", saida1)
            print("Intensidade no momento 1 (I1) = ", saida2)
            print("Intensidade no momento 2 (I2) = ", intensidade)
        print()

    elif(opcao == "2"):
        posInicial = int(input("Qual a posicão inicial? (I0, I1, I2 ou I3 - Digite somento o número): "))
        intensidade = float(input("Digite a intencidade: "))
        ang1 = float(input("Digite o primeiro ângulo: "))
        ang2 = float(input("Digite o segundo ângulo: "))
        ang3 = float(input("Digite o terceiro ângulo: "))
        print()

        if(posInicial != 1 or posInicial != 2 or posInicial != 3 or posInicial != 4):
            saida1, saida2, saida3 = tresPolarizadores(posInicial, intensidade, ang1, ang2, ang3)
        else:
            print("Entrada inválida.")
            print()
            continue

        if(posInicial == 0):
            print("Intensidade no momento 0 (I0) = ", intensidade)
            print("Intensidade no momento 1 (I1) = ", saida1)
            print("Intensidade no momento 2 (I2) = ", saida2)
            print("Intensidade no momento 3 (I3) = ", saida3)
        elif(posInicial == 1):
            print("Intensidade no momento 0 (I0) = ", saida1)
            print("Intensidade no momento 1 (I1) = ", intensidade)
            print("Intensidade no momento 2 (I2) = ", saida2)
            print("Intensidade no momento 3 (I3) = ", saida3)
        elif(posInicial == 2):
            print("Intensidade no momento 0 (I0) = ", saida1)
            print("Intensidade no momento 1 (I1) = ", saida2)
            print("Intensidade no momento 2 (I2) = ", intensidade)
            print("Intensidade no momento 3 (I3) = ", saida3)
        elif(posInicial == 3):
            print("Intensidade no momento 0 (I0) = ", saida1)
            print("Intensidade no momento 1 (I1) = ", saida2)
            print("Intensidade no momento 2 (I2) = ", saida3)
            print("Intensidade no momento 3 (I3) = ", intensidade)
        print()


    elif(opcao == "0"):
        print("Saindo...")
        break
