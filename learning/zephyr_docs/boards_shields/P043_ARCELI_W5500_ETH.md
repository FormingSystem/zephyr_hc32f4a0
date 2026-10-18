---
id: learning.zephyr-docs.boards-shields.page-43
title: ARCELI W5500 ETH
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/arceli_eth_w5500/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arceli-w5500-eth"></a>

<a id="arceli-eth-w5500"></a>

# 第43章\_ARCELI W5500以太网模块（ETH）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/arceli_eth_w5500/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id2"></a>

ARCELI [W5500](https://wiznet.io/products/iethernet-chips/w5500)以太网引出板通过10针排针提供SPI访问。W5500 [注1](#id1)是10/100 Mbit/s独立以太网控制器，集成MAC及PHY，具有16 Kbytes FIFO缓冲区及SPI串行接口。

<a id="pins-assignment-of-the-w5500-shield"></a>

### W5500扩展板的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>RST#，低有效复位</td>
<td>以太网控制器复位</td>
</tr>
<tr>
<td>CS#，低有效片选</td>
<td>SPI片选</td>
</tr>
<tr>
<td>串行时钟（SCK）</td>
<td>SPI时钟</td>
</tr>
<tr>
<td>串行数据输出（SDO）</td>
<td>SPI从机数据输出MISO</td>
</tr>
<tr>
<td>SDI</td>
<td>SPI从机数据输入，原文括号仍写MISO，照录并提示</td>
</tr>
<tr>
<td>中断（INT）</td>
<td>以太网控制器中断输出</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板／引出板可用于通过Arduino或自定义排针提供SPI的任意开发板；自定义接口需调整覆盖文件。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield arceli_eth_w5500，例如：

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield arceli_eth_w5500 samples/net/dhcpv4_client
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://wiznet.io/products/iethernet-chips/w5500](https://wiznet.io/products/iethernet-chips/w5500)

## 译注

原文SPI输入引脚说明出现MISO字样，与通常的模块端MOSI输入命名不同，未据此自行改动接线表。

---

[上一章](P042_Panasonic_Grid-EYE_Shields.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P044_ArduCam_CU450_OV5640_Camera_Module.md)
