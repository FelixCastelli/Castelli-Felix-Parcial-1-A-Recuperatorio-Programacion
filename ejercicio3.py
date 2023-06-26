def ordenarCaracteres(cadena_ingresada:str) -> str:
    lista_cadena_ingresada = list(cadena_ingresada)
    tam = len(lista_cadena_ingresada)

    for i in range(tam - 1):
        for j in range (i + 1, tam):
            if (lista_cadena_ingresada[i] > lista_cadena_ingresada[j]):
                aux = lista_cadena_ingresada[i]
                lista_cadena_ingresada[i] = lista_cadena_ingresada[j]
                lista_cadena_ingresada[j] = aux

    cadena_ingresada = "".join(lista_cadena_ingresada)
    print(cadena_ingresada)

cadena_ingresada = input("Ingrese una cadena de caracteres, la cual quiera ordenar las letras por orden alfabetico: ")
ordenarCaracteres(cadena_ingresada)