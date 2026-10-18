---
id: learning.zephyr-docs.boards-shields.page-23
title: Adafruit INA3221 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_ina3221/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-ina3221-shield"></a>

<a id="adafruit-ina3221"></a>

# 第23章\_Adafruit INA3221扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_ina3221/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit INA3221三通道功率监测扩展板采用TI INA3221，带2个STEMMA QT连接器，可测量3路电流及总线电压。（[Adafruit INA3221 三通道功率监测器 扩展板](https://learn.adafruit.com/adafruit-ina3221-breakout)；[TI INA3221 电流传感器](https://www.ti.com/product/INA3221)）

<a id="id1"></a>

![官方原图：Adafruit INA3221 Shield](images/adafruit_ina3221.webp)

Adafruit INA3221扩展板（Shield），图片来源：Adafruit

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
<td>串行时钟线（SCL）</td>
<td>I2C串行时钟（SCL）</td>
</tr>
<tr>
<td>串行数据线（SDA）</td>
<td>I2C串行数据（SDA）</td>
</tr>
<tr>
<td>VIN3+</td>
<td>通道3电流检测正端</td>
</tr>
<tr>
<td>VIN3-</td>
<td>通道3电流检测负端</td>
</tr>
<tr>
<td>VIN2+</td>
<td>通道2电流检测正端</td>
</tr>
<tr>
<td>VIN2-</td>
<td>通道2电流检测负端</td>
</tr>
<tr>
<td>VIN1+</td>
<td>通道1电流检测正端</td>
</tr>
<tr>
<td>VIN1-</td>
<td>通道1电流检测负端</td>
</tr>
<tr>
<td>WRN</td>
<td>电流值中断</td>
</tr>
<tr>
<td>CRI</td>
<td>过流中断</td>
</tr>
<tr>
<td>TC</td>
<td>时序控制中断</td>
</tr>
<tr>
<td>VALID</td>
<td>电源有效中断</td>
</tr>
<tr>
<td>VPU</td>
<td>VALID引脚上拉电压</td>
</tr>
</table>

如何修改设备树，例如调整采样平均，见[ti,ina3221](../sensor_st_ti_power_capacitance_binding_reference/P027_ti_ina3221.md#std-dtcompatible-ti-ina3221)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_ina3221，例如运行传感器Shell示例：（[传感器Shell（Sensor Shell）](../sensors/P025_传感器Shell示例.md#sensor_shell)）

```text
# From the root of the zephyr repository
west build -b adafruit_feather_canbus_rp2040 --shield adafruit_ina3221 samples/sensor/sensor_shell
west flash
```

用Shell命令显示通道1的电压、电流及功率，本例电压及电流约为5 V和3 mA：

```text
uart:~$ sensor get ina3221@40
channel type=33(voltage) index=0 shift=3 num_samples=1 value=63920453436ns (5.079999)
channel type=35(current) index=0 shift=3 num_samples=1 value=63920453436ns (0.003199)
channel type=36(power) index=0 shift=3 num_samples=1 value=63920453436ns (0.016255)
```

用以下命令将通道1改为通道2：

```text
uart:~$ sensor attr_set ina3221@40 voltage 19 2
```

---

[上一章](P022_Adafruit_INA237_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P024_Adafruit_ISM330DHCX_Shield.md)
