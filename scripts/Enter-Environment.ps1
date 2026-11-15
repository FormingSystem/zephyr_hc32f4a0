# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$dependencyLock = Get-Content -LiteralPath (Join-Path $projectRoot 'dependencies.lock.json') -Raw |
    ConvertFrom-Json
$localEnvironment = $null
$localEnvironmentFile = Join-Path $projectRoot '.local/environment.json'
if (Test-Path -LiteralPath $localEnvironmentFile) {
    $localEnvironment = Get-Content -LiteralPath $localEnvironmentFile -Raw | ConvertFrom-Json
}
$zephyrRoot = $projectRoot
if (-not (Test-Path -LiteralPath (Join-Path $zephyrRoot 'VERSION'))) {
    throw 'The project checkout is missing its Zephyr source.'
}
$zephyrRoot = (Resolve-Path -LiteralPath $zephyrRoot).Path
$westWorkspace = Split-Path -Parent $zephyrRoot
$pythonEnvironment = Join-Path $projectRoot '.venv'
$pythonScripts = Join-Path $pythonEnvironment 'Scripts'
if (-not (Test-Path -LiteralPath (Join-Path $pythonScripts 'python.exe'))) {
    throw 'Create the repository .venv using scripts/setup_environment.py first.'
}
$sdkRoot = $env:ZEPHYR_SDK_INSTALL_DIR
if (-not $sdkRoot -and $localEnvironment) { $sdkRoot = $localEnvironment.sdk_root }
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
# This checkout contains all target modules; never discover a sibling workspace.
$env:ZEPHYR_MODULES = (@(
    (Join-Path $projectRoot 'modules/hal/cmsis_6'),
    (Join-Path $projectRoot 'modules/hal/xhsc')
) -join ';').Replace('\', '/')
foreach ($moduleVariable in @('EXTRA_ZEPHYR_MODULES', 'ZEPHYR_EXTRA_MODULES')) {
    [Environment]::SetEnvironmentVariable($moduleVariable, $null, 'Process')
}
Set-Location -LiteralPath $projectRoot
Write-Host "Development repository: $projectRoot"
Write-Host "Zephyr source:          $env:ZEPHYR_BASE"
Write-Host "SDK:                    $env:ZEPHYR_SDK_INSTALL_DIR"
Write-Host 'Commands: python scripts/project.py doctor | check | build | test | debug'
