---
id: learning.zephyr-docs.boards-shields.page-162
title: Seeed W5500 Ethernet Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/seeed_w5500/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="seeed-w5500-ethernet-shield"></a>

<a id="seeed-w5500"></a>

# 第162章\_Seeed W5500以太网扩展板（Ethernet Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/seeed_w5500/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id5"></a>

Seeed W5500以太网扩展板[注2](#id4)采用Arduino连接器，具有：（[W5500 以太网扩展板](https://wiki.seeedstudio.com/W5500_Ethernet_Shield_v1.0)）


- <a id="id3"></a>

  [W5500](https://wiznet.io/products/iethernet-chips/w5500)[注1](#id2)独立10/100 Mbps以太网控制器，集成MAC及PHY，FIFO缓冲区为16 KB；
- SPI串行接口；
- Grove UART连接器；
- Grove I2C连接器；
- SD卡槽。

<a id="id1"></a>

![官方原图：Seeed W5500 Ethernet Shield](images/seeed_w5500.webp)

Seeed W5500以太网扩展板（Ethernet Shield）

<a id="pins-assignment-of-the-w5500-shield"></a>

### W5500扩展板的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>复位（RST）</td>
<td>以太网控制器复位</td>
</tr>
<tr>
<td>D2</td>
<td>以太网控制器中断输出</td>
</tr>
<tr>
<td>D10</td>
<td>SPI片选</td>
</tr>
<tr>
<td>D11</td>
<td>SPI主机输出从机输入MOSI</td>
</tr>
<tr>
<td>D12</td>
<td>SPI主机输入从机输出MISO</td>
</tr>
<tr>
<td>D13</td>
<td>SPI时钟</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield seeed_w5500，例如：

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield seeed_w5500 samples/net/dhcpv4_client
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://wiznet.io/products/iethernet-chips/w5500](https://wiznet.io/products/iethernet-chips/w5500)

<a id="id4"></a>

〔[2](#id5)〕 [https://wiki.seeedstudio.com/W5500_Ethernet_Shield_v1.0](https://wiki.seeedstudio.com/W5500_Ethernet_Shield_v1.0)

---

[上一章](P161_RTKMIPILCDB00000BE_MIPI_Display.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P163_Seeed_Studio_COB_LED_Driver_Board_for_XIAO.md)
