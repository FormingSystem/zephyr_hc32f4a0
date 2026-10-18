---
id: learning.zephyr-docs.boards-shields.page-28
title: Adafruit LPS22 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_lps22/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-lps22-shield"></a>

<a id="adafruit-lps22"></a>

# 第28章\_Adafruit LPS22扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_lps22/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit LPS22气压扩展板采用意法半导体LPS22HB，带2个STEMMA QT连接器，可测量气压及温度。（[Adafruit LPS22 压力传感器 扩展板](https://learn.adafruit.com/adafruit-lps25-pressure-sensor)；[ST Microelectronics LPS22HB 压力传感器](https://www.st.com/en/mems-and-sensors/lps22hb.html)）

<a id="id1"></a>

![官方原图：Adafruit LPS22 Shield](images/adafruit_lps22.webp)

Adafruit LPS22扩展板（Shield），图片来源：Adafruit

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板可用于提供I2C连接器的开发板，例如STEMMA QT或Qwiic；目标板必须定义zephyr_i2c节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>扩展板引脚（Shield Pin）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>串行时钟（SCK）</td>
<td>LPS22 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>SDI</td>
<td>LPS22 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行数据输出（SDO）</td>
<td>LPS22 I2C地址调整</td>
</tr>
<tr>
<td>片选（CS）</td>
<td>LPS22模式选择，上拉时使用I2C</td>
</tr>
<tr>
<td>中断（INT）</td>
<td>LPS22中断输出</td>
</tr>
</table>

如何修改设备树见[st,lps22hb-press](../sensor_st_lis_lps_binding_reference/P021_st_lps22hb-press.md#std-dtcompatible-st-lps22hb-press)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_lps22，例如运行气压与温度传感器轮询示例：（[气压及温度传感器轮询示例](../sensors/P022_气压温度传感器轮询示例.md#pressure_polling)）

```text
# From the root of the zephyr repository
west build -b adafruit_feather_rp2040 --shield adafruit_lps22 samples/sensor/pressure_polling
west flash
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [lps22hb.html](https://www.st.com/en/mems-and-sensors/lps22hb.html)：HTTP Error 567: Unknown Status。

---

[上一章](P027_Adafruit_LIS3MDL_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P029_Adafruit_LTR-329_Shield.md)
