while True:
    operation = input("Seleccione una operación a realizar:\n1. Suma\n2. Resta\n3. División\n4. Multiplicación\n5. Salir\n")
    if not operation.isnumeric():
        print("El valor que ingresó no está soportado, vuelva a intentarlo")
        continue
    
    if int(operation) == 5:
        break

    while True:
        a = input("Ingrese el primer número\n")
        b = input("Ingrese el segundo número\n")
        try:
            a = float(a)
            b = float(b)
            break
        except:
            print("Alguno de los número que ingresó no es numérico, inténtelo otra vez\n")
    
    match int(operation):
        case 1:
            print("La suma es: ")
            continue
        case 2:
            print("La resta es: ")
            continue
        case 3:
            print("La multiplicación es: ")
            continue
        case 4:
            print("La división es: ")
            continue
        case _:
            print("No se conoce esta opción: ")
            continue