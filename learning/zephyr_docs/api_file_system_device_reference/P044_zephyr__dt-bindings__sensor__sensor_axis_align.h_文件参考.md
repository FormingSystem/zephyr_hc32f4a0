---
id: learning.zephyr-docs.api-file-system-device-reference.page-44
title: zephyr__dt-bindings__sensor__sensor_axis_align.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor__axis__align_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_zephyr\_\_dt-bindings\_\_sensor\_\_sensor\_axis\_align.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensor__axis__align_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

sensor axis alignment的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

sensor axis alignment的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 44.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 坐标轴索引（Axis index）

设备树 `axis-align-x`、`axis-align-y` 和 `axis-align-z` 属性的取值。

<a id="r_gafdae0414687f21fb56bf1c686bf06ab7"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_X 0
```

相关声明：[SENSOR_AXIS_ALIGN_DT_X](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#gafdae0414687f21fb56bf1c686bf06ab7)。

X 轴（X axis）。

<a id="r_gab8af40a6341913c267779ad6f4fb19fe"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_Y 1
```

相关声明：[SENSOR_AXIS_ALIGN_DT_Y](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#gab8af40a6341913c267779ad6f4fb19fe)。

Y 轴（Y axis）。

<a id="r_ga22cf8de4997026cc61606fd9d4653d2c"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_Z 2
```

相关声明：[SENSOR_AXIS_ALIGN_DT_Z](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#ga22cf8de4997026cc61606fd9d4653d2c)。

Z 轴（Z axis）。

<a id="define-members-1"></a>

### 坐标轴方向（Axis direction）

设备树 `axis-align-x-sign`、`axis-align-y-sign` 和 `axis-align-z-sign` 属性的取值。

<a id="r_ga0284999ba6171b1bbb79fb8801594e86"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_NEG 0
```

相关声明：[SENSOR_AXIS_ALIGN_DT_NEG](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#ga0284999ba6171b1bbb79fb8801594e86)。

负方向（negative direction）。

<a id="r_ga8be323d0ef1415e94838f807493b456e"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_POS 2
```

相关声明：[SENSOR_AXIS_ALIGN_DT_POS](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#ga8be323d0ef1415e94838f807493b456e)。

正方向（positive direction）。


## 44.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P766_sensor_axis_align.h_源码浏览.md)
- [SENSOR_AXIS_ALIGN_DT_X](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#gafdae0414687f21fb56bf1c686bf06ab7)
- [SENSOR_AXIS_ALIGN_DT_Y](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#gab8af40a6341913c267779ad6f4fb19fe)
- [SENSOR_AXIS_ALIGN_DT_Z](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#ga22cf8de4997026cc61606fd9d4653d2c)
- [SENSOR_AXIS_ALIGN_DT_NEG](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#ga0284999ba6171b1bbb79fb8801594e86)
- [SENSOR_AXIS_ALIGN_DT_POS](../api_device_topic_reference/P022_传感器坐标轴对齐（Sensor axis alignment）.md#ga8be323d0ef1415e94838f807493b456e)

<a id="header-details"></a>

---

[上一章](P043_zephyr__drivers__interrupt_controller__riscv_clic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P045_zephyr__dt-bindings__clock__sf32lb-clocks-common.h_文件参考.md)
