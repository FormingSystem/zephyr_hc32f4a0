---
id: learning.zephyr-docs.boards-shields.page-216
title: X-NUCLEO-WB05KN1 BLE expansion board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_wb05kn1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="x-nucleo-wb05kn1-ble-expansion-board"></a>

<a id="x-nucleo-wb05kn1"></a>

# 第216章\_X-NUCLEO-WB05KN1：低功耗蓝牙BLE扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_wb05kn1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

X-NUCLEO-WB05KN1是用于扩展STM32 Nucleo的低功耗蓝牙评估板。射频模块已获FCC认证，FCC ID为YCP-MB203202，以及IC认证，IC编号为8976A-MB203202。

<a id="id2"></a>

X-NUCLEO-WB05KN1出厂即兼容Arduino UNO R3连接器，通过默认UART或SPI外设连接主机微控制器。但出厂固件与Zephyr不兼容，须使用CN8排针烧录仅控制器（Controller-only）镜像。固件更换方法见[UM3406](https://www.st.com/resource/en/user_manual/um3406-getting-started-with-the-xcubewb05n-bluetooth-low-energy-software-expansion-for-stm32cube-stmicroelectronics.pdf)[注1](#id1)第3.3节。

注意（Note）

<a id="id4"></a>

ST的[X-CUBE-WB05N](https://www.st.com/en/embedded-software/x-cube-wb05n.html)软件包[注2](#id3)在Utilities/BLE_Transparent_Mode_STM32WB05_controller_only目录下提供Zephyr兼容固件，按所需接口选择SPI或UART子目录。

![官方原图：X-NUCLEO-WB05KN1](images/x-nucleo-wb05kn1.webp)

<a id="id6"></a>

更多信息见X-NUCLEO-WB05KN1网站[注3](#id5)。（[X-NUCLEO-WB05KN1 网站](https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html)）

<a id="configurations"></a>

## 配置（Configurations）

X-NUCLEO-WB05KN1可作为具有UART或SPI主机控制器接口HCI-UART／HCI-SPI的低功耗蓝牙控制器扩展板。

UART默认设置：


- 波特率：921600 bps
- 8个数据位，无校验，1个停止位

<table>
<tr>
<th>UART引脚</th>
<th>Arduino连接器引脚</th>
</tr>
<tr>
<td>接收（RX）</td>
<td>D0</td>
</tr>
<tr>
<td>发送（TX）</td>
<td>D1</td>
</tr>
</table>

SPI默认设置：


- 模式：全双工从机
- 帧格式：Motorola
- 数据长度：8位，高位先传MSB first
- 时钟极性：高，CPOL=1
- 时钟相位：第二边沿，CPHA=1
- CS类型：软件控制

除SPI引脚外，还需要IRQ及复位引脚。

<table>
<tr>
<th>SPI配置引脚</th>
<th>Arduino连接器引脚</th>
</tr>
<tr>
<td>串行时钟（SCK）</td>
<td>D13</td>
</tr>
<tr>
<td>主机输入从机输出（MISO）</td>
<td>D12</td>
</tr>
<tr>
<td>主机输出从机输入（MOSI）</td>
<td>D11</td>
</tr>
<tr>
<td>片选（CS）</td>
<td>D10</td>
</tr>
<tr>
<td>IRQ</td>
<td>A0</td>
</tr>
<tr>
<td>复位（RESET）</td>
<td><code>D7</code></td>
</tr>
</table>

X-NUCLEO-WB05KN1的更多信息：


- <a id="id8"></a>

  X-NUCLEO-WB05KN1数据手册[注4](#id7)（[X-NUCLEO-WB05KN1 数据手册](https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf)）

<a id="programming"></a>

## 编程（Programming）

按UART或SPI接口选择，在west build中添加--shield x_nucleo_wb05kn1_uart或--shield x_nucleo_wb05kn1_spi，为项目构建启用扩展板：

> ```text
> west build -b your_board_name --shield x_nucleo_wb05kn1_uart your_app
> ```

或（Or）

> ```text
> west build -b your_board_name --shield x_nucleo_wb05kn1_spi your_app
> ```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.st.com/resource/en/user_manual/um3406-getting-started-with-the-xcubewb05n-bluetooth-low-energy-software-expansion-for-stm32cube-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3406-getting-started-with-the-xcubewb05n-bluetooth-low-energy-software-expansion-for-stm32cube-stmicroelectronics.pdf)

<a id="id3"></a>

〔[2](#id4)〕 [https://www.st.com/en/embedded-software/x-cube-wb05n.html](https://www.st.com/en/embedded-software/x-cube-wb05n.html)

<a id="id5"></a>

〔[3](#id6)〕 [https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html](https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html)

<a id="id7"></a>

〔[4](#id8)〕 [https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf](https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf)

## 译注

出厂网络固件与Zephyr不兼容，必须烧录controller-only固件；默认UART为921600波特率。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [x-cube-wb05n.html](https://www.st.com/en/embedded-software/x-cube-wb05n.html)：HTTP Error 567: Unknown Status。
- [x-nucleo-wb05kn1.html](https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html)：HTTP Error 567: Unknown Status。
- [stm32wb05kn.pdf](https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf)：HTTP Error 567: Unknown Status。
- [um3406-getting-started-with-the-xcubewb05n-bluetooth-low-energy-software-expansion-for-stm32cube-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3406-getting-started-with-the-xcubewb05n-bluetooth-low-energy-software-expansion-for-stm32cube-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P215_X-NUCLEO-PGEEZ1_page_EEPROM_expansion_board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P217_X-NUCLEO-WBA25A1_BLE_expansion_board.md)
