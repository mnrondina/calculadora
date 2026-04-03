#Calculadora

def sumar (a,b):
    return a+b

def resta (a,b):
    return a-b

def multi (a,b):
    return a*b

def division (a,b):
    if b == 0:
        raise ValueError ("No se puede dividir por CERO.")
    return a/b


def calculadora ():
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        print("Elija la operación\n")
        opcion = input("1) SUMA\n2) RESTA\n3) MULTIPLICACIÓN\n4) DIVISIÓN\n")

        if opcion == "1":
            resultado = sumar(a,b)
        elif opcion == "2":
            resultado = resta(a,b)
        elif opcion == "3":
            resultado = multi(a,b)
        elif opcion == "4":
            resultado = division(a,b)
        else:
            raise ValueError ("Opción inválida")
        
        print(f"El resultado es: {resultado} ")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Operación finalizada")

if __name__ == "__main__":
    calculadora()