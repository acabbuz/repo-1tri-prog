def etapa_edu(edad):
    result = ""

    if 0<=edad<=6:
        result = "Infantil"
    elif 7<=edad<=11:
        result= "Primaria"
    elif 12<=edad<=16:
        result= "Secundaria Obligatoria"
    else:
        result="Post-Obligatoria"
    
    return result

#Primera Etapa
print(etapa_edu(0))
print(etapa_edu(6))
#Segunda Etapa
print(etapa_edu(7))
print(etapa_edu(11))
#Tercera Etapa
print(etapa_edu(12))
print(etapa_edu(16))
#Cuarta Etapa
print(etapa_edu(17))
print(etapa_edu(21))