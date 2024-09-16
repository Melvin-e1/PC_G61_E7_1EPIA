<#
.SYNOPSIS
    Genera un respaldo de un directorio
.DESCRIPTION
    Genera un respaldo de un directorio cuya ruta es definifa por el usuario
.NOTES
    El modulo usa el manejo de errores y excepciones así como el modo estricto y la ayuda mediante get-help.
    Al definir la ruta donde se va a guardar, verificar que la ruta exista en su computadora.
.EXAMPLE
    Ejemplo de ruta del directorio a ingresar: "\Users\DELL\Documents\TAREAS_PREPA_4TO"
    Siendo el directorio "TAREAS_PREPA_4TO" el que se va a duplicar
#>

Set-StrictMode -Version Latest

function Duplicate-Dir{
    $Main = Read-Host "Ingrese dirección del directorio"
    $MainRoute = "$Main"
    #Ya depende de donde lo quieras pero aquí se va a guardar el respaldo
    #Por predeterminado, pq creo que la ruta se puede crear ahí en todas las compus
    $BackupRoute =  "C:\Backup"

    #Revisa si el directorio en el que se respaldará la info, existe
    #Si no existe, lo crea
    if (-not (Test-Path -Path $BackupRoute)) {
        New-Item -ItemType Directory -Path $BackupRoute
    }

    #Obtiene los archivos de el directorio original
    $MainFiles = Get-ChildItem -Path $MainRoute

    #Para cada archivo del directorio define su ruta en el nuevo directorio
    
    try{
        foreach ($file in $MainFiles) {
            $BackupFilePath = Join-Path $BackupRoute $file.Name

            #Revisa si el archivo ya existe en el respaldo
            if (Test-Path -Path $BackupFilePath) {
                #Si ya existe revisa si se ha editado desde que se guardó
                if ($file.LastWriteTime -gt (Get-Item $BackupFilePath).LastWriteTime) {
                    #Si sí se editó, lo vuelve a guardar, ahora teniendo el archivo más actualizado
                    Copy-Item -Path $file.FullName -Destination $BackupFilePath -Force
                }
            } else {
                #Si el archivo no existe en el respaldo todavía, lo crea
                Copy-Item -Path $file.FullName -Destination $BackupFilePath
            }
        }
    } 
    catch{
        Write-Host "Ocurrió un error, vuelva a ejecutar la función"
    }
}