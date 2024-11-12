import shodan
import logging
import hashlib
from datetime import datetime

def hash_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as archivo:
        while chunk := archivo.read(8192):
            h.update(chunk)
        return h.hexdigest()

def shodan_module():
    #Configuracion del logging
    logging.basicConfig(
        filename='Shodan_.log',
        level=logging.DEBUG,
        format='| %(asctime)s | %(levelname)s | %(message)s'
    )

    API_KEY = 'pdltGOgtErDmR7DSWL5Qk0fOiJd9z4j6'
    api = shodan.Shodan(API_KEY)

    #Menu para seleccionar el servicio
    def ports_menu():
        print("¿Que servicio desea buscar?")
        print("1. FTP (puerto 21)\n2. SSH (puerto 22)\n3. HTTP (puerto 80)\n4. MySQL (puerto 3306)")

    while True:
        ports_menu()
        try:
            service_number = int(input("Ingresa el numero de el servicio deseado: "))
            if 1 <= service_number <= 4:
                if service_number == 1:
                    service = "port:21"
                elif service_number == 2:
                    service = "port:22"
                elif service_number == 3:
                    service = "port:80"
                elif service_number == 4:
                    service = "port:3306"
                break
            else:
                print("Opcion no valida, intentelo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un numero valido.")

    try:
        print(f"Buscando informacion del servicio: {service}")
        logging.info(f"Buscando informacion del servicio: {service}")
        results = api.search(service)

        print(f"Resultados encontrados: {results['total']}")
        logging.info(f"Resultados encontrados: {results['total']}")

        reportpath = "C:\\Results\\Shodan_report.txt"
        ip_list = []

        with open(reportpath, 'a') as archivo:
            archivo.write(f'Resultados encontrados: {results["total"]}\n\n\n')
            for result in results['matches']:
                ip_address = result["ip_str"]
                ip_list.append(ip_address)

                logging.info(f'Resultado encontrado: IP {ip_address}, Organizacion {result.get("org", "Desconocida")}')
                
                archivo.write(f'IP: {ip_address}\n')
                archivo.write(f'Organizacion: {result.get("org", "Desconocida")}\n')
                archivo.write(f'Sistema Operativo: {result.get("os", "No especificado")}\n')
                archivo.write(f'Puertos: {result.get("port")}\n')
                archivo.write(f'Datos del servicio:\n{result["data"]}\n\n\n\n')

        #Guarda las IPs en un archivo para que el script de ip data abuse las lea
        with open("C:\\Results\\ip_addresses.txt", 'w') as ip_file:
            for ip in ip_list:
                ip_file.write(f"{ip}\n")

        print(f"Hash del archivo: {hash_file(reportpath)}")
        print(f"Ubicacion del archivo: {reportpath}")
        
    except shodan.APIError as error:
        logging.error(f"Error en la busqueda: {error}")
        print(f'Error en la busqueda: {error}')
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        print(f'Error inesperado: {e}')

if __name__ == "__main__":
    shodan_module()