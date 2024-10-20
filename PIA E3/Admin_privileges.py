import sys
import ctypes

def get_permissions():
    """
    Verifica si el script esta siendo ejecutado con permisos de administrador, en caso que no los tenga solicita los permisos y reinicia el script
    """
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    except (AttributeError, OSError) as e:
        print(f"Error al obtener permisos de administrador: {e}")