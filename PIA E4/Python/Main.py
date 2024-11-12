import subprocess
import IP_Data_Abuse as IpDataAbuse
import Keylogger
import os
import sys
import PC_PIA_PwGenerator as PwGenerator
from PC_DetectOS import detect_os
from menu_sql_injection import main
from PIA_ShodanWithIP_Abuse import shodan_module
from IP_Data_AbuseWithShodan import ip_abuse_module

def executePw(command):
    a = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
    return a.stdout

    
print('\t----PIA 4E Menu----')
print('[1] Python')
print('[2] Powershell')
print('[3] Bash')
print('[4] Salir')

while True:
    op = int(input('Opcion a usar: '))
    if 1<= op <=4:
        match op:
            case 1:
                os.system('cls')
                print('\t----Modulos Python----')
                print('[1] AbuseIPDB')
                print('[2] Keylogger')
                print('[3] PwGenerator')
                print('[4] SQL Injection')
                print('[5] Shodan (antes del ip abusewithshodan)')
                print('[6] IpDataAbuseWithShodan')
                opPy = int(input('Opcion a usar: '))
                
                #Python modules
                match opPy:
                    #AbuseIPDB
                    case 1: 
                        os.system('cls')
                        print('\t----AbuseIPDB----')
                        print('[1] Report ip')
                        print('[2] Ip query')     
                        opADB = int(input('Opcion a usar: '))
                        
                        match opADB:
                            case 1:
                                os.system('cls')
                                print('\t\t--Reportar IP--')
                                ip = input('Ip (ejemplo: 8.8.8.8): ')
                                comment = input('Comentario (ejemplo: Ip con sospecha de actividad maliciosa): ')
                                categories = int(input('Categoria (Puede ver las categorias en https://www.abuseipdb.com/categories): '))
                                try:
                                    IpDataAbuse.report_ip(ip, comment, categories)
                                except Exception as e:
                                    print(f'Error: {e}')
                                break
                            case 2:
                                os.system('cls')
                                print('\t\t--Consultar IP--')
                                ip = input('Ip (ejemplo: 8.8.8.8): ')
                                try:
                                    print(IpDataAbuse.ip_query(ip))
                                except Exception as e:
                                    print(f'Error: {e}')
                                break
                    #Keylogger
                    case 2:
                        os.system('cls')
                        print('Funciones: ')
                        print('[1]Keylogger')
                        print('[2]Grabar/Usar macros')
                        op2 = int(input('Ingrese la opcion a usar: '))
                        match op2:
                            case 1:
                                os.system('cls')
                                file_name = input('Nombre del archivo (Default: TeclasPulsadas_log.txt): ')
                                try:
                                    Keylogger.keylogger(file_name)
                                except Exception as e:
                                    print(f'Error: {e}')
                                break
                            case 2:
                                try:
                                    Keylogger.macros()
                                except Exception as e:
                                    print(f'Error: {e}')
                                break
                        break
                    #PwGenerator
                    case 3:
                        os.system('cls')
                        try: 
                            PwGenerator.password_generator()
                        except Exception as e:
                                    print(f'Error: {e}')
                        break
                    #sql injection
                    case 4:
                        os.system('cls')
                        try:
                            main()
                        except Exception as e:
                            print(f'Error: {e}')
                        break
                    #Shodan junto con Ip abuse (usar este primero)
                    case 5:
                        os.system('cls')
                        try:
                            shodan_module()
                        except Exception as e:
                            print(f'Error: {e}')
                        break
                    #Ip data abuse junto con shodan, (usar antes el de shodan)
                    case 6:
                        os.system('cls')
                        try:
                            ip_abuse_module()
                        except Exception as e:
                            print(f'Error: {e}')
                        break
                break
            #Powershell
            case 2:
                os.system('cls')
                whoOS = detect_os()
                if whoOS != 1: #Macos y Linux
                    print('!!!Es posible que los scripts no funcionen correctamente en este sistema operativo')
                    print('Si hay cualquier duda o fallo inesperado, todos los scripts completamente funcionales se encuentran en el repositorio de github :)')
                
                print('\t----Modulos Powershell----')
                print('[1] DuplicateDir')
                print('[2] HiddenFile')
                print('[3] SystemResources')
                print('[4] VirusTotal')
                opPw = int(input('Opcion a usar: '))
                
                match opPw:
                    #DuplicateDir
                    case 1:
                        os.system('cls')
                        path = input("Ingrese la ruta del directorio a duplicar: ")
                        module_path = "DuplicateDir"
                        comando = f"Import-Module {module_path}; DuplicateDir" 
                        a = executePw(comando)
                        print(a)
                        
                        break
                    #HiddenFiles
                    case 2:
                        os.system('cls')
                        path = input("Ingrese la ruta del directorio a inspeccionar: ")
                        module_path = "HiddenFile"
                        comando = f"Import-Module {module_path}; HiddenFile -path {path}"
                        a = executePw(comando)
                        print(a) 
                        break
                    #SystemResources
                    case 3:
                        os.system('cls')
                        module_path = "SystemResource"
                        comando = f"Import-Module {module_path}; SystemResource"
                        a = executePw(comando)
                        print(a) 
                        
                        break
                    case 4:
                        os.system('cls')
                        module_path = "VirusTotal"
                        comando = f"Import-Module {module_path}; VirusTotal"
                        a = executePw(comando)
                        print(a) 
                        break

                break
            
            #Bash
            case 3:
                print("No es posible ejecutarlos en este sistema operativo pero se encuentran en las carpetas de cada sistema operativo en el github") 
                break
            


