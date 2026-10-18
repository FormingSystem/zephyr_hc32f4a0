---
id: learning.zephyr-docs.boards-shields.page-95
title: MikroElektronika Ambient 2 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_ambient_2_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-ambient-2-click"></a>

<a id="mikroe-ambient-2-click-shield"></a>

# 第95章\_MikroElektronika Ambient 2 Click环境光扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_ambient_2_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[Ambient 2 Click](https://www.mikroe.com/ambient-2-click)是紧凑附加板，只测量光谱的可见部分，模拟人眼对光的感知。

扩展板采用TI OPT3001数字环境光传感器，带I2C及中断。光谱响应接近人眼明视觉响应，可抑制99%的红外光；分辨率0.01 lx，最大可检测照度83865.6 lx，有效动态范围23位，适合住宅及商业自动照明管理等环境光测量应用。

<a id="id1"></a>

[![官方原图：Ambient 2 Click](images/mikroe_ambient_2_click.webp)](images/mikroe_ambient_2_click.webp)

Ambient 2 Click环境光扩展板

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS插座，并为其I2C接口定义mikrobus_i2c节点标签的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=mikroe_ambient_2_click，例如：

```text
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 --shield mikroe_ambient_2_click samples/sensor/light_polling
```

<a id="references"></a>

## 参考资料（References）


- [Ambient 2 Click环境光扩展板](https://www.mikroe.com/ambient-2-click)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [ambient-2-click](https://www.mikroe.com/ambient-2-click)：HTTP Error 403: Forbidden。

---

[上一章](P094_MikroElektronika_Air_Quality_3_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P096_MikroElektronika_BLE_TINY_Click.md)
