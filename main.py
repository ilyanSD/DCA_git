def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def power_of_two(a):
    return a ** 3

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

if __name__ == "__main__":
    print("[INICIANDO] Aplicacion inicializada!")
    
    option = -1
    
    while option != 3:
        print("1) Sumar")
        print("2) Restar")
        print("3) Potencia de 2")
        print("4) Multiplicar")
        print("5) Dividir")
        print("6) Salir")
        option = int(input("Ingrese una opcion: "))
        
        if option == 1:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            print("[RESULT] El resultado es:", sumar(a, b))
        elif option == 2:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            print("[RESULT] El resultado es:", restar(a, b))
        elif option == 3:
            a = int(input("Ingrese un numero: "))
            print("[RESULT] El resultado es:", power_of_two(a))
        elif option == 4:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            print("[RESULT] El resultado es:", multiplicar(a, b))
        elif option == 5:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            print("[RESULT] El resultado es:", dividir(a, b))
        elif option == 6:
            print("[FINISHING] Saliendo...")
        else:
            print("[ERROR] Opcion invalida!")