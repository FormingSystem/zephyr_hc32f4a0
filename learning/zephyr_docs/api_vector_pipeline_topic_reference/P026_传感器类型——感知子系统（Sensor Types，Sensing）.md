---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-26
title: 传感器类型——感知子系统（Sensor Types，Sensing）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor__types.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_传感器类型——感知子系统（Sensor Types，Sensing）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor__types.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

感知子系统使用的传感器类型标识符。

<a id="details"></a>

感知子系统（Sensing Subsystem）使用的传感器类型标识符（Sensor Type Identifiers）。类型定义遵循人机接口设备（HID）标准：[HID 传感器用法提案](https://usb.org/sites/default/files/hutrr39b_0.pdf)。**待办（TODO）：**将添加更多类型。

<a id="header-files"></a>
<a id="files"></a>

## 26.1\_文件（Files）

<a id="r_sensing_5Fsensor_5Ftypes_2Eh"></a>

```c
file sensing_sensor_types.h
```

相关声明：[sensing_sensor_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h.html)。

感知子系统（Sensing Subsystem）传感器类型定义的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 26.2\_宏定义（Macros）

<a id="r_ga9f6bc03e84167bf0b1ae8ea4fe016223"></a>

```c
#define SENSING_SENSOR_TYPE_ALL 0xFFFF
```

相关声明：[SENSING_SENSOR_TYPE_ALL](#ga9f6bc03e84167bf0b1ae8ea4fe016223)。

表示所有传感器的传感器类型。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 26.3\_光传感器（Light Sensors）

<a id="r_gaee0dce0047c15b65556f7a1444c93337"></a>

```c
#define SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT 0x41
```

相关声明：[SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT](#gaee0dce0047c15b65556f7a1444c93337)。

环境光传感器（Ambient Light Sensor）类型。

## 26.4\_运动传感器（Motion Sensors）

<a id="r_ga6368e8d035eae53d153ebb9dd0c6871e"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D 0x73
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D](#ga6368e8d035eae53d153ebb9dd0c6871e)。

三维加速度计（3D Accelerometer）类型。

<a id="r_gaaa716f0ff9e8ba8fac8ff5a539d3f785"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D 0x76
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D](#gaaa716f0ff9e8ba8fac8ff5a539d3f785)。

三维陀螺仪（3D Gyrometer）类型。

<a id="r_gae562dc942a869d95703893d41dcc2373"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_MOTION_DETECTOR 0x77
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_MOTION_DETECTOR](#gae562dc942a869d95703893d41dcc2373)。

运动检测器（Motion Detector）类型。

<a id="r_ga1dc895e135ec8a07efdfe5d196692898"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D 0x240
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D](#ga1dc895e135ec8a07efdfe5d196692898)。

未校准三维加速度计（Uncalibrated 3D Accelerometer）类型。

<a id="r_ga1db5105621424ea60ffbc07fe6c25ae3"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE 0x20B
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE](#ga1db5105621424ea60ffbc07fe6c25ae3)。

铰链角度传感器（Hinge Angle Sensor）类型。

## 26.5\_其他传感器（Other Sensors）

<a id="r_gac637e2b7d193603ffa150fa4876e96b9"></a>

```c
#define SENSING_SENSOR_TYPE_OTHER_CUSTOM 0xE1
```

相关声明：[SENSING_SENSOR_TYPE_OTHER_CUSTOM](#gac637e2b7d193603ffa150fa4876e96b9)。

自定义传感器（Custom Sensor）类型。

## 26.6\_详细说明（Detailed Documentation）

<a id="ga9f6bc03e84167bf0b1ae8ea4fe016223"></a>

### `SENSING_SENSOR_TYPE_ALL`

```c
#define SENSING_SENSOR_TYPE_ALL 0xFFFF
```

```c
#include <zephyr/sensing/sensing_sensor_types.h>
```

表示所有传感器的传感器类型。

本宏定义表示所有传感器的传感器类型。

**说明（Note）**：**注意（Note）：**此值不是有效的传感器类型，而是用于表示所有传感器类型的哨兵值（Sentinel Value）。

<a id="gaee0dce0047c15b65556f7a1444c93337"></a>

### `SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT`

```c
#define SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT 0x41
```

```c
#include <zephyr/sensing/sensing_sensor_types.h>
```

环境光传感器（Ambient Light Sensor）类型。

<a id="ga6368e8d035eae53d153ebb9dd0c6871e"></a>

### `SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D`

```c
#define SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D 0x73
```

```c
#include <zephyr/sensing/sensing_sensor_types.h>
```

三维加速度计（3D Accelerometer）类型。

<a id="gaaa716f0ff9e8ba8fac8ff5a539d3f785"></a>

### `SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D`

```c
#define SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D 0x76
```

```c
#include <zephyr/sensing/sensing_sensor_types.h>
```

三维陀螺仪（3D Gyrometer）类型。

<a id="ga1db5105621424ea60ffbc07fe6c25ae3"></a>

### `SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE`

```c
#define SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE 0x20B
```

```c
#include <zephyr/sensing/sensing_sensor_types.h>
```

铰链角度传感器（Hinge Angle Sensor）类型。

<a id="gae562dc942a869d95703893d41dcc2373"></a>

### `SENSING_SENSOR_TYPE_MOTION_MOTION_DETECTOR`

```c
#define SENSING_SENSOR_TYPE_MOTION_MOTION_DETECTOR 0x77
```

```c
#include <zephyr/sensing/sensing_sensor_types.h>
```

运动检测器（Motion Detector）类型。

<a id="ga1dc895e135ec8a07efdfe5d196692898"></a>

### `SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D`

```c
#define SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D 0x240
```

```c
#include <zephyr/sensing/sensing_sensor_types.h>
```

未校准三维加速度计（Uncalibrated 3D Accelerometer）类型。

<a id="gac637e2b7d193603ffa150fa4876e96b9"></a>

### `SENSING_SENSOR_TYPE_OTHER_CUSTOM`

```c
#define SENSING_SENSOR_TYPE_OTHER_CUSTOM 0xE1
```

```c
#include <zephyr/sensing/sensing_sensor_types.h>
```

自定义传感器（Custom Sensor）类型。


## 26.7\_原页交叉引用（Cross References）

- [sensing_sensor_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h.html)
- [https://usb.org/sites/default/files/hutrr39b_0.pdf](https://usb.org/sites/default/files/hutrr39b_0.pdf)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P025_PCIe 主机消息信号中断（MSI）接口.md) · [返回大纲](大纲.md) · [下一章](P027_1-Wire 驱动后端 API（Driver Backend API）.md)
