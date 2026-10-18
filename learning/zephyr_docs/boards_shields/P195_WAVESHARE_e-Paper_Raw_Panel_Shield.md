---
id: learning.zephyr-docs.boards-shields.page-195
title: WAVESHARE e-Paper Raw Panel Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/waveshare_epaper/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="waveshare-e-paper-raw-panel-shield"></a>

<a id="waveshare-epaper"></a>

# 第195章\_WAVESHARE电子纸裸屏扩展板（e-Paper Raw Panel Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/waveshare_epaper/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

WAVESHARE电子纸裸屏扩展板是通用驱动扩展板，可通过SPI驱动多种电泳电子墨水显示屏（Electrophoretic Display，EPD）。板上还包含23LC1024 1 Mbit SPI串行SRAM，目前Zephyr RTOS尚不支持。

<a id="id2"></a>

更多信息见Universal e-Paper Raw Panel Driver Shield网站[注1](#id1)。（[通用电子纸 裸屏驱动器 扩展板 网站](https://www.waveshare.com/e-paper-shield.htm)）

<a id="pins-assignment-of-the-e-paper-shield"></a>

### 电子纸扩展板的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
<th></th>
</tr>
<tr>
<td>D5</td>
<td>RAM低有效片选CSn</td>
<td>RAM片选</td>
</tr>
<tr>
<td>D6</td>
<td>SD低有效片选CSn</td>
<td>电子纸SD卡片选</td>
</tr>
<tr>
<td><code>D7</code></td>
<td>电子纸忙信号EPD BUSY</td>
<td>电子纸忙状态输出</td>
</tr>
<tr>
<td>D8</td>
<td>电子纸低有效复位EPD RESETn</td>
<td>电子纸复位输入</td>
</tr>
<tr>
<td>D9</td>
<td>电子纸数据／命令EPD DC</td>
<td>电子纸数据／命令输入</td>
</tr>
<tr>
<td>D10</td>
<td>电子纸低有效片选EPD CSn</td>
<td>电子纸片选输入</td>
</tr>
<tr>
<td>D11</td>
<td>SPI主机输出从机输入（MOSI）</td>
<td>串行数据输入</td>
</tr>
<tr>
<td>D12</td>
<td>SPI主机输入从机输出（MISO）</td>
<td>串行数据输出</td>
</tr>
<tr>
<td>D13</td>
<td>SPI串行时钟（SCK）</td>
<td>串行时钟输入</td>
</tr>
</table>

<a id="current-supported-displays"></a>

### 当前支持的显示屏

<table>
<tr>
<th>显示（Display）</th>
<th>排线标签（Ribbon Cable Label）</th>
<th>控制器／驱动（Controller/Driver）</th>
<th>扩展板名称（Designation）</th>
</tr>
<tr>
<td>Good Display GDEH0213B1显示屏</td>
<td>HINK-E0213</td>
<td>SSD1673控制器／ssd16xx驱动</td>
<td>waveshare_epaper_gdeh0213b1</td>
</tr>
<tr>
<td>Good Display GDEH0213B72显示屏</td>
<td>HINK-E0213A22</td>
<td>SSD1675A控制器／ssd16xx驱动</td>
<td>waveshare_epaper_gdeh0213b72</td>
</tr>
<tr>
<td>Good Display GDEH029A1显示屏</td>
<td>E029A01</td>
<td>SSD1608控制器／ssd16xx驱动</td>
<td>waveshare_epaper_gdeh029a1</td>
</tr>
<tr>
<td>Good Display GDEW075T7显示屏</td>
<td>WFT0583CZ61</td>
<td>UC8179控制器／gd7965驱动</td>
<td>waveshare_epaper_gdew075t7</td>
</tr>
<tr>
<td>Good Display GDEH0154D67显示屏</td>
<td>HINK-E0154A07</td>
<td>SSD1681控制器／ssd16xx驱动</td>
<td>waveshare_epaper_gdeh0154a07</td>
</tr>
<tr>
<td>Good Display GDEW042T2显示屏</td>
<td>WFT0420CZ15</td>
<td>UC8176控制器／gd7965驱动</td>
<td>waveshare_epaper_gdew042t2及waveshare_epaper_gdew042t2-p</td>
</tr>
<tr>
<td>Good Display GDEY0213B74显示屏</td>
<td>FPC-A002</td>
<td>SSD1680控制器／ssd16xx驱动</td>
<td>waveshare_epaper_gdey0213b74</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时，必须输入与显示屏匹配的扩展板名称，见上表。例如：

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield waveshare_epaper_gdeh0213b1 samples/subsys/display/lvgl
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.waveshare.com/e-paper-shield.htm](https://www.waveshare.com/e-paper-shield.htm)

## 译注

板载23LC1024串行SRAM尚不受支持。

---

[上一章](P194_WAVESHARE_DSI_LCD_Panel.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P196_Waveshare_1.14inch_LCD_Display_Module_for_Raspberry_Pi_Pico.md)
