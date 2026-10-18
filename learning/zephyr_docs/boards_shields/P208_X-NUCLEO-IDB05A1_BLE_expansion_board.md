---
id: learning.zephyr-docs.boards-shields.page-208
title: X-NUCLEO-IDB05A1 BLE expansion board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_idb05a1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="x-nucleo-idb05a1-ble-expansion-board"></a>

<a id="x-nucleo-idb05a1"></a>

# 第208章\_X-NUCLEO-IDB05A1：低功耗蓝牙BLE扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_idb05a1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

X-NUCLEO-IDB05A1是采用SPBTLE-RF BlueNRG-MS射频模块的低功耗蓝牙评估板，用于扩展STM32 Nucleo。模块已获FCC认证，FCC ID为S9NSPBTLERF，以及IC认证，IC编号为8976C-SPBTLERF。

X-NUCLEO-IDB05A1兼容ST Morpho及Arduino UNO R3连接器布局，可按需安装ST Morpho连接器。它通过SPI与主机微控制器连接，可改变评估板上的电阻，调整默认SPI时钟、片选及中断IRQ引脚。

注意：此扩展板出厂即兼容Arduino UNO R3连接器，但CS及SCK并非标准Arduino SPI_CS及SPI_SCK信号，见“硬件配置”。

![官方原图：X-NUCLEO-IDB05A1](images/x-nucleo-idb05a1.jpg)

<a id="id2"></a>

更多信息见X-NUCLEO-IDB05A1网站[注1](#id1)。（[X-NUCLEO-IDB05A1 网站](https://www.st.com/en/ecosystems/x-nucleo-idb05a1.html)）

<a id="hardware-configuration"></a>

## 硬件配置（Hardware Configuration）

X-NUCLEO-IDB05A1出厂使用Arduino D3作为SPI SCK，而不是UNO R3通常使用的D13。如果Nucleo在D3提供SPI SCK即可直接使用，否则应更改扩展板配置，见下文。SPI CS使用A1，而不是通常的D10；由于CS为软件驱动的GPIO，使用A1不成问题，见x_nucleo_idb05a1.overlay中的cs-gpios。

可按以下方式移动电阻更改配置：

> - SPI SCK：若用D13替代D3，移除R4并安装R6。

此外，可根据主板对BLE扩展板进行以下改动：

> - CS：若用D10替代A1，移除R2并安装R7。
> - IRQ：若用D9替代A0，移除R1并安装R8。

<a id="id4"></a>

详情可查看X-NUCLEO-IDB05A1产品简介[注2](#id3)图3。（[X-NUCLEO-IDB05A1 产品简介](https://www.st.com/resource/en/data_brief/x-nucleo-idb05a1.pdf)）

已知stm32mp157x_dk2需要上述CS／IRQ引脚改动，见boards/stm32mp157x_dk2.overlay；nucleo_l476rg不需要硬件改动。

<a id="hardware"></a>

## 硬件（Hardware）

X-NUCLEO-IDB05A1采用SPBTLE-RF芯片，主要特性：

> - 基于Bluetooth® SMART 4.1网络处理器BlueNRG-MS的低功耗蓝牙模块，具有FCC及IC认证
> - 集成巴伦BALF-NRG-01D3
> - 芯片天线（Chip Antenna）

X-NUCLEO-IDB05A1的更多信息：


- <a id="id5"></a>

  X-NUCLEO-IDB05A1产品简介[注2](#id3)（[X-NUCLEO-IDB05A1 产品简介](https://www.st.com/resource/en/data_brief/x-nucleo-idb05a1.pdf)）

<a id="programming"></a>

## 编程（Programming）

可将X-NUCLEO-IDB05A1用作具有SPI主机控制器接口HCI-SPI的低功耗蓝牙控制器扩展板。构建项目时添加--shield参数启用：

> ```text
> west build -b your_board_name --shield x_nucleo_idb05a1 your_app
> ```

也可在项目CMakeLists.txt中设置使用此扩展板：

```text
set(SHIELD x_nucleo_idb05a1)
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.st.com/en/ecosystems/x-nucleo-idb05a1.html](https://www.st.com/en/ecosystems/x-nucleo-idb05a1.html)

<a id="id3"></a>

〔2〕 ([1](#id4),[2](#id5)) [https://www.st.com/resource/en/data_brief/x-nucleo-idb05a1.pdf](https://www.st.com/resource/en/data_brief/x-nucleo-idb05a1.pdf)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [x-nucleo-idb05a1.html](https://www.st.com/en/ecosystems/x-nucleo-idb05a1.html)：HTTP Error 567: Unknown Status。
- [x-nucleo-idb05a1.pdf](https://www.st.com/resource/en/data_brief/x-nucleo-idb05a1.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P207_X-NUCLEO-GNSS1A1_GNSS_expansion_board_based_on_Teseo-LIV3F.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P209_X-NUCLEO-IKS01A1_MEMS_Inertial_and_Environmental_Multi_sensor_shield.md)
