import Admin_privileges as admin
import keyboard
import logging

logging.basicConfig(
    filename='Keylogger.log',
    level=logging.DEBUG,
    format='| %(asctime)s | %(name)s | %(levelname)s | %(message)s'
)

def keylogger(Keylogging_file='TeclasPulsadas_log.txt'):
    """
    Registra las pulsaciones de teclas y las guarda en un archivo .txt, la funcion deja de registrar las pulsaciones hasta que el usaria presiona la tecla 'esc'
    
    Args:
        log_file (str, optional): Nombre del archivo donde se guardaran las teclas pulsadas, Nombre por defecto: 'registro_teclas.txt'
    """
    try:
        logging.debug('Obteniendo permisos de administrador')
        admin.get_permissions()
    except ModuleNotFoundError as e:
        print(f"Error: {e}")
        logging.error(f'Modulo no instalado. Error: {e}')
        return
    except OSError as e:
        print(f'Error {e}')
        logging.error(f'Se requieren permisos de administrador. Error: {e}')
        return
    
    lista = []
    
    #Registra en tiempo real las teclas presionadas y las guarda en una lista, el script se queda en espera hasta presionar la tecla 'esc'
    try:
        logging.debug('Se registran las pulsaciones de las teclas')
        keyboard.on_press(lambda teclas: lista.append(teclas.name))
        print("Presione 'esc' para terminar.")
        logging.debug("Se espera la pulsacion de la tecla 'esc' para terminar registro de pulsaciones")
        keyboard.wait('esc')
    except Exception as e:
        print(f'Error: {e}')
        logging.error(f'Error: {e}')
        return
    
    #Crea/Abre el archivo en modo append y agrega la lista al txt
    try:
        logging.debug(f'Se guardan el registro de pulsaciones en {Keylogging_file}')
        with open(Keylogging_file, "a") as archivo:
            archivo.write(" ".join(lista)+'\n')
    except (FileNotFoundError, OSError):
        print(f'Error al interactuar con el archivo: {e}')
        logging.error(f'Error: {e}')
        return


def macros():
    """
    Graba las pulsaciones del usuario a tiempo real contemplando el intervalo de tiempo entre cada pulsacion para posteriormente asignar una tecla para reproducirlo
    """
    #Verifica y obtiene permisos de admin
    try:
        admin.get_permissions()
    except ModuleNotFoundError as e:
        print(f"Error: {e}")
        logging.error(f'Modulo no instalado. Error: {e}')
        return
    
    #Graba las pulsaciones del teclado hasta que se presione la tecla 'esc' y las guarda en la variable
    print("Grabando teclas!!\nPresione 'esc' para terminar.\n")
    try:
        logging.debug('Grabacion de teclas. NOTA: La grabacion de teclas considera el tiempo de pulsacion entre cada teclas asi mismo el tiempo que se mantuvo pulsada la tecla')
        events = keyboard.record('esc')
    except (RuntimeError, AttributeError) as e:
        print(f"Error al registra: {e}")
        logging.error(f'Error al registrar las teclas: {e}')
        return
    
    #Reproduce el macros grabado anteriormente cada vez que se pulse la tecla '/' y el script se queda en espera para poder seguir usando el macros
    try:
        print("Presiona '/' para reproducir el macros\n")
        keyboard.add_hotkey('/', lambda: keyboard.play(events))
        logging.debug('Asignacion de hotkey para la utilizacion del macros')
        
        print("Presione la tecla 'esc' para dejar de usar el macros")
        keyboard.wait('esc')
        logging.debug("Se espera la pulsacion de la tecla 'esc' para la continuacion del script")
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f'Error al usar el macros: {e}')
        exit 