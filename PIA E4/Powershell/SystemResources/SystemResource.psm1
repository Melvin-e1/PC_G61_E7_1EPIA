<#
.SYNOPSIS
    Revisa el uso de recursos de memoria, disco, procesador y red
.DESCRIPTION
    Este modulo está conformado por 4 funciones, al llamarlas verifica el uso de recursos de distintos componentes
.NOTES
    El modulo usa el manejo de errores y excepciones así como el modo estricto y la ayuda mediante get-help. 
.EXAMPLE
    Al momento de ingresar la opción deseada, poner 2 para los recursos de disco
#>

Set-StrictMode -Version Latest

#Memoria
function Mem-Res {
    try{
        $memoria = Get-WmiObject -Class Win32_OperatingSystem | Select-Object FreePhysicalMemory, TotalVisibleMemorySize
        #$memoria | Format-List
    } catch {
        Write-Host "Ocurrió un problema al ejecutar la función, inténtelo de nuevo."
    }

    $reportpath = "C:\Results\MemoryRes_report.txt"
    $memoria | Out-File -FilePath $reportpath

    #consigue la clave HASH del reporte
    $hash = Get-FileHash -Path $reportpath -Algorithm SHA256

    $date = Get-Date
    #Informacion en terminal
    Write-Host "Fecha: $date"
    Write-Host "HASH del reporte: $hash"
    Write-Host "Nombre del reporte: MemoryRes_report.txt"
    Write-Host "Ubicacion del reporte: $reportpath"
}

#Disco
function SSD-Res {
    try{
        $disco = Get-WmiObject -Class Win32_LogicalDisk | Select-Object DeviceID, FreeSpace, Size
        #$disco | Format-List
    } catch{
        Write-Host "Ocurrió un problema al ejecutar la función, inténtelo de nuevo."
    }

    $reportpath = "C:\Results\SSDRes_report.txt"
    $disco | Out-File -FilePath $reportpath

    #consigue la clave HASH del reporte
    $hash = Get-FileHash -Path $reportpath -Algorithm SHA256

    $date = Get-Date
    #Informacion en terminal
    Write-Host "Fecha: $date"
    Write-Host "HASH del reporte: $hash"
    Write-Host "Nombre del reporte: SSDRes_report.txt"
    Write-Host "Ubicacion del reporte: $reportpath"
}

#Procesador
function CPU-Res {
    try{
        $procesador = Get-WmiObject Win32_Processor | Measure-Object -Property LoadPercentage -Average
        $porcentaje = $procesador.Average
       # Write-Host 'Porcentaje de uso: '
        #"$porcentaje%"

    } catch {
        Write-Host "Ocurrió un problema al ejecutar la función, inténtelo de nuevo."
    }

    $reportpath = "C:\Results\CPURes_report.txt"
    $porcentaje | Out-File -FilePath $reportpath

    #consigue la clave HASH del reporte
    $hash = Get-FileHash -Path $reportpath -Algorithm SHA256

    $date = Get-Date
    #Informacion en terminal
    Write-Host "Fecha: $date"
    Write-Host "HASH del reporte: $hash"
    Write-Host "Nombre del reporte: CPURes_report.txt"
    Write-Host "Ubicacion del reporte: $reportpath"
}

#Red
#En este se puede usar el que está puesto o el que está comentarizado
#El que está comentarizado da mucha información, por eso dejé el otro
function Net-Res {
    try{
        $red = netstat -e
        #$red = Get-NetAdapterStatistics
        #$red | Format-List
    } catch{
        Write-Host "Ocurrió un problema al ejecutar la función, inténtelo de nuevo."
    }

    $reportpath = "C:\Results\NetworkRes_reporte.txt"
    $result | Out-File -FilePath $reportpath

    #consigue la clave HASH del reporte
    $hash = Get-FileHash -Path $reportpath -Algorithm SHA256

    $date = Get-Date
    #Informacion en terminal
    Write-Host "Fecha: $date"
    Write-Host "HASH del reporte: $hash"
    Write-Host "Nombre del reporte: NetworkRes_reporte.txt"
    Write-Host "Ubicacion del reporte: $reportpath"
}


