import subprocess
import time
import os
import sys
from sql_injection_test import run_injection_tests

def display_menu():
    print("=== Menu de Pruebas de Ciberseguridad ===")
    print("1. Ejecutar pruebas de inyeccion SQL")
    print("2. Salir")

def main():
    #Iniciar la aplicacion web vulnerable en un proceso separado
    with open(os.devnull, 'w') as devnull:
        app_process = subprocess.Popen(['python', 'vulnerable_app.py'], stdout=devnull, stderr=devnull)

    time.sleep(2)  #Esperar un momento para asegurarse de que la aplicacion este en funcionamiento

    
    while True:
        display_menu()
        choice = input("Seleccione una opcion: ")
            
        if choice == '1':
            run_injection_tests()
        elif choice == '2':
            print("Saliendo del programa.")
            app_process.terminate()  #Para cerrar la aplicscion web al salir
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")
    

if __name__ == "__main__":
    main()