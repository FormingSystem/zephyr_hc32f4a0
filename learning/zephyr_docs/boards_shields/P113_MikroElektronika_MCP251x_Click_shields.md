---
id: learning.zephyr-docs.boards-shields.page-113
title: MikroElektronika MCP251x Click shields
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_mcp251x_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-mcp251x-click-shields"></a>

<a id="mikroe-mcp251x-click-shield"></a>

# 第113章\_MikroElektronika MCP251x Click扩展板（Shields）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_mcp251x_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="id5"></a>

<a id="id7"></a>

Zephyr支持多种搭载Microchip[外部CAN控制器](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-external-controllers)[注1](#id4)的Click扩展板，既有带集成CAN收发器[注2](#id6)的型号，也有不带的型号。（[CAN收发器（Transceiver）](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-transceivers)）

<a id="mikroelektronika-can-spi-3-3v-5v-click-shield"></a>

<a id="mikroe-can-spi-click-shield"></a>

## MikroElektronika CAN SPI 3.3V／5V Click扩展板

<a id="overview"></a>

### 概述（Overview）

<a id="id11"></a>

<a id="id9"></a>

CAN SPI 3.3V／5V Click采用SPI接口[MCP2515](https://www.microchip.com/en-us/product/MCP2515)独立CAN控制器[注4](#id10)及[SN65HVD230](https://www.ti.com/product/SN65HVD230)高速CAN收发器[注3](#id8)。

<a id="id18"></a>

<a id="id20"></a>

更多信息见Mikroe CAN SPI 3.3V Click [注7](#id17)及5V Click [注8](#id19)。（[Mikroe CAN SPI 3.3V click模块](https://www.mikroe.com/can-spi-33v-click)；[Mikroe CAN SPI 5V click模块](https://www.mikroe.com/can-spi-5v-click)）

<a id="id2"></a>

![官方原图：MikroElektronika CAN SPI 3.3V/5V Click](images/mikroe_can_spi_click.webp)

MikroElektronika CAN SPI 3.3V／5V Click，图片来源：MikroElektronika

<a id="mikroelektronika-mcp25625-click-shield"></a>

<a id="mikroe-mcp25625-click-shield"></a>

## MikroElektronika MCP25625 Click扩展板

<a id="id1"></a>

### 概述（Overview）

<a id="id16"></a>

<a id="id14"></a>

<a id="id12"></a>

[MCP25625](https://www.microchip.com/en-us/product/MCP25625) Click采用SPI接口[MCP2562](https://www.microchip.com/en-us/product/MCP2562)5 CAN控制器[注6](#id15)，集成MCP2562高速CAN收发器[注5](#id13)，软件兼容独立[MCP2515](https://www.microchip.com/en-us/product/MCP2515)控制器[注4](#id10)。

<a id="id22"></a>

更多信息见Mikroe MCP25625 Click [注9](#id21)。（[Mikroe MCP25625 click模块](https://www.mikroe.com/mcp25625-click)）

<a id="id3"></a>

![官方原图：MikroElektronika MCP25625 Click](images/mikroe_mcp25625_click.webp)

MikroElektronika MCP25625 Click，图片来源：MikroElektronika

<a id="requirements"></a>

## 前置要求（Requirements）

这些扩展板使用mikroBUS，目标板须定义mikrobus_spi及mikrobus_header标签，支持电平触发中断及最高10 MHz SPI时钟，标签详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield mikroe_can_spi_click或--shield mikroe_mcp25625_click，例如：

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s28 --shield mikroe_can_spi_click samples/drivers/can/counter
west flash
```

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s28 --shield mikroe_mcp25625_click samples/drivers/can/counter
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id4"></a>

〔[1](#id5)〕 [https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-external-controllers](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-external-controllers)

<a id="id6"></a>

〔[2](#id7)〕 [https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-transceivers](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-transceivers)

<a id="id8"></a>

〔[3](#id9)〕 [https://www.ti.com/product/SN65HVD230](https://www.ti.com/product/SN65HVD230)

<a id="id10"></a>

〔4〕 ([1](#id11),[2](#id12)) [https://www.microchip.com/en-us/product/MCP2515](https://www.microchip.com/en-us/product/MCP2515)

<a id="id13"></a>

〔[5](#id14)〕 [https://www.microchip.com/en-us/product/MCP2562](https://www.microchip.com/en-us/product/MCP2562)

<a id="id15"></a>

〔[6](#id16)〕 [https://www.microchip.com/en-us/product/MCP25625](https://www.microchip.com/en-us/product/MCP25625)

<a id="id17"></a>

〔[7](#id18)〕 [https://www.mikroe.com/can-spi-33v-click](https://www.mikroe.com/can-spi-33v-click)

<a id="id19"></a>

〔[8](#id20)〕 [https://www.mikroe.com/can-spi-5v-click](https://www.mikroe.com/can-spi-5v-click)

<a id="id21"></a>

〔[9](#id22)〕 [https://www.mikroe.com/mcp25625-click](https://www.mikroe.com/mcp25625-click)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [MCP2515](https://www.microchip.com/en-us/product/MCP2515)：HTTP Error 403: Forbidden。
- [MCP2562](https://www.microchip.com/en-us/product/MCP2562)：HTTP Error 403: Forbidden。
- [MCP25625](https://www.microchip.com/en-us/product/MCP25625)：HTTP Error 403: Forbidden。
- [can-external-controllers](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-external-controllers)：HTTP Error 403: Forbidden。
- [can-transceivers](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-transceivers)：HTTP Error 403: Forbidden。
- [can-spi-33v-click](https://www.mikroe.com/can-spi-33v-click)：HTTP Error 403: Forbidden。
- [can-spi-5v-click](https://www.mikroe.com/can-spi-5v-click)：HTTP Error 403: Forbidden。
- [mcp25625-click](https://www.mikroe.com/mcp25625-click)：HTTP Error 403: Forbidden。

---

[上一章](P112_MikroElektronika_LTE_IoT_7_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P114_MikroElektronika_MCP251xFD_Click_shields.md)
