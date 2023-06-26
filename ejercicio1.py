def AplicarAumento(precio: float) -> float:
    aumento = precio * 0.05

    precio_con_aumento = precio + aumento 
    return precio_con_aumento

try:
    precio_ingresado = float(input("Ingrese el precio del cual desea calcular el (5%) de aumento: "))
except ValueError:
    precio_ingresado = float(input("ERROR, eso no es un precio, ingrese el precio del cual desea calcular el (5%) de aumento: "))

precio_con_aumento = AplicarAumento(precio_ingresado)

print(f"El precio final con el aumento del 5% es: ${precio_con_aumento}")