---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-135
title: bt_uuid_any_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__uuid__any.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第135章\_bt\_uuid\_any\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__uuid__any.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可保存任意大小UUID的辅助类型（Helper Type）。

```c
#include <zephyr/bluetooth/uuid.h>
```

<a id="details"></a>

可保存任意大小UUID的辅助类型（Helper Type）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 135.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_ad4118a943045af2247cfb6e677a98fdf"></a>

```c
struct bt_uuid uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#a08fab9ce3f49d00dcb7af0cc7a7ad3af)。

通用 UUID 视图（Generic UUID view）。

<a id="r_ad9503c0e56cd063aa29a1f99160f16da"></a>

```c
struct bt_uuid_16 u16
```

相关声明：[bt_uuid_16](P133_bt_uuid_16_结构体.md)、[u16](#aea87835ffd5ee2e01bbc6674a0bc83e1)。

16 位 UUID 视图（16-bit UUID view）。

<a id="r_aa45c55080495e33d0d96826dd0b8af93"></a>

```c
struct bt_uuid_32 u32
```

相关声明：[bt_uuid_32](P134_bt_uuid_32_结构体.md)、[u32](#adc9711e614e3839f6af9dd4db315dc66)。

32 位 UUID 视图（32-bit UUID view）。

<a id="r_ac834cf9666324eca401e100d19616c42"></a>

```c
struct bt_uuid_128 u128
```

相关声明：[bt_uuid_128](P132_bt_uuid_128_结构体.md)、[u128](#a504aec6e7e793c3de13242aef56fb833)。

128 位 UUID 视图（128-bit UUID view）。

<a id="r_a79491b44c5f32d0e01e1352fe390d3e3"></a>

```c
};
```

所有受支持 UUID 大小的联合体（Union）。

## 135.2\_详细说明（Detailed Documentation）

<a id="a79491b44c5f32d0e01e1352fe390d3e3"></a>

### `[union]`

```c
union { ... } bt_uuid_any
```

所有受支持 UUID 大小的联合体（Union）。

<a id="a504aec6e7e793c3de13242aef56fb833"></a>

### `u128`

```c
struct bt_uuid_128 bt_uuid_any::u128
```

128 位 UUID 视图（128-bit UUID view）。

<a id="aea87835ffd5ee2e01bbc6674a0bc83e1"></a>

### `u16`

```c
struct bt_uuid_16 bt_uuid_any::u16
```

16 位 UUID 视图（16-bit UUID view）。

<a id="adc9711e614e3839f6af9dd4db315dc66"></a>

### `u32`

```c
struct bt_uuid_32 bt_uuid_any::u32
```

32 位 UUID 视图（32-bit UUID view）。

<a id="a08fab9ce3f49d00dcb7af0cc7a7ad3af"></a>

### `uuid`

```c
struct bt_uuid bt_uuid_any::uuid
```

通用 UUID 视图（Generic UUID view）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/uuid.h`

## 135.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [bt_uuid_16](P133_bt_uuid_16_结构体.md)
- [bt_uuid_32](P134_bt_uuid_32_结构体.md)
- [bt_uuid_128](P132_bt_uuid_128_结构体.md)
- [bt_uuid_any](P135_bt_uuid_any_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P134_bt_uuid_32_结构体.md) · [返回大纲](大纲.md)
