def acceso_estudiantes(nota_mates, nota_ing, nota_prog, asistencia):
    result = ""
    promedio  = (nota_mates + nota_ing + nota_prog) // 3
    if promedio >= 85 :
        result = f"Estudiante admitido con beca, promedio: {promedio}" 
    elif 70<=promedio<=84 and asistencia >=75:
        result = f"Estudiante admitido sin beca, promedio: {promedio}"
    elif 60<=promedio<=69 :
        result = f"Estudiante en Lista de espera, promedio: {promedio}"
    else:
        result = f"Estudiante rechazado, promedio: {promedio}"

    return result

print(acceso_estudiantes(87,82,85,80))
print(acceso_estudiantes(90,90,90,80))
print(acceso_estudiantes(90,50,50,80))
print(acceso_estudiantes(87,82,85,74))