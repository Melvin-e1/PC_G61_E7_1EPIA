<#
.SYNOPSIS
    Revisa los hashes de archivos locales y los consulta en la API de VirusTotal.
.DESCRIPTION
    Este modulo genera el hash del archivo local especificado por el usuario y lo consulta en la API de VirusTotal para comprobar si ha sido reportado como malicioso.
#>

#Se usa mi clave para mayor facilidad y no tener que solicitar crear una cuenta en VirusTotal y demas
$apikey = "30c8e2f455b2e09df2b917773e379b92c32c7aadca54d01f51f826184c17cee3"

function Get-FileHash {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, HelpMessage = "Ingresa la direccion del archivo: ")]
        [string]$FilePath,

        [Parameter(HelpMessage = "Tipo de hash a generar: MD5, SHA1 o SHA256.")]
        [string]$HashType
    )

    <#
    .SYNOPSIS
        Genera el hash de un archivo local que ingreses.

    .DESCRIPTION
        Esta funcion calcula el hash de un archivo local utilizando el tipo de hash especificado (MD5, SHA1 o SHA256) y genera un reporte en un archivo de texto.

    .PARAMETER FilePath
        La ruta completa del archivo cuyo hash se desea calcular.

    .PARAMETER HashType
        El tipo de hash a calcular (MD5, SHA1 o SHA256), si no se especifica se solicitara al usuario que elija uno.

    .OUTPUTS
        Devuelve el hash del archivo como una cadena.

    .EXAMPLE
        Get-FileHash -FilePath "C:\ruta\al\archivo.exe" -HashType "SHA256"
    #>

    try {
        if (-not (Test-Path -Path $FilePath)) {
            throw "El archivo no existe: $FilePath"
        }

        if (-not $HashType) {
            $HashTypes = @("MD5", "SHA1", "SHA256")
            Write-Host "Selecciona el tipo de hash: "
            for ($i = 0; $i -lt $HashTypes.Count; $i++) {
                Write-Host "$($i + 1). $($HashTypes[$i])"
            }

            $selection = Read-Host "Ingrese el numero de la opción deseada: "

            if ($selection -match '^[0-9]+$' -and $selection -ge 1 -and $selection -le $HashTypes.Count) {
                $HashType = $HashTypes[$selection - 1]
            }
            else {
                throw "Seleccion invalida. Debe ingresar un numero del 1 al $($HashTypes.Count)."
            }
        }

        $HashAlgorithm = switch ($HashType) {
            "MD5"    { [System.Security.Cryptography.MD5]::Create() }
            "SHA1"   { [System.Security.Cryptography.SHA1]::Create() }
            "SHA256" { [System.Security.Cryptography.SHA256]::Create() }
            default  { throw "Algoritmo de hash no soportado: $HashType" }
        }

        $fileBytes = [System.IO.File]::ReadAllBytes($FilePath)
        $HashBytes = $HashAlgorithm.ComputeHash($fileBytes)
        $hashString = [BitConverter]::ToString($HashBytes) -replace '-', ''

        # Generar reporte en formato .txt
        $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
        $reportFile = "C:\Reports\FileHashReport_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
        New-Item -Path $reportFile -ItemType File -Force | Out-Null

        $reportContent = @(
            "Reporte de Generación de Hash - $timestamp",
            "Archivo: $FilePath",
            "Hash ($HashType): $hashString"
        )

        # Guardar contenido en el archivo de reporte
        $reportContent | Out-File -FilePath $reportFile -Encoding UTF8

        # Generar hash del archivo de reporte para verificacion
        $reportHash = [System.Security.Cryptography.SHA256]::Create().ComputeHash([System.IO.File]::ReadAllBytes($reportFile))
        $reportHashString = [BitConverter]:: ToString($reportHash) -replace '-', ''

        # Mostrar mensaje en terminal con detalles de la tarea ejecutada
        Write-Host "La tarea Get-FileHash se ejecuto en $timestamp" -ForegroundColor Green
        Write-Host "Hash del reporte: $reportHashString" -ForegroundColor Green
        Write-Host "Reporte generado en: $reportFile" -ForegroundColor Green

        return $hashString
    }
    catch {
        Write-Host "Error al generar el hash: $_" -ForegroundColor Red
        return $null
    }
}

