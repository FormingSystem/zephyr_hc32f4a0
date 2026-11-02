---
id: zephyr-p002-module-1
title: 主机工具与 Python 环境
kind: engineering
status: evolving
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第4章\_主机工具与Python环境：UCRT64

上一章留下了 `zephyr-main` 源码，里面已经有 `hello_world` 应用和 `mps2/an386` 的板支持。可是文件放在磁盘上不会自行变成固件：CMake 要读取构建规则，Ninja 要执行编译任务，Python 要运行 Zephyr 的配置和模块工具。本章先让这些**在 Windows 主机上执行的程序**可用，并把项目需要的 Python 包放到同一份 `.venv`；下一章才准备生成 ARM 指令的目标编译器。

对照板与后续 HC32 板共用这套主机环境，因此不因换芯片而重装一份 Python。我们要能在任意一个新开的 UCRT64 窗口里，回到同一源码根并恢复它。 返回 [环境与依赖导航](环境与依赖导航.md)。各章独立编号，完整复制单元按当前小节编号放在 [当前命令索引](commands/current/P004_主机工具与Python环境_UCRT64/README.md)。

**官方译文对照：** [入门指南的主机依赖与 Python 环境](../zephyr_docs/getting_started/P002_入门指南.md)。本章保留教程选择的 Windows CPython 3.12.10、west 1.5.0 和 UCRT64 操作顺序；官方完整工作区的 `west packages` 流程与本章先安装基础构建依赖的步骤应分开理解。

实验源码根为 Windows 的 `G:\zephyr_practice\zephyr-main`，UCRT64 中为 `/g/zephyr_practice/zephyr-main`。默认 UCRT64；Windows 专用 setup.cmd 等步骤按正文切换 PowerShell。各模块不重复安装已经完成的前置工具。

**复制命令：** [当前命令索引](commands/current/P004_主机工具与Python环境_UCRT64/README.md)。按正文选择分支，不把整个目录的命令依次执行。

<a id="section-4-1"></a>

## 4.1\_固定 UCRT64 工具与 Windows Python

```mermaid
flowchart LR
    S1["1 主机工具"]
    S2["2 Python 与 venv"]
    S3["3 SDK"]
    S4["4 依赖选择依据"]
    S5["5 CMSIS；HC32 再备 HAL"]
    S6["6 交接检查"]
    S1 --> S2 --> S3 --> S4 --> S5 --> S6
    style S1 stroke:#007F8A,stroke-width:3px
```

先确认自己仍在上一期的终端里。进入某个叫 `ucrt64` 的文件夹并不会切换环境，判断依据是启动器和环境标识：

```bash
# 当前位置：任意目录；终端：MSYS2 UCRT64。
echo "$MSYSTEM"
echo "$MINGW_PREFIX"
```

**对应第 2—3 行：** `echo "$MSYSTEM"` 应输出 `UCRT64`，`echo "$MINGW_PREFIX"` 应输出 `/ucrt64`。如果不是，重新打开 MSYS2 UCRT64，再回到本节。上一期没有完成系统更新的读者，先执行 `pacman -Syu`，按提示关闭并重开终端后继续更新；不要只同步软件包数据库而长期不升级系统。

<a id="section-4-1-1"></a>

### 4.1.1\_安装 UCRT64 原生构建工具

当前选择的是 UCRT64 路线，所以 CMake、Ninja 和 DTC 统一使用 UCRT64 的 Windows 原生包。PowerShell 原生路线已经在 P003 的对应章节独立说明，不在两个安装路线间来回切换。

```bash
# Windows UCRT64；任意目录；已完成系统更新，只安装缺失包。
pacman -S --needed mingw-w64-ucrt-x86_64-cmake \
  mingw-w64-ucrt-x86_64-ninja mingw-w64-ucrt-x86_64-dtc \
  mingw-w64-ucrt-x86_64-gperf mingw-w64-ucrt-x86_64-7zip
type -a cmake ninja dtc gperf 7z cygpath
/ucrt64/bin/cmake --version
/ucrt64/bin/ninja --version
/ucrt64/bin/dtc --version
```

