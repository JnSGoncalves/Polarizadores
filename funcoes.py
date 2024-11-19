from math import cos, radians

def tresPolarizadores(posIni, intensidade, an1, an2, an3):
    if (posIni == 0):
        resul1 = (intensidade / 2)
        resul2 = resul1 * (cos(radians(an2-an1)))**2
        resulFinal = resul2 * (cos(radians(an3-an2)))**2
        return resul1, resul2, resulFinal

    elif(posIni == 1):
        resul1 = (intensidade * 2)
        resul2 = intensidade * cos(radians(an2-an1))**2
        resulFinal = resul2 * cos(radians(an3-an2))**2
        return resul1, resul2, resulFinal

    elif(posIni == 2):
        resul2 = intensidade / cos(radians(an2-an1))**2
        resul1 = resul2 * 2
        resulFinal = intensidade * cos(radians(an3-an2))**2
        return resul1, resul2, resulFinal

    elif(posIni == 3):
        resulFinal = intensidade / cos(radians(an3-an2))**2
        resul2 = resulFinal / cos(radians(an2-an1))**2
        resul1 = resul2 * 2
        return resul1, resul2, resulFinal

def doisPolarizadores(posInicial, intensidade, ang1, ang2):
    if(posInicial == 0):
        i2 = (intensidade / 2)
        i3 = i2 * cos(radians(ang2 - ang1))**2
        return i2, i3 
    elif (posInicial == 1):
        i1 = intensidade * 2
        i3 = intensidade * cos(radians(ang2 - ang1))**2
        return i1, i3
    elif (posInicial == 2):
        i2 = intensidade / cos(radians(ang1 - ang2))**2
        i1 = i2 * 2
        return i1, i2

def tresPolarizadoresPolarizados(intensidade, an1, an2, an3):
    i1 = intensidade * cos(radians(an1))**2
    i2 = i1 * cos(radians(an2 - an1))**2
    i3 = i2 * cos(radians(an3 - an2))**2
    return i1, i2, i3

def doisPolarizadoresPolarizados(intensidade, ang1, ang2):
    i1 = intensidade * cos(radians(ang1))**2
    i2 = i1 * cos(radians(ang2 - ang1))**2
    return i1, i2
