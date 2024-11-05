from math import radians
from funcoes import *

intensidadeInicial = float(input("Digite a Intensidade incial: "))
posInicial = int(input("Digite qual a posição da intensidade dada (I1, I2, I3): "))
ang1 = float(input("Digite o angulo do primeiro polarizador (θ°): "))
ang2 = float(input("Digite o angulo do segundo polarizador (θ°): "))

ang1 = radians(ang1)
ang2 = radians(ang2)

saida1, saida2 = doisPolarizadores(posInicial, intensidadeInicial, ang1, ang2)
print(saida1, saida2)
