---
id: learning.zephyr-docs.device-power-control-model-reference.page-21
title: it8801_mfd_callback_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structit8801__mfd__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_it8801\_mfd\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structit8801__mfd__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/mfd/mfd_ite_it8801.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_ab9b86565265e5f8c7409e44b559732ea"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#ab9b86565265e5f8c7409e44b559732ea)。

<a id="r_a859a3813a936433024681903bc951b7d"></a>

```c
it8801_callback_handler_t cb
```

相关声明：[it8801_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/mfd__ite__it8801_8h.html#a50e301d4cfb9211625e851b0cc40f130)、[cb](#a859a3813a936433024681903bc951b7d)。

<a id="r_a9d4df8a0ba22f560bb799a1945a73592"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#a9d4df8a0ba22f560bb799a1945a73592)。

## 21.2\_详细说明（Detailed Documentation）

<a id="a859a3813a936433024681903bc951b7d"></a>

### `cb`

```c
it8801_callback_handler_t it8801_mfd_callback::cb
```

<a id="a9d4df8a0ba22f560bb799a1945a73592"></a>

### `dev`

```c
const struct device* it8801_mfd_callback::dev
```

<a id="ab9b86565265e5f8c7409e44b559732ea"></a>

### `node`

```c
sys_snode_t it8801_mfd_callback::node
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/mfd/mfd_ite_it8801.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mfd/mfd_ite_it8801.h](https://docs.zephyrproject.org/latest/doxygen/html/mfd__ite__it8801_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [it8801_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/mfd__ite__it8801_8h.html#a50e301d4cfb9211625e851b0cc40f130)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_ifx_clk_peri_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_it8801_vendor_id_t_结构体.md)
