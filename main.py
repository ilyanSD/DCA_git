def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

if __name__ == "__main__":
    print("[INICIANDO] Aplicacion inicializada!")
    
    option = -1
    
    while option != 3:
        print("1) Sumar")
        print("2) Restar")
        print("3) Salir")
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
            print("[FINISHING] Saliendo...")
        else:
            print("[ERROR] Opcion invalida!")