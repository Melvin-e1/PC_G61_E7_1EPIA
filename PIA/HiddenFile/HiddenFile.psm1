Function HiddenFile {
    <#
    .Synopsis
    Busca archivos ocultos en una carpeta/directorio

    .Description
    El usuario ingresa un ruta para poder inspeccionar dentro de una carpeta/directorio en especifico la existencia de archivos ocultos

    .Parameter path
    Ruta especifica de la carpeta a inspeccionar

    .Example 
    HiddenFile -path C:\Users\pepit\Desktop\Uni
     #>
    param( 
        [Parameter (Mandatory)]
        [string] $path
    )

    #Verifica la existencia de la ruta
    try {
        if (-Not (Test-Path -Path $path)) {
            throw "La ruta no existe: $path"
        }
        #Obtiene los archivos ocultos con el parametro hidden en la ruta dada en el caso que exista
        Get-ChildItem -Path $path -Hidden
    }
    #Si no existe se lanza un Exception.message y posteriormente se pide ingresar una nueva ruta
    catch {
        Write-Output ($_.Exception.Message)
        $NewPath = Read-Host -Prompt "Intente nuevamente"
        #se manda a llamar asi mismo con la nueva ruta
        HiddenFile -path $NewPath
    }
}