from funcoes import *

print("""Autores:

Jônatas da Silva Gonçalves.
Wallace dos Santos Izidoro.
Pedro Henrique da Fonseca do Nascimento.
Vinícius do Nascimento Generoso.\n""")

print('''
Descrição do Programa
Este programa, desenvolvido em Python, tem como objetivo o estudo da polarização da luz, 
utilizando os conceitos fundamentais da óptica moderna. Ele permite calcular a intensidade 
da luz após atravessar até três polarizadores em diferentes ângulos, considerando a 
aplicação da Lei de Malus. A luz incidente é inicialmente não polarizada, e a orientação 
dos ângulos dos polarizadores é definida em relação à vertical.
      
Conceitos Físicos Envolvidos
Polarização da luz: Fenômeno onde a direção de oscilação do campo elétrico é restringida a um único plano.
Lei de Malus: Define como a intensidade da luz varia em função do ângulo entre os polarizadores:
I = Io * cos²(o).
Luz não polarizada: Antes de passar pelo primeiro polarizador, a intensidade é reduzida pela metade devido 
à ausência de orientação preferencial dos campos elétricos.
      
Limitações do Programa
O programa realiza cálculos baseados exclusivamente na Lei de Malus. Para situações mais complexas, como 
interferências ou efeitos de difração, cálculos adicionais são necessários.
Requer que o usuário compreenda os conceitos físicos para interpretar os resultados corretamente.
''')

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
print()


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
        intensidade = float(input("Digite a intensidade em w/cm²: "))
        ang1 = float(input("Digite o 1º ângulo em graus: "))
        ang2 = float(input("Digite o 2º ângulo em graus: "))

        if(posInicial != 1 or posInicial != 2 or posInicial != 3):
            saida1, saida2 = doisPolarizadores(posInicial, intensidade, ang1, ang2)
            saida1Cientifica = f"{saida1:.4e}"  
            saida2Cientifica = f"{saida2:.4e}"  
            intensidadeCientifica = f"{intensidade:.4e}"
        else:
            print("Entrada inválida.")
            print()
            continue
        print()

        if(posInicial == 0):
            saida1Po, saida2Po = doisPolarizadoresPolarizados(intensidade, ang1, ang2)
            saida1PoCientifica = f"{saida1Po:.4e}"
            saida2PoCientifica = f"{saida2Po:.4e}"
            print("Para luz não polarizada:")
            print("Intensidade no momento 0 (I0) = ", intensidadeCientifica + " [w/cm²]")
            print("Intensidade no momento 1 (I1) = ", saida1Cientifica + " [w/cm²]")
            print("Intensidade no momento 2 (I2) = ", saida2Cientifica + " [w/cm²]")
            print()
            print("Para luz polarizada:")
            print("Intensidade no momento 0 (I0) = ", intensidadeCientifica + " [w/cm²]")
            print("Intensidade no momento 1 (I1) = ", saida1PoCientifica + " [w/cm²]")
            print("Intensidade no momento 2 (I2) = ", saida2PoCientifica + " [w/cm²]")
        elif(posInicial == 1):
            print("Intensidade no momento 0 (I0) = ", saida1Cientifica + " [w/cm²]")
            print("Intensidade no momento 1 (I1) = ", intensidadeCientifica + " [w/cm²]")
            print("Intensidade no momento 3 (I2) = ", saida2Cientifica + " [w/cm²]")
        elif(posInicial == 2):
            print("Intensidade no momento 0 (I0) = ", saida1Cientifica + " [w/cm²]")
            print("Intensidade no momento 1 (I1) = ", saida2Cientifica + " [w/cm²]")
            print("Intensidade no momento 2 (I2) = ", intensidadeCientifica + " [w/cm²]")
        print()

    elif(opcao == "2"):
        posInicial = int(input("Qual a posicão inicial? (I0, I1, I2 ou I3 - Digite somento o número): "))
        intensidade = float(input("Digite a intencidade em w/cm²: "))
        ang1 = float(input("Digite o 1º ângulo em graus: "))
        ang2 = float(input("Digite o 2º ângulo em graus: "))
        ang3 = float(input("Digite o 3º ângulo em graus: "))
        print()

        if(posInicial != 1 or posInicial != 2 or posInicial != 3 or posInicial != 4):
            saida1, saida2, saida3 = tresPolarizadores(posInicial, intensidade, ang1, ang2, ang3)
            saida1Cientifica = f"{saida1:.4e}"
            saida2Cientifica = f"{saida2:.4e}"
            saida3Cientifica = f"{saida3:.4e}"
            intensidadeCientifica = f"{intensidade:.4e}"
        else:
            print("Entrada inválida.")
            print()
            continue

        if(posInicial == 0):
            saida1Po, saida2Po, saida3Po = tresPolarizadoresPolarizados(intensidade,
                                            ang1, ang2, ang3)
            saida1PoCientifica = f"{saida1Po:.4e}"
            saida2PoCientifica = f"{saida2Po:.4e}"
            saida3PoCientifica = f"{saida3Po:.4e}"
            print("Para luz não polarizada:")
            print("Intensidade no momento 0 (I0) = ", intensidadeCientifica + " [w/cm²]")
            print("Intensidade no momento 1 (I1) = ", saida1Cientifica + " [w/cm²]")
            print("Intensidade no momento 2 (I2) = ", saida2Cientifica + " [w/cm²]")
            print("Intensidade no momento 3 (I3) = ", saida3Cientifica + " [w/cm²]")
            print()
            print("Para luz polarizada: ")
            print("Intensidade no momento 0 (I0) = ", intensidadeCientifica + " [w/cm²]")
            print("Intensidade no momento 1 (I1) = ", saida1PoCientifica + " [w/cm²]")
            print("Intensidade no momento 2 (I2) = ", saida2PoCientifica + " [w/cm²]")
            print("Intensidade no momento 3 (I3) = ", saida3PoCientifica + " [w/cm²]")
        elif(posInicial == 1):
            print("Intensidade no momento 0 (I0) = ", saida1Cientifica + " [w/cm²]")
            print("Intensidade no momento 1 (I1) = ", intensidadeCientifica + " [w/cm²]")
            print("Intensidade no momento 2 (I2) = ", saida2Cientifica + " [w/cm²]")
            print("Intensidade no momento 3 (I3) = ", saida3Cientifica + " [w/cm²]")
        elif(posInicial == 2):
            print("Intensidade no momento 0 (I0) = ", saida1Cientifica + " [w/cm²]")
            print("Intensidade no momento 1 (I1) = ", saida2Cientifica + " [w/cm²]")
            print("Intensidade no momento 2 (I2) = ", intensidadeCientifica + " [w/cm²]")
            print("Intensidade no momento 3 (I3) = ", saida3Cientifica + " [w/cm²]")
        elif(posInicial == 3):
            print("Intensidade no momento 0 (I0) = ", saida1Cientifica + " [w/cm²]")
            print("Intensidade no momento 1 (I1) = ", saida2Cientifica + " [w/cm²]")
            print("Intensidade no momento 2 (I2) = ", saida3Cientifica + " [w/cm²]")
            print("Intensidade no momento 3 (I3) = ", intensidadeCientifica + " [w/cm²]")
        print()

    elif(opcao == "0"):
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        print()

