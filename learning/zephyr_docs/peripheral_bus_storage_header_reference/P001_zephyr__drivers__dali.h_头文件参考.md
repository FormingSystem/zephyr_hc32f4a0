---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-1
title: zephyr__drivers__dali.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dali_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_dali.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dali_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）的驱动API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/sys/clock.h>
#include <zephyr/sys/__assert.h>
#include <errno.h>
#include <stdbool.h>
#include <zephyr/syscalls/dali.h>
```

查看此文件的源码。

数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）的驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_dali_5Fframe"></a>

```c
struct dali_frame
```

相关声明：[dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)。

数字可寻址照明接口（DALI）的帧结构。

<a id="r_dali_5Fdriver_5Fapi"></a>

```c
struct dali_driver_api
```

相关声明：[dali_driver_api](../peripheral_bus_storage_model_reference/P001_dali_driver_api_结构体.md)。

驱动操作（Driver Operations）：数字可寻址照明接口（DALI）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_ga7fc3646c3814fb3bebba8e77e0c0d424"></a>

```c
typedef void(* dali_receive_callback_t) (const struct device *dev, struct dali_frame frame, void *user_data)
```

相关声明：[dali_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7fc3646c3814fb3bebba8e77e0c0d424)、[device](../device_reference/P002_设备对象结构.md)、[dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)。

定义用于接收 DALI 帧的应用程序回调处理函数签名（Function signature）。

<a id="r_ga7ab4bdd2312ee38e473e7a2b56983166"></a>

```c
typedef void(* dali_transmit_callback_t) (const struct device *dev, int error, void *user_data)
```

相关声明：[dali_transmit_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7ab4bdd2312ee38e473e7a2b56983166)、[device](../device_reference/P002_设备对象结构.md)。

定义用于发送 DALI 帧的应用程序回调处理函数签名。

<a id="r_ga00ceb1581576430fa6864a073eaa73b0"></a>

```c
typedef int(* dali_api_set_receive_callback_t) (const struct device *dev, dali_receive_callback_t callback, void *user_data)
```

相关声明：[dali_api_set_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#ga00ceb1581576430fa6864a073eaa73b0)、[device](../device_reference/P002_设备对象结构.md)、[dali_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7fc3646c3814fb3bebba8e77e0c0d424)。

用于接收 DALI 帧的 API。

<a id="r_gac6b54d7e448fd97e8936d4fd04177da0"></a>

```c
typedef int(* dali_api_transmit_t) (const struct device *dev, const struct dali_frame *frame, dali_transmit_callback_t callback, void *user_data)
```

相关声明：[dali_api_transmit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#gac6b54d7e448fd97e8936d4fd04177da0)、[device](../device_reference/P002_设备对象结构.md)、[dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)、[dali_transmit_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7ab4bdd2312ee38e473e7a2b56983166)。

用于发送 DALI 帧的 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_ga0e295a9e86bc694d1516cb50cb579f91"></a>

```c
enum dali_event_type { DALI_FRAME_CORRUPT , DALI_FRAME_BACKWARD , DALI_FRAME_GEAR , DALI_FRAME_DEVICE , DALI_FRAME_FIRMWARE , DALI_EVENT_BUS_FAILURE , DALI_EVENT_BUS_IDLE }
```

相关声明：[dali_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga0e295a9e86bc694d1516cb50cb579f91)、[DALI_FRAME_CORRUPT](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a83871ac60c4dc5461b8284f10c0a0b65)、[DALI_FRAME_BACKWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a7468d402b7b1068f8d513eee733a4941)、[DALI_FRAME_GEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91acd8816fb935ec5bd21d26a8ba8cf8a4e)、[DALI_FRAME_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a6e641806624668e934197ce903a61718)、[DALI_FRAME_FIRMWARE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91aae27944de3b26b455b91f9e4cbc4b7cf)、[DALI_EVENT_BUS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a6ba6fe5f5bc598601ee8593b2d7b995d)、[DALI_EVENT_BUS_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91acce7255d3368342e6dadf4321be23962)。

DALI 帧类型（Frame types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga79f624e680f364a0790119b3d5e09083"></a>

```c
int dali_set_receive_callback (const struct device *dev, dali_receive_callback_t callback, void *user_data)
```

相关声明：[dali_set_receive_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga79f624e680f364a0790119b3d5e09083)、[device](../device_reference/P002_设备对象结构.md)、[dali_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7fc3646c3814fb3bebba8e77e0c0d424)。

设置接收 DALI 总线帧的回调函数。

<a id="r_gac25513281a022dce8bfe4a2fe46b609e"></a>

```c
int dali_transmit (const struct device *dev, const struct dali_frame *frame, dali_transmit_callback_t callback, void *user_data)
```

相关声明：[dali_transmit](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gac25513281a022dce8bfe4a2fe46b609e)、[device](../device_reference/P002_设备对象结构.md)、[dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)、[dali_transmit_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7ab4bdd2312ee38e473e7a2b56983166)。

在 DALI 总线上发送帧。


## 1.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/dali_8h_source.html)
- [dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)
- [dali_driver_api](../peripheral_bus_storage_model_reference/P001_dali_driver_api_结构体.md)
- [dali_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7fc3646c3814fb3bebba8e77e0c0d424)
- [device](../device_reference/P002_设备对象结构.md)
- [dali_transmit_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7ab4bdd2312ee38e473e7a2b56983166)
- [dali_api_set_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#ga00ceb1581576430fa6864a073eaa73b0)
- [dali_api_transmit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#gac6b54d7e448fd97e8936d4fd04177da0)
- [dali_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga0e295a9e86bc694d1516cb50cb579f91)
- [DALI_FRAME_CORRUPT](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a83871ac60c4dc5461b8284f10c0a0b65)
- [DALI_FRAME_BACKWARD](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a7468d402b7b1068f8d513eee733a4941)
- [DALI_FRAME_GEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91acd8816fb935ec5bd21d26a8ba8cf8a4e)
- [DALI_FRAME_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a6e641806624668e934197ce903a61718)
- [DALI_FRAME_FIRMWARE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91aae27944de3b26b455b91f9e4cbc4b7cf)
- [DALI_EVENT_BUS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91a6ba6fe5f5bc598601ee8593b2d7b995d)
- [DALI_EVENT_BUS_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gga0e295a9e86bc694d1516cb50cb579f91acce7255d3368342e6dadf4321be23962)
- [dali_set_receive_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga79f624e680f364a0790119b3d5e09083)
- [dali_transmit](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gac25513281a022dce8bfe4a2fe46b609e)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__misc__devmux__devmux.h_头文件参考.md)
