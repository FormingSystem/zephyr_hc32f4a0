---
id: learning.zephyr-docs.device-power-control-model-reference.page-91
title: st_transfer_properties_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structst__transfer__properties.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_st\_transfer\_properties\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structst__transfer__properties.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

详细传输属性（Detailed Transfer Properties）。

```c
#include <zephyr/drivers/misc/renesas_rx_dtc/renesas_rx_dtc.h>
```

<a id="details"></a>

详细传输属性（Detailed Transfer Properties）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 91.1\_数据成员（Data Fields）

<a id="r_a477f10434b31f151e1ab5154f2d72557"></a>

```c
uint32_t block_count_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[block_count_max](#a477f10434b31f151e1ab5154f2d72557)。

最大块数。

<a id="r_a80c7a09f3f586e7bc44cfc64b498757e"></a>

```c
uint32_t block_count_remaining
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[block_count_remaining](#a80c7a09f3f586e7bc44cfc64b498757e)。

剩余块数。

<a id="r_a93150e77bbc172e5743ab64fba5d303c"></a>

```c
uint32_t transfer_length_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[transfer_length_max](#a93150e77bbc172e5743ab64fba5d303c)。

最大传输次数。

<a id="r_a118301424e4b981bf73787f6cac0a1d0"></a>

```c
uint32_t transfer_length_remaining
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[transfer_length_remaining](#a118301424e4b981bf73787f6cac0a1d0)。

剩余传输次数。

## 91.2\_详细说明（Detailed Documentation）

<a id="a477f10434b31f151e1ab5154f2d72557"></a>

### `block_count_max`

```c
uint32_t st_transfer_properties::block_count_max
```

最大块数。

<a id="a80c7a09f3f586e7bc44cfc64b498757e"></a>

### `block_count_remaining`

```c
uint32_t st_transfer_properties::block_count_remaining
```

剩余块数。

<a id="a93150e77bbc172e5743ab64fba5d303c"></a>

### `transfer_length_max`

```c
uint32_t st_transfer_properties::transfer_length_max
```

最大传输次数。

<a id="a118301424e4b981bf73787f6cac0a1d0"></a>

### `transfer_length_remaining`

```c
uint32_t st_transfer_properties::transfer_length_remaining
```

剩余传输次数。

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/renesas_rx_dtc/renesas_rx_dtc.h`

## 91.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/renesas_rx_dtc/renesas_rx_dtc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P090_st_transfer_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P092_svc_driver_api_结构体.md)
