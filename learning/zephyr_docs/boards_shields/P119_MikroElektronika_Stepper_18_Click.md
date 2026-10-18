---
id: learning.zephyr-docs.boards-shields.page-119
title: MikroElektronika Stepper 18 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_stepper_18_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-stepper-18-click"></a>

<a id="mikroe-stepper-18-click-shield"></a>

# 第119章\_MikroElektronika Stepper 18 Click步进驱动扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_stepper_18_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Stepper 18 Click通过GPIO访问TI步进驱动器，并使用Microchip MCP4726 DAC控制电流。微步引脚由实体开关控制，Zephyr无法访问。驱动默认采用工作队列计时源。译注：原文首句型号写DRV426，末句写DRV8426，差异保留。

MCP4726兼容MCP4725驱动。

<a id="id3"></a>

更多信息见Mikroe Stepper 18 Click [注1](#id2)。（[Mikroe Stepper 18 click模块](https://www.mikroe.com/stepper-18-click)）

<a id="id1"></a>

![官方原图：MikroElektronika Stepper 18 Click](images/stepper_18_click.webp)

MikroElektronika Stepper 18 Click步进驱动扩展板，图片来源：MikroElektronika

<a id="requirements"></a>

## 前置要求（Requirements）

扩展板使用mikroBUS，目标板须定义mikrobus_i2c及mikrobus_header节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

```text
# From the root of the zephyr repository
west build -b <board> --shield mikroe_stepper_18_click samples/drivers/stepper/generic/
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.mikroe.com/stepper-18-click](https://www.mikroe.com/stepper-18-click)

## 译注

原文DRV426与DRV8426型号拼写不一致；细分设置由硬件决定，未写作Zephyr运行时功能。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [stepper-18-click](https://www.mikroe.com/stepper-18-click)：HTTP Error 403: Forbidden。

---

[上一章](P118_MikroElektronika_RTC_18_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P120_MikroElektronika_Stepper_19_Click.md)
