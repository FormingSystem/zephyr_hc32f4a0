---
id: learning.zephyr-docs.boards-shields.page-21
title: Adafruit INA228 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_ina228/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-ina228-shield"></a>

<a id="adafruit-ina228"></a>

# 第21章\_Adafruit INA228扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_ina228/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit INA228高侧／低侧功率监测扩展板采用TI INA228，即I2C接口20位功率监测芯片，带2个STEMMA QT连接器，可在最高85 V直流共模电压下进行高侧或低侧测量，电流范围从毫安到安培。（[Adafruit INA228 高侧或低侧功率监测器](https://learn.adafruit.com/adafruit-ina228-i2c-power-monitor/)；[TI INA228 电流传感器](https://www.ti.com/product/INA228)）

<a id="id1"></a>

![官方原图：Adafruit INA228 Shield](images/adafruit_ina228.webp)

Adafruit INA228扩展板（Shield），图片来源：Adafruit

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
<td>INA228 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>INA228 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>ALRT</td>
<td>INA228报警输出ALERT</td>
</tr>
<tr>
<td>VIN-</td>
<td>电流检测负端</td>
</tr>
<tr>
<td>VIN+</td>
<td>电流检测正端</td>
</tr>
<tr>
<td>USB总线电源（VBUS）</td>
<td>电压检测（Voltage Sense）</td>
</tr>
</table>

如何修改设备树，例如调整采样平均，见[ti,ina228](../sensor_st_ti_power_capacitance_binding_reference/P022_ti_ina228.md#std-dtcompatible-ti-ina228)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_ina228，例如运行传感器Shell示例：（[传感器Shell（Sensor Shell）](../sensors/P025_传感器Shell示例.md#sensor_shell)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield adafruit_ina228 samples/sensor/sensor_shell
```

---

[上一章](P020_Adafruit_INA219_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_Adafruit_INA237_Shield.md)