function CheckFileHash {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, HelpMessage = "Ingresa la direccion del archivo: ")]
        [string]$FilePath,

        [Parameter(HelpMessage = "Tipo de hash a verificar: MD5, SHA1 o SHA256")]
        [string]$HashType
    )

    <#
    .SYNOPSIS
        Verifica el hash de un archivo en VirusTotal.

    .DESCRIPTION
        Esta funcion consulta la API de VirusTotal para verificar si el hash de un archivo ha sido reportado como malicioso.

    .PARAMETER FilePath
        La ruta completa del archivo cuyo hash se desea verificar.

    .PARAMETER HashType
        El tipo de hash a verificar (MD5, SHA1 o SHA256), si no se especific se solicitara al usuario que elija uno.

    .OUTPUTS
        No devuelve valores pero genera un reporte en un archivo de texto

    .EXAMPLE
        CheckFileHash -FilePath "C:\ruta\al\archivo.exe" -HashType "SHA256"
    #>

    try {
        if (-not (Test-Path -Path $FilePath)) {
            throw "El archivo no existe: $FilePath"
        }

        if (-not $HashType) {
            $hashTypes = @("MD5", "SHA1", "SHA256")
            Write-Host "Seleccione el tipo de hash: "
            for ($i = 0; $i -lt $hashTypes.Count; $i++) {
                Write-Host "$($i + 1). $($hashTypes[$i])"
            }

            $selection = Read-Host "Ingrese el numero de la opcion deseada"

            if ($selection -match '^[0-9]+$' -and $selection -ge 1 -and $selection -le $hashTypes.Count) {
                $HashType = $hashTypes[$selection - 1]
            }
            else {
                throw "Seleccion invalida. Debe ingresar un numero del 1 al $($hashTypes.Count)."
            }
        }

        $fileHash = Get-FileHash -FilePath $FilePath -HashType $HashType
        if (-not $fileHash) {
            throw "No se pudo calcular el hash del archivo."
        }

        $url = "https://www.virustotal.com/vtapi/v2/file/report?apikey=$apikey&resource=$fileHash"

        $response = Invoke-RestMethod -Uri $url -Method Get -ErrorAction Stop

        $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
        $reportFile = "C:\Reports\VirusTotalReport_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
        New-Item -Path $reportFile -ItemType File -Force | Out-Null

        if ($response.response_code -eq 1) {
            $reportContent = @(
                "Reporte de Analisis de VirusTotal - $timestamp",
                "Archivo: $FilePath",
                "Hash ($HashType): $fileHash",
                "Positivos: $($response.positives)",
                "Total de analisis: $($response.total)"
            )
        }
        else {
            $reportContent = @(
                "Reporte de Analisis de VirusTotal - $timestamp",
                "Archivo: $FilePath",
                "Hash ($HashType): $fileHash",
                "Resultado: El archivo no se encuentra en la base de datos de VirusTotal"
            )
        }

        $reportContent | Out-File -FilePath $reportFile -Encoding UTF8

        $reportHash = [System.Security.Cryptography.SHA256]::Create().ComputeHash([System.IO.File]::ReadAllBytes($reportFile))
        $reportHashString = [BitConverter]::ToString($reportHash) -replace '-', ''

        Write-Host "La tarea CheckFileHash se ejecuto en $timestamp" -ForegroundColor Green
        Write-Host "Hash del reporte: $reportHashString" -ForegroundColor Green
        Write-Host "Reporte generado en: $reportFile" -ForegroundColor Green
    }
    catch {
        Write-Host "Error al consultar VirusTotal: $_" -ForegroundColor Red
    }
}

Export-ModuleMember -Function Get-FileHash, CheckFileHash