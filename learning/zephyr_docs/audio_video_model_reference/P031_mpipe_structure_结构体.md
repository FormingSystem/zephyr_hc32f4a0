---
id: learning.zephyr-docs.audio-video-model-reference.page-31
title: mpipe_structure_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__structure.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_mpipe\_structure\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__structure.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存一项能力（Capability）各字段的固定大小容器。

```c
#include <zephyr/mpipe/mpipe_structure.h>
```

<a id="details"></a>

用于保存一项能力各字段的固定大小容器。字段占据 `ids` 和 `values` 的前 `num_fields` 个槽位，这两个数组一一对应：`ids[i]` 指定 `values[i]` 保存的字段名称。槽位索引本身不带额外含义，因此系统中存在多少种标识符不会增加此处的存储开销；真正占用空间的是一个结构同时保存的字段数，其上限为 `CONFIG_MPIPE_STRUCTURE_MAX_FIELDS`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a369725cad51f522a1ad631c97ad66e0b"></a>

```c
uint8_t media_type_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[media_type_id](#a369725cad51f522a1ad631c97ad66e0b)。

结构的媒体类型（media type），参见 `mpipe_media_type`。

<a id="r_aec4c4cdf74b7aeaeb49fc76ffabb55c8"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#aec4c4cdf74b7aeaeb49fc76ffabb55c8)。

结构标志，参见 `MPIPE_STRUCTURE_FLAG_ANY`。

<a id="r_a70a820ab037028c1cdcd3471ec262f8f"></a>

```c
uint8_t num_fields
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_fields](#a70a820ab037028c1cdcd3471ec262f8f)。

`ids` 和 `values` 开头已使用的槽位数量。

<a id="r_a77c9646be70c5276be0475017bfc0b0e"></a>

```c
uint8_t ids [CONFIG_MPIPE_STRUCTURE_MAX_FIELDS]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ids](#a77c9646be70c5276be0475017bfc0b0e)。

各槽位保存的字段标识符，参见 `mpipe_caps_field`。

<a id="r_ad7a264c02f28023249e59b25bd5b21fd"></a>

```c
struct mpipe_value values [CONFIG_MPIPE_STRUCTURE_MAX_FIELDS]
```

相关声明：[mpipe_value](P036_mpipe_value_结构体.md)、[values](#ad7a264c02f28023249e59b25bd5b21fd)。

各槽位保存的值。

## 31.2\_详细说明（Detailed Documentation）

<a id="aec4c4cdf74b7aeaeb49fc76ffabb55c8"></a>

### `flags`

```c
uint8_t mpipe_structure::flags
```

结构标志，参见 `MPIPE_STRUCTURE_FLAG_ANY`。

<a id="a77c9646be70c5276be0475017bfc0b0e"></a>

### `ids`

```c
uint8_t mpipe_structure::ids[CONFIG_MPIPE_STRUCTURE_MAX_FIELDS]
```

各槽位保存的字段标识符，参见 `mpipe_caps_field`。

<a id="a369725cad51f522a1ad631c97ad66e0b"></a>

### `media_type_id`

```c
uint8_t mpipe_structure::media_type_id
```

结构的媒体类型（media type），参见 `mpipe_media_type`。

<a id="a70a820ab037028c1cdcd3471ec262f8f"></a>

### `num_fields`

```c
uint8_t mpipe_structure::num_fields
```

`ids` 和 `values` 开头已使用的槽位数量。

<a id="ad7a264c02f28023249e59b25bd5b21fd"></a>

### `values`

```c
struct mpipe_value mpipe_structure::values[CONFIG_MPIPE_STRUCTURE_MAX_FIELDS]
```

各槽位保存的值。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_structure.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_structure.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__structure_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_media_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga4e2bcc7f5152bfde2579bd92618b7b1c)
- [mpipe_caps_field](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html#ga0165db3d65894c7832dc455e8014deb5)
- [mpipe_value](P036_mpipe_value_结构体.md)
- [CONFIG_MPIPE_STRUCTURE_MAX_FIELDS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_STRUCTURE_MAX_FIELDS)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_mpipe_src_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_mpipe_tee_结构体.md)
