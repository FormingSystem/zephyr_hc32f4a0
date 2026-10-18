---
id: learning.zephyr-docs.boards-shields.page-55
title: Buydisplay 2.8 TFT Touch Shield with Arduino adapter
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/buydisplay_2_8_tft_touch_arduino/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="buydisplay-2-8-tft-touch-shield-with-arduino-adapter"></a>

<a id="buydisplay-2-8-tft-touch-arduino"></a>

# 第55章\_Buydisplay 2.8英寸TFT触摸扩展板及Arduino适配器

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/buydisplay_2_8_tft_touch_arduino/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Buydisplay 2.8英寸TFT触摸扩展板分辨率320×240，采用ILI9341显示控制器及FT6206电容触摸控制器，使用时需要Arduino适配器。

<a id="id2"></a>

<a id="id4"></a>

更多信息见Buydisplay 2.8英寸TFT Touch Shield网站[注1](#id1)及Arduino适配器网站[注2](#id3)。（[Buydisplay 2.8” TFT触摸 扩展板 网站](https://www.buydisplay.com/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module)；[Arduino 适配器 网站](https://www.buydisplay.com/arduino-shield-for-tft-lcd-with-ili9341-controller-and-arduino-due-mega-uno)）

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>D5</td>
<td>触摸控制器中断IRQ，见下方说明</td>
</tr>
<tr>
<td><code>D7</code></td>
<td>ILI9341数据／命令选择DC</td>
</tr>
<tr>
<td>D10</td>
<td>ILI9341复位</td>
</tr>
<tr>
<td>D9</td>
<td>ILI9341 SPI低有效片选CSn</td>
</tr>
<tr>
<td>D11</td>
<td>SPI MOSI，串行数据输入</td>
</tr>
<tr>
<td>D12</td>
<td>SPI MISO，串行数据输出</td>
</tr>
<tr>
<td>D13</td>
<td>SPI SCK，串行时钟输入</td>
</tr>
<tr>
<td>串行数据线（SDA）</td>
<td>FT6206数据SDA</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>FT6206时钟SCL</td>
</tr>
</table>

注意（Note）

触摸控制器IRQ默认未连接，使用前须焊接“5 INT”跳线，并调整驱动配置及设备树条目。

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield buydisplay_2_8_tft_touch_arduino，例如：

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield buydisplay_2_8_tft_touch_arduino samples/subsys/display/lvgl
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.buydisplay.com/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module](https://www.buydisplay.com/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module)

<a id="id3"></a>

〔[2](#id4)〕 [https://www.buydisplay.com/arduino-shield-for-tft-lcd-with-ili9341-controller-and-arduino-due-mega-uno](https://www.buydisplay.com/arduino-shield-for-tft-lcd-with-ili9341-controller-and-arduino-due-mega-uno)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module](https://www.buydisplay.com/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module)：HTTP Error 403: Forbidden。
- [arduino-shield-for-tft-lcd-with-ili9341-controller-and-arduino-due-mega-uno](https://www.buydisplay.com/arduino-shield-for-tft-lcd-with-ili9341-controller-and-arduino-due-mega-uno)：HTTP Error 403: Forbidden。

---

[上一章](P054_BOOSTXL-ULPSENSE_Ultra-low_Power_Sensor_BoosterPack.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P056_Buydisplay_3.5_TFT_Touch_Shield_with_Arduino_adapter.md)
