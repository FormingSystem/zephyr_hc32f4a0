---
id: learning.zephyr-docs.boards-shields.page-170
title: Semtech SX1276MB1MAS LoRa Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/semtech_sx1276mb1mas/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="semtech-sx1276mb1mas-lora-shield"></a>

<a id="semtech-sx1276mb1mas"></a>

# 第170章\_Semtech SX1276MB1MAS LoRa扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/semtech_sx1276mb1mas/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Semtech SX1276MB1MAS是兼容Arduino的LoRa扩展板，采用Semtech SX1276 LoRa收发器（Transceiver）。

<a id="id2"></a>

更多扩展板信息见mbed SX1276MB1xAS网站[注1](#id1)。（[mbed SX1276MB1xAS 网站](https://os.mbed.com/components/SX1276MB1xAS/)）

<a id="pins-assignment-of-the-semtech-sx1276mb1mas-lora-shield"></a>

### Semtech SX1276MB1MAS LoRa扩展板的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>A0</td>
<td>SX1276复位RESET</td>
</tr>
<tr>
<td>A3</td>
<td>SX1276数字I/O DIO4（1）</td>
</tr>
<tr>
<td>A4</td>
<td>天线接收／发送RX／TX</td>
</tr>
<tr>
<td>D2</td>
<td>SX1276数字I/O DIO0</td>
</tr>
<tr>
<td><code>D3</code></td>
<td>SX1276数字I/O DIO1</td>
</tr>
<tr>
<td><code>D4</code></td>
<td>SX1276数字I/O DIO2</td>
</tr>
<tr>
<td>D5</td>
<td>SX1276数字I/O DIO3</td>
</tr>
<tr>
<td>D8</td>
<td>SX1276数字I/O DIO4（1）</td>
</tr>
<tr>
<td>D9</td>
<td>SX1276数字I/O DIO5</td>
</tr>
<tr>
<td>D10</td>
<td>SX1276 SPI低有效片选NSS</td>
</tr>
<tr>
<td>D11</td>
<td>SX1276 SPI主机输出从机输入MOSI</td>
</tr>
<tr>
<td>D12</td>
<td>SX1276 SPI主机输入从机输出MISO</td>
</tr>
<tr>
<td>D13</td>
<td>SX1276 SPI时钟SCK</td>
</tr>
</table>


1. SX1276 DIO4默认配置到D8，需要时可通过设备树改到A3。

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield semtech_sx1276mb1mas，例如：

```text
# From the root of the zephyr repository
west build -b nucleo_l073rz --shield semtech_sx1276mb1mas samples/subsys/lorawan/class_a
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://os.mbed.com/components/SX1276MB1xAS/](https://os.mbed.com/components/SX1276MB1xAS/)

---

[上一章](P169_Semtech_SX1272MB2DAS_LoRa_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P171_Sparkfun_SparkFun_MicroMod_Asset_Tracker_Shield.md)
