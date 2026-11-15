---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-3
title: zephyr__drivers__gnss.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_gnss.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全球导航卫星系统（GNSS）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/data/navigation.h>
#include <errno.h>
#include <zephyr/syscalls/gnss.h>
```

查看此文件的源码。

全球导航卫星系统（GNSS）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_gnss_5Finfo"></a>

```c
struct gnss_info
```

相关声明：[gnss_info](../sensor_navigation_model_reference/P012_gnss_info_结构体.md)。

全球导航卫星系统（GNSS）的信息数据结构。

<a id="r_gnss_5Ftime"></a>

```c
struct gnss_time
```

相关声明：[gnss_time](../sensor_navigation_model_reference/P017_gnss_time_结构体.md)。

全球导航卫星系统（GNSS）的时间数据结构。

<a id="r_gnss_5Fdriver_5Fapi"></a>

```c
struct gnss_driver_api
```

相关声明：[gnss_driver_api](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md)。

驱动操作（Driver Operations）：全球导航卫星系统（GNSS）驱动操作。

<a id="r_gnss_5Fdata"></a>

```c
struct gnss_data
```

相关声明：[gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)。

全球导航卫星系统（GNSS）的数据结构。

<a id="r_gnss_5Fdata_5Fcallback"></a>

```c
struct gnss_data_callback
```

相关声明：[gnss_data_callback](../sensor_navigation_model_reference/P010_gnss_data_callback_结构体.md)。

全球导航卫星系统（GNSS）的回调结构。

<a id="r_gnss_5Fsatellite"></a>

```c
struct gnss_satellite
```

相关声明：[gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)。

全球导航卫星系统（GNSS）的卫星结构。

<a id="r_gnss_5Fsatellites_5Fcallback"></a>

```c
struct gnss_satellites_callback
```

相关声明：[gnss_satellites_callback](../sensor_navigation_model_reference/P016_gnss_satellites_callback_结构体.md)。

全球导航卫星系统（GNSS）的回调结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_gae9c3fd5804bd6f8e6790cb1b7e47e4a6"></a>

```c
#define GNSS_DATA_CALLBACK_DEFINE(_dev, _callback)
```

相关声明：[GNSS_DATA_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gae9c3fd5804bd6f8e6790cb1b7e47e4a6)。

为发布的全球导航卫星系统（GNSS）数据注册回调结构体。

<a id="r_ga00d744003c1c8f71f06a685ecb8d07b1"></a>

```c
#define GNSS_DT_DATA_CALLBACK_DEFINE(_node_id, _callback)
```

相关声明：[GNSS_DT_DATA_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga00d744003c1c8f71f06a685ecb8d07b1)。

<a id="r_ga414a414635e1cd00ef800edaf70bc234"></a>

```c
#define GNSS_SATELLITES_CALLBACK_DEFINE(_dev, _callback)
```

相关声明：[GNSS_SATELLITES_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga414a414635e1cd00ef800edaf70bc234)。

为发布的 GNSS 卫星信息（Satellites）注册回调结构体。

<a id="r_ga794cc5cadc7a7f470b6f57395bf333f1"></a>

```c
#define GNSS_DT_SATELLITES_CALLBACK_DEFINE(_node_id, _callback)
```

相关声明：[GNSS_DT_SATELLITES_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga794cc5cadc7a7f470b6f57395bf333f1)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_ga731907f9ae501909bf26ecae5441a5ce"></a>

```c
typedef uint32_t gnss_systems_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

保存 GNSS 系统位掩码（System Bitmask）的类型。

<a id="r_ga8f617e5c8a0938e5eef4d69a3f753303"></a>

```c
typedef int(* gnss_start_t) (const struct device *dev, enum gnss_start_mode mode)
```

相关声明：[gnss_start_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga8f617e5c8a0938e5eef4d69a3f753303)、[device](../device_reference/P002_设备对象结构.md)、[gnss_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga7106633a65ddaa29e19ba9f15b86f0f9)。

用于启动 GNSS 接收机引擎（Receiver Engine）的 API。