**对应主机工具安装块：** 第 2—4 行 `pacman -S` 安装原生 UCRT64 包；第 5 行 `type -a` 核对入口，第 6—8 行分别显示 CMake、Ninja、dtc 版本。构建工具使用 `/ucrt64/bin` 下的程序；负责路径转换的 `cygpath` 则应来自当前 MSYS2 的 `/usr/bin`，不能混用其他软件附带的同名程序。`/usr/bin/cmake` 属于另一套运行时，不作为本教程的构建入口。后续 Zephyr 配置明确调用 /ucrt64/bin/cmake，并把跨进程路径转换成 Windows 绝对路径。P008 给出完整操作，不只凭同名命令的版本判断。

Windows SDK 的 setup.cmd 在 PowerShell 中运行，需要该窗口能找到 Windows CMake 和 7-Zip。若 PowerShell 的 Get-Command cmake,7z 找不到，可以从官方安装器准备这两个 Windows 工具，并重开窗口；这不改变 UCRT64 构建固定使用的工具来源。

Python 单独使用 Windows CPython 创建的项目 .venv，不把 pacman 自带 Python 当作它的替代品。这样 pip、west 和 CMake 子进程可固定到同一个解释器。

Windows CPython/west 应配合 Windows 原生 Git。本系列优先使用 P003 准备的 `/ucrt64/bin/git`，已安装的 Git for Windows 也可复用。`/usr/bin/git` 依赖 MSYS2 运行时，与 Windows Python 的调用边界不同；只看 `git --version` 无法确认选中哪一种。本次故障记录是在 Windows west 调用 `/usr/bin/git` 时看到 `^{commit}` 变成 `^commit`，保持清单和提交不变、改用 `/ucrt64/bin/git` 后恢复；花括号具体在哪一层改变尚未跟踪定位。原生版本的区分见 [MSYS2 Git 说明](https://www.msys2.org/docs/git/)，完整故障证据见 [Git 兼容故障参考](reference/CMSIS来源与历史排错.md#west-git-compat)。

```bash
# Windows UCRT64；任意目录；先查看别名、函数和多个 Git 候选。
type -a git
command -v git
```

若 `type -a` 的优先项是别名或函数，先检查自己的 Bash 配置，消除遮蔽。主线 `command -v git` 应为 `/ucrt64/bin/git`（可带 `.exe` 后缀）；**仍为 `/usr/bin/git` 时，停止 west 模块下载，先按下面的同章步骤修复**。已有正确路径时跳过补装和 PATH 调整。

若原生 Git 缺失，下面仅补装 `mingw-w64-ucrt-x86_64-git`；若已经安装但路径选错，则只调整当前终端。运行前必须已完成 P003 的完整系统更新；遇到旧包数据库错误先返回 P003 更新，不使用 `pacman -Sy` 单独刷新后继续。本块附件：[复制完整命令](commands/current/P004_主机工具与Python环境_UCRT64/004-bash.txt)。

```bash
# Windows UCRT64；任意目录；P003 完整系统更新已完成。
# 仅原生 Git 缺失或当前窗口选错路径时执行；已有正确选择则跳过。
if ! test -x /ucrt64/bin/git.exe; then
  pacman -S --needed mingw-w64-ucrt-x86_64-git
fi
if test -x /ucrt64/bin/git.exe; then
  export PATH="/ucrt64/bin:$PATH"
  hash -r
else
  printf '原生 Git 尚未可用，停止模块下载并检查安装错误。\n' >&2
fi
type -a git
command -v git
```

**对应修复块末尾的两项查询：** `type -a git` 检查别名、函数及候选程序，`command -v git` 确认最终入口为原生 Git 路径。此处核对的是 Bash 命令入口；4.2 创建或激活 Windows Python 环境后，还要核对 Python 实际找到的 Git，两步不能互相替代。

**备用：复用已安装的 Git for Windows。** 只有决定使用这条路线时才运行下块，无需再安装一份 Git。在资源管理器找到该安装的 `cmd` 目录（含 git.exe，默认常为 `C:\Program Files\Git\cmd`）。`GIT_CMD_DIR` 只是本块接收粘贴路径的临时 Bash 变量，不是 Zephyr 设置；它用于 PATH，随后删除。不要填写作者电脑的安装位置。

```bash
# Windows UCRT64；备用路线：复用已有 Git for Windows；粘贴真实 cmd 目录，不加引号。
read -r -p 'Git for Windows 的 cmd 目录：' GIT_CMD_DIR
if test -f "$(cygpath -u "$GIT_CMD_DIR")/git.exe"; then
  export PATH="$(cygpath -u "$GIT_CMD_DIR"):$PATH"
  hash -r
else
  printf '该目录没有 git.exe，停止模块下载并核对安装位置。\n' >&2
fi
unset GIT_CMD_DIR
type -a git
command -v git
```

PATH 调整只影响当前 UCRT64 及其子进程；重开终端后重新检查，或把核对后的实际目录写入自己的 Bash 启动配置。前面的官方安装仍在 PowerShell 中，接下来 Git/west 命令继续在 UCRT64 执行。

<a id="section-4-1-2"></a>

### 4.1.2\_固定 Windows Python 3.12.10

本教程固定 **Windows CPython 3.12.10 x64**，west 固定 **1.5.0**，项目包统一装入源码根的 `.venv`。这里固定的是两个工具版本，不表示 pip 和所有传递依赖也已锁定。

原生源码的 `doc/develop/getting_started/index.rst` 给出主机要求，`cmake/modules/python.cmake` 的 `PYTHON_MINIMUM_REQUIRED` 检查最低版本；它们没有要求只能使用 3.12.10。`.github/workflows/assigner.yml` 中的 `python-version: 3.12` 只为该 CI 任务选择解释器，不能作为所有构建的版本要求。

![CI 任务选择 Python 系列，不能替代构建最低要求](assets/p002-ci-python-series.png)

先分清“下载过安装器”和“安装过 Python”：电脑里有一个 `.exe` 文件，只能说明安装器已取得。先在 UCRT64 执行下面的版本选择；输出为 3.12.10 就复用已有安装，不必找到或复制教程中的安装目录。

```bash
# Windows UCRT64；任意目录；检查已安装的 3.12 系列解释器。
py -3.12 --version
```

若提示找不到 `py`，先看 4.1.4 的无 Launcher 分支，不立即断定 Python 未安装。若 Launcher 明确报告没有 3.12，再从下列两种安装方式选一种。`-3.12` 选择的是系列，输出中的补丁号仍须核对为本教程的 3.12.10。

[Python 3.12.10 发行页](https://www.python.org/downloads/release/python-31210/)提供本章的 Windows 安装器。这是 3.12 系列最后一个完整维护版本，后续版本仅做安全修复；3.12.10 用作本教程的可复现安装基线，不代表最新安全版本。不要执行 `pacman -S mingw-w64-ucrt-x86_64-python` 来“固定 3.12”：MSYS2 是滚动仓库，该命令取得仓库当时的版本，且 MSYS2 Python 与官方 Windows Python 的包兼容性不同。版本变化可查 [MSYS2 Python 包页](https://packages.msys2.org/packages/mingw-w64-ucrt-x86_64-python)；正文不写死它将来安装哪个版本。

下面三种操作各有目的：Windows 图形安装和 UCRT64 命令安装是**二选一**的基础解释器安装方式；随后都检查 UCRT64 如何定位解释器；最后统一创建 `.venv`。如果机器已有 3.12.10，不再重复安装，直接进入 4.1.4。已有本项目 `.venv` 的读者直接按 4.2.2 激活并检查，版本正确即可继续。

![Python 官方下载页的 Windows 安装器选择](assets/p002-python-official-download.png)

Windows 图形安装：仅在尚未安装所需版本时，打开上述发行页，在 **Files** 表选择 **Windows installer (64-bit)**，文件名为 `python-3.12.10-amd64.exe`。`amd64` 也适用于 Intel x64 电脑。默认安装位置即可；选择 Customize installation 时也可以保留自己已有的工具目录。保留 pip 和 Python Launcher；Python Launcher（`py`）可用于发现解释器，Add python.exe to PATH 则控制命令搜索路径，两者作用不同。安装完成后重开 UCRT64。不要下载源码包或 embeddable package 来替代完整安装器。

![下载到的 Python 安装程序](assets/p002-python-download-file.png)

![安装首页的自定义安装入口](assets/p002-python-installer-start.png)

以下两张为保留的 Windows Python 安装截图。目录示范是 `E:\python\python3_12`，不是必选路径；调试符号和调试二进制是可选项，Zephyr 基础环境不要求勾选。

![Windows Python 的 pip 和 Launcher 组件](assets/p002-python-features-annotated.png)

![Windows Python 自定义安装位置](assets/p002-python-location-annotated.png)

![Windows Python 安装完成](assets/p002-python-install-success.png)

### 4.1.3\_从 UCRT64 下载并安装官方 Python

这条路线与上面的图形安装二选一，安装的仍是 Windows CPython。它只改变下载、启动安装器的操作方式，安装后的使用方式相同。已有 3.12.10 时直接跳到 4.1.4。

先看 Windows 下载目录是否已经保存官方 `python-3.12.10-amd64.exe`。已有文件时，核对来源和文件属性中的数字签名，直接从资源管理器运行；不用为了匹配下方路径再下载一份。没有安装器时，下面将它保存到 `G:\zephyr_practice\downloads`，对应 UCRT64 的 `/g/zephyr_practice/downloads`。这里仅保存下载文件，Python 不会安装在这个目录。

```bash
# Windows UCRT64；仅在没有官方 3.12.10 安装器时下载。
mkdir -p /g/zephyr_practice/downloads
cd /g/zephyr_practice/downloads
curl -fL https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe \
  -o python-3.12.10-amd64.exe
```

下载正常结束后，在同一终端执行下面的安装命令。若 curl 报错，先解决下载问题，不启动未下载完整的文件。安装器采用 Windows 的默认用户安装位置，不放入 Zephyr 源码或 `build`。

```bash
# Windows UCRT64；官方安装器已完整下载，尚未安装该版本。
cd /g/zephyr_practice/downloads
MSYS2_ARG_CONV_EXCL='*' ./python-3.12.10-amd64.exe \
  /passive InstallAllUsers=0 PrependPath=1 \
  Include_pip=1 Include_launcher=1 InstallLauncherAllUsers=0 Include_test=0
```

**对应安装器参数块，从上往下读：** 第 3 行 `MSYS2_ARG_CONV_EXCL='*'` 仅对这次调用关闭 MSYS2 参数路径转换，保留 `/passive` 原样；第 4 行 `/passive` 显示安装进度，`InstallAllUsers=0` 安装给当前用户，`PrependPath=1` 让新终端可找到 Python；第 5 行 `Include_pip=1` 保留包安装器，`Include_launcher=1` 安装 `py`，`InstallLauncherAllUsers=0` 将启动器也装给当前用户，`Include_test=0` 不安装 Python 自带的测试套件。参数依据见 [Python 官方安装说明](https://docs.python.org/3.12/using/windows.html#installing-without-ui)。

等待安装成功后，关闭当前 UCRT64 并重新打开，再按下一节选择解释器。若进入 Modify/Repair 维护界面，说明已有安装；先核对版本，不能用换目录的方式假定安装了第二份。

### 4.1.4\_用版本选择解释器，再交给虚拟环境

`py -3.12` 让 Windows Launcher 查找已安装的 3.12 解释器，安装在 C 盘还是 E 盘都不改变这条命令。`python` 则由当前终端的 PATH 决定。前者能执行而后者报 `command not found`，通常只是短命令尚未进入 PATH；不需要为此重装或移动 Python。

```bash
# Windows UCRT64；安装完成后重新打开的终端，任意目录。
py -3.12 --version
py -3.12 -m pip --version
```

确认第 2 行 `py -3.12 --version` 的输出是 Python 3.12.10，第 3 行 `py -3.12 -m pip --version` 能显示对应的 pip，就可以用 `py -3.12 -m venv .venv` 创建工程环境，具体位置见 4.2.1。pip 输出中出现安装路径只是说明它属于哪个 Python，**不要求你的路径与截图一致，也不要求复现一个测试目录**。

![UCRT64 用 py 检查 Windows Python 身份](assets/p002-python-launcher-check.png)

截图保留了当时的 `sys.executable` 和 `win32` 输出，用于解释“这是 Windows Python”。日常步骤只需要选择版本和激活环境，不必重复获取这些路径。

**没有 Launcher，但 python 已可执行。** 如果安装时选过 Add python.exe to PATH，重新打开 UCRT64 后可以检查：

```bash
# Windows UCRT64；任意目录；只用于 py 不存在但 python 可执行的分支。
python --version
python -m pip --version
```

只有输出同样为 3.12.10 时，才将下一节创建命令换为 `python -m venv .venv`。版本不符时不要使用它创建环境；可以用官方安装器 Modify 补上 Launcher 后使用 `py -3.12`。若两个命令都找不到，先重新打开终端，再检查 Windows“已安装的应用”或安装器维护界面，确认是否已安装及是否勾选 Launcher/PATH。

这两种入口都只负责第一次创建 `.venv`。激活之后，后续统一用 `python -m pip`、`python -m west` 和 `python 脚本.py`；不要继续用带版本的 `py -3.12 -m pip` 安装项目依赖，否则会选回基础解释器。项目环境的激活会为当前 Bash 设置命令查找顺序，无需另写基础 Python 的路径变量或修改 `.bashrc`。

<a id="section-4-2"></a>

## 4.2\_给正确的\_Python\_安装依赖包

```mermaid
flowchart LR
    S1["1 主机工具"]
    S2["2 Python 与 venv"]
    S3["3 SDK"]
    S4["4 依赖选择依据"]
    S5["5 CMSIS；HC32 再备 HAL"]
    S6["6 交接检查"]
    S1 --> S2 --> S3 --> S4 --> S5 --> S6
    style S2 stroke:#007F8A,stroke-width:3px
```

现在基础 Python 已经能执行，但 Zephyr 的配置脚本还需要 Python 库。把包直接装进电脑的全局 Python，会让不同项目共享同一份版本选择。本期使用 **Python 虚拟环境（virtual environment，venv）**：为项目准备独立的解释器入口和包目录，安装动作由这个环境自己的 **pip 包安装器** 完成。

下面继续在同一份实验源码中创建 `.venv`，再说明下次打开终端如何恢复。本主线不另建 `build/learning-tools/west-textbook-tools`，避免后续命令混用两个环境。HC32 适配也沿用这里的环境，不要求尚未创建的项目安装脚本。

### 4.2.1\_上一期下载的是上游\_Zephyr\_源码

回到上一期的源码目录。这里使用 `.venv` 作为本次练习自定的环境目录名；如果已经有可用 `.venv`，直接激活并检查，不覆盖或删除现有环境。下面直接使用 UCRT64 路径：

```bash
# 当前位置：任意目录；终端：UCRT64。输入上游源码根目录。
cd /g/zephyr_practice/zephyr-main
# 当前位置：上游 Zephyr 源码根目录。
ls VERSION SDK_VERSION scripts/requirements-base.txt
```

确认源码目录后，使用 4.1.4 已核对为 3.12.10 的 Launcher 创建环境。下面是**第一次创建**的步骤；若本目录已经有 `.venv`，直接用 4.2.2 激活并检查。

```bash
# 当前位置：上游 Zephyr 源码根目录；终端：UCRT64。
py -3.12 -m venv .venv
source .venv/Scripts/activate
python --version
python -m pip --version
python -c "import sys; print(sys.executable)"
python -c "import shutil; print(shutil.which('git'))"
```

**对应创建环境块：** 第 2 行 `py -3.12 -m venv .venv` 使用 4.1 节核对过的解释器创建环境；第 3 行 `source .venv/Scripts/activate` 让当前 Bash 优先使用它。第 4 行检查 Python 版本，第 5 行的 pip 路径应包含当前工程 `.venv`，第 6 行 `sys.executable` 应指向这份 `.venv/Scripts/python.exe`。它们用于确认项目包的归属，盘符不必与截图一致。即使终端是 Bash，Windows Python 的激活脚本仍在 `Scripts/activate`，不是 Linux 教程里的 `bin/activate`。

最后一行用 `shutil.which('git')` 查看**这一个 Windows Python 按 PATH 找到的 Git**。主线应输出 MSYS2 安装目录下的 `ucrt64/bin/git.exe`；备用路线应输出前面已核对来源的 Git for Windows `cmd/git.exe`。Windows 的反斜杠和扩展名大小写不影响判断。**若为 `None` 或落在 `usr/bin/git.exe`，停止后续 west 模块下载，返回 4.1.1 修复，再重新执行这两行；不要以 Bash 能运行 Git 或版本号能打印作为通过条件。**

已有 `.venv` 时，只需激活并核对，不再创建。独立复核操作见 [当前命令索引](commands/current/P004_主机工具与Python环境_UCRT64/README.md)。

现在才开始安装包，避免把“装了哪个包”和“给哪个 Python 装包”混在一起。这里一并安装 west：它负责读取 P002 中的依赖清单，并调用 Git 管理多个源码仓库。这个程序装进 `.venv`，工作区配置却由之后的 init 保存在父目录 `.west`，二者作用不同。安装完成只代表工具能运行，P006 才把它与当前源码和模块关联起来；需要构建时，P008 先直接使用 CMake，P009 再解释 west 怎样提供同一构建过程的命令入口。

下面要求能访问所用 Python 包索引，内部索引也可以提供这些包。完全离线时使用 [P006 的本地包安装](P006_源码依赖与离线准备.md#offline-host-tools)，已有依赖齐全时不重复安装：

```bash
# 当前位置：上游 Zephyr 源码根目录；终端：UCRT64，已激活 .venv。
python -m pip install -r scripts/requirements-base.txt "west==1.5.0"
python -m pip check
python -m west --version
```

`west==1.5.0` 与 `-r` 放在同一次解析中，固定本教程使用的 west，版本见 [west 1.5.0 官方发布记录](https://pypi.org/project/west/1.5.0/)。源码升级后若依赖冲突，先核对版本要求，不忽略错误继续安装。`-r` 让 pip 读取当前源码列出的包要求；pip 从包索引解析并下载适合此解释器的文件，放入 `.venv`。此修订的 base 清单包含 west；若使用的其他修订拆分了依赖文件，按该修订的说明选择清单。成功后 `pip check` 应报告 `No broken requirements found.`，west 应返回 `West version: v1.5.0`。测试、文档生成等任务可能还需要额外依赖，本节只建立基础构建工具环境。

下载慢时可以仅对这次安装指定索引，例如把安装命令替换为 `python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r scripts/requirements-base.txt "west==1.5.0"`。这只影响 pip，不影响 SDK；镜像缺包或同步延迟时恢复默认索引重试，先保留原始错误信息。不要通过关闭证书校验来处理普通的超时。

west 可以运行，只表示管理工具已安装。P006 才会检查或建立 `.west` 工作区，读取当前 `west.yml` 并取得 MPS2 对照示例配套的 cmsis 与 cmsis_6；P010 先解释官方工程的驱动模型，P011 再展开构建系统的模块发现。`pip install west` 不会下载 CMSIS，也不会令当前目录自动变成 west 工作区。按 P014 准备 HC32 时再增加它所需的 HAL，不能把华大 DDL 当成所有 ARM 应用的公共前提；更完整的模块管理见 [west 大纲](../west/大纲.md)。

### 4.2.2\_重新打开终端后恢复环境

工具安装完成后，重新开一个 UCRT64 窗口，确认环境能从磁盘恢复：

```bash
# 当前位置：任意目录；终端：UCRT64。
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
python --version
python -m pip --version
python -m pip check
python -m west --version
python -c "import sys; print(sys.executable)"
python -c "import shutil; print(shutil.which('git'))"
```

**对应恢复块第 4—9 行：** `python --version` 应为 3.12.10；`pip --version` 和 `sys.executable` 应指向当前项目 `.venv`；`pip check` 应通过；`west --version` 应返回 1.5.0；末行 `shutil.which('git')` 应仍找到 `ucrt64/bin/git.exe`，或已核对的 Git for Windows `cmd/git.exe`。**若重开窗口后变成 `usr/bin/git.exe` 或 `None`，先停止 west 模块下载，回到 4.1.1 修复当前窗口的 PATH，再复核。** 前一次终端中的 `export PATH` 不会自动传到这次新终端。

这里只恢复 Python 工具环境；接着在 P005 准备 SDK，P006 确定并下载 CMSIS，P010 解释工程与驱动模型，P014 再接入 HC32 DDL 和外部模块。工程怎样发现这些输入在后续 P011 展开，不是当前安装的前提。虚拟环境不会替你选择板卡，也不会自动下载清单中的源码。

基础 Python 依赖来自当前源码，下面截图仅用于定位，实际内容以当前 checkout 为准。

![requirements-base.txt 源码位置](assets/p002-requirements-base-source.png)

本章的实际产物是源码根内的 `.venv` 和能从新终端再次找到的主机命令。把最后一组恢复命令留好：后续每次进入同一源码根、激活这份环境，就可以继续工作，不必重新安装。此时 `python`、`west` 可运行仍不能证明 ARM 固件可生成，因为目标编译器还没有准备。

下一章 [P005 SDK 准备与编译器选型](P005_SDK准备与编译器选型.md) 沿同一 `hello_world + mps2/an386` 任务选 Windows 主机可运行的 ARM 工具链，并核对它的安装根。之后 P006 才处理源码依赖。


阅读导航：前一阶段：[P003_环境安装与源码准备_Linux](P003_环境安装与源码准备_Linux.md)、[P003_环境安装与源码准备_PowerShell](P003_环境安装与源码准备_PowerShell.md)、[P003_环境安装与源码准备_UCRT64](P003_环境安装与源码准备_UCRT64.md)；下一阶段：[P005_SDK准备与编译器选型](P005_SDK准备与编译器选型.md)。
