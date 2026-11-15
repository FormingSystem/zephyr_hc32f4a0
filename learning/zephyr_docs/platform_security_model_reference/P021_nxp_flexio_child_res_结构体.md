---
id: learning.zephyr-docs.platform-security-model-reference.page-21
title: nxp_flexio_child_res_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnxp__flexio__child__res.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_nxp\_flexio\_child\_res\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnxp__flexio__child__res.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含FlexIO子设备所需资源信息的结构。

```c
#include <zephyr/drivers/misc/nxp_flexio/nxp_flexio.h>
```

<a id="details"></a>

包含FlexIO子设备所需资源信息的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_afd4633d2dbb04c9155f9088206aa5772"></a>

```c
uint8_t * shifter_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[shifter_index](#afd4633d2dbb04c9155f9088206aa5772)。

保存已分配移位器（shifter）索引的输出数组。

<a id="r_afac825cb54e1dcd093c8ca19a78fa4dd"></a>

```c
uint8_t shifter_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[shifter_count](#afac825cb54e1dcd093c8ca19a78fa4dd)。

子设备所需的移位器索引数量。

<a id="r_ae1187d65f541a282da4651a53b0626d8"></a>

```c
uint8_t * timer_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[timer_index](#ae1187d65f541a282da4651a53b0626d8)。

保存已分配定时器（timer）索引的输出数组。

<a id="r_ad62e4adfc76a26841f613552e871a187"></a>

```c
uint8_t timer_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[timer_count](#ad62e4adfc76a26841f613552e871a187)。

子设备所需的定时器索引数量。

## 21.2\_详细说明（Detailed Documentation）

<a id="afac825cb54e1dcd093c8ca19a78fa4dd"></a>

### `shifter_count`

```c
uint8_t nxp_flexio_child_res::shifter_count
```

子设备所需的移位器索引数量。

<a id="afd4633d2dbb04c9155f9088206aa5772"></a>

### `shifter_index`

```c
uint8_t* nxp_flexio_child_res::shifter_index
```

保存已分配移位器（shifter）索引的输出数组。

必须指向至少包含 `shifter_count` 个条目的数组。值为从 0 开始的硬件索引，并且必须对所绑定的 FlexIO 有效。

<a id="ad62e4adfc76a26841f613552e871a187"></a>

### `timer_count`

```c
uint8_t nxp_flexio_child_res::timer_count
```

子设备所需的定时器索引数量。

<a id="ae1187d65f541a282da4651a53b0626d8"></a>

### `timer_index`

```c
uint8_t* nxp_flexio_child_res::timer_index
```

保存已分配定时器（timer）索引的输出数组。

必须指向至少包含 `timer_count` 个条目的数组。值为从 0 开始的硬件索引，并且必须对所绑定的 FlexIO 有效。

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/nxp_flexio/nxp_flexio.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/nxp_flexio/nxp_flexio.h](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexio_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_nxp_flexio_child_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_nxp_gint_group_config_结构体.md)
