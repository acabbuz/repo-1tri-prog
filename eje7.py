"""
def es_vocal_bucle(caracter):
    vocales = ["A","E","I","O","U"]
    result = ""
    num = 0

    if caracter in vocales:
        for i in range(len(vocales)):
            if vocales[i] == caracter:
                num= i
                result = f"La vocal {caracter} esta en la posición {str(num+1)}"  
            
    else:
        result = "No es una vocal"

    return result
"""
"""
print(es_vocal("A"))
print(es_vocal("I"))
print(es_vocal("R"))
"""

# def es_vocal_simple(caracter):
#     result = ""
#     vocales = ["A","E","I","O","U"]
#     if caracter in vocales:
#         result = f"El caracter {caracter} esta en la posicion {vocales.index(caracter) + 1} "
#     else:
#         result= "No es una vocal"
#     return result
# print(es_vocal_simple("A"))
# print(es_vocal_simple("I"))
# print(es_vocal_simple("R"))

def es_vocal_condicionales(caracter):
    result = ""
    if caracter.upper() == "A":
        result = f"Tu caracter {caracter} esta en la Primera posición"
    elif caracter.upper() == "E":
        result = f"Tu caracter {caracter} esta en la Segunda posición"
    elif caracter.upper() == "I":
        result = f"Tu caracter {caracter} esta en la Tercera posición"
    elif caracter.upper() == "O":
        result = f"Tu caracter {caracter} esta en la Cuarta posición"
    elif caracter.upper() == "U":
        result = f"Tu caracter {caracter} esta en la Quinta posición"
    else:
        result = "No es una vocal"
    return result

print(es_vocal_condicionales("a"))
print(es_vocal_condicionales("e"))
print(es_vocal_condicionales("i"))
print(es_vocal_condicionales("o"))
print(es_vocal_condicionales("u"))
print(es_vocal_condicionales("w"))










