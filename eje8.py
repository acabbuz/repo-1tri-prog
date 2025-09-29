# def descuentos_segun_estado_edad(caracter, edad):
#     estado_cv = ["S", "C", "V", "D"]
#     result = ""
#     if caracter not in estado_cv or edad<0:
#         result = "Caracter invalido o edad invalida"
#     else:
#         if edad>50:
#             result = f"Para los {caracter} con la edad {edad}, se le aplicara un porcentaje de 8.5%"
#         elif caracter=="S" or caracter=="D" and edad<=35:
#             result =f"Para los {caracter} con la edad {edad}, se le aplicara un porcentaje de 12%"
#         elif caracter=="V" or caracter=="C " and edad<=35:
#             result =f"Para los {caracter} con la edad {edad}, se le aplicara un porcentaje de 11.3%"          
#         else:
#             result =f"Para los {caracter} con la edad {edad}, se le aplicara un porcentaje de 10.5%"          
#     return result
# print(descuentos_segun_estado_edad("S",20))
# print(descuentos_segun_estado_edad("D",50))
# print(descuentos_segun_estado_edad("S",20))
# print(descuentos_segun_estado_edad("V",20))
# print(descuentos_segun_estado_edad("",-10))

def descuentos_segun_estado_edad_condicionales(caracter, edad):
    result  =""
    if (caracter.upper() == "S" or caracter.upper() == "C" or caracter.upper() == "V" or caracter.upper() == "D") and 0<edad:
        if edad>50:
            result = f"Para los {caracter} con la edad {edad}, se le aplicara un porcentaje de 8.5%"
        elif caracter.upper()=="S" or caracter.upper()=="D" and edad<=35:
            result =f"Para los {caracter} con la edad {edad}, se le aplicara un porcentaje de 12%"
        elif caracter.upper()=="V" or caracter.upper()=="C " and edad<=35:
            result =f"Para los {caracter} con la edad {edad}, se le aplicara un porcentaje de 11.3%"
            
        else:
            result =f"Para los {caracter} con la edad {edad}, se le aplicara un porcentaje de 10.5%"
    else:
        result = "Caracter invalido o edad invalida"

    return result


print(descuentos_segun_estado_edad_condicionales("s",20))
print(descuentos_segun_estado_edad_condicionales("d",50))
print(descuentos_segun_estado_edad_condicionales("s",20))
print(descuentos_segun_estado_edad_condicionales("v",20))
print(descuentos_segun_estado_edad_condicionales("",-10))
print(descuentos_segun_estado_edad_condicionales("d",0))