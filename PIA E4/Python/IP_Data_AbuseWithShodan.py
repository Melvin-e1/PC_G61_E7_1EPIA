import requests
import logging
import hashlib
import json
import os
from datetime import datetime

def ip_abuse_module():
    #Configuracion del logging
    logging.basicConfig(
    filename='IpDataAbuse.log',
    level=logging.DEBUG,
    format='| %(asctime)s | %(name)s | %(levelname)s | %(message)s'
    )
    #La apikey ya esta definida usando la mia propia para evitar problemas
    apikey = "778462b093ac2dc95d8787392a9fc9e70bf4d499621910024de465ed397e1e2fb3b9b96d563b137c"
    url = "https://api.abuseipdb.com/api/v2"

    def report_ip(ip, comment, categories):
        try:
            response = requests.post(
                f"{url}/report",
                headers={"Key": apikey, "Accept": "application/json"},
                data={"ip": ip, "comment": comment, "categories": categories}
            )
            logging.debug(f'{ip}: {comment}')
            return response.json()
        except requests.RequestException as e:
            logging.error(f'Ocurrio un error al intentar reportar la IP {ip}: {e}')
            return None

    def ip_query(ip):
        try:
            response = requests.get(
                f"{url}/check",
                headers={"Key": apikey, "Accept": "application/json"},
                params={"ipAddress": ip}
            )
            logging.debug(f'Consulta de IP {ip}: {response.json()}')
            return response.json()
        except requests.RequestException as e:
            logging.error(f'Error al consultar la IP {ip}: {e}')
            return None

    def hash_file(filepath): 
        h = hashlib.sha256() 
        with open(filepath, 'rb') as archivo: 
            while chunk := archivo.read(8192): 
                h.update(chunk) 
        return h.hexdigest()

    def read_ips_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                ips = [line.strip() for line in file.readlines() if line.strip()]
            return ips
        except FileNotFoundError:
            print(f"El archivo {file_path} no se encontro.")
            return []

    if __name__ == "__main__":
        ip_file_path = r"C:\Results\ip_addresses.txt"
        reportpath = r"C:\Results\Ipdataabuse_report.txt"
    
        #Asegurarse de que la carpeta existe
        os.makedirs(os.path.dirname(reportpath), exist_ok=True)

        #Leer las IPs desde el archivo creado por el script de Shodan
        ip_list = read_ips_from_file(ip_file_path)

        #Lista para almacenar los resultados
        resultados = []

        #Procesar cada IP del archivo creado por el script de Shodan
        for ip in ip_list:
            #Consultar la IP
            consulta_resultado = ip_query(ip)
            if consulta_resultado is not None:
                resultados.append(json.dumps(consulta_resultado, indent=4))

            #Reportar la IP
            comment = "Reporte automatico"
            categories = [22]
            report_response = report_ip(ip, comment, categories)
            if report_response is not None:
                resultados.append(json.dumps(report_response, indent=4))

        #Generar el reporte
        with open(reportpath, 'a') as archivo:
            for resultado in resultados:
                archivo.write(resultado + "\n")

        print(f"Nombre del archivo: IpDataAbuseWithShodan_report_{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.txt")
        print(f"Ubicacion del archivo: {reportpath}")
        print(f"Hash del archivo: {hash_file(reportpath)}")
if __name__=="__main__":
    ip_abuse_module()
