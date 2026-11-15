---
id: learning.zephyr-docs.api-file-service-reference.page-42
title: zephyr__drivers__ptp_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ptp__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_zephyr\_\_drivers\_\_ptp\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ptp__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

精确时间协议（Precision Time Protocol，PTP）时钟驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/sys/util.h>
#include <zephyr/net/ptp_time.h>
#include <zephyr/syscalls/ptp_clock.h>
```

查看此文件的源码。

精确时间协议（Precision Time Protocol，PTP）时钟驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 42.1\_数据结构（Data Structures）

<a id="r_ptp_5Fclock_5Fdriver_5Fapi"></a>

```c
struct ptp_clock_driver_api
```

相关声明：[ptp_clock_driver_api](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md)。

驱动操作（Driver Operations）：精确时间协议时钟（PTP Clock）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 42.2\_宏定义（Macros）

<a id="r_ga31fba0e7a6444b3301cbe0372e6d1996"></a>

```c
#define PTP_CLOCK_NAME "PTP_CLOCK"
```

相关声明：[PTP_CLOCK_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga31fba0e7a6444b3301cbe0372e6d1996)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 42.3\_类型定义（Typedefs）

<a id="r_gaeda56e624ddc47b5f23ebd090031982a"></a>

```c
typedef int(* ptp_clock_api_set_t) (const struct device *dev, struct net_ptp_time *tm)
```

相关声明：[ptp_clock_api_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gaeda56e624ddc47b5f23ebd090031982a)、[device](../device_reference/P002_设备对象结构.md)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

设置精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_ga59a1c7530e59fd19b3fa25ff6f4e346c"></a>

```c
typedef int(* ptp_clock_api_get_t) (const struct device *dev, struct net_ptp_time *tm)
```

相关声明：[ptp_clock_api_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#ga59a1c7530e59fd19b3fa25ff6f4e346c)、[device](../device_reference/P002_设备对象结构.md)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

获取精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_gad3b345ba7db470f274cffa33b1128810"></a>

```c
typedef int(* ptp_clock_api_adjust_t) (const struct device *dev, int increment)
```

相关声明：[ptp_clock_api_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gad3b345ba7db470f274cffa33b1128810)、[device](../device_reference/P002_设备对象结构.md)。

调整精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_gae94ee94813969d15f8dc841814562ac3"></a>

```c
typedef int(* ptp_clock_api_rate_adjust_t) (const struct device *dev, double ratio)
```

相关声明：[ptp_clock_api_rate_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gae94ee94813969d15f8dc841814562ac3)、[device](../device_reference/P002_设备对象结构.md)。

基于标称频率（Nominal Frequency）调整精确时间协议时钟（PTP Clock）的速率比（Rate Ratio）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 42.4\_函数（Functions）

<a id="r_ga41123183be722b3423d5e993d3cde7c2"></a>

```c
static int ptp_clock_set (const struct device *dev, struct net_ptp_time *tm)
```

相关声明：[ptp_clock_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga41123183be722b3423d5e993d3cde7c2)、[device](../device_reference/P002_设备对象结构.md)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

设置精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_ga443f97ef2766e87c0b42c6ad6f7b63b4"></a>

```c
int ptp_clock_get (const struct device *dev, struct net_ptp_time *tm)
```

相关声明：[ptp_clock_get](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga443f97ef2766e87c0b42c6ad6f7b63b4)、[device](../device_reference/P002_设备对象结构.md)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

获取精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_gabd11d19b5ec5491e5813bf7cb74ab9b0"></a>

```c
static int ptp_clock_adjust (const struct device *dev, int increment)
```

相关声明：[ptp_clock_adjust](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#gabd11d19b5ec5491e5813bf7cb74ab9b0)、[device](../device_reference/P002_设备对象结构.md)。

调整精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_ga310ee4974e6f3b01c4aa1b985194e57a"></a>

```c
static int ptp_clock_rate_adjust (const struct device *dev, double rate)
```

相关声明：[ptp_clock_rate_adjust](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga310ee4974e6f3b01c4aa1b985194e57a)、[device](../device_reference/P002_设备对象结构.md)。

基于标称频率（Nominal Frequency）调整精确时间协议时钟（PTP Clock）的速率比（Rate Ratio）。


## 42.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/net/ptp_time.h](../api_source_reference/P681_ptp_time.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P150_ptp_clock.h_源码浏览.md)
- [ptp_clock_driver_api](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md)
- [PTP_CLOCK_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga31fba0e7a6444b3301cbe0372e6d1996)
- [ptp_clock_api_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gaeda56e624ddc47b5f23ebd090031982a)
- [device](../device_reference/P002_设备对象结构.md)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [ptp_clock_api_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#ga59a1c7530e59fd19b3fa25ff6f4e346c)
- [ptp_clock_api_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gad3b345ba7db470f274cffa33b1128810)
- [ptp_clock_api_rate_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gae94ee94813969d15f8dc841814562ac3)
- [ptp_clock_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga41123183be722b3423d5e993d3cde7c2)
- [ptp_clock_get](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga443f97ef2766e87c0b42c6ad6f7b63b4)
- [ptp_clock_adjust](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#gabd11d19b5ec5491e5813bf7cb74ab9b0)
- [ptp_clock_rate_adjust](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga310ee4974e6f3b01c4aa1b985194e57a)

<a id="header-details"></a>

---

[上一章](P041_zephyr__net__ptp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P043_zephyr__dt-bindings__gpio__raspberrypi-csi-connector.h_文件参考.md)
