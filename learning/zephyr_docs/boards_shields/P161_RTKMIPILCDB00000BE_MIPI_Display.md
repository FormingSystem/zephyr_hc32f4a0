---
id: learning.zephyr-docs.boards-shields.page-161
title: RTKMIPILCDB00000BE MIPI Display
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/rtkmipilcdb00000be/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rtkmipilcdb00000be-mipi-display"></a>

<a id="rtkmipilcdb00000be"></a>

# 第161章\_RTKMIPILCDB00000BE MIPI显示屏（Display）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/rtkmipilcdb00000be/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Focus LCDs RTKMIPILCDB00000BE MIPI显示屏是4.5英寸480×854像素TFT电容触摸面板，并配有背光单元。

此显示屏使用26针排针连接器。

<a id="pins-assignment-of-the-renesas-rtkmipilcdb00000be-mipi-display"></a>

### Renesas RTKMIPILCDB00000BE MIPI显示屏的引脚分配

<table>
<tr>
<th>连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>14</td>
<td>触摸控制器I2C数据SDA</td>
</tr>
<tr>
<td>15</td>
<td>显示屏背光使能</td>
</tr>
<tr>
<td>16</td>
<td>触摸控制器I2C时钟SCL</td>
</tr>
<tr>
<td>17</td>
<td>外部中断</td>
</tr>
<tr>
<td>18</td>
<td>显示屏复位</td>
</tr>
</table>

<a id="hardware-requirements"></a>

## 硬件要求（Hardware Requirements）：

支持的Renesas RA开发板：EK-RA8D1；需要1块RA开发板及1根Micro USB线。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield=rtkmipilcdb00000be，例如：

```text
# From the root of the zephyr repository
west build -b ek_ra8d1 --shield rtkmipilcdb00000be tests/drivers/display/display_read_write
```

---

[上一章](P160_RTKLCDPAR1S00001BE_Display.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P162_Seeed_W5500_Ethernet_Shield.md)
