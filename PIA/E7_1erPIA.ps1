<# 
    .SYNOPSIS
    Script donde se puede ejecutar multiples modulos

    .DESCRIPTION
    Menu que permite una facil ejecucion de multiples modulos y sus funciones correspondientes

    .EXAMPLE
    cd "C:\Ruta\Al\Script"
    .\E7_1erPIA.ps1

    .NOTES
    Autores: Equipo 7 ;)
#>

#Modulos usados
Import-Module HiddenFile
Import-Module VirusTotal2
Import-Module SystemResource
Import-Module Duplicate-Dir
clear

#Menu de modulos
function Menu {
    Write-Host "Modulos"
    Write-Host "1: Revisión de hashes de archivos y consulta de la API VirusTotal"
    Write-Host "2: Listado de archivos ocultos"
    Write-Host "3: Revisión de uso de recursos del sistema"
    Write-Host "4: Respaldo de archivos de una carpeta"
    Write-Host "5: Salir" 
    
}

function Main{
    #Con este while se impide el cierre del programa tras un fallo, haciendo que la unica forma de cerrarlo sea usando la opcion 5 en el switch
    while ($true){
        Menu
        #Mediante el uso del Switch se usan los modulos y las funciones que el usuario elija 
        $opt = Read-Host "Ingrese el modulo a usar"
        Switch ($opt) {
            #Modulo de revision de Hashes
            1 { Clear  
                #Menu de funciones del modulo
                Write-Host 'VirusTotal: '
                Write-Host '[1]Get-FileHash'
                Write-Host '[2]CheckFileHash'
                $opt2 = Read-Host "Funcion a usar"

                Switch ($opt2){ 
                    1{
                        #Para todas las funciones de los modulos se usa un try en caso de falle la ejecucion de dicha funcion y senala el error que ocurrio
                        try{
                            Get-FileHash

                        } catch{
                            Write-Host "Error al ejecutar: $_"
                        }
                     }
                    2{
                        try{
                            CheckFileHash
                        } catch{
                            Write-Host "Error al ejecutar: $_"
                        }
                 
                     }
                    default {Write-Host "Opcion no valida"}
                    }
                }

            #Modulo de Listado de archivos ocultos
            2 { Clear
                try{
                    HiddenFile
                } catch {
                    Write-Host "Error al ejecutar: $_"
                }
              
              
              }
            #Modulo de revision de uso de recursos del sistema
            3 { Clear
                #Menu de funciones del modulo
                Write-Host("Uso de recursos de:`n    1)Memoria"  )
                Write-Host ("    2)Disco")
                Write-Host ("    3)Procesador")
                Write-Host ("    4)Red")
                $opt3 = Read-Host "Ingrese la opción deseada"
                switch ($opt3) {
                    1{ 
                        try{
                            Mem-Res
                        } catch {
                            Write-Host "Error al ejecutar: $_"
                        } 
                     }
                    2{ 
                        try{
                            SSD-Res
                        } catch {
                            Write-Host "Error al ejecutar: $_"
                        }
                     }
                    3{ 
                        try{
                            CPU-Res 
                        } catch {
                            Write-Host "Error al ejecutar: $_"
                        }
                     }
                    4{ 
                        try{
                            Net-Res 
                        } catch {
                            Write-Host "Error al ejecutar: $_"
                        }
                     }
                }
                  
              }
            #Modulo de Respaldo de archivos
            4{ Clear
               try{ 
                    Duplicate-Dir
               } catch {
                    Write-Host "Error al ejecutar: $_"
               }
             }
            #Cierre del script
            5 { write-host "bye"; exit }
            default {Write-Host "Opcion no valida"}
            }
            #Cuando algo falle o despues del uso de alguna funcion el script se espera 3 segundos y despues borra pantalla para volver a mostrar el menu de modulos
            Start-Sleep -Seconds 3
            clear
        }
    }
    #MAIN ;)
    Main
