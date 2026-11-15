# SPDX-License-Identifier: Apache-2.0
#requires -Version 5.1
[CmdletBinding()]
param([ValidateSet('Bash', 'PowerShell', 'CMD')][string]$Shell = 'Bash')
$ErrorActionPreference = 'Stop'
$repo = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..'))
Import-Module (Join-Path $PSScriptRoot 'Environment.psm1') -Force -DisableNameChecking
$config = Read-Json (Join-Path $repo '.local\windows\installation.json')
$before = Get-RawEnvironment 'Process'
try {
    $env:Path = @((Join-Path $repo '.venv\Scripts'), (Join-Path $config.sdk 'gnu\arm-zephyr-eabi\bin'), (Join-Path $config.sdk 'hosttools\qemu'), (Join-Path $config.sdk 'hosttools\openocd\bin'), (Split-Path $config.git), (Split-Path $config.python), (Join-Path $config.msysRoot 'ucrt64\bin'), (Join-Path $config.msysRoot 'usr\bin'), $before['Path']) -join ';'
    $env:VIRTUAL_ENV = Join-Path $repo '.venv'
    $env:ZEPHYR_BASE = $repo
    $env:ZEPHYR_SDK_INSTALL_DIR = $config.sdk
    $env:ZEPHYR_TOOLCHAIN_VARIANT = 'zephyr'
    $env:MSYSTEM = 'UCRT64'; $env:MSYS2_PATH_TYPE = 'inherit'; $env:CHERE_INVOKING = '1'
    $env:PYTHONUTF8 = '1'; $env:PYTHONHOME = $null; $env:PYTHONPATH = $null
    $env:PIP_CACHE_DIR = Join-Path $config.downloads 'pip'
    $env:TEMP = Join-Path $config.downloads 'tmp'; $env:TMP = $env:TEMP
    # Login profiles prepend UCRT64; restore Windows Python/MinGit priority afterwards.
    $env:HC32_WINDOWS_PATH = $env:Path
    Push-Location $repo
    try {
        switch ($Shell) {
            'Bash' {
                & (Join-Path $config.msysRoot 'usr\bin\bash.exe') --login (Join-Path $PSScriptRoot 'enter.sh').Replace('\', '/')
            }
            'PowerShell' { & powershell.exe -NoLogo -NoProfile -NoExit }
            'CMD' { & $env:ComSpec /d }
        }
    } finally { Pop-Location }
    exit $LASTEXITCODE
} finally {
    foreach ($name in @('Path', 'VIRTUAL_ENV', 'ZEPHYR_BASE', 'ZEPHYR_SDK_INSTALL_DIR', 'ZEPHYR_TOOLCHAIN_VARIANT', 'MSYSTEM', 'MSYS2_PATH_TYPE', 'CHERE_INVOKING', 'PYTHONUTF8', 'PYTHONHOME', 'PYTHONPATH', 'PIP_CACHE_DIR', 'TEMP', 'TMP', 'HC32_WINDOWS_PATH')) {
        [Environment]::SetEnvironmentVariable($name, $before[$name], 'Process')
    }
}