<a id="r_ga906cecc7e7173893106d6154c7421fc6"></a>

```c
typedef int(* gnss_stop_t) (const struct device *dev)
```

相关声明：[gnss_stop_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga906cecc7e7173893106d6154c7421fc6)、[device](../device_reference/P002_设备对象结构.md)。

用于停止 GNSS 接收机引擎（Receiver Engine）的 API。

<a id="r_ga79e5975d5ec6c0557af4a71004a6da93"></a>

```c
typedef int(* gnss_set_fix_rate_t) (const struct device *dev, uint32_t fix_interval_ms)
```

相关声明：[gnss_set_fix_rate_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga79e5975d5ec6c0557af4a71004a6da93)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于设置定位更新率（Fix Rate）的 API。

<a id="r_ga63a98e08bc7e4b9c70a27de48dc9cd8c"></a>

```c
typedef int(* gnss_get_fix_rate_t) (const struct device *dev, uint32_t *fix_interval_ms)
```

相关声明：[gnss_get_fix_rate_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga63a98e08bc7e4b9c70a27de48dc9cd8c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于获取定位更新率（Fix Rate）的 API。

<a id="r_gae946fce6ecced7c8fa09e06d75855abe"></a>

```c
typedef int(* gnss_set_navigation_mode_t) (const struct device *dev, enum gnss_navigation_mode mode)
```

相关声明：[gnss_set_navigation_mode_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#gae946fce6ecced7c8fa09e06d75855abe)、[device](../device_reference/P002_设备对象结构.md)、[gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)。

用于设置导航模式（Navigation Mode）的 API。

<a id="r_ga9705b36019161fde431e78d943eff604"></a>

```c
typedef int(* gnss_get_navigation_mode_t) (const struct device *dev, enum gnss_navigation_mode *mode)
```

相关声明：[gnss_get_navigation_mode_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga9705b36019161fde431e78d943eff604)、[device](../device_reference/P002_设备对象结构.md)、[gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)。

用于获取导航模式（Navigation Mode）的 API。

<a id="r_ga91948cc0567c343bee62b6c70a2f461d"></a>

```c
typedef int(* gnss_set_enabled_systems_t) (const struct device *dev, gnss_systems_t systems)
```

相关声明：[gnss_set_enabled_systems_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga91948cc0567c343bee62b6c70a2f461d)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

用于启用卫星系统（Systems）的 API。

<a id="r_gad87bd07c46ea1f79caf9a484c51ec0c9"></a>

```c
typedef int(* gnss_get_enabled_systems_t) (const struct device *dev, gnss_systems_t *systems)
```

相关声明：[gnss_get_enabled_systems_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#gad87bd07c46ea1f79caf9a484c51ec0c9)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

用于获取已启用卫星系统（Enabled Systems）的 API。

<a id="r_gaf52a65dee0d28286ac40e5c8bc86825a"></a>

```c
typedef int(* gnss_get_supported_systems_t) (const struct device *dev, gnss_systems_t *systems)
```

相关声明：[gnss_get_supported_systems_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#gaf52a65dee0d28286ac40e5c8bc86825a)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

用于获取已启用卫星系统（Enabled Systems）的 API。

<a id="r_gaa482aa8a996b743aba7e68f36b4780a8"></a>

```c
typedef int(* gnss_get_latest_timepulse_t) (const struct device *dev, k_ticks_t *timestamp)
```

相关声明：[gnss_get_latest_timepulse_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#gaa482aa8a996b743aba7e68f36b4780a8)、[device](../device_reference/P002_设备对象结构.md)、[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)。

用于获取最后一个秒脉冲（PPS Pulse）的时间戳（Timestamp）的 API。

<a id="r_ga025c965369275ad8e5ab5ad44c14a23b"></a>

```c
typedef void(* gnss_data_callback_t) (const struct device *dev, const struct gnss_data *data)
```

相关声明：[gnss_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga025c965369275ad8e5ab5ad44c14a23b)、[device](../device_reference/P002_设备对象结构.md)、[gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)。

GNSS 数据回调模板（Data Callback Template）。

<a id="r_ga80cf700468d1c942cfa064368e212e6f"></a>

```c
typedef void(* gnss_satellites_callback_t) (const struct device *dev, const struct gnss_satellite *satellites, uint16_t size)
```

相关声明：[gnss_satellites_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga80cf700468d1c942cfa064368e212e6f)、[device](../device_reference/P002_设备对象结构.md)、[gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

GNSS 卫星信息回调模板（Satellites Callback Template）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.4\_枚举（Enumerations）

<a id="r_ga7106633a65ddaa29e19ba9f15b86f0f9"></a>

```c
enum gnss_start_mode { GNSS_HOT_START = 0 , GNSS_WARM_START = 1 , GNSS_COLD_START = 2 }
```

相关声明：[gnss_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga7106633a65ddaa29e19ba9f15b86f0f9)、[GNSS_HOT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga7106633a65ddaa29e19ba9f15b86f0f9ad0ecfd51dd2e99b5bd7e8abd49143da7)、[GNSS_WARM_START](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga7106633a65ddaa29e19ba9f15b86f0f9adff054d3999e9f0c2f3c6efc96772cc8)、[GNSS_COLD_START](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga7106633a65ddaa29e19ba9f15b86f0f9af594a76c0f37da20791b1ce4e2a4f5a3)。

GNSS 接收机启动模式（Receiver Start Modes）。

<a id="r_ga2b43ac2fec33053a769b7070c4ed3263"></a>

```c
enum gnss_pps_mode { GNSS_PPS_MODE_DISABLED = 0 , GNSS_PPS_MODE_ENABLED = 1 , GNSS_PPS_MODE_ENABLED_AFTER_LOCK = 2 , GNSS_PPS_MODE_ENABLED_WHILE_LOCKED = 3 }
```

相关声明：[gnss_pps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga2b43ac2fec33053a769b7070c4ed3263)、[GNSS_PPS_MODE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc)、[GNSS_PPS_MODE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa)、[GNSS_PPS_MODE_ENABLED_AFTER_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507)、[GNSS_PPS_MODE_ENABLED_WHILE_LOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc)。

GNSS 秒脉冲模式（PPS Modes）。

<a id="r_gadb734bb12433276d3014e08a1d21bb18"></a>

```c
enum gnss_navigation_mode { GNSS_NAVIGATION_MODE_ZERO_DYNAMICS = 0 , GNSS_NAVIGATION_MODE_LOW_DYNAMICS = 1 , GNSS_NAVIGATION_MODE_BALANCED_DYNAMICS = 2 , GNSS_NAVIGATION_MODE_HIGH_DYNAMICS = 3 }
```

相关声明：[gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)、[GNSS_NAVIGATION_MODE_ZERO_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff)、[GNSS_NAVIGATION_MODE_LOW_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453)、[GNSS_NAVIGATION_MODE_BALANCED_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d)、[GNSS_NAVIGATION_MODE_HIGH_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f)。

GNSS 导航模式（Navigation Modes）。

<a id="r_ga928a05b4e820a9fcc8bc2db81f5f8c79"></a>

```c
enum gnss_system { GNSS_SYSTEM_GPS = BIT(0) , GNSS_SYSTEM_GLONASS = BIT(1) , GNSS_SYSTEM_GALILEO = BIT(2) , GNSS_SYSTEM_BEIDOU = BIT(3) , GNSS_SYSTEM_QZSS = BIT(4) , GNSS_SYSTEM_IRNSS = BIT(5) , GNSS_SYSTEM_SBAS = BIT(6) , GNSS_SYSTEM_IMES = BIT(7) }
```

相关声明：[gnss_system](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga928a05b4e820a9fcc8bc2db81f5f8c79)、[GNSS_SYSTEM_GPS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33)、[GNSS_SYSTEM_GLONASS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd)、[GNSS_SYSTEM_GALILEO](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c)、[GNSS_SYSTEM_BEIDOU](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55)、[GNSS_SYSTEM_QZSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff)、[GNSS_SYSTEM_IRNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242)、[GNSS_SYSTEM_SBAS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd)、[GNSS_SYSTEM_IMES](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9)。

`gnss_systems_t` 中包含的卫星系统（Systems）。

<a id="r_ga15536308e2229a45493d06e8b61e63d9"></a>

```c
enum gnss_fix_status { GNSS_FIX_STATUS_NO_FIX = 0 , GNSS_FIX_STATUS_GNSS_FIX = 1 , GNSS_FIX_STATUS_DGNSS_FIX = 2 , GNSS_FIX_STATUS_ESTIMATED_FIX = 3 }
```

相关声明：[gnss_fix_status](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga15536308e2229a45493d06e8b61e63d9)、[GNSS_FIX_STATUS_NO_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe)、[GNSS_FIX_STATUS_GNSS_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343)、[GNSS_FIX_STATUS_DGNSS_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc)、[GNSS_FIX_STATUS_ESTIMATED_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb)。

GNSS 定位状态（Fix Status）。

<a id="r_gacf5a3464c487ae7609d526c73ccc758a"></a>

```c
enum gnss_fix_quality { GNSS_FIX_QUALITY_INVALID = 0 , GNSS_FIX_QUALITY_GNSS_SPS = 1 , GNSS_FIX_QUALITY_DGNSS = 2 , GNSS_FIX_QUALITY_GNSS_PPS = 3 , GNSS_FIX_QUALITY_RTK = 4 , GNSS_FIX_QUALITY_FLOAT_RTK = 5 , GNSS_FIX_QUALITY_ESTIMATED = 6 }
```

相关声明：[gnss_fix_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gacf5a3464c487ae7609d526c73ccc758a)、[GNSS_FIX_QUALITY_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30)、[GNSS_FIX_QUALITY_GNSS_SPS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f)、[GNSS_FIX_QUALITY_DGNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8)、[GNSS_FIX_QUALITY_GNSS_PPS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f)、[GNSS_FIX_QUALITY_RTK](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6)、[GNSS_FIX_QUALITY_FLOAT_RTK](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6)、[GNSS_FIX_QUALITY_ESTIMATED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a)。

GNSS 定位质量（Fix Quality）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.5\_函数（Functions）

<a id="r_ga6bdabc1e89f5c7b10c1099fa74e6c6ca"></a>

```c
int gnss_start (const struct device *dev, enum gnss_start_mode mode)
```

相关声明：[gnss_start](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga6bdabc1e89f5c7b10c1099fa74e6c6ca)、[device](../device_reference/P002_设备对象结构.md)、[gnss_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga7106633a65ddaa29e19ba9f15b86f0f9)。

启动 GNSS 接收机引擎（Receiver Engine）。

<a id="r_ga43f285927c94079e3b72e81303cff520"></a>

```c
int gnss_stop (const struct device *dev)
```

相关声明：[gnss_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga43f285927c94079e3b72e81303cff520)、[device](../device_reference/P002_设备对象结构.md)。

停止 GNSS 接收机引擎（Receiver Engine）。

<a id="r_ga16e8326737f114bd6017983812c7f28d"></a>

```c
int gnss_set_fix_rate (const struct device *dev, uint32_t fix_interval_ms)
```

相关声明：[gnss_set_fix_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga16e8326737f114bd6017983812c7f28d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 GNSS 定位更新率（Fix Rate）。

<a id="r_ga8e625fb3f8758eab78c115d12bef6a72"></a>

```c
int gnss_get_fix_rate (const struct device *dev, uint32_t *fix_interval_ms)
```

相关声明：[gnss_get_fix_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga8e625fb3f8758eab78c115d12bef6a72)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 GNSS 定位更新率（Fix Rate）。

<a id="r_ga9d0347640e68d5702b1cb43ddf8380df"></a>

```c
int gnss_set_navigation_mode (const struct device *dev, enum gnss_navigation_mode mode)
```

相关声明：[gnss_set_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga9d0347640e68d5702b1cb43ddf8380df)、[device](../device_reference/P002_设备对象结构.md)、[gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)。

设置 GNSS 导航模式（Navigation Mode）。

<a id="r_gae5614f8125dad02a3ebd30400b575e6d"></a>

```c
int gnss_get_navigation_mode (const struct device *dev, enum gnss_navigation_mode *mode)
```

相关声明：[gnss_get_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gae5614f8125dad02a3ebd30400b575e6d)、[device](../device_reference/P002_设备对象结构.md)、[gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)。

获取 GNSS 导航模式（Navigation Mode）。

<a id="r_ga818e42c7a979623679eba26887662823"></a>

```c
int gnss_set_enabled_systems (const struct device *dev, gnss_systems_t systems)
```

相关声明：[gnss_set_enabled_systems](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga818e42c7a979623679eba26887662823)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

设置启用的 GNSS 卫星系统（Enabled Systems）。

<a id="r_ga155126e113195c08158ef49e2a6b4f6a"></a>

```c
int gnss_get_enabled_systems (const struct device *dev, gnss_systems_t *systems)
```

相关声明：[gnss_get_enabled_systems](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga155126e113195c08158ef49e2a6b4f6a)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

获取启用的 GNSS 卫星系统（Enabled Systems）。

<a id="r_ga598609846ff196ff300fcad8237b2d51"></a>

```c
int gnss_get_supported_systems (const struct device *dev, gnss_systems_t *systems)
```

相关声明：[gnss_get_supported_systems](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga598609846ff196ff300fcad8237b2d51)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

获取支持的 GNSS 卫星系统（Supported Systems）。

<a id="r_ga8eb37446d71c020e0517a406ea240fc2"></a>

```c
int gnss_get_latest_timepulse (const struct device *dev, k_ticks_t *timestamp)
```

相关声明：[gnss_get_latest_timepulse](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga8eb37446d71c020e0517a406ea240fc2)、[device](../device_reference/P002_设备对象结构.md)、[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)。

获取最近一次秒脉冲（PPS Timepulse）的时间戳（Timestamp）。


## 3.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/data/navigation.h](../api_source_reference/P572_navigation.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P291_gnss.h_源码浏览.md)
- [gnss_info](../sensor_navigation_model_reference/P012_gnss_info_结构体.md)
- [gnss_time](../sensor_navigation_model_reference/P017_gnss_time_结构体.md)
- [gnss_driver_api](../sensor_navigation_model_reference/P011_gnss_driver_api_结构体.md)
- [gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)
- [gnss_data_callback](../sensor_navigation_model_reference/P010_gnss_data_callback_结构体.md)
- [gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)
- [gnss_satellites_callback](../sensor_navigation_model_reference/P016_gnss_satellites_callback_结构体.md)
- [GNSS_DATA_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gae9c3fd5804bd6f8e6790cb1b7e47e4a6)
- [GNSS_DT_DATA_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga00d744003c1c8f71f06a685ecb8d07b1)
- [GNSS_SATELLITES_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga414a414635e1cd00ef800edaf70bc234)
- [GNSS_DT_SATELLITES_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga794cc5cadc7a7f470b6f57395bf333f1)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)
- [gnss_start_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga8f617e5c8a0938e5eef4d69a3f753303)
- [device](../device_reference/P002_设备对象结构.md)
- [gnss_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga7106633a65ddaa29e19ba9f15b86f0f9)
- [gnss_stop_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga906cecc7e7173893106d6154c7421fc6)
- [gnss_set_fix_rate_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga79e5975d5ec6c0557af4a71004a6da93)
- [gnss_get_fix_rate_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga63a98e08bc7e4b9c70a27de48dc9cd8c)
- [gnss_set_navigation_mode_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#gae946fce6ecced7c8fa09e06d75855abe)
- [gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)
- [gnss_get_navigation_mode_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga9705b36019161fde431e78d943eff604)
- [gnss_set_enabled_systems_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#ga91948cc0567c343bee62b6c70a2f461d)
- [gnss_get_enabled_systems_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#gad87bd07c46ea1f79caf9a484c51ec0c9)
- [gnss_get_supported_systems_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#gaf52a65dee0d28286ac40e5c8bc86825a)
- [gnss_get_latest_timepulse_t](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md#gaa482aa8a996b743aba7e68f36b4780a8)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)
- [gnss_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga025c965369275ad8e5ab5ad44c14a23b)
- [gnss_satellites_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga80cf700468d1c942cfa064368e212e6f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [GNSS_HOT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga7106633a65ddaa29e19ba9f15b86f0f9ad0ecfd51dd2e99b5bd7e8abd49143da7)
- [GNSS_WARM_START](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga7106633a65ddaa29e19ba9f15b86f0f9adff054d3999e9f0c2f3c6efc96772cc8)
- [GNSS_COLD_START](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga7106633a65ddaa29e19ba9f15b86f0f9af594a76c0f37da20791b1ce4e2a4f5a3)
- [gnss_pps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga2b43ac2fec33053a769b7070c4ed3263)
- [GNSS_PPS_MODE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc)
- [GNSS_PPS_MODE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa)
- [GNSS_PPS_MODE_ENABLED_AFTER_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507)
- [GNSS_PPS_MODE_ENABLED_WHILE_LOCKED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc)
- [GNSS_NAVIGATION_MODE_ZERO_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff)
- [GNSS_NAVIGATION_MODE_LOW_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453)
- [GNSS_NAVIGATION_MODE_BALANCED_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d)
- [GNSS_NAVIGATION_MODE_HIGH_DYNAMICS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f)
- [gnss_system](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga928a05b4e820a9fcc8bc2db81f5f8c79)
- [GNSS_SYSTEM_GPS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33)
- [GNSS_SYSTEM_GLONASS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd)
- [GNSS_SYSTEM_GALILEO](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c)
- [GNSS_SYSTEM_BEIDOU](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55)
- [GNSS_SYSTEM_QZSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff)
- [GNSS_SYSTEM_IRNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242)
- [GNSS_SYSTEM_SBAS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd)
- [GNSS_SYSTEM_IMES](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9)
- [gnss_fix_status](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga15536308e2229a45493d06e8b61e63d9)
- [GNSS_FIX_STATUS_NO_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe)
- [GNSS_FIX_STATUS_GNSS_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343)
- [GNSS_FIX_STATUS_DGNSS_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc)
- [GNSS_FIX_STATUS_ESTIMATED_FIX](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb)
- [gnss_fix_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gacf5a3464c487ae7609d526c73ccc758a)
- [GNSS_FIX_QUALITY_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30)
- [GNSS_FIX_QUALITY_GNSS_SPS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f)
- [GNSS_FIX_QUALITY_DGNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8)
- [GNSS_FIX_QUALITY_GNSS_PPS](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f)
- [GNSS_FIX_QUALITY_RTK](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6)
- [GNSS_FIX_QUALITY_FLOAT_RTK](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6)
- [GNSS_FIX_QUALITY_ESTIMATED](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a)
- [gnss_start](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga6bdabc1e89f5c7b10c1099fa74e6c6ca)
- [gnss_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga43f285927c94079e3b72e81303cff520)
- [gnss_set_fix_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga16e8326737f114bd6017983812c7f28d)
- [gnss_get_fix_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga8e625fb3f8758eab78c115d12bef6a72)
- [gnss_set_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga9d0347640e68d5702b1cb43ddf8380df)
- [gnss_get_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gae5614f8125dad02a3ebd30400b575e6d)
- [gnss_set_enabled_systems](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga818e42c7a979623679eba26887662823)
- [gnss_get_enabled_systems](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga155126e113195c08158ef49e2a6b4f6a)
- [gnss_get_supported_systems](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga598609846ff196ff300fcad8237b2d51)
- [gnss_get_latest_timepulse](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga8eb37446d71c020e0517a406ea240fc2)

<a id="header-details"></a>

---

[上一章](P002_zephyr__drivers__dai.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__net__ssh__common.h_文件参考.md)
