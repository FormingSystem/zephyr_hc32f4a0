---
id: learning.zephyr-docs.boards-shields.page-202
title: X-NUCLEO-67W61M1 Wi-Fi 6 expansion board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_67w61m1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="x-nucleo-67w61m1-wi-fi-6-expansion-board"></a>

<a id="x-nucleo-67w61m1"></a>

# 第202章\_X-NUCLEO-67W61M1：Wi-Fi 6扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_67w61m1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

X-NUCLEO-67W61M1是采用ST67W611M1 Wi-Fi协处理器模块的Wi-Fi 6评估板，用于扩展STM32 Nucleo。

X-NUCLEO-67W61M1兼容Arduino UNO R3排针，也可使用树莓派40针GPIO排针。它通过默认Arduino SPI引脚及D3、D5、D6、D10与主机微控制器连接。

![官方原图：X-NUCLEO-67W61M1](images/x-nucleo-67w61m1.webp)

<a id="id2"></a>

更多信息见X-NUCLEO-67W61M1网站[注1](#id1)。（[X-NUCLEO-67W61M1 网站](https://www.st.com/en/evaluation-tools/x-nucleo-67w61m1.html)）

<a id="features"></a>

## 功能（Features）

X-NUCLEO-67W61M1采用ST67W611M1芯片，主要特性：

> - 2.4 GHz Wi-Fi 6
> - 站点STA及STA＋软件接入点SoftAP模式
> - 全双工SPI通信，最高40 MHz
> - 基于DTIM或目标唤醒时间TWT的低功耗模式

<a id="coprocessor-flashing"></a>

## 协处理器烧录（Coprocessor Flashing）

<a id="id8"></a>

<a id="id4"></a>

<a id="id6"></a>

仅支持TCP/IP运行在主机的T02架构。必须使用官方[X-CUBE-ST67W61软件包](https://github.com/STMicroelectronics/x-cube-st67w61)[注4](#id7)中的外部工具烧录正确固件，见[ST67W611M1硬件设置](https://wiki.st.com/stm32mcu/wiki/Connectivity:Wi-Fi_MCU_Hardware_Setup)[注2](#id3)及[X-CUBE-ST67W61架构](https://wiki.st.com/stm32mcu/wiki/Connectivity:X-CUBE-ST67W61_Architecture)[注3](#id5)。

X-CUBE软件包包含烧录脚本：

```text
cd x-cube-st67w61/Projects/ST67W6X_Scripts/Binaries/
./NCP_update_mission_profile_t02.sh
```

注意（Note）

早于v2.0.106的固件未获完整支持，可能导致低功耗等功能出现问题。

<a id="programming"></a>

## 编程（Programming）

构建项目时添加--shield参数以启用扩展板：

```text
west build -b your_board_name --shield x_nucleo_67w61m1 your_app
```

例如，zperf示例可按以下方式构建：

```text
west build -b your_board_name --shield x_nucleo_67w61m1 samples/net/zperf -- -DEXTRA_CONF_FILE=boards/x_nucleo_67w61m1.conf
```

<a id="improve-performance"></a>

## 提升性能（Improve Performance）

为提升性能，ST67W611M1驱动在主机支持时使用DMA，且DMA必须配置为TX／RX模式。此配置与开发板有关，因此只有部分开发板可直接使用该功能。每块板都须在boards/shields/x_nucleo_67w61m1/boards/中提供专用设备树覆盖文件，因此该目录也相当于DMA兼容列表。

<a id="at-commands"></a>

## AT命令（AT Commands）

<a id="id10"></a>

主机与ST67W611M1内部使用AT命令执行多种控制及配置功能，见[ST67W611M1 AT命令文档](https://applist67.github.io/Web_AT_Documentation_ST67/)[注5](#id9)。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.st.com/en/evaluation-tools/x-nucleo-67w61m1.html](https://www.st.com/en/evaluation-tools/x-nucleo-67w61m1.html)

<a id="id3"></a>

〔[2](#id4)〕 [https://wiki.st.com/stm32mcu/wiki/Connectivity:Wi-Fi_MCU_Hardware_Setup](https://wiki.st.com/stm32mcu/wiki/Connectivity:Wi-Fi_MCU_Hardware_Setup)

<a id="id5"></a>

〔[3](#id6)〕 [https://wiki.st.com/stm32mcu/wiki/Connectivity:X-CUBE-ST67W61_Architecture](https://wiki.st.com/stm32mcu/wiki/Connectivity:X-CUBE-ST67W61_Architecture)

<a id="id7"></a>

〔[4](#id8)〕 [https://github.com/STMicroelectronics/x-cube-st67w61](https://github.com/STMicroelectronics/x-cube-st67w61)

<a id="id9"></a>

〔[5](#id10)〕 [https://applist67.github.io/Web_AT_Documentation_ST67/](https://applist67.github.io/Web_AT_Documentation_ST67/)

## 译注

仅支持TCP/IP运行在主机的T02固件架构；旧于v2.0.106的固件不完全支持。DMA需板级覆盖配置。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Connectivity:Wi-Fi_MCU_Hardware_Setup](https://wiki.st.com/stm32mcu/wiki/Connectivity:Wi-Fi_MCU_Hardware_Setup)：The read operation timed out。
- [Connectivity:X-CUBE-ST67W61_Architecture](https://wiki.st.com/stm32mcu/wiki/Connectivity:X-CUBE-ST67W61_Architecture)：The read operation timed out。
- [x-nucleo-67w61m1.html](https://www.st.com/en/evaluation-tools/x-nucleo-67w61m1.html)：HTTP Error 567: Unknown Status。

---

[上一章](P201_X-NUCLEO-53L0A1_ranging_and_gesture_detection_sensor_expansion_board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P203_X-NUCLEO-BNRG2A1_BLE_expansion_board.md)
