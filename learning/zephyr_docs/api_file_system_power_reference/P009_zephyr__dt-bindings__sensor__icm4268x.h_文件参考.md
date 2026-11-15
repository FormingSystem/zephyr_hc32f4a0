---
id: learning.zephyr-docs.api-file-system-power-reference.page-9
title: zephyr__dt-bindings__sensor__icm4268x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2icm4268x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_sensor\_\_icm4268x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2icm4268x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TDK InvenSense ICM4268x惯性测量单元（IMUs）共享的设备树绑定常量。

<a id="details"></a>

```c
#include "sensor_axis_align.h"
```

查看此文件的源码。

TDK InvenSense ICM4268x惯性测量单元（IMUs）共享的设备树绑定常量。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计电源模式（Accelerometer Power Modes）

设备树属性（Devicetree Property）`accel-pwr-mode` 的取值。

<a id="r_gaf62125a80155dc35e6e4f2515e8612fb"></a>

```c
#define ICM4268X_DT_ACCEL_OFF 0
```

相关声明：[ICM4268X_DT_ACCEL_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf62125a80155dc35e6e4f2515e8612fb)。

已断电（Powered Down）。

<a id="r_ga57ec4d12a7591211a0a0b86bc82fe231"></a>

```c
#define ICM4268X_DT_ACCEL_LP 2
```

相关声明：[ICM4268X_DT_ACCEL_LP](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga57ec4d12a7591211a0a0b86bc82fe231)。

低功耗模式（Low-power Mode）。

<a id="r_ga15803e78f53d4cd6b1a73977d9a2d7f2"></a>

```c
#define ICM4268X_DT_ACCEL_LN 3
```

相关声明：[ICM4268X_DT_ACCEL_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga15803e78f53d4cd6b1a73977d9a2d7f2)。

低噪声模式（Low-noise Mode）。

<a id="define-members-1"></a>

### 陀螺仪电源模式（Gyroscope Power Modes）

设备树属性（Devicetree Property）`gyro-pwr-mode` 的取值。

<a id="r_ga0ed5ffc1cad9f3a93fc6b35481a6bc0f"></a>

```c
#define ICM4268X_DT_GYRO_OFF 0
```

相关声明：[ICM4268X_DT_GYRO_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0ed5ffc1cad9f3a93fc6b35481a6bc0f)。

已断电（Powered Down）。

<a id="r_gac39cbda0e1ea17f416a6b93c87a8307f"></a>

```c
#define ICM4268X_DT_GYRO_STANDBY 1
```

相关声明：[ICM4268X_DT_GYRO_STANDBY](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac39cbda0e1ea17f416a6b93c87a8307f)。

待机（Standby）。

<a id="r_ga2dbd021704b4480f8529e63e1a6c7bbf"></a>

```c
#define ICM4268X_DT_GYRO_LN 3
```

相关声明：[ICM4268X_DT_GYRO_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga2dbd021704b4480f8529e63e1a6c7bbf)。

低噪声模式（Low-noise Mode）。

<a id="define-members-2"></a>

### 加速度计数据速率选项（Accelerometer Data Rate Options）

设备树（Devicetree）属性 `accel-odr` 的取值。

<a id="r_ga7d921e728429957ebf06b39b28e4aee4"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_32000 1
```

相关声明：[ICM4268X_DT_ACCEL_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d921e728429957ebf06b39b28e4aee4)。

频率（Frequency）：32 kHz。

<a id="r_ga1b30ff257f338277142adad272d3fb61"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_16000 2
```

相关声明：[ICM4268X_DT_ACCEL_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga1b30ff257f338277142adad272d3fb61)。

频率（Frequency）：16 kHz。

<a id="r_gac28b1215367f9a571aa3db1cf1760649"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_8000 3
```

相关声明：[ICM4268X_DT_ACCEL_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac28b1215367f9a571aa3db1cf1760649)。

频率（Frequency）：8 kHz。

<a id="r_ga6124a2372e403657672e838121b24016"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_4000 4
```

相关声明：[ICM4268X_DT_ACCEL_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga6124a2372e403657672e838121b24016)。

频率（Frequency）：4 kHz。

<a id="r_ga7711f8b4ce0e8c9375a9ab054b4d3653"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_2000 5
```

相关声明：[ICM4268X_DT_ACCEL_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7711f8b4ce0e8c9375a9ab054b4d3653)。

频率（Frequency）：2 kHz。

<a id="r_ga002b562a990715f7718aa008b2025cbb"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_1000 6
```

相关声明：[ICM4268X_DT_ACCEL_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga002b562a990715f7718aa008b2025cbb)。

频率（Frequency）：1 kHz。

<a id="r_gac057ecd6a55247301e311f89f16ccfef"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_200 7
```

相关声明：[ICM4268X_DT_ACCEL_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac057ecd6a55247301e311f89f16ccfef)。

频率：200 Hz。

<a id="r_ga018b11db318c78827ac5ddb1d28354bf"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_100 8
```

