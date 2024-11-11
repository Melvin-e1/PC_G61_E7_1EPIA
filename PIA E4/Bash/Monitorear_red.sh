#!/bin/bash

# Funcion que monitorea el trafico de red utilizando iftop
function monitor_netTraffic() {
    local interface=$1
    local report_file="trafico_red_${interface}_$(date +%Y%m%d_%H%M%S).txt"
    
    if [[ -z $interface ]]; then
        echo "Error: No se selecciono una interfaz de red."
        return 1
    fi

    if ! command -v iftop &> /dev/null; then
        echo "Error: no tienes iftop instalado, por favor instalalo con el siguiente comando 'sudo apt install iftop' e intentalo de nuevo."
        return 1
    fi

    echo "Monitoreando la red en la interfaz: $interface"
    sudo iftop -i "$interface" -t -s 10 > "$report_file"

    # Calcular el hash del archivo
    local hash=$(sha256sum "$report_file" | awk '{print $1}')
    echo "Se ejecuto la tarea de monitoreo en la interfaz $interface el $(date)."
    echo "Hash del reporte: $hash"
    echo "Nombre del archivo: $report_file"
    echo "Ubicacion del archivo: $(realpath "$report_file")"
}

# Funcion para generar un reporte del trafico de red usando iftop
function generate_report() {
    local interface=$1
    local report_file=$2
    if [[ -z $interface ]]; then
        echo "Error: NO se selecciono una interfaz de red para el reporte."
        return 1
    fi

    # Validar que el archivo sea un txt
    if [[ ! $report_file =~ \.txt$ ]]; then
        echo "Error: el nombre del archivo debe terminar con .txt"
        return 1
    fi

    echo "Generando reporte en la interfaz: $interface "

    sudo iftop -i "$interface" -t -s 10 > "$report_file"

    # Calcular el hash del archivo
    local hash=$(sha256sum "$report_file" | awk '{print $1}')
    echo "Se ejecuto la tarea de generacion de reporte en la interfaz $interface el $(date)."
    echo "Hash del reporte: $hash"
    echo "Nombre del archivo: $report_file"
    echo "Ubicacion del archivo: $(realpath "$report_file")"
}

# Funcion para manejar los errores de datos de entrada en el menu
function handle_error() {
    echo "Opcion invalida, ingresa alguna de las opciones validas."
}

# Funcion para validar la entrada de la interfaz de red
function validate_interface() {
    local interface=$1
    if [[ "$interface" != "wlan0" && "$interface" != "eth0" ]]; then
        echo "Error. La interfaz de red ingresada es invalida"
        return 1
    fi
    return 0
}

function validate_new_interface() {
    local new_interface=$1
    if [[ "$new_interface" != "wlan0" && "$new_interface" != "eth0" ]]; then
        echo "Error. La interfaz de red ingresada es invalida"
        return 1
    fi
    return 0
}

# Funcion para mostrar el menu principal
function main_menu() {
    while true; do
        echo "==== Script para Monitorear la red ===="
        echo "1. Monitorear el Trafico de Red"
        echo "2. Generar Reporte de Trafico de Red"
        echo "3. Correr de nuevo el monitoreo con otros parametros"
        echo "4. Salir"
        read -p "Elige una opcion: " op

        case $op in
            1)
                read -p "Introduce la interfaz de red (por ejemplo: wlan0, eth0): " interface
                if validate_interface "$interface"; then
                    monitor_netTraffic "$interface"
                fi
                ;;
            2)
                read -p "Ingresa la interfaz de red para el reporte (por ejemplo: wlan0, eth0): " interface
                if validate_interface "$interface"; then
                    read -p "Ingresa el nombre que le deseas poner al reporte seguido de .txt (Por ejemplo: mireporte.txt): " report_file
                    generate_report "$interface" "$report_file"
                fi
                ;;
            3)
                read -p "Ingresa la nueva interfaz de red: " new_interface
                if validate_new_interface "$new_interface"; then
                    monitor_netTraffic "$new_interface"
                fi
                ;;
            4)
                echo "Saliendo del script."
                exit 0
                ;;
            *)
                handle_error
                ;;
        esac
    done
}

# Ejecucion principal del programa
if [[ $EUID -ne 0 ]]; then
    echo "Este script debe ejecutarse con privilegios o como root."
    exit 1
fi

main_menu
