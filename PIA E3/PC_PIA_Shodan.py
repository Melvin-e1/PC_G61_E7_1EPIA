def shodan_module():

    def ports_menu():

        print("¿Qué servicio desea buscar?")
        print("1. FTP \n2. SSH \n3. HTTP \n4. MySQL\n")
        
    import shodan
    
    API_KEY = 'pdltGOgtErDmR7DSWL5Qk0fOiJd9z4j6'
    api = shodan.Shodan(API_KEY)

    while True:
        ports_menu()
        service_number = int(input("Ingresa el número de el servicio deseado: "))
        if 1 <= service_number <= 4:
            match service_number:
                case 1:
                    service = "port:21"
                case 2:
                    service = "port:22"
                case 3:
                    service = "port:80"
                case 4:
                    service = "port:3306"
            break
        else:
            print("Opción no válida, inténtelo de nuevo.")
    
    try:
        results = api.search(service)
        
        print(f'Resultados encontrados: {results["total"]}')
        
        for result in results['matches']:
            print(f'IP: {result["ip_str"]}')
            print(f'Organización: {result.get("org", "Desconocida")}')
            print(f'Sistema Operativo: {result.get("os", "No especificado")}')
            print(f'Puertos: {result.get("port")}')
            print(f'Datos del servicio:\n{result["data"]}')
            print('-' * 50)
        
    except shodan.APIError as error:
        print(f'Error en la búsqueda: {error}')

