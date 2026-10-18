---
id: learning.zephyr-docs.api-protocol-topic-reference.page-53
title: 精确时间协议时钟（PTP Clock）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_精确时间协议时钟（PTP Clock）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

精确时间协议（Precision Time Protocol，PTP）时钟接口。

<a id="details"></a>

精确时间协议（Precision Time Protocol，PTP）时钟接口。自 Zephyr 1.13 起提供；API 版本为 1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 53.1\_主题（Topics）

<a id="r_ptp_5Fclock_5Finterface_5Fbackend"></a>

相关声明：[PTP 时钟驱动后端 API](P054_PTP 时钟驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 53.2\_文件（Files）

<a id="r_ptp_5Fclock_2Eh"></a>

```c
file ptp_clock.h
```

相关声明：[ptp_clock.h](../api_file_service_reference/P042_zephyr__drivers__ptp_clock.h_文件参考.md)。

精确时间协议（Precision Time Protocol，PTP）时钟驱动API的主头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 53.3\_宏定义（Macros）

<a id="r_ga31fba0e7a6444b3301cbe0372e6d1996"></a>

```c
#define PTP_CLOCK_NAME "PTP_CLOCK"
```

相关声明：[PTP_CLOCK_NAME](#ga31fba0e7a6444b3301cbe0372e6d1996)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 53.4\_函数（Functions）

<a id="r_ga41123183be722b3423d5e993d3cde7c2"></a>

```c
static int ptp_clock_set (const struct device *dev, struct net_ptp_time *tm)
```

相关声明：[ptp_clock_set](#ga41123183be722b3423d5e993d3cde7c2)、[device](../device_reference/P002_设备对象结构.md)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

设置精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_ga443f97ef2766e87c0b42c6ad6f7b63b4"></a>

```c
int ptp_clock_get (const struct device *dev, struct net_ptp_time *tm)
```

相关声明：[ptp_clock_get](#ga443f97ef2766e87c0b42c6ad6f7b63b4)、[device](../device_reference/P002_设备对象结构.md)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

获取精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_gabd11d19b5ec5491e5813bf7cb74ab9b0"></a>

```c
static int ptp_clock_adjust (const struct device *dev, int increment)
```

相关声明：[ptp_clock_adjust](#gabd11d19b5ec5491e5813bf7cb74ab9b0)、[device](../device_reference/P002_设备对象结构.md)。

调整精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_ga310ee4974e6f3b01c4aa1b985194e57a"></a>

```c
static int ptp_clock_rate_adjust (const struct device *dev, double rate)
```

相关声明：[ptp_clock_rate_adjust](#ga310ee4974e6f3b01c4aa1b985194e57a)、[device](../device_reference/P002_设备对象结构.md)。

基于标称频率（Nominal Frequency）调整精确时间协议时钟（PTP Clock）的速率比（Rate Ratio）。

## 53.5\_详细说明（Detailed Documentation）

<a id="ga31fba0e7a6444b3301cbe0372e6d1996"></a>

### `PTP_CLOCK_NAME`

```c
#define PTP_CLOCK_NAME "PTP_CLOCK"
```

```c
#include <zephyr/drivers/ptp_clock.h>
```

<a id="gabd11d19b5ec5491e5813bf7cb74ab9b0"></a>

### `ptp_clock_adjust()`

```c
int ptp_clock_adjust ( const struct device * dev, int increment )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/ptp_clock.h>
```

调整精确时间协议时钟（PTP Clock）的时间（Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PTP 时钟设备（clock device）。 |
| `increment` | 时钟增量（increment），单位为纳秒。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga443f97ef2766e87c0b42c6ad6f7b63b4"></a>

### `ptp_clock_get()`

```c
int ptp_clock_get ( const struct device * dev, struct net_ptp_time * tm )
```

```c
#include <zephyr/drivers/ptp_clock.h>
```

获取精确时间协议时钟（PTP Clock）的时间（Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PTP 时钟设备（clock device）。 |
| `tm` | 用于存储当前时间的位置。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga310ee4974e6f3b01c4aa1b985194e57a"></a>

### `ptp_clock_rate_adjust()`

```c
int ptp_clock_rate_adjust ( const struct device * dev, double rate )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/ptp_clock.h>
```

基于标称频率（Nominal Frequency）调整精确时间协议时钟（PTP Clock）的速率比（Rate Ratio）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PTP 时钟设备（clock device）。 |
| `rate` | 相对于其标称频率（nominal frequency）的速率比（rate ratio）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga41123183be722b3423d5e993d3cde7c2"></a>

### `ptp_clock_set()`

```c
int ptp_clock_set ( const struct device * dev, struct net_ptp_time * tm )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/ptp_clock.h>
```

设置精确时间协议时钟（PTP Clock）的时间（Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PTP 时钟设备（clock device）。 |
| `tm` | 要设置的时间。 |

返回（Returns）：成功时为0，出错时小于0。


## 53.6\_原页交叉引用（Cross References）

- [PTP 时钟驱动后端 API](P054_PTP 时钟驱动后端 API.md)
- [ptp_clock.h](../api_file_service_reference/P042_zephyr__drivers__ptp_clock.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P052_PS_2 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P054_PTP 时钟驱动后端 API.md)
