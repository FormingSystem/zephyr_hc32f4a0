---
id: learning.zephyr-docs.boards-shields.page-15
title: Adafruit FeatherWing 128x32 OLED Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_featherwing_128x32_oled/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-featherwing-128x32-oled-shield"></a>

<a id="adafruit-featherwing-128x32-oled"></a>

# 第15章\_Adafruit FeatherWing 128×32 OLED扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_featherwing_128x32_oled/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit OLED FeatherWing采用兼容SSD1306的128×32 OLED显示屏，配有3个用户按键。（[Adafruit OLED FeatherWing 扩展板](https://learn.adafruit.com/adafruit-oled-featherwing)）

<a id="id1"></a>

![官方原图：Adafruit FeatherWing 128x32 OLED Shield](images/adafruit_featherwing_128x32_oled.webp)

Adafruit FeatherWing 128×32 OLED扩展板（Shield），图片来源：Adafruit

<a id="pins-assignment-of-the-adafruit-featherwing-128x32-oled-shield"></a>

### Adafruit FeatherWing 128×32 OLED扩展板的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>串行数据线（SDA）</td>
<td>SSD1306 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>SSD1306 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>GPIO5</td>
<td>按键C，INPUT_KEY_C</td>
</tr>
<tr>
<td>GPIO6</td>
<td>按键B，INPUT_KEY_B</td>
</tr>
<tr>
<td>GPIO9</td>
<td>按键A，INPUT_KEY_A</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Feather连接器配置并定义I2C节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_featherwing_128x32_oled，例如：

```text
# From the root of the zephyr repository
west build -b adafruit_feather_nrf52840 --shield adafruit_featherwing_128x32_oled samples/subsys/display/lvgl
```

---

[上一章](P014_Adafruit_DS2484_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_Adafruit_FeatherWing_128x64_OLED_Shield.md)
