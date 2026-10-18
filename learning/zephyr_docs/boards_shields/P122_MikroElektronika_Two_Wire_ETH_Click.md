---
id: learning.zephyr-docs.boards-shields.page-122
title: MikroElektronika Two Wire ETH Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_two_wire_eth_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-two-wire-eth-click"></a>

<a id="mikroe-two-wire-eth-click-shield"></a>

# 第122章\_MikroElektronika Two Wire ETH Click双线以太网扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_two_wire_eth_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id5"></a>

<a id="id3"></a>

Two-Wire ETH Click采用Microchip [LAN8651B1-E/LM](https://www.microchip.com/en-us/product/lan8651) [注2](#id4)低功耗10BASE-T1S MAC-PHY控制器。它集成MAC及以太网PHY，使低成本MCU可接入支持多点及点对点拓扑的10BASE-T1S网络；主机通过符合OPEN Alliance 10BASE-T1x MAC-PHY串行接口规范的高速SPI通信，更多信息见扩展板网站[注1](#id2)。（[Two-Wire ETH Click模块 扩展板 网站](https://www.mikroe.com/two-wire-eth-click)）

<a id="id1"></a>

[![官方原图：MikroElektronika Two Wire ETH Click](images/mikroe_two-wire-eth-click.webp)](images/mikroe_two-wire-eth-click.webp)

MikroElektronika Two Wire ETH Click双线以太网扩展板，图片来源：MikroElektronika

<a id="pins-assignment-of-the-eth-click-shield"></a>

# 第122章\_ETH Click扩展板的引脚分配

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
<td>SPI从机数据输入MOSI</td>
</tr>
<tr>
<td>中断（INT）</td>
<td>以太网控制器中断输出</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS连接器配置，并定义SPI及GPIO节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield mikroe_two_wire_eth_click，例如：

```text
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947/cpu0 --shield mikroe_two_wire_eth_click samples/net/dhcpv4_client
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.mikroe.com/two-wire-eth-click](https://www.mikroe.com/two-wire-eth-click)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.microchip.com/en-us/product/lan8651](https://www.microchip.com/en-us/product/lan8651)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [lan8651](https://www.microchip.com/en-us/product/lan8651)：HTTP Error 403: Forbidden。
- [two-wire-eth-click](https://www.mikroe.com/two-wire-eth-click)：HTTP Error 403: Forbidden。

---

[上一章](P121_MikroElektronika_Temp_Hum_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P123_MikroElektronika_Weather_Click.md)
