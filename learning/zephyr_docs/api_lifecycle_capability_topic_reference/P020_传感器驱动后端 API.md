---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-20
title: 传感器驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_传感器驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现传感器驱动（Sensor Driver）所需的 API 类型定义、回调签名（Callback Signatures）及其他辅助接口（Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 20.1\_数据结构（Data Structures）

<a id="r_sensor_5Fdriver_5Fapi"></a>

```c
struct sensor_driver_api
```

相关声明：[sensor_driver_api](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md)。

驱动操作（Driver Operations）：传感器（Sensor）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 20.2\_类型定义（Typedefs）

<a id="r_ga38422ace4194a66a9a912a8ef1e088fb"></a>

```c
typedef int(* sensor_attr_set_t) (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, const struct sensor_value *val)
```

相关声明：[sensor_attr_set_t](#ga38422ace4194a66a9a912a8ef1e088fb)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

设置传感器属性（Sensor Attribute）的回调 API。

<a id="r_ga00d05c82b46e56dca5f6e8f7f01c31b8"></a>

```c
typedef int(* sensor_attr_get_t) (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, struct sensor_value *val)
```

相关声明：[sensor_attr_get_t](#ga00d05c82b46e56dca5f6e8f7f01c31b8)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

获取传感器属性（Sensor Attribute）的回调 API。

<a id="r_gad7f7a3d9e714cc16f23656ca06592aa4"></a>

```c
typedef int(* sensor_trigger_set_t) (const struct device *dev, const struct sensor_trigger *trig, sensor_trigger_handler_t handler)
```

相关声明：[sensor_trigger_set_t](#gad7f7a3d9e714cc16f23656ca06592aa4)、[device](../device_reference/P002_设备对象结构.md)、[sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)、[sensor_trigger_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga890c1fb6d6974aea22a2d08829a75902)。

设置传感器触发器与处理程序（Sensor Trigger and Handler）的回调 API。

<a id="r_gacae110a4edb6f29dfb457cb1ea8d68c1"></a>

```c
typedef int(* sensor_sample_fetch_t) (const struct device *dev, enum sensor_channel chan)
```

相关声明：[sensor_sample_fetch_t](#gacae110a4edb6f29dfb457cb1ea8d68c1)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)。

将传感器样本获取到驱动缓冲区（Driver Buffer）的回调 API。

<a id="r_ga5c9b5ed9097464562004b446856043fd"></a>

```c
typedef int(* sensor_channel_get_t) (const struct device *dev, enum sensor_channel chan, struct sensor_value *val)
```

相关声明：[sensor_channel_get_t](#ga5c9b5ed9097464562004b446856043fd)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

从驱动缓冲区（Driver Buffer）读取传感器通道（Sensor Channel）的回调 API。

<a id="r_ga21e407d552d140cfb6bfd0d9513c7d42"></a>

```c
typedef int(* sensor_get_decoder_t) (const struct device *dev, const struct sensor_decoder_api **api)
```

相关声明：[sensor_get_decoder_t](#ga21e407d552d140cfb6bfd0d9513c7d42)、[device](../device_reference/P002_设备对象结构.md)、[sensor_decoder_api](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md)。

获取传感器解码器实现（Sensor Decoder Implementation）的回调 API。

<a id="r_gad77732c8f0ec5520cdd71c2829787981"></a>

```c
typedef void(* sensor_submit_t) (const struct device *sensor, struct rtio_iodev_sqe *sqe)
```

相关声明：[sensor_submit_t](#gad77732c8f0ec5520cdd71c2829787981)、[device](../device_reference/P002_设备对象结构.md)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

处理传感器设备 RTIO 提交（Submission）的回调 API。

## 20.3\_详细说明（Detailed Documentation）

<a id="ga00d05c82b46e56dca5f6e8f7f01c31b8"></a>

### `sensor_attr_get_t`

```c
typedef int(* sensor_attr_get_t) (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, struct sensor_value *val)
```

```c
#include <zephyr/drivers/sensor.h>
```

获取传感器属性（Sensor Attribute）的回调 API。

参数说明（Argument Description）参见 `sensor_attr_get()`。

<a id="ga38422ace4194a66a9a912a8ef1e088fb"></a>

### `sensor_attr_set_t`

```c
typedef int(* sensor_attr_set_t) (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, const struct sensor_value *val)
```

```c
#include <zephyr/drivers/sensor.h>
```

设置传感器属性（Sensor Attribute）的回调 API。

参数说明（Argument Description）参见 `sensor_attr_set()`。

<a id="ga5c9b5ed9097464562004b446856043fd"></a>

### `sensor_channel_get_t`

```c
typedef int(* sensor_channel_get_t) (const struct device *dev, enum sensor_channel chan, struct sensor_value *val)
```

```c
#include <zephyr/drivers/sensor.h>
```

从驱动缓冲区（Driver Buffer）读取传感器通道（Sensor Channel）的回调 API。

参数说明（Argument Description）参见 `sensor_channel_get()`。

<a id="ga21e407d552d140cfb6bfd0d9513c7d42"></a>

### `sensor_get_decoder_t`

```c
typedef int(* sensor_get_decoder_t) (const struct device *dev, const struct sensor_decoder_api **api)
```

```c
#include <zephyr/drivers/sensor.h>
```

获取传感器解码器实现（Sensor Decoder Implementation）的回调 API。

参数说明（Argument Description）参见 `sensor_get_decoder()`。

<a id="gacae110a4edb6f29dfb457cb1ea8d68c1"></a>

### `sensor_sample_fetch_t`

```c
typedef int(* sensor_sample_fetch_t) (const struct device *dev, enum sensor_channel chan)
```

```c
#include <zephyr/drivers/sensor.h>
```

将传感器样本获取到驱动缓冲区（Driver Buffer）的回调 API。

参数说明（Argument Description）参见 `sensor_sample_fetch_chan()`。

<a id="gad77732c8f0ec5520cdd71c2829787981"></a>

### `sensor_submit_t`

```c
typedef void(* sensor_submit_t) (const struct device *sensor, struct rtio_iodev_sqe *sqe)
```

```c
#include <zephyr/drivers/sensor.h>
```

处理传感器设备 RTIO 提交（Submission）的回调 API。

异步传感器路径（Asynchronous Sensor Path）将工作分派给驱动时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sensor` | 传感器设备（Sensor Device）。 |
| `sqe` | RTIO 提交队列条目（Submission Queue Entry）。 |

<a id="gad7f7a3d9e714cc16f23656ca06592aa4"></a>

### `sensor_trigger_set_t`

```c
typedef int(* sensor_trigger_set_t) (const struct device *dev, const struct sensor_trigger *trig, sensor_trigger_handler_t handler)
```

```c
#include <zephyr/drivers/sensor.h>
```

设置传感器触发器与处理程序（Sensor Trigger and Handler）的回调 API。

参数说明（Argument Description）参见 `sensor_trigger_set()`。


## 20.4\_原页交叉引用（Cross References）

- [sensor_driver_api](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)
- [sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)
- [sensor_trigger_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga890c1fb6d6974aea22a2d08829a75902)
- [sensor_decoder_api](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attr_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaedfdfc71dce702dc1fb1c6e60ff0f73a)
- [sensor_attr_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gafbf65226a227e9f8824908bc38e336f5)
- [sensor_channel_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e0e6c1408d32c52267984bae7cb268d)
- [sensor_get_decoder()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga12db6fc43adce48d34c25c16fd2336a3)
- [sensor_sample_fetch_chan()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gac16192826432438a15274cf28d66e8a6)
- [sensor_trigger_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga7c72aca732e0641612d2f9437c2e41b7)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P019_Iclegend S3KM1110 API主题.md) · [返回大纲](大纲.md) · [下一章](P021_安全外壳（SSH）客户端库.md)
