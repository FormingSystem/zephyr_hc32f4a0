---
id: learning.zephyr-docs.boards-shields.page-196
title: Waveshare 1.14inch LCD Display Module for Raspberry Pi Pico
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/waveshare_pico_lcd_1_14/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="waveshare-1-14inch-lcd-display-module-for-raspberry-pi-pico"></a>

<a id="waveshare-pico-lcd-1-14"></a>

# 第196章\_树莓派Pico用Waveshare 1.14英寸LCD显示模块

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/waveshare_pico_lcd_1_14/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

树莓派Pico用Waveshare 1.14英寸LCD显示模块采用ST7789V控制器，是240×135像素、65K色IPS LCD模块，通过SPI连接。模块具有2个按键及摇杆，供用户程序使用，便于实现用户界面。

<a id="id2"></a>

扩展板及Arduino适配器详情见Waveshare Pico-LCD-1.14模块网站[注1](#id1)。（[Waveshare Pico-LCD-1.14 模块网站](https://www.waveshare.com/wiki/Pico-LCD-1.14)）

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>GP2</td>
<td>向上（UP）</td>
<td>摇杆向上</td>
</tr>
<tr>
<td>GP3</td>
<td>CTRL</td>
<td>摇杆中心</td>
</tr>
<tr>
<td>GP8</td>
<td>LCD_DC</td>
<td>数据／命令控制引脚</td>
</tr>
<tr>
<td>GP9</td>
<td>LCD_CS</td>
<td>SPI片选，SPI1_CSN</td>
</tr>
<tr>
<td>GP10</td>
<td>LCD_CLK</td>
<td>SPI时钟输入，SPI1_SCK</td>
</tr>
<tr>
<td>GP11</td>
<td>LCD_DIN</td>
<td>SPI数据输入，SPI1_TX</td>
</tr>
<tr>
<td>GP12</td>
<td>LCD_RST</td>
<td>复位（Reset）</td>
</tr>
<tr>
<td>GP13</td>
<td>LCD_BL</td>
<td>背光（Backlight）</td>
</tr>
<tr>
<td>GP15</td>
<td>通用输入输出（GPIO）</td>
<td>用户按键A</td>
</tr>
<tr>
<td>GP17</td>
<td>通用输入输出（GPIO）</td>
<td>用户按键1</td>
</tr>
<tr>
<td>GP18</td>
<td>向下（DOWN）</td>
<td>摇杆向下</td>
</tr>
<tr>
<td>GP20</td>
<td>向右（RIGHT）</td>
<td>摇杆向右</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=waveshare_pico_lcd_1_14，例如：

```text
# From the root of the zephyr repository
west build -b rpi_pico --shield waveshare_pico_oled_1_14 samples/subsys/display/lvgl
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.waveshare.com/wiki/Pico-LCD-1.14](https://www.waveshare.com/wiki/Pico-LCD-1.14)

---

[上一章](P195_WAVESHARE_e-Paper_Raw_Panel_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P197_Waveshare_1.3inch_OLED_Display_Module_for_Raspberry_Pi_Pico.md)
