---
id: learning.zephyr-docs.api-file-service-interface-reference.page-44
title: zephyr__sensing__sensing_sensor_types.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_zephyr\_\_sensing\_\_sensing\_sensor\_types.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

感知子系统（Sensing Subsystem）传感器类型定义的头文件。

查看此文件的源码。

<a id="details"></a>

感知子系统（Sensing Subsystem）传感器类型定义的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 44.1\_宏定义（Macros）

<a id="r_ga9f6bc03e84167bf0b1ae8ea4fe016223"></a>

```c
#define SENSING_SENSOR_TYPE_ALL 0xFFFF
```

相关声明：[SENSING_SENSOR_TYPE_ALL](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#ga9f6bc03e84167bf0b1ae8ea4fe016223)。

表示所有传感器的传感器类型。

<a id="define-members-0"></a>

### 光传感器（Light Sensors）

<a id="r_gaee0dce0047c15b65556f7a1444c93337"></a>

```c
#define SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT 0x41
```

相关声明：[SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#gaee0dce0047c15b65556f7a1444c93337)。

环境光传感器（Ambient Light Sensor）类型。

<a id="define-members-1"></a>

### 运动传感器（Motion Sensors）

<a id="r_ga6368e8d035eae53d153ebb9dd0c6871e"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D 0x73
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#ga6368e8d035eae53d153ebb9dd0c6871e)。

三维加速度计（3D Accelerometer）类型。

<a id="r_gaaa716f0ff9e8ba8fac8ff5a539d3f785"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D 0x76
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#gaaa716f0ff9e8ba8fac8ff5a539d3f785)。

三维陀螺仪（3D Gyrometer）类型。

<a id="r_gae562dc942a869d95703893d41dcc2373"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_MOTION_DETECTOR 0x77
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_MOTION_DETECTOR](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#gae562dc942a869d95703893d41dcc2373)。

运动检测器（Motion Detector）类型。

<a id="r_ga1dc895e135ec8a07efdfe5d196692898"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D 0x240
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#ga1dc895e135ec8a07efdfe5d196692898)。

未校准三维加速度计（Uncalibrated 3D Accelerometer）类型。

<a id="r_ga1db5105621424ea60ffbc07fe6c25ae3"></a>

```c
#define SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE 0x20B
```

相关声明：[SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#ga1db5105621424ea60ffbc07fe6c25ae3)。

铰链角度传感器（Hinge Angle Sensor）类型。

<a id="define-members-2"></a>

### 其他传感器（Other Sensors）

<a id="r_gac637e2b7d193603ffa150fa4876e96b9"></a>

```c
#define SENSING_SENSOR_TYPE_OTHER_CUSTOM 0xE1
```

相关声明：[SENSING_SENSOR_TYPE_OTHER_CUSTOM](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#gac637e2b7d193603ffa150fa4876e96b9)。

自定义传感器（Custom Sensor）类型。


## 44.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P760_sensing_sensor_types.h_源码浏览.md)
- [SENSING_SENSOR_TYPE_ALL](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#ga9f6bc03e84167bf0b1ae8ea4fe016223)
- [SENSING_SENSOR_TYPE_LIGHT_AMBIENTLIGHT](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#gaee0dce0047c15b65556f7a1444c93337)
- [SENSING_SENSOR_TYPE_MOTION_ACCELEROMETER_3D](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#ga6368e8d035eae53d153ebb9dd0c6871e)
- [SENSING_SENSOR_TYPE_MOTION_GYROMETER_3D](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#gaaa716f0ff9e8ba8fac8ff5a539d3f785)
- [SENSING_SENSOR_TYPE_MOTION_MOTION_DETECTOR](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#gae562dc942a869d95703893d41dcc2373)
- [SENSING_SENSOR_TYPE_MOTION_UNCALIB_ACCELEROMETER_3D](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#ga1dc895e135ec8a07efdfe5d196692898)
- [SENSING_SENSOR_TYPE_MOTION_HINGE_ANGLE](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#ga1db5105621424ea60ffbc07fe6c25ae3)
- [SENSING_SENSOR_TYPE_OTHER_CUSTOM](../api_vector_pipeline_topic_reference/P026_传感器类型——感知子系统（Sensor Types，Sensing）.md#gac637e2b7d193603ffa150fa4876e96b9)

<a id="header-details"></a>

---

[上一章](P043_zephyr__drivers__pwm__max2221x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P045_zephyr__drivers__sensor_clock.h_文件参考.md)
