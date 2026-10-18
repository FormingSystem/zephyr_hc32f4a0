---
id: learning.zephyr-docs.boards-shields.page-197
title: Waveshare 1.3inch OLED Display Module for Raspberry Pi Pico
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/waveshare_pico_oled_1_3/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="waveshare-1-3inch-oled-display-module-for-raspberry-pi-pico"></a>

<a id="waveshare-pico-oled-1-3"></a>

# 第197章\_树莓派Pico用Waveshare 1.3英寸OLED显示模块

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/waveshare_pico_oled_1_3/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

树莓派Pico用Waveshare 1.3英寸OLED显示模块采用SinoWealth SH1107控制器，尺寸为64×128像素，纵向较长；原文此处称为LCD模块。它通过I2C连接，也可选用SPI，但需要焊接。模块具有2个用户程序可用的按键，便于实现用户界面。

<a id="id2"></a>

扩展板及Arduino适配器详情见Waveshare Pico OLED 1.3模块网站[注1](#id1)。（[Waveshare Pico OLED 1.3 模块网站](https://www.waveshare.com/wiki/Pico-OLED-1.3)）

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>GP6</td>
<td>I2C_SDA</td>
<td>I2C数据输入，I2C1_SDA</td>
</tr>
<tr>
<td>GP7</td>
<td>I2C_SCL</td>
<td>I2C时钟输入，I2C1_SCL</td>
</tr>
<tr>
<td>GP8</td>
<td>OLED_DC</td>
<td>数据／命令控制引脚，可选</td>
</tr>
<tr>
<td>GP9</td>
<td>OLED_CS</td>
<td>SPI片选，SPI1_CSN，可选</td>
</tr>
<tr>
<td>GP10</td>
<td>OLED_CLK</td>
<td>SPI时钟输入，SPI1_SCK，可选</td>
</tr>
<tr>
<td>GP11</td>
<td>OLED_DIN</td>
<td>SPI数据输入，SPI1_TX，可选</td>
</tr>
<tr>
<td>GP12</td>
<td>OLED_RST</td>
<td>复位（Reset）</td>
</tr>
<tr>
<td>GP15</td>
<td>通用输入输出（GPIO）</td>
<td>用户按键0</td>
</tr>
<tr>
<td>GP17</td>
<td>通用输入输出（GPIO）</td>
<td>用户按键1</td>
</tr>
</table>

注意（Note）

SPI接口默认不可用。将J1、J2及J3的0 Ω电阻移到SPI一侧以启用SPI；原文registers按上下文译为电阻。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=waveshare_pico_oled_1_3，例如：

```text
# From the root of the zephyr repository
west build -b rpi_pico --shield waveshare_pico_oled_1_3 samples/subsys/display/lvgl
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.waveshare.com/wiki/Pico-OLED-1.3](https://www.waveshare.com/wiki/Pico-OLED-1.3)

## 译注

标题为OLED，原文概述称LCD；切换SPI需要移动0 Ω电阻。

---

[上一章](P196_Waveshare_1.14inch_LCD_Display_Module_for_Raspberry_Pi_Pico.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P198_Waveshare_Pico_UPS-B_shield.md)
