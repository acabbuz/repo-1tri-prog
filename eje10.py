# def hora_mayor():
#     result = ""
#     print("Acontinuación introduzca los datos para la primera hora")
#     h1 = int(input("Introduce una hora entre 0-23>: "))
#     m1 = int(input("Introduce unos mins entre 0-59>: "))
#     s1 = int(input("Introduce unos segundos entre 0-59>: "))

#     print("Acontinuación introduzca los datos para la segunda hora")
#     m2 = int(input("Introduce unos mins entre 0-59>: "))
#     h2 = int(input("Introduce una hora entre 0-23>: "))
#     s2 = int(input("Introduce unos segundos entre 0-59>: "))
    
#     if h1 > h2:
#         result = "La primera hora es mayor"
#     elif h1 < h2:
#         result = "La segunda hora es mayor"

#     else:  
#         if m1 > m2:
#             result = "La primera hora es mayor"
#         elif m1 < m2:
#             result = "La segunda hora es mayor"
#         else:  
#             if s1 > s2:
#                 result = "La primera hora es mayor"
#             elif s1 < s2:
#                 result = "La segunda hora es mayor"
#             else:
#                 result = "Son iguales"
#     return result


# print(hora_mayor())


def calcular_hora_mayor():
    result = ""
    print("Acontinuación introduzca los datos para la primera hora")
    h1 = int(input("Introduce una hora entre 0-23>: "))
    m1 = int(input("Introduce unos mins entre 0-59>: "))
    s1 = int(input("Introduce unos segundos entre 0-59>: "))

    print("Acontinuación introduzca los datos para la segunda hora")
    m2 = int(input("Introduce unos mins entre 0-59>: "))
    h2 = int(input("Introduce una hora entre 0-23>: "))
    s2 = int(input("Introduce unos segundos entre 0-59>: "))

    if (0<=h1<=23 and 0<=m1<=59 and 0<=s1<=59 ) and (0<=h2<=23 and 0<=m2<=59 and 0<=s2<=59 ):

        hora1 = (h1*3060) + (m1*60) + (s1)
        hora2 = (h2*3060) + (m2*60) + (s2)
        
        if hora1 > hora2:
            result = "La primera Hora es mayor"
        elif hora1 < hora2:
            result = "La segunda es mayor"
        else:
            result = "Son iguales"

    else:
        result = "Datos Inválidos"

    return result
    
print(calcular_hora_mayor())
