---
id: learning.zephyr-docs.api-file-system-power-reference.page-41
title: zephyr__drivers__sensor__tdk_apex.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tdk__apex_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_zephyr\_\_drivers\_\_sensor\_\_tdk\_apex.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tdk__apex_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TDK微机电系统（MEMS）传感器的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

TDK 微机电系统（MEMS）传感器的扩展公共 API（Extended Public API）。此传感器的部分能力与运行要求无法通过传感器驱动抽象层（Sensor Driver Abstraction）表达。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 41.1\_宏定义（Macros）

<a id="define-members-0"></a>

### TDK APEX 功能（Features）

<a id="r_ac1c25ab2f69390238daa82b5cb582bad"></a>

```c
#define TDK_APEX_DISABLE (0)
```

相关声明：[TDK_APEX_DISABLE](#ac1c25ab2f69390238daa82b5cb582bad)。

禁用 APEX 功能（Feature）。

<a id="r_a0dd9a01a81c985de9a3a1edd1d9f84a6"></a>

```c
#define TDK_APEX_PEDOMETER (1)
```

相关声明：[TDK_APEX_PEDOMETER](#a0dd9a01a81c985de9a3a1edd1d9f84a6)。

启用计步器（Pedometer）功能。

<a id="r_aa635dbac54613d9f389b0e45de63d274"></a>

```c
#define TDK_APEX_TILT (2)
```

相关声明：[TDK_APEX_TILT](#aa635dbac54613d9f389b0e45de63d274)。

启用倾斜检测（Tilt Detection）功能。

<a id="r_a5ebd1faf982dd9a4b5b13bda71927afb"></a>

```c
#define TDK_APEX_SMD (3)
```

相关声明：[TDK_APEX_SMD](#a5ebd1faf982dd9a4b5b13bda71927afb)。

启用显著运动检测器（Significant Motion Detector，SMD）功能。

<a id="r_adad62736e0caaa3e2d01a810ef180b8a"></a>

```c
#define TDK_APEX_WOM (4)
```

相关声明：[TDK_APEX_WOM](#adad62736e0caaa3e2d01a810ef180b8a)。

启用运动唤醒（Wake on Motion，WoM）功能。

<a id="r_a3a828218b7ad4684983aeb5304dd0796"></a>

```c
#define TDK_APEX_TAP (5)
```

相关声明：[TDK_APEX_TAP](#a3a828218b7ad4684983aeb5304dd0796)。

启用敲击手势检测（TAP Gesture Detection）功能。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 41.2\_枚举（Enumerations）

<a id="r_a944436d98a2aea1f93977a2d0738d959"></a>

```c
enum sensor_channel_tdk_apex { SENSOR_CHAN_APEX_MOTION = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_tdk_apex](#a944436d98a2aea1f93977a2d0738d959)、[SENSOR_CHAN_APEX_MOTION](#a944436d98a2aea1f93977a2d0738d959a5181bce02684391a151723bbd7f86af5)。

支持 APEX 功能的 TDK MEMS 扩展传感器通道（Extended Sensor Channel）。

## 41.3\_详细说明（Detailed Documentation）

<a id="ac1c25ab2f69390238daa82b5cb582bad"></a>

### `TDK_APEX_DISABLE`

```c
#define TDK_APEX_DISABLE (0)
```

禁用 APEX 功能（Feature）。

<a id="a0dd9a01a81c985de9a3a1edd1d9f84a6"></a>

### `TDK_APEX_PEDOMETER`

```c
#define TDK_APEX_PEDOMETER (1)
```

启用计步器（Pedometer）功能。

<a id="a5ebd1faf982dd9a4b5b13bda71927afb"></a>

### `TDK_APEX_SMD`

```c
#define TDK_APEX_SMD (3)
```

启用显著运动检测器（Significant Motion Detector，SMD）功能。

<a id="a3a828218b7ad4684983aeb5304dd0796"></a>

### `TDK_APEX_TAP`

```c
#define TDK_APEX_TAP (5)
```

启用敲击手势检测（TAP Gesture Detection）功能。

<a id="aa635dbac54613d9f389b0e45de63d274"></a>

### `TDK_APEX_TILT`

```c
#define TDK_APEX_TILT (2)
```

启用倾斜检测（Tilt Detection）功能。

<a id="adad62736e0caaa3e2d01a810ef180b8a"></a>

### `TDK_APEX_WOM`

```c
#define TDK_APEX_WOM (4)
```

启用运动唤醒（Wake on Motion，WoM）功能。

<a id="a944436d98a2aea1f93977a2d0738d959"></a>

### `sensor_channel_tdk_apex`

```c
enum sensor_channel_tdk_apex
```

支持 APEX 功能的 TDK MEMS 扩展传感器通道（Extended Sensor Channel）。

这里公开 TDK MEMS 的传感器通道（Sensor Channel），用于获取 APEX 功能数据。

TDK MEMS 的 APEX（Advanced Pedometer and Event Detection – neXt gen，下一代高级计步与事件检测）包括以下功能：

- 计步器（Pedometer）：跟踪步数。
- 倾斜检测（Tilt Detection）：检测倾斜角是否超过 35 度。
- 运动唤醒（Wake on Motion，WoM）：在加速度计采样超过可编程阈值时检测到运动；该运动事件可用于使设备从休眠模式（Sleep Mode）开始工作。
- 显著运动检测器（Significant Motion Detector，SMD）：根据加速度计数据检测显著运动。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_APEX_MOTION` | APEX 功能（Features）。 |


## 41.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P860_tdk_apex.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a944436d98a2aea1f93977a2d0738d959a5181bce02684391a151723bbd7f86af5"></a>

---

[上一章](P040_zephyr__drivers__modem__st87mxx_app_services.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P042_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_toolchain.h_文件参考.md)
