---
id: learning.zephyr-docs.device-power-control-model-reference.page-52
title: numaker_scc_subsys_rate_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnumaker__scc__subsys__rate.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_numaker\_scc\_subsys\_rate\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnumaker__scc__subsys__rate.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NuMaker时钟子系统频率选择器（Rate Selector）。

```c
#include <zephyr/drivers/clock_control/clock_control_numaker.h>
```

<a id="details"></a>

NuMaker时钟子系统频率选择器（Rate Selector）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a95401561a0a73331a2e1d5e0a773371e"></a>

```c
struct numaker_scc_subsys_pcc_rate pcc
```

相关声明：[numaker_scc_subsys_pcc_rate](P051_numaker_scc_subsys_pcc_rate_结构体.md)、[pcc](#a159486917a5c695f66edebb4749cd1d7)。

外设时钟频率信息。

<a id="r_a8e299571c1e39a9078d02a9865a82b56"></a>

```c
};
```

## 52.2\_详细说明（Detailed Documentation）

<a id="a8e299571c1e39a9078d02a9865a82b56"></a>

### `[union]`

```c
union { ... } numaker_scc_subsys_rate
```

<a id="a159486917a5c695f66edebb4749cd1d7"></a>

### `pcc`

```c
struct numaker_scc_subsys_pcc_rate numaker_scc_subsys_rate::pcc
```

外设时钟频率信息。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_numaker.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_numaker.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h_source.html)
- [numaker_scc_subsys_pcc_rate](P051_numaker_scc_subsys_pcc_rate_结构体.md)
- [numaker_scc_subsys_rate](P052_numaker_scc_subsys_rate_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_numaker_scc_subsys_pcc_rate_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_numicro_scc_subsys_结构体.md)
