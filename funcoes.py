from math import cos, sqrt

def doisPolarizadores(posInicial, intensidade, ang1, ang2):
    if(posInicial == 1):
        i2 = intensidade / 2
        i3 = i2 * cos(ang2)**2
        return i2, i3 
    elif (posInicial == 2):
        i1 = intensidade * 2
        i3 = intensidade * cos(ang2 - ang1)**2
        return i1, i3
    elif (posInicial == 3):
        i2 = intensidade / cos(ang1 - ang2)**2
        i1 = i2 * 2
        return i1, i2