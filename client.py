import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")


def mostrar_menu():
    print("\n=== Menú de la Calculadora ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
def obtener_numeros():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    return a, b

def iniciar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            a, b = obtener_numeros()
            print(f"Resultado: {proxy.add(a, b)}")
        elif opcion == "2":
            a, b = obtener_numeros()
            print(f"Resultado: {proxy.res(a, b)}")
        elif opcion == "3":
            a, b = obtener_numeros()
            print(f"Resultado: {proxy.mul(a, b)}")
        elif opcion == "4":
            a, b = obtener_numeros()
            print(f"Resultado: {proxy.div(a, b)}")
        elif opcion == "5":
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


iniciar_calculadora()