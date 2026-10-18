---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-160
title: bt_sdp_attr_value_int_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__int.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第160章\_bt\_sdp\_attr\_value\_int\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__int.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）有符号整数类型的属性值。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

有符号整数类型的 SDP 属性值。此结构体保存从 SDP 属性中解析出的有符号整数值。`size` 字段指示整数值的实际大小。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 160.1\_数据成员（Data Fields）

<a id="r_a4dd9e9eae0d95dcc3af855d711ead35e"></a>

```c
uint8_t size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[size](#a4dd9e9eae0d95dcc3af855d711ead35e)。

有符号整数值的大小，单位为字节。

```c
union {
```

<a id="r_af26593d9197abd7e55ee2f5668215717"></a>

```c
int8_t s8
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[s8](#a282cf4821d1ba734df65e447687bb8ec)。

8 位有符号整数值。

<a id="r_a8678249db3c8a8efff03d5433069a8ba"></a>

```c
int16_t s16
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[s16](#ae2eeaa2eaf83b7923ea5f6d743d480b7)。

16 位有符号整数值。

<a id="r_a83e51364d74236bc05c121112f8ade57"></a>

```c
int32_t s32
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[s32](#ad114c103a0d2248cffdf5a0a458e8c57)。

32 位有符号整数值。

<a id="r_a05575e70b50740de54d4407d06eb6dad"></a>

```c
int64_t s64
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[s64](#a12c991cdf87a2d48d1c5b3d5cb639ead)。

64 位有符号整数值。

<a id="r_af767b3e6a59aeaaea27ea4ffbba9c39a"></a>

```c
uint8_t s128 [(1UL<<(0x14 &0x07))]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[s128](#a9fe2006da0ce55441dcffd4080ac287a)。

以字节数组表示的 128 位有符号整数值。

<a id="r_aa49f0246b5a636b00b025240edb2d9f9"></a>

```c
};
```

根据 `size` 保存有符号整数值的联合体。

## 160.2\_详细说明（Detailed Documentation）

<a id="aa49f0246b5a636b00b025240edb2d9f9"></a>

### `[union]`

```c
union { ... } bt_sdp_attr_value_int
```

根据 `size` 保存有符号整数值的联合体。

<a id="a9fe2006da0ce55441dcffd4080ac287a"></a>

### `s128`

```c
uint8_t bt_sdp_attr_value_int::s128[(1UL<<(0x14 &0x07))]
```

以字节数组表示的 128 位有符号整数值。

<a id="ae2eeaa2eaf83b7923ea5f6d743d480b7"></a>

### `s16`

```c
int16_t bt_sdp_attr_value_int::s16
```

16 位有符号整数值。

<a id="ad114c103a0d2248cffdf5a0a458e8c57"></a>

### `s32`

```c
int32_t bt_sdp_attr_value_int::s32
```

32 位有符号整数值。

<a id="a12c991cdf87a2d48d1c5b3d5cb639ead"></a>

### `s64`

```c
int64_t bt_sdp_attr_value_int::s64
```

64 位有符号整数值。

<a id="a282cf4821d1ba734df65e447687bb8ec"></a>

### `s8`

```c
int8_t bt_sdp_attr_value_int::s8
```

8 位有符号整数值。

<a id="a4dd9e9eae0d95dcc3af855d711ead35e"></a>

### `size`

```c
uint8_t bt_sdp_attr_value_int::size
```

有符号整数值的大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 160.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [bt_sdp_attr_value_int](P160_bt_sdp_attr_value_int_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P159_bt_sdp_attr_value_结构体.md) · [返回大纲](大纲.md) · [下一章](P161_bt_sdp_attr_value_pair_结构体.md)