相关声明：[ICM4268X_DT_ACCEL_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga018b11db318c78827ac5ddb1d28354bf)。

频率：100 Hz。

<a id="r_ga9c1b503304efbecd6e43998cd76fca3f"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_50 9
```

相关声明：[ICM4268X_DT_ACCEL_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga9c1b503304efbecd6e43998cd76fca3f)。

频率：50 Hz。

<a id="r_ga0318e0340cb82663ddc779c5928163ca"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_25 10
```

相关声明：[ICM4268X_DT_ACCEL_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0318e0340cb82663ddc779c5928163ca)。

频率：25 Hz。

<a id="r_gadd58206e7413d43fb5d132116a7a5365"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_12_5 11
```

相关声明：[ICM4268X_DT_ACCEL_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gadd58206e7413d43fb5d132116a7a5365)。

频率：12.5 Hz。

<a id="r_gad20d9cfa5bb90c7a165abf9f7ab3664f"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_6_25 12
```

相关声明：[ICM4268X_DT_ACCEL_ODR_6_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gad20d9cfa5bb90c7a165abf9f7ab3664f)。

频率：6.25 Hz。

<a id="r_ga3e1a90cbb6580992ed201ecb0b5345d0"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_3_125 13
```

相关声明：[ICM4268X_DT_ACCEL_ODR_3_125](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3e1a90cbb6580992ed201ecb0b5345d0)。

频率（Frequency）：3.125 Hz。

<a id="r_gab37631e21578afd1de24eaefc49d5aa6"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_1_5625 14
```

相关声明：[ICM4268X_DT_ACCEL_ODR_1_5625](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gab37631e21578afd1de24eaefc49d5aa6)。

频率（Frequency）：1.5625 Hz。

<a id="r_ga19a61dfae5899d0839cffb16194e60e8"></a>

```c
#define ICM4268X_DT_ACCEL_ODR_500 15
```

相关声明：[ICM4268X_DT_ACCEL_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga19a61dfae5899d0839cffb16194e60e8)。

频率（Frequency）：500 Hz。

<a id="define-members-3"></a>

### 陀螺仪数据速率选项（Gyroscope Data Rate Options）

设备树属性（Devicetree Property）`gyro-odr` 的取值。

<a id="r_ga8cef750fe17171662da932b0123027ff"></a>

```c
#define ICM4268X_DT_GYRO_ODR_32000 1
```

相关声明：[ICM4268X_DT_GYRO_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8cef750fe17171662da932b0123027ff)。

频率（Frequency）：32 kHz。

<a id="r_ga8a1915f4ec22be71d0460b5e4b104f18"></a>

```c
#define ICM4268X_DT_GYRO_ODR_16000 2
```

相关声明：[ICM4268X_DT_GYRO_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8a1915f4ec22be71d0460b5e4b104f18)。

频率（Frequency）：16 kHz。

<a id="r_gaaea9abea12bd6fbfb5336d9cb523dd82"></a>

```c
#define ICM4268X_DT_GYRO_ODR_8000 3
```

相关声明：[ICM4268X_DT_GYRO_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaaea9abea12bd6fbfb5336d9cb523dd82)。

频率（Frequency）：8 kHz。

<a id="r_ga21d6c35ee4059840fe1a1f6e5b53f50a"></a>

```c
#define ICM4268X_DT_GYRO_ODR_4000 4
```

相关声明：[ICM4268X_DT_GYRO_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga21d6c35ee4059840fe1a1f6e5b53f50a)。

频率（Frequency）：4 kHz。

<a id="r_ga81483ad0a4a847460af6e3b34cde489e"></a>

```c
#define ICM4268X_DT_GYRO_ODR_2000 5
```

相关声明：[ICM4268X_DT_GYRO_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga81483ad0a4a847460af6e3b34cde489e)。

频率（Frequency）：2 kHz。

<a id="r_ga5d5738a58c499b1bb8853471ec3d357e"></a>

```c
#define ICM4268X_DT_GYRO_ODR_1000 6
```

相关声明：[ICM4268X_DT_GYRO_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga5d5738a58c499b1bb8853471ec3d357e)。

频率（Frequency）：1 kHz。

<a id="r_ga37ed7fc033b31067f5331734e98ac906"></a>

```c
#define ICM4268X_DT_GYRO_ODR_200 7
```

相关声明：[ICM4268X_DT_GYRO_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga37ed7fc033b31067f5331734e98ac906)。

频率：200 Hz。

<a id="r_gaf79aa174e89c3c22128bd298cfab3805"></a>

```c
#define ICM4268X_DT_GYRO_ODR_100 8
```

相关声明：[ICM4268X_DT_GYRO_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf79aa174e89c3c22128bd298cfab3805)。

频率：100 Hz。

<a id="r_ga7d1438b46e72745204b0b37c57e57cf5"></a>

```c
#define ICM4268X_DT_GYRO_ODR_50 9
```

