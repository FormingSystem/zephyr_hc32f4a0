---
id: learning.zephyr-docs.api-network-time-topic-reference.page-17
title: 指令内存接口（Instruction Memory APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_指令内存接口（Instruction Memory APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__instr__mem.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.1\_函数（Functions）

<a id="r_ga61c79df57849b7e914cd33e0de4316a3"></a>

```c
bool arch_is_instr_mem (const void *addr, size_t len)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arch_is_instr_mem](#ga61c79df57849b7e914cd33e0de4316a3)。

检查区域（Region）是否位于指令内存（Instruction Memory）。

<a id="r_gae80e1083bf80acaf0466d0bc2fe96bb4"></a>

```c
void * arch_memset_instr (void *buf, int c, size_t n)
```

相关声明：[arch_memset_instr](#gae80e1083bf80acaf0466d0bc2fe96bb4)。

对指令内存（Instruction Memory）中的缓冲区执行内存填充（Memset）。

<a id="r_ga506986b790b95fca0423e4c47690b1fe"></a>

```c
void * arch_memcpy_to_instr (void *d, const void *s, size_t n)
```

相关声明：[arch_memcpy_to_instr](#ga506986b790b95fca0423e4c47690b1fe)。

将缓冲区从数据内存（Data Memory）复制（Memcpy）到指令内存（Instruction Memory）。

<a id="r_ga03af01659004f2d96438b948f8c065a9"></a>

```c
void * arch_memcpy_from_instr (void *d, const void *s, size_t n)
```

相关声明：[arch_memcpy_from_instr](#ga03af01659004f2d96438b948f8c065a9)。

将缓冲区从指令内存（Instruction Memory）复制（Memcpy）到数据内存（Data Memory）。

## 17.2\_详细说明（Detailed Documentation）

<a id="ga61c79df57849b7e914cd33e0de4316a3"></a>

### `arch_is_instr_mem()`

```c
bool arch_is_instr_mem ( const void * addr, size_t len )
```

```c
#include <zephyr/arch/common/instr_mem.h>
```

检查区域（Region）是否位于指令内存（Instruction Memory）。

检查给定地址范围是否位于指令存储器（instruction memory）。对于非哈佛架构（non-Harvard architectures），此函数始终返回 true；对于哈佛架构，如果无法判断区域是否位于指令存储器，例如缺少设备树信息，则应返回 false。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 区域的起始地址。 |
| `len` | 区域长度，单位为字节。 |

**返回（Returns）**：返回值：架构不是哈佛架构，或该区域位于指令存储器时为 true，否则为 false。

<a id="ga03af01659004f2d96438b948f8c065a9"></a>

### `arch_memcpy_from_instr()`

```c
void * arch_memcpy_from_instr ( void * d, const void * s, size_t n )
```

```c
#include <zephyr/arch/common/instr_mem.h>
```

将缓冲区从指令内存（Instruction Memory）复制（Memcpy）到数据内存（Data Memory）。

用于将缓冲区从指令存储器复制到数据存储器（data memory）的 `memcpy`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d` | 目标缓冲区。 |
| `s` | 源缓冲区。 |
| `n` | 要复制的字节数。 |

**返回（Returns）**：返回值：所提供的目标缓冲区指针；出错时返回 `NULL`。

<a id="ga506986b790b95fca0423e4c47690b1fe"></a>

### `arch_memcpy_to_instr()`

```c
void * arch_memcpy_to_instr ( void * d, const void * s, size_t n )
```

```c
#include <zephyr/arch/common/instr_mem.h>
```

将缓冲区从数据内存（Data Memory）复制（Memcpy）到指令内存（Instruction Memory）。

用于将缓冲区从数据存储器复制到指令存储器的 `memcpy`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d` | 目标缓冲区。 |
| `s` | 源缓冲区。 |
| `n` | 要复制的字节数。 |

**返回（Returns）**：返回值：所提供的目标缓冲区指针；出错时返回 `NULL`。

<a id="gae80e1083bf80acaf0466d0bc2fe96bb4"></a>

### `arch_memset_instr()`

```c
void * arch_memset_instr ( void * buf, int c, size_t n )
```

```c
#include <zephyr/arch/common/instr_mem.h>
```

对指令内存（Instruction Memory）中的缓冲区执行内存填充（Memset）。

对指令内存（Instruction Memory）中的缓冲区执行内存填充（Memset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要执行 `memset` 的缓冲区。 |
| `c` | 要设置的值。 |
| `n` | 要设置的字节数。 |

**返回（Returns）**：返回值：所提供的缓冲区指针；出错时返回 `NULL`。


## 17.3\_原页交叉引用（Cross References）

- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/arch/common/instr_mem.h](../api_file_service_reference/P018_zephyr__arch__common__instr_mem.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_模拟轴（Analog axis）.md) · [返回大纲](大纲.md) · [下一章](P018_LSM6DSV16X API主题.md)
