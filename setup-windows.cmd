@echo off
rem SPDX-License-Identifier: Apache-2.0
setlocal
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\windows\setup.ps1" %*
exit /b %errorlevel%
