def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print("[INICIANDO] Aplicacion inicializada!")
    
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    
    print("El resultado de la suma es:", sumar(a, b))