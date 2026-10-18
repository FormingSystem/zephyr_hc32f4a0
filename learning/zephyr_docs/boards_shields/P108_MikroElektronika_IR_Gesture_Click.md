---
id: learning.zephyr-docs.boards-shields.page-108
title: MikroElektronika IR Gesture Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_ir_gesture_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-ir-gesture-click"></a>

<a id="mikroe-ir-gesture-click-shield"></a>

# 第108章\_MikroElektronika IR Gesture Click红外手势扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_ir_gesture_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[IR Gesture Click](https://www.mikroe.com/ir-gesture-click)是支持非接触识别、环境光及接近感测的紧凑附加板。

它采用Avago Technologies APDS-9960数字接近、环境光、RGB及手势传感器，集成红外LED及4个方向的光电二极管。内部手势引擎在消除环境光影响的同时，推算附近物体速度、方向及距离，支持上下左右滑动及复杂组合手势。接近功能还可在人手靠近时自动唤醒手势引擎，适用于手势检测、颜色和环境光感测、机械开关替代等应用。

<a id="id1"></a>

[![官方原图：IR Gesture Click](images/mikroe_ir_gesture_click.webp)](images/mikroe_ir_gesture_click.webp)

IR Gesture Click红外手势扩展板

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS插座，并为其I2C接口定义mikrobus_i2c节点标签的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=mikroe_ir_gesture_click，例如：

```text
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 --shield mikroe_ir_gesture_click samples/sensor/apds9960 -- -DCONFIG_APDS9960_TRIGGER_GLOBAL_THREAD=y
```

<a id="references"></a>

## 参考资料（References）


- [IR Gesture Click红外手势扩展板](https://www.mikroe.com/ir-gesture-click)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [ir-gesture-click](https://www.mikroe.com/ir-gesture-click)：HTTP Error 403: Forbidden。

---

[上一章](P107_MikroElektronika_Illuminance_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P109_MikroElektronika_LIN_Click.md)
