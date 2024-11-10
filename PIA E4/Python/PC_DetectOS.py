import platform

def detect_os():
    
    os = platform.system()
    if os == "Windows":
        print("Sistema Operativo: Windows")
        os_id = 1
    
    elif os == "Linux":
        print("Sistema Operativo: Linux")
        os_id = 2
    
    elif os == "Darwin":
        print("Sistema Operativo: macOS")
        os_id = 3
    
    else:
        print("Sistema operativo desconocido")
        return "Sistema operativo desconocido"
    
    return os_id

#cosa = detect_os()
#print(cosa)
