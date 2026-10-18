---
id: learning.zephyr-docs.boards-shields.page-107
title: MikroElektronika Illuminance Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_illuminance_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-illuminance-click"></a>

<a id="mikroe-illuminance-click-shield"></a>

# 第107章\_MikroElektronika Illuminance Click照度扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_illuminance_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[Illuminance Click](https://www.mikroe.com/illuminance-click)模拟人眼感光，采用ams OSRAM TSL2583高灵敏度光数转换器，通过I2C输出光强数字值。单个CMOS芯片集成宽带可见光／红外光电二极管及红外光电二极管，在16位有效动态范围及16位分辨率下提供接近人眼明视觉的响应，适用于通用光照感测，以延长电池寿命并优化不同照明下的显示效果。

<a id="id1"></a>

[![官方原图：Illuminance Click](images/mikroe_illuminance_click.webp)](images/mikroe_illuminance_click.webp)

Illuminance Click照度扩展板

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS插座，并为其I2C接口定义mikrobus_i2c节点标签的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=mikroe_illuminance_click，例如：

```text
# From the root of the zephyr repository
west build -b mikroe_quail --shield mikroe_illuminance_click samples/sensor/light_polling
```

原文此处指向[ams,tsl2561](../sensor_ams_aosong_bosch_binding_reference/P008_ams_tsl2561.md#std-dtcompatible-ams-tsl2561)及TSL2561的绑定属性，例如增益和积分时间；前文器件为TSL2583，型号差异保留。

<a id="references"></a>

## 参考资料（References）


- [Illuminance Click照度扩展板](https://www.mikroe.com/illuminance-click)

## 译注

概述传感器型号为TSL2583，绑定链接为tsl2561，按来源保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [illuminance-click](https://www.mikroe.com/illuminance-click)：HTTP Error 403: Forbidden。

---

[上一章](P106_MikroElektronika_H_Bridge_4_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P108_MikroElektronika_IR_Gesture_Click.md)
