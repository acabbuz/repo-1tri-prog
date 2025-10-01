def comprobar_fecha(day,month,year):

    meses = ["Enero", "Febrero", "Marzo" , "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    result = ""

    if(month == 4 or month == 6 or month == 9 or month==11) and 1<=day<=30:
        result = f"Existe el día {day} de {meses[month-1]}"

    elif (month==1 or month ==3 or  month==5 or month ==7 or month==8 or month ==10 or month==12) and 1<=day<=31:
        result = f"Existe el día {day} de {meses[month-1]}"
    
    elif (month ==2 and year%4==0 and year%100!=0 or year%400==0) and 1<=day<=29:
        result = f"Existe el día {day} de {meses[month-1]}"
        
    elif month==2 and 1<=day<=28:
        result = f"Existe el día {day} de {meses[month-1]}"
    
    else:
        result = f"No existe el día {day} de {meses[month-1]}"

    return result

print(comprobar_fecha(29,2,2004))
print(comprobar_fecha(28,2,2003))
print(comprobar_fecha(31,1,2004))
print(comprobar_fecha(0,2,2004))


