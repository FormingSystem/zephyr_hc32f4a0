---
id: learning.zephyr-docs.boards-shields.page-114
title: MikroElektronika MCP251xFD Click shields
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_mcp251xfd_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-mcp251xfd-click-shields"></a>

<a id="mikroe-mcp251xfd-click-shield"></a>

# 第114章\_MikroElektronika MCP251xFD Click扩展板（Shields）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_mcp251xfd_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="id7"></a>

<a id="id9"></a>

Zephyr支持多种搭载Microchip[外部CAN FD控制器](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-external-controllers)[注1](#id6)的Click扩展板，既有带集成[CAN FD收发器](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-transceivers)[注2](#id8)的型号，也有不带的型号。

<a id="mikroelektronika-mcp2517fd-click-shield"></a>

<a id="mikroe-mcp2517fd-click-shield"></a>

## MikroElektronika MCP2517FD Click扩展板

<a id="overview"></a>

### 概述（Overview）

<a id="id15"></a>

<a id="id11"></a>

[MCP2517FD](https://www.microchip.com/en-us/product/MCP2517FD) Click采用SPI接口MCP2517FD CAN FD控制器[注4](#id14)及[ATA6563](https://www.microchip.com/en-us/product/ATA6563)高速CAN收发器[注3](#id10)。

<a id="id22"></a>

更多信息见Mikroe MCP2517FD Click [注7](#id21)。（[Mikroe MCP2517FD click模块](https://www.mikroe.com/mcp2517fd-click)）

<a id="id3"></a>

![官方原图：MikroElektronika MCP2517FD Click](images/mikroe_mcp2517fd_click.webp)

MikroElektronika MCP2517FD Click，图片来源：MikroElektronika

<a id="mikroelektronika-mcp2518fd-click-shield"></a>

<a id="mikroe-mcp2518fd-click-shield"></a>

## MikroElektronika MCP2518FD Click扩展板

<a id="id1"></a>

### 概述（Overview）

<a id="id17"></a>

<a id="id12"></a>

[MCP2518FD](https://www.microchip.com/en-us/product/MCP2518FD) Click采用SPI接口MCP2518FD CAN FD控制器[注5](#id16)及[ATA6563](https://www.microchip.com/en-us/product/ATA6563)高速CAN收发器[注3](#id10)。

<a id="id24"></a>

更多信息见Mikroe MCP2518FD Click [注8](#id23)。（[Mikroe MCP2518FD click模块](https://www.mikroe.com/mcp2518fd-click)）

<a id="id4"></a>

![官方原图：MikroElektronika MCP2518FD Click](images/mikroe_mcp2518fd_click.webp)

MikroElektronika MCP2518FD Click，图片来源：MikroElektronika

<a id="mikroelektronika-mcp251863-click-shield"></a>

<a id="mikroe-mcp251863-click-shield"></a>

## MikroElektronika MCP251863 Click扩展板

<a id="id2"></a>

### 概述（Overview）

<a id="id20"></a>

<a id="id13"></a>

<a id="id18"></a>

[MCP251863](https://www.microchip.com/en-us/product/MCP251863) Click采用SPI接口MCP251863 CAN FD控制器[注6](#id19)，集成[ATA6563](https://www.microchip.com/en-us/product/ATA6563)高速CAN收发器[注3](#id10)，软件兼容独立[MCP2518FD](https://www.microchip.com/en-us/product/MCP2518FD)控制器[注5](#id16)。

<a id="id26"></a>

更多信息见Mikroe MCP251863 Click [注9](#id25)。（[Mikroe MCP251863 click模块](https://www.mikroe.com/mcp251863-click)）

<a id="id5"></a>

![官方原图：MikroElektronika MCP251863 Click](images/mikroe_mcp251863_click.webp)

MikroElektronika MCP251863 Click，图片来源：MikroElektronika

<a id="requirements"></a>

## 前置要求（Requirements）

这些扩展板使用mikroBUS，目标板须定义mikrobus_spi及mikrobus_header标签，支持电平触发中断及最高18 MHz SPI时钟，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时选择--shield mikroe_mcp2517fd_click、--shield mikroe_mcp2518fd_click或--shield mikroe_mcp251863_click，例如：

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s28 --shield mikroe_mcp2517fd_click samples/drivers/can/counter
west flash
```

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s28 --shield mikroe_mcp2518fd_click samples/drivers/can/counter
west flash
```

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s28 --shield mikroe_mcp251863_click samples/drivers/can/counter
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id6"></a>

〔[1](#id7)〕 [https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-external-controllers](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-external-controllers)

<a id="id8"></a>

〔[2](#id9)〕 [https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-transceivers](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-transceivers)

<a id="id10"></a>

〔3〕 ([1](#id11),[2](#id12),[3](#id13)) [https://www.microchip.com/en-us/product/ATA6563](https://www.microchip.com/en-us/product/ATA6563)

<a id="id14"></a>

〔[4](#id15)〕 [https://www.microchip.com/en-us/product/MCP2517FD](https://www.microchip.com/en-us/product/MCP2517FD)

<a id="id16"></a>

〔5〕 ([1](#id17),[2](#id18)) [https://www.microchip.com/en-us/product/MCP2518FD](https://www.microchip.com/en-us/product/MCP2518FD)

<a id="id19"></a>

〔[6](#id20)〕 [https://www.microchip.com/en-us/product/MCP251863](https://www.microchip.com/en-us/product/MCP251863)

<a id="id21"></a>

〔[7](#id22)〕 [https://www.mikroe.com/mcp2517fd-click](https://www.mikroe.com/mcp2517fd-click)

<a id="id23"></a>

〔[8](#id24)〕 [https://www.mikroe.com/mcp2518fd-click](https://www.mikroe.com/mcp2518fd-click)

<a id="id25"></a>

〔[9](#id26)〕 [https://www.mikroe.com/mcp251863-click](https://www.mikroe.com/mcp251863-click)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [ATA6563](https://www.microchip.com/en-us/product/ATA6563)：HTTP Error 403: Forbidden。
- [MCP2517FD](https://www.microchip.com/en-us/product/MCP2517FD)：HTTP Error 403: Forbidden。
- [MCP251863](https://www.microchip.com/en-us/product/MCP251863)：HTTP Error 403: Forbidden。
- [MCP2518FD](https://www.microchip.com/en-us/product/MCP2518FD)：HTTP Error 403: Forbidden。
- [can-external-controllers](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-external-controllers)：HTTP Error 403: Forbidden。
- [can-transceivers](https://www.microchip.com/en-us/products/interface-and-connectivity/can/can-transceivers)：HTTP Error 403: Forbidden。
- [mcp2517fd-click](https://www.mikroe.com/mcp2517fd-click)：HTTP Error 403: Forbidden。
- [mcp251863-click](https://www.mikroe.com/mcp251863-click)：HTTP Error 403: Forbidden。
- [mcp2518fd-click](https://www.mikroe.com/mcp2518fd-click)：HTTP Error 403: Forbidden。

---

[上一章](P113_MikroElektronika_MCP251x_Click_shields.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P115_MikroElektronika_Pressure_3_Click.md)
