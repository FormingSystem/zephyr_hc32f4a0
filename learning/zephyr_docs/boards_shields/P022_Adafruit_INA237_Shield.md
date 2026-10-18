---
id: learning.zephyr-docs.boards-shields.page-22
title: Adafruit INA237 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_ina237/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-ina237-shield"></a>

<a id="adafruit-ina237"></a>

# 第22章\_Adafruit INA237扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_ina237/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit INA237直流电流、电压及功率监测扩展板采用TI INA237，带2个STEMMA QT连接器，可测量电流及总线电压。（[Adafruit INA237 直流电流、电压及功率监测传感器 扩展板](https://learn.adafruit.com/adafruit-ina237-dc-current-voltage-power-monitor)；[TI INA237 电流传感器](https://www.ti.com/product/INA237)）

<a id="id1"></a>

![官方原图：Adafruit INA237 Shield](images/adafruit_ina237.webp)

Adafruit INA237扩展板（Shield），图片来源：Adafruit

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
<td>INA237 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>INA237 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>ALRT</td>
<td>INA237报警输出ALERT</td>
</tr>
</table>

如何修改设备树，例如调整采样平均，见[ti,ina237](../sensor_st_ti_power_capacitance_binding_reference/P026_ti_ina237.md#std-dtcompatible-ti-ina237)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_ina237，例如运行传感器Shell示例：（[传感器Shell（Sensor Shell）](../sensors/P025_传感器Shell示例.md#sensor_shell)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield adafruit_ina237 samples/sensor/sensor_shell
```

---

[上一章](P021_Adafruit_INA228_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P023_Adafruit_INA3221_Shield.md)
