import shodan
import logging

def shodan_module():

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
        
        print(f'Resultados encontrados: {results["total"]}')
        
        for result in results['matches']:
            print(f'IP: {result["ip_str"]}')
            print(f'Organización: {result.get("org", "Desconocida")}')
            print(f'Sistema Operativo: {result.get("os", "No especificado")}')
            print(f'Puertos: {result.get("port")}')
            print(f'Datos del servicio:\n{result["data"]}')
            print('-' * 50)
            logging.info(f'Resultado encontrado: IP {result["ip_str"]}, Organización {result.get("org", "Desconocida")}')
        
    except shodan.APIError as error:
        logging.error(f"Error en la búsqueda: {error}")
        print(f'Error en la búsqueda: {error}')
