import shodan
import logging
import hashlib
import datetime from datetime

def hash_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as archivo:
        while chunk := archivo.read(8192): h.update(chunk)
        return h.hexdigest()

def shodan_module():
    """
    Brinda información sobre puertos abiertos con servicios específicos
    
    """
    logging.basicConfig(
        filename='Shodan_.log',
        level=logging.DEBUG,
        format='| %(asctime)s | %(name)s | %(levelname)s | %(message)s'
    )
    
    def ports_menu():

        print("¿Qué servicio desea buscar?")
        print("1. FTP \n2. SSH \n3. HTTP \n4. MySQL\n")
            
    API_KEY = 'pdltGOgtErDmR7DSWL5Qk0fOiJd9z4j6'
    api = shodan.Shodan(API_KEY)

    while True:
        ports_menu()
        service_number = int(input("Ingresa el número de el servicio deseado: "))
        if 1 <= service_number <= 4:
            match service_number:
                case 1:
                    service = "port:21"
                    logging.info("El usuario seleccionó FTP (puerto 21).")

                case 2:
                    service = "port:22"
                    logging.info("El usuario seleccionó SSH (puerto 22).")

                case 3:
                    service = "port:80"
                    logging.info("El usuario seleccionó HTTP (puerto 80).")

                case 4:
                    service = "port:3306"
                    logging.info("El usuario seleccionó MySQL (puerto 3306).")

            break
        else:
            logging.warning("Opción no válida seleccionada por el usuario.")
            print("Opción no válida, inténtelo de nuevo.")
    
    try:
        logging.info(f"Buscando información del servicio: {service}")
        results = api.search(service)
        logging.info(f"Resultados encontrados: {results['total']}")

        reportpath = "C:\Results\Shodan_report.txt"
        with open (reportpath, 'a') as archivo:
            archivo.write(f'Resultados encontrados: {results['total']}\n\n\n')
            for result in results['matches']:
                
                logging.info(f'Resultado encontrado: IP {result["ip_str"]}, Organización {result.get("org", "Desconocida")}')
                
                archivo.write(f'IP: {result["ip_str"]}\n')
                archivo.write(f'Organización: {result.get("org", "Desconocida")}\n')
                archivo.write(f'Sistema Operativo: {result.get("os", "No especificado")}\n')
                archivo.write(f'Puertos: {result.get("port")}\n')
                archivo.write(f'Datos del servicio:\n{result["data"]}\n\n\n\n')

        print(f"Fecha: {datetime.now().date()}")
        print(f"Hash del archivo: {hash_file(reportpath)}")
        print(f"Ubicación del archivo: {reportpath}")
        print(f"Nombre del archivo: Shodan_report.txt")
        
    except shodan.APIError as error:
        logging.error(f"Error en la búsqueda: {error}")
        print(f'Error en la búsqueda: {error}')
