#!/bin/bash

#Nada tiene acentos porque lo considero no importante de aprenderme del teclado en ingles
#Pero si quieren cambiarlo, adelante

#Funcion para mostrar el menu
popup_menu() {
  echo "Selecciona una opcion:"
  echo "1) Escanear puertos con nmap"
  echo "2) Mostrar IP"
  echo "3) Salir"
}

#Funci[on de escaneo de puertos con nmap
#No puse que que sean todos los puertos porque se me hacian muchos
#Lo bajaba y se seguia tardando, lo dejo en 8080 porque son los importantes
nmapport_scanning(){
  read -p "Introduce la IP a escanear: " ip
  echo "Escaneando puertos de $ip ..."
  echo "Presiona Enter para observar el progreso"
  nmap -p 1-8080 $ip || echo "Error: no se pudo escanear la ip $ip "
}

#Funcion para mostrar la IP local
show_ip(){
  ip addr show | grep 'inet ' | awk '{print $2}' | grep -v '127.0.0.1'
}

while true; do
  popup_menu
  read -p "Elige una opcion: " opcion

  case $opcion in 
    1)
      nmapport_scanning
      ;;
    2)
      echo "La IP del sistema es:"
      show_ip
      echo ""
      ;;
    3)
      echo "Saliendo..."
      exit 0
      ;;
    *)
      echo "Opcion no valida, intentalo de nuevo"
  esac
  echo ""

done
