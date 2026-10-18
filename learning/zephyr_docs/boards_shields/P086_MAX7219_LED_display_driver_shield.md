---
id: learning.zephyr-docs.boards-shields.page-86
title: MAX7219 LED display driver shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/max7219/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="max7219-led-display-driver-shield"></a>

<a id="max7219-shield"></a>

# 第86章\_MAX7219 LED显示驱动扩展板（Display Driver Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/max7219/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

这是基于MAX7219的LED矩阵通用扩展板定义。此类显示屏采用SPI，通常只有VCC、GND、DIN、CS及CLK五个引脚。

<a id="current-supported-displays"></a>

### 当前支持的显示屏

<table>
<tr>
<th>显示（Display）</th>
<th>控制器（Controller）</th>
<th>扩展板名称（Designation）</th>
</tr>
<tr>
<td>无品牌8×8像素模块</td>
<td>MAX7219</td>
<td>max7219_8x8</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置并定义SPI节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield max7219_8x8，例如：

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield max7219_8x8 samples/drivers/display/
```

---

[上一章](P085_M5Stack_Unit_Mini_OLED.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P087_MB1280_STMod_fan-out_shield.md)
