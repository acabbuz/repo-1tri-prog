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


# def cobro_llamada1(dia, turno, time):
#     costo = 0
#     if time >= 10:
#         costo += 10 * 0.66
#         time -= 10
#     else:
#         time * 0.66
    
#     if time >= 3:
#         costo += 3 * 0.50
#         time -= 3
#     else:
#         costo + time * 0.50
    
#     if time >= 2:
#         costo += 2 * 0.45
#         time -= 2
#     else:
#         costo + time * 0.45
    
#     costo += time * 0.35
    
#     if dia == "domingo":
#         impuesto = costo *0.03
#         costo += impuesto
#     else:
#         if turno == "manana" :
#             impuesto = costo *0.15
#             costo += impuesto
#         elif turno == "tarde":
#             impuesto = costo *0.10
#             costo += impuesto
#         else:
#             costo = f"Algun dato invalido"

#     return costo

# print(cobro_llamada1("domingo","manana", 13))   
# print(cobro_llamada1("lunes","tarde",  12))  
# print(cobro_llamada1("martes", "manana", 13))  
# print(cobro_llamada1("miercoles", "tarde",16))  
# print(cobro_llamada1("miercoles", "noche",16))  


def cobro_llamada(dia, turno, time):
    costo = 0
    if time >= 10:
        costo += 10 * 0.66
        time -= 10
        if time>=3:
            costo += 3 * 0.50
            time -= 3
            if time >=2:
                costo += 2 * 0.45
                time -= 2
                if time>=1:
                    costo + time * 0.35
                    time -=time
            else:
                  costo + time * 0.45
        else:
            costo + time * 0.50
    else:
     costo += time * 0.66
    
    if dia == "domingo":
        impuesto = costo *0.03
        costo += impuesto
    else:
        if turno == "manana" :
            impuesto = costo *0.15
            costo += impuesto
        elif turno == "tarde":
            impuesto = costo *0.10
            costo += impuesto
        else:
            costo = f"Algun dato invalido"

    return costo

print(cobro_llamada("domingo","manana", 13))     
print(cobro_llamada("lunes","tarde",  12))  
print(cobro_llamada("martes", "manana", 13))  
print(cobro_llamada("miercoles", "tarde",16))  
print(cobro_llamada("miercoles", "noche",16))  