相关声明：[ICM4268X_DT_GYRO_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d1438b46e72745204b0b37c57e57cf5)。

频率：50 Hz。

<a id="r_ga3788cbbf8b8e7ccded755ab52a5abe53"></a>

```c
#define ICM4268X_DT_GYRO_ODR_25 10
```

相关声明：[ICM4268X_DT_GYRO_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3788cbbf8b8e7ccded755ab52a5abe53)。

频率：25 Hz。

<a id="r_ga319a7710d327b82b39cee2a9d2348702"></a>

```c
#define ICM4268X_DT_GYRO_ODR_12_5 11
```

相关声明：[ICM4268X_DT_GYRO_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga319a7710d327b82b39cee2a9d2348702)。

频率：12.5 Hz。

<a id="r_ga638d6c4de6d0eea72a31a14bdf18df01"></a>

```c
#define ICM4268X_DT_GYRO_ODR_500 15
```

相关声明：[ICM4268X_DT_GYRO_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga638d6c4de6d0eea72a31a14bdf18df01)。

频率（Frequency）：500 Hz。


## 9.2\_原页交叉引用（Cross References）

- [sensor_axis_align.h](../api_source_reference/P766_sensor_axis_align.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P203_icm4268x.h_源码浏览.md)
- [ICM4268X_DT_ACCEL_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf62125a80155dc35e6e4f2515e8612fb)
- [ICM4268X_DT_ACCEL_LP](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga57ec4d12a7591211a0a0b86bc82fe231)
- [ICM4268X_DT_ACCEL_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga15803e78f53d4cd6b1a73977d9a2d7f2)
- [ICM4268X_DT_GYRO_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0ed5ffc1cad9f3a93fc6b35481a6bc0f)
- [ICM4268X_DT_GYRO_STANDBY](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac39cbda0e1ea17f416a6b93c87a8307f)
- [ICM4268X_DT_GYRO_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga2dbd021704b4480f8529e63e1a6c7bbf)
- [ICM4268X_DT_ACCEL_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d921e728429957ebf06b39b28e4aee4)
- [ICM4268X_DT_ACCEL_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga1b30ff257f338277142adad272d3fb61)
- [ICM4268X_DT_ACCEL_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac28b1215367f9a571aa3db1cf1760649)
- [ICM4268X_DT_ACCEL_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga6124a2372e403657672e838121b24016)
- [ICM4268X_DT_ACCEL_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7711f8b4ce0e8c9375a9ab054b4d3653)
- [ICM4268X_DT_ACCEL_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga002b562a990715f7718aa008b2025cbb)
- [ICM4268X_DT_ACCEL_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac057ecd6a55247301e311f89f16ccfef)
- [ICM4268X_DT_ACCEL_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga018b11db318c78827ac5ddb1d28354bf)
- [ICM4268X_DT_ACCEL_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga9c1b503304efbecd6e43998cd76fca3f)
- [ICM4268X_DT_ACCEL_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0318e0340cb82663ddc779c5928163ca)
- [ICM4268X_DT_ACCEL_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gadd58206e7413d43fb5d132116a7a5365)
- [ICM4268X_DT_ACCEL_ODR_6_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gad20d9cfa5bb90c7a165abf9f7ab3664f)
- [ICM4268X_DT_ACCEL_ODR_3_125](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3e1a90cbb6580992ed201ecb0b5345d0)
- [ICM4268X_DT_ACCEL_ODR_1_5625](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gab37631e21578afd1de24eaefc49d5aa6)
- [ICM4268X_DT_ACCEL_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga19a61dfae5899d0839cffb16194e60e8)
- [ICM4268X_DT_GYRO_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8cef750fe17171662da932b0123027ff)
- [ICM4268X_DT_GYRO_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8a1915f4ec22be71d0460b5e4b104f18)
- [ICM4268X_DT_GYRO_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaaea9abea12bd6fbfb5336d9cb523dd82)
- [ICM4268X_DT_GYRO_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga21d6c35ee4059840fe1a1f6e5b53f50a)
- [ICM4268X_DT_GYRO_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga81483ad0a4a847460af6e3b34cde489e)
- [ICM4268X_DT_GYRO_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga5d5738a58c499b1bb8853471ec3d357e)
- [ICM4268X_DT_GYRO_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga37ed7fc033b31067f5331734e98ac906)
- [ICM4268X_DT_GYRO_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf79aa174e89c3c22128bd298cfab3805)
- [ICM4268X_DT_GYRO_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d1438b46e72745204b0b37c57e57cf5)
- [ICM4268X_DT_GYRO_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3788cbbf8b8e7ccded755ab52a5abe53)
- [ICM4268X_DT_GYRO_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga319a7710d327b82b39cee2a9d2348702)
- [ICM4268X_DT_GYRO_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga638d6c4de6d0eea72a31a14bdf18df01)

<a id="header-details"></a>

---

[上一章](P008_zephyr__drivers__mfd__adp5360.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__sensor__lis2dh.h_文件参考.md)
