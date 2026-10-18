---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-6
title: FCX-MLDX5 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_FCX-MLDX5 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Angst+Pfister FCX-MLDX5 氧气（O2）传感器。

<a id="details"></a>

Angst+Pfister FCX-MLDX5 氧气（O2）传感器。

<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_fcx_5Fmldx5_2Eh"></a>

```c
file fcx_mldx5.h
```

相关声明：[fcx_mldx5.h](../api_file_configuration_reference/P026_zephyr__drivers__sensor__fcx_mldx5.h_文件参考.md)。

FCX-MLDX5传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.2\_枚举（Enumerations）

<a id="r_ga61852fad03f2a92a59a20cdc7bbbdd49"></a>

```c
enum sensor_attribute_fcx_mldx5 { SENSOR_ATTR_FCX_MLDX5_STATUS = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_FCX_MLDX5_RESET }
```

相关声明：[sensor_attribute_fcx_mldx5](#ga61852fad03f2a92a59a20cdc7bbbdd49)、[SENSOR_ATTR_FCX_MLDX5_STATUS](#gga61852fad03f2a92a59a20cdc7bbbdd49aac5a09e1192a54d29275ba7f3c9d52b7)、[SENSOR_ATTR_FCX_MLDX5_RESET](#gga61852fad03f2a92a59a20cdc7bbbdd49a59ad17024844d8904168256f8f153585)。

FCX-MLDX5 的自定义传感器属性（Custom Sensor Attributes）。

<a id="r_ga413367eb7215e5c3e509e3cd039d37b1"></a>

```c
enum fcx_mldx5_status { FCX_MLDX5_STATUS_STANDBY = 2 , FCX_MLDX5_STATUS_RAMP_UP = 3 , FCX_MLDX5_STATUS_RUN = 4 , FCX_MLDX5_STATUS_ERROR = 5 , FCX_MLDX5_STATUS_UNKNOWN }
```

相关声明：[fcx_mldx5_status](#ga413367eb7215e5c3e509e3cd039d37b1)、[FCX_MLDX5_STATUS_STANDBY](#gga413367eb7215e5c3e509e3cd039d37b1adb1e1c971bfaaeecc7d376291f021a00)、[FCX_MLDX5_STATUS_RAMP_UP](#gga413367eb7215e5c3e509e3cd039d37b1a9e08ae3cedf51bbeaccbd390990a6ad4)、[FCX_MLDX5_STATUS_RUN](#gga413367eb7215e5c3e509e3cd039d37b1a002a770d06574829304afba178f8a179)、[FCX_MLDX5_STATUS_ERROR](#gga413367eb7215e5c3e509e3cd039d37b1a94945852b893160875764c9d34915540)、[FCX_MLDX5_STATUS_UNKNOWN](#gga413367eb7215e5c3e509e3cd039d37b1aa9ec19b887f79f85bf7d61d824698ca7)。

传感器状态（Sensor Status）。

## 6.3\_详细说明（Detailed Documentation）

<a id="ga413367eb7215e5c3e509e3cd039d37b1"></a>

### `fcx_mldx5_status`

```c
enum fcx_mldx5_status
```

```c
#include <zephyr/drivers/sensor/fcx_mldx5.h>
```

传感器状态（Sensor Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FCX_MLDX5_STATUS_STANDBY` | 待机（Standby）：氧气（O2）传感器加热处于待机状态，无法测量 O2。 |
| `FCX_MLDX5_STATUS_RAMP_UP` | 升温（Ramp-up）：O2 传感器处于加热阶段，无法测量 O2。 |
| `FCX_MLDX5_STATUS_RUN` | 运行（Run）：O2 模块正常工作。 |
| `FCX_MLDX5_STATUS_ERROR` | 错误（Error）：O2 模块检测到系统错误，无法测量 O2。 |
| `FCX_MLDX5_STATUS_UNKNOWN` | 未知状态（Unknown status）：传感器不会发送此状态，驱动用它表示错误情况。 |

<a id="ga61852fad03f2a92a59a20cdc7bbbdd49"></a>

### `sensor_attribute_fcx_mldx5`

```c
enum sensor_attribute_fcx_mldx5
```

```c
#include <zephyr/drivers/sensor/fcx_mldx5.h>
```

FCX-MLDX5 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_FCX_MLDX5_STATUS` | 传感器状态（status）。`sensor_value.val1` 为传感器状态，参见 `fcx_mldx5_status` 枚举。 |
| `SENSOR_ATTR_FCX_MLDX5_RESET` | 复位传感器。 |


## 6.4\_原页交叉引用（Cross References）

- [fcx_mldx5.h](../api_file_configuration_reference/P026_zephyr__drivers__sensor__fcx_mldx5.h_文件参考.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga413367eb7215e5c3e509e3cd039d37b1adb1e1c971bfaaeecc7d376291f021a00"></a>
<a id="gga413367eb7215e5c3e509e3cd039d37b1a9e08ae3cedf51bbeaccbd390990a6ad4"></a>
<a id="gga413367eb7215e5c3e509e3cd039d37b1a002a770d06574829304afba178f8a179"></a>
<a id="gga413367eb7215e5c3e509e3cd039d37b1a94945852b893160875764c9d34915540"></a>
<a id="gga413367eb7215e5c3e509e3cd039d37b1aa9ec19b887f79f85bf7d61d824698ca7"></a>
<a id="gga61852fad03f2a92a59a20cdc7bbbdd49aac5a09e1192a54d29275ba7f3c9d52b7"></a>
<a id="gga61852fad03f2a92a59a20cdc7bbbdd49a59ad17024844d8904168256f8f153585"></a>

---

[上一章](P005_模拟器（Simulator）.md) · [返回大纲](大纲.md) · [下一章](P007_FDC2X1X API主题.md)
