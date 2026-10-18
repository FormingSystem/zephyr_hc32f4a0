---
id: learning.zephyr-docs.system-service-model-reference.page-84
title: stat_mgmt_entry_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structstat__mgmt__entry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_stat\_mgmt\_entry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structstat__mgmt__entry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示统计组（Statistics Group）中的单个值。

```c
#include <zephyr/mgmt/mcumgr/grp/stat_mgmt/stat_mgmt.h>
```

<a id="details"></a>

表示统计组（Statistics Group）中的单个值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 84.1\_数据成员（Data Fields）

<a id="r_a44621593259f6f298bb62eb2675c1efb"></a>

```c
const char * name
```

相关声明：[name](#a44621593259f6f298bb62eb2675c1efb)。

统计项名称。

<a id="r_aa8441c1d2a1ce5acaa660e2e9b9d260d"></a>

```c
uint64_t value
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[value](#aa8441c1d2a1ce5acaa660e2e9b9d260d)。

统计项值。

## 84.2\_详细说明（Detailed Documentation）

<a id="a44621593259f6f298bb62eb2675c1efb"></a>

### `name`

```c
const char* stat_mgmt_entry::name
```

统计项名称。

<a id="aa8441c1d2a1ce5acaa660e2e9b9d260d"></a>

### `value`

```c
uint64_t stat_mgmt_entry::value
```

统计项值。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/stat_mgmt/stat_mgmt.h`

## 84.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/stat_mgmt/stat_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/stat__mgmt_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P083_smp_transport_bridge_结构体.md) · [返回大纲](大纲.md) · [下一章](P085_stats_hdr_结构体.md)
