def reemplazarCaracteres(cadena: str, caracter_a_reemplazar: str, caracter_de_reemplazo: str) -> str:
    contador = 0
    nueva_cadena = cadena.replace(caracter_a_reemplazar, caracter_de_reemplazo)
    for caracter in cadena:
        if caracter == caracter_a_reemplazar:
            contador += 1
    return nueva_cadena, contador

cadena_ingresada = input("Ingrese un texto: ")
caracter_para_reemplazar_ingresado = input("Ingrese el caracter que quiere reemplazar: ")
caracter_de_reemplazo_ingresado = input("Ingrese el caracter por el que quiere reemplazar al caracter anterior: ")

nueva_cadena, contador = reemplazarCaracteres(cadena_ingresada, caracter_para_reemplazar_ingresado, caracter_de_reemplazo_ingresado)

print(f"Nueva cadena: {nueva_cadena}")
print(f"Cantidad de reemplazos: {contador}")