---
id: learning.zephyr-docs.boards-shields.page-160
title: RTKLCDPAR1S00001BE Display
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/rtklcdpar1s00001be/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rtklcdpar1s00001be-display"></a>

<a id="rtklcdpar1s00001be"></a>

# 第160章\_RTKLCDPAR1S00001BE显示屏（Display）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/rtklcdpar1s00001be/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

图形扩展板包含1024×600像素TFT彩色LCD，覆盖电容触摸层。

此显示屏使用40针排针连接器。

<a id="pins-assignment-of-the-renesas-rtklcdpar1s00001be-display"></a>

### Renesas RTKLCDPAR1S00001BE显示屏的引脚分配

<table>
<tr>
<th>连接器引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>1</td>
<td>显示屏背光使能</td>
</tr>
<tr>
<td>2</td>
<td>触摸控制器I2C数据SDA</td>
</tr>
<tr>
<td>3</td>
<td>外部中断</td>
</tr>
<tr>
<td>4</td>
<td>触摸控制器I2C时钟SCL</td>
</tr>
<tr>
<td>6</td>
<td>显示屏复位</td>
</tr>
</table>

<a id="hardware-requirements"></a>

## 硬件要求（Hardware Requirements）：

支持的Renesas RA开发板：EK-RA8P1


- 1块RA开发板
- 1根Micro USB线

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield=rtklcdpar1s00001be，例如：

```text
# From the root of the zephyr repository
west build -b ek_ra8p1/r7ka8p1kflcac/cm85 --shield rtklcdpar1s00001be tests/drivers/display/display_read_write
```

---

[上一章](P159_RTKAPPLCDMS02001BE_MIPI_Display.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P161_RTKMIPILCDB00000BE_MIPI_Display.md)
