---
id: learning.zephyr-docs.boards-shields.page-39
title: Adafruit VEML7700 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_veml7700/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-veml7700-shield"></a>

<a id="adafruit-veml7700"></a>

# 第39章\_Adafruit VEML7700扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_veml7700/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit VEML7700照度扩展板采用Vishay VEML7700高精度环境光传感器，带2个STEMMA QT连接器，测量范围0～140000 lx。传感器有顶视及侧视两个版本，Adafruit均有销售，此定义兼容两者。（[Adafruit VEML7700 照度传感器 扩展板](https://learn.adafruit.com/adafruit-veml7700)；[Vishay VEML7700 高精度环境光传感器](https://www.vishay.com/en/product/84286/)）

<a id="id1"></a>

![官方原图：Adafruit VEML7700 Shield](images/adafruit_veml7700.webp)

Adafruit VEML7700扩展板，顶视版本；图片来源：Adafruit

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
<td>VEML7700 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>VEML7700 I2C时钟线（SCL）</td>
</tr>
</table>

如何修改设备树，例如启用节能模式，见[vishay,veml7700](../sensor_ti_vishay_wurth_sensing_binding_reference/P016_vishay_veml7700.md#std-dtcompatible-vishay-veml7700)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_veml7700，例如运行通用光照传感器轮询示例：（[通用光照传感器轮询（Generic Light Sensor Polling）](../sensors/P019_光照传感器轮询示例.md#light_sensor_polling)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield adafruit_veml7700 samples/sensor/light_polling
```

---

[上一章](P038_Adafruit_VCNL4040_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P040_Adafruit_WINC1500_Wifi_Shield.md)
