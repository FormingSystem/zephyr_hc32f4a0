---
id: learning.zephyr-docs.boards-shields.page-4
title: Adafruit 2.8 TFT Touch Shield v2
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_2_8_tft_touch_v2/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-2-8-tft-touch-shield-v2"></a>

<a id="adafruit-2-8-tft-touch-v2"></a>

# 第4章\_Adafruit 2.8英寸TFT触摸扩展板v2

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_2_8_tft_touch_v2/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

Adafruit 2.8英寸TFT触摸扩展板v2采用ILI9341控制器，分辨率320×240，可选电阻触摸屏STMPE610或电容触摸屏FT6206。Zephyr RTOS支持两种屏幕的显示输出，但触摸输入仅支持电容版本；更多信息见Adafruit 2.8英寸TFT Touch Shield v2网站[注1](#id2)。（[Adafruit 2.8” TFT触摸 扩展板 v2 网站](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2)）

<a id="id1"></a>

![官方原图：Adafruit 2.8" TFT Touch Shield v2](images/adafruit_2_8_tft_touch_v2.webp)

Adafruit 2.8英寸TFT触摸扩展板v2（TFT Touch Shield），图片来源：Adafruit

<a id="pins-assignment-of-the-adafruit-2-8-tft-touch-shield-v2"></a>

### Adafruit 2.8英寸TFT触摸扩展板v2的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td><code>D4</code></td>
<td>MicroSD SPI低有效片选CSn</td>
</tr>
<tr>
<td><code>D7</code></td>
<td>触摸控制器中断IRQ，见下方说明</td>
</tr>
<tr>
<td>D8</td>
<td>STMPE610 SPI低有效片选CSn，电阻触摸版本</td>
</tr>
<tr>
<td>D9</td>
<td>ILI9341数据／命令选择DC</td>
</tr>
<tr>
<td>D10</td>
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
<td>FT6206 SDA，电容触摸版本</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>FT6206 SCL，电容触摸版本</td>
</tr>
</table>

注意（Note）

触摸控制器IRQ默认未连接，使用前须焊接ICSP_SI1跳线，并调整驱动配置及其设备树条目。

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino或Arduino Nano连接器配置，并定义SPI及GPIO接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_2_8_tft_touch_v2，例如：

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield adafruit_2_8_tft_touch_v2 samples/subsys/display/lvgl
```

若连接到Arduino Nano接口开发板，调用west build时设置--shield adafruit_2_8_tft_touch_v2_nano。

```text
# From the root of the zephyr repository
west build -b arduino_nano_33_ble --shield adafruit_2_8_tft_touch_v2_nano samples/subsys/display/lvgl
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2)

## 译注

显示输出支持两种触摸屏版本，但Zephyr触摸输入仅支持FT6206电容版本；IRQ跳线需另行焊接。

---

[上一章](P003_Adafruit_24LC32_EEPROM_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_Adafruit_I2C_to_8_Channel_Solenoid_Driver_Shield.md)
