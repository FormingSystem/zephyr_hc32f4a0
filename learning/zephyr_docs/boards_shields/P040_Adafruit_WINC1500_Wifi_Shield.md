---
id: learning.zephyr-docs.boards-shields.page-40
title: Adafruit WINC1500 Wifi Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_winc1500/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-winc1500-wifi-shield"></a>

<a id="adafruit-winc1500"></a>

# 第40章\_Adafruit WINC1500 Wi-Fi扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_winc1500/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit WINC1500是兼容Arduino的Wi-Fi扩展板，采用Microchip ATWINC1500控制器，并提供microSD卡槽。

目前不支持SD卡槽。

<a id="id2"></a>

更多信息见Adafruit WINC1500网站[注1](#id1)。（[Adafruit WINC1500 网站](https://learn.adafruit.com/adafruit-winc1500-wifi-shield-for-arduino)）

<a id="pins-assignment-of-the-adafruit-winc1500-wifi-shield"></a>

### Adafruit WINC1500 Wi-Fi扩展板的引脚分配

<table>
<tr>
<th>扩展板连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td><code>D4</code></td>
<td>MicroSD SPI低有效片选CSn，暂不支持</td>
</tr>
<tr>
<td>D5</td>
<td>WINC1500 RST，低有效复位</td>
</tr>
<tr>
<td>D6，标记b</td>
<td>WINC1500 EN，使能</td>
</tr>
<tr>
<td><code>D7</code></td>
<td>WINC1500 IRQ，中断输出</td>
</tr>
<tr>
<td>D10</td>
<td>WINC1500 SPI低有效片选CSn</td>
</tr>
<tr>
<td>D11，标记a</td>
<td>SPI MOSI，串行数据输入</td>
</tr>
<tr>
<td>D12，标记a</td>
<td>SPI MISO，串行数据输出</td>
</tr>
<tr>
<td>D13，标记a</td>
<td>SPI SCK，串行时钟输入</td>
</tr>
</table>

标记a的引脚须用跳线接到扩展板SPI接口；要支持低功耗，须将标记b的引脚接到扩展板En端。

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_winc1500，例如：

```text
# From the root of the zephyr repository
west build -b frdm_k64f --shield adafruit_winc1500 samples/net/wifi
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://learn.adafruit.com/adafruit-winc1500-wifi-shield-for-arduino](https://learn.adafruit.com/adafruit-winc1500-wifi-shield-for-arduino)

## 译注

microSD功能原文注明尚不支持；SPI与使能跳线需按图设置。

---

[上一章](P039_Adafruit_VEML7700_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P041_Analog_Devices_Low-Speed_Mixed-Signal_Playground.md)
