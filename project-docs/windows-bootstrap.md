<!-- SPDX-License-Identifier: Apache-2.0 -->

# Windows 一键准备与教学环境恢复

入口位于工程根目录 `setup-windows.cmd`，适用于 Windows 10/11 x64、Windows PowerShell 5.1 或更新版本。
先下载本仓库并解压/克隆到你选择的工程目录，再运行入口。脚本使用自身所在的仓库，与你从哪个终端目录调用无关。
Linux 不使用此安装器。逐步手工安装仍见[环境说明](environment.md)。

## 第一次安装

在工程根目录打开 PowerShell 或 CMD，执行同一条命令：

```powershell
.\setup-windows.cmd
```

开头选择中文或 English，随后选择 MSYS2、其他工具目录、可复用的 Windows Python、环境变量作用域和镜像区域。
默认示例为作者的 `E:\Msys2`；其他工具默认放在同盘 `zephyr-tools`，**没有 E 盘时必须换成实际存在的盘符**。
工具路径采用短 ASCII 路径，不含空格、中文、网络路径、链接或盘符根目录，减少 MSYS2/SDK 工具的路径兼容问题。
源码工程可在其他盘，工具不能安装到源码仓库里面。确认列出的目录后按 Enter 开始，输入 `q` 退出。

默认目录结构如下；盘符、MSYS2 目录、工具目录都可改：

```text
E:\Msys2\                         Bash、pacman、UCRT64 工具和包缓存
E:\zephyr-tools\git\              原生 Windows MinGit
E:\zephyr-tools\python312\        官方 Windows Python（也可选择已有解释器）
E:\zephyr-tools\sdk\               SDK 及 ARM 工具链
E:\zephyr-tools\downloads\         下载文件、pip 缓存、安装进程 TEMP/TMP
E:\zephyr-tools\bin\               hc32-shell.cmd 启动器
工程\.venv\                       项目 Python 包
工程\.local\windows\              安装计划、日志、配置清单和环境变量恢复记录
```

工具、缓存和完整快照需要自行预留空间，建议工具所在盘至少空余 10 GiB；完整备份另需约一份 MSYS2 的容量。
目录选择控制主要工具与下载占用；Windows Installer 自己维护的系统缓存/登记仍可能写入系统盘，不能承诺 C 盘零写入。
脚本不改变系统范围的 TEMP/TMP，也不修改全局 pip 配置。

已有同版本 Python 的机器默认从注册表找到并复用它，也可输入其他官方解释器的 `python.exe` 完整路径。
安装前计划会显示实际选择，不把复用的已有安装移动到新工具目录。官方 Python 安装器会识别注册过的版本并进入维护模式，
因此脚本发现已注册 Python 时会停止新装，避免把另选目录误报为安装成功。工程已有 `.venv` 会复用并校验；
如果基础 Python 已删除导致 `.venv` 无法启动，先保留/移走旧 `.venv`，再重新安装，不在损坏环境上继续。

只看计划、不下载、不写环境变量：

```powershell
.\setup-windows.cmd -Action Plan -Language zh -NonInteractive
```

无人值守示例（运行前把目录改成自己的选择）：

```powershell
.\setup-windows.cmd -Language zh -MsysRoot E:\Msys2 -ToolsRoot E:\zephyr-tools -Mirror China -EnvironmentScope User -NonInteractive
```

`-DownloadRoot` 可单独指定下载与临时文件目录；`-SdkRoot` 指定放置 `zephyr-sdk-版本号` 的父目录。
`-PythonExe` 选择已有官方 Windows Python 3.12+。脚本读取工程 `dependencies.lock.json`，当前新装 Python 3.12.10、SDK 1.0.1。
参数路径不支持与其他工具子目录相互嵌套。

## 安装完成后的入口

打开新的终端，执行：

```powershell
hc32-shell
hc32-shell -Shell PowerShell
hc32-shell -Shell CMD
```

