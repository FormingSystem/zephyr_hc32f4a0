---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-3
title: GNSS 驱动后端 API（Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_GNSS 驱动后端 API（Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

此组包含实现全球导航卫星系统（GNSS）驱动所需的 API 类型定义、回调签名（Callback Signatures）及其他辅助接口。

<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_gnss_5Fpublish_2Eh"></a>

```c
file gnss_publish.h
```

相关声明：[gnss_publish.h](../api_file_configuration_reference/P033_zephyr__drivers__gnss__gnss_publish.h_文件参考.md)。

用于发布数据和卫星信息的GNSS驱动后端辅助接口（Backend Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.2\_数据结构（Data Structures）

<a id="r_gnss_5Fdriver_5Fapi"></a>

```c
struct gnss_driver_api
```

相关声明：[gnss_driver_api](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md)。

驱动操作（Driver Operations）：全球导航卫星系统（GNSS）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_ga8f617e5c8a0938e5eef4d69a3f753303"></a>

```c
typedef int(* gnss_start_t) (const struct device *dev, enum gnss_start_mode mode)
```

相关声明：[gnss_start_t](#ga8f617e5c8a0938e5eef4d69a3f753303)、[device](../device_reference/P002_设备对象结构.md)、[gnss_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga7106633a65ddaa29e19ba9f15b86f0f9)。

用于启动 GNSS 接收机引擎（Receiver Engine）的 API。

<a id="r_ga906cecc7e7173893106d6154c7421fc6"></a>

```c
typedef int(* gnss_stop_t) (const struct device *dev)
```

相关声明：[gnss_stop_t](#ga906cecc7e7173893106d6154c7421fc6)、[device](../device_reference/P002_设备对象结构.md)。

用于停止 GNSS 接收机引擎（Receiver Engine）的 API。

<a id="r_ga79e5975d5ec6c0557af4a71004a6da93"></a>

```c
typedef int(* gnss_set_fix_rate_t) (const struct device *dev, uint32_t fix_interval_ms)
```

相关声明：[gnss_set_fix_rate_t](#ga79e5975d5ec6c0557af4a71004a6da93)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于设置定位更新率（Fix Rate）的 API。

<a id="r_ga63a98e08bc7e4b9c70a27de48dc9cd8c"></a>

```c
typedef int(* gnss_get_fix_rate_t) (const struct device *dev, uint32_t *fix_interval_ms)
```

相关声明：[gnss_get_fix_rate_t](#ga63a98e08bc7e4b9c70a27de48dc9cd8c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于获取定位更新率（Fix Rate）的 API。

<a id="r_gae946fce6ecced7c8fa09e06d75855abe"></a>

```c
typedef int(* gnss_set_navigation_mode_t) (const struct device *dev, enum gnss_navigation_mode mode)
```

相关声明：[gnss_set_navigation_mode_t](#gae946fce6ecced7c8fa09e06d75855abe)、[device](../device_reference/P002_设备对象结构.md)、[gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)。

用于设置导航模式（Navigation Mode）的 API。

<a id="r_ga9705b36019161fde431e78d943eff604"></a>

```c
typedef int(* gnss_get_navigation_mode_t) (const struct device *dev, enum gnss_navigation_mode *mode)
```

相关声明：[gnss_get_navigation_mode_t](#ga9705b36019161fde431e78d943eff604)、[device](../device_reference/P002_设备对象结构.md)、[gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)。

用于获取导航模式（Navigation Mode）的 API。

<a id="r_ga91948cc0567c343bee62b6c70a2f461d"></a>

```c
typedef int(* gnss_set_enabled_systems_t) (const struct device *dev, gnss_systems_t systems)
```

相关声明：[gnss_set_enabled_systems_t](#ga91948cc0567c343bee62b6c70a2f461d)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

用于启用卫星系统（Systems）的 API。

<a id="r_gad87bd07c46ea1f79caf9a484c51ec0c9"></a>

```c
typedef int(* gnss_get_enabled_systems_t) (const struct device *dev, gnss_systems_t *systems)
```

相关声明：[gnss_get_enabled_systems_t](#gad87bd07c46ea1f79caf9a484c51ec0c9)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

用于获取已启用卫星系统（Enabled Systems）的 API。

<a id="r_gaf52a65dee0d28286ac40e5c8bc86825a"></a>

```c
typedef int(* gnss_get_supported_systems_t) (const struct device *dev, gnss_systems_t *systems)
```

相关声明：[gnss_get_supported_systems_t](#gaf52a65dee0d28286ac40e5c8bc86825a)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

用于获取已启用卫星系统（Enabled Systems）的 API。

<a id="r_gaa482aa8a996b743aba7e68f36b4780a8"></a>

```c
typedef int(* gnss_get_latest_timepulse_t) (const struct device *dev, k_ticks_t *timestamp)
```

相关声明：[gnss_get_latest_timepulse_t](#gaa482aa8a996b743aba7e68f36b4780a8)、[device](../device_reference/P002_设备对象结构.md)、[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)。

用于获取最后一个秒脉冲（PPS Pulse）的时间戳（Timestamp）的 API。

<a id="r_gad2d05fbf4073b71df054b025b65d51b1"></a>

```c
void gnss_publish_data (const struct device *dev, const struct gnss_data *data)
```

相关声明：[gnss_publish_data](#gad2d05fbf4073b71df054b025b65d51b1)、[device](../device_reference/P002_设备对象结构.md)、[gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)。

向已注册的回调（Callbacks）发布全球导航卫星系统数据（GNSS Data）。

<a id="r_gad55e06af3b36823b48d921df1852ad09"></a>

```c
void gnss_publish_satellites (const struct device *dev, const struct gnss_satellite *satellites, uint16_t size)
```

相关声明：[gnss_publish_satellites](#gad55e06af3b36823b48d921df1852ad09)、[device](../device_reference/P002_设备对象结构.md)、[gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向已注册的回调（Callbacks）发布全球导航卫星系统卫星信息（GNSS Satellite Information）。

## 3.4\_详细说明（Detailed Documentation）

<a id="gad87bd07c46ea1f79caf9a484c51ec0c9"></a>

### `gnss_get_enabled_systems_t`

```c
typedef int(* gnss_get_enabled_systems_t) (const struct device *dev, gnss_systems_t *systems)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于获取已启用卫星系统（Enabled Systems）的 API。

<a id="ga63a98e08bc7e4b9c70a27de48dc9cd8c"></a>

### `gnss_get_fix_rate_t`

```c
typedef int(* gnss_get_fix_rate_t) (const struct device *dev, uint32_t *fix_interval_ms)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于获取定位更新率（Fix Rate）的 API。

<a id="gaa482aa8a996b743aba7e68f36b4780a8"></a>

### `gnss_get_latest_timepulse_t`

```c
typedef int(* gnss_get_latest_timepulse_t) (const struct device *dev, k_ticks_t *timestamp)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于获取最后一个秒脉冲（PPS Pulse）的时间戳（Timestamp）的 API。

<a id="ga9705b36019161fde431e78d943eff604"></a>

### `gnss_get_navigation_mode_t`

```c
typedef int(* gnss_get_navigation_mode_t) (const struct device *dev, enum gnss_navigation_mode *mode)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于获取导航模式（Navigation Mode）的 API。

<a id="gaf52a65dee0d28286ac40e5c8bc86825a"></a>

### `gnss_get_supported_systems_t`

```c
typedef int(* gnss_get_supported_systems_t) (const struct device *dev, gnss_systems_t *systems)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于获取已启用卫星系统（Enabled Systems）的 API。

<a id="ga91948cc0567c343bee62b6c70a2f461d"></a>

### `gnss_set_enabled_systems_t`

```c
typedef int(* gnss_set_enabled_systems_t) (const struct device *dev, gnss_systems_t systems)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于启用卫星系统（Systems）的 API。

<a id="ga79e5975d5ec6c0557af4a71004a6da93"></a>

### `gnss_set_fix_rate_t`

```c
typedef int(* gnss_set_fix_rate_t) (const struct device *dev, uint32_t fix_interval_ms)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于设置定位更新率（Fix Rate）的 API。

<a id="gae946fce6ecced7c8fa09e06d75855abe"></a>

### `gnss_set_navigation_mode_t`

```c
typedef int(* gnss_set_navigation_mode_t) (const struct device *dev, enum gnss_navigation_mode mode)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于设置导航模式（Navigation Mode）的 API。

<a id="ga8f617e5c8a0938e5eef4d69a3f753303"></a>

### `gnss_start_t`

```c
typedef int(* gnss_start_t) (const struct device *dev, enum gnss_start_mode mode)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于启动 GNSS 接收机引擎（Receiver Engine）的 API。

<a id="ga906cecc7e7173893106d6154c7421fc6"></a>

### `gnss_stop_t`

```c
typedef int(* gnss_stop_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/gnss.h>
```

用于停止 GNSS 接收机引擎（Receiver Engine）的 API。

<a id="gad2d05fbf4073b71df054b025b65d51b1"></a>

### `gnss_publish_data()`

```c
void gnss_publish_data ( const struct device * dev, const struct gnss_data * data )
```

```c
#include <zephyr/drivers/gnss/gnss_publish.h>
```

向已注册的回调（Callbacks）发布全球导航卫星系统数据（GNSS Data）。

调用通过 `GNSS_DATA_CALLBACK_DEFINE()` 和 `GNSS_DT_DATA_CALLBACK_DEFINE()` 注册且与 `dev` 匹配的所有回调函数（Callbacks）。

每当接收机提供新的导航数据（Navigation Data）时，GNSS 驱动都应调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 发布数据的 GNSS 设备实例（Device Instance）。 |
| `data` | 要发布的导航数据（Navigation Data）、定位信息（Fix Information）及协调世界时（UTC）。 |

**参阅（See Also）**：另请参见：`GNSS_DATA_CALLBACK_DEFINE()`、`GNSS_DT_DATA_CALLBACK_DEFINE()`。

<a id="gad55e06af3b36823b48d921df1852ad09"></a>

### `gnss_publish_satellites()`

```c
void gnss_publish_satellites ( const struct device * dev, const struct gnss_satellite * satellites, uint16_t size )
```

```c
#include <zephyr/drivers/gnss/gnss_publish.h>
```

向已注册的回调（Callbacks）发布全球导航卫星系统卫星信息（GNSS Satellite Information）。

调用通过 `GNSS_SATELLITES_CALLBACK_DEFINE()` 和 `GNSS_DT_SATELLITES_CALLBACK_DEFINE()` 注册且与 `dev` 匹配的所有回调函数（Callbacks）。

每当接收机提供更新的卫星跟踪信息（Satellite Tracking Information）时，GNSS 驱动都应调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 发布卫星数据的 GNSS 设备实例（Device Instance）。 |
| `satellites` | 卫星跟踪数据数组（Satellite Tracking Data Array）。 |
| `size` | `satellites` 中的元素个数。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_GNSS_SATELLITES` 时可用。

**参阅（See Also）**：另请参见：`GNSS_SATELLITES_CALLBACK_DEFINE()`、`GNSS_DT_SATELLITES_CALLBACK_DEFINE()`。


## 3.5\_原页交叉引用（Cross References）

- [gnss_publish.h](../api_file_configuration_reference/P033_zephyr__drivers__gnss__gnss_publish.h_文件参考.md)
- [gnss_driver_api](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [gnss_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga7106633a65ddaa29e19ba9f15b86f0f9)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)
- [gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)
- [gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)
- [gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/drivers/gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h.html)
- [GNSS_DATA_CALLBACK_DEFINE()](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gae9c3fd5804bd6f8e6790cb1b7e47e4a6)
- [GNSS_DT_DATA_CALLBACK_DEFINE()](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga00d744003c1c8f71f06a685ecb8d07b1)
- [GNSS_SATELLITES_CALLBACK_DEFINE()](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga414a414635e1cd00ef800edaf70bc234)
- [GNSS_DT_SATELLITES_CALLBACK_DEFINE()](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga794cc5cadc7a7f470b6f57395bf333f1)
- [CONFIG_GNSS_SATELLITES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GNSS_SATELLITES)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_以太网桥接 API（Ethernet Bridging API）.md) · [返回大纲](大纲.md) · [下一章](P004_ICM566xx API主题.md)
