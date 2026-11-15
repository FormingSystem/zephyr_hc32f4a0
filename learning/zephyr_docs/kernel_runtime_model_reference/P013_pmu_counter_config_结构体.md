---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-13
title: pmu_counter_config_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpmu__counter__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_pmu\_counter\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpmu__counter__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

性能监测单元（PMU）计数器的配置条目。

```c
#include <zephyr/arch/pmu.h>
```

<a id="details"></a>

性能监测单元（PMU）计数器的配置条目。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a482305d6da6760f7a177a8737f720f88"></a>

```c
pmu_evt_t event
```

相关声明：[pmu_evt_t](https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h.html#a1e81090eaba4c1aa7009fe85f5bf2f6a)、[event](#a482305d6da6760f7a177a8737f720f88)。

事件（Event），例如：

<a id="r_ab8f9346eec1110d9b45dba5570aef2cd"></a>

```c
bool enabled
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enabled](#ab8f9346eec1110d9b45dba5570aef2cd)。

配置时启用此计数器（Counter）。

## 13.2\_详细说明（Detailed Documentation）

<a id="ab8f9346eec1110d9b45dba5570aef2cd"></a>

### `enabled`

```c
bool pmu_counter_config::enabled
```

配置时启用此计数器（Counter）。

<a id="a482305d6da6760f7a177a8737f720f88"></a>

### `event`

```c
pmu_evt_t pmu_counter_config::event
```

事件（Event），例如：

启用CONFIG_ARM64时的PMU_EVT_*枚举值（Enumerators）。

本数据类型文档由以下文件生成：

- `zephyr/arch/pmu.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/arch/pmu.h](https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h_source.html)
- [pmu_evt_t](https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h.html#a1e81090eaba4c1aa7009fe85f5bf2f6a)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_k_work_sync_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_pmu_info_t_结构体.md)
