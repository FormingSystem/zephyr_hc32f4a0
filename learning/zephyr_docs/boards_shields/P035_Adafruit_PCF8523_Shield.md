---
id: learning.zephyr-docs.boards-shields.page-35
title: Adafruit PCF8523 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_pcf8523/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-pcf8523-shield"></a>

<a id="adafruit-pcf8523"></a>

# 第35章\_Adafruit PCF8523扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_pcf8523/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit PCF8523实时时钟扩展板采用NXP PCF8523，带2个Qwiic连接器及CR1220、3 V备份纽扣电池。（[Adafruit PCF8523 实时时钟 扩展板](https://learn.adafruit.com/adafruit-pcf8523-real-time-clock)；[NXP PCF8523 实时时钟](https://www.nxp.com/products/analog-and-mixed-signal/real-time-clocks/100-na-real-time-clock-calendar-with-battery-backup:PCF8523)）

<a id="id1"></a>

![官方原图：Adafruit PCF8523 Shield](images/adafruit_pcf8523.webp)

Adafruit PCF8523扩展板（Shield），图片来源：Adafruit

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
<td>串行数据线（SDA）</td>
<td>PCF8523 I2C数据SDA，也连接Qwiic接口</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>PCF8523 I2C时钟SCL，也连接Qwiic接口</td>
</tr>
<tr>
<td>SQW</td>
<td>PCF8523 INT/CLK中断或方波输出</td>
</tr>
</table>

使用PCF8523中断输出时，须将扩展板SQW接到微控制器板合适的GPIO，并修改设备树设置；可用选项见[nxp,pcf8523](../microchip_microcrystal_nxp_rtc_binding_reference/P016_nxp_pcf8523.md#std-dtcompatible-nxp-pcf8523)。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_pcf8523，例如运行实时时钟RTC示例：（[实时时钟（RTC）](../timer_reference/P066_实时时钟示例.md#rtc)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield adafruit_pcf8523 samples/drivers/rtc
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [100-na-real-time-clock-calendar-with-battery-backup:PCF8523](https://www.nxp.com/products/analog-and-mixed-signal/real-time-clocks/100-na-real-time-clock-calendar-with-battery-backup:PCF8523)：HTTP Error 404: Not Found。

---

[上一章](P034_Adafruit_16-channel_PWM_Servo_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P036_Adafruit_SHT40_SHT41_and_SHT45_Shields.md)
