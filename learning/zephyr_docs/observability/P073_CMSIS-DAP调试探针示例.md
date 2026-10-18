---
id: learning.zephyr-docs.observability.page-73
title: CMSIS-DAP调试探针示例
kind: reference
status: maintained
domains: [zephyr, observability, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/dap/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="cmsis-dap"></a>

# 第73章\_CMSIS-DAP调试探针示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/dap/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/dap/README.rst/..)。

<a id="overview"></a>

## 73.1 概述（Overview）

本应用示例展示如何通过DAP USB后端（DAP USB Backend），使用串行线调试端口（Serial Wire Debug Port，SWDP）接口驱动和CMSIS-DAP控制器。

<a id="requirements"></a>

## 73.2 要求（Requirements）

本示例支持多种硬件配置。最简单的配置是将`SWDIO`连接到`dio`、将`SWDCLK`连接到`clk`，还可以选择将`nRESET`连接到`reset`。可选的`noe`引脚用于启用端口，例如用于SWD连接被复用的情况。

> 译注——引脚名称与设备树：这里的`dio`、`clk`等是接口信号名称，不是某个芯片通用的物理脚号。当前示例的`app.overlay`与板专用覆盖文件分别定义GPIO连接，部分配置还涉及`dout`和`dnoe`。应按实际生效的设备树、探针硬件和目标板接口核对连接，不能把某个覆盖文件中的Arduino接口编号当作所有平台的引脚映射。

<a id="building-and-running"></a>

## 73.3 构建与运行（Building and Running）

以下原文命令构建并烧录DAP示例：

```sh
west build -b nrf52840dk_nrf52840 samples/subsys/dap
west flash
```

> 译注——板目标版本：原命令使用旧式名称`nrf52840dk_nrf52840`；当前官方`tests.yaml`列出的板目标为`nrf52840dk/nrf52840`。测试项标记为`build_only: true`，不能据此声称已经通过目标连接、读内存或调试实测。以实际版本的板目标和覆盖文件为准。

> 译注——命令前提：在已经准备所用Zephyr版本的Python依赖、目标工具链和烧录工具的UCRT64 Bash或Linux Bash中，以Zephyr源码根目录执行。示例固件应写入承担探针功能的开发板；构建成功后再烧录。构建失败先处理板目标、配置或依赖问题，烧录失败则检查烧录器与连接，不把旧固件视为本次构建结果。

将HIC连接到目标设备，并尝试一些pyOCD命令，例如：

```text
pyocd commander -t nrf52840

0029527 W Board ID FE5D is not recognized [mbed_board]
Connected to NRF52840 [Sleeping]: FE5D244DFE1F33DB
pyocd> read32 0x20004f18 32
20004f18:  20001160 2000244c 00000000 0000e407    | ..` .$L........|
20004f28:  ffffffff ffffffff 00000000 aaaaaaaa    |................|
pyocd> halt
Successfully halted device
pyocd> reg
general registers:
      lr: 0x00009cdd                   r7: 0x00000000 (0)
      pc: 0x000033ca                   r8: 0x00000000 (0)
      r0: 0x00000000 (0)               r9: 0x00000000 (0)
      r1: 0x20002854 (536881236)      r10: 0x00000000 (0)
      r2: 0x20000be4 (536873956)      r11: 0x00000000 (0)
      r3: 0x00000000 (0)              r12: 0x00000000 (0)
      r4: 0x200017e8 (536877032)       sp: 0x20002898
      r5: 0x20001867 (536877159)     xpsr: 0x61000000 (1627389952)
      r6: 0x00000000 (0)
```

> 译注——探针与目标的角色：这里的HIC是运行CMSIS-DAP示例固件的探针端；`pyocd commander -t nrf52840`中的`-t`选择被调试目标。两者可能使用不同芯片，不能把探针固件的构建板目标直接当成pyOCD的目标类型。该命令要求主机已安装pyOCD且能够访问探针USB接口。原日志中的板识别警告、地址、寄存器和连接结果全部保留，只代表原文示例；若本机不能连接，应先核对探针枚举、目标类型和硬件连接，不据此执行后续内存或寄存器操作。本文未连接探针、暂停目标或烧录硬件。


> 译注——配置与实现依据：[samples/subsys/dap/tests.yaml](../../../samples/subsys/dap/tests.yaml)、[samples/subsys/dap/app.overlay](../../../samples/subsys/dap/app.overlay)、[samples/subsys/dap/boards/nrf52840dk_nrf52840.overlay](../../../samples/subsys/dap/boards/nrf52840dk_nrf52840.overlay)。本地参照采用相对链接，其版本可能与所核对的官方main快照不同，文件摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/subsys/dap/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/dap/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/dap/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/subsys/dap/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P072_MIPISysT日志示例.md) · [返回大纲](大纲.md)
