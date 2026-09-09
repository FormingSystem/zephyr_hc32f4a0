# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$SdkRoot,
    [string]$Python = 'python'
)

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$sdkDirectory = (Resolve-Path -LiteralPath $SdkRoot).Path
$lock = Get-Content -LiteralPath (Join-Path $projectRoot 'dependencies.lock.json') -Raw |
    ConvertFrom-Json
if (-not (Test-Path -LiteralPath (Join-Path $sdkDirectory 'gnu/arm-zephyr-eabi/bin/arm-zephyr-eabi-gcc.exe'))) {
    throw 'SdkRoot must contain the installed ARM Zephyr SDK toolchain.'
}
if ((Get-Content -LiteralPath (Join-Path $sdkDirectory 'sdk_version') -Raw).Trim() -ne $lock.sdk.version) {
    throw 'The SDK version differs from dependencies.lock.json.'
}
& $Python -c 'import sys; sys.exit(0 if sys.version_info >= (3, 12) else 1)'
if ($LASTEXITCODE -ne 0) { throw 'Python 3.12 or newer is required.' }

$environmentDirectory = Join-Path $projectRoot '.venv'
$environmentPython = Join-Path $environmentDirectory 'Scripts/python.exe'
if (-not (Test-Path -LiteralPath $environmentPython)) {
    & $Python -m venv $environmentDirectory
    if ($LASTEXITCODE -ne 0) { throw 'Creating the Python environment failed.' }
}
& $environmentPython -m pip install -r (Join-Path $projectRoot 'scripts/requirements-base.txt') `
    -r (Join-Path $projectRoot 'requirements-tools.txt')
if ($LASTEXITCODE -ne 0) { throw 'Installing Python build dependencies failed.' }

$localDirectory = Join-Path $projectRoot '.local'
New-Item -ItemType Directory -Path $localDirectory -Force | Out-Null
$localEnvironment = @{ sdk_root = $sdkDirectory; python_environment = $environmentDirectory }
[IO.File]::WriteAllText((Join-Path $localDirectory 'environment.json'),
    ($localEnvironment | ConvertTo-Json) + "`n", [Text.UTF8Encoding]::new($false))
# Folder settings override the shared workspace's initial interpreter selection.
$editorDirectory = Join-Path $projectRoot '.vscode'
New-Item -ItemType Directory -Path $editorDirectory -Force | Out-Null
$editorFile = Join-Path $editorDirectory 'settings.json'
if (-not (Test-Path -LiteralPath $editorFile)) {
    $editorSettings = @{ 'python.defaultInterpreterPath' = $environmentPython }
    [IO.File]::WriteAllText($editorFile, ($editorSettings | ConvertTo-Json) + "`n",
        [Text.UTF8Encoding]::new($false))
}
$env:VIRTUAL_ENV = $environmentDirectory
$env:ZEPHYR_SDK_INSTALL_DIR = $sdkDirectory
. (Join-Path $PSScriptRoot 'Enter-Environment.ps1')
& $environmentPython (Join-Path $PSScriptRoot 'git_setup.py')
if ($LASTEXITCODE -ne 0) { throw 'Project Git setup failed.' }
& $environmentPython (Join-Path $PSScriptRoot 'project.py') doctor
if ($LASTEXITCODE -ne 0) { throw 'Environment check failed; see missing host commands above.' }
