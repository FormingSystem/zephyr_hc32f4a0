# SPDX-License-Identifier: Apache-2.0
# Windows PowerShell 5.1 compatible. Keep mutations behind explicit functions.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$script:Language = 'en'

function Set-UiLanguage([string]$Language) { $script:Language = $Language }
function Get-Text([string]$Zh, [string]$En) {
    if ($script:Language -eq 'zh') { $Zh } else { $En }
}
function Write-Note([string]$Zh, [string]$En) { Write-Host (Get-Text $Zh $En) }
function Write-Utf8([string]$Path, [string]$Text) {
    [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($Path)) | Out-Null
    [IO.File]::WriteAllText($Path, $Text, (New-Object Text.UTF8Encoding $false))
}
function Save-Json([string]$Path, $Value) { Write-Utf8 $Path ($Value | ConvertTo-Json -Depth 12) }
function Read-Json([string]$Path) { Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json }

function Assert-ToolPath([string]$Path) {
    # Restrict paths interpolated into CMD/Bash installers; reject roots and dot segments.
    if ($Path -notmatch '^[A-Za-z]:\\[A-Za-z0-9_.\\-]+$' -or $Path -match '(^|\\)\.\.?($|\\)') {
        throw (Get-Text "工具路径须为本地绝对路径，只含英文字母、数字、下划线、横线和点，不能是盘符根目录: $Path" "Use a local absolute tool path with ASCII letters, digits, underscores, hyphens and dots; not a drive root: $Path")
    }
    $full = [IO.Path]::GetFullPath($Path).TrimEnd('\')
    foreach ($part in $Path.TrimEnd('\').Substring(3).Split('\')) {
        if ($part.EndsWith('.') -or $part -match '^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?$') { throw "Invalid Windows path component: $part" }
    }
    if (-not (Test-Path -LiteralPath ([IO.Path]::GetPathRoot($full)))) { throw "Drive unavailable: $full" }
    $cursor = $full
    while ($cursor -and $cursor -ne [IO.Path]::GetPathRoot($cursor)) {
        if (Test-Path -LiteralPath $cursor) {
            if ((Get-Item -LiteralPath $cursor -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) {
                throw "Reparse point in tool path: $cursor"
            }
        }
        $cursor = [IO.Path]::GetDirectoryName($cursor)
    }
    return $full
}
function Test-Within([string]$Child, [string]$Parent) {
    $c = [IO.Path]::GetFullPath($Child).TrimEnd('\')
    $p = [IO.Path]::GetFullPath($Parent).TrimEnd('\')
    return $c.Equals($p, [StringComparison]::OrdinalIgnoreCase) -or $c.StartsWith($p + '\', [StringComparison]::OrdinalIgnoreCase)
}
function Assert-SeparatePaths([string[]]$Paths) {
    for ($i = 0; $i -lt $Paths.Count; $i++) {
        for ($j = $i + 1; $j -lt $Paths.Count; $j++) {
            if ((Test-Within $Paths[$i] $Paths[$j]) -or (Test-Within $Paths[$j] $Paths[$i])) {
                throw "Overlapping directories: $($Paths[$i]) / $($Paths[$j])"
            }
        }
    }
}
function Assert-EmptyDirectory([string]$Path) {
    if ((Test-Path -LiteralPath $Path) -and @(Get-ChildItem -LiteralPath $Path -Force).Count) {
        throw (Get-Text "目标目录非空，已保留原文件，请换空目录: $Path" "Destination is not empty; files preserved. Choose an empty directory: $Path")
    }
}
function Assert-Admin([string]$Scope) {
    if ($Scope -eq 'Machine') {
        $principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
        if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
            throw (Get-Text '系统级环境变量需要管理员 PowerShell；也可选 User。' 'Machine environment requires an administrator PowerShell; alternatively select User.')
        }
    }
}
function ConvertTo-WindowsArgument([string]$Value) {
    # CommandLineToArgvW / CRT quoting, including quotes and trailing backslashes.
    '"' + [regex]::Replace([regex]::Replace($Value, '(\\*)"', '$1$1\"'), '(\\+)$', '$1$1') + '"'
}
function Invoke-Tool([string]$File, [string[]]$Arguments = @()) {
    Write-Host ('> ' + $File + ' ' + ($Arguments -join ' '))
    $info = New-Object Diagnostics.ProcessStartInfo
    $info.FileName = $File
    $info.Arguments = (@($Arguments | ForEach-Object { ConvertTo-WindowsArgument $_ }) -join ' ')
    $info.UseShellExecute = $false
    $info.CreateNoWindow = $true
    $info.RedirectStandardOutput = $true
    $info.RedirectStandardError = $true
    $process = [Diagnostics.Process]::Start($info)
    try {
        # Drain stderr concurrently to avoid pipe deadlocks; stdout stays live and
        # is included in PowerShell's transcript even when no console is attached.
        $errors = $process.StandardError.ReadToEndAsync()
        while ($null -ne ($line = $process.StandardOutput.ReadLine())) { Write-Host $line }
        $process.WaitForExit()
        $errorText = $errors.GetAwaiter().GetResult()
        if ($errorText) { Write-Host $errorText }
        if ($process.ExitCode -ne 0) { throw "Command failed ($($process.ExitCode)): $File" }
    } finally { $process.Dispose() }
}
function Get-Release([string]$Repository, [string]$Tag = 'latest') {
    $suffix = if ($Tag -eq 'latest') { 'latest' } else { 'tags/' + $Tag }
    Invoke-RestMethod -UseBasicParsing -Uri "https://api.github.com/repos/$Repository/releases/$suffix" -Headers @{ 'User-Agent' = 'hc32-windows-bootstrap'; Accept = 'application/vnd.github+json' } -TimeoutSec 60
}
function Get-AssetHash($Asset) {
    if (-not $Asset.PSObject.Properties['digest'] -or $Asset.digest -notmatch '^sha256:([a-fA-F0-9]{64})$') {
        throw "Release asset has no authoritative SHA256 digest: $($Asset.name)"
    }
    $Matches[1].ToLowerInvariant()
}
function Get-Download([string[]]$Urls, [string]$Destination, [string]$Sha256 = '') {
    if ($Sha256 -and (Test-Path -LiteralPath $Destination) -and (Get-FileHash -LiteralPath $Destination -Algorithm SHA256).Hash -eq $Sha256) {
        return $Destination
    }
    [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($Destination)) | Out-Null
    $partial = $Destination + '.partial'
    foreach ($url in $Urls) {
        if (-not $url.StartsWith('https://')) { throw "HTTPS required: $url" }
        for ($attempt = 1; $attempt -le 2; $attempt++) {
            try {
                Write-Host "Download [$attempt/2]: $url"
                Invoke-WebRequest -UseBasicParsing -Uri $url -OutFile $partial -TimeoutSec 900
                if ($Sha256 -and (Get-FileHash -LiteralPath $partial -Algorithm SHA256).Hash -ne $Sha256) { throw 'SHA256 mismatch' }
                Move-Item -LiteralPath $partial -Destination $Destination -Force
                return $Destination
            } catch { Write-Warning $_.Exception.Message }
        }
    }
    throw "Download failed; rerun to retry: $Destination"
}
function Select-Mirror([string]$Preference, [string]$Language) {
    if ($Preference -ne 'Auto') { return $Preference }
    # Language/region are hints, not IP geolocation; the official redirector is global.
    if ($Language -eq 'zh' -or (Get-Culture).Name -match '^zh-CN$' -or (Get-WinHomeLocation).GeoId -eq 45) { return 'China' }
    return 'Global'
}
function Get-MirrorBases([string]$Mirror) {
    if ($Mirror -eq 'China') { 'https://mirrors.tuna.tsinghua.edu.cn/msys2'; 'https://mirrors.ustc.edu.cn/msys2' }
    'https://mirror.msys2.org'; 'https://repo.msys2.org'
}
function Set-MsysMirrors([string]$MsysRoot, [string]$Mirror, [string]$BackupDir) {
    foreach ($kind in @('msys', 'mingw')) {
        $path = Join-Path $MsysRoot "etc\pacman.d\mirrorlist.$kind"
        if (-not (Test-Path -LiteralPath $path)) { throw "Missing mirror configuration: $path" }
        [IO.Directory]::CreateDirectory($BackupDir) | Out-Null
        Copy-Item -LiteralPath $path -Destination (Join-Path $BackupDir "mirrorlist.$kind")
        $suffix = if ($kind -eq 'msys') { '/msys/$arch/' } else { '/mingw/$repo/' }
        $lines = @(Get-MirrorBases $Mirror | ForEach-Object { 'Server = ' + $_ + $suffix })
        Write-Utf8 $path (($lines -join "`n") + "`n")
    }
    # Never disable pacman's signature verification or overwrite pacman.conf.
}
function Assert-MsysIdle([string]$MsysRoot) {
    $busy = @(Get-Process | Where-Object {
        try { $_.Path -and (Test-Within $_.Path $MsysRoot) } catch { $false }
    })
    if ($busy.Count) { throw (Get-Text "请先关闭该 MSYS2 的所有终端和工具: $($busy.Name -join ', ')" "Close all terminals and tools from this MSYS2 first: $($busy.Name -join ', ')") }
    if (Test-Path -LiteralPath (Join-Path $MsysRoot 'var\lib\pacman\db.lck')) { throw 'pacman db.lck exists; inspect the interrupted transaction first.' }
}
function Invoke-Msys([string]$MsysRoot, [string]$Command) {
    $oldSystem = $env:MSYSTEM; $oldPath = $env:MSYS2_PATH_TYPE; $oldChere = $env:CHERE_INVOKING
    try {
        $env:MSYSTEM = 'UCRT64'; $env:MSYS2_PATH_TYPE = 'strict'; $env:CHERE_INVOKING = '1'
        Invoke-Tool (Join-Path $MsysRoot 'usr\bin\bash.exe') @('--login', '-c', $Command)
    } finally { $env:MSYSTEM = $oldSystem; $env:MSYS2_PATH_TYPE = $oldPath; $env:CHERE_INVOKING = $oldChere }
}
function Install-Msys([string]$MsysRoot, [string]$Cache, [string]$Mirror, [string]$State, [string]$StageFile) {
    if (-not (Test-Path -LiteralPath (Join-Path $MsysRoot 'usr\bin\bash.exe'))) {
        Assert-EmptyDirectory $MsysRoot
        # /latest can resolve to a nightly tag; select a dated stable release.
        $releases = Invoke-RestMethod -UseBasicParsing -Uri 'https://api.github.com/repos/msys2/msys2-installer/releases?per_page=30' -Headers @{ 'User-Agent' = 'hc32-windows-bootstrap' } -TimeoutSec 60
        $release = @($releases | Where-Object { -not $_.prerelease -and $_.tag_name -match '^\d{4}-\d{2}-\d{2}$' } | Select-Object -First 1)
        if ($release.Count -ne 1) { throw 'No dated stable MSYS2 release found' }
        $release = $release[0]
        $asset = @($release.assets | Where-Object name -Match '^msys2-x86_64-.*\.exe$')
        if ($asset.Count -ne 1) { throw 'Unexpected MSYS2 release layout' }
        $asset = $asset[0]
        $urls = @(Get-MirrorBases $Mirror | ForEach-Object { "$_/distrib/x86_64/$($asset.name)" }) + @($asset.browser_download_url)
        $installer = Get-Download $urls (Join-Path $Cache $asset.name) (Get-AssetHash $asset)
        Save-Json (Join-Path $State 'msys-release.json') $asset
        Invoke-Tool $installer @('in', '--confirm-command', '--accept-messages', '--root', $MsysRoot.Replace('\', '/'))
    }
    Assert-MsysIdle $MsysRoot
    Set-MsysMirrors $MsysRoot $Mirror (Join-Path $State 'mirrors-before')
    # Copy to an ASCII installation path; repository paths never enter shell code.
    $stage = Join-Path $MsysRoot 'tmp\hc32-bootstrap.sh'
    Write-Utf8 $stage ([IO.File]::ReadAllText($StageFile).Replace("`r`n", "`n"))
    # Core upgrades may terminate the shell. A fresh full upgrade MUST then succeed.
    try { Invoke-Msys $MsysRoot 'exec bash /tmp/hc32-bootstrap.sh core' }
    catch { Write-Note '核心更新中断或失败，重新启动 Bash 验证完整更新。' 'Core update interrupted or failed; restarting Bash to require a successful full update.' }
    Invoke-Msys $MsysRoot 'exec bash /tmp/hc32-bootstrap.sh packages'
}

function Install-NativeGit([string]$Root, [string]$Cache, [string]$State) {
    $git = Join-Path $Root 'cmd\git.exe'
    if (-not (Test-Path -LiteralPath $git)) {
        Assert-EmptyDirectory $Root
        $release = Get-Release 'git-for-windows/git'
        $asset = @($release.assets | Where-Object name -Match '^MinGit-[0-9.]+-64-bit.zip$')
        if ($asset.Count -ne 1) { throw 'Unexpected MinGit release layout' }
        $zip = Get-Download @($asset[0].browser_download_url) (Join-Path $Cache $asset[0].name) (Get-AssetHash $asset[0])
        Save-Json (Join-Path $State 'git-release.json') $asset[0]
        Expand-Archive -LiteralPath $zip -DestinationPath $Root
    }
    Invoke-Tool $git @('--version')
    return $git
}
function Get-RegisteredWindowsPython([string]$Version) {
    $minor = ($Version.Split('.')[0..1] -join '.')
    foreach ($name in @("HKCU:\Software\Python\PythonCore\$minor\InstallPath", "HKLM:\Software\Python\PythonCore\$minor\InstallPath")) {
        if (Test-Path $name) {
            $key = Get-Item $name
            $path = $key.GetValue('ExecutablePath')
            if (-not $path -and $key.GetValue('')) { $path = Join-Path $key.GetValue('') 'python.exe' }
            if ($path -and (Test-Path -LiteralPath $path -PathType Leaf)) { return [string]$path }
        }
    }
    return $null
}
function Install-WindowsPython([string]$Root, [string]$ExistingExe, [string]$Version, [string]$Cache) {
    $python = if ($ExistingExe) { $ExistingExe } else { Join-Path $Root 'python.exe' }
    if (-not (Test-Path -LiteralPath $python)) {
        if ($ExistingExe) { throw "Python executable not found: $python" }
        Assert-EmptyDirectory $Root
        $minor = ($Version.Split('.')[0..1] -join '.')
        foreach ($key in @("HKCU:\Software\Python\PythonCore\$minor\InstallPath", "HKLM:\Software\Python\PythonCore\$minor\InstallPath")) {
            if (Test-Path $key) {
                $registered = (Get-Item $key).GetValue('')
                throw (Get-Text "已注册 Python $minor 于 $registered。请用 -PythonExe 指定已有解释器，避免安装器进入维护模式。" "Python $minor is registered at $registered. Select it with -PythonExe to avoid installer maintenance mode.")
            }
        }
        $name = "python-$Version-amd64.exe"
        $installer = Get-Download @("https://www.python.org/ftp/python/$Version/$name") (Join-Path $Cache $name)
        $signature = Get-AuthenticodeSignature -LiteralPath $installer
        if ($signature.Status -ne 'Valid' -or $signature.SignerCertificate.Subject -notmatch 'Python Software Foundation') { throw 'Python installer signature is not valid / not Python Software Foundation' }
        # No launcher, global PATH changes, shortcuts or all-user installation.
        Invoke-Tool $installer @('/quiet', 'InstallAllUsers=0', "TargetDir=$Root", 'PrependPath=0', 'Include_launcher=0', 'Include_test=0', 'Include_doc=0', 'Shortcuts=0', 'Include_pip=1', '/log', (Join-Path $Cache 'python-install.log'))
    }
    Invoke-Tool $python @('-c', 'import sys,sysconfig; assert sys.version_info >= (3,12); assert sys.platform == "win32" and not sysconfig.get_platform().startswith("mingw"); print(sys.executable, sys.version)')
    return $python
}
function Install-ZephyrSdk([string]$Root, [string]$Version, [string]$Cache, [string]$SevenZip, [string]$State) {
    $sdk = Join-Path $Root "zephyr-sdk-$Version"
    $marker = Join-Path $sdk 'sdk_version'
    if ((Test-Path -LiteralPath $sdk) -and -not (Test-Path -LiteralPath $marker)) { Assert-EmptyDirectory $sdk }
    if ((Test-Path -LiteralPath $marker) -and (Get-Content -LiteralPath $marker -Raw).Trim() -ne $Version) { throw 'SDK version conflict' }
    if (-not (Test-Path -LiteralPath (Join-Path $sdk 'gnu\arm-zephyr-eabi\bin\arm-zephyr-eabi-gcc.exe'))) {
        $release = Get-Release 'zephyrproject-rtos/sdk-ng' "v$Version"
        $names = @("zephyr-sdk-${Version}_windows-x86_64_minimal.7z", 'toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z')
        for ($i = 0; $i -lt $names.Count; $i++) {
            $asset = @($release.assets | Where-Object name -EQ $names[$i])
            if ($asset.Count -ne 1) { throw "SDK asset missing: $($names[$i])" }
            $archive = Get-Download @($asset[0].browser_download_url) (Join-Path $Cache $names[$i]) (Get-AssetHash $asset[0])
            Save-Json (Join-Path $State "sdk-asset-$i.json") $asset[0]
            $destination = if ($i -eq 0) { $Root } else { Join-Path $sdk 'gnu' }
            Invoke-Tool $SevenZip @('x', '-y', "-o$destination", $archive)
        }
    }
    if (-not (Test-Path -LiteralPath $marker) -or (Get-Content -LiteralPath $marker -Raw).Trim() -ne $Version) { throw 'SDK validation failed' }
    Invoke-Tool (Join-Path $sdk 'gnu\arm-zephyr-eabi\bin\arm-zephyr-eabi-gcc.exe') @('--version')
    Invoke-Tool (Join-Path $sdk 'hosttools\qemu\qemu-system-arm.exe') @('--version')
    # Explicit SDK selection in project_env.py avoids global CMake registration.
    return $sdk
}

function Get-RawEnvironment([string]$Scope) {
    if ($Scope -eq 'Process') {
        $result = @{}
        foreach ($entry in [Environment]::GetEnvironmentVariables('Process').GetEnumerator()) { $result[$entry.Key] = [string]$entry.Value }
        return $result
    }
    $hive = if ($Scope -eq 'User') { [Microsoft.Win32.Registry]::CurrentUser } else { [Microsoft.Win32.Registry]::LocalMachine }
    $name = if ($Scope -eq 'User') { 'Environment' } else { 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment' }
    $key = $hive.OpenSubKey($name)
    $result = @{}
    try {
        if ($key) { foreach ($n in $key.GetValueNames()) { $result[$n] = [string]$key.GetValue($n, $null, [Microsoft.Win32.RegistryValueOptions]::DoNotExpandEnvironmentNames) } }
    } finally { if ($key) { $key.Dispose() } }
    return $result
}
function Get-EnvironmentKind([string]$Name, [string]$Scope) {
    if ($Scope -eq 'Process') { return 'String' }
    $hive = if ($Scope -eq 'User') { [Microsoft.Win32.Registry]::CurrentUser } else { [Microsoft.Win32.Registry]::LocalMachine }
    $path = if ($Scope -eq 'User') { 'Environment' } else { 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment' }
    $key = $hive.OpenSubKey($path)
    try {
        if ($key -and $Name -in $key.GetValueNames()) { return $key.GetValueKind($Name).ToString() }
        return 'String'
    } finally { if ($key) { $key.Dispose() } }
}
function Set-EnvironmentValue([string]$Name, $Value, [string]$Scope, [string]$Kind = 'String') {
    if ($Scope -eq 'Process') { [Environment]::SetEnvironmentVariable($Name, $Value, 'Process'); return }
    $hive = if ($Scope -eq 'User') { [Microsoft.Win32.Registry]::CurrentUser } else { [Microsoft.Win32.Registry]::LocalMachine }
    $path = if ($Scope -eq 'User') { 'Environment' } else { 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment' }
    $key = $hive.CreateSubKey($path)
    try {
        if ($null -eq $Value -or $Value -eq '') { $key.DeleteValue($Name, $false) }
        else { $key.SetValue($Name, [string]$Value, [Microsoft.Win32.RegistryValueKind]$Kind) }
    } finally { $key.Dispose() }
}
function Join-EnvironmentPath([string]$Original, [string[]]$Added) {
    $result = $Original
    foreach ($p in $Added) {
        $items = @($result -split ';')
        if ($p -and -not @($items | Where-Object { $_.TrimEnd('\') -ieq $p.TrimEnd('\') }).Count) {
            if ($result -and -not $result.EndsWith(';')) { $result += ';' }
            $result += $p
        }
    }
    return $result
}
function Undo-EnvironmentPath([string]$Current, [string]$Before, [string]$After) {
    if ($Current -ceq $After) { return $Before }
    $beforeParts = @($Before -split ';' | Where-Object { $_ })
    $added = @($After -split ';' | Where-Object { $_ -and $_ -notin $beforeParts })
    $kept = @($Current -split ';' | Where-Object { $_ -and $_ -notin $added }) -join ';'
    $removed = @($beforeParts | Where-Object { $_ -notin @($After -split ';') })
    return Join-EnvironmentPath $kept $removed
}
function Send-EnvironmentChanged {
    if (-not ('Hc32.EnvironmentBroadcast' -as [type])) {
        Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
namespace Hc32 { public static class EnvironmentBroadcast {
    [DllImport("user32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
    public static extern IntPtr SendMessageTimeout(IntPtr h, uint m, UIntPtr w, string l, uint f, uint t, out UIntPtr r);
} }
'@
    }
    $result = [UIntPtr]::Zero
    [Hc32.EnvironmentBroadcast]::SendMessageTimeout([IntPtr]0xffff, 0x1a, [UIntPtr]::Zero, 'Environment', 2, 3000, [ref]$result) | Out-Null
}
function Set-ManagedEnvironment([hashtable]$Values, [string[]]$PathEntries, [string]$Scope, [string]$Journal) {
    Assert-Admin $Scope
    $before = Get-RawEnvironment $Scope
    $after = @{}; $old = @{}; $kinds = @{}; $newKinds = @{}
    foreach ($name in $Values.Keys) { $old[$name] = $before[$name]; $after[$name] = $Values[$name] }
    $old['Path'] = $before['Path']; $after['Path'] = Join-EnvironmentPath $before['Path'] $PathEntries
    foreach ($name in $after.Keys) {
        $kinds[$name] = Get-EnvironmentKind $name $Scope
        $newKinds[$name] = if ($name -eq 'Path') { 'ExpandString' } else { $kinds[$name] }
    }
    # Save BEFORE the first mutation; supports rollback after partial failure.
    Save-Json $Journal @{ schema = 1; scope = $Scope; before = $old; after = $after; beforeKinds = $kinds; afterKinds = $newKinds }
    foreach ($name in $after.Keys) { Set-EnvironmentValue $name $after[$name] $Scope $newKinds[$name] }
    if ($Scope -ne 'Process') { Send-EnvironmentChanged }
}
function Restore-ManagedEnvironment([string]$Journal) {
    $data = Read-Json $Journal
    if ($data.schema -ne 1 -or $data.scope -notin @('User', 'Machine', 'Process')) { throw 'Invalid environment journal' }
    Assert-Admin $data.scope
    $current = Get-RawEnvironment $data.scope
    foreach ($property in $data.after.PSObject.Properties) {
        $name = $property.Name
        $previous = $data.before.$name
        if ($name -ieq 'Path') {
            $value = Undo-EnvironmentPath $current[$name] $previous $property.Value
            Set-EnvironmentValue $name $value $data.scope $data.beforeKinds.$name
        } elseif ($current[$name] -ceq $property.Value) {
            Set-EnvironmentValue $name $previous $data.scope $data.beforeKinds.$name
        } elseif ($current[$name] -cne $previous) {
            Write-Warning (Get-Text "$name 后来被修改，已保留当前值。" "$name was modified later; preserving its current value.")
        }
    }
    if ($data.scope -ne 'Process') { Send-EnvironmentChanged }
}

function Backup-Msys([string]$MsysRoot, [string]$Destination, [bool]$Full) {
    $MsysRoot = Assert-ToolPath $MsysRoot
    if (Test-Within $Destination $MsysRoot) { throw 'Backup must be outside MSYS2' }
    Assert-EmptyDirectory $Destination
    if ($Full) { Assert-MsysIdle $MsysRoot }
    elseif (Test-Path -LiteralPath (Join-Path $MsysRoot 'var\lib\pacman\db.lck')) { throw 'pacman is busy; wait before exporting package inventory' }
    [IO.Directory]::CreateDirectory($Destination) | Out-Null
    $envData = @{}
    # Only relevant values: do not export arbitrary credentials from the environment.
    foreach ($scope in @('User', 'Machine')) {
        $envData[$scope] = @{}
        foreach ($entry in (Get-RawEnvironment $scope).GetEnumerator()) {
            if ($entry.Key -match '^(Path|MSYS.*|MINGW.*|ZEPHYR.*|PYTHON.*|WEST.*|VIRTUAL_ENV)$') { $envData[$scope][$entry.Key] = $entry.Value }
        }
    }
    Save-Json (Join-Path $Destination 'environment-reference.json') $envData
    $pacman = Join-Path $MsysRoot 'usr\bin\pacman.exe'
    if (-not (Test-Path -LiteralPath $pacman)) { throw "MSYS2 not found: $MsysRoot" }
    $packages = & $pacman -Q
    if ($LASTEXITCODE -ne 0) { throw 'Cannot export package versions' }
    Write-Utf8 (Join-Path $Destination 'packages-versions.txt') (($packages -join "`n") + "`n")
    $explicit = & $pacman -Qqe
    if ($LASTEXITCODE -ne 0) { throw 'Cannot export explicit packages' }
    Write-Utf8 (Join-Path $Destination 'packages-explicit.txt') (($explicit -join "`n") + "`n")
    Copy-Item -LiteralPath (Join-Path $MsysRoot 'etc\pacman.conf') -Destination $Destination
    Copy-Item -LiteralPath (Join-Path $MsysRoot 'etc\pacman.d') -Destination $Destination -Recurse
    $hash = $null
    if ($Full) {
        # Windows tar runs outside MSYS2: the installation can remain quiescent.
        $tar = Join-Path $env:SystemRoot 'System32\tar.exe'
        if (-not (Test-Path -LiteralPath $tar)) { throw 'Windows tar.exe is required for full snapshots' }
        $archive = Join-Path $Destination 'msys2.tar'
        Invoke-Tool $tar @('-cf', $archive, '-C', $MsysRoot, '.')
        & $tar -tf $archive > $null
        if ($LASTEXITCODE -ne 0) { throw 'Snapshot archive verification failed' }
        $hash = (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash
    }
    Save-Json (Join-Path $Destination 'snapshot.json') @{ schema = 1; msysRoot = $MsysRoot; full = $Full; sha256 = $hash; created = [DateTimeOffset]::Now.ToString('o') }
    Write-Note "备份完成: $Destination" "Backup complete: $Destination"
}
function Restore-Msys([string]$Snapshot) {
    $data = Read-Json (Join-Path $Snapshot 'snapshot.json')
    if ($data.schema -ne 1 -or -not $data.full) { throw 'A complete MSYS2 snapshot is required, not a configuration inventory' }
    $root = Assert-ToolPath $data.msysRoot
    Assert-EmptyDirectory $root
    Assert-MsysIdle $root
    $archive = Join-Path $Snapshot 'msys2.tar'
    if ((Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash -ne $data.sha256) { throw 'Snapshot checksum mismatch' }
    [IO.Directory]::CreateDirectory($root) | Out-Null
    Invoke-Tool (Join-Path $env:SystemRoot 'System32\tar.exe') @('-xf', $archive, '-C', $root)
    if (-not (Test-Path -LiteralPath (Join-Path $root 'usr\bin\bash.exe'))) { throw 'Restored snapshot is incomplete' }
    Write-Note "MSYS2 已恢复到原位置: $root。Windows 快捷方式/卸载登记不属于文件快照。" "MSYS2 restored to its original path: $root. Windows shortcuts/uninstaller registration are outside the file snapshot."
}

function Restore-SnapshotMsysEnvironment([string]$Snapshot, [string]$Scope, [string]$Journal) {
    Assert-Admin $Scope
    $snapshotData = Read-Json (Join-Path $Snapshot 'snapshot.json')
    if ($snapshotData.schema -ne 1) { throw 'Invalid snapshot schema' }
    $reference = Read-Json (Join-Path $Snapshot 'environment-reference.json')
    $baseline = $reference.$Scope
    $current = Get-RawEnvironment $Scope
    $values = @{}
    foreach ($item in $baseline.PSObject.Properties) {
        if ($item.Name -match '^(MSYS|MINGW)') {
            if (-not $current[$item.Name]) { $values[$item.Name] = $item.Value }
            elseif ($current[$item.Name] -cne $item.Value) {
                Write-Warning (Get-Text "$($item.Name) 与快照不同，保留当前值；可先回退教学安装的 journal。" "$($item.Name) differs from the snapshot; kept current value. Roll back the teaching installation journal first if needed.")
            }
        }
    }
    $paths = @()
    if ($baseline.PSObject.Properties['Path']) {
        $paths = @($baseline.Path -split ';' | Where-Object {
            $expanded = [Environment]::ExpandEnvironmentVariables($_).Trim('"')
            $expanded -match '^[A-Za-z]:\\' -and (Test-Within $expanded $snapshotData.msysRoot)
        })
    }
    # Only recover entries belonging to the restored MSYS2, not unrelated tools.
    Set-ManagedEnvironment $values $paths $Scope $Journal
    Write-Note "已补回快照中的 MSYS2 环境变量和 PATH（$Scope），请重开终端。" "Recovered missing MSYS2 environment/PATH entries ($Scope). Open a new terminal."
}

function Assert-UninstallLocation([string]$MsysRoot, [string[]]$ProtectedPaths) {
    $root = Assert-ToolPath $MsysRoot
    foreach ($path in $ProtectedPaths) {
        if ($path -and (Test-Within $path $root)) { throw "Uninstall target contains a protected path: $path" }
    }
    return $root
}
function Assert-NoReparseTree([string]$Root) {
    # Do not recursively enumerate through junctions/symlinks, even on PS 5.1.
    $pending = New-Object 'System.Collections.Generic.Stack[string]'
    $pending.Push($Root)
    while ($pending.Count) {
        foreach ($entry in Get-ChildItem -LiteralPath $pending.Pop() -Force) {
            if ($entry.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "Uninstall refuses a junction/symlink: $($entry.FullName)" }
            if ($entry.PSIsContainer) { $pending.Push($entry.FullName) }
        }
    }
}
function Assert-MsysInstallation([string]$MsysRoot) {
    foreach ($marker in @('usr\bin\bash.exe', 'usr\bin\pacman.exe', 'etc\msystem')) {
        if (-not (Test-Path -LiteralPath (Join-Path $MsysRoot $marker) -PathType Leaf)) { throw "Not a recognized MSYS2 installation: $MsysRoot ($marker missing)" }
    }
}
function Assert-UninstallSnapshot([string]$Snapshot, [string]$MsysRoot) {
    if (Test-Within $Snapshot $MsysRoot) { throw 'Uninstall backup must be outside MSYS2' }
    $data = Read-Json (Join-Path $Snapshot 'snapshot.json')
    if ($data.schema -ne 1 -or -not $data.full -or [IO.Path]::GetFullPath($data.msysRoot).TrimEnd('\') -ine $MsysRoot) { throw 'A full snapshot of this exact MSYS2 path is required' }
    if ((Get-FileHash -LiteralPath (Join-Path $Snapshot 'msys2.tar') -Algorithm SHA256).Hash -ne $data.sha256) { throw 'Uninstall backup checksum mismatch' }
    if (-not (Test-Path -LiteralPath (Join-Path $Snapshot 'environment-reference.json'))) { throw 'Backup environment reference missing' }
}
function Expand-StoredEnvironment([string]$Value, [hashtable]$Context) {
    for ($i = 0; $i -lt 8; $i++) {
        $previous = $Value
        $Value = [regex]::Replace($Value, '%([^%]+)%', {
            param($match)
            $name = $match.Groups[1].Value
            if ($Context.ContainsKey($name)) { return [string]$Context[$name] }
            return $match.Value
        })
        if ($Value -ceq $previous) { break }
    }
    $Value.Trim().Trim('"').Replace('/', '\')
}
function Get-MsysEnvironmentRemoval([hashtable]$Values, [string]$MsysRoot, [hashtable]$Context) {
    $changes = @{}
    if ($Values.ContainsKey('Path')) {
        $kept = foreach ($entry in ($Values['Path'] -split ';')) {
            $expanded = Expand-StoredEnvironment $entry $Context
            if ($expanded -notmatch '^[A-Za-z]:\\' -or -not (Test-Within $expanded $MsysRoot)) { $entry }
        }
        $path = $kept -join ';'
        if ($path -cne $Values['Path']) { $changes['Path'] = $path }
    }
    foreach ($name in $Values.Keys) {
        if ($name -match '^(MSYS|MINGW|ZEPHYR|PYTHON|WEST|VIRTUAL_ENV)') {
            $expanded = Expand-StoredEnvironment $Values[$name] $Context
            if ($expanded -match '^[A-Za-z]:\\' -and $expanded -notmatch ';' -and (Test-Within $expanded $MsysRoot)) { $changes[$name] = $null }
        }
    }
    return $changes
}
function Get-MsysRemovalPlan([string]$MsysRoot, [string[]]$Scopes) {
    $stored = @{ User = (Get-RawEnvironment User); Machine = (Get-RawEnvironment Machine) }
    $context = Get-RawEnvironment Process
    $contexts = @{}
    foreach ($scope in @('Machine', 'User')) {
        foreach ($entry in $stored[$scope].GetEnumerator()) { $context[$entry.Key] = $entry.Value }
        $contexts[$scope] = $context.Clone()
    }
    $plan = @{}
    foreach ($scope in $Scopes) { $plan[$scope] = Get-MsysEnvironmentRemoval $stored[$scope] $MsysRoot $contexts[$scope] }
    return $plan
}
function Set-EnvironmentRemoval([hashtable]$Changes, [string]$Scope, [string]$Journal) {
    Assert-Admin $Scope
    $current = Get-RawEnvironment $Scope
    $before = @{}; $kinds = @{}
    foreach ($name in $Changes.Keys) { $before[$name] = $current[$name]; $kinds[$name] = Get-EnvironmentKind $name $Scope }
    Save-Json $Journal @{ schema = 1; scope = $Scope; before = $before; after = $Changes; beforeKinds = $kinds; afterKinds = $kinds }
    foreach ($name in $Changes.Keys) { Set-EnvironmentValue $name $Changes[$name] $Scope $kinds[$name] }
    if ($Scope -ne 'Process') { Send-EnvironmentChanged }
}
function Remove-MsysInstallation([string]$MsysRoot, [string]$Snapshot, [string[]]$ProtectedPaths) {
    $root = Assert-UninstallLocation $MsysRoot (@($ProtectedPaths) + @($Snapshot))
    Assert-MsysInstallation $root
    Assert-MsysIdle $root
    Assert-NoReparseTree $root
    Assert-UninstallSnapshot $Snapshot $root
    $uninstaller = Join-Path $root 'uninstall.exe'
    if (Test-Path -LiteralPath $uninstaller -PathType Leaf) {
        Invoke-Tool $uninstaller @('pr', '--confirm-command')
    }
    # The official uninstaller may leave home/packages behind. Only remove this
    # previously validated installation, after a complete verified snapshot.
    if (Test-Path -LiteralPath $root) {
        $checked = Assert-UninstallLocation $root (@($ProtectedPaths) + @($Snapshot))
        Assert-MsysIdle $checked
        Assert-NoReparseTree $checked
        Remove-Item -LiteralPath $checked -Recurse -Force -ErrorAction Stop
    }
    if (Test-Path -LiteralPath $root) { throw "MSYS2 removal incomplete: $root" }
}

Export-ModuleMember -Function *
