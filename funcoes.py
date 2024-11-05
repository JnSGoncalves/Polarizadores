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





