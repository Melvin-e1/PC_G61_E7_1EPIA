import IP_Data_Abuse as IpDataAbuse
import Keylogger
import PC_PIA_PwGenerator as PwGenerator
import PC_PIA_Shodan as mshodan
from os import system

print('\t\t---Modulos---')
print('1-AbuseIPDB')
print('2-Shodan')
print('3-Keylogger')
print('4-Password Generator')
print('5-PentTest')

while True:
    op = int(input('Ingrese la opcion a usar: '))
    if 1<= op <=5:
        match op:
            case 1:
                system('cls')
                print('Funciones: ')
                print('[1]Reportar una ip')
                print('[2]Consultar sobre una ip')
                op2 = int(input('Ingrese la opcion a usar: '))
                match op2:
                    case 1:
                        system('cls')
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
                        system('cls')
                        print('\t\t--Consultar IP--')
                        ip = input('Ip (ejemplo: 8.8.8.8): ')
                        try:
                            print(IpDataAbuse.ip_query(ip))
                        except Exception as e:
                            print(f'Error: {e}')
                        break
                break
            case 2:
                system('cls')
                try:
                    mshodan.shodan_module()
                except Exception as e:
                            print(f'Error: {e}')
                break
            case 3:
                system('cls')
                print('Funciones: ')
                print('[1]Keylogger')
                print('[2]Grabar/Usar macros')
                op2 = int(input('Ingrese la opcion a usar: '))
                match op2:
                    case 1:
                        system('cls')
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
            case 4:
                system('cls')
                try: 
                    PwGenerator.password_generator()
                except Exception as e:
                            print(f'Error: {e}')
                break
            case 5:
                break
