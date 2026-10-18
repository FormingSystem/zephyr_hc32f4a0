---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-40
title: sensor_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_sensor\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：传感器（Sensor）驱动操作。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：传感器（Sensor）驱动操作。这是每个传感器驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_a2d230a976b19a699d132034f58bb2b6a"></a>

```c
sensor_attr_set_t attr_set
```

相关声明：[sensor_attr_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga38422ace4194a66a9a912a8ef1e088fb)、[attr_set](#a2d230a976b19a699d132034f58bb2b6a)。

可选（OPT）：设置传感器的属性。

<a id="r_a3e28950f844c3f8b8da5ba9ff8052e46"></a>

```c
sensor_attr_get_t attr_get
```

相关声明：[sensor_attr_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga00d05c82b46e56dca5f6e8f7f01c31b8)、[attr_get](#a3e28950f844c3f8b8da5ba9ff8052e46)。

可选（OPT）：获取传感器的属性。

<a id="r_a4708070fd6654ecbbe631819aba319bd"></a>

```c
sensor_trigger_set_t trigger_set
```

相关声明：[sensor_trigger_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#gad7f7a3d9e714cc16f23656ca06592aa4)、[trigger_set](#a4708070fd6654ecbbe631819aba319bd)。

可选（OPT）：启用传感器触发器，并设置触发处理函数。

<a id="r_a4b40e25b81fe070e2f6bdcf7f8a4a31f"></a>

```c
sensor_sample_fetch_t sample_fetch
```

相关声明：[sensor_sample_fetch_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#gacae110a4edb6f29dfb457cb1ea8d68c1)、[sample_fetch](#a4b40e25b81fe070e2f6bdcf7f8a4a31f)。

必需（REQ）：从传感器获取一个样本，并存储到驱动内部缓冲区。

<a id="r_a667b41bf51f2c7a6bb31713fbf889113"></a>

```c
sensor_channel_get_t channel_get
```

相关声明：[sensor_channel_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga5c9b5ed9097464562004b446856043fd)、[channel_get](#a667b41bf51f2c7a6bb31713fbf889113)。

必需（REQ）：从传感器设备获取一个读数。

<a id="r_a004f9d342805dc72249ab9b8c17a544b"></a>

```c
sensor_get_decoder_t get_decoder
```

相关声明：[sensor_get_decoder_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga21e407d552d140cfb6bfd0d9513c7d42)、[get_decoder](#a004f9d342805dc72249ab9b8c17a544b)。

可选（OPT）：获取传感器的解码器 API（decoder API）。

<a id="r_ae3ba0adeba21351e8f660896e5a0e702"></a>

```c
sensor_submit_t submit
```

相关声明：[sensor_submit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#gad77732c8f0ec5520cdd71c2829787981)、[submit](#ae3ba0adeba21351e8f660896e5a0e702)。

可选（OPT）：处理提交给此传感器的 RTIO 请求。

## 40.2\_详细说明（Detailed Documentation）

<a id="a3e28950f844c3f8b8da5ba9ff8052e46"></a>

### `attr_get`

```c
sensor_attr_get_t sensor_driver_api::attr_get
```

可选（OPT）：获取传感器的属性。

<a id="a2d230a976b19a699d132034f58bb2b6a"></a>

### `attr_set`

```c
sensor_attr_set_t sensor_driver_api::attr_set
```

可选（OPT）：设置传感器的属性。

<a id="a667b41bf51f2c7a6bb31713fbf889113"></a>

### `channel_get`

```c
sensor_channel_get_t sensor_driver_api::channel_get
```

必需（REQ）：从传感器设备获取一个读数。

<a id="a004f9d342805dc72249ab9b8c17a544b"></a>

### `get_decoder`

```c
sensor_get_decoder_t sensor_driver_api::get_decoder
```

可选（OPT）：获取传感器的解码器 API（decoder API）。

<a id="a4b40e25b81fe070e2f6bdcf7f8a4a31f"></a>

### `sample_fetch`

```c
sensor_sample_fetch_t sensor_driver_api::sample_fetch
```

必需（REQ）：从传感器获取一个样本，并存储到驱动内部缓冲区。

<a id="ae3ba0adeba21351e8f660896e5a0e702"></a>

### `submit`

```c
sensor_submit_t sensor_driver_api::submit
```

可选（OPT）：处理提交给此传感器的 RTIO 请求。

<a id="a4708070fd6654ecbbe631819aba319bd"></a>

### `trigger_set`

```c
sensor_trigger_set_t sensor_driver_api::trigger_set
```

可选（OPT）：启用传感器触发器，并设置触发处理函数。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [sensor_attr_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga38422ace4194a66a9a912a8ef1e088fb)
- [sensor_attr_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga00d05c82b46e56dca5f6e8f7f01c31b8)
- [sensor_trigger_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#gad7f7a3d9e714cc16f23656ca06592aa4)
- [sensor_sample_fetch_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#gacae110a4edb6f29dfb457cb1ea8d68c1)
- [sensor_channel_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga5c9b5ed9097464562004b446856043fd)
- [sensor_get_decoder_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#ga21e407d552d140cfb6bfd0d9513c7d42)
- [sensor_submit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html#gad77732c8f0ec5520cdd71c2829787981)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_sensor_decoder_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_sensor_game_rotation_vector_data_结构体.md)
