import string
import random
import logging

def password_generator():

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
