# SPDX-License-Identifier: Apache-2.0
# Offline tests: no installation, registry mutation or existing MSYS2 changes.
#requires -Version 5.1
param([string]$PythonExe)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
Import-Module (Join-Path $PSScriptRoot 'Environment.psm1') -Force -DisableNameChecking
Set-UiLanguage en
$repo = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..'))
$root = Join-Path $repo ('build\windows-bootstrap-tests\' + [Guid]::NewGuid().ToString('N'))
[IO.Directory]::CreateDirectory($root) | Out-Null
if (-not $PythonExe) { $PythonExe = Join-Path $repo '.venv\Scripts\python.exe' }
$script:passed = 0
function Assert($Condition, [string]$Message) {
    if (-not $Condition) { throw "FAIL: $Message" }
    $script:passed++
}
function Assert-Throws([scriptblock]$Block, [string]$Message) {
    $thrown = $false
    try { & $Block | Out-Null } catch { $thrown = $true }
    Assert $thrown $Message
}
$drive = [IO.Path]::GetPathRoot($repo)
Assert ((Assert-ToolPath ($drive + 'tools')) -eq ($drive + 'tools')) 'absolute path accepted'
foreach ($bad in @($drive, 'relative', ($drive + 'a\..\b'), ($drive + 'tool space'), ($drive + 'a&b'), '\\server\share', ($drive + 'NUL'), ($drive + 'tools.'))) {
    Assert-Throws { Assert-ToolPath $bad } "unsafe path rejected: $bad"
}
Assert-Throws { Assert-SeparatePaths @(($drive + 'tools'), ($drive + 'tools\cache')) } 'overlap rejected'
Assert (-not (Test-Within ($drive + 'tools-other') ($drive + 'tools'))) 'prefix is not containment'
Assert ((Select-Mirror Auto zh) -eq 'China') 'Chinese default'
Assert ((Select-Mirror Global zh) -eq 'Global') 'explicit global override'
Assert ((Join-EnvironmentPath 'X:\old;%TEMP%\bin' @('x:\OLD', 'Y:\new')) -ceq 'X:\old;%TEMP%\bin;Y:\new') 'PATH keeps raw references and avoids duplicates'
Assert ((Join-EnvironmentPath 'X:\old;X:\old;' @('Y:\new')) -ceq 'X:\old;X:\old;Y:\new') 'existing PATH entries are not rewritten'
Assert ((Undo-EnvironmentPath 'X:\old;Y:\new;Z:\later' 'X:\old' 'X:\old;Y:\new') -eq 'X:\old;Z:\later') 'rollback retains later PATH additions'
Assert ((Undo-EnvironmentPath 'X:\old;Y:\new' 'X:\old' 'X:\old;Y:\new') -eq 'X:\old') 'exact rollback'
Assert ((Undo-EnvironmentPath 'Z:\later' 'X:\old' 'X:\old;Y:\new') -eq 'Z:\later') 'rollback does not undo later removals'

$mirrorRoot = Join-Path $root 'mirrors'
foreach ($kind in @('msys', 'mingw')) { Write-Utf8 (Join-Path $mirrorRoot "etc\pacman.d\mirrorlist.$kind") 'old-mirror' }
Write-Utf8 (Join-Path $mirrorRoot 'etc\pacman.conf') 'SigLevel = Required'
Set-MsysMirrors $mirrorRoot China (Join-Path $root 'mirror-backup')
$mirror = [IO.File]::ReadAllText((Join-Path $mirrorRoot 'etc\pacman.d\mirrorlist.mingw'))
Assert ($mirror.Contains('https://mirrors.tuna.tsinghua.edu.cn/msys2/mingw/$repo/')) 'literal pacman repo variable'
Assert ($mirror.IndexOf('tuna') -lt $mirror.IndexOf('ustc')) 'author mirror order'
Assert ($mirror.Contains('mirror.msys2.org')) 'global fallback'
Assert ((Get-Content (Join-Path $root 'mirror-backup\mirrorlist.mingw')) -eq 'old-mirror') 'mirror backup'
Assert ((Get-Content (Join-Path $mirrorRoot 'etc\pacman.conf')) -eq 'SigLevel = Required') 'signature checks preserved'

$before = Get-RawEnvironment Process
try {
    $env:HC32_BOOTSTRAP_TEST = 'before'
    $journal = Join-Path $root 'environment.json'
    Set-ManagedEnvironment @{ HC32_BOOTSTRAP_TEST = 'after' } @('X:\hc32-test-tool') Process $journal
    $env:Path += ';Z:\added-after-install'
    Restore-ManagedEnvironment $journal
    Assert ($env:HC32_BOOTSTRAP_TEST -eq 'before') 'variable restored'
    Assert ($env:Path -notlike '*X:\hc32-test-tool*' -and $env:Path -like '*Z:\added-after-install*') 'journal preserves later PATH edits'
    Set-ManagedEnvironment @{ HC32_BOOTSTRAP_TEST = 'after' } @() Process $journal
    $env:HC32_BOOTSTRAP_TEST = 'later'
    Restore-ManagedEnvironment $journal
    Assert ($env:HC32_BOOTSTRAP_TEST -eq 'later') 'conflicting later variable preserved'
} finally {
    $env:Path = $before['Path']; $env:HC32_BOOTSTRAP_TEST = $before['HC32_BOOTSTRAP_TEST']
}

# Real child process exercises PS 5.1 quoting, spaces, quotes and trailing slashes.
$output = Join-Path $root 'arguments.json'
$code = 'import json,sys; from pathlib import Path; Path(sys.argv[1]).write_text(json.dumps(sys.argv[2:]))'
$arguments = @('', 'with space', 'a"quote', 'C:\ends-in-slash\', '$HOME;not-code')
Invoke-Tool $PythonExe (@('-c', $code, $output) + $arguments)
$actual = Read-Json $output
Assert (($actual | ConvertTo-Json -Compress) -eq ($arguments | ConvertTo-Json -Compress)) 'native argument round trip'
Assert-Throws { Invoke-Tool $PythonExe @('-c', 'raise SystemExit(17)') } 'native failure propagates'

# Restore a tiny real tar snapshot, then prove nonempty targets and corruption fail.
$fakeMsys = Join-Path $root 'original-msys'
Write-Utf8 (Join-Path $fakeMsys 'usr\bin\bash.exe') 'fixture-not-an-executable'
Write-Utf8 (Join-Path $fakeMsys 'home\reader\file.txt') 'original content'
$snapshot = Join-Path $root 'snapshot'
[IO.Directory]::CreateDirectory($snapshot) | Out-Null
$archive = Join-Path $snapshot 'msys2.tar'
Invoke-Tool (Join-Path $env:SystemRoot 'System32\tar.exe') @('-cf', $archive, '-C', $fakeMsys, '.')
$destination = Join-Path $root 'restored-msys'
Save-Json (Join-Path $snapshot 'snapshot.json') @{ schema = 1; full = $true; msysRoot = $destination; sha256 = (Get-FileHash $archive -Algorithm SHA256).Hash }
Restore-Msys $snapshot
Assert ((Get-Content (Join-Path $destination 'home\reader\file.txt')) -eq 'original content') 'full snapshot content restored'
Save-Json (Join-Path $snapshot 'environment-reference.json') @{ Process = @{ Path = "$destination\ucrt64\bin;Z:\unrelated"; MSYS2_TEST_RECOVERY = 'original'; PYTHONHOME = 'do-not-restore' } }
$originalPath = $env:Path; $originalMsysTest = $env:MSYS2_TEST_RECOVERY; $originalPythonHome = $env:PYTHONHOME
try {
    $env:MSYS2_TEST_RECOVERY = $null
    Restore-SnapshotMsysEnvironment $snapshot Process (Join-Path $root 'recovery-journal.json')
    Assert ($env:Path -like "*$destination\ucrt64\bin*" -and $env:Path -notlike '*Z:\unrelated*') 'snapshot only restores MSYS2 PATH entries'
    Assert ($env:MSYS2_TEST_RECOVERY -eq 'original') 'missing MSYS variable recovered'
    Assert ($env:PYTHONHOME -ceq $originalPythonHome) 'snapshot does not rewrite Python configuration'
} finally { $env:Path = $originalPath; $env:MSYS2_TEST_RECOVERY = $originalMsysTest; $env:PYTHONHOME = $originalPythonHome }
Assert-Throws { Restore-Msys $snapshot } 'nonempty restore target rejected'
$metadata = Read-Json (Join-Path $snapshot 'snapshot.json')
$metadata.msysRoot = Join-Path $root 'corrupt-destination'; $metadata.sha256 = '0' * 64
Save-Json (Join-Path $snapshot 'snapshot.json') $metadata
Assert-Throws { Restore-Msys $snapshot } 'corrupted snapshot rejected'
Assert (-not (Test-Path $metadata.msysRoot)) 'corruption rejected before target creation'
# Uninstall tests use only disposable marker files under this test run.
$removeRoot = Join-Path $root 'uninstall-msys'
$removeBackup = Join-Path $root 'uninstall-backup'
foreach ($marker in @('usr\bin\bash.exe', 'usr\bin\pacman.exe', 'etc\msystem', 'home\reader\note.txt')) {
    Write-Utf8 (Join-Path $removeRoot $marker) 'test fixture'
}
Assert-Throws { Assert-UninstallLocation $removeRoot @((Join-Path $removeRoot 'backup')) } 'backup inside uninstall root rejected'
Assert-Throws { Assert-UninstallLocation $repo @($repo) } 'repository root protected'
Assert-Throws { Assert-MsysInstallation $root } 'unrecognized installation rejected'
Assert-Throws { Assert-UninstallSnapshot $snapshot $removeRoot } 'snapshot for another installation rejected'
$context = @{ MSYS2_ROOT = $removeRoot; OTHER = 'Z:\unrelated' }
$values = @{ Path = "%MSYS2_ROOT%\ucrt64\bin;$removeRoot-other\bin;%OTHER%\bin;"; MSYS2_ROOT = $removeRoot; PYTHONHOME = 'Z:\Python'; MSYSTEM = 'UCRT64' }
$changes = Get-MsysEnvironmentRemoval $values $removeRoot $context
Assert ($changes['Path'] -ceq "$removeRoot-other\bin;%OTHER%\bin;") 'remove only MSYS PATH and retain raw unrelated entries'
Assert ($changes.ContainsKey('MSYS2_ROOT') -and $null -eq $changes['MSYS2_ROOT']) 'remove variable pointing into MSYS'
Assert (-not $changes.ContainsKey('PYTHONHOME') -and -not $changes.ContainsKey('MSYSTEM')) 'unrelated and ambiguous variables retained'
Assert ((Undo-EnvironmentPath 'X:\keep;Z:\later' 'X:\keep;Y:\removed' 'X:\keep') -eq 'X:\keep;Z:\later;Y:\removed') 'rollback restores removed PATH while retaining new entries'
$originalPath = $env:Path; $originalMsysTest = $env:MSYS2_TEST_RECOVERY
try {
    $env:Path = 'X:\keep;Y:\removed'; $env:MSYS2_TEST_RECOVERY = 'Y:\removed'
    $journal = Join-Path $root 'uninstall-environment.json'
    Set-EnvironmentRemoval @{ Path = 'X:\keep'; MSYS2_TEST_RECOVERY = $null } Process $journal
    Assert ($env:Path -eq 'X:\keep' -and -not $env:MSYS2_TEST_RECOVERY) 'uninstall environment changes applied'
    $env:Path += ';Z:\later'
    Restore-ManagedEnvironment $journal
    Assert ($env:Path -eq 'X:\keep;Z:\later;Y:\removed' -and $env:MSYS2_TEST_RECOVERY -eq 'Y:\removed') 'uninstall environment journal restores removed values'
} finally { $env:Path = $originalPath; $env:MSYS2_TEST_RECOVERY = $originalMsysTest }
$junctionRoot = Join-Path $root 'junction-test'
$outside = Join-Path $root 'junction-outside'
Write-Utf8 (Join-Path $outside 'keep.txt') 'keep me'
[IO.Directory]::CreateDirectory($junctionRoot) | Out-Null
New-Item -ItemType Junction -Path (Join-Path $junctionRoot 'link') -Target $outside | Out-Null
Assert-Throws { Assert-NoReparseTree $junctionRoot } 'junction traversal rejected'
Assert (Test-Path (Join-Path $outside 'keep.txt')) 'junction target preserved'
[IO.Directory]::CreateDirectory($removeBackup) | Out-Null
$removeArchive = Join-Path $removeBackup 'msys2.tar'
Invoke-Tool (Join-Path $env:SystemRoot 'System32\tar.exe') @('-cf', $removeArchive, '-C', $removeRoot, '.')
Save-Json (Join-Path $removeBackup 'snapshot.json') @{ schema = 1; full = $true; msysRoot = $removeRoot; sha256 = (Get-FileHash $removeArchive -Algorithm SHA256).Hash }
Save-Json (Join-Path $removeBackup 'environment-reference.json') @{}
Remove-MsysInstallation $removeRoot $removeBackup @($repo)
Assert (-not (Test-Path $removeRoot)) 'portable MSYS fixture removed'
Assert (Test-Path $removeArchive) 'backup survives uninstall'
Restore-Msys $removeBackup
Assert ((Get-Content (Join-Path $removeRoot 'home\reader\note.txt')) -eq 'test fixture') 'uninstalled files restore from snapshot'

# Fake official uninstaller, intercepting the process boundary; never execute it.
Write-Utf8 (Join-Path $removeRoot 'uninstall.exe') 'not executable'
$module = Get-Module Environment
$nativeTool = & $module { ${function:Invoke-Tool} }
try {
    & $module { function script:Invoke-Tool { param($File, $Arguments) throw 'simulated uninstaller failure' } }
    Assert-Throws { Remove-MsysInstallation $removeRoot $removeBackup @($repo) } 'official uninstaller failure aborts deletion'
    Assert (Test-Path (Join-Path $removeRoot 'home\reader\note.txt')) 'failed uninstaller does not trigger recursive fallback'
    & $module {
        function script:Invoke-Tool {
            param($File, $Arguments)
            if ($File -notlike '*\uninstall.exe' -or ($Arguments -join ' ') -ne 'pr --confirm-command') { throw 'Unexpected uninstaller invocation' }
        }
    }
    Remove-MsysInstallation $removeRoot $removeBackup @($repo)
    Assert (-not (Test-Path $removeRoot)) 'official uninstaller remainder removed'
} finally { & $module { param($original) Set-Item Function:script:Invoke-Tool $original } $nativeTool }
Write-Host "PASS: $script:passed offline checks; fixtures: $root"
