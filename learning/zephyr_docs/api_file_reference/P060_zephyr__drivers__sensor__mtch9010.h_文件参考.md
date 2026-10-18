---
id: learning.zephyr-docs.api-file-reference.page-60
title: zephyr__drivers__sensor__mtch9010.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2mtch9010_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_zephyr\_\_drivers\_\_sensor\_\_mtch9010.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2mtch9010_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/logging/log.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 60.1\_宏定义（Macros）

<a id="r_ad677f9a7375cae8cf6b86dcb0c69f629"></a>

```c
#define MTCH9010_MAX_RESULT 65535
```

相关声明：[MTCH9010_MAX_RESULT](#ad677f9a7375cae8cf6b86dcb0c69f629)。

<a id="r_a86ee1b6b92f193116819271e31b64997"></a>

```c
#define MTCH9010_MIN_RESULT 0
```

相关声明：[MTCH9010_MIN_RESULT](#a86ee1b6b92f193116819271e31b64997)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 60.2\_枚举（Enumerations）

<a id="r_a7e868bff47cb80d7993d527c85f8eec6"></a>

```c
enum sensor_channel_mtch9010 { SENSOR_CHAN_MTCH9010_OUT_STATE = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_MTCH9010_SW_OUT_STATE , SENSOR_CHAN_MTCH9010_REFERENCE_VALUE , SENSOR_CHAN_MTCH9010_THRESHOLD_VALUE , SENSOR_CHAN_MTCH9010_MEAS_RESULT , SENSOR_CHAN_MTCH9010_MEAS_DELTA , SENSOR_CHAN_MTCH9010_HEARTBEAT_ERROR_STATE }
```

相关声明：[sensor_channel_mtch9010](#a7e868bff47cb80d7993d527c85f8eec6)、[SENSOR_CHAN_MTCH9010_OUT_STATE](#a7e868bff47cb80d7993d527c85f8eec6a81f03d51cd3863d10aec276f6ca9b410)、[SENSOR_CHAN_MTCH9010_SW_OUT_STATE](#a7e868bff47cb80d7993d527c85f8eec6a26e2972fe91dbd1d164433eb62f519d1)、[SENSOR_CHAN_MTCH9010_REFERENCE_VALUE](#a7e868bff47cb80d7993d527c85f8eec6a59562ebe83f33fcc8e8aa1d39cc77368)、[SENSOR_CHAN_MTCH9010_THRESHOLD_VALUE](#a7e868bff47cb80d7993d527c85f8eec6a19a220dbc77399698ef9090d106a7ec5)、[SENSOR_CHAN_MTCH9010_MEAS_RESULT](#a7e868bff47cb80d7993d527c85f8eec6afc2a579b9ef34b4b087ea36e2c7cfae2)、[SENSOR_CHAN_MTCH9010_MEAS_DELTA](#a7e868bff47cb80d7993d527c85f8eec6a46b889a0dac6904fd8f6d8f4827694bb)、[SENSOR_CHAN_MTCH9010_HEARTBEAT_ERROR_STATE](#a7e868bff47cb80d7993d527c85f8eec6a407f4f15c183f4e7b3e165f29e30f987)。

## 60.3\_详细说明（Detailed Documentation）

<a id="ad677f9a7375cae8cf6b86dcb0c69f629"></a>

### `MTCH9010_MAX_RESULT`

```c
#define MTCH9010_MAX_RESULT 65535
```

<a id="a86ee1b6b92f193116819271e31b64997"></a>

### `MTCH9010_MIN_RESULT`

```c
#define MTCH9010_MIN_RESULT 0
```

<a id="a7e868bff47cb80d7993d527c85f8eec6"></a>

### `sensor_channel_mtch9010`

```c
enum sensor_channel_mtch9010
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_MTCH9010_OUT_STATE` |  |
| `SENSOR_CHAN_MTCH9010_SW_OUT_STATE` |  |
| `SENSOR_CHAN_MTCH9010_REFERENCE_VALUE` |  |
| `SENSOR_CHAN_MTCH9010_THRESHOLD_VALUE` |  |
| `SENSOR_CHAN_MTCH9010_MEAS_RESULT` |  |
| `SENSOR_CHAN_MTCH9010_MEAS_DELTA` |  |
| `SENSOR_CHAN_MTCH9010_HEARTBEAT_ERROR_STATE` |  |


## 60.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/drivers/uart.h](../uart_driver_reference/P002_UART驱动头文件源码.md)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [zephyr/logging/log.h](../log_core_reference/P004_日志公共头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2mtch9010_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a7e868bff47cb80d7993d527c85f8eec6a81f03d51cd3863d10aec276f6ca9b410"></a>
<a id="a7e868bff47cb80d7993d527c85f8eec6a26e2972fe91dbd1d164433eb62f519d1"></a>
<a id="a7e868bff47cb80d7993d527c85f8eec6a59562ebe83f33fcc8e8aa1d39cc77368"></a>
<a id="a7e868bff47cb80d7993d527c85f8eec6a19a220dbc77399698ef9090d106a7ec5"></a>
<a id="a7e868bff47cb80d7993d527c85f8eec6afc2a579b9ef34b4b087ea36e2c7cfae2"></a>
<a id="a7e868bff47cb80d7993d527c85f8eec6a46b889a0dac6904fd8f6d8f4827694bb"></a>
<a id="a7e868bff47cb80d7993d527c85f8eec6a407f4f15c183f4e7b3e165f29e30f987"></a>

---

[上一章](P059_zephyr__drivers__sensor__it8xxx2_vcmp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P061_zephyr__net__dsa_tag.h_文件参考.md)
