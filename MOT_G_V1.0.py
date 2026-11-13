# Head: Conteo de cuartos, precios y cálculo inicial
Precio_de_cuartos = (300, 330, 370, 580, 800)

Cuartos_de_300 = int(input("Ingrese la cantidad de cuartos de 300: "))
cuartos_de_330 = int(input("Ingrese la cantidad de cuartos de 330: "))
cuartos_de_370 = int(input("Ingrese la cantidad de cuartos de 370: "))
cuartos_de_580 = int(input("Ingrese la cantidad de cuartos de 580: "))
cuartos_de_800 = int(input("Ingrese la cantidad de cuartos de 800: "))

# 1. Total base de cuartos
total_cuartos = (Cuartos_de_300 * Precio_de_cuartos[0]) + \
                (cuartos_de_330 * Precio_de_cuartos[1]) + \
                (cuartos_de_370 * Precio_de_cuartos[2]) + \
                (cuartos_de_580 * Precio_de_cuartos[3]) + \
                (cuartos_de_800 * Precio_de_cuartos[4])

# Inicializamos variables para los extras por si no se usan
total_extras = 0
total_tiempo_extra = 0

# Manejo de extras
Extras_de_cuartos = input("¿Hacemos el total de bar, varios, alimentos y costo personal por separado o dame solo el total? (si/no): ").lower()

if Extras_de_cuartos == "si":
    total_extras = float(input("Cuanto es el costo total de extras: "))
else:
    # Bar
    bar = input("¿Hay cosas en el bar? (si/no): ").lower()
    if bar == "si":
        total_extras += float(input("Ingrese la cantidad de bar: "))
    
    # Alimentos
    alimentos = input("¿Hay alimentos? (si/no): ").lower()
    if alimentos == "si":
        total_extras += float(input("Ingrese la cantidad de alimentos: "))
    
    # Varios
    varios = input("¿Hay cosas en varios? (si/no): ").lower()
    if varios == "si":
        total_extras += float(input("Ingrese la cantidad de varios: "))
    
    # Costo personal
    costo_personal = input("¿Hay costo personal? (si/no): ").lower()
    if costo_personal == "si":
        total_extras += float(input("Ingrese la cantidad de costo personal: "))

# Tiempo extra
tiempo_extra = input("¿Hay tiempo extra? (si/no): ").lower()
if tiempo_extra == "si":
    total_tiempo_extra = float(input("Ingrese la cantidad de tiempo extra: "))

# --- CÁLCULOS INTERMEDIOS PARA EL REPORTE ---
cuartos_con_extras = total_cuartos + total_extras
cuartos_con_tiempo = total_cuartos + total_tiempo_extra
suma_general = total_cuartos + total_extras + total_tiempo_extra

# --- PAGOS CON TARJETA Y EFECTIVO ---
num_pagos = int(input("\n¿Cuántos pagos con tarjeta hay?: "))

pagos_tarjeta = [370] * num_pagos

if num_pagos > 0:
    print("\n--- Verificación de pagos con tarjeta ---")
    print("Presiona ENTER para aceptar 370, o escribe el monto real si cambió.\n")
    
    for i in range(num_pagos):
        entrada = input(f"Pago {i + 1} [Valor por defecto: 370]: ")
        if entrada.strip() != "":
            pagos_tarjeta[i] = float(entrada)

total_tarjeta = sum(pagos_tarjeta)

# El efectivo se calcula restando el total de tarjetas al acumulado general real
efectivo = suma_general - total_tarjeta

# --- REPORTE FINAL ESTRICTO ---
print("\n========== REPORTE FINAL ==========")
print(f"Total de cuartos: ${total_cuartos:,.2f}")
print(f"Total de cuartos con bar, alimentos, varios y personal: ${cuartos_con_extras:,.2f}")
print(f"Total de cuartos con tiempo extra: ${cuartos_con_tiempo:,.2f}")
print(f"Total de cuartos con bar, alimentos, varios y personal y con tiempo extra: ${suma_general:,.2f}")
print(f"Total de pago con tarjetas de crédito: ${total_tarjeta:,.2f}")
print(f"Total de efectivo: ${efectivo:,.2f}")