---
id: learning.zephyr-docs.boards-shields.page-17
title: Adafruit FeatherWing MAX3421E Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_featherwing_max3421e/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-featherwing-max3421e-shield"></a>

<a id="adafruit-featherwing-max3421e"></a>

# 第17章\_Adafruit FeatherWing MAX3421E扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_featherwing_max3421e/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit USB Host FeatherWing采用MAX3421E USB外设／主机控制器，通过SPI连接。（[Adafruit MAX3421E USB主机FeatherWing](https://learn.adafruit.com/adafruit-usb-host-featherwing-with-max3421e)）

<a id="id1"></a>

![官方原图：Adafruit FeatherWing MAX3421E Shield](images/adafruit_featherwing_max3421e.webp)

Adafruit FeatherWing MAX3421E扩展板（Shield），图片来源：Adafruit

<a id="pins-assignment-of-the-shield-connector"></a>

### 扩展板连接器的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>D9</td>
<td>MAX3421E中断IRQ</td>
</tr>
<tr>
<td>D10</td>
<td>SPI片选（CS）</td>
</tr>
<tr>
<td>串行时钟（SCK）</td>
<td>SPI串行时钟（SCK）</td>
</tr>
<tr>
<td>主机输出从机输入（MOSI）</td>
<td>SPI主机输出从机输入（MOSI）</td>
</tr>
<tr>
<td>主机输入从机输出（MISO）</td>
<td>SPI主机输入从机输出（MISO）</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

在Zephyr应用中调用west build时设置--shield adafruit_featherwing_max3421e。

---

[上一章](P016_Adafruit_FeatherWing_128x64_OLED_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P018_Adafruit_HT16K33_LED_Matrix_Shield.md)
