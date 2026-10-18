---
id: learning.zephyr-docs.boards-cdac-to-cthings.page-4
title: Xtensa simulator
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/cdns/xt-sim/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="xt-sim"></a>

# 第4章\_Xtensa仿真器（Simulator）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/cdns/xt-sim/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/xt-sim.jpg](images/xt-sim.jpg)](images/xt-sim.jpg)

Xtensa仿真器（Simulator）

名称（Name）：

`xt-sim`

厂商（Vendor）：

[Cadence Design Systems Inc.公司](https://docs.zephyrproject.org/latest/boards/index.html#vendor=cdns)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[xtensa](https://docs.zephyrproject.org/latest/boards/index.html#arch=xtensa)

片上系统（SoC）：

[xtensa_sample_controller](https://docs.zephyrproject.org/latest/boards/index.html#soc=xtensa_sample_controller)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/cdns/xt-sim/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

Xtensa处理器架构是一种可配置、可扩展、可综合（Synthesizable）的32位精简指令集（RISC）处理器内核。处理器及SoC厂商可以选择不同的处理器选项，甚至在基础指令集架构（ISA）之上创建自定义指令，从而使处理器适应特定应用。

更多信息见[https://ip.cadence.com/ipportfolio/tensilica-ip/xtensa-customizable](https://ip.cadence.com/ipportfolio/tensilica-ip/xtensa-customizable)。

<a id="hardware"></a>

## 硬件（Hardware）

官方支持以下Xtensa内核：


- sample_controller

<a id="system-clock"></a>

### 系统时钟（System Clock）

Xtensa内核可配置为使用内部或外部定时器。仿真时的时钟频率设为25 MHz。

<a id="system-requirements"></a>

## 系统要求（System Requirements）

<a id="prerequisites"></a>

### 前置条件（Prerequisites）

Xtensa开发需要Linux主机系统。原文推荐Debian 9.x（Stretch）或较新的Ubuntu发行版，并启用多库（Multilib）支持。

官方仅支持RF-2016.4-linux及更新版本的Xtensa工具。其他版本可能可用，但不在Cadence Systems Inc.支持范围内。

为了设置Zephyr OS构建系统，Linux构建主机必须安装32位GCC编译器。如有需要，可通过下载Zephyr SDK或使用发行版包管理器安装GCC。

在Debian／Ubuntu系统上，可按以下方式安装`gcc-multilib`软件包：

```text
#aptitude install gcc-multilib # Or what ever package manager (apt, apt-get, ...)
```

<a id="set-up-build-environment"></a>

### 设置构建环境（Set Up Build Environment）

原文建议创建`~/.zephyrrc`文件。它是一个Shell脚本，每次开始Zephyr工作前都应在当前Shell中加载（Source）。可以使用以下代码创建该文件：

```text
$ cat > ~/.zephyrrc
if test "${CROSS}" = xcc
then
    export ARCH=xtensa
    export BOARD=xt-sim
    export ZEPHYR_TOOLCHAIN_VARIANT=xcc
    export XTENSA_TOOLS_PATH=/opt/xtensa/XtDevTools/install/tools/RG-2016.4-linux/XtensaTools
    export XTENSA_BUILDS_PATH=/opt/xtensa/XtDevTools/install/builds/RG-2016.4-linux
    #export XTENSA_BUILD_DIR= #Keep empty to use default directory
    export EMU_PLATFORM=xt-run
elif test "${CROSS}" = zephyr-xtensa
then
    export ARCH=xtensa
    export BOARD=qemu
    export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
    export ZEPHYR_SDK_INSTALL_DIR=/opt/xtensa/zephyr-sdk-64-INTERNAL-11-22-2016
elif test "${CROSS}" = zephyr-x86
then
    export ARCH=x86
    export BOARD=qemu_x86
    export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
    export ZEPHYR_SDK_INSTALL_DIR=/opt/xtensa/zephyr-sdk-64-INTERNAL-11-22-2016
else
    echo "Unsupported compiler '${CROSS}' defined by environment variable CROSS"
fi
```

创建`~/.zephyrrc`后即可开始工作。不过，每次启动新Shell时，都必须先执行以下命令，然后才能编译：

```text
$ cd path/to/zephyr # replace path/to by a real path
$ CROSS=xcc source zephyr-env.sh # Select xcc as compiler
```

<a id="adding-a-user-defined-xtensa-core"></a>

### 添加用户自定义Xtensa内核（User-Defined Xtensa Core）

按以下步骤将自定义内核加入支持列表：

```text
$ XTENSA_CORE=myCore
$ $(which echo) -e "config ${XTENSA_CORE}\n\tbool \"${XTENSA_CORE} core\"\n" >> "soc/xtensa/Kconfig.cores"
```

为该内核创建目录：

```text
$ mkdir soc/xtensa/${XTENSA_CORE}
```

创建自定义链接脚本（Linker Script）并复制到该目录，下一节还会介绍链接脚本：

```text
$ cp  linker.ld  soc/xtensa/${XTENSA_CORE}/linker.ld
```

添加Makefile：

```text
$ echo "obj-y = soc.o" > soc/xtensa/${XTENSA_CORE}/Makefile
```

向链接脚本添加Zephyr专用段（Sections）。`soc/xtensa/linker_more.ld`文件包含这些段，应将其加入默认链接脚本`linker.ld`的`SECTIONS`区域。如果没有使用链接脚本，则必须创建一个并加入这些段。存储器段（Memory Segment）和程序头（PHDR）应替换为适当值。

链接脚本应命名为`linker.ld`，放在`soc/xtensa/${XTENSA_CORE}`目录中。

<a id="configuring-build"></a>

### 配置构建（Configuring Build）

```text
# From the root of the zephyr repository
west build -b None samples/hello_world
west build -t menuconfig
```

以下为典型配置的使用示例：


1. 选择Architecture（架构）


  1. 选择Xtensa架构
2. 选择XTENSA core Selection（XTENSA内核选择）


  1. 选择适当内核，例如`hifi3_bd5`
3. 选择XTENSA Options（XTENSA选项）


  1. 将Hardware clock cycles per second（每秒硬件时钟周期数）设为适当值
  2. 将The path to Xtensa tool（Xtensa工具路径）设为适当值
  3. 将The version of Xtensa tool（Xtensa工具版本）设为适当版本
  4. 将Xtensa build directory（Xtensa构建目录）设为适当值
4. 选择Board Selection（开发板选择）


  1. 选择Xtensa Development ISS（Xtensa开发指令集仿真器）
5. 选择Device Drivers（设备驱动）


  1. 取消勾选Serial Drivers（串口驱动）
6. 选择Compile and Link Features（编译与链接功能）


  1. 按照项目要求正确设置编译器配置及构建选项
7. 选择Exit（退出），并确认保存更改。

还可能需要根据项目的具体需求，更改`menuconfig`中的其他选项。

<a id="compiling-and-running"></a>

### 编译与运行（Compiling and Running）

Xtensa可执行程序既可以在仿真器的独立内核上运行，也可以在连接了仿真外设的内核上运行。

按以下方式构建和运行：

```text
west build -b None
west build -t run
```

<a id="references"></a>

## 参考资料（References）

## 译注

该latest页面仍保留Debian 9.x、RF-2016.4-linux、Makefile及soc/xtensa旧式配置说明。译文保留原始版本、路径与命令以对应原文，不据此声称这些历史步骤已在当前工具链重新验证。 原文版本说明写RF-2016.4-linux，而示例路径写RG-2016.4-linux；构建命令的开发板参数为None。均按原文保留并视为需要核对的历史示例，不能直接当作当前可用命令。代码中的/opt/xtensa是上游工具安装示例目录，不是本译文仓库的位置，使用时应按实际安装配置替换。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [xtensa-customizable](https://ip.cadence.com/ipportfolio/tensilica-ip/xtensa-customizable)：HTTP Error 404: Not Found。

---

[上一章](P003_Cadence_Design_Systems_Inc..md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_nRF9160_Feather.md)
