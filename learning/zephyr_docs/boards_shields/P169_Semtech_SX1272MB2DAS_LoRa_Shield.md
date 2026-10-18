---
id: learning.zephyr-docs.boards-shields.page-169
title: Semtech SX1272MB2DAS LoRa Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/semtech_sx1272mb2das/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="semtech-sx1272mb2das-lora-shield"></a>

<a id="semtech-sx1272mb2das"></a>

# 第169章\_Semtech SX1272MB2DAS LoRa扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/semtech_sx1272mb2das/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Semtech SX1272MB2DAS是兼容Arduino的LoRa扩展板，采用Semtech SX1272 LoRa收发器（Transceiver）。

<a id="id2"></a>

更多扩展板信息见mbed SX1272MB2xAS网站[注1](#id1)。（[mbed SX1272MB2xAS 网站](https://os.mbed.com/components/SX1272MB2xAS/)）

<a id="pins-assignment-of-the-semtech-sx1272mb2das-lora-shield"></a>

### Semtech SX1272MB2DAS LoRa扩展板的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>A0</td>
<td>SX1272复位RESET</td>
</tr>
<tr>
<td>D2</td>
<td>SX1272数字I/O DIO0</td>
</tr>
<tr>
<td><code>D3</code></td>
<td>SX1272数字I/O DIO1</td>
</tr>
<tr>
<td><code>D4</code></td>
<td>SX1272数字I/O DIO2</td>
</tr>
<tr>
<td>D5</td>
<td>SX1272数字I/O DIO3</td>
</tr>
<tr>
<td>D10</td>
<td>SX1272 SPI低有效片选NSS</td>
</tr>
<tr>
<td>D11</td>
<td>SX1272 SPI主机输出从机输入MOSI</td>
</tr>
<tr>
<td>D12</td>
<td>SX1272 SPI主机输入从机输出MISO</td>
</tr>
<tr>
<td>D13</td>
<td>SX1272 SPI时钟SCK</td>
</tr>
</table>

SX1272信号DIO4及DIO5未引到扩展板连接器。

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield semtech_sx1272mb2das，例如：

```text
# From the root of the zephyr repository
west build -b nucleo_f429zi --shield semtech_sx1272mb2das samples/subsys/lorawan/class_a
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://os.mbed.com/components/SX1272MB2xAS/](https://os.mbed.com/components/SX1272MB2xAS/)

---

[上一章](P168_Semtech_SX1262MB2DAS_LoRa_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P170_Semtech_SX1276MB1MAS_LoRa_Shield.md)
