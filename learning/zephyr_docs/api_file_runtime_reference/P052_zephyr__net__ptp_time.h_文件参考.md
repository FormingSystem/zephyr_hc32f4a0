---
id: learning.zephyr-docs.api-file-runtime-reference.page-52
title: zephyr__net__ptp_time.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_zephyr\_\_net\_\_ptp\_time.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

精确时间协议（Precision Time Protocol）时间规格（Time Specification）的公共函数。

<a id="details"></a>

```c
#include <zephyr/net/net_core.h>
#include <zephyr/net/net_time.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

精确时间协议时间规范（Precision Time Protocol Time Specification）的公共函数。引用的规范为 2019 版 IEEE 1588（PTP）和 2020 版 IEEE 802.1AS（gPTP）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 52.1\_数据结构（Data Structures）

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

## 52.2\_函数（Functions）

<a id="r_gaf9f253990e644e161e1b3cc317e8e9e9"></a>

```c
static net_time_t net_ptp_time_to_ns (struct net_ptp_time *ts)
```

相关声明：[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)、[net_ptp_time_to_ns](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html#gaf9f253990e644e161e1b3cc317e8e9e9)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)。

将精确时间协议时间戳（PTP Timestamp）转换为纳秒精度时间戳（Nanosecond Precision Timestamp），两者均相对于本地网络参考时钟（Local Network Reference Clock）。

<a id="r_gafd9d45cca3d630ce51109537165d53df"></a>

```c
static struct net_ptp_time ns_to_net_ptp_time (net_time_t nsec)
```

相关声明：[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[ns_to_net_ptp_time](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html#gafd9d45cca3d630ce51109537165d53df)、[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)。

将纳秒精度时间戳（Nanosecond Precision Timestamp）转换为精确时间协议时间戳（PTP Timestamp），两者均相对于本地网络参考时钟（Local Network Reference Clock）。


## 52.3\_原页交叉引用（Cross References）

- [zephyr/net/net_core.h](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h_source.html)
- [zephyr/net/net_time.h](../api_source_supplement_reference/P125_net_time.h_源码浏览.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P681_ptp_time.h_源码浏览.md)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [net_ptp_time_to_ns](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html#gaf9f253990e644e161e1b3cc317e8e9e9)
- [ns_to_net_ptp_time](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html#gafd9d45cca3d630ce51109537165d53df)

<a id="header-details"></a>

---

[上一章](P051_zephyr__sys__printk-hooks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P053_zephyr__dt-bindings__pwm__pwm_ifx_tcpwm.h_文件参考.md)