三条命令分别进入工程的 UCRT64 Bash、PowerShell、CMD。默认使用 Bash，符合本仓库教学命令主线。
如果终端还没有刷新 PATH，直接从工程根运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\windows\start.ps1
```

启动器只在子终端设置工程 `.venv`、`ZEPHYR_BASE`、SDK 和工具优先级。Bash 启动器读取登录配置后重新选定 Python/MinGit，
最终交互 shell 不读取 `.bashrc`，防止用户旧配置再次覆盖解释器。个人别名可进入后手工 `source ~/.bashrc`，随后复核工具路径。

在该终端中可执行：

```bash
python scripts/project_env.py doctor
python scripts/project_env.py check
python scripts/project_env.py build
python scripts/project_env.py test
```

自动安装阶段执行 `doctor` 和 `pip check`，不烧录、不连接探针，也不自动运行最后三条工程验收命令。
构建、QEMU 与实板结果分别记录，不能用安装成功代替固件或硬件验证。

## 安装器具体准备什么

MSYS2 使用官方**带日期的稳定发行版**，避免 GitHub `latest` 偶尔指向 nightly。下载采用 GitHub 发布资产的 SHA-256，
国内镜像下载的安装器也必须符合该摘要。MinGit、SDK 同样校验发布资产摘要；官方 Python 安装器校验有效的 PSF Authenticode 签名。
缺少摘要、摘要不匹配或签名失败都会停止，不降级为不校验安装。

MSYS2 先更新核心，再重开 Bash 执行完整升级和依赖安装，处理运行时更新关闭 shell 的情况；最终升级失败则退出。
安装前需关闭目标 MSYS2 的终端/工具，不会杀进程或擅自删除 `db.lck`。已存在的可用工具可以复用，不自动卸载旧环境。

| 工具层 | 安装内容 |
| --- | --- |
| MSYS 基础工具 | base-devel、Git、OpenSSH、curl、wget、zip/unzip、rsync |
| UCRT64 主机工具 | GCC、GDB、CMake、Ninja、dtc、gperf、7-Zip |
| Windows 原生工具 | MinGit、官方 Python；避免 MinGW Python 与 PyPI 二进制 wheel 不兼容 |
| Zephyr SDK | 锁定版本的 minimal 包 + `arm-zephyr-eabi`；Windows minimal 包已附带 QEMU/OpenOCD |
| 项目 Python | 调用现有 `scripts/setup_environment.py`，安装 requirements-dev.txt 到根 `.venv` |
| 项目配置 | 调用 configure_west.py，登记 SDK、主机工具目录和编辑器解释器，再运行 doctor |

SDK 1.0.1 的 Windows minimal 包实际含 QEMU，`setup.cmd /h` 跳过的是额外安装；此入口校验自带 QEMU，显式路径选择 SDK，
无需把 SDK 注册到全局 CMake 包表。镜像与 MSYS2 包、MinGit、Python 传递依赖仍可能随时间变化；安装记录保存下载资产信息，
完整 MSYS2 快照用于恢复原包版本，包名清单只能重建当时镜像提供的版本。

## 镜像如何选择

当前作者源配置为清华 TUNA 优先、中科大 USTC 备用；公共默认配置沿用此顺序，并保留官方回退源。
`Auto` 根据所选语言、Windows 区域判断：中文或中国区域优先国内源，否则使用官方 `mirror.msys2.org` 就近重定向。
这不是 IP 国家定位；旅行、代理或其他国家的用户应手动选择 `Global`。不通过第三方定位服务收集 IP。

`China` 修改 `mirrorlist.msys` 与 `mirrorlist.mingw`，MSYS 仓库保留 `$arch`，UCRT64 等 MinGW 仓库保留 `$repo`；
修改前备份原文件，保留 pacman 签名校验。软件包下载由 pacman 按列表回退。
pip 在本次安装进程中使用 TUNA，`Global` 使用 PyPI；pip 镜像访问失败时退出，可改 `-Mirror Global` 重试。
GitHub/PSF 资产始终使用官方 HTTPS 下载，不自动替换成未知代理站。

## 环境变量与回退

`User` 为默认，写当前用户注册表；`Machine` 写系统注册表，需要主动在管理员 PowerShell 运行；
`Process` 不留下持久环境变量，通过工程启动脚本进入即可。无需把 PowerShell 执行策略永久改为 Unrestricted。

持久 PATH 追加启动器、原生 Git、选定 Python 和 Scripts、UCRT64 bin，不加入 MSYS `/usr/bin`。
全局变量为 `MSYS2_ROOT`、`HC32_ENV_HOME`、`ZEPHYR_SDK_INSTALL_DIR`、`ZEPHYR_TOOLCHAIN_VARIANT`。
`ZEPHYR_BASE`、项目 `.venv`、临时文件位置在启动器进程内设置。已有系统 PATH 的优先级可能高于用户 PATH，
因此开发和验收使用工程启动器/`project_env.py`，它们选定本机配置中的工具路径。

每次写环境变量**之前**生成独立的 `environment-journal.json`，记录原值、新值、作用域和注册表类型；
不使用有截断风险的 `setx PATH`。通知 Windows 环境已改变后仍需重开终端。
撤销某次安装的环境变量改动：

```powershell
.\setup-windows.cmd -Action RestoreEnvironment -Language zh -Journal .local\windows\runs\实际运行目录\environment-journal.json
```

PATH 没有变化时恢复原值；后来追加了其他项目路径时，只移除本次新增项。
其他变量如果已被后来修改则保留并提示冲突，不覆盖其他工作。多次安装应按时间从新到旧回退；
它不卸载工具、不删除文件、不回退 pacman 更新，也不回退 `.local/environment.json` 等项目配置。

## 一键卸载 MSYS2

本指令针对教学前清理 MSYS2：卸载指定目录及其中的 UCRT64 工具、home 文件和包缓存，保留工程、外部 Python、
Git、SDK、下载缓存及备份。它不把整台 Windows 的开发软件全部卸载。

先查看准确范围（不创建备份、不卸载、不写环境变量）：

```powershell
.\setup-windows.cmd -Action Uninstall -Language zh -MsysRoot E:\Msys2 -Snapshot F:\msys2-before-class -WhatIf
```

关闭该 MSYS2 的所有终端和后台工具，在工程根目录的 PowerShell/CMD 执行：

```powershell
.\setup-windows.cmd -Action Uninstall -Language zh -MsysRoot E:\Msys2 -Snapshot F:\msys2-before-class -Yes
```

脚本先创建完整快照并验证 SHA-256，再调用该目录的官方卸载器，成功后清除残留目录；没有卸载器的解压版按文件目录卸载。
已有 `snapshot.json` 时只接受同一路径的完整、摘要正确的快照，恢复只能回到该快照的时间点。
要保留最新数据，请给一个新的备份目录；省略 `-Snapshot` 会在工程 `.local/windows/backups/` 创建带时间戳的新备份。
配置清单不能作为卸载备份，备份失败不会开始卸载。

不加 `-Yes` 时会要求输入 `UNINSTALL`；无人值守可同时加 `-NonInteractive -Yes`。
`-WhatIf`、`-Yes` 仅适用于 Uninstall，安装预览仍用 `-Action Plan`。
默认检查用户和系统环境变量，仅清理指向当前 MSYS2 目录的 PATH 项和路径变量；其他 MSYS2 实例、同名前缀目录、
外部 Python/SDK 以及无路径归属的 `MSYSTEM` 等变量保持原值。能解析 `%MSYS2_ROOT%` 形式的 PATH，保留无关项的原始写法。
如果需要修改系统环境变量，脚本在卸载前要求管理员 PowerShell；也可用 `-EnvironmentScope User` 明确只处理用户范围。

卸载记录和环境变量回退记录写入 `.local/windows/runs/uninstall-时间/`。
官方卸载器报错、目录仍有进程、发现目录联接/符号链接、目标包含工程/备份或快照校验失败时停止，不自动杀进程，
也不在官方卸载失败后强行递归删除。若中途失败，记录中的 status 表示最后尝试的阶段，不代表已完成。
`environment-User.json` / `environment-Machine.json` 可传给 `-Action RestoreEnvironment -Journal` 撤销本脚本的环境清理；
实际文件按下一节的完整快照恢复。环境记录只在该作用域存在清理项时生成。

卸载逻辑已用工程 build 目录下的小型临时目录验证删除、备份恢复、环境回退及模拟官方卸载器失败；
没有对作者当前 MSYS2 执行真实卸载，官方卸载器的真实执行仍待用户实际卸载时验收。

## 教学前备份，教学后恢复

**在卸载前先完成完整备份**。关闭 E 盘 MSYS2 的终端、编辑器后台任务和工具，保留 Windows PowerShell/CMD，执行：

```powershell
.\setup-windows.cmd -Action Backup -Language zh -MsysRoot E:\Msys2 -Snapshot F:\msys2-before-class
```

备份目标必须为空且在 MSYS2 目录外。脚本保存完整 `msys2.tar`，包括工具、home、pacman 数据库和缓存，计算 SHA-256，
另存源配置、安装包清单及相关用户/系统环境变量参考。tar 不压缩，节省备份/恢复 CPU 时间；需要足够磁盘空间。
完整快照可能含 home 下的密钥和私人文件，保持本机私有，不提交 Git、不分发给读者。

只导出小体积配置清单可加 `-ConfigurationOnly`；**这种清单不能代替完整快照**。
本轮已在 `.local/windows/backups/` 导出作者配置清单，没有在仍运行的 MSYS2 上创建完整快照。

教学结束，先把教学用 MSYS2 正常卸载或自行移走，确保快照中的**原始路径为空**，再执行：

```powershell
.\setup-windows.cmd -Action Restore -Language zh -Snapshot F:\msys2-before-class
```

恢复前检查快照摘要，任何目标非空都拒绝覆盖；按原路径恢复，避免移动 MSYS2 导致绝对路径失效。
若教学安装改过环境变量，先按上一节回退相应 journal，或在 Restore 同时传 `-Journal`。
恢复默认补回快照中属于 MSYS2 的用户 PATH 项及缺失的 MSYS/MINGW 变量，不覆盖后来修改的变量，也不恢复无关工具的 PATH。
原来设置在系统范围的变量，可在管理员 PowerShell 加 `-EnvironmentScope Machine` 恢复；`Process` 跳过持久环境变量恢复。
文件已恢复后，只补回系统环境变量可运行 `setup-windows.cmd -Action RestoreEnvironment -Snapshot F:\msys2-before-class -EnvironmentScope Machine -Language zh`。
快照中的 `environment-reference.json` 另保留 Zephyr/Python 相关变量供核对，不全量覆盖当前注册表。
Windows 开始菜单快捷方式和卸载登记不在文件快照内，恢复后可以直接运行 `E:\Msys2\ucrt64.exe`。

备份范围是 MSYS2，**不是整机镜像**：仓库源码、项目 `.venv`、外部 Python/SDK、编辑器及父目录 `.west` 不在 tar 中。
教学要替换这些内容时，应分别保留 `.local/environment.json`、`.vscode/settings.json` 和 `.west/config`，
并保留原 Python/SDK 安装目录。恢复后重新用原 SDK 执行 setup_environment.py 并运行 doctor。
仓库文件快照和教学机器/虚拟机快照可用于更大范围恢复。

## 失败重试与实测边界

安装日志、每步下载资产信息和原镜像配置位于 `.local/windows/runs/`；下载文件保留在选定目录，可校验后复用。
网络失败不会继续后面的安装步骤；修复网络或更换镜像后用原参数重跑。已有 SDK 编译器和 Git 会复用。
若安装器/解压中断留下无法识别的非空目录，脚本拒绝覆盖；先检查并保留该目录，再选择空目录重试。
不会为继续安装而关闭 TLS 校验、禁用包签名、覆盖非空恢复目录或忽略失败退出码。

离线回归入口：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\windows\test-bootstrap.ps1
```

覆盖路径拒绝、镜像模板、环境变量恢复、子进程参数及非零返回码、真实 tar 小型快照的还原/损坏拒绝。
产物位于工程 `build/windows-bootstrap-tests/`，不写系统 PATH，也不安装工具。
加入卸载后 53 项离线检查通过；前一轮 51 项工程工具测试、已有环境 doctor/check 和本次相关文档检查通过；
另实际完成 MinGit、SDK minimal 与 ARM 包的下载、摘要校验、解压、GCC/QEMU 版本检查。
这些验证不等于干净 Windows 完整安装验收；本轮未卸载作者的 MSYS2，完整联网新装和实板尚待单独验收。

依据：[MSYS2 安装](https://www.msys2.org/docs/installer/)、[完整更新](https://www.msys2.org/docs/updating/)、
[镜像](https://www.msys2.org/docs/mirrors/)、[Python 二进制差异](https://www.msys2.org/docs/python/)，
以及仓库锁文件、现有 SDK setup.cmd 和[Zephyr SDK 发布页](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v1.0.1)。
