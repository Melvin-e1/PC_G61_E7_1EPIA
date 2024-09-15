#Establecer el modo estricto
Set-StrictMode -Version Latest

$apikey="30c8e2f455b2e09df2b917773e379b92c32c7aadca54d01f51f826184c17cee3"
#Ayuda del modulo
<#
.SINOPSIS
    revisa los hashes de archivos locales y los consulta en la API de VirusTotal
.DESCRIPCION
    Este modulo genera el hash del archivo local especificado por el usuario y lo consulta en la API de VirusTotal para comprobar si han sido reportados como maliciosos
.PARAMETRO FilePath
    Es la direccion del archivo cuyo hash se desea generar o consultar en la API
.PARAMETRO Hashtype
    Es el tipo de hash que se desea generar ya sea MD5, SHA1 o SHA256
.EJEMPLO
    CheckFileHash -FilePath "C:\Direccion del archivo" (donde "Direccion del archivo" es la direccion completa del archivo a ejecutar con su extension)
.NOTAS
    El modulo usa el manejo de errores y excepciones asi como el modo estricto y la ayuda mediante get-help. 
#>
function Get-FileHash {
    [CmdletBinding()]
    param(
    [Parameter(Mandatory = $true, HelpMessage = "Ingresa la direccion del archivo: ")]
    [string]$FilePath,

    [string]$HashType
    )

    try {
        if (-not (Test-Path -Path $FilePath)) {
            throw "El archivo no existe: $FilePath"
        }

        #validar el tipo de hash y si no esta bien definido solicitarlo
        if (-not $HashType) {
            $HashTypes = @("MD5", "SHA1", "SHA256")
            Write-Host "Selecciona el tipo de hash: "
            for ($i = 0; $i -lt $HashTypes.Count; $i++) {
                Write-Host "$($i + 1). $($hashTypes[$i])"
            }

            $selection = Read-Host "Ingrese el numero de la opcion que desea: "

            if ($selection -match '^[0-9]+$' -and $selection -ge 1 -and $selection -le $HashTypes.Count) {
                $HashType = $HashTypes[$selection - 1]
            }
            else {
                throw "Seleccion invalida. Ingrese un numero del 1 al $($HashTypes.Count)."
            }
        }

        #Seleccionar el algoritmo de hash adecuado
        $HashAlgorithm = switch ($HashType) {
            "MD5"    { [System.Security.Cryptography.MD5]::Create() }
            "SHA1"   { [System.Security.Cryptography.SHA1]::Create() }
            "SHA256" { [System.Security.Cryptography.SHA256]::Create() }
            default  { throw "Algoritmo de hash no soportado: $HashType" }
        }

        #Leer el archivo en formato binario
        $fileBytes = [System.IO.File]::ReadAllBytes($FilePath)

        #Obtener el hash del arcghivo
        $HashBytes = $HashAlgorithm.ComputeHash($fileBytes)
        $hashString = [BitConverter]::ToString($HashBytes) -replace '-', ''

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

        [string]$HashType
    )

    try {
        #verificar que el archivo exista
        if (-not (Test-Path -Path $FilePath)) {
            throw "El archivo no existe: $FilePath"
        }

        #validar que el hash este definido
        if (-not $HashType) {
            $hashTypes = @("MD5", "SHA1", "SHA256")
            Write-Host "Seleccione el tipo de hash: "
            for ($i = 0; $i -lt $hashTypes.Count; $i++) {
                Write-Host "$($i + 1). $($hashTypes[$i])"
            }

            $selection = Read-Host "Ingrese el número de la opción deseada"

            if ($selection -match '^[0-9]+$' -and $selection -ge 1 -and $selection -le $hashTypes.Count) {
                $HashType = $hashTypes[$selection - 1]
            }
            else {
                throw "Selección inválida. Debe ingresar un número del 1 al $($hashTypes.Count)."
            }
        }

        #Obtener el hash del archivo
        $fileHash = Get-FileHash -FilePath $FilePath -HashType $HashType
        if (-not $fileHash) {
            throw "No se pudo calcular el hash del archivo."
        }

        Write-Host "hash del archivo ($HashType): $fileHash"

        $url = "https://www.virustotal.com/vtapi/v2/file/report?apikey=$apikey&resource=$fileHash"

        #Realizar la solicitud a la API de VirusTotal
        $response = Invoke-RestMethod -Uri $url -Method Get -ErrorAction Stop

        if ($response.response_code -eq 1) {
            Write-Host "Resultado de VirusTotal:"
            Write-Host "Positivos: $($response.positives)"
            Write-Host "Total de analisis: $($response.total)"
        }
        else {
            Write-Host "El archiv no se encuentra en la base de datos de VirusTotal"
        }
    }
    catch {
        Write-Host "Error al consultar VirusTotal: $_" -ForegroundColor Red
    }
}

#Exportar funciones
Export-ModuleMember -Function Get-FileHash, CheckFileHash

