---
id: zephyr-native-powershell
title: 环境安装与源码准备 Windows PowerShell
kind: engineering
status: maintained
domains: [zephyr, windows, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第3章\_环境安装与源码准备：Windows PowerShell

本章从一台 Windows x64 电脑开始，准备原生工具和 Zephyr 源码。所有日常操作都在 PowerShell 中完成；不需要安装 MSYS2。先读 P002 的目录关系，再按本章准备，随后到 P005 安装 SDK、P006 获取源码模块、P008 构建同一个 hello_world。

这里使用 `G:\zephyr_practice\zephyr-main` 作示例源码根。你可以选自己的位置，但后续整套命令要保持同一目录。先检查已有环境，只有缺少时安装，不要求卸载其他项目的工具。

## 3.1\_准备在电脑上执行的工具

CMake 读取工程规则，Ninja 执行生成的编译任务，Python 运行 Zephyr 的配置脚本，Git 用于版本仓库操作，7-Zip 解压 SDK，DTC 和 gperf 支持相应构建环节。先在 PowerShell 查询：

```powershell
# Windows PowerShell；任意目录；只读检查。
Get-Command cmake, ninja, py, git, 7z, dtc, gperf -ErrorAction SilentlyContinue |
    Select-Object Name, Source
py -3.12 --version
```

**先读查询结果的两列：** `Name` 是命令名，`Source` 是 PowerShell 实际找到的程序路径；第 4 行 `py -3.12 --version` 再核对 Python 版本。CMake、Ninja、Git、dtc 也应分别运行 `--version`，确认满足所用源码的要求。本系列采用 Python 3.12；它与最终芯片使用的指令集没有关系，因为 Python 在电脑上运行。

缺少工具时可按 Zephyr 官方 Windows 路线使用 winget；已有工具无须重复安装。需要的安装权限由安装器提示，完成后重新打开 PowerShell：

```powershell
# Windows PowerShell；任意目录；按检查结果安装缺少的工具。
winget install Kitware.CMake Ninja-build.Ninja Python.Python.3.12 Git.Git 7zip.7zip oss-winget.dtc oss-winget.gperf
```

winget 的 Python 3.12 ID 选择一个版本系列，不承诺固定补丁号。若没有 winget，从各工具官方发行页安装匹配 Windows x64 的版本，并确保可执行目录可被当前 PATH 找到。安装来源见[主机工具参考](主机工具与官方安装来源.md)；官方依据是 [Getting Started / Install dependencies](https://docs.zephyrproject.org/latest/develop/getting_started/index.html#install-dependencies) 和源码 `doc/develop/getting_started/index.rst`。

重新打开终端后执行 `cmake --version`、`ninja --version`、`git --version`、`dtc --version` 和 `py -3.12 --version`。路径应指向你选择的原生工具，不应误选 MSYS2 的 usr/bin 程序。若同名命令有多个来源，使用 `Get-Command cmake -All` 核对，并在首次构建时固定正确的可执行文件。

## 3.2\_Git 获取与 ZIP 获取只选一条

下面只取得主源码，不会自动带齐模块和 SDK。Git 获取需要当前网络能连接仓库；有旧 Git 历史但现在网络不通，也要准备已有依赖或走归档补齐路线。

**Git 可用时：** 以下用 HEAD 表示当前检出提交，VERSION 与 SDK_VERSION 分别是源码版本和推荐工具包版本文件。PowerShell 的自动变量 $LASTEXITCODE 保存刚结束的外部程序退出码；非零时立即停止。

```powershell
# Windows PowerShell；准备父目录；目标源码目录必须尚不存在。
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force -Path 'G:\zephyr_practice' | Out-Null
Set-Location -LiteralPath 'G:\zephyr_practice'
if (Test-Path -LiteralPath 'zephyr-main') { throw '目录已存在；先核对并复用，不覆盖' }
git clone https://github.com/zephyrproject-rtos/zephyr.git zephyr-main
if ($LASTEXITCODE -ne 0) { throw '克隆失败；保留现场，检查网络或改走 ZIP' }
Set-Location -LiteralPath '.\zephyr-main'
git rev-parse HEAD
Get-Content VERSION
Get-Content SDK_VERSION
```

**对应 Git 克隆块：** 第 6 行 `git clone` 获取执行时仓库的默认分支，第 9 行 `git rev-parse HEAD` 输出实际提交号，第 10—11 行读取 `VERSION` 与 `SDK_VERSION`。用这三项记录本次源码与推荐 SDK，提交号可能不同于旧截图。正式复现某次实验时应使用已确认的提交或标签并记录它；有自己改动的目录不要为了匹配旧文稿随意切换版本。

**只有 ZIP 时：** SHA256 是 SHA-256 摘要算法的命令参数名，用于核对归档内容是否一致。 在浏览器打开所选官方标签或提交的归档下载，或者接收联网机器转来的同一修订归档。把它放进父目录后执行：

```powershell
# Windows PowerShell；ZIP 已取得；示例文件名请改成实际文件名。
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath 'G:\zephyr_practice'
$archive = '.\zephyr-source.zip'
$unpack = '.\unpacked-zephyr'
if (-not (Test-Path -LiteralPath $archive -PathType Leaf)) { throw '先取得源码归档并填写实际文件名' }
if (Test-Path -LiteralPath $unpack) { throw '解压目标已存在；先检查，不合并覆盖' }
Get-FileHash -LiteralPath $archive -Algorithm SHA256
Expand-Archive -LiteralPath $archive -DestinationPath $unpack
Get-ChildItem -LiteralPath $unpack -Directory
```

**对应 ZIP 解压块：** `$archive` 是已取得的压缩包，`$unpack` 是本次解压目录；`Get-FileHash` 显示本地文件摘要，`Expand-Archive` 解压，末尾 `Get-ChildItem` 列出解压结果。摘要用于比较文件是否相同，不能单独证明源码来源。归档通常带一层 `zephyr-提交号` 或 `zephyr-main`。在资源管理器中找到直接含 VERSION、west.yml 和 samples 的那一层，将其放成最终 `G:\zephyr_practice\zephyr-main`；已有同名目录时先停止，不拖进去合并。这个整理动作只改变外层名字，不创建 Git 历史。

摘要用于以后确认文件是否相同，来源修订仍要结合下载 URL 和记录。没有 .git 时，git rev-parse 或 git describe 失败是预期现象。不要先补 Git 历史才继续准备；在 P006 按同一源码的 west.yml 取得匹配模块归档即可。

完成任一路线后，在最终源码根检查：

```powershell
# Windows PowerShell；最终源码根。
Set-Location -LiteralPath 'G:\zephyr_practice\zephyr-main'
Get-Content VERSION
Get-Content SDK_VERSION
Get-Item west.yml, samples/hello_world/CMakeLists.txt, boards/arm/mps2/board.yml
```

**对应源码检查块：** `Get-Content VERSION` 与 `Get-Content SDK_VERSION` 显示版本记录；`Get-Item` 应找到 `west.yml`、应用的 `CMakeLists.txt` 和板的 `board.yml`。文件缺失时先核对是否选错解压层；不要新建同名空文件蒙混通过。

## 3.3\_为这份源码创建 Windows Python 环境

不同项目可能要求不同的 Python 包版本。venv 为当前项目提供独立安装位置，避免把构建所需包塞进所有项目共用的全局环境。基础解释器仍由 Windows 安装；venv 不是随源码 ZIP 自带的目录。

```powershell
# Windows PowerShell；源码根；py -3.12 已检查通过。
Set-Location -LiteralPath 'G:\zephyr_practice\zephyr-main'
if (-not (Test-Path -LiteralPath '.venv')) {
    py -3.12 -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw '创建 venv 失败' }
}
if (-not (Test-Path -LiteralPath '.venv\Scripts\python.exe')) {
    throw '.venv 存在但不是可用的 Windows 环境；先核对来源'
}
& .\.venv\Scripts\python.exe -c 'import sys; print(sys.executable); print(sys.version); print(sys.platform)'
```

**对应第 10 行的三个输出：** `sys.executable` 显示当前项目的 `.venv/Scripts/python.exe`，`sys.version` 显示 Python 3.12 系列，`sys.platform` 显示 `win32`。若已有 .venv 指向另一种解释器或损坏，不直接覆盖，先保留其包清单再重建。Linux 的 .venv/bin 不能拿到这里运行。

随后给这个解释器安装当前源码需要的基础包，其中包括 west。P002 中用它把多个 Git 仓库组织成工作区；本章先安装这个管理程序，P006 再让它读取具体清单、准备配套模块。因此，安装 west 和取得 Zephyr 源码是不同动作，下面的 pip 命令也不会替你建立 `.west`。公司内部包索引可以提供同一个 west 程序，后续 Git 仓库从哪里取得则由另一份依赖清单决定。

以下安装要求能访问所用包索引；已有包齐全时只做检查，离线材料的收集与本地安装见 [P006 的 6.4](P006_源码依赖与离线准备.md#offline-host-tools)：

```powershell
# Windows PowerShell；源码根；能够访问所用 Python 包索引。
& .\.venv\Scripts\python.exe -m pip install -r scripts/requirements-base.txt 'west==1.5.0'
if ($LASTEXITCODE -ne 0) { throw '依赖安装失败；先读首个网络或依赖错误' }
& .\.venv\Scripts\python.exe -m pip check
if ($LASTEXITCODE -ne 0) { throw '依赖关系检查失败' }
& .\.venv\Scripts\python.exe -m west --version
& .\.venv\Scripts\python.exe -c 'import shutil; print(shutil.which("git"))'
```

**对应安装与检查块：** 第 2 行 `-m pip install` 由指定的 `.venv/Scripts/python.exe` 安装包到项目环境；第 4 行 `pip check` 应返回 `No broken requirements found.`，第 6 行 `west --version` 应返回 1.5.0，第 7 行 `shutil.which("git")` 应输出可用的 Windows Git 路径。west 是安装在这个环境里的 Python 工具；有 west 命令不等于已有 west 工作区，更不等于已经下载 CMSIS。

返回 407 时首先解决代理认证，不把后面的 No matching distribution found 直接当成版本不存在。只能离线安装时转到 P006 的 wheelhouse 分支；venv 不跨电脑直接复制。当前源码若要求不同 west 版本，以其 requirements 为依据调整并记录，不为匹配截图强行降级。

## 3.4\_重新开窗口以后恢复什么

本章一直用完整的项目解释器路径，所以无需修改系统执行策略。新窗口只要重新进入源码根，再调用同一个解释器即可：

```powershell
# Windows PowerShell；新窗口；恢复当前位置并检查项目环境。
Set-Location -LiteralPath 'G:\zephyr_practice\zephyr-main'
& .\.venv\Scripts\python.exe --version
& .\.venv\Scripts\python.exe -m pip check
& .\.venv\Scripts\python.exe -m west --version
```

这不会修改系统 Python，也不会为本窗口自动选择 SDK。环境变量只传给本进程及其后续子进程；CMake 还会在自己的构建目录保存缓存。两者的生效范围在后面的输入与缓存章节展开。

现在主源码和主机 Python 已准备好，下一步到 [P005](P005_SDK准备与编译器选型.md)选择 Windows SDK，再按 [P006](P006_源码依赖与离线准备.md)准备模块。P004 是 UCRT64 的主机适配，PowerShell 读者不必切换终端再做一遍。

配套命令：[当前命令索引](commands/current/P003_环境安装与源码准备_PowerShell/README.md)。

阅读导航：前一阶段：[P002_工程布局与构建全景](P002_工程布局与构建全景.md)；同阶段其他环境：[P003_环境安装与源码准备_Linux](P003_环境安装与源码准备_Linux.md)、[P003_环境安装与源码准备_UCRT64](P003_环境安装与源码准备_UCRT64.md)；下一阶段：[P004_主机工具与Python环境_UCRT64](P004_主机工具与Python环境_UCRT64.md)。
