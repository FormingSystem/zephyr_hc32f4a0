---
id: learning.zephyr-docs.driver_samples.page-36
title: DALI照明接口示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/dali/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="dali"></a>

# 第36章\_DALI照明接口示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/dali/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 36.1\_概览（Overview）

本例利用[数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）](../hardware/P133_数字可寻址照明接口.md#dali-api)驱动API，使支持DALI的LED驱动器闪烁。

<a id="building-and-running"></a>

## 36.2\_构建与运行（Building and Running）

DALI总线接口在开发板设备树（Devicetree）中定义。原文要求设备树包含提供DALI总线访问的`dali0`节点。示例可参考[samples/drivers/dali/boards中的预定义覆盖文件（Overlay）](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/dali/boards)。

**注意：**正常运行需要DALI专用物理接口（Physical Interface）。

> 译注——节点与别名：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/dali/src/main.c)实际通过DT_ALIAS(dali)选择设备；[扩展板覆盖文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/boards/shields/mikroe_dali_2_click/mikroe_dali_2_click.overlay)把dali别名指向mikroe_dali2_click节点。因此原文所说dali0与当前读取入口不能混为一谈，应按所使用版本同时核对设备节点和别名。

<a id="building-and-running-for-st-nucleo-f091rc"></a>

### 36.2.1\_ST Nucleo F091RC构建与运行（Building and Running for ST Nucleo F091RC）

[samples/drivers/dali/boards/nucleo_f091rc.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/dali/boards/nucleo_f091rc.overlay)专门面向用作DALI总线物理接口的Mikroe-2672 DALI2 click开发板。该板以负逻辑（Negative Logic）发送信号，即Tx低电平对应DALI总线空闲（Tx Low ↔ DALI Bus Idle）。

可按以下方式为[Nucleo F091RC](https://docs.zephyrproject.org/latest/boards/st/nucleo_f091rc/doc/index.html#nucleo_f091rc)构建并运行：

> 译注——执行位置与条件：在已配置Zephyr开发环境的终端、Zephyr源码根目录执行，使用上述物理接口和两个指定扩展板配置。构建成功后再烧录；物理接口、目标或设备树报错时，先返回相应板级配置核对。

```bash
west build -b nucleo_f091rc --shield arduino_uno_click --shield mikroe_dali_2_click samples/drivers/dali
west flash
```

<a id="building-and-running-for-nordic-nrf52840"></a>

### 36.2.2\_Nordic nRF52840构建与运行（Building and Running for Nordic nRF52840）

[samples/drivers/dali/boards/nrf52840dk_nrf52840.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/dali/boards/nrf52840dk_nrf52840.overlay)同样专门面向作为DALI物理接口的Mikroe-2672 DALI2 click开发板。其引脚分配支持使用Arduino UNO click扩展板。click板以负逻辑发送信号，即Tx低电平对应DALI总线空闲。

可按以下方式为[nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk)构建并运行；终端、工作目录与前一分支相同：

```bash
west build -b nrf52840dk --shield arduino_uno_click --shield mikroe_dali_2_click samples/drivers/dali
west flash
```

> 译注——版本对应：原命令的nrf52840dk写法按原文保留；读者应按所用版本的开发板文档确认完整目标及自动限定规则，不能因覆盖文件名包含nrf52840就省略版本核对。

<a id="sample-output"></a>

### 36.2.3\_示例输出（Sample output）

应能看到每2秒向DALI总线发送一帧，帧内容交替变化：一帧向全部控制装置（Control Gear）广播DALI OFF关闭命令，另一帧广播DALI RECALL MAX恢复最大亮度命令。接入控制装置后，其LED会在无光输出与最大输出之间交替。

> 译注——发送顺序：所读实现先发送RECALL MAX LEVEL（0xff05），休眠2000毫秒，再发送OFF（0xff00），再次休眠。这里的“广播”作用于该DALI总线上的全部控制装置；本批未发送任何照明控制命令。


对应官方文档源码：[samples/drivers/dali/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/dali/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/dali/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/dali/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P035_LIN模拟响应节点示例.md) · [返回大纲](大纲.md) · [下一章](P037_PS2接口示例.md)
