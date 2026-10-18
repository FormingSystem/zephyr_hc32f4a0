---
id: learning.zephyr-docs.boards-shields.page-159
title: RTKAPPLCDMS02001BE MIPI Display
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/rtkapplcdms02001be/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rtkapplcdms02001be-mipi-display"></a>

<a id="rtkapplcdms02001be"></a>

# 第159章\_RTKAPPLCDMS02001BE MIPI显示屏（Display）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/rtkapplcdms02001be/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Focus LCDs RTKAPPLCDMS02001BE MIPI显示屏是5英寸1280×720像素TFT电容触摸面板。

此显示屏使用40针排针连接器。

<a id="pins-assignment-of-the-renesas-rtkapplcdms02001be-mipi-display"></a>

### Renesas RTKAPPLCDMS02001BE MIPI显示屏的引脚分配

<table>
<tr>
<th>连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>20</td>
<td>触摸控制器I2C数据SDA</td>
</tr>
<tr>
<td>21</td>
<td>显示屏背光使能</td>
</tr>
<tr>
<td>22</td>
<td>触摸控制器I2C时钟SCL</td>
</tr>
<tr>
<td>23</td>
<td>外部中断</td>
</tr>
<tr>
<td>24</td>
<td>显示屏复位</td>
</tr>
</table>

<a id="hardware-requirements"></a>

## 硬件要求（Hardware Requirements）：

支持的Renesas RZ开发板：EK-RZ/A3M；需要1块RZ开发板及1根USB-C线。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield=rtkapplcdms02001be，例如：

```text
# From the root of the zephyr repository
west build -b rza3m_ek --shield rtkapplcdms02001be tests/drivers/display/display_read_write
```

---

[上一章](P158_RTK7EKA6M3B00001BU_Display.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P160_RTKLCDPAR1S00001BE_Display.md)
