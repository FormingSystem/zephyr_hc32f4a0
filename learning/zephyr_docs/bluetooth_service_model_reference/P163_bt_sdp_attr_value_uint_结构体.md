---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-163
title: bt_sdp_attr_value_uint_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__uint.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第163章\_bt\_sdp\_attr\_value\_uint\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value__uint.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）无符号整数类型的属性值。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

无符号整数类型的 SDP 属性值。此结构体保存从 SDP 属性中解析出的无符号整数值。`size` 字段指示整数值的实际大小。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 163.1\_数据成员（Data Fields）

<a id="r_a5741e3d3c00c8dc8085d496692d1114c"></a>

```c
uint8_t size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[size](#a5741e3d3c00c8dc8085d496692d1114c)。

无符号整数值的大小，单位为字节。

```c
union {
```

<a id="r_a427285272ac25fdd49b34dea502f584a"></a>

```c
uint8_t u8
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[u8](#a7dae539fd3f8232842fe4a1bebca1824)。

8 位无符号整数值。

<a id="r_a31e4a272f7d2e1a08b43591325160874"></a>

```c
uint16_t u16
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[u16](#af88e041745b2e69ac207afc5e4d369c1)。

16 位无符号整数值。

<a id="r_a098487e109824b40424d2ceaeac50719"></a>

```c
uint32_t u32
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[u32](#ae0a02d6f23b160c98022f58b9c38ab37)。

32 位无符号整数值。

<a id="r_a07f1eab02930508781e7966f30f8eefe"></a>

```c
uint64_t u64
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[u64](#a4752a1517d75c13454db83f095b5da4f)。

64 位无符号整数值。

<a id="r_a55389b19ff0d24adb1ca0a45ac098af4"></a>

```c
uint8_t u128 [(1UL<<(0x0c &0x07))]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[u128](#a7b609be27cad4508d2713b169d8bd4b5)。

以字节数组表示的 128 位无符号整数值。

<a id="r_a3571eaaac6fb8df0d830cbbd75638558"></a>

```c
};
```

根据 `size` 保存无符号整数值的联合体。

## 163.2\_详细说明（Detailed Documentation）

<a id="a3571eaaac6fb8df0d830cbbd75638558"></a>

### `[union]`

```c
union { ... } bt_sdp_attr_value_uint
```

根据 `size` 保存无符号整数值的联合体。

<a id="a5741e3d3c00c8dc8085d496692d1114c"></a>

### `size`

```c
uint8_t bt_sdp_attr_value_uint::size
```

无符号整数值的大小，单位为字节。

<a id="a7b609be27cad4508d2713b169d8bd4b5"></a>

### `u128`

```c
uint8_t bt_sdp_attr_value_uint::u128[(1UL<<(0x0c &0x07))]
```

以字节数组表示的 128 位无符号整数值。

<a id="af88e041745b2e69ac207afc5e4d369c1"></a>

### `u16`

```c
uint16_t bt_sdp_attr_value_uint::u16
```

16 位无符号整数值。

<a id="ae0a02d6f23b160c98022f58b9c38ab37"></a>

### `u32`

```c
uint32_t bt_sdp_attr_value_uint::u32
```

32 位无符号整数值。

<a id="a4752a1517d75c13454db83f095b5da4f"></a>

### `u64`

```c
uint64_t bt_sdp_attr_value_uint::u64
```

64 位无符号整数值。

<a id="a7dae539fd3f8232842fe4a1bebca1824"></a>

### `u8`

```c
uint8_t bt_sdp_attr_value_uint::u8
```

8 位无符号整数值。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 163.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bt_sdp_attr_value_uint](P163_bt_sdp_attr_value_uint_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P162_bt_sdp_attr_value_text_结构体.md) · [返回大纲](大纲.md) · [下一章](P164_bt_sdp_attr_value_url_结构体.md)
