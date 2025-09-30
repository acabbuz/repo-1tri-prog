# def cobro_llamada(day, time):
#     costo = 0
#     if time > 10 :
#         costo += 10 * 0.66
#         time-=10

#         if time>=3:
#             costo+= 3*0.50
#             time=-3

#             if time>=2:
#                 costo+= 2*0.45
#                 time=-2

#                 if time>0:
#                     costo += time* 0.35

#             else:
#                 costo+=time*0.45
#         else:
#             costo+= time*0.50

#     else: 
#         costo+= time * 0.66

#     return costo
# print(cobro_llamada(2, 9))
# print(cobro_llamada(2, 12))
# print(cobro_llamada(2, 13))


def cobro_llamada(dia, turno, time):
    costo = 0
    
    if time >= 10:
        costo += 10 * 0.66
        time -= 10
    else:
        time * 0.66
    
    if time >= 3:
        costo += 3 * 0.50
        time -= 3
    else:
        costo + time * 0.50
    
    if time >= 2:
        costo += 2 * 0.45
        time -= 2
    else:
        costo + time * 0.45
    
    costo += time * 0.35
    
    
    if dia == "domingo":
        impuesto = costo *0.03
        costo += impuesto
    else:
        if turno == "manana" :
            impuesto = costo *0.15
            costo += impuesto
        else:
            impuesto = costo *0.10
            costo += impuesto

    return costo

print(cobro_llamada("domingo","mañana", 10))   
print(cobro_llamada("lunes","tarde",  12))  
print(cobro_llamada("martes", "manaña", 13))  
print(cobro_llamada("miercoles", "tarde",16))  
