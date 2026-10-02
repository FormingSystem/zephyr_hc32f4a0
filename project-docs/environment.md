<!-- SPDX-License-Identifier: Apache-2.0 -->

# 当前工程的下载、安装与工具环境

本文说明如何下载本工程、安装主机工具与 SDK、建立 Python 环境并完成首次验收。核对日期：2026-10-01。主线为 Windows x64 + UCRT64 Bash；主机安装和 SDK 安装中标为 PowerShell 的代码块使用 PowerShell，其余工程命令从仓库根目录的 UCRT64 Bash 执行。工具机制见 [learning](../learning/README.md)，源码基线见 [dependencies.lock.json](../dependencies.lock.json)。

当前仓库已包含 Zephyr **4.4.99** 固定节点、HC32 板级支持、CMSIS_6 与华大 HAL。安装者下载的是本工程，随后安装外部工具；无需另建上游 `zephyr-workspace` 或下载 v4.2.0。每条命令成功后再继续；遇到下载或安装错误时先处理错误，不把后续失败当成新的根因。

## 哪些东西由谁提供

| 层 | 当前来源 | 如何选择与验证 |
| --- | --- | --- |
| Zephyr 内核、构建系统、板卡、驱动 | 本仓库受控源码 | project.py 检查根目录与编译数据库 |
| CMSIS_6、华大 HAL | modules/hal 下受控快照 | lock 记录来源；应用与入口限定模块集合 |
| Python 构建/测试包 | 本仓库 .venv | requirements-dev.txt 汇总依赖；pip check |
| west / pyOCD | .venv 中安装 | requirements-tools.txt 固定 1.5.0 / 0.45.1 |
| ARM 编译器、SDK QEMU | 外部 Zephyr SDK 1.0.1 | .local/environment.json 登记；doctor 核对 |
| Git、CMake、Ninja、dtc、gperf | 主机安装 | doctor 查可执行文件与版本 |
| 主机 C 实验的 GCC/GDB | MSYS2 UCRT64 | gcc --version、gdb --version |
| VS Code 插件 | 编辑器安装 | 工作区推荐扩展；不代替编译器 |

`requirements-dev.txt` 引入 Zephyr 的 base、build-test、run-test 依赖以及项目工具依赖。上游若声明版本范围，安装结果可能随时间变化；它不是所有平台通用的完整传递依赖锁。

## 1. 安装 Windows 主机工具

