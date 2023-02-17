# Daniela Morales Ponce - Carné 19213
# Ricardo Pellecer Orellana - Carné 19072
# Calculadora

from modulos import calculadora
calc = calculadora()

# Inicio del menú
while True:
    operation = input("Seleccione una operación a realizar:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Historial\n6. Salir\n")
    if not operation.isnumeric():
        print("El valor que ingresó no está soportado, vuelva a intentarlo")
        continue
    if int(operation) == 6:
        break
    if int(operation) == 5:
        print(calc)
        continue
    
    nums = []
    while True:
        try:
            a = float(input("Ingrese el número a: "))
            b = float(input("Ingrese el número b: "))
            nums.append(b)
            nums.append(a)
            while True:
                multiple_op = input("Desea ingresar más números? El default es no [si/no]")
                if multiple_op != "si":
                    break
                c = float(input("Ingrese otro número: "))
                nums.append(c)
            break
        except:
            print("Alguno de los número que ingresó no es numérico, inténtelo otra vez\n")
    
    match int(operation):
        case 1:
            print(calc.sumar(nums))
            continue
        case 2:
            print(calc.restar(nums))
            continue
        case 3:
            print(calc.multiplicar(nums))
            continue
        case 4:
            print(calc.dividir(nums))
            continue
        case _:
            print("Esta opción no existe. Inténtelo de nuevo: ")
            continue
