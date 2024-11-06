import string
import random
import logging
import hashlib
from datetime import datetime

def hash_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as archivo:
        while chunk := archivo.read(8192): h.update(chunk)
        return h.hexdigest()

def password_generator():
    """
    Crea contraseñas aleatorias siguiendo un par de preferencias del usuario
        
    """
    logging.basicConfig(
        filename='PwGenerator.log',
        level=logging.DEBUG,
        format='| %(asctime)s | %(name)s | %(levelname)s | %(message)s'
    )
    
    while True:
        password_length = int(input("Introduce la longitud deseada de la contraseña (mínimo 8): "))
        use_special = input("¿Incluir caracteres especiales? (s/n): ").strip().lower() == 's'

        logging.info(f"Longitud de la contraseña seleccionada: {password_length}")
        logging.info(f"Incluir caracteres especiales: {'Sí' if use_special else 'No'}")
        
        if password_length < 8:
            logging.warning("La longitud mínima de la contraseña es 8. El usuario ingresó una longitud no válida.")
            print("La longitud mínima de la contraseña debe ser 8.")
        else:
            break
    
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation
        
    password = ''
    for i in range(password_length):
        password += random.choice(characters)

    logging.info("Contraseña generada exitosamente.")
    print(f"Contraseña generada: {password}")

    reportpath = "C:\Results\PWGenerator_report.txt"
    with open (reportpath, 'a') as archivo:
        archivo.write(password)

    print(f"Fecha: {datetime.now().date()}")
    print(f"Hash del archivo: {hash_file(reportpath)}")
    print(f"Ubicación del archivo: {reportpath}")
    print(f"Nombre del archivo: PWGenerator_report.txt")
