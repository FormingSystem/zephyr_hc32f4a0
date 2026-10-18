---
id: learning.zephyr-docs.boards-shields.page-176
title: SSD1306 128x64 32 pixels generic shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/ssd1306/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="ssd1306-128x64-32-pixels-generic-shield"></a>

<a id="ssd1306-128-shield"></a>

# 第176章\_SSD1306 128x64(/32) pixels通用扩展板（Generic Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/ssd1306/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

这是基于SSD1306控制器、分辨率为128×64或128×32像素OLED显示屏的通用扩展板。显示屏使用I2C接口，通常只有GND、VCC、SCL及SDA四个引脚，可用跳线连接开发板排针。

<a id="current-supported-displays"></a>

### 当前支持的显示屏

<table>
<tr>
<th>显示（Display）</th>
<th>控制器／驱动（Controller/Driver）</th>
<th>扩展板名称（Designation）</th>
</tr>
<tr>
<td>无品牌128×64像素显示屏</td>
<td>SSD1306控制器／ssd1306驱动</td>
<td>ssd1306_128x64</td>
</tr>
<tr>
<td>无品牌128×32像素显示屏</td>
<td>SSD1306控制器／ssd1306驱动</td>
<td>ssd1306_128x32</td>
</tr>
<tr>
<td>无品牌128×64像素显示屏</td>
<td>SH1106控制器／ssd1306驱动</td>
<td>sh1106_128x64</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于已配置Arduino连接器且定义I2C接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield ssd1306_128x64，例如：

```text
# From the root of the zephyr repository
west build -b frdm_k64f --shield ssd1306_128x64 samples/subsys/display/lvgl
```

---

[上一章](P175_Sparkfun_SHTC3_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P177_Generic_ST7735R_Display_Shield.md)
