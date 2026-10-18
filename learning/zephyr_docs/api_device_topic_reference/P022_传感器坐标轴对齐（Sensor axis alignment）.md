---
id: learning.zephyr-docs.api-device-topic-reference.page-22
title: 传感器坐标轴对齐（Sensor axis alignment）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__axis__align__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_传感器坐标轴对齐（Sensor axis alignment）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__axis__align__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

在设备树中重新映射传感器坐标轴时使用的共享常量。

<a id="details"></a>

在设备树中重新映射传感器坐标轴时使用的共享常量。

<a id="header-files"></a>
<a id="files"></a>

## 22.1\_文件（Files）

<a id="r_sensor_5Faxis_5Falign_2Eh"></a>

```c
file sensor_axis_align.h
```

相关声明：[sensor_axis_align.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__axis__align_8h.html)。

sensor axis alignment的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 22.2\_坐标轴索引（Axis index）

设备树 `axis-align-x`、`axis-align-y` 和 `axis-align-z` 属性的取值。

<a id="r_gafdae0414687f21fb56bf1c686bf06ab7"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_X 0
```

相关声明：[SENSOR_AXIS_ALIGN_DT_X](#gafdae0414687f21fb56bf1c686bf06ab7)。

X 轴（X axis）。

<a id="r_gab8af40a6341913c267779ad6f4fb19fe"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_Y 1
```

相关声明：[SENSOR_AXIS_ALIGN_DT_Y](#gab8af40a6341913c267779ad6f4fb19fe)。

Y 轴（Y axis）。

<a id="r_ga22cf8de4997026cc61606fd9d4653d2c"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_Z 2
```

相关声明：[SENSOR_AXIS_ALIGN_DT_Z](#ga22cf8de4997026cc61606fd9d4653d2c)。

Z 轴（Z axis）。

## 22.3\_坐标轴方向（Axis direction）

设备树 `axis-align-x-sign`、`axis-align-y-sign` 和 `axis-align-z-sign` 属性的取值。

<a id="r_ga0284999ba6171b1bbb79fb8801594e86"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_NEG 0
```

相关声明：[SENSOR_AXIS_ALIGN_DT_NEG](#ga0284999ba6171b1bbb79fb8801594e86)。

负方向（negative direction）。

<a id="r_ga8be323d0ef1415e94838f807493b456e"></a>

```c
#define SENSOR_AXIS_ALIGN_DT_POS 2
```

相关声明：[SENSOR_AXIS_ALIGN_DT_POS](#ga8be323d0ef1415e94838f807493b456e)。

正方向（positive direction）。

## 22.4\_详细说明（Detailed Documentation）

<a id="ga0284999ba6171b1bbb79fb8801594e86"></a>

### `SENSOR_AXIS_ALIGN_DT_NEG`

```c
#define SENSOR_AXIS_ALIGN_DT_NEG 0
```

```c
#include <zephyr/dt-bindings/sensor/sensor_axis_align.h>
```

负方向（negative direction）。

<a id="ga8be323d0ef1415e94838f807493b456e"></a>

### `SENSOR_AXIS_ALIGN_DT_POS`

```c
#define SENSOR_AXIS_ALIGN_DT_POS 2
```

```c
#include <zephyr/dt-bindings/sensor/sensor_axis_align.h>
```

正方向（positive direction）。

<a id="gafdae0414687f21fb56bf1c686bf06ab7"></a>

### `SENSOR_AXIS_ALIGN_DT_X`

```c
#define SENSOR_AXIS_ALIGN_DT_X 0
```

```c
#include <zephyr/dt-bindings/sensor/sensor_axis_align.h>
```

X 轴（X axis）。

<a id="gab8af40a6341913c267779ad6f4fb19fe"></a>

### `SENSOR_AXIS_ALIGN_DT_Y`

```c
#define SENSOR_AXIS_ALIGN_DT_Y 1
```

```c
#include <zephyr/dt-bindings/sensor/sensor_axis_align.h>
```

Y 轴（Y axis）。

<a id="ga22cf8de4997026cc61606fd9d4653d2c"></a>

### `SENSOR_AXIS_ALIGN_DT_Z`

```c
#define SENSOR_AXIS_ALIGN_DT_Z 2
```

```c
#include <zephyr/dt-bindings/sensor/sensor_axis_align.h>
```

Z 轴（Z axis）。


## 22.5\_原页交叉引用（Cross References）

- [sensor_axis_align.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__axis__align_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P021_一次性可编程存储器（One Time Programmable Memory）.md) · [返回大纲](大纲.md) · [下一章](P023_视频流（Video Stream）.md)
