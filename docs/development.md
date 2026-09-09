<!--
SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 开发与验证

以下命令在仓库根目录执行。先加载工程环境：

```powershell
. ./scripts/Enter-Environment.ps1
python scripts/project.py doctor
```

入口使用外部 Zephyr 工作区、Python 虚拟环境与 SDK；具体参数以脚本帮助为准。
受版本控制的文件不保存某台机器的盘符或用户目录。
新机器的系统依赖参照 [Zephyr Getting Started Guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)。

## 基本工作循环

```powershell
python scripts/project.py check
python scripts/project.py build
python scripts/project.py test
```

`check` 检查工程与调试配置，`build` 构建本仓库 `samples/bringup`，`test` 运行已实现的验证。
目前默认板为 `mps2/an386`，对应 Cortex-M4 仿真平台；成功构建和运行只证明工程集成与主机工具可用。
尚不存在可用于 `west build -b` 的本工程 HC32 实板目标。

构建输出在 `build/bringup`，Twister 输出在 `build/twister`；均被 Git 忽略。
需要全新构建时使用 `python scripts/project.py build --pristine`。

直接运行调试器离线检查：

```powershell
python debug/verify_pyocd.py
```

它从临时无关目录创建真正的 pyOCD Session，以仓库根作为 project_dir，加载实际 YAML 和
相对用户脚本，验证初始化钩子前后的存储图。不会枚举、打开、连接或烧写硬件。

## 实板调试入口

板级操作先阅读 [hardware.md](hardware.md)。板载 DAP 默认 CMSIS-DAP 2.x/WinUSB、
10 MHz SWD；USB2/DAP 一根线同时提供调试与串口。先确认实际主机枚举：

```powershell
pyocd list
python scripts/project.py debug
```

工程 debug 入口使用 `debug/pyocd.yaml`，固定 2 MiB Flash 目标 `hc32f4a0xi`，加载 SRAM
地址修正并关闭自动解锁擦除。直接使用 pyOCD 的等价配置方式是：

```powershell
pyocd gdbserver --project . --config debug/pyocd.yaml
```

`--project` 与 `--config` 放在 `gdbserver` 子命令之后。在其他工作目录直接调用 pyOCD 时，
把 `--project` 指向仓库根，把 `--config` 指向该仓库的配置文件。
外部探针或接线条件需要更低频率时，可以显式覆盖为 1 MHz：

```powershell
python scripts/project.py debug --frequency 1000000
pyocd gdbserver --project . --config debug/pyocd.yaml -f 1000000
```

上述两条是工程入口与原生入口的等价写法，按需选择一条。连接多个探针时，工程入口支持
`--probe <唯一编号>`，编号由 `pyocd list` 读取。

pyOCD 0.45.1 原始目标把主 SRAM 起点写成 `0x1FFFE000`；本地钩子修正为
`0x1FFE0000`，长度 512 KiB。不要跳过配置而直接使用未修正的内置目标。
机制参见官方[用户脚本](https://pyocd.io/docs/user_scripts.html#will_init_target)与
[配置文档](https://pyocd.io/docs/configuration.html)。

使用外部 JLINK/STLINK 前，先执行用户确认的板载 DAP 停用步骤：关电、按住复位、开电、
松开复位，完整步骤两次，橙灯不闪表示停用。H2 不符合标准 ARM 10-pin 顺序，按硬件文档接线。

## 变更与结果记录

使用仓库提供的 Git 工作流；修改前检查本仓库状态，避免在外部 Zephyr 仓库提交工程文件。
本仓库源码、脚本、配置与文档一起评审；不提交 SDK、虚拟环境、PDF、构建输出或调试日志。
状态变化写入 [porting-status.md](porting-status.md)，写清目标、命令、结果及是否使用实板。

当前完整 Zephyr 提交合规依赖未全部安装；已知固定版本 reuse 下载曾遇到 Codeberg HTTP 429。
基础编译与测试依赖已经验证。提交前按实际改动补充相关检查，不把基础 smoke 通过写成完整合规通过。
