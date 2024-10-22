import subprocess
import time
import threading

##variable para almacenrar el proceso de la app
app_process = None

##Funcion para ejecutar la app vulnerable
def run_vulnerable_app():
    global app_process
    app_process = subprocess.Popen(['python', 'vulnerable_app.py'])
    app_process.wait()

def sql_injection_menu():
    while True:
        print("=== Menu Principal ===")
        print("1. Realizar pruebas de Inyeccion SQL")
        print("2. Salir")

        op = input("Seleccione una opcion: ").strip()

        if op == '1':
            print("[*] Iniciando servidor de la aplicacion vulnerable...")
            app_thread = threading.Thread(target=run_vulnerable_app)
            app_thread.start()
            time.sleep(2)  # Esperar un momento para que la app inicie
            print("[*] Iniciando pruebas de inyección SQL...")
            try:
                from sql_injection_test import test_sql_injection, generate_report
                results = test_sql_injection()
                generate_report(results)
            except Exception as e:
                print(f"[!] Error durante las pruebas: {e}")
        elif op == '2':
            print("Saliendo...")
            if app_process is not None:
                app_process.terminate()
                app_process.wait()
            break
        else:
            print("Opcion invalida. por favor ingrese su opcion de nuevo")

if __name__ == '__main__':
    sql_injection_menu()