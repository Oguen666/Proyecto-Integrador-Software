from src import reto_owen, reto_martin, reto_paulo, reto_rigo, reto_baruch

def menu():
    while True:
        print("\nModulos de retos de programacion")
        print("1. Reto Sort")
        print("2. Reto +++++")
        print("3. Reto +++++")
        print("4. Reto +++++")
        print("5. Reto de Pedro")
        print("6. Salir")
        
        opcion = input("Selecciona un reto: ")
        
        if opcion == "1":
            reto_owen.ejecutar()
        elif opcion == "2":
            reto_martin.ejecutar()
        elif opcion == "3":
            reto_paulo.ejecutar()
        elif opcion == "4":
            reto_rigo.ejecutar()
        elif opcion == "5":
            reto_baruch.ejecutar()
        elif opcion == "6":
            break
        else:
            print("selecciona una opcion valida")

if __name__ == "__main__":
    menu()