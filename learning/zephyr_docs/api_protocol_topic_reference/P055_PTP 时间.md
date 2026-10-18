---
id: learning.zephyr-docs.api-protocol-topic-reference.page-55
title: PTP 时间
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_PTP 时间

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

精确时间协议时间规范（Precision Time Protocol time specification）。

<a id="details"></a>

精确时间协议时间表示（Precision Time Protocol time specification）。自 Zephyr 1.13 起提供；API 版本为 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 55.1\_数据结构（Data Structures）

<a id="r_net_5Fptp_5Ftime"></a>

```c
struct net_ptp_time
```

相关声明：[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)。

（通用）精确时间协议（(g)PTP）的时间戳格式。

<a id="r_net_5Fptp_5Fextended_5Ftime"></a>

```c
struct net_ptp_extended_time
```

相关声明：[net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)。

通用精确时间协议（gPTP）的扩展时间戳格式。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 55.2\_函数（Functions）

<a id="r_gaf9f253990e644e161e1b3cc317e8e9e9"></a>

```c
static net_time_t net_ptp_time_to_ns (struct net_ptp_time *ts)
```

相关声明：[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)、[net_ptp_time_to_ns](#gaf9f253990e644e161e1b3cc317e8e9e9)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)。

将精确时间协议时间戳（PTP Timestamp）转换为纳秒精度时间戳（Nanosecond Precision Timestamp），两者均相对于本地网络参考时钟（Local Network Reference Clock）。

<a id="r_gafd9d45cca3d630ce51109537165d53df"></a>

```c
static struct net_ptp_time ns_to_net_ptp_time (net_time_t nsec)
```

相关声明：[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[ns_to_net_ptp_time](#gafd9d45cca3d630ce51109537165d53df)、[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)。

将纳秒精度时间戳（Nanosecond Precision Timestamp）转换为精确时间协议时间戳（PTP Timestamp），两者均相对于本地网络参考时钟（Local Network Reference Clock）。

## 55.3\_详细说明（Detailed Documentation）

<a id="gaf9f253990e644e161e1b3cc317e8e9e9"></a>

### `net_ptp_time_to_ns()`

```c
net_time_t net_ptp_time_to_ns ( struct net_ptp_time * ts)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ptp_time.h>
```

将精确时间协议时间戳（PTP Timestamp）转换为纳秒精度时间戳（Nanosecond Precision Timestamp），两者均相对于本地网络参考时钟（Local Network Reference Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ts` | PTP 时间戳（timestamp）。 |

**说明（Note）**：注意：只有表示时长不超过约 290 年的时间戳才能转换为纳秒时间戳。更大的时间戳会返回纳秒精度时间戳所能表示的最大值。

**返回（Returns）**：返回值：对应的纳秒精度时间戳（nanosecond precision timestamp）。

<a id="gafd9d45cca3d630ce51109537165d53df"></a>

### `ns_to_net_ptp_time()`

```c
struct net_ptp_time ns_to_net_ptp_time ( net_time_t nsec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/ptp_time.h>
```

将纳秒精度时间戳（Nanosecond Precision Timestamp）转换为精确时间协议时间戳（PTP Timestamp），两者均相对于本地网络参考时钟（Local Network Reference Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nsec` | 纳秒精度时间戳。 |

**返回（Returns）**：返回值：对应的 PTP 时间戳。


## 55.4\_原页交叉引用（Cross References）

- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [zephyr/net/ptp_time.h](../api_file_runtime_reference/P052_zephyr__net__ptp_time.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P054_PTP 时钟驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P056_CH32复位控制器辅助定义（Reset Controller Helpers）.md)
