---
id: learning.zephyr-docs.network-core-model-reference.page-143
title: net_stats_pm_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__pm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第143章\_net\_stats\_pm\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__pm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电源管理（Power Management）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

电源管理（Power Management）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 143.1\_数据成员（Data Fields）

<a id="r_ab43935fcfe9efc1cd5f3e7e329996805"></a>

```c
uint64_t overall_suspend_time
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[overall_suspend_time](#ab43935fcfe9efc1cd5f3e7e329996805)。

总挂起时间（Total suspend time）。

<a id="r_ac14122a4765c499c045f18c70af355a0"></a>

```c
net_stats_t suspend_count
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[suspend_count](#ac14122a4765c499c045f18c70af355a0)。

挂起次数（Suspend count）。

<a id="r_a0bdf9c3676298e2df4ff3bfa03f5e823"></a>

```c
uint32_t last_suspend_time
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[last_suspend_time](#a0bdf9c3676298e2df4ff3bfa03f5e823)。

上一次挂起的持续时间（Last suspend duration）。

<a id="r_a6784806eaa093431ed3c0f7acfe5a89c"></a>

```c
uint32_t start_time
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[start_time](#a6784806eaa093431ed3c0f7acfe5a89c)。

网络接口上一次挂起的开始时间（Last suspend start time）。

## 143.2\_详细说明（Detailed Documentation）

<a id="a0bdf9c3676298e2df4ff3bfa03f5e823"></a>

### `last_suspend_time`

```c
uint32_t net_stats_pm::last_suspend_time
```

上一次挂起的持续时间（Last suspend duration）。

<a id="ab43935fcfe9efc1cd5f3e7e329996805"></a>

### `overall_suspend_time`

```c
uint64_t net_stats_pm::overall_suspend_time
```

总挂起时间（Total suspend time）。

<a id="a6784806eaa093431ed3c0f7acfe5a89c"></a>

### `start_time`

```c
uint32_t net_stats_pm::start_time
```

网络接口上一次挂起的开始时间（Last suspend start time）。

<a id="ac14122a4765c499c045f18c70af355a0"></a>

### `suspend_count`

```c
net_stats_t net_stats_pm::suspend_count
```

挂起次数（Suspend count）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 143.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P142_net_stats_pkts_结构体.md) · [返回大纲](大纲.md) · [下一章](P144_net_stats_ppp_结构体.md)