在 PowerShell 中检查 `winget --version`。若没有 WinGet，按 [Microsoft 安装说明](https://learn.microsoft.com/windows/package-manager/winget/)准备；已有工具先检查版本，只安装缺少的部分：

```powershell
winget install --id Git.Git --exact
winget install --id Python.Python.3.12 --exact
winget install --id Kitware.CMake --exact
winget install --id Ninja-build.Ninja --exact
winget install --id oss-winget.gperf --exact
winget install --id oss-winget.dtc --exact
winget install --id 7zip.7zip --exact
```

安装后重新打开终端，使 PATH 生效，再逐项检查：

```powershell
git --version
py -3.12 --version
cmake --version
ninja --version
gperf --version
dtc --version
Get-Command 7z
```

本源码要求 Python 至少 3.12、CMake 至少 3.28.0、dtc 至少 1.4.6，依据是仓库内的[上游主机准备说明](../doc/develop/getting_started/index.rst)与 [CMake 版本检查](../cmake/modules/zephyr_default.cmake)。当前工程已验证 Python 3.12.10；完整依赖选择以锁文件为准。

若 `7z` 找不到，将实际的 7-Zip 安装目录加入用户 PATH 后重开终端。WinGet 不可用时可从 [Git](https://git-scm.com/downloads)、[Python](https://www.python.org/downloads/windows/)、[CMake](https://cmake.org/download/)等官方入口安装，最终仍以上面的命令能找到工具为准。

从 [MSYS2 官方网站](https://www.msys2.org/)安装 MSYS2，打开 **MSYS2 UCRT64** 终端，按其说明完成 `pacman -Syu` 更新；若更新要求关闭终端，重开 UCRT64 后继续更新。在该终端执行 `echo "$MSYSTEM"`，应得到 `UCRT64`。

UCRT64 提供 Bash，工程 Python 使用 Windows Python。主机 C 实验另需 UCRT64 GCC/GDB，可在 UCRT64 终端按需安装：

```bash
pacman -S --needed mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-gdb
```

这些主机 GCC/GDB 用于学习实验；HC32 固件使用下一节 SDK 内的 ARM 编译器。后文用 `py -3.12` 创建 Windows Python 环境，即使从 Bash 执行，激活路径仍为 `.venv/Scripts/activate`。

## 2. 下载本工程并核对目录

**已经打开本工程的读者直接核对当前路径，跳过 clone。** 在当前工程终端运行：

```bash
pwd
git rev-parse --show-toplevel
git remote -v
```

Git 根目录应是你当前打开的项目文件夹，远程应对应 `FormingSystem/zephyr_hc32f4a0`。若同名目录出现多个副本，先确定当前项目的完整路径，不在旧副本继续操作。

首次下载时，在自己选择的源码存放目录打开 UCRT64 Bash，创建一个新的专用工作区。下面的 `mkdir` 若提示目录已存在，先检查内容或另选目录，不继续覆盖已有工作区：

```bash
mkdir hc32-workspace
cd hc32-workspace
git clone https://github.com/FormingSystem/zephyr_hc32f4a0.git
cd zephyr_hc32f4a0
git rev-parse --show-toplevel
git remote -v
git rev-parse HEAD
```

HTTPS 与协作约定中的 SSH 地址指向同一仓库；访问私有仓库时需要相应账号权限。记录 `HEAD` 可准确说明安装使用的项目提交，不能把上游 Zephyr 标签当成本工程的发布标签。若维护者指定发布修订，使用该修订后再读取其依赖文件。

clone 会取得当前 HC32 构建所需的受控源码。这里不用 `west init -m` 下载另一个 Zephyr，也不用上游 `west update` 补齐已有模块。本项目活动清单为 `project-west.yml`，其中 `projects: []` 表示模块已经内置。工作区父目录的 `.west/` 后面由项目脚本配置。

## 3. 下载并安装 Zephyr SDK 1.0.1

打开 [SDK 1.0.1 官方发行页](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v1.0.1)，在 SDK Bundle 表中选择 **Windows / GNU / x86-64**，文件名为 `zephyr-sdk-1.0.1_windows-x86_64_gnu.7z`。同时下载该发行版的 `sha256.sum`。这是当前锁文件要求的版本；换用其他项目修订时先核对锁文件，不直接选择最新发行版。

在下载文件所在目录的 PowerShell 中执行：

```powershell
Get-FileHash -Algorithm SHA256 .\zephyr-sdk-1.0.1_windows-x86_64_gnu.7z
Select-String -LiteralPath .\sha256.sum -Pattern 'zephyr-sdk-1\.0\.1_windows-x86_64_gnu\.7z$'
```

比较两处 SHA-256，忽略字母大小写后必须一致。相同版本的 minimal 包不包含工具链，需要另外下载；LLVM 包不满足当前 GNU 工具链入口。使用 GNU 完整包可以减少首次安装时的工具链选择步骤。

用 7-Zip 将安装包解压到自选工具目录，SDK 放在源码仓库外。然后在解压出的 `zephyr-sdk-1.0.1` 目录打开 PowerShell，执行：

```powershell
.\setup.cmd /t arm-zephyr-eabi /h /c
Get-Content .\sdk_version
Test-Path .\gnu\arm-zephyr-eabi\bin\arm-zephyr-eabi-gcc.exe
Test-Path .\hosttools\qemu\qemu-system-arm.exe
```

`/t` 选择 ARM GNU 工具链，`/h` 安装主机工具，`/c` 注册 SDK 的 CMake 包。安装可能仍需联网；不能将只解压 minimal 包视为完成安装。预期版本为 `1.0.1`，两项路径检查均为 `True`。SDK 目录移动后应重新运行 setup 并重新登记项目 SDK 路径。安装布局参见[仓库内 SDK 说明](../doc/develop/toolchains/zephyr_sdk.rst)。

SDK 安装需要先完成，是因为项目的 `setup_environment.py` 会检查 SDK 版本及 ARM 编译器后才创建 `.venv`。不用先建立一个临时上游 Zephyr 工作区来安装 SDK。

## 4. 创建根目录 Python 环境并配置 west

回到**本工程根目录的 UCRT64 Bash**。输入 SDK 的实际目录时使用 Windows 可识别的路径，例如盘符路径并采用正斜杠；不要把 Bash 的 `/盘符/...` 路径直接写入项目配置。

```bash
read -r -p "请输入已安装的 SDK 目录: " SDK_DIR
py -3.12 scripts/setup_environment.py --sdk "$SDK_DIR"
source .venv/Scripts/activate
python scripts/configure_west.py
python scripts/project_env.py doctor
```

可以输入自己机器的 SDK 路径；不要把示例作者的路径抄进仓库。setup 不下载 SDK、不修改全局 Python，不自动改 Git 配置。它创建或复用根目录 .venv、安装依赖、执行 pip check，将 SDK 路径和编辑器本机设置写入被忽略的 .local、.vscode。项目 Git 钩子初始化是独立的 `python scripts/git_setup.py`。

`configure_west.py` 在当前克隆的父目录生成 `.west/config`，指向本项目 `project-west.yml`。父目录已有其他工作区时脚本拒绝覆盖，应先检查实际布局。完成后可以确认：

```bash
python -c "import sys; print(sys.executable)"
python scripts/project_env.py exec west topdir
python scripts/project_env.py exec west manifest --path
```

解释器应位于当前工程 `.venv/Scripts`；west 根应为当前工程父目录；清单路径应指向当前工程 `project-west.yml`。目录结构与冲突恢复见[项目 west](west/README.md)。项目入口显式绑定当前 Zephyr，无需再执行 `west zephyr-export`。

## 5. 首次构建与软件验收

仍在工程根目录、已激活 `.venv` 的 UCRT64 Bash 中逐条执行：

```bash
python scripts/project_env.py check
python scripts/project_env.py build
python scripts/project_env.py test
```

| 检查 | 应观察的结果 | 能说明什么 |
| --- | --- | --- |
| `doctor` | 工具与模块路径正确，依赖检查通过 | 当前环境绑定到本工程及匹配 SDK |
| `check` | 工具测试和 pyOCD 离线配置检查通过 | 工程辅助工具与离线配置可用 |
| `build` | 生成 `build/bringup/zephyr/zephyr.elf`，镜像与源码来源审计通过 | HC32 目标可以编译、链接并通过镜像检查 |
| `test` | QEMU 软件测试通过，记录位于 `build/twister/` | `mps2/an386` 模拟目标的软件回归通过 |

上述步骤无需连接开发板。HC32 构建目标是 `uyup_rpi_a/hc32f4a0pitb`；QEMU 使用另一个目标，两者产物用途不同。真正的探针连接、下载和板上运行按[开发与调试](development.md)及[硬件操作](hardware.md)单独进行，不用模拟结果代替板卡验收。

## 6. 每次打开工程后继续工作

在当前工程根目录打开 UCRT64 Bash，只需：

```bash
source .venv/Scripts/activate
python scripts/project_env.py doctor
python scripts/project_env.py build
```

也可不激活，直接使用 `.venv/Scripts/python.exe scripts/project_env.py build`。Linux 使用满足版本要求的 python3 创建环境，解释器与激活路径分别换成 .venv/bin/python、.venv/bin/activate；Linux/macOS 分支尚未在本轮实测。

已有工作区不需要再次 clone 或初始化 west。切换项目提交后若依赖变化，重新运行安装入口；SDK 版本变化时先安装对应 SDK，再用 `--sdk` 登记。新机器及发布流程见[发布与重建](distribution.md)。

## 7. Ubuntu 的对应入口

Ubuntu 24.04 x86_64 可按以下方式安装主机依赖；本轮只核对命令与工程脚本，未在 Linux 重建环境：

```bash
sudo apt update
sudo apt install --no-install-recommends git cmake ninja-build gperf \
  ccache dfu-util device-tree-compiler wget python3-dev python3-venv python3-tk \
  xz-utils file make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1
python3 --version
cmake --version
dtc --version
```

仍需满足 Python 3.12、CMake 3.28.0 和 dtc 1.4.6 下限。Ubuntu 22.04 默认工具版本可能不足，不能照抄旧版本 Zephyr 的安装下限。ARM64 主机须按对应平台调整 multilib 软件包与 SDK 架构。

按第 2 节 clone 工程，并从同一 SDK 发行页下载 Linux GNU x86-64 包，核对 SHA-256、解压后在 SDK 目录执行 `./setup.sh`，安装 ARM 工具链与主机工具。之后回到工程根目录执行：

```bash
read -r -p "请输入已安装的 SDK 目录: " SDK_DIR
python3 scripts/setup_environment.py --sdk "$SDK_DIR"
source .venv/bin/activate
python scripts/configure_west.py
python scripts/project_env.py doctor
python scripts/project_env.py check
python scripts/project_env.py build
python scripts/project_env.py test
```

Linux 使用其本机路径和 `.venv/bin`，不能复用 Windows 虚拟环境。WSL 的编译环境与 USB 探针接入也需分别验证。

## 入口究竟配置了什么

[setup_environment.py](../scripts/setup_environment.py) 管安装；[project_env.py](../scripts/project_env.py) 管每条命令运行时的环境；[project.py](../scripts/project.py) 管工程动作。后者通过 exec 入口也可包装 CMake、west、Twister、课程脚本。

project_env.py 总是定位当前克隆的 .venv，SDK 优先读 .local 配置，再读 ZEPHYR_SDK_INSTALL_DIR。它设置 ZEPHYR_BASE、ZEPHYR_MODULES、ZEPHYR_TOOLCHAIN_VARIANT，清除会串入其他工程的 PYTHONPATH 和额外模块环境变量。Windows 下补充已安装的用户/系统 PATH，并优先使用 Git for Windows，避免 MSYS Git 路径输出与 Windows Python 混用。

应用 [samples/bringup/CMakeLists.txt](../samples/bringup/CMakeLists.txt) 也明确绑定当前源码与模块。新增模块按 [CMake P02](../learning/cmake/P02_接入Zephyr模块.md) 在应用声明，不依赖终端里遗留的环境变量。

## 迁移、重建和故障

.venv 不可作为可搬运工具包；换电脑或移动克隆后，保留依赖文件，重新创建环境并安装。先退出旧环境，把旧 .venv 移到自己确认的备份位置，再运行 setup；不要删除未核对的目录。已有 .local SDK 路径有效时可省略 --sdk。

`python -m pip check` 查包依赖一致性；doctor 查工程环境；check 查工具逻辑与离线调试配置；build 查 HC32 编译；test 查 QEMU 软件运行。它们是不同证据，最后两项也不能证明真实 PCB 正确。

若 .venv 缺失，入口明确失败，不借用相邻工程的环境。若 SDK 版本不符，安装正确版本后重新 --sdk。若 VS Code 记住其他 Python，在 Python: Select Interpreter 中选择本仓库 .venv。带注释的既有 settings.json 不被 setup 自动重写，按提示手工选择解释器与工具链路径。

原 PowerShell 入口保留兼容；新机器主线使用上述 Bash + Python。发布时提交哪些配置见[发布说明](distribution.md)。

| 现象 | 从哪里检查 |
| --- | --- |
| 安装后工具仍找不到 | 重开终端；PowerShell 用 `Get-Command`、Bash 用 `command -v` 检查工具路径 |
| SDK 下载失败或解压失败 | 区分网络、Release 附件、磁盘空间和 `7z` 错误；校验值不一致时重新下载 |
| setup 提示 SDK 版本或编译器缺失 | 检查 `sdk_version` 与 `gnu/arm-zephyr-eabi/bin`，确认选择 GNU 包且完成 SDK setup |
| Python 包安装失败 | 保留 pip 首个错误；检查网络、所用 Python 版本及 requirements 文件，修复后重跑 setup |
| west 清单来自其他工程 | 核对当前克隆与父目录 `.west/config`，按项目 west 文档处理，不直接覆盖已有配置 |
| `unknown command build` | 先配置项目 west，再检查实际清单；日常构建可使用 `project_env.py build` |
| 固件构建成功但 QEMU 失败 | 检查 SDK `hosttools/qemu` 和测试日志，编译器可用不代表模拟器可用 |

报告问题时附上失败命令、完整文本输出、`git rev-parse --show-toplevel`、`git rev-parse HEAD` 和 doctor 输出。首次下载依赖网络，重试时保留已有源码和个人修改，不删除整个工程作为恢复手段。

本次安装文档的核对与实测范围单独记录在[移植状态](porting-status.md)；既有环境检查不能代替全新机器下载安装验证。
