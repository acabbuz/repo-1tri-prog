# def dia_senana(num):
#     semana = ["Lunes" , "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
#     result = ""

#     if 1<=num<=7:
#         result = semana[num-1]
#     else:
#         result = "Datos invalidos"
#     return result

# print(dia_senana(1000000))
# print(dia_senana(0))
# print(dia_senana(1))
# print(dia_senana(2))
# print(dia_senana(3))


def dia_semana_simple(day):
    result = ""

    if day == 1:
        result = "Lunes"
    elif day == 2:
        result = "Martes"
    elif day == 3:
        result = "Miercoles"
    elif day ==4:
        result = "Jueves"
    elif day ==5:
        result = "Viernes"
    elif day ==6:
        result = "Sabado"
    elif day ==7:
        result = "Domingo"
    else:
        result = "Día fuera de rango"

    return result

print(dia_semana_simple(2))
print(dia_semana_simple(0))
print(dia_semana_simple(3))
print(dia_semana_simple(4))
print(dia_semana_simple(5))

