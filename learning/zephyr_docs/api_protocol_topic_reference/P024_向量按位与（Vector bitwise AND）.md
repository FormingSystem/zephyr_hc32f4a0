---
id: learning.zephyr-docs.api-protocol-topic-reference.page-24
title: 向量按位与（Vector bitwise AND）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__and.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_向量按位与（Vector bitwise AND）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__and.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

计算逻辑按位与。

<a id="details"></a>

计算按位逻辑与（bitwise AND）。分别为 `uint32_t`、`uint16_t` 和 `uint7_t` 数据类型提供独立函数。译注：原文写作 `uint7_t`，此处保留；实际接口类型请以本页原始声明为准。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.1\_函数（Functions）

<a id="r_ga22c8c022d4f8cd9e34f1e1e47433d121"></a>

```c
void zdsp_and_u8 (const uint8_t *src_a, const uint8_t *src_b, uint8_t *dst, uint32_t block_size)
```

相关声明：[zdsp_and_u8](#ga22c8c022d4f8cd9e34f1e1e47433d121)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑与（bitwise AND）。

<a id="r_ga988879dc54666692130793f6ce26fd23"></a>

```c
void zdsp_and_u16 (const uint16_t *src_a, const uint16_t *src_b, uint16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_and_u16](#ga988879dc54666692130793f6ce26fd23)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑与（bitwise AND）。

<a id="r_ga99019932e69574ca8aef86b4ace9c3b6"></a>

```c
void zdsp_and_u32 (const uint32_t *src_a, const uint32_t *src_b, uint32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_and_u32](#ga99019932e69574ca8aef86b4ace9c3b6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算两个定点向量（fixed-point vectors）的按位逻辑与（bitwise AND）。

## 24.2\_详细说明（Detailed Documentation）

<a id="ga988879dc54666692130793f6ce26fd23"></a>

### `zdsp_and_u16()`

```c
void zdsp_and_u16 ( const uint16_t * src_a, const uint16_t * src_b, uint16_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

计算两个定点向量（fixed-point vectors）的按位逻辑与（bitwise AND）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向输入向量 A。 |
| `[in] src_b` | 指向输入向量 B。 |
| `[out] dst` | 指向输出向量。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="ga99019932e69574ca8aef86b4ace9c3b6"></a>

### `zdsp_and_u32()`

```c
void zdsp_and_u32 ( const uint32_t * src_a, const uint32_t * src_b, uint32_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

计算两个定点向量（fixed-point vectors）的按位逻辑与（bitwise AND）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向输入向量 A。 |
| `[in] src_b` | 指向输入向量 B。 |
| `[out] dst` | 指向输出向量。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="ga22c8c022d4f8cd9e34f1e1e47433d121"></a>

### `zdsp_and_u8()`

```c
void zdsp_and_u8 ( const uint8_t * src_a, const uint8_t * src_b, uint8_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

计算两个定点向量（fixed-point vectors）的按位逻辑与（bitwise AND）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_a` | 指向输入向量 A。 |
| `[in] src_b` | 指向输入向量 B。 |
| `[out] dst` | 指向输出向量。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |


## 24.3\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/dsp/basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P023_轻量级M2M（LwM2M）的路径辅助宏。.md) · [返回大纲](大纲.md) · [下一章](P025_向量按位非（Vector bitwise NOT）.md)
