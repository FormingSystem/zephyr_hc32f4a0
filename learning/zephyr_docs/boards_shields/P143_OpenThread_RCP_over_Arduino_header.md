---
id: learning.zephyr-docs.boards-shields.page-143
title: OpenThread RCP over Arduino header
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/openthread_rcp_arduino/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="openthread-rcp-over-arduino-header"></a>

<a id="openthread-rcp-arduino-shield"></a>

# 第143章\_通过Arduino排针连接OpenThread RCP

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/openthread_rcp_arduino/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id2"></a>

此虚拟扩展板可将具有Arduino R3兼容排针的开发板连接外部[OpenThread RCP](https://openthread.io/platforms/co-processor)设备[注1](#id1)；RCP提供Thread射频，另一块板作为OpenThread主机。

<a id="requirements"></a>

## 前置要求（Requirements）

<a id="id4"></a>

必须有RCP射频设备才能使用。以下采用OpenThread在[nRF52840 DK](../boards_nordic/P006_nRF52840_DK.md#nrf52840dk)上的参考实现演示，见OpenThread on nRF52840示例网站[注2](#id3)。（[OpenThread on nRF52840 示例网站](https://github.com/openthread/ot-nrf528xx/blob/main/src/nrf52840/README.md)）

按开发板接线，可使用UART或SPI传输。

以下命令在Ubuntu 24.04上构建并烧录RCP固件：

<a id="preparation"></a>

### 准备（Preparation）

```text
git clone https://github.com/openthread/ot-nrf528xx.git --recurse-submodules
cd ot-nrf528xx
python3 -m venv .venv
source .venv/bin/activate
./script/bootstrap
```

<a id="building"></a>

### 构建（Building）

<a id="tab-0-VUFSVA=="></a>

<a id="tab-0-U1BJ"></a>

<a id="panel-0-VUFSVA=="></a>

**通用异步收发器（UART）**

```text
# Set -DOT_PLATFORM_DEFINES="UART_HWFC_ENABLED=1" to enable flow control
./script/build nrf52840 UART_trans -DOT_PLATFORM_DEFINES="UART_HWFC_ENABLED=0"
```

<a id="panel-0-U1BJ"></a>

**串行外设接口（SPI）**

```text
./script/build nrf52840 SPI_trans_NCP
```

<a id="flashing"></a>

### 烧录（Flashing）

```text
arm-none-eabi-objcopy -O ihex build/bin/ot-rcp build/bin/ot-rcp.hex
nrfjprog -f nrf52 --chiperase --program build/bin/ot-rcp.hex --reset
```

<a id="pins-assignments"></a>

### 引脚分配（Pin Assignments）

RCP固件默认分配了引脚，下表列出Arduino排针与nRF52840 DK引脚。

<a id="tab-1-VUFSVA=="></a>

<a id="tab-1-U1BJ"></a>

<a id="panel-1-VUFSVA=="></a>

**通用异步收发器（UART）**

<table>
<tr>
<th>Arduino排针引脚</th>
<th>主机功能</th>
<th>nRF52840 DK引脚</th>
</tr>
<tr>
<td>D0</td>
<td>UART接收（RX）</td>
<td>P0.06</td>
</tr>
<tr>
<td>D1</td>
<td>UART发送（TX）</td>
<td>P0.08</td>
</tr>
<tr>
<td>取决于主机</td>
<td>UART清除发送（CTS）</td>
<td>P0.05，流控</td>
</tr>
<tr>
<td>取决于主机</td>
<td>UART请求发送（RTS）</td>
<td>P0.07，流控</td>
</tr>
</table>

<a id="panel-1-U1BJ"></a>

**串行外设接口（SPI）**

<table>
<tr>
<th>Arduino排针引脚</th>
<th>功能（Function）</th>
<th>nRF52840 DK引脚</th>
</tr>
<tr>
<td>D8</td>
<td>RSTn</td>
<td>P0.18/RESET</td>
</tr>
<tr>
<td>D9</td>
<td>INTn</td>
<td>P0.30</td>
</tr>
<tr>
<td>D10</td>
<td>SPI低有效片选CSn</td>
<td>P0.29</td>
</tr>
<tr>
<td>D11</td>
<td>SPI主机输出从机输入（MOSI）</td>
<td>P0.04</td>
</tr>
<tr>
<td>D12</td>
<td>SPI主机输入从机输出（MISO）</td>
<td>P0.28</td>
</tr>
<tr>
<td>D13</td>
<td>SPI串行时钟（SCK）</td>
<td>P0.03</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

构建使用此扩展板的项目时，为west build添加--shield openthread_rcp_arduino_serial或--shield openthread_rcp_arduino_spi，例如：

<a id="tab-2-VUFSVA=="></a>

<a id="tab-2-U1BJ"></a>

<a id="panel-2-VUFSVA=="></a>

**通用异步收发器（UART）**

```text
# From the root of the zephyr repository
west build -b stm32h573i_dk/stm32h573xx --shield openthread_rcp_arduino_serial samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-ot-rcp-host-uart.conf"
```

<a id="panel-2-U1BJ"></a>

**串行外设接口（SPI）**

```text
# From the root of the zephyr repository
west build -b stm32h573i_dk/stm32h573xx --shield openthread_rcp_aduino_spi samples/net/sockets/echo_client -- -DCONF_FILE="prj.conf overlay-ot-rcp-host-uart.conf"
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://openthread.io/platforms/co-processor](https://openthread.io/platforms/co-processor)

<a id="id3"></a>

〔[2](#id4)〕 [https://github.com/openthread/ot-nrf528xx/blob/main/src/nrf52840/README.md](https://github.com/openthread/ot-nrf528xx/blob/main/src/nrf52840/README.md)

---

[上一章](P142_Olimex_SHIELD-MIDI.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P144_P3T1755DP_Arduino_Shield_Evaluation_Board.md)
