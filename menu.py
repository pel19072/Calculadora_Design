from modulos import calculadora
calc = calculadora()

# Inicio del menú
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
    """ 
    Inicio de las operaciones
    Se realizó de tal forma que se puedan operar múltiples números a la vez
    Casos:
    * Suma: Se suman todos los números que se ingresen
    * Resta: Se restan del primer número ingresado todos los demás agregados
    * Multiplicación: Se multiplican todos los números que se ingresan
    * División: Se dividen al primero dentro de todos los demás agregados de forma consecutiva
    """
    nums = []
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            nums.append(a)
            nums.append(b)
            while True:
                multiple_op = input("Desea ingresar más números? [si/no(default)]")
                if multiple_op != "si":
                    break
                c = float(input("Ingrese el otro número: "))
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
            print("No se conoce esta opción: ")
            continue
