---
id: learning.zephyr-docs.qemu-other-reference.page-5
title: QEMU_Hexagon仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/hexagon/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_QEMU\_Hexagon仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/hexagon/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

## 5.1\_开发板概况与概述

<a id="qemu_hexagon"></a>

名称：`qemu_hexagon`。厂商：[QEMU，通用开源机器仿真器与虚拟化器](https://docs.zephyrproject.org/latest/boards/index.html#vendor=qemu)。状态：持续维护（Maintained）。架构（Architecture）：[hexagon](https://docs.zephyrproject.org/latest/boards/index.html#arch=hexagon)；片上系统（System on Chip，SoC）：[qemu_hexagon_virt](https://docs.zephyrproject.org/latest/boards/index.html#soc=qemu_hexagon_virt)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/hexagon)。

<a id="overview"></a>

此配置使用 QEMU 仿真 Qualcomm Hexagon 数字信号处理器（Digital Signal Processor，DSP）虚拟平台。Hexagon DSP 是 Qualcomm 设计的超长指令字（Very Long Instruction Word，VLIW）数字信号处理器，存在于 Snapdragon 片上系统中。本配置提供基于 QEMU 的环境，用于开发和测试面向 Hexagon 架构的 Zephyr 应用。

Hexagon 上的 Zephyr 作为客户机（Guest）运行于 Hexagon VM 虚拟机监控器（Hypervisor）之下。**`zephyr.elf` 二进制不能直接启动，必须通过 HVM 的 `loadlinux` 引导加载器（Boot Loader）加载**。

支持以下设备：HVM 可编程中断控制器（Programmable Interrupt Controller，PIC）、HVM 定时器，以及作为控制台（Console）的 PL011 UART。

<a id="hardware"></a>

## 5.2\_硬件

<a id="supported-features"></a>

<a id="qemu_hexagon-hw-features"></a>

官方在此提供 `qemu_hexagon` 的硬件特性（Supported Features）及图例。片上（on-chip）表示特性集成在 SoC 内，板上（on-board）表示位于开发板。启用／禁用数字是相应状态的实例数量，数字链接跳转到开发板或 SoC 设备树源码（DTS）中该状态的第一个实例；兼容字符串（Compatible String，如 `vnd,foo`）链接跳转到绑定文档。

RAM 为随机存取存储器，Flash 为闪存，SRAM 为静态随机存取存储器；KiB、MiB 分别为二进制千字节、兆字节。CPU 为中央处理器，UART 为通用异步收发器。

原页没有列出具体构建目标及硬件特性表行，译文保留这一状态。

<a id="devices"></a>

<a id="system-clock"></a>

### 5.2.1\_设备与系统时钟

此配置使用 1 MHz 系统时钟频率。

<a id="known-problems-or-limitations"></a>

已知问题与限制（Known Problems or Limitations）：部分覆盖 `CONFIG_USERSPACE` 用户空间代码路径的测试，可能导致客户虚拟机在运行时崩溃。

<a id="getting-started"></a>

## 5.3\_开始使用

本节说明为 QEMU Hexagon 开发板构建和运行 Zephyr 所需的工具及依赖。

<a id="prerequisites"></a>

### 5.3.1\_前提条件

需要以下工具：

- west 构建工具及 Zephyr Python 依赖，见步骤5。
- Hexagon LLVM/Clang 交叉编译器（Cross-compiler），见下文。
- 支持 Hexagon 的 QEMU，见下文。
- Hexagon 虚拟机监控器的 `loadlinux` 引导加载器，见下文。

> 译注：以下是官方 Linux shell 操作示例，`$` 是提示符；`/opt/hexagon-toolchain`、`/opt/hexagon-sdk` 是官方示例安装目录，不是本仓库路径。阅读时应以实际安装目录设置环境变量，代码原文保留用于对照。

<a id="step-1-install-the-hexagon-llvm-toolchain"></a>

### 5.3.2\_步骤1：安装Hexagon LLVM工具链

从 [toolchain_for_hexagon 发行页面](https://github.com/quic/toolchain_for_hexagon/releases/tag/v22.1.4_)下载预编译的 Hexagon LLVM 交叉编译器。对于 Ubuntu 22.04 及以后版本的 x86_64 宿主机，推荐使用的发行文件是：

```text
clang+llvm-22.1.4-cross-hexagon-unknown-linux-musl.tar.zst
```

下载并解压到自行选择的目录，例如 `/opt/hexagon-toolchain`：

```shell
$ wget https://artifacts.codelinaro.org/artifactory/codelinaro-toolchain-for-hexagon/22.1.4_/clang+llvm-22.1.4-cross-hexagon-unknown-linux-musl.tar.zst
$ mkdir -p /opt/hexagon-toolchain
$ tar -xf clang+llvm-22.1.4-cross-hexagon-unknown-linux-musl.tar.zst \
      -C /opt/hexagon-toolchain --strip-components=2
```

> 原文注意：压缩包顶层包含 `x86_64-linux-gnu/` 子目录。`--strip-components=2` 同时去掉归档名称前缀和该子目录，使 `bin/clang` 直接位于安装目录之下。

选择 `hexagon` 工具链变体（Toolchain Variant），并让 `HEXAGON_TOOLCHAIN_PATH` 指向解压目录：

```shell
$ export ZEPHYR_TOOLCHAIN_VARIANT=hexagon
$ export HEXAGON_TOOLCHAIN_PATH=/opt/hexagon-toolchain
```

关于 `hexagon` 工具链变体，详见 [Qualcomm Hexagon LLVM 工具链](../toolchains/P014_Hexagon_LLVM工具链.md#toolchain-hexagon)。

<a id="step-2-qemu-with-hexagon-support"></a>

### 5.3.3\_步骤2：支持Hexagon的QEMU

标准 QEMU 发行版不包含 Hexagon 系统仿真（System Emulation）。步骤1安装的工具链在其 `bin` 目录中附带 `qemu-system-hexagon`；构建系统会先到该处查找，所以 `west build -t run` 或 Twister 测试运行器无需额外配置。

若要使用其他 QEMU，可从 Qualcomm 分支仓库（Fork）构建：

```shell
$ git clone https://github.com/qualcomm/qemu.git -b hexagon-sysemu-22-may-2026 qemu-hexagon
$ cd qemu-hexagon
$ mkdir build && cd build
$ ../configure --target-list=hexagon-softmmu --disable-werror
$ make -j$(nproc)
```

生成的二进制文件是当前所在 `build` 目录中的 `qemu-system-hexagon`。将 `QEMU_BIN_PATH` 指向该目录，即可优先选择它而不是工具链附带的版本：

```shell
$ export QEMU_BIN_PATH="$PWD"
```

<a id="step-3-install-the-hexagon-sdk"></a>

### 5.3.4\_步骤3：安装Hexagon SDK

`loadlinux` 引导加载器需要 Hexagon 软件开发工具包（SDK），其中提供 `hexagon-clang` 及相关工具。下载并解压 SDK 归档：

```shell
$ curl -LO https://github.com/snapdragon-toolchain/hexagon-sdk/releases/download/v6.4.0.2/hexagon-sdk-v6.4.0.2-amd64-lnx.tar.xz
$ tar -xf hexagon-sdk-v6.4.0.2-amd64-lnx.tar.xz -C /opt/hexagon-sdk
$ export HEXAGON_SDK_ROOT=/opt/hexagon-sdk/6.4.0.2
$ export HEXAGON_TOOLS_ROOT=$HEXAGON_SDK_ROOT/tools/HEXAGON_Tools/19.0.04
$ export PATH=$HEXAGON_TOOLS_ROOT/Tools/bin:$PATH
```

验证 SDK 工具链可以访问：

```shell
$ hexagon-clang --version
```

<a id="step-4-build-the-hexagon-hypervisor-boot-loader"></a>

### 5.3.5\_步骤4：构建Hexagon虚拟机监控器引导加载器

Zephyr 必须作为客户机运行于 Hexagon VM（H2）虚拟机监控器之下。监控器仓库中的 `loadlinux` 二进制用作 QEMU 的 `-bios` 参数；它随后加载并启动 Zephyr ELF 可执行文件。

克隆监控器仓库并检出所需标签（Tag）。直接克隆到 `$ZEPHYR_BASE` 中，可以让 Zephyr 构建系统自动找到 `loadlinux`：

```shell
$ git clone https://github.com/androm3da/hexagon-hypervisor.git \
      $ZEPHYR_BASE/hexagon-hypervisor
$ cd $ZEPHYR_BASE/hexagon-hypervisor
$ git checkout h2-bcain-1-june-2026
```

先构建 H2 监控器库。`NULL_ANGEL_TRAP=1` 禁用 angel 半主机处理程序（Semihosting Handler）；否则，该程序会使 QEMU `virt` 机器无提示地挂起：

```shell
$ ARCHV=73
$ make USE_PKW=0 ARCHV=$ARCHV TARGET=opt NULL_ANGEL_TRAP=1 -j$(nproc)
```

然后从 `linux/` 子目录构建 `loadlinux`。Makefile 默认采用 `../install` 和 `../kernel` 作为构建路径，但上一步的产物位于 `artifacts/v${ARCHV}/opt/`，因此调用 `make` 前应导出正确路径：

```shell
$ export INSTALLPATH=$(pwd)/artifacts/v${ARCHV}/opt/install
$ export KERNELPATH=$(pwd)/artifacts/v${ARCHV}/opt/build/kernel
$ make -C linux USE_PKW=0 ARCHV=$ARCHV NO_LOAD=1 \
      NULL_ANGEL_TRAP=1 LINUX_LINK_ADDR=0xa0000000 loadlinux
```

生成的 `linux/loadlinux` 通过 `-bios` 标志传给 QEMU。Zephyr 构建系统默认在 `$ZEPHYR_BASE/hexagon-hypervisor/linux/loadlinux` 查找它。可通过设置 `HEXAGON_H2_LOADLINUX` 环境变量，或向 CMake 传入 `-DHEXAGON_H2_LOADLINUX=<path>` 来覆盖该路径。

<a id="step-5-set-up-the-zephyr-environment"></a>

### 5.3.6\_步骤5：配置Zephyr环境

按照标准[入门指南](../getting_started/P002_入门指南.md#getting-started)安装 Zephyr 依赖并初始化工作区。

创建 Python 3.12 虚拟环境（Virtual Environment），将 west 和 Zephyr 的 Python 依赖安装到其中，然后激活：

```shell
$ python3.12 -m venv ~/zephyr-venv
$ ~/zephyr-venv/bin/pip install west
$ ~/zephyr-venv/bin/pip install -r $ZEPHYR_BASE/scripts/requirements.txt
$ source ~/zephyr-venv/bin/activate
```

在当前 shell 中加载 Zephyr 环境脚本：

```shell
$ source $ZEPHYR_BASE/zephyr-env.sh
```

<a id="programming-and-debugging"></a>

## 5.4\_编程与调试

原页在此列出 `qemu_hexagon` 支持的运行器及关联 west 命令，但表格只有列标题，表体为空：

| 运行器 | `west flash` | `west debug` |
| --- | --- | --- |

<a id="building"></a>

### 5.4.1\_构建

为此开发板构建 Zephyr 应用。必须显式指定工具链，因为 Hexagon 使用 LLVM 交叉编译器构建，而不是使用 Zephyr SDK。以下命令在 Zephyr 仓库根目录执行，原代码注释也表示这一位置：

```shell
# From the root of the zephyr repository
west build -b qemu_hexagon/qemu_hexagon_virt samples/hello_world -- -DZEPHYR_TOOLCHAIN_VARIANT=hexagon -DHEXAGON_TOOLCHAIN_PATH=/opt/hexagon-toolchain
```

> 原文注意：将 `/opt/hexagon-toolchain` 替换为步骤1设置的 `$HEXAGON_TOOLCHAIN_PATH` 实际值。如果已导出步骤1中的环境变量，则这两个参数都可以省略。

构建生成的 `zephyr.elf` 同时用于调试，以及由虚拟机监控器在运行时加载。

<a id="running"></a>

### 5.4.2\_运行

如果 `loadlinux` 位于默认路径，可执行：

```shell
$ west build -t run
```

手动运行时，显式传入 QEMU 二进制和 `loadlinux` 引导加载器的路径：

```shell
$ qemu-system-hexagon \
    -machine virt -nographic -m 4G \
    -bios path/to/hexagon-hypervisor/linux/loadlinux \
    -device loader,file=build/zephyr/zephyr.elf
```

将 `path/to/hexagon-hypervisor/linux/loadlinux` 替换为实际 `loadlinux` 二进制路径。原文称该文件在“步骤3”取得。

> 译注：上文步骤3安装的是 SDK，实际构建 `loadlinux` 的是步骤4；这里保留原文的步骤指向并指出差异。

按 `CTRL+A`，再按 `x` 退出 QEMU。`samples/hello_world` 的预期输出为：

```text
*** Booting Zephyr OS build v4.x.x ***
Hello World! qemu_hexagon/qemu_hexagon_virt
```

<a id="debugging"></a>

### 5.4.3\_调试

详细概述参见[应用调试](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

QEMU 支持通过 GDB 远程串行协议（GDB Remote Serial Protocol）进行远程调试。以 `-s -S` 标志启动 QEMU，使执行暂停，并在端口1234等待调试器连接：

```shell
$ qemu-system-hexagon \
    -machine virt -nographic -m 4G \
    -bios path/to/hexagon-hypervisor/linux/loadlinux \
    -device loader,file=build/zephyr/zephyr.elf \
    -s -S
```

使用 LLDB 调试器连接目标。GDB 不支持 Hexagon 指令集架构（ISA）：

```shell
$ lldb build/zephyr/zephyr.elf
(lldb) gdb-remote 1234
(lldb) b main
(lldb) continue
```

<a id="references"></a>

## 5.5\_参考资料

- [Qualcomm Hexagon V67 程序员参考手册（Programmer’s Reference Manual）](https://docs.qualcomm.com/bundle/publicresource/80-N2040-59_AA_Qualcomm_Hexagon_V67_Programmers_Reference_Manual.pdf)。
- [Hexagon 工具链发行版（LLVM Cross-compiler）](https://github.com/quic/toolchain_for_hexagon/releases)。
- [QEMU Hexagon 源码，hexagon-sysemu-22-may-2026 分支](https://github.com/qualcomm/qemu/tree/hexagon-sysemu-22-may-2026)。
- [Hexagon 虚拟机监控器（Hypervisor）](https://github.com/qualcomm/hexagon-hypervisor)。

> 译注：命令、输出和历史版本号按官方原文保留；本次翻译未运行固件，也未安装工具链。

---

[上一章](P004_QEMU_Renesas_RX仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P006_QEMU_Infineon_AURIX_TC39x与TC4Dx仿真开发板.md)
