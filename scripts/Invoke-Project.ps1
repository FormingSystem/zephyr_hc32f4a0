# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('doctor', 'check', 'build', 'test', 'debug')]
    [string]$Action,
    [switch]$Pristine
)

$ErrorActionPreference = 'Stop'
if ($Pristine -and $Action -ne 'build') {
    throw '-Pristine is only supported for the build action.'
}

. (Join-Path $PSScriptRoot 'Enter-Environment.ps1')
$projectArguments = @((Join-Path $PSScriptRoot 'project.py'), $Action)
if ($Pristine) { $projectArguments += '--pristine' }
& (Join-Path $env:VIRTUAL_ENV 'Scripts\python.exe') @projectArguments
exit $LASTEXITCODE
