# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$dependencyLock = Get-Content -LiteralPath (Join-Path $projectRoot 'dependencies.lock.json') -Raw |
    ConvertFrom-Json
$zephyrRoot = $env:ZEPHYR_BASE
if (-not $zephyrRoot) {
    $zephyrRoot = Join-Path (Split-Path -Parent $projectRoot) 'zephyr'
}
if (-not (Test-Path -LiteralPath (Join-Path $zephyrRoot 'VERSION'))) {
    throw 'Set ZEPHYR_BASE to the prepared Zephyr source directory.'
}
$zephyrRoot = (Resolve-Path -LiteralPath $zephyrRoot).Path
$westWorkspace = Split-Path -Parent $zephyrRoot
$pythonEnvironment = $env:VIRTUAL_ENV
if (-not $pythonEnvironment) { $pythonEnvironment = Join-Path $westWorkspace '.venv' }
$pythonScripts = Join-Path $pythonEnvironment 'Scripts'
if (-not (Test-Path -LiteralPath (Join-Path $pythonScripts 'python.exe'))) {
    throw 'Set VIRTUAL_ENV to a Python environment containing Zephyr dependencies.'
}
$sdkRoot = $env:ZEPHYR_SDK_INSTALL_DIR
if (-not $sdkRoot) {
    $sdkRoot = Join-Path (Split-Path -Parent $westWorkspace) ('zephyr-sdk-' + $dependencyLock.sdk.version)
}
$armBin = Join-Path $sdkRoot 'gnu\arm-zephyr-eabi\bin'
if (-not (Test-Path -LiteralPath (Join-Path $armBin 'arm-zephyr-eabi-gcc.exe'))) {
    throw 'Set ZEPHYR_SDK_INSTALL_DIR to the prepared Zephyr SDK.'
}
$pathEntries = @($pythonScripts, $armBin, (Join-Path $sdkRoot 'hosttools\qemu'),
    (Join-Path $sdkRoot 'hosttools\openocd\bin'))
$pathEntries += ($env:Path -split ';')
$pathEntries += ([Environment]::GetEnvironmentVariable('Path', 'User') -split ';')
$pathEntries += ([Environment]::GetEnvironmentVariable('Path', 'Machine') -split ';')
$env:Path = ($pathEntries | Where-Object { $_ } | Select-Object -Unique) -join ';'
$env:VIRTUAL_ENV = $pythonEnvironment
$env:PYTHONUTF8 = '1'
$env:ZEPHYR_BASE = $zephyrRoot
$env:ZEPHYR_SDK_INSTALL_DIR = (Resolve-Path -LiteralPath $sdkRoot).Path
$env:ZEPHYR_TOOLCHAIN_VARIANT = 'zephyr'
# Use Zephyr's current variable name; preserve other user-selected extra modules.
$misplacedRoot = Join-Path $zephyrRoot '_hc32f4a0'
foreach ($moduleVariable in @('EXTRA_ZEPHYR_MODULES', 'ZEPHYR_EXTRA_MODULES')) {
    $currentModules = [Environment]::GetEnvironmentVariable($moduleVariable, 'Process') -split ';'
    # Discard the exact stale entry left by relocating this checkout.
    $currentModules = @($currentModules | Where-Object {
        $_ -and [IO.Path]::GetFullPath($_) -ne $misplacedRoot
    })
    [Environment]::SetEnvironmentVariable($moduleVariable, ($currentModules -join ';'), 'Process')
}
$extraModules = @($projectRoot) + ($env:EXTRA_ZEPHYR_MODULES -split ';')
$env:EXTRA_ZEPHYR_MODULES = ($extraModules | Where-Object { $_ } | Select-Object -Unique) -join ';'
Set-Location -LiteralPath $projectRoot
Write-Host "Development repository: $projectRoot"
Write-Host "Zephyr dependency:      $env:ZEPHYR_BASE"
Write-Host "SDK:                    $env:ZEPHYR_SDK_INSTALL_DIR"
Write-Host 'Commands: python scripts/project.py doctor | check | build | test | debug'
