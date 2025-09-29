def numero_par_impar(num):

    result = ""
    if isinstance(num,(int,float)):
        if num%2==0:
            result = "Par"
        else:
            result= "Impar"
    else:
        result = "Caracter Invalido"
    
    return result

print(numero_par_impar(3))
print(numero_par_impar(""))
print(numero_par_impar(2))