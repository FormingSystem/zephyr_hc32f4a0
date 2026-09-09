<!--
SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 开发、构建与调试

以下命令在本仓库根目录执行。本仓库包含 Zephyr 和当前 HC32 所需模块的源码，
不需要初始化外部 west 工作区，也不从旁边的官方源码目录构建。

## 新机器准备

先安装 Python 3.12、Git、CMake、Ninja、devicetree compiler、gperf，以及 Zephyr SDK 1.0.1
的 ARM 工具链。主机工具的安装方法见
[Zephyr Getting Started Guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)；
本工程已包含源码快照，不必重复执行文档中的源码下载流程。

在 PowerShell 中指定已经安装好的 SDK：

```powershell
$SdkRoot = Read-Host '请输入现有 Zephyr SDK 目录'
./scripts/Setup-Environment.ps1 -SdkRoot $SdkRoot
. ./scripts/Enter-Environment.ps1
python scripts/git_setup.py
python scripts/project.py doctor
```

Setup 在仓库内创建 `.venv`，安装 `requirements-tools.txt` 与
`scripts/requirements-base.txt`，保存本机 SDK 位置；不会把 SDK 或虚拟环境写入 Git。
现有机器可以加载已经配置的环境，日常不需要重复执行 Setup。主机工具可用性和依赖由 doctor 检查。

## 日常命令

```powershell
. ./scripts/Enter-Environment.ps1
python scripts/project.py check
python scripts/project.py build
```

`check` 运行工程工具和 pyOCD 离线检查。`build` 直接调用 CMake/Ninja，默认目标是
**`uyup_rpi_a/hc32f4a0pitb`**，应用为 `samples/bringup`。结果位于：

| 产物 | 路径 |
| --- | --- |
| HC32 ELF / HEX / BIN | `build/bringup/zephyr/zephyr.elf`、`zephyr.hex`、`zephyr.bin` |
| 编译数据库 | `build/bringup/compile_commands.json` |
| 生成的设备树与配置 | `build/bringup/zephyr/zephyr.dts`、`.config` |

需要重新配置时执行 `python scripts/project.py build --pristine`。
HC32 构建成功后自动运行 `scripts/verify_hc32_image.py`，检查目标、向量表、ICG、
内存边界和编译源码来源；审计失败会使构建入口失败，也可单独执行该脚本复核现有产物。
首版 CPU 与总线使用 **板载 12 MHz XTAL 直驱**，所有总线 DIV1、Flash/SRAM 0 等待，不启用 PLL。
MRC 仅作为启动过渡；晶振稳定失败会停止启动。该固件的工作频率是 12 MHz，不能描述成 240 MHz 固件。

## QEMU 软件回归

```powershell
python scripts/project.py build --board mps2/an386
python scripts/project.py test
```

显式 MPS2 构建保存到 `build/mps2`；test 通过本仓库 Twister 在 `mps2/an386` 上运行样例，
结果保存到 `build/twister`。QEMU 验证软件回归，不能替代 HC32 的时钟、UART、GPIO 或 Flash 实板验收。
不要将 MPS2 镜像下载到 HC32。

## VS Code 工作区

打开根目录的 `zephyr_hc32f4a0.code-workspace`：

```powershell
code ./zephyr_hc32f4a0.code-workspace
```

资源管理器只有本仓库一个根目录，直接呈现完整 Zephyr 源码和 HC32 组件。
新终端加载工程环境；`Ctrl+Shift+B` 构建默认 HC32 目标。环境检查、工具检查、
QEMU 测试与 pyOCD 服务从“终端 → 运行任务”选择。

C/C++ 补全读取 `build/bringup/compile_commands.json`，首次使用前构建一次。
构建统一通过项目任务发起，避免 CMake 扩展另建一套配置。
Python 使用工程配置的虚拟环境；VS Code 已记住其他解释器时，通过“Python: Select Interpreter”切换。

## 调试器与实板操作

操作开发板前阅读 [hardware.md](hardware.md)。板载 CMSIS-DAP 出厂为 2.x/WinUSB，
支持 10 MHz SWD；USB2/DAP 一根线同时提供调试与串口。

```powershell
pyocd list
python scripts/project.py debug
```

工程 debug 命令启动 GDB 服务，使用 `debug/pyocd.yaml` 的 `hc32f4a0xi`、10 MHz SWD、
SRAM 地址修正与禁止自动解锁擦除配置。GDB 服务启动本身不是下载或实板运行验收。
连接多个探针时使用 `--probe <唯一编号>`；编号按实际 `pyocd list` 结果填写。

外部探针需要更低 SWD 频率时：

```powershell
python scripts/project.py debug --frequency 1000000
```

原生 pyOCD 的等价配置方式为：

```powershell
pyocd gdbserver --project . --config debug/pyocd.yaml
```

`--project` 和 `--config` 放在子命令之后。若从其他目录调用，将两者指向本仓库根与配置文件。
内置 pyOCD 0.45.1 将主 SRAM 起点误写成 `0x1FFFE000`；本地钩子修正为
`0x1FFE0000..0x2005FFFF`。跳过工程配置就不会应用该修正。
机制参见官方[用户脚本](https://pyocd.io/docs/user_scripts.html#will_init_target)与
[配置说明](https://pyocd.io/docs/configuration.html)。

仅检查主机配置而不接触硬件：

```powershell
python debug/verify_pyocd.py
```

使用外部 JLINK/STLINK 前先停用板载 DAP：关电、按住复位、开电、松开复位，
完整步骤两次，橙灯不闪表示停用。H2 不是标准 ARM 10-pin 接线顺序，按硬件文档信号名连接。

## 记录与提交

所有源码、适配、脚本和项目文档都在本仓库评审与提交。SDK、`.venv`、`.local`、`build`、
调试日志及原始资料 PDF 不提交。导入源码保留原许可证与来源记录，更新基线时先检查本地差异。
实际完成的构建、软件测试与硬件操作分别写入 [porting-status.md](porting-status.md)。

完整 Zephyr 上游合规检查尚未完成；固定版本 reuse 下载曾遇到 Codeberg HTTP 429。
项目 check 与基础构建通过不能替代全部上游合规检查。
