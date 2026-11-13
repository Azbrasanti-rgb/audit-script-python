#head conteo de cuartos, precio por cuarto, precio de bar, precio de Varios, tiempo extra, y total

Precio_de_cuartos = (300, 330, 370, 580, 800)
Cantidad_de_cuartos = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)

Cuartos = int(input("Ingrese la cantidad de cuartos: "))

Cuartos_de_300 = int(input("Ingrese la cantidad de cuartos de 300: "))
cuartos_de_330 = int(input("Ingrese la cantidad de cuartos de 330: "))
cuartos_de_370 = int(input("Ingrese la cantidad de cuartos de 370: "))
cuartos_de_580 = int(input("Ingrese la cantidad de cuartos de 580: "))
cuartos_de_800 = int(input("Ingrese la cantidad de cuartos de 800: "))

suma_cuartos = (Cuartos_de_300 * Precio_de_cuartos[0]) + (cuartos_de_330 * Precio_de_cuartos[1]) + (cuartos_de_370 * Precio_de_cuartos[2]) + (cuartos_de_580 * Precio_de_cuartos[3]) + (cuartos_de_800 * Precio_de_cuartos[4])

#Hacemos el conteo por separado o juntoamos bar, alimentos, varios y costo personal

Extras_de_cuartos = (input("Hacemos el total de bar, varios, alimentos y costo personal o dame solo el total por cuartos?: "))
if Extras_de_cuartos == "si":
    Extre_de_cuartos = int(input("Cuanto es el costo total: "))
else:
    bar = input("hay cosas en var bar?: ")
    if bar == "si":
        cantidad_bar = (input("Ingrese la cantidad de bar: "))
        suma_cuartos += cantidad_bar  
    else:
        print("No hay cosas en el bar")
            
        #alimentos 
        Alimentos: str = input("hay alimentos?: ")
        if Alimentos == "si":
            cantidad_alimentos = int(input("Ingrese la cantidad de alimentos: "))
            suma_cuartos += cantidad_alimentos  
        else:
            print("No hay alimentos")
            
        #varios
        Varios = input("hay cosas varios?: ")
        if Varios == "si":
            cantidad_varios = int(input("Ingrese la cantidad de varios: "))
            suma_cuartos += cantidad_varios  
        else:
            print("No hay cosas varios")
            
        #costo personal
        costo_personal = input("hay costo personal?: ")
        if costo_personal == "si":
            cantidad_costo_personal = int(input("Ingrese la cantidad de costo personal: "))
            suma_cuartos += cantidad_costo_personal  
        else:
            print("No hay costo personal")



#Tiempo extra
tiempo_extra = input("hay tiempo extra?: ")
if tiempo_extra == "si":
    cantidad_tiempo_extra = int(input("Ingrese la cantidad de tiempo extra: "))
    suma_cuartos += cantidad_tiempo_extra
else:
    print("No hay tiempo extra")
    
#pagos con tarjeta y efectivo
Pagos_con_tarjeta = int(input("Cuantos pagos con tarjeta hay?: "))
# 1. Pedir cuántos pagos con tarjeta hay
num_pagos = int(input("¿Cuántos pagos con tarjeta hay?: "))

# 2. Crear una lista asumiendo que TODOS valen 370 por defecto
pagos_tarjeta = [370] * num_pagos

print(
    "\n--- Verificación de pagos ---"
)
print("Presiona ENTER para aceptar 370, o escribe el monto real si cambió.\n")

# 3. Recorrer la lista para confirmar o modificar individualmente
for i in range(num_pagos):
  entrada = input(f"Pago {i + 1} [Valor por defecto: 370]: ")

  # Si el usuario escribe algo, reemplazamos el 370 por ese valor
  if entrada.strip() != "":
    pagos_tarjeta[i] = float(
        entrada
    )  # Usamos float por si hay decimales, o int si son enteros

# 4. Calcular el total de tarjeta sumando la lista
total_tarjeta = sum(pagos_tarjeta)

# 5. Obtener el total de cuartos para calcular el efectivo
print("\n--------------------------------")
suma_cuartos = float(
    input("Ingresa el resultado total de cuartos (para la resta): ")
)

# 6. Restar el total de tarjetas al total de cuartos para sacar el efectivo
efectivo = suma_cuartos - total_tarjeta

# 7. Mostrar resultados finales
print("\n========== RESULTADOS ==========")
print(f"Lista final de pagos con tarjeta: {pagos_tarjeta}")
print(f"Suma total de tarjeta: ${total_tarjeta:,.2f}")
print(f"Total de cuartos: ${suma_cuartos:,.2f}")
print(f"Efectivo resultante: ${efectivo:,.2f}")

    
    
    
    
print ("El total de cuartos es: ", suma_cuartos)
