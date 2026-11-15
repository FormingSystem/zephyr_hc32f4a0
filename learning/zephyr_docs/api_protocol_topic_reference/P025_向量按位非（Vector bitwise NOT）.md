---
id: learning.zephyr-docs.api-protocol-topic-reference.page-25
title: 向量按位非（Vector bitwise NOT）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__not.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_向量按位非（Vector bitwise NOT）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__not.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

计算逻辑按位非。

<a id="details"></a>

计算按位逻辑非（bitwise NOT）。分别为 `uint32_t`、`uint16_t` 和 `uint7_t` 数据类型提供独立函数。译注：原文写作 `uint7_t`，此处保留；实际接口类型请以本页原始声明为准。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.1\_函数（Functions）

<a id="r_gaafd38edd648a03d328d51b5ca9097b5d"></a>

```c
void zdsp_not_u8 (const uint8_t *src, uint8_t *dst, uint32_t block_size)
```

相关声明：[zdsp_not_u8](#gaafd38edd648a03d328d51b5ca9097b5d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算定点向量（fixed-point vector）的按位逻辑非（bitwise NOT）。

<a id="r_ga3bca20f3c626e1a64dd79d0e22a43bed"></a>

```c
void zdsp_not_u16 (const uint16_t *src, uint16_t *dst, uint32_t block_size)
```

相关声明：[zdsp_not_u16](#ga3bca20f3c626e1a64dd79d0e22a43bed)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算定点向量（fixed-point vector）的按位逻辑非（bitwise NOT）。

<a id="r_gafd6993acd6abeaa529dea84f3fd4d3a9"></a>

```c
void zdsp_not_u32 (const uint32_t *src, uint32_t *dst, uint32_t block_size)
```

相关声明：[zdsp_not_u32](#gafd6993acd6abeaa529dea84f3fd4d3a9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算定点向量（fixed-point vector）的按位逻辑非（bitwise NOT）。

## 25.2\_详细说明（Detailed Documentation）

<a id="ga3bca20f3c626e1a64dd79d0e22a43bed"></a>

### `zdsp_not_u16()`

```c
void zdsp_not_u16 ( const uint16_t * src, uint16_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

计算定点向量（fixed-point vector）的按位逻辑非（bitwise NOT）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量。 |
| `[out] dst` | 指向输出向量。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="gafd6993acd6abeaa529dea84f3fd4d3a9"></a>

### `zdsp_not_u32()`

```c
void zdsp_not_u32 ( const uint32_t * src, uint32_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

计算定点向量（fixed-point vector）的按位逻辑非（bitwise NOT）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量。 |
| `[out] dst` | 指向输出向量。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |

<a id="gaafd38edd648a03d328d51b5ca9097b5d"></a>

### `zdsp_not_u8()`

```c
void zdsp_not_u8 ( const uint8_t * src, uint8_t * dst, uint32_t block_size )
```

```c
#include <zephyr/dsp/basicmath.h>
```

计算定点向量（fixed-point vector）的按位逻辑非（bitwise NOT）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 指向输入向量。 |
| `[out] dst` | 指向输出向量。 |
| `[in] block_size` | 每个向量（vector）中的样本数。 |


## 25.3\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/dsp/basicmath.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P024_向量按位与（Vector bitwise AND）.md) · [返回大纲](大纲.md) · [下一章](P026_向量按位或（Vector bitwise OR）.md)
