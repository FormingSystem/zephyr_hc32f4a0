---
id: learning.zephyr-docs.boards-shields.page-10
title: Adafruit AW9523 GPIO Expander and LED Driver
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_aw9523/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-aw9523-gpio-expander-and-led-driver"></a>

<a id="adafruit-aw9523"></a>

# 第10章\_Adafruit AW9523 GPIO扩展器及LED驱动器

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_aw9523/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit AW9523提供16通道GPIO／LED控制器功能。（[Adafruit AW9523 GPIO扩展器及LED驱动器](https://learn.adafruit.com/adafruit-aw9523-gpio-expander-and-led-driver)）

<a id="id6"></a>

![官方原图：Adafruit AW9523](images/adafruit_aw9523.webp)

Adafruit AW9523，图片来源：Adafruit

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>扩展板引脚（Shield Pin）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>串行数据线（SDA）</td>
<td>AW9523B I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>AW9523B I2C时钟线（SCL）</td>
</tr>
<tr>
<td>INT，板上焊盘</td>
<td><a id="id1"></a><br><br>AW9523B中断输出<a href="#id3">注1</a></td>
</tr>
<tr>
<td>RST，板上焊盘</td>
<td><a id="id2"></a><br><br>AW9523B复位引脚<a href="#id4">注2</a></td>
</tr>
</table>

<a id="id3"></a>

〔[1](#id1)〕 若要接收中断，将INT接到SoC的GPIO，并在额外设备树覆盖文件的int-gpios属性中指定该GPIO。INT端必须上拉。

<a id="id4"></a>

〔[2](#id2)〕 若要从SoC控制复位引脚，将其接到SoC GPIO，并在额外覆盖文件中定义reset-gpios属性。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_aw9523。

---

[上一章](P009_Adafruit_APDS9960_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_Adafruit_Data_Logger_Shield.md)
