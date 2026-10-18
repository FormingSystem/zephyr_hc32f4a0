---
id: learning.zephyr-docs.boards-shields.page-158
title: RTK7EKA6M3B00001BU Display
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/rtk7eka6m3b00001bu/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rtk7eka6m3b00001bu-display"></a>

<a id="rtk7eka6m3b00001bu"></a>

# 第158章\_RTK7EKA6M3B00001BU显示屏（Display）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/rtk7eka6m3b00001bu/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

图形扩展板包含4.3英寸480×272像素TFT彩色LCD，覆盖电容触摸层。

此显示屏使用40针排针连接器。

<a id="pins-assignment-of-the-renesas-rtk7eka6m3b00001bu-display"></a>

### Renesas RTK7EKA6M3B00001BU显示屏的引脚分配

<table>
<tr>
<th>连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>39</td>
<td>显示屏背光使能</td>
</tr>
<tr>
<td>21</td>
<td>触摸控制器I2C数据SDA</td>
</tr>
<tr>
<td>38</td>
<td>外部中断</td>
</tr>
<tr>
<td>5</td>
<td>触摸控制器I2C时钟SCL</td>
</tr>
<tr>
<td>35</td>
<td>显示屏复位</td>
</tr>
</table>

注意（Note）


- 用于EK-RA8D1时，需要EK-RA8D1转RTK7EKA6M3B00001BU显示适配器，才能将此扩展板连接到并行图形扩展端口J57。（[EK-RA8D1转RTK7EKA6M3B00001BU显示适配器（Display Adapter）](P063_EK-RA8D1_to_RTK7EKA6M3B00001BU_Display_Adapter.md#ek-ra8d1-rtk7eka6m3b00001bu)）

<a id="hardware-requirements"></a>

## 硬件要求（Hardware Requirements）：

支持的Renesas RA开发板：EK-RA8D1


- 1块RA开发板
- 1根Micro USB线

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield=rtk7eka6m3b00001bu，例如：

```text
# From the root of the zephyr repository
west build -b ek_ra8d1 --shield rtk7eka6m3b00001bu tests/drivers/display/display_read_write
```

---

[上一章](P157_RTK0EG0019B01002BJ_Capacitive_Touch_Application_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P159_RTKAPPLCDMS02001BE_MIPI_Display.md)
