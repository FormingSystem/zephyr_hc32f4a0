---
id: learning.zephyr-docs.boards-shields.page-59
title: DFRobot Gravity TM6605 Haptic Motor Driver Module
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/dfrobot_gravity_tm6605/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="dfrobot-gravity-tm6605-haptic-motor-driver-module"></a>

<a id="dfrobot-gravity-tm6605"></a>

# 第59章\_DFRobot Gravity TM6605触觉电机驱动模块（Haptic Motor Driver Module）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/dfrobot_gravity_tm6605/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

DFRobot Gravity TM6605模块DRI0056采用[Titan Micro Electronics TM6605](http://www.titanmec.com/)，驱动线性谐振执行器LRA，通过4针Gravity连接器提供I2C。（[DFRobot Gravity TM6605触觉电机驱动模块（Haptic Motor Driver Module）](https://www.dfrobot.com/product-3003.html)）

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板可用于提供Gravity、STEMMA QT或Qwiic等I2C连接器的开发板；目标板须定义zephyr_i2c节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>扩展板引脚（Shield Pin）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>TM6605 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>串行数据线（SDA）</td>
<td>TM6605 I2C数据线（SDA）</td>
</tr>
<tr>
<td>电源（VCC）</td>
<td>电源（Power Supply）</td>
</tr>
<tr>
<td>地（GND）</td>
<td>地（Ground）</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield dfrobot_gravity_tm6605，例如运行TM6605触觉驱动示例：（[TM6605 触觉驱动器](../hardware/P163_TM6605触觉驱动示例.md#tm6605)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield dfrobot_gravity_tm6605 samples/drivers/haptics/tm6605
```

---

[上一章](P058_DAC80508_Evaluation_Module.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P060_DH_electronics_DHSBC_RS485_CAN_Shield.md)
