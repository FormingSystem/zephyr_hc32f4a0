<!--
SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 开发、构建与调试

以下命令在本仓库根目录执行。本仓库包含 Zephyr 和当前 HC32 所需模块的源码，
不需要初始化外部 west 工作区，也不从旁边的官方源码目录构建。

主线使用 UCRT64 Bash。首次安装、源码与工具选择见[工程环境](environment.md)，
west 初始化见[项目 west](west/README.md)，发布给他人的克隆步骤见[发布与重建](distribution.md)。
工具机制与独立实验见[learning](../learning/README.md)。

## 新机器准备

按环境文档安装工具后，在本仓库创建 Python 环境并登记 SDK：

```bash
read -r -p "请输入已安装的 SDK 目录: " SDK_DIR
py -3.12 scripts/setup_environment.py --sdk "$SDK_DIR"
source .venv/Scripts/activate
python scripts/configure_west.py
python scripts/project_env.py doctor
```

安装入口汇总构建和测试依赖；日常入口固定根目录 .venv 与本仓库源码，不回退到共享环境。
原 PowerShell 脚本保留兼容，不再是主线前提。

## 日常命令

```bash
source .venv/Scripts/activate
python scripts/project_env.py check
python scripts/project_env.py build
```

`check` 运行工程工具和 pyOCD 离线检查。`build` 直接调用 CMake/Ninja，默认目标是
**`uyup_rpi_a/hc32f4a0pitb`**，应用为 `samples/bringup`。结果位于：

| 产物 | 路径 |
| --- | --- |
| HC32 ELF / HEX / BIN | `build/bringup/zephyr/zephyr.elf`、`zephyr.hex`、`zephyr.bin` |
| 编译数据库 | `build/bringup/compile_commands.json` |
| 生成的设备树与配置 | `build/bringup/zephyr/zephyr.dts`、`.config` |

需要重新配置时执行 `python scripts/project_env.py build --pristine`。
HC32 构建成功后自动运行 `scripts/verify_hc32_image.py`，检查目标、向量表、ICG、
内存边界和编译源码来源；审计失败会使构建入口失败，也可单独执行该脚本复核现有产物。
首版 CPU 与总线使用 **板载 12 MHz XTAL 直驱**，所有总线 DIV1、Flash/SRAM 0 等待，不启用 PLL。
MRC 仅作为启动过渡；晶振稳定失败会停止启动。该固件的工作频率是 12 MHz，不能描述成 240 MHz 固件。

## QEMU 软件回归

```bash
python scripts/project_env.py build --board mps2/an386
python scripts/project_env.py test
```

显式 MPS2 构建保存到 `build/mps2`；test 通过本仓库 Twister 在 `mps2/an386` 上运行样例，
结果保存到 `build/twister`。QEMU 验证软件回归，不能替代 HC32 的时钟、UART、GPIO 或 Flash 实板验收。
不要将 MPS2 镜像下载到 HC32。

## 学习实验

课程应用通过独立入口选择，不向 project.py 添加不存在的应用参数：

```bash
python scripts/project_env.py exec python scripts/learning/run.py test --app tests/learning/c_lifetime --variant normal
python scripts/project_env.py exec python scripts/learning/run.py test --app tests/learning/first_evidence --variant normal
```

以上分别运行对象边界和基础断言实验，默认目标为 `mps2/an386`。
需要选择目标、附加配置或设置超时时，查[工具使用说明](../scripts/learning/README.md)。
各次结果保存在独立的 build/learning/runs 目录，终端的 Evidence 路径定位本次记录；原始日志不提交。
故障与恢复步骤、编译对象观察实验从[学习路线](learning/README.md)进入，首次阅读先看[开始学习](learning/开始学习.md)。

## VS Code 工作区

打开根目录的 `zephyr_hc32f4a0.code-workspace`：

```bash
code ./zephyr_hc32f4a0.code-workspace
```

资源管理器只有本仓库一个根目录，直接呈现完整 Zephyr 源码和 HC32 组件。
终端按需激活 .venv，工程任务自行配置环境；`Ctrl+Shift+B` 构建默认 HC32 目标。环境检查、工具检查、
QEMU 测试与 pyOCD 服务从“终端 → 运行任务”选择。

C/C++ 补全读取 `build/bringup/compile_commands.json`，首次使用前构建一次。
构建统一通过项目任务发起，避免 CMake 扩展另建一套配置。
工作区另有连接现有 pyOCD 服务的 Cortex-Debug 附加配置，不自动烧录。
插件安装、主机断点与 HC32 附加步骤见[VS Code 教程](../learning/vscode/P01_搭建编译与单步调试环境.md)。
Python 使用工程配置的虚拟环境；VS Code 已记住其他解释器时，通过“Python: Select Interpreter”切换。

## 调试器与实板操作

操作开发板前阅读 [hardware.md](hardware.md)。板载 CMSIS-DAP 出厂为 2.x/WinUSB，
支持 10 MHz SWD；USB2/DAP 一根线同时提供调试与串口。

```bash
python scripts/project_env.py exec pyocd list
python scripts/project_env.py debug
```

工程 debug 命令启动 GDB 服务，使用 `debug/pyocd.yaml` 的 `hc32f4a0xi`、10 MHz SWD、
SRAM 地址修正与禁止自动解锁擦除配置。GDB 服务启动本身不是下载或实板运行验收。
连接多个探针时使用 `--probe <唯一编号>`；编号按实际 `pyocd list` 结果填写。

外部探针需要更低 SWD 频率时：

```bash
python scripts/project_env.py debug --frequency 1000000
```

原生 pyOCD 的等价配置方式为：

```bash
python scripts/project_env.py exec pyocd gdbserver --project . --config debug/pyocd.yaml
```

`--project` 和 `--config` 放在子命令之后。若从其他目录调用，将两者指向本仓库根与配置文件。
内置 pyOCD 0.45.1 将主 SRAM 起点误写成 `0x1FFFE000`；本地钩子修正为
`0x1FFE0000..0x2005FFFF`。跳过工程配置就不会应用该修正。
机制参见官方[用户脚本](https://pyocd.io/docs/user_scripts.html#will_init_target)与
[配置说明](https://pyocd.io/docs/configuration.html)。

仅检查主机配置而不接触硬件：

```bash
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
