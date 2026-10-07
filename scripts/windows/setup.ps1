# SPDX-License-Identifier: Apache-2.0
#requires -Version 5.1
[CmdletBinding()]
param(
    [ValidateSet('Install', 'Plan', 'Backup', 'Restore', 'RestoreEnvironment', 'Uninstall')][string]$Action = 'Install',
    [ValidateSet('zh', 'en')][string]$Language,
    [string]$MsysRoot,
    [string]$ToolsRoot,
    [string]$DownloadRoot,
    [string]$SdkRoot,
    [string]$PythonExe,
    [ValidateSet('Auto', 'China', 'Global')][string]$Mirror = 'Auto',
    [ValidateSet('User', 'Machine', 'Process')][string]$EnvironmentScope,
    [string]$Snapshot,
    [string]$Journal,
    [switch]$ConfigurationOnly,
    [switch]$WhatIf,
    [switch]$Yes,
    [switch]$NonInteractive
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
Import-Module (Join-Path $PSScriptRoot 'Environment.psm1') -Force -DisableNameChecking
$repo = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..'))
$local = Join-Path $repo '.local\windows'
$oldProcess = Get-RawEnvironment 'Process'
$transcript = $false
try {
    if (-not $Language) {
        if ($NonInteractive) { $Language = 'zh' }
        else {
            $answer = Read-Host '请选择语言 / Select language: 1 中文 [default], 2 English'
            $Language = if ($answer -in @('2', 'en')) { 'en' } else { 'zh' }
        }
    }
    Set-UiLanguage $Language
    if (($WhatIf -or $Yes) -and $Action -ne 'Uninstall') { throw '-WhatIf and -Yes apply only to -Action Uninstall; use -Action Plan to preview installation.' }
    if ($env:OS -ne 'Windows_NT' -or -not [Environment]::Is64BitOperatingSystem -or -not [Environment]::Is64BitProcess -or $env:PROCESSOR_ARCHITECTURE -ne 'AMD64') {
        throw (Get-Text '仅支持 Windows 10/11 x64，请使用 64 位 PowerShell。' 'Windows 10/11 x64 and 64-bit PowerShell are required.')
    }
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
    $ProgressPreference = 'SilentlyContinue'
    if ($Action -eq 'RestoreEnvironment') {
        if ($Snapshot) {
            if (-not $EnvironmentScope) { $EnvironmentScope = 'User' }
            if ($EnvironmentScope -eq 'Process') { throw 'Select User or Machine to restore snapshot environment entries' }
            $restoreJournal = Join-Path $local ('runs\restore-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff') + '\environment-journal.json')
            Restore-SnapshotMsysEnvironment ([IO.Path]::GetFullPath($Snapshot)) $EnvironmentScope $restoreJournal
        } else {
            if (-not $Journal) { throw (Get-Text '请用 -Journal 指定安装记录，或用 -Snapshot 指定备份目录。' 'Pass an installation -Journal or a backup -Snapshot.') }
            Restore-ManagedEnvironment ([IO.Path]::GetFullPath($Journal))
        }
        Write-Note '环境变量恢复完成，请重新打开终端。' 'Environment restored. Open a new terminal.'
        exit 0
    }
    if ($Action -eq 'Restore') {
        if (-not $Snapshot) { throw (Get-Text '请用 -Snapshot 指定完整备份目录。' 'Pass the full backup directory with -Snapshot.') }
        if (-not $EnvironmentScope) { $EnvironmentScope = 'User' }
        Assert-Admin $EnvironmentScope
        if ($Journal) {
            $journalData = Read-Json ([IO.Path]::GetFullPath($Journal))
            Assert-Admin $journalData.scope
        }
        Restore-Msys ([IO.Path]::GetFullPath($Snapshot))
        if ($Journal) { Restore-ManagedEnvironment ([IO.Path]::GetFullPath($Journal)) }
        if ($EnvironmentScope -ne 'Process') {
            $restoreJournal = Join-Path $local ('runs\restore-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff') + '\environment-journal.json')
            Restore-SnapshotMsysEnvironment ([IO.Path]::GetFullPath($Snapshot)) $EnvironmentScope $restoreJournal
        }
        exit 0
    }
    if (-not $MsysRoot) {
        $MsysRoot = 'E:\Msys2'
        if (-not $NonInteractive) {
            Write-Note '作者的 MSYS2 配置为 E:\Msys2；目录由你选择。' 'The author uses E:\Msys2; choose your own location.'
            $value = Read-Host (Get-Text "MSYS2 安装目录 [$MsysRoot]" "MSYS2 installation directory [$MsysRoot]")
            if ($value) { $MsysRoot = $value }
        }
    }
    $MsysRoot = Assert-ToolPath $MsysRoot
    if ($Action -eq 'Uninstall') {
        if ($ConfigurationOnly -or $Journal -or $EnvironmentScope -eq 'Process') { throw 'Uninstall requires a full snapshot and User/Machine environment cleanup; -Journal and -ConfigurationOnly do not apply.' }
        if (-not $Snapshot) { $Snapshot = Join-Path $local ('backups\before-uninstall-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff')) }
        $Snapshot = [IO.Path]::GetFullPath($Snapshot)
        $state = Join-Path $local ('runs\uninstall-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff'))
        $MsysRoot = Assert-UninstallLocation $MsysRoot @($repo, $Snapshot, $state, $env:SystemRoot, $env:USERPROFILE)
        Assert-MsysInstallation $MsysRoot
        $scopes = if ($EnvironmentScope) { @($EnvironmentScope) } else { @('User', 'Machine') }
        $removal = Get-MsysRemovalPlan $MsysRoot $scopes
        Write-Note "将卸载 MSYS2（包括 UCRT64、home 和缓存）: $MsysRoot" "Remove MSYS2 (including UCRT64, home and cache): $MsysRoot"
        Write-Note "完整备份: $Snapshot" "Full backup: $Snapshot"
        Write-Note '保留工程、外部 Python/Git/SDK、下载缓存与备份。' 'Keep the project, external Python/Git/SDK, download cache and backups.'
        foreach ($scope in $scopes) { Write-Host ("{0}: {1}" -f $scope, ($removal[$scope].Keys -join ', ')) }
        if ($WhatIf) {
            Write-Note '仅预览；未备份、未卸载、未修改环境变量。' 'Preview only; no backup, removal or environment changes.'
            exit 0
        }
        if (-not $Yes) {
            if ($NonInteractive) { throw (Get-Text '无人值守卸载必须同时指定 -Yes；可先用 -WhatIf 查看。' 'Unattended uninstall requires -Yes; preview with -WhatIf first.') }
            $answer = Read-Host (Get-Text '输入 UNINSTALL 确认备份后卸载，其他输入取消' 'Type UNINSTALL to back up and uninstall; anything else cancels')
            if ($answer -cne 'UNINSTALL') { exit 0 }
        }
        foreach ($scope in $scopes) { if ($removal[$scope].Count) { Assert-Admin $scope } }
        Assert-MsysIdle $MsysRoot
        Assert-NoReparseTree $MsysRoot
        [IO.Directory]::CreateDirectory($state) | Out-Null
        Start-Transcript -LiteralPath (Join-Path $state 'uninstall.log') | Out-Null
        $transcript = $true
        $receipt = @{ schema = 1; action = 'Uninstall'; msysRoot = $MsysRoot; snapshot = $Snapshot; status = 'preparing' }
        Save-Json (Join-Path $state 'uninstall.json') $receipt
        if (Test-Path -LiteralPath (Join-Path $Snapshot 'snapshot.json')) {
            Write-Note '使用已有完整快照；卸载后只能恢复到该快照的时间点。' 'Using the existing full snapshot; recovery returns to its recorded point in time.'
            Assert-UninstallSnapshot $Snapshot $MsysRoot
        } else { Backup-Msys $MsysRoot $Snapshot $true }
        $receipt.status = 'removing'
        Save-Json (Join-Path $state 'uninstall.json') $receipt
        Remove-MsysInstallation $MsysRoot $Snapshot @($repo, $state, $env:SystemRoot, $env:USERPROFILE)
        $receipt.status = 'cleaning-environment'
        Save-Json (Join-Path $state 'uninstall.json') $receipt
        # Re-read after the official uninstaller, preserving its independent edits.
        $removal = Get-MsysRemovalPlan $MsysRoot $scopes
        foreach ($scope in $scopes) {
            if ($removal[$scope].Count) { Set-EnvironmentRemoval $removal[$scope] $scope (Join-Path $state "environment-$scope.json") }
        }
        $receipt.status = 'complete'
        Save-Json (Join-Path $state 'uninstall.json') $receipt
        Write-Note "卸载完成，备份保存在 $Snapshot；请重新打开终端。" "Uninstall complete; backup saved at $Snapshot. Open a new terminal."
        exit 0
    }
    if ($Action -eq 'Backup') {
        if (-not $Snapshot) { $Snapshot = Join-Path $local ('backups\' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff')) }
        Backup-Msys $MsysRoot ([IO.Path]::GetFullPath($Snapshot)) (-not $ConfigurationOnly)
        exit 0
    }
    $lockFile = Join-Path $repo 'dependencies.lock.json'
    if (-not (Test-Path -LiteralPath $lockFile) -or -not (Test-Path -LiteralPath (Join-Path $repo 'scripts\setup_environment.py'))) { throw "Incomplete project: $repo" }
    $lock = Read-Json $lockFile
    if (-not $ToolsRoot) {
        $ToolsRoot = ([IO.Path]::GetPathRoot($MsysRoot) + 'zephyr-tools')
        if (-not $NonInteractive) {
            $value = Read-Host (Get-Text "其他工具目录（Python/Git/SDK/下载缓存）[$ToolsRoot]" "Other tools directory (Python/Git/SDK/downloads) [$ToolsRoot]")
            if ($value) { $ToolsRoot = $value }
        }
    }
    $ToolsRoot = Assert-ToolPath $ToolsRoot
    if (-not $DownloadRoot) { $DownloadRoot = Join-Path $ToolsRoot 'downloads' }
    if (-not $SdkRoot) { $SdkRoot = Join-Path $ToolsRoot 'sdk' }
    $DownloadRoot = Assert-ToolPath $DownloadRoot
    $SdkRoot = Assert-ToolPath $SdkRoot
    $pythonRoot = Join-Path $ToolsRoot 'python312'
    $gitRoot = Join-Path $ToolsRoot 'git'
    $bin = Join-Path $ToolsRoot 'bin'
    Assert-SeparatePaths @($MsysRoot, $DownloadRoot, $SdkRoot, $pythonRoot, $gitRoot, $bin)
    foreach ($path in @($MsysRoot, $ToolsRoot, $DownloadRoot, $SdkRoot)) {
        if ((Test-Within $repo $path) -or (Test-Within $path $repo)) { throw "Keep tool installations outside the source checkout: $path" }
    }
    # Paths written into generated CMD launchers must not contain CMD metacharacters.
    if ($repo -match '[%!]') { throw 'Repository path cannot contain % or ! for CMD launchers' }
    if (-not $PythonExe) {
        $PythonExe = Get-RegisteredWindowsPython $lock.python.verified
        if (-not $NonInteractive) {
            $hint = if ($PythonExe) { $PythonExe } else { Get-Text '新装' 'new installation' }
            $value = Read-Host (Get-Text "官方 Windows Python 路径，留空采用 [$hint]" "Official Windows Python path; Enter to use [$hint]")
            if ($value) { $PythonExe = $value }
        }
    }
    if ($PythonExe) {
        $PythonExe = [IO.Path]::GetFullPath($PythonExe)
        if (-not (Test-Path -LiteralPath $PythonExe -PathType Leaf)) { throw "Python not found: $PythonExe" }
    }
    if (-not $EnvironmentScope) {
        $EnvironmentScope = 'User'
        if (-not $NonInteractive) {
            $value = Read-Host (Get-Text '环境变量: 1 当前用户 [默认], 2 系统级（需管理员）, 3 仅启动器' 'Environment: 1 User [default], 2 Machine (administrator), 3 Launcher only')
            if ($value -eq '2') { $EnvironmentScope = 'Machine' }
            elseif ($value -eq '3') { $EnvironmentScope = 'Process' }
        }
    }
    if (-not $NonInteractive -and $Mirror -eq 'Auto') {
        $value = Read-Host (Get-Text '下载源: 1 自动 [中文优先清华/中科大], 2 中国, 3 全球自动就近' 'Mirrors: 1 Auto [default], 2 China (TUNA/USTC), 3 Global geo-redirector')
        if ($value -eq '2') { $Mirror = 'China' }
        elseif ($value -eq '3') { $Mirror = 'Global' }
    }
    $Mirror = Select-Mirror $Mirror $Language
    $plan = [ordered]@{ Repository = $repo; MsysRoot = $MsysRoot; ToolsRoot = $ToolsRoot; Downloads = $DownloadRoot; Sdk = (Join-Path $SdkRoot "zephyr-sdk-$($lock.sdk.version)"); Python = $(if ($PythonExe) { $PythonExe } else { Join-Path $pythonRoot 'python.exe' }); Mirror = $Mirror; EnvironmentScope = $EnvironmentScope }
    $plan | Format-List | Out-Host
    Write-Note '预留至少 10 GiB；首次安装需要联网。MSYS2、pip 是滚动依赖，快照才可恢复原版本。' 'Reserve at least 10 GiB; initial setup needs internet. MSYS2/pip dependencies roll forward; snapshots preserve original versions.'
    if ($Action -eq 'Plan') { exit 0 }
    Assert-Admin $EnvironmentScope
    if (Test-Path -LiteralPath (Join-Path $MsysRoot 'usr\bin\bash.exe')) { Assert-MsysIdle $MsysRoot }
    if (-not $NonInteractive) {
        $answer = Read-Host (Get-Text '按 Enter 开始安装，输入 q 退出' 'Press Enter to install, or q to quit')
        if ($answer -eq 'q') { exit 0 }
    }
    $state = Join-Path $local ('runs\' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff'))
    [IO.Directory]::CreateDirectory($state) | Out-Null
    [IO.Directory]::CreateDirectory($DownloadRoot) | Out-Null
    $env:TEMP = Join-Path $DownloadRoot 'tmp'; $env:TMP = $env:TEMP
    [IO.Directory]::CreateDirectory($env:TEMP) | Out-Null
    $env:PIP_CACHE_DIR = Join-Path $DownloadRoot 'pip'
    $env:PYTHONUTF8 = '1'
    $env:PYTHONHOME = $null; $env:PYTHONPATH = $null
    # Session-only index selection: leave the user's pip.ini untouched.
    $env:PIP_INDEX_URL = if ($Mirror -eq 'China') { 'https://pypi.tuna.tsinghua.edu.cn/simple' } else { 'https://pypi.org/simple' }
    $env:PIP_EXTRA_INDEX_URL = $null
    Save-Json (Join-Path $state 'plan.json') $plan
    Start-Transcript -LiteralPath (Join-Path $state 'install.log') | Out-Null
    $transcript = $true
    if (Test-Path -LiteralPath (Join-Path $MsysRoot 'usr\bin\pacman.exe')) {
        Backup-Msys $MsysRoot (Join-Path $state 'configuration-before') $false
    }
    Install-Msys $MsysRoot $DownloadRoot $Mirror $state (Join-Path $PSScriptRoot 'msys-stage.sh')
    $git = Install-NativeGit $gitRoot $DownloadRoot $state
    $python = Install-WindowsPython $pythonRoot $PythonExe $lock.python.verified $DownloadRoot
    $env:Path = @((Split-Path $git), (Split-Path $python), (Join-Path $MsysRoot 'ucrt64\bin'), (Join-Path $MsysRoot 'usr\bin'), $oldProcess['Path']) -join ';'
    $actualRoot = & $git -C $repo rev-parse --show-toplevel
    if ($LASTEXITCODE -ne 0 -or [IO.Path]::GetFullPath($actualRoot) -ine $repo) { throw 'Git root differs from the script repository' }
    & $git -C $repo remote -v | Out-Host
    $sevenZip = Join-Path $MsysRoot 'ucrt64\bin\7z.exe'
    if (-not (Test-Path -LiteralPath $sevenZip)) { throw "7-Zip executable missing: $sevenZip" }
    $sdk = Install-ZephyrSdk $SdkRoot $lock.sdk.version $DownloadRoot $sevenZip $state
    $venv = Join-Path $repo '.venv\Scripts\python.exe'
    if (Test-Path -LiteralPath $venv) {
        Invoke-Tool $venv @('-c', 'import sys; assert sys.version_info >= (3,12); print(sys.executable)')
    }
    Invoke-Tool $python @((Join-Path $repo 'scripts\setup_environment.py'), '--sdk', $sdk)
    $environmentFile = Join-Path $repo '.local\environment.json'
    $projectEnvironment = Read-Json $environmentFile
    $hostPaths = @((Split-Path $git), (Join-Path $MsysRoot 'ucrt64\bin'), (Join-Path $MsysRoot 'usr\bin'))
    $projectEnvironment | Add-Member -NotePropertyName host_paths -NotePropertyValue $hostPaths -Force
    Save-Json $environmentFile $projectEnvironment
    Invoke-Tool $venv @((Join-Path $repo 'scripts\configure_west.py'))
    Invoke-Tool $venv @((Join-Path $repo 'scripts\project_env.py'), 'doctor')
    $config = @{ schema = 1; repository = $repo; msysRoot = $MsysRoot; toolsRoot = $ToolsRoot; git = $git; python = $python; sdk = $sdk; mirror = $Mirror; language = $Language; downloads = $DownloadRoot; lastRun = $state }
    Save-Json (Join-Path $local 'installation.json') $config
    $launcher = '@echo off' + "`r`n" + 'powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "' + (Join-Path $PSScriptRoot 'start.ps1') + '" %*' + "`r`n"
    # UTF-8 CMD files switch to UTF-8 before reading a non-ASCII repository path.
    Write-Utf8 (Join-Path $bin 'hc32-shell.cmd') ($launcher.Replace('@echo off', "@echo off`r`nchcp 65001 >nul"))
    $values = @{ MSYS2_ROOT = $MsysRoot; HC32_ENV_HOME = $ToolsRoot; ZEPHYR_SDK_INSTALL_DIR = $sdk; ZEPHYR_TOOLCHAIN_VARIANT = 'zephyr' }
    $pathEntries = @($bin, (Split-Path $git), (Split-Path $python), (Join-Path (Split-Path $python) 'Scripts'), (Join-Path $MsysRoot 'ucrt64\bin'))
    Set-ManagedEnvironment $values $pathEntries $EnvironmentScope (Join-Path $state 'environment-journal.json')
    Write-Note '安装成功。新终端运行 hc32-shell，或执行 scripts\windows\start.ps1。' 'Installation complete. Run hc32-shell in a new terminal, or scripts\windows\start.ps1.'
    Write-Note "环境变量恢复记录: $state\environment-journal.json" "Environment rollback journal: $state\environment-journal.json"
    Write-Note '已完成 doctor；固件构建、QEMU 测试和实板操作需要另行执行。' 'doctor passed; firmware builds, QEMU tests and hardware operations are separate steps.'
} catch {
    Write-Host (Get-Text "失败: $($_.Exception.Message)" "Failed: $($_.Exception.Message)") -ForegroundColor Red
    Write-Host (Get-Text '保留下载和日志，排除问题后可重试；不会将失败阶段标为成功。' 'Downloads and logs are preserved. Fix the error and rerun; failed stages are not marked successful.')
    exit 1
} finally {
    if ($transcript) { Stop-Transcript | Out-Null }
    foreach ($name in @('TEMP', 'TMP', 'PIP_CACHE_DIR', 'PIP_INDEX_URL', 'PIP_EXTRA_INDEX_URL', 'PYTHONHOME', 'PYTHONPATH', 'PYTHONUTF8', 'Path', 'MSYS2_ROOT', 'HC32_ENV_HOME', 'ZEPHYR_SDK_INSTALL_DIR', 'ZEPHYR_TOOLCHAIN_VARIANT')) {
        [Environment]::SetEnvironmentVariable($name, $oldProcess[$name], 'Process')
    }
}
