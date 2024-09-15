Import-Module HiddenFile
Import-Module VirusTotal2

#Menu de modulos
Write-Host "Modulos"
Write-Host "1: Revisión de hashes de archivos y consulta de la API VirusTotal"
Write-Host "2: Listado de archivos ocultos"
Write-Host "3: Revisión de uso de recursos del sistema"
Write-Host "4: Módulo 4"
Write-Host "5: Salir" 

$opt = Read-Host "Ingrese el modulo a usar: "

Switch ($opt) {
    1 { Clear  
        Write-Host 'VirusTotal: '
        Write-Host '[1]Get-FileHash'
        Write-Host '[2]CheckFileHash'
        $opt2 = Read-Host "Funcion a usar: "
        Switch ($opt2){ 
        1{Get-FileHash}
        2{Check-FileHash}
        }
        }

    2 { Clear; HiddenFile }
    3 { Clear; }
       
    4 { Clear; }
    5 { write-host "bye"; break }
    default {Write-Host "Opcion no valida"}
    }