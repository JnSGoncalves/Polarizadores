import math

def tresPolarizadores(posIni, intensidade, an1, an2, an3):
    if (posIni == 0):
        resul1 = (intensidade / 2)
        resul2 = resul2 * (math.cos(math.radians(an2-an1))**2)
        resulFinal = resul2 * (math.cos(math.radians(an3-(an2+an1)))**2)
        return resul1, resul2, resulFinal

    elif(posIni == 1):
        resul1 = (intensidade * 2)
        resul2 = resul2 * (math.cos(math.radians(an2-an1))**2)
        resulFinal = resul2 * (math.cos(math.radians(an3-(an2+an1)))**2)
        return resul1, resul2, resulFinal

    elif(posIni == 2):
        resul2 = intensidade / (math.cos(math.radians(an2-an1))**2)
        resul1 = resul2 * 2
        resulFinal = intensidade * (math.cos(math.radians(an3-(an2+an1)))**2)
        return resul1, resul2, resulFinal

    elif(posIni == 3):
        resulFinal = intensidade / (math.cos(math.radians(an3-(an2+an1)))**2)
        resul2 = resulFinal / (math.cos(math.radians(an2-an1))**2)
        resul1 = resul2 * 2
        return resul1, resul2, resulFinal

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

