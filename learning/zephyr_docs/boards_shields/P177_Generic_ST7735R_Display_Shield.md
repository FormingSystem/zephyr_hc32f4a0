---
id: learning.zephyr-docs.boards-shields.page-177
title: Generic ST7735R Display Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/st7735r/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="generic-st7735r-display-shield"></a>

<a id="st7735r-generic"></a>

# 第177章\_通用ST7735R显示扩展板（Generic Display Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/st7735r/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id2"></a>

这是基于ST7735R显示控制器的通用显示扩展板定义。控制器详情见ST7735R数据手册[注1](#id1)。（[ST7735R 数据手册](https://www.crystalfontz.com/controllers/Sitronix/ST7735R/319/)）

<a id="pins-assignment-of-the-generic-st7735r-display-shield"></a>

### 通用ST7735R显示扩展板的引脚分配

<table>
<tr>
<th>Arduino连接器引脚</th>
<th colspan="2">功能（Function）</th>
</tr>
<tr>
<td>D8</td>
<td>ST7735R复位</td>
<td></td>
</tr>
<tr>
<td>D9</td>
<td>ST7735R数据／命令选择DC</td>
<td>数据／命令，Data/Command</td>
</tr>
<tr>
<td>D10</td>
<td>SPI从机选择（SS）</td>
<td>串行从机选择，Serial Slave Select</td>
</tr>
<tr>
<td>D11</td>
<td>SPI主机输出从机输入（MOSI）</td>
<td>串行数据输入，Serial Data Input</td>
</tr>
<tr>
<td>D12</td>
<td>SPI主机输入从机输出（MISO）</td>
<td>串行数据输出，Serial Data Out</td>
</tr>
<tr>
<td>D13</td>
<td>SPI串行时钟（SCK）</td>
<td>串行时钟输入，Serial Clock Input</td>
</tr>
</table>

<a id="current-supported-displays"></a>

### 当前支持的显示屏

<table>
<tr>
<th>显示（Display）</th>
<th>扩展板名称（Designation）</th>
</tr>
<tr>
<td>Adafruit 160×128像素18位TFT</td>
<td>st7735r_ada_160x128</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield st7735r_ada_160x128，例如：

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield st7735r_ada_160x128 samples/subsys/display/lvgl
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.crystalfontz.com/controllers/Sitronix/ST7735R/319/](https://www.crystalfontz.com/controllers/Sitronix/ST7735R/319/)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://www.crystalfontz.com/controllers/Sitronix/ST7735R/319/)：HTTP Error 403: Forbidden。

---

[上一章](P176_SSD1306_128x64_32_pixels_generic_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P178_Generic_ST7789V_Display_Shield.md)
