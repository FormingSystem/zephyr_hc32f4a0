---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-1
title: k_cycle_stats_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__cycle__stats.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_k\_cycle\_stats\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__cycle__stats.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于跟踪线程与CPU使用情况内部统计信息的结构。

```c
#include <zephyr/kernel/stats.h>
```

<a id="details"></a>

用于跟踪线程与CPU使用情况内部统计信息的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a1d49158db605872cd8d31225c0ae8ab5"></a>

```c
uint64_t total
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[total](#a1d49158db605872cd8d31225c0ae8ab5)。

总使用量，以周期（Cycles）计。

<a id="r_a8a955f987ddc88ff587edab8cb71dd6f"></a>

```c
bool track_usage
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[track_usage](#a8a955f987ddc88ff587edab8cb71dd6f)。

正在收集使用统计信息（Usage Statistics）时为true。

<a id="pub-attribs-0"></a>

### 选择CONFIG_SCHED_THREAD_USAGE_ANALYSIS时可用的字段（Fields）

<a id="r_a9c12b140936bcc4a8630c68680a245b4"></a>

```c
uint64_t current
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[current](#a9c12b140936bcc4a8630c68680a245b4)。

当前使用窗口（Usage Window）内的周期数。

<a id="r_a161c8d21c7d4a3d21c7cce87237c8334"></a>

```c
uint64_t longest
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[longest](#a161c8d21c7d4a3d21c7cce87237c8334)。

最长使用窗口（Usage Window）内的周期数。

<a id="r_acdb6a6b005384535607aaf1bc5dd3feb"></a>

```c
uint32_t num_windows
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_windows](#acdb6a6b005384535607aaf1bc5dd3feb)。

使用窗口（Usage Windows）的数量。

## 1.2\_详细说明（Detailed Documentation）

<a id="a9c12b140936bcc4a8630c68680a245b4"></a>

### `current`

```c
uint64_t k_cycle_stats::current
```

当前使用窗口（Usage Window）内的周期数。

<a id="a161c8d21c7d4a3d21c7cce87237c8334"></a>

### `longest`

```c
uint64_t k_cycle_stats::longest
```

最长使用窗口（Usage Window）内的周期数。

<a id="acdb6a6b005384535607aaf1bc5dd3feb"></a>

### `num_windows`

```c
uint32_t k_cycle_stats::num_windows
```

使用窗口（Usage Windows）的数量。

<a id="a1d49158db605872cd8d31225c0ae8ab5"></a>

### `total`

```c
uint64_t k_cycle_stats::total
```

总使用量，以周期（Cycles）计。

<a id="a8a955f987ddc88ff587edab8cb71dd6f"></a>

### `track_usage`

```c
bool k_cycle_stats::track_usage
```

正在收集使用统计信息（Usage Statistics）时为true。

本数据类型文档由以下文件生成：

- `zephyr/kernel/stats.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/kernel/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2stats_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_k_ipi_work_结构体.md)
