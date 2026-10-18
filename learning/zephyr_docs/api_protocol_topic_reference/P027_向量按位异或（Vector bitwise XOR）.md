---
id: learning.zephyr-docs.api-protocol-topic-reference.page-27
title: 向量按位异或（Vector bitwise XOR）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__xor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_向量按位异或（Vector bitwise XOR）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__xor.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

计算逻辑按位异或。

<a id="details"></a>

计算按位逻辑异或（bitwise XOR）。分别为 `uint32_t`、`uint16_t` 和 `uint7_t` 数据类型提供独立函数。译注：原文写作 `uint7_t`，此处保留；实际接口类型请以本页原始声明为准。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.1\_函数（Functions）

<a id="r_ga4f5a442ce2ce79a6d09fde4648ceb100"></a>

```c
void zdsp_xor_u8 (const uint8_t *src_a, const uint8_t *src_b, uint8_t *dst, uint32_t block_size)
```

相关声明：[zdsp_xor_u8](#ga4f5a442ce2ce79a6d09fde4648ceb100)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑异或（bitwise XOR）。

<a id="r_gaa4d486a9a9022120e86e6e5d62940444"></a>

```c
void zdsp_xor_u16 (const uint16_t *src_a, const uint16_t *src_b, uint16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_xor_u16](#gaa4d486a9a9022120e86e6e5d62940444)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑异或（bitwise XOR）。

<a id="r_gac4dd8fed6e7485a0e989fb37b3fe0c77"></a>

```c
void zdsp_xor_u32 (const uint32_t *src_a, const uint32_t *src_b, uint32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_xor_u32](#gac4dd8fed6e7485a0e989fb37b3fe0c77)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑异或（bitwise XOR）。

## 27.2\_详细说明（Detailed Documentation）

<a id="gaa4d486a9a9022120e86e6e5d62940444"></a>

### `zdsp_xor_u16()`

```c
void zdsp_xor_u16 ( const uint16_t * src_a, const uint16_t * src_b, uint16_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

计算两个定点向量（fixed-point vectors）的按位逻辑异或（bitwise XOR）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向输入向量 A。 |
| `[in] src_b` | 指向输入向量 B。 |
| `[out] dst` | 指向输出向量。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="gac4dd8fed6e7485a0e989fb37b3fe0c77"></a>

### `zdsp_xor_u32()`

```c
void zdsp_xor_u32 ( const uint32_t * src_a, const uint32_t * src_b, uint32_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

计算两个定点向量（fixed-point vectors）的按位逻辑异或（bitwise XOR）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向输入向量 A。 |
| `[in] src_b` | 指向输入向量 B。 |
| `[out] dst` | 指向输出向量。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="ga4f5a442ce2ce79a6d09fde4648ceb100"></a>

### `zdsp_xor_u8()`

```c
void zdsp_xor_u8 ( const uint8_t * src_a, const uint8_t * src_b, uint8_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

计算两个定点向量（fixed-point vectors）的按位逻辑异或（bitwise XOR）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向输入向量 A。 |
| `[in] src_b` | 指向输入向量 B。 |
| `[out] dst` | 指向输出向量。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |


## 27.3\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/dsp/basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P026_向量按位或（Vector bitwise OR）.md) · [返回大纲](大纲.md) · [下一章](P028_枚举管理（Enumeration Management）.md)
