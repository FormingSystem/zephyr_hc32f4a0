---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-12
title: zephyr__sys__winstream.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_sys\_\_winstream.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_sys_5Fwinstream"></a>

```c
struct sys_winstream
```

相关声明：[sys_winstream](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md)。

无锁共享内存字节流IPC（Lockless Shared Memory Byte Stream IPC）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.2\_函数（Functions）

<a id="r_acc72f0f65bd88e8f2b630a3832006f9c"></a>

```c
static struct sys_winstream * sys_winstream_init (void *buf, int buflen)
```

相关声明：[sys_winstream](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md)、[sys_winstream_init](#acc72f0f65bd88e8f2b630a3832006f9c)。

根据一块内存区域（Memory Region）构造 `sys_winstream`。

<a id="r_ae8686be598c081858322378c8e4368cb"></a>

```c
void sys_winstream_write (struct sys_winstream *ws, const char *data, uint32_t len)
```

相关声明：[sys_winstream_write](#ae8686be598c081858322378c8e4368cb)、[sys_winstream](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 `sys_winstream` 写入字节（Bytes）。

<a id="r_a55dc3b77ec21e6d799aa951e327dc392"></a>

```c
uint32_t sys_winstream_read (struct sys_winstream *ws, uint32_t *seq, char *buf, uint32_t buflen)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sys_winstream_read](#a55dc3b77ec21e6d799aa951e327dc392)、[sys_winstream](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 `sys_winstream` 读取字节（Bytes）。

## 12.3\_详细说明（Detailed Documentation）

<a id="acc72f0f65bd88e8f2b630a3832006f9c"></a>

### `sys_winstream_init()`

```c
struct sys_winstream * sys_winstream_init ( void * buf, int buflen )
```

声明属性：`inline`、`static`。

根据一块内存区域（Memory Region）构造 `sys_winstream`。

在任意大小的内存区域（Memory Region）中初始化 `sys_winstream`，并返回生成的对象，其地址保证与缓冲区相同。显然，该内存必须由读者和写者共享，且对它的所有操作必须保持一致性（Coherence）和一致的顺序（Consistent Ordering）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向用于容纳流（Stream）的内存区域的指针。 |
| `buflen` | 缓冲区长度（Buffer Length），必须足以容纳 `struct sys_winstream` 和至少 1 字节数据。 |

**返回（Returns）**：**返回值（Returns）：**指向已初始化 `sys_winstream` 的指针，与 `buf` 参数地址相同。

<a id="a55dc3b77ec21e6d799aa951e327dc392"></a>

### `sys_winstream_read()`

```c
uint32_t sys_winstream_read ( struct sys_winstream * ws, uint32_t * seq, char * buf, uint32_t buflen )
```

从 `sys_winstream` 读取字节（Bytes）。

从 `sys_winstream` 读取字节到指定缓冲区。本函数始终在常数时间（Constant Time）内返回，不阻塞，除内存顺序（Memory Ordering）外不执行其他同步。返回写入缓冲区的字节数；但写者推进速度超过当前读取上下文时，可能发生下溢（Underflow）。可通过指针返回的序列号（Sequence Number）检测：若 `*seq != old_seq + return_value`，表示发生下溢，部分字节已丢失。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ws` | 要读取的 `sys_winstream`。 |
| `seq` | 指向整数的指针，其中保存上次从流中读取的序列号（Sequence Number）；`0` 表示流起点（Start of Stream）。该值原地更新，供后续调用和下溢检测使用。 |
| `buf` | 用于存储读取数据的缓冲区（Buffer）。 |
| `buflen` | `buf` 的字节长度（Length in Bytes）。 |

**返回（Returns）**：**返回值（Returns）：**写入缓冲区的字节数（Number of Bytes）。

<a id="ae8686be598c081858322378c8e4368cb"></a>

### `sys_winstream_write()`

```c
void sys_winstream_write ( struct sys_winstream * ws, const char * data, uint32_t len )
```

向 `sys_winstream` 写入字节（Bytes）。

将指定数量的字节写入流（Stream）。本函数始终同步返回，不阻塞，除内存写入顺序（Memory Write Ordering）外不执行其他同步。超过缓冲区可容纳范围的字节会被静默丢弃，但读者可通过序列号（Sequence Number）检测出其存在。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ws` | 要写入的 `sys_winstream`。 |
| `data` | 指向待写入字节（Bytes）的指针。 |
| `len` | 要写入的字节数。 |


## 12.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P056_winstream.h_源码浏览.md)
- [sys_winstream](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_zephyr__dt-bindings__timer__ti-dmtimer.h_文件参考.md) · [返回大纲](大纲.md)
