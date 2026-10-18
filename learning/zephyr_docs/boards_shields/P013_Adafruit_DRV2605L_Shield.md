---
id: learning.zephyr-docs.boards-shields.page-13
title: Adafruit DRV2605L Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_drv2605l/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-drv2605l-shield"></a>

<a id="adafruit-drv2605l"></a>

# 第13章\_Adafruit DRV2605L扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_drv2605l/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit DRV2605L触觉电机控制器扩展板采用TI DRV2605触觉驱动器，带2个STEMMA QT连接器；DRV2605L是DRV2605的低电压版本。（[Adafruit DRV2605L 触觉电机控制器 扩展板](https://learn.adafruit.com/adafruit-drv2605-haptic-controller-breakout)；[TI DRV2605 触觉驱动器](https://www.ti.com/product/DRV2605)）

<a id="id1"></a>

![官方原图：Adafruit DRV2605L Shield](images/adafruit_drv2605l.webp)

Adafruit DRV2605L扩展板（Shield），图片来源：Adafruit

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
<td>DRV2605 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>DRV2605 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>IN/TRIG</td>
<td>用于触发触觉效果的数字输入</td>
</tr>
</table>

触觉电机可以是偏心旋转质量（ERM）或线性谐振执行器（LRA）。本扩展板设备树默认指定ERM电机，因为Adafruit配售该类型电机；若使用LRA，须修改设备树，详情见[ti,drv2605](../sound_haptic_binding_reference/P017_ti_drv2605.md#std-dtcompatible-ti-drv2605)。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_drv2605l，例如运行DRV2605触觉驱动示例：（[DRV2605 触觉驱动器](../hardware/P162_DRV2605触觉驱动示例.md#drv2605)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield adafruit_drv2605l samples/drivers/haptics/drv2605
```

## 译注

默认设备树采用ERM电机；使用LRA时须按绑定文档修改。

---

[上一章](P012_Adafruit_DPS310_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_Adafruit_DS2484_Shield.md)
