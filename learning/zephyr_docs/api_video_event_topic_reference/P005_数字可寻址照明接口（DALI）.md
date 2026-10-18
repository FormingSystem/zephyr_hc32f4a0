---
id: learning.zephyr-docs.api-video-event-topic-reference.page-5
title: 数字可寻址照明接口（DALI）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_数字可寻址照明接口（DALI）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DALI 接口（Interface）

<a id="details"></a>

数字可寻址照明接口（DALI）。自 4.4 起提供，版本 0.1.0。DALI API 提供符合 IEC 62386 的底层通信支持。

<a id="header-groups"></a>
<a id="groups"></a>

## 5.1\_主题（Topics）

<a id="r_dali_5Finterface_5Fbackend"></a>

相关声明：[DALI 驱动后端 API（Driver Backend API）](../api_extension_topic_reference/P010_DALI 驱动后端 API（Driver Backend API）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 5.2\_文件（Files）

<a id="r_dali_2Eh"></a>

```c
file dali.h
```

相关声明：[dali.h](../peripheral_bus_storage_header_reference/P001_zephyr__drivers__dali.h_头文件参考.md)。

数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）的驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.3\_数据结构（Data Structures）

<a id="r_dali_5Fframe"></a>

```c
struct dali_frame
```

相关声明：[dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)。

数字可寻址照明接口（DALI）的帧结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.4\_类型定义（Typedefs）

<a id="r_ga7fc3646c3814fb3bebba8e77e0c0d424"></a>

```c
typedef void(* dali_receive_callback_t) (const struct device *dev, struct dali_frame frame, void *user_data)
```

相关声明：[dali_receive_callback_t](#ga7fc3646c3814fb3bebba8e77e0c0d424)、[device](../device_reference/P002_设备对象结构.md)、[dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)。

定义用于接收 DALI 帧的应用程序回调处理函数签名（Function signature）。

<a id="r_ga7ab4bdd2312ee38e473e7a2b56983166"></a>

```c
typedef void(* dali_transmit_callback_t) (const struct device *dev, int error, void *user_data)
```

相关声明：[dali_transmit_callback_t](#ga7ab4bdd2312ee38e473e7a2b56983166)、[device](../device_reference/P002_设备对象结构.md)。

定义用于发送 DALI 帧的应用程序回调处理函数签名。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.5\_枚举（Enumerations）

<a id="r_ga0e295a9e86bc694d1516cb50cb579f91"></a>

```c
enum dali_event_type { DALI_FRAME_CORRUPT , DALI_FRAME_BACKWARD , DALI_FRAME_GEAR , DALI_FRAME_DEVICE , DALI_FRAME_FIRMWARE , DALI_EVENT_BUS_FAILURE , DALI_EVENT_BUS_IDLE }
```

相关声明：[dali_event_type](#ga0e295a9e86bc694d1516cb50cb579f91)、[DALI_FRAME_CORRUPT](#gga0e295a9e86bc694d1516cb50cb579f91a83871ac60c4dc5461b8284f10c0a0b65)、[DALI_FRAME_BACKWARD](#gga0e295a9e86bc694d1516cb50cb579f91a7468d402b7b1068f8d513eee733a4941)、[DALI_FRAME_GEAR](#gga0e295a9e86bc694d1516cb50cb579f91acd8816fb935ec5bd21d26a8ba8cf8a4e)、[DALI_FRAME_DEVICE](#gga0e295a9e86bc694d1516cb50cb579f91a6e641806624668e934197ce903a61718)、[DALI_FRAME_FIRMWARE](#gga0e295a9e86bc694d1516cb50cb579f91aae27944de3b26b455b91f9e4cbc4b7cf)、[DALI_EVENT_BUS_FAILURE](#gga0e295a9e86bc694d1516cb50cb579f91a6ba6fe5f5bc598601ee8593b2d7b995d)、[DALI_EVENT_BUS_IDLE](#gga0e295a9e86bc694d1516cb50cb579f91acce7255d3368342e6dadf4321be23962)。

DALI 帧类型（Frame types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.6\_函数（Functions）

<a id="r_ga79f624e680f364a0790119b3d5e09083"></a>

```c
int dali_set_receive_callback (const struct device *dev, dali_receive_callback_t callback, void *user_data)
```

相关声明：[dali_set_receive_callback](#ga79f624e680f364a0790119b3d5e09083)、[device](../device_reference/P002_设备对象结构.md)、[dali_receive_callback_t](#ga7fc3646c3814fb3bebba8e77e0c0d424)。

设置接收 DALI 总线帧的回调函数。

<a id="r_gac25513281a022dce8bfe4a2fe46b609e"></a>

```c
int dali_transmit (const struct device *dev, const struct dali_frame *frame, dali_transmit_callback_t callback, void *user_data)
```

相关声明：[dali_transmit](#gac25513281a022dce8bfe4a2fe46b609e)、[device](../device_reference/P002_设备对象结构.md)、[dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)、[dali_transmit_callback_t](#ga7ab4bdd2312ee38e473e7a2b56983166)。

在 DALI 总线上发送帧。

## 5.7\_详细说明（Detailed Documentation）

<a id="ga7fc3646c3814fb3bebba8e77e0c0d424"></a>

### `dali_receive_callback_t`

```c
typedef void(* dali_receive_callback_t) (const struct device *dev, struct dali_frame frame, void *user_data)
```

```c
#include <zephyr/drivers/dali.h>
```

定义用于接收 DALI 帧的应用程序回调处理函数签名（Function signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体的指针。 |
| `frame` | 已接收的 DALI 帧（Frame）。 |
| `user_data` | 设置回调函数时提供的用户数据（User Data）。 |

<a id="ga7ab4bdd2312ee38e473e7a2b56983166"></a>

### `dali_transmit_callback_t`

```c
typedef void(* dali_transmit_callback_t) (const struct device *dev, int error, void *user_data)
```

```c
#include <zephyr/drivers/dali.h>
```

定义用于发送 DALI 帧的应用程序回调处理函数签名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构体的指针。 |
| `error` | 事务（Transaction）的错误码。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `user_data` | 发送帧（Frame）时提供的用户数据（User Data）。 |

**参阅（See Also）**：另请参见：`dali_transmit`。

<a id="ga0e295a9e86bc694d1516cb50cb579f91"></a>

### `dali_event_type`

```c
enum dali_event_type
```

```c
#include <zephyr/drivers/dali.h>
```

DALI 帧类型（Frame types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DALI_FRAME_CORRUPT` | 损坏帧（Corrupt Frame），适用于发送／接收。 |
| `DALI_FRAME_BACKWARD` | 反向 8 位帧（Backward 8-bit Frame），适用于发送／接收。 |
| `DALI_FRAME_GEAR` | 前向 16 位控制装置帧（Forward 16-bit Gear Frame），适用于发送／接收。 |
| `DALI_FRAME_DEVICE` | 前向 24 位设备帧（Forward 24-bit Device Frame），适用于发送／接收。 |
| `DALI_FRAME_FIRMWARE` | 前向 32 位固件帧（Forward 32-bit Firmware Frame），适用于发送／接收。 |
| `DALI_EVENT_BUS_FAILURE` | 检测到总线故障（Bus Failure），仅适用于接收。 |
| `DALI_EVENT_BUS_IDLE` | 检测到总线在故障后重新空闲（Idle），仅适用于接收。 |

<a id="ga79f624e680f364a0790119b3d5e09083"></a>

### `dali_set_receive_callback()`

```c
int dali_set_receive_callback ( const struct device * dev, dali_receive_callback_t callback, void * user_data )
```

```c
#include <zephyr/drivers/dali.h>
```

设置接收 DALI 总线帧的回调函数。

为 DALI 驱动设置回调函数（Callback Function）。每当完整接收到 DALI 帧或检测到相关总线事件时，都会在驱动的工作队列上下文（Workqueue Context）中调用回调。每个驱动实例仅支持一个回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向该驱动实例的 DALI 设备结构体（Device Structure）的指针。 |
| `callback` | 每当收到帧或检测到相关事件时，DALI 驱动都会调用此函数。 |
| `user_data` | 要传递给回调函数（Callback Function）的用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOSYS` | 未实现此函数时。 |

**说明（Note）**：注意：回调函数在停止条件（Stop Condition）结束时调用。帧间时序（Interframe Timings）必须考虑这一点。

<a id="gac25513281a022dce8bfe4a2fe46b609e"></a>

### `dali_transmit()`

```c
int dali_transmit ( const struct device * dev, const struct dali_frame * frame, dali_transmit_callback_t callback, void * user_data )
```

```c
#include <zephyr/drivers/dali.h>
```

在 DALI 总线上发送帧。

立即开始向 DALI 总线发送 DALI 帧。发生错误时，驱动不会自动重传（Re-transmit）该帧。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向该驱动实例的 DALI 设备结构体（Device Structure）的指针。 |
| `frame` | 要发送的 DALI 帧（Frame）。 |
| `callback` | 可选回调，在帧成功发送或检测到发送错误时调用。回调在驱动的工作队列上下文（Workqueue Context）中执行。回调的 `err` 参数含义请参见 `dali_transmit` 的返回码。 |
| `user_data` | 要传递给回调函数（Callback Function）的用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EBUSY` | 有帧正在发送（Frame Transmission Active）时。 |
| `-EINVAL` | 传给函数的参数无效（Invalid Parameter）时。 |
| `-ECANCELED` | 发送让位于显性帧（Dominant Frame）时。 |
| `-ECOMM` | 发送期间发生冲突（Collision）时。 |
| `-EAGAIN` | 总线不可用（Bus Unavailable）时。 |
| `-ENOSYS` | 未实现此函数时。 |


## 5.8\_原页交叉引用（Cross References）

- [DALI 驱动后端 API（Driver Backend API）](../api_extension_topic_reference/P010_DALI 驱动后端 API（Driver Backend API）.md)
- [dali.h](../peripheral_bus_storage_header_reference/P001_zephyr__drivers__dali.h_头文件参考.md)
- [dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0e295a9e86bc694d1516cb50cb579f91a83871ac60c4dc5461b8284f10c0a0b65"></a>
<a id="gga0e295a9e86bc694d1516cb50cb579f91a7468d402b7b1068f8d513eee733a4941"></a>
<a id="gga0e295a9e86bc694d1516cb50cb579f91acd8816fb935ec5bd21d26a8ba8cf8a4e"></a>
<a id="gga0e295a9e86bc694d1516cb50cb579f91a6e641806624668e934197ce903a61718"></a>
<a id="gga0e295a9e86bc694d1516cb50cb579f91aae27944de3b26b455b91f9e4cbc4b7cf"></a>
<a id="gga0e295a9e86bc694d1516cb50cb579f91a6ba6fe5f5bc598601ee8593b2d7b995d"></a>
<a id="gga0e295a9e86bc694d1516cb50cb579f91acce7255d3368342e6dadf4321be23962"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_蓝牙 Mesh 设备固件更新（Device Firmware Update）.md) · [返回大纲](大纲.md) · [下一章](P006_调制解调器管道（Modem Pipe）.md)
