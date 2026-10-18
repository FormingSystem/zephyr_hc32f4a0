---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-9
title: 全球导航卫星系统（GNSS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_全球导航卫星系统（GNSS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全球导航卫星系统（Global Navigation Satellite System，GNSS）接收机接口。

<a id="details"></a>

全球导航卫星系统接收机接口（Global Navigation Satellite System Receiver Interfaces，GNSS）。起始版本（Since）：3.6。接口版本（Version）：0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 9.1\_主题（Topics）

<a id="r_gnss_5Finterface_5Fbackend"></a>

相关声明：[GNSS 驱动后端 API（Driver Backend API）](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 9.2\_文件（Files）

<a id="r_gnss_2Eh"></a>

```c
file gnss.h
```

相关声明：[gnss.h](../api_file_serial_motion_reference/P003_zephyr__drivers__gnss.h_文件参考.md)。

全球导航卫星系统（GNSS）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.3\_数据结构（Data Structures）

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

## 9.4\_宏定义（Macros）

<a id="r_gae9c3fd5804bd6f8e6790cb1b7e47e4a6"></a>

```c
#define GNSS_DATA_CALLBACK_DEFINE(_dev, _callback)
```

相关声明：[GNSS_DATA_CALLBACK_DEFINE](#gae9c3fd5804bd6f8e6790cb1b7e47e4a6)。

为发布的全球导航卫星系统（GNSS）数据注册回调结构体。

<a id="r_ga00d744003c1c8f71f06a685ecb8d07b1"></a>

```c
#define GNSS_DT_DATA_CALLBACK_DEFINE(_node_id, _callback)
```

相关声明：[GNSS_DT_DATA_CALLBACK_DEFINE](#ga00d744003c1c8f71f06a685ecb8d07b1)。

<a id="r_ga414a414635e1cd00ef800edaf70bc234"></a>

```c
#define GNSS_SATELLITES_CALLBACK_DEFINE(_dev, _callback)
```

相关声明：[GNSS_SATELLITES_CALLBACK_DEFINE](#ga414a414635e1cd00ef800edaf70bc234)。

为发布的 GNSS 卫星信息（Satellites）注册回调结构体。

<a id="r_ga794cc5cadc7a7f470b6f57395bf333f1"></a>

```c
#define GNSS_DT_SATELLITES_CALLBACK_DEFINE(_node_id, _callback)
```

相关声明：[GNSS_DT_SATELLITES_CALLBACK_DEFINE](#ga794cc5cadc7a7f470b6f57395bf333f1)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.5\_类型定义（Typedefs）

<a id="r_ga731907f9ae501909bf26ecae5441a5ce"></a>

```c
typedef uint32_t gnss_systems_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[gnss_systems_t](#ga731907f9ae501909bf26ecae5441a5ce)。

保存 GNSS 系统位掩码（System Bitmask）的类型。

<a id="r_ga025c965369275ad8e5ab5ad44c14a23b"></a>

```c
typedef void(* gnss_data_callback_t) (const struct device *dev, const struct gnss_data *data)
```

相关声明：[gnss_data_callback_t](#ga025c965369275ad8e5ab5ad44c14a23b)、[device](../device_reference/P002_设备对象结构.md)、[gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)。

GNSS 数据回调模板（Data Callback Template）。

<a id="r_ga80cf700468d1c942cfa064368e212e6f"></a>

```c
typedef void(* gnss_satellites_callback_t) (const struct device *dev, const struct gnss_satellite *satellites, uint16_t size)
```

相关声明：[gnss_satellites_callback_t](#ga80cf700468d1c942cfa064368e212e6f)、[device](../device_reference/P002_设备对象结构.md)、[gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

GNSS 卫星信息回调模板（Satellites Callback Template）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.6\_枚举（Enumerations）

<a id="r_ga7106633a65ddaa29e19ba9f15b86f0f9"></a>

```c
enum gnss_start_mode { GNSS_HOT_START = 0 , GNSS_WARM_START = 1 , GNSS_COLD_START = 2 }
```

相关声明：[gnss_start_mode](#ga7106633a65ddaa29e19ba9f15b86f0f9)、[GNSS_HOT_START](#gga7106633a65ddaa29e19ba9f15b86f0f9ad0ecfd51dd2e99b5bd7e8abd49143da7)、[GNSS_WARM_START](#gga7106633a65ddaa29e19ba9f15b86f0f9adff054d3999e9f0c2f3c6efc96772cc8)、[GNSS_COLD_START](#gga7106633a65ddaa29e19ba9f15b86f0f9af594a76c0f37da20791b1ce4e2a4f5a3)。

GNSS 接收机启动模式（Receiver Start Modes）。

<a id="r_ga2b43ac2fec33053a769b7070c4ed3263"></a>

```c
enum gnss_pps_mode { GNSS_PPS_MODE_DISABLED = 0 , GNSS_PPS_MODE_ENABLED = 1 , GNSS_PPS_MODE_ENABLED_AFTER_LOCK = 2 , GNSS_PPS_MODE_ENABLED_WHILE_LOCKED = 3 }
```

相关声明：[gnss_pps_mode](#ga2b43ac2fec33053a769b7070c4ed3263)、[GNSS_PPS_MODE_DISABLED](#gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc)、[GNSS_PPS_MODE_ENABLED](#gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa)、[GNSS_PPS_MODE_ENABLED_AFTER_LOCK](#gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507)、[GNSS_PPS_MODE_ENABLED_WHILE_LOCKED](#gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc)。

GNSS 秒脉冲模式（PPS Modes）。

<a id="r_gadb734bb12433276d3014e08a1d21bb18"></a>

```c
enum gnss_navigation_mode { GNSS_NAVIGATION_MODE_ZERO_DYNAMICS = 0 , GNSS_NAVIGATION_MODE_LOW_DYNAMICS = 1 , GNSS_NAVIGATION_MODE_BALANCED_DYNAMICS = 2 , GNSS_NAVIGATION_MODE_HIGH_DYNAMICS = 3 }
```

相关声明：[gnss_navigation_mode](#gadb734bb12433276d3014e08a1d21bb18)、[GNSS_NAVIGATION_MODE_ZERO_DYNAMICS](#ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff)、[GNSS_NAVIGATION_MODE_LOW_DYNAMICS](#ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453)、[GNSS_NAVIGATION_MODE_BALANCED_DYNAMICS](#ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d)、[GNSS_NAVIGATION_MODE_HIGH_DYNAMICS](#ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f)。

GNSS 导航模式（Navigation Modes）。

<a id="r_ga928a05b4e820a9fcc8bc2db81f5f8c79"></a>

```c
enum gnss_system { GNSS_SYSTEM_GPS = BIT(0) , GNSS_SYSTEM_GLONASS = BIT(1) , GNSS_SYSTEM_GALILEO = BIT(2) , GNSS_SYSTEM_BEIDOU = BIT(3) , GNSS_SYSTEM_QZSS = BIT(4) , GNSS_SYSTEM_IRNSS = BIT(5) , GNSS_SYSTEM_SBAS = BIT(6) , GNSS_SYSTEM_IMES = BIT(7) }
```

相关声明：[gnss_system](#ga928a05b4e820a9fcc8bc2db81f5f8c79)、[GNSS_SYSTEM_GPS](#gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33)、[GNSS_SYSTEM_GLONASS](#gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd)、[GNSS_SYSTEM_GALILEO](#gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c)、[GNSS_SYSTEM_BEIDOU](#gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55)、[GNSS_SYSTEM_QZSS](#gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff)、[GNSS_SYSTEM_IRNSS](#gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242)、[GNSS_SYSTEM_SBAS](#gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd)、[GNSS_SYSTEM_IMES](#gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9)。

`gnss_systems_t` 中包含的卫星系统（Systems）。

<a id="r_ga15536308e2229a45493d06e8b61e63d9"></a>

```c
enum gnss_fix_status { GNSS_FIX_STATUS_NO_FIX = 0 , GNSS_FIX_STATUS_GNSS_FIX = 1 , GNSS_FIX_STATUS_DGNSS_FIX = 2 , GNSS_FIX_STATUS_ESTIMATED_FIX = 3 }
```

相关声明：[gnss_fix_status](#ga15536308e2229a45493d06e8b61e63d9)、[GNSS_FIX_STATUS_NO_FIX](#gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe)、[GNSS_FIX_STATUS_GNSS_FIX](#gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343)、[GNSS_FIX_STATUS_DGNSS_FIX](#gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc)、[GNSS_FIX_STATUS_ESTIMATED_FIX](#gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb)。

GNSS 定位状态（Fix Status）。

<a id="r_gacf5a3464c487ae7609d526c73ccc758a"></a>

```c
enum gnss_fix_quality { GNSS_FIX_QUALITY_INVALID = 0 , GNSS_FIX_QUALITY_GNSS_SPS = 1 , GNSS_FIX_QUALITY_DGNSS = 2 , GNSS_FIX_QUALITY_GNSS_PPS = 3 , GNSS_FIX_QUALITY_RTK = 4 , GNSS_FIX_QUALITY_FLOAT_RTK = 5 , GNSS_FIX_QUALITY_ESTIMATED = 6 }
```

相关声明：[gnss_fix_quality](#gacf5a3464c487ae7609d526c73ccc758a)、[GNSS_FIX_QUALITY_INVALID](#ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30)、[GNSS_FIX_QUALITY_GNSS_SPS](#ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f)、[GNSS_FIX_QUALITY_DGNSS](#ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8)、[GNSS_FIX_QUALITY_GNSS_PPS](#ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f)、[GNSS_FIX_QUALITY_RTK](#ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6)、[GNSS_FIX_QUALITY_FLOAT_RTK](#ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6)、[GNSS_FIX_QUALITY_ESTIMATED](#ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a)。

GNSS 定位质量（Fix Quality）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.7\_函数（Functions）

<a id="r_ga6bdabc1e89f5c7b10c1099fa74e6c6ca"></a>

```c
int gnss_start (const struct device *dev, enum gnss_start_mode mode)
```

相关声明：[gnss_start](#ga6bdabc1e89f5c7b10c1099fa74e6c6ca)、[device](../device_reference/P002_设备对象结构.md)、[gnss_start_mode](#ga7106633a65ddaa29e19ba9f15b86f0f9)。

启动 GNSS 接收机引擎（Receiver Engine）。

<a id="r_ga43f285927c94079e3b72e81303cff520"></a>

```c
int gnss_stop (const struct device *dev)
```

相关声明：[gnss_stop](#ga43f285927c94079e3b72e81303cff520)、[device](../device_reference/P002_设备对象结构.md)。

停止 GNSS 接收机引擎（Receiver Engine）。

<a id="r_ga16e8326737f114bd6017983812c7f28d"></a>

```c
int gnss_set_fix_rate (const struct device *dev, uint32_t fix_interval_ms)
```

相关声明：[gnss_set_fix_rate](#ga16e8326737f114bd6017983812c7f28d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 GNSS 定位更新率（Fix Rate）。

<a id="r_ga8e625fb3f8758eab78c115d12bef6a72"></a>

```c
int gnss_get_fix_rate (const struct device *dev, uint32_t *fix_interval_ms)
```

相关声明：[gnss_get_fix_rate](#ga8e625fb3f8758eab78c115d12bef6a72)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 GNSS 定位更新率（Fix Rate）。

<a id="r_ga9d0347640e68d5702b1cb43ddf8380df"></a>

```c
int gnss_set_navigation_mode (const struct device *dev, enum gnss_navigation_mode mode)
```

相关声明：[gnss_set_navigation_mode](#ga9d0347640e68d5702b1cb43ddf8380df)、[device](../device_reference/P002_设备对象结构.md)、[gnss_navigation_mode](#gadb734bb12433276d3014e08a1d21bb18)。

设置 GNSS 导航模式（Navigation Mode）。

<a id="r_gae5614f8125dad02a3ebd30400b575e6d"></a>

```c
int gnss_get_navigation_mode (const struct device *dev, enum gnss_navigation_mode *mode)
```

相关声明：[gnss_get_navigation_mode](#gae5614f8125dad02a3ebd30400b575e6d)、[device](../device_reference/P002_设备对象结构.md)、[gnss_navigation_mode](#gadb734bb12433276d3014e08a1d21bb18)。

获取 GNSS 导航模式（Navigation Mode）。

<a id="r_ga818e42c7a979623679eba26887662823"></a>

```c
int gnss_set_enabled_systems (const struct device *dev, gnss_systems_t systems)
```

相关声明：[gnss_set_enabled_systems](#ga818e42c7a979623679eba26887662823)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](#ga731907f9ae501909bf26ecae5441a5ce)。

设置启用的 GNSS 卫星系统（Enabled Systems）。

<a id="r_ga155126e113195c08158ef49e2a6b4f6a"></a>

```c
int gnss_get_enabled_systems (const struct device *dev, gnss_systems_t *systems)
```

相关声明：[gnss_get_enabled_systems](#ga155126e113195c08158ef49e2a6b4f6a)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](#ga731907f9ae501909bf26ecae5441a5ce)。

获取启用的 GNSS 卫星系统（Enabled Systems）。

<a id="r_ga598609846ff196ff300fcad8237b2d51"></a>

```c
int gnss_get_supported_systems (const struct device *dev, gnss_systems_t *systems)
```

相关声明：[gnss_get_supported_systems](#ga598609846ff196ff300fcad8237b2d51)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](#ga731907f9ae501909bf26ecae5441a5ce)。

获取支持的 GNSS 卫星系统（Supported Systems）。

<a id="r_ga8eb37446d71c020e0517a406ea240fc2"></a>

```c
int gnss_get_latest_timepulse (const struct device *dev, k_ticks_t *timestamp)
```

相关声明：[gnss_get_latest_timepulse](#ga8eb37446d71c020e0517a406ea240fc2)、[device](../device_reference/P002_设备对象结构.md)、[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)。

获取最近一次秒脉冲（PPS Timepulse）的时间戳（Timestamp）。

## 9.8\_详细说明（Detailed Documentation）

<a id="gae9c3fd5804bd6f8e6790cb1b7e47e4a6"></a>

### `GNSS_DATA_CALLBACK_DEFINE`

```c
#define GNSS_DATA_CALLBACK_DEFINE ( _dev, _callback )
```

```c
#include <zephyr/drivers/gnss.h>
```

为发布的全球导航卫星系统（GNSS）数据注册回调结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_dev` | 设备指针（Device Pointer）。 |
| `_callback` | 回调函数（Callback Function），参见 `gnss_data_callback_t`。 |

<a id="ga00d744003c1c8f71f06a685ecb8d07b1"></a>

### `GNSS_DT_DATA_CALLBACK_DEFINE`

```c
#define GNSS_DT_DATA_CALLBACK_DEFINE ( _node_id, _callback )
```

```c
#include <zephyr/drivers/gnss.h>
```

<a id="ga794cc5cadc7a7f470b6f57395bf333f1"></a>

### `GNSS_DT_SATELLITES_CALLBACK_DEFINE`

```c
#define GNSS_DT_SATELLITES_CALLBACK_DEFINE ( _node_id, _callback )
```

```c
#include <zephyr/drivers/gnss.h>
```

<a id="ga414a414635e1cd00ef800edaf70bc234"></a>

### `GNSS_SATELLITES_CALLBACK_DEFINE`

```c
#define GNSS_SATELLITES_CALLBACK_DEFINE ( _dev, _callback )
```

```c
#include <zephyr/drivers/gnss.h>
```

为发布的 GNSS 卫星信息（Satellites）注册回调结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_dev` | 设备指针（Device Pointer）。 |
| `_callback` | 回调函数（Callback Function），参见 `gnss_satellites_callback_t`。 |

<a id="ga025c965369275ad8e5ab5ad44c14a23b"></a>

### `gnss_data_callback_t`

```c
typedef void(* gnss_data_callback_t) (const struct device *dev, const struct gnss_data *data)
```

```c
#include <zephyr/drivers/gnss.h>
```

GNSS 数据回调模板（Data Callback Template）。

<a id="ga80cf700468d1c942cfa064368e212e6f"></a>

### `gnss_satellites_callback_t`

```c
typedef void(* gnss_satellites_callback_t) (const struct device *dev, const struct gnss_satellite *satellites, uint16_t size)
```

```c
#include <zephyr/drivers/gnss.h>
```

GNSS 卫星信息回调模板（Satellites Callback Template）。

<a id="ga731907f9ae501909bf26ecae5441a5ce"></a>

### `gnss_systems_t`

```c
typedef uint32_t gnss_systems_t
```

```c
#include <zephyr/drivers/gnss.h>
```

保存 GNSS 系统位掩码（System Bitmask）的类型。

<a id="gacf5a3464c487ae7609d526c73ccc758a"></a>

### `gnss_fix_quality`

```c
enum gnss_fix_quality
```

```c
#include <zephyr/drivers/gnss.h>
```

GNSS 定位质量（Fix Quality）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `GNSS_FIX_QUALITY_INVALID` | 无效定位（Invalid Fix）。 |
| `GNSS_FIX_QUALITY_GNSS_SPS` | 标准定位服务（Standard Positioning Service）。 |
| `GNSS_FIX_QUALITY_DGNSS` | 差分全球导航卫星系统（Differential GNSS）。 |
| `GNSS_FIX_QUALITY_GNSS_PPS` | 精密定位服务（Precise Positioning Service）。 |
| `GNSS_FIX_QUALITY_RTK` | 实时动态定位（Real-time Kinematic，RTK）。 |
| `GNSS_FIX_QUALITY_FLOAT_RTK` | 浮点实时动态定位（Floating Real-time Kinematic）。 |
| `GNSS_FIX_QUALITY_ESTIMATED` | 估算定位（Estimated Fix）。 |

<a id="ga15536308e2229a45493d06e8b61e63d9"></a>

### `gnss_fix_status`

```c
enum gnss_fix_status
```

```c
#include <zephyr/drivers/gnss.h>
```

GNSS 定位状态（Fix Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `GNSS_FIX_STATUS_NO_FIX` | 尚未获得 GNSS 定位（GNSS Fix）。 |
| `GNSS_FIX_STATUS_GNSS_FIX` | 已获得 GNSS 定位（GNSS Fix）。 |
| `GNSS_FIX_STATUS_DGNSS_FIX` | 已获得差分 GNSS 定位（Differential GNSS Fix）。 |
| `GNSS_FIX_STATUS_ESTIMATED_FIX` | 已获得估算定位（Estimated Fix）。 |

<a id="gadb734bb12433276d3014e08a1d21bb18"></a>

### `gnss_navigation_mode`

```c
enum gnss_navigation_mode
```

```c
#include <zephyr/drivers/gnss.h>
```

GNSS 导航模式（Navigation Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `GNSS_NAVIGATION_MODE_ZERO_DYNAMICS` | 动态特性（Dynamics）对跟踪（Tracking）没有影响。 |
| `GNSS_NAVIGATION_MODE_LOW_DYNAMICS` | 低动态（Low Dynamics）对跟踪（Tracking）的影响更大。 |
| `GNSS_NAVIGATION_MODE_BALANCED_DYNAMICS` | 低动态和高动态（Low and High Dynamics）对跟踪（Tracking）的影响相同。 |
| `GNSS_NAVIGATION_MODE_HIGH_DYNAMICS` | 高动态（High Dynamics）对跟踪（Tracking）的影响更大。 |

<a id="ga2b43ac2fec33053a769b7070c4ed3263"></a>

### `gnss_pps_mode`

```c
enum gnss_pps_mode
```

```c
#include <zephyr/drivers/gnss.h>
```

GNSS 秒脉冲模式（PPS Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `GNSS_PPS_MODE_DISABLED` | 禁用秒脉冲输出（PPS Output）。 |
| `GNSS_PPS_MODE_ENABLED` | 始终启用秒脉冲输出（PPS Output）。 |
| `GNSS_PPS_MODE_ENABLED_AFTER_LOCK` | 从首次锁定（First Lock）开始启用秒脉冲输出（PPS Output）。 |
| `GNSS_PPS_MODE_ENABLED_WHILE_LOCKED` | 锁定（Locked）期间启用秒脉冲输出（PPS Output）。 |

<a id="ga7106633a65ddaa29e19ba9f15b86f0f9"></a>

### `gnss_start_mode`

```c
enum gnss_start_mode
```

```c
#include <zephyr/drivers/gnss.h>
```

GNSS 接收机启动模式（Receiver Start Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `GNSS_HOT_START` | 保留全部导航数据（Navigation Data）重新启动，首次定位时间（TTFF）最短。 |
| `GNSS_WARM_START` | 清除星历（Ephemeris）重新启动，保留历书（Almanac）和位置（Position）。 |
| `GNSS_COLD_START` | 清除全部导航数据（Navigation Data）重新启动，首次定位时间（TTFF）最长。 |

<a id="ga928a05b4e820a9fcc8bc2db81f5f8c79"></a>

### `gnss_system`

```c
enum gnss_system
```

```c
#include <zephyr/drivers/gnss.h>
```

`gnss_systems_t` 中包含的卫星系统（Systems）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `GNSS_SYSTEM_GPS` | 全球定位系统（Global Positioning System，GPS）。 |
| `GNSS_SYSTEM_GLONASS` | 格洛纳斯全球导航卫星系统（GLObal NAvigation Satellite System，GLONASS）。 |
| `GNSS_SYSTEM_GALILEO` | 伽利略（Galileo）。 |
| `GNSS_SYSTEM_BEIDOU` | 北斗导航卫星系统（BeiDou Navigation Satellite System）。 |
| `GNSS_SYSTEM_QZSS` | 准天顶卫星系统（Quasi-Zenith Satellite System，QZSS）。 |
| `GNSS_SYSTEM_IRNSS` | 印度区域导航卫星系统（Indian Regional Navigation Satellite System，IRNSS）。 |
| `GNSS_SYSTEM_SBAS` | 星基增强系统（Satellite-Based Augmentation System，SBAS）。 |
| `GNSS_SYSTEM_IMES` | 室内消息系统（Indoor Messaging System，IMES）。 |

<a id="ga155126e113195c08158ef49e2a6b4f6a"></a>

### `gnss_get_enabled_systems()`

```c
int gnss_get_enabled_systems ( const struct device * dev, gnss_systems_t * systems )
```

```c
#include <zephyr/drivers/gnss.h>
```

获取启用的 GNSS 卫星系统（Enabled Systems）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |
| `systems` | 用于存储已启用系统（Enabled Systems）的目标位置。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；失败时为 `-errno`，即负的 errno 错误码。

<a id="ga8e625fb3f8758eab78c115d12bef6a72"></a>

### `gnss_get_fix_rate()`

```c
int gnss_get_fix_rate ( const struct device * dev, uint32_t * fix_interval_ms )
```

```c
#include <zephyr/drivers/gnss.h>
```

获取 GNSS 定位更新率（Fix Rate）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |
| `fix_interval_ms` | 用于存储定位间隔（Fix Interval）的目标位置，以毫秒为单位。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；失败时为 `-errno`，即负的 errno 错误码。

<a id="ga8eb37446d71c020e0517a406ea240fc2"></a>

### `gnss_get_latest_timepulse()`

```c
int gnss_get_latest_timepulse ( const struct device * dev, k_ticks_t * timestamp )
```

```c
#include <zephyr/drivers/gnss.h>
```

获取最近一次秒脉冲（PPS Timepulse）的时间戳（Timestamp）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |
| `timestamp` | 秒脉冲（PPS Pulse）发生时的内核节拍计数（Kernel Tick Count）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOSYS` | 驱动不支持该 API 时。 |
| `-ENOTSUP` | 驱动未连接秒脉冲引脚（PPS Pin）时。 |
| `-EAGAIN` | 秒脉冲（PPS Pulse）被判定为无效时。 |

**说明（Note）**：注意（Note）：时间脉冲引脚（Timepulse Pin）正在持续翻转时，时间戳（Timestamp）被视为有效。

<a id="gae5614f8125dad02a3ebd30400b575e6d"></a>

### `gnss_get_navigation_mode()`

```c
int gnss_get_navigation_mode ( const struct device * dev, enum gnss_navigation_mode * mode )
```

```c
#include <zephyr/drivers/gnss.h>
```

获取 GNSS 导航模式（Navigation Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |
| `mode` | 用于存储导航模式（Navigation Mode）的目标位置。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；失败时为 `-errno`，即负的 errno 错误码。

<a id="ga598609846ff196ff300fcad8237b2d51"></a>

### `gnss_get_supported_systems()`

```c
int gnss_get_supported_systems ( const struct device * dev, gnss_systems_t * systems )
```

```c
#include <zephyr/drivers/gnss.h>
```

获取支持的 GNSS 卫星系统（Supported Systems）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |
| `systems` | 用于存储受支持系统（Supported Systems）的目标位置。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；失败时为 `-errno`，即负的 errno 错误码。

<a id="ga818e42c7a979623679eba26887662823"></a>

### `gnss_set_enabled_systems()`

```c
int gnss_set_enabled_systems ( const struct device * dev, gnss_systems_t systems )
```

```c
#include <zephyr/drivers/gnss.h>
```

设置启用的 GNSS 卫星系统（Enabled Systems）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |
| `systems` | 要启用的系统（Systems）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；失败时为 `-errno`，即负的 errno 错误码。

<a id="ga16e8326737f114bd6017983812c7f28d"></a>

### `gnss_set_fix_rate()`

```c
int gnss_set_fix_rate ( const struct device * dev, uint32_t fix_interval_ms )
```

```c
#include <zephyr/drivers/gnss.h>
```

设置 GNSS 定位更新率（Fix Rate）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |
| `fix_interval_ms` | 要设置的定位间隔（Fix Interval），以毫秒为单位。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；失败时为 `-errno`，即负的 errno 错误码。

<a id="ga9d0347640e68d5702b1cb43ddf8380df"></a>

### `gnss_set_navigation_mode()`

```c
int gnss_set_navigation_mode ( const struct device * dev, enum gnss_navigation_mode mode )
```

```c
#include <zephyr/drivers/gnss.h>
```

设置 GNSS 导航模式（Navigation Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |
| `mode` | 要设置的导航模式（Navigation Mode）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；失败时为 `-errno`，即负的 errno 错误码。

<a id="ga6bdabc1e89f5c7b10c1099fa74e6c6ca"></a>

### `gnss_start()`

```c
int gnss_start ( const struct device * dev, enum gnss_start_mode mode )
```

```c
#include <zephyr/drivers/gnss.h>
```

启动 GNSS 接收机引擎（Receiver Engine）。

启动或恢复 GNSS 接收机引擎（Receiver Engine）。`mode` 控制重新启动时保留哪些导航数据（Navigation Data），用于在首次定位时间（Time-to-first-fix）与最初几次定位的精度之间取舍。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |
| `mode` | 启动模式（Start Mode）：`GNSS_HOT_START`、`GNSS_WARM_START` 或 `GNSS_COLD_START`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOSYS` | 驱动不支持本函数（Function）。 |
| `-ENODEV` | 设备尚未启动，电源管理（PM）尚未恢复。 |
| `-EINVAL` | 模式（Mode）无效。 |
| `-errno` | 其他驱动特定错误（Driver-specific Error）。 |

<a id="ga43f285927c94079e3b72e81303cff520"></a>

### `gnss_stop()`

```c
int gnss_stop ( const struct device * dev)
```

```c
#include <zephyr/drivers/gnss.h>
```

停止 GNSS 接收机引擎（Receiver Engine）。

指示接收机停止位置计算（Position Computation），同时保持通信链路（Communication Link）打开。调用 `gnss_start()` 可恢复。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例（Device Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOSYS` | 驱动不支持本函数（Function）。 |
| `-ENODEV` | 设备尚未启动，电源管理（PM）尚未恢复。 |
| `-errno` | 其他驱动特定错误（Driver-specific Error）。 |


## 9.9\_原页交叉引用（Cross References）

- [GNSS 驱动后端 API（Driver Backend API）](../api_bridge_paging_topic_reference/P003_GNSS 驱动后端 API（Driver Backend API）.md)
- [gnss.h](../api_file_serial_motion_reference/P003_zephyr__drivers__gnss.h_文件参考.md)
- [gnss_info](../sensor_navigation_model_reference/P012_gnss_info_结构体.md)
- [gnss_time](../sensor_navigation_model_reference/P017_gnss_time_结构体.md)
- [gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)
- [gnss_data_callback](../sensor_navigation_model_reference/P010_gnss_data_callback_结构体.md)
- [gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)
- [gnss_satellites_callback](../sensor_navigation_model_reference/P016_gnss_satellites_callback_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30"></a>
<a id="ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f"></a>
<a id="ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8"></a>
<a id="ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f"></a>
<a id="ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6"></a>
<a id="ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6"></a>
<a id="ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a"></a>
<a id="gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe"></a>
<a id="gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343"></a>
<a id="gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc"></a>
<a id="gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb"></a>
<a id="ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff"></a>
<a id="ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453"></a>
<a id="ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d"></a>
<a id="ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f"></a>
<a id="gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc"></a>
<a id="gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa"></a>
<a id="gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507"></a>
<a id="gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc"></a>
<a id="gga7106633a65ddaa29e19ba9f15b86f0f9ad0ecfd51dd2e99b5bd7e8abd49143da7"></a>
<a id="gga7106633a65ddaa29e19ba9f15b86f0f9adff054d3999e9f0c2f3c6efc96772cc8"></a>
<a id="gga7106633a65ddaa29e19ba9f15b86f0f9af594a76c0f37da20791b1ce4e2a4f5a3"></a>
<a id="gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33"></a>
<a id="gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd"></a>
<a id="gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c"></a>
<a id="gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55"></a>
<a id="gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff"></a>
<a id="gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242"></a>
<a id="gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd"></a>
<a id="gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_ESP32 Wi-Fi 网状网络（Wi-Fi Mesh）.md) · [返回大纲](大纲.md) · [下一章](P010_映像管理（Image Management）.md)
