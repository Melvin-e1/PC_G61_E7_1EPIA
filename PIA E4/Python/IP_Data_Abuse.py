import requests
import logging
import hashlib
import json
from datetime import datetime

logging.basicConfig(
    filename='IpDataAbuse.log',
    level=logging.DEBUG,
    format='| %(asctime)s | %(name)s | %(levelname)s | %(message)s'
)

apikey = "778462b093ac2dc95d8787392a9fc9e70bf4d499621910024de465ed397e1e2fb3b9b96d563b137c"
url = "https://api.abuseipdb.com/api/v2"

def report_ip(ip, comment, categories):
    """
    Reporta la ip dada por usuario, agregando un comentario y el id de tipo de ataque que tiene categorizado la api

    Args:
        ip (str): ip a reportar
        comment (str): comentario acerca de dicha ip
        categories (int): id de la categoria de ataque ejem: 22 corresponde a SSH, en la documentacion del DataIPDB

    """
    try:
        response = requests.post(
            f"{url}/report",
            headers={"Key": apikey, "Accept": "application/json"},
            data={"ip": ip, "comment": comment, "categories": categories}
        )
        logging.debug(f'{ip}: {comment}')
        return response.json()
    except requests.RequestException as e:
        logging.error(f'Ocurrio un error al intentar reportar la ip {ip}: {e}')
        print(f"Error: {e}")

def ip_query(ip):
    """
    Se consulta en la Api la ip dada por el usuario en busca de reportes anterior que pudiera tener

    Args:
        ip (str): Ip a consultar
    """
    try:
        response = requests.get(
            f"{url}/check",
            headers={"Key": apikey, "Accept": "application/json"},
            params={"ipAddress": ip}
        )
        logging.debug(f'Consulta de ip {ip}: {response.json()}')
        reportpath = "C:\Results\Ipdataabuse_report.txt"
        respuesta = response.json()
        respuesta_str = json.dumps(respuesta, indent=4)
        with open (reportpath, 'a') as archivo:
            archivo.write(respuesta_str)
    except requests.RequestException as e:
        logging.error(f'Error al consultar la ip {ip}: {e}')
        print(f"Error: {e}")
        
    print(f"Fecha: {datetime.now().date()}")
    print(f"Hash del archivo: {hash_file(reportpath)}")
    print(f"Ubicacion del archivo: {reportpath}")
    print("Nombre del archivo: Ipdataabuse_report.txt")
    
def hash_file(ruta_archivo): 
    h = hashlib.sha256() 
    with open(ruta_archivo, 'rb') as archivo: 
        while chunk := archivo.read(8192): h.update(chunk) 
        return h.hexdigest()

