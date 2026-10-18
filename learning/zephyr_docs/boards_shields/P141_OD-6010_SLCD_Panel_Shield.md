---
id: learning.zephyr-docs.boards-shields.page-141
title: OD-6010 SLCD Panel Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/od_6010/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="od-6010-slcd-panel-shield"></a>

<a id="od-6010-shield"></a>

# 第141章\_OD-6010分段LCD面板扩展板（SLCD Panel Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/od_6010/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

OD-6010为6位七段数字LCD面板，另有6个点指示器，设计用于分段LCD控制器。

显示特性：


- 显示类型：七段数码显示
- 6个数字位置，按数据手册从右到左编号1～6
- 每位7段，标为A、B、C、D、E、F及G
- 6个点指示器P1～P6，位于数字之间
- 4条公共端COM0～COM3，用于复用扫描
- 12条前面板段引脚，编号0～11

<a id="hardware-pinout"></a>

## 硬件引脚定义（Pinout）

OD-6010使用以下引脚到信号映射：

```text
     |PIN0|PIN1|PIN2|PIN3|PIN4|PIN5|PIN6|PIN7|PIN8|PIN9|PIN10|PIN11
-----+----+----+----+----+----+----+----+----+----+----+-----+-----
COM0 | 1A | P6 | 2A | P3 | 3A | P2 | 4A | P1 | 5A | P4 | 6A  | P5
COM1 | 1B | 1F | 2B | 2F | 3B | 3F | 4B | 4F | 5B | 5F | 6B  | 6F
COM2 | 1C | 1G | 2C | 2G | 3C | 3G | 4C | 4G | 5C | 5G | 6C  | 6G
COM3 | 1D | 1E | 2D | 2E | 3D | 3E | 4D | 4E | 5D | 5E | 6D  | 6E
```

<a id="segment-display-mapping"></a>

## 七段显示映射

6个数字位置均包含标为A～G的七段显示：

```text
 AAA
F   B
 GGG
E   C
 DDD
```

七段显示可表示：


- 数字0～9

<a id="display-layout"></a>

## 显示布局

面板从左到右排列为dig6～dig1。

```text
 __   __  P1  __  P2  __  P3  __   __
|__| |__|    |__|    |__|    |__| |__|
|__| |__| P4 |__| P5 |__| P6 |__| |__|
dig6 dig5    dig4    dig3    dig2 dig1
```

<a id="dot-indicators"></a>

## 点指示器（Dot Indicators）

6个点指示器P1～P6作为数字间分隔点，均由COM0驱动。P1～P3为上点，P4～P6为同一间隙的下点：


- P1：dig5与dig4之间的上点，间隙1，引脚7，COM0
- P2：dig4与dig3之间的上点，间隙2，引脚5，COM0
- P3：dig3与dig2之间的上点，间隙3，引脚3，COM0
- P4：dig5与dig4之间的下点，间隙1，引脚9，COM0
- P5：dig4与dig3之间的下点，间隙2，引脚11，COM0
- P6：dig3与dig2之间的下点，间隙3，引脚1，COM0

在数字位置写入冒号“:”会同时点亮该间隙上下两点；写入句点“.”只点亮下点。

---

[上一章](P140_NXP_S32K5XX-MB_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P142_Olimex_SHIELD-MIDI.md)
