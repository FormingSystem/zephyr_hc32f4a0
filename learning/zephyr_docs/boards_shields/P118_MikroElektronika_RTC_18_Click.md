---
id: learning.zephyr-docs.boards-shields.page-118
title: MikroElektronika RTC 18 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_rtc_18_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-rtc-18-click"></a>

<a id="mikroe-rtc-18-click-shield"></a>

# 第118章\_MikroElektronika RTC 18 Click时钟扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_rtc_18_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

RTC 18 Click采用Micro Crystal RV-3032-C7温度补偿实时时钟模块，提供I2C、支持闰年的计时、闹钟及中断，以及备份电池切换电路。

该RTC精度约±0.22秒／天，功耗极低，主电源断开后可用小型备份电池继续计时。

<a id="id3"></a>

更多信息见Mikroe RTC 18 Click [注1](#id2)。（[Mikroe RTC 18 click模块](https://www.mikroe.com/rtc-18-click)）

<a id="id1"></a>

![官方原图：MikroElektronika RTC 18 Click](images/rtc_18_click.webp)

MikroElektronika RTC 18 Click时钟扩展板，图片来源：MikroElektronika d.o.o.

<a id="requirements"></a>

## 前置要求（Requirements）

扩展板使用mikroBUS，目标板须定义mikrobus_i2c及mikrobus_header节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

```text
# From the root of the zephyr repository
west build -b <board> --shield mikroe_rtc_18_click samples/drivers/rtc/
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.mikroe.com/rtc-18-click](https://www.mikroe.com/rtc-18-click)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [rtc-18-click](https://www.mikroe.com/rtc-18-click)：HTTP Error 403: Forbidden。

---

[上一章](P117_MikroElektronika_RS485_Isolator_5_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P119_MikroElektronika_Stepper_18_Click.md)
