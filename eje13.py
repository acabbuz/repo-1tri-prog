def contar_monedas():
    monedas_dos = (int(input("Monedas de dos euros a contar: ")) *2)*100
    monedas_uno = int(input("Monedas de un euros a contar: ")) * 100
    monedas_cincuenta_cents = int(input("Monedas de cicuenta centimos a contar: ")) * 50
    monedas_veinte_cents = int(input("Monedas de veinte centimos a contar: "))*20
    monedas_diez_cents = int(input("Monedas de diez centimos a contar: "))*10
    monedas_cinco_cents = int(input("Monedas de cinco centimos a contar: "))*5
    monedas_dos_cents =int(input("Monedas de dos centimos a contar: "))*2
    monedas_un_cents = int(input("Monedas de un centimos a contar: "))

    result = f"Tienes : {(monedas_dos+ monedas_uno + monedas_cincuenta_cents + monedas_veinte_cents + monedas_diez_cents + monedas_cinco_cents + monedas_dos_cents + monedas_un_cents)/100} €"
    
    return result

print(contar_monedas())




