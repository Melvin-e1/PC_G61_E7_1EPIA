#!/bin/bash

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
  nmap -p 1-8080 $ip || echo "Error: no se pudo escanear la ip $ip " >> PortScan_reporte.txt
}

#Funcion para mostrar la IP local
show_ip(){
  ip addr show | grep 'inet ' | awk '{print $2}' | grep -v '127.0.0.1' >> PortScan_reporte.txt
}

show_help() {
  echo "Uso: $0 [opciones]"
  echo
  echo "Opciones:"
  echo "  -h, --help          Muestra esta ayuda y sale"
  echo "  1) Escanear puertos con nmap"
  echo "  2) Mostrar IP"
  echo "  3) Salir"
  echo
  echo "Ejemplo:"
  echo "  Ejecuta el script sin opciones para acceder al menú."
}

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
  show_help
  exit 0
fi

while true; do
  popup_menu
  read -p "Elige una opcion: " opcion

  case $opcion in 
    1)
      nmapport_scanning
      ;;
    2)
      echo "La IP del sistema es:" >> PortScan_reporte.txt
      show_ip
      echo "" >> PortScan_reporte.txt
      ;;
    3)
      echo "Saliendo..."
      echo "Los resultados fueron guardados en el archivo PortScan_reporte.txt"
      path=$(realpath PortScan_reporte.txt)
      echo "El archivo se encuentra en $path"
      echo "El script se ejecutó el: $(date)"
      hash_sha256=$(sha256sum PortScan_reporte.txt | awk '{print $1}')
      echo "Hash SHA-256 del archivo: $hash_sha256"

      exit 0
      ;;
    *)
      echo "Opcion no valida, intentalo de nuevo"
  esac
  echo ""

done
