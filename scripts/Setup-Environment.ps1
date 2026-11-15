# SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$SdkRoot,
    [string]$Python = 'python'
)

$ErrorActionPreference = 'Stop'
# Compatibility entry: keep dependency and local settings logic in Python.
& $Python (Join-Path $PSScriptRoot 'setup_environment.py') --sdk $SdkRoot
if ($LASTEXITCODE -ne 0) { throw 'Project environment setup failed.' }
