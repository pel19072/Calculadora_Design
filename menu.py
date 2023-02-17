from modulos import calculadora
calc = calculadora()

while True:
    operation = input("Seleccione una operación a realizar:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Historial\n6. Salir\n")
    if not operation.isnumeric():
        print("El valor que ingresó no está soportado, vuelva a intentarlo")
        continue
    if int(operation) == 5:
        print(calc)
        continue
    if int(operation) == 6:
        break


    while True:
        a = input("Ingrese el primer número: ")
        b = input("Ingrese el segundo número: ")
        try:
            a = float(a)
            b = float(b)
            break
        except:
            print("Alguno de los número que ingresó no es numérico, inténtelo otra vez\n")
    
    match int(operation):
        case 1:
            print(calc.sumar([a, b]))
            continue
        case 2:
            print(calc.restar([a, b]))
            continue
        case 3:
            print(calc.multiplicar([a, b]))
            continue
        case 4:
            print(calc.dividir([a, b]))
            continue
        case _:
            print("No se conoce esta opción: ")
            continue