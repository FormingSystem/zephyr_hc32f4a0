---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-19
title: sys_winstream_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsys__winstream.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_sys\_winstream\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsys__winstream.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

无锁共享内存字节流IPC（Lockless Shared Memory Byte Stream IPC）。

```c
#include <zephyr/sys/winstream.h>
```

<a id="details"></a>

无锁共享内存字节流IPC（Lockless Shared Memory Byte Stream IPC）。sys_winstream工具在读写双方共享的内存区域上，实现具有简单读写语义的单向字节流。除可靠的内存操作顺序之外，它不需要锁或其他同步机制，因此适合异构共享内存环境，例如Zephyr需要与系统中运行各自软件的其他CPU通信时。此对象不跟踪上次读取的序列号（Sequence Number）；读取方必须自行保存该状态，并在每次读取操作中提供。达到稳定状态（Steady State）后，由于缓冲区始终为满，end与start相隔一个字节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a30b03df76a51ecbf0cbe33975d5aaa66"></a>

```c
uint32_t len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[len](#a30b03df76a51ecbf0cbe33975d5aaa66)。

<a id="r_a1cc84dfd9f812b3491135d13365c7a98"></a>

```c
uint32_t start
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[start](#a1cc84dfd9f812b3491135d13365c7a98)。

<a id="r_a6b80cf715e4a3ca7b7b74b9efd150a23"></a>

```c
uint32_t end
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[end](#a6b80cf715e4a3ca7b7b74b9efd150a23)。

<a id="r_a7d946d6a54652a8ac035dd8cd0ba861a"></a>

```c
uint32_t seq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[seq](#a7d946d6a54652a8ac035dd8cd0ba861a)。

<a id="r_a341203116bfee52d4b801466097fc3eb"></a>

```c
uint8_t data []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a341203116bfee52d4b801466097fc3eb)。

## 19.2\_详细说明（Detailed Documentation）

<a id="a341203116bfee52d4b801466097fc3eb"></a>

### `data`

```c
uint8_t sys_winstream::data[]
```

<a id="a6b80cf715e4a3ca7b7b74b9efd150a23"></a>

### `end`

```c
uint32_t sys_winstream::end
```

<a id="a30b03df76a51ecbf0cbe33975d5aaa66"></a>

### `len`

```c
uint32_t sys_winstream::len
```

<a id="a7d946d6a54652a8ac035dd8cd0ba861a"></a>

### `seq`

```c
uint32_t sys_winstream::seq
```

<a id="a1cc84dfd9f812b3491135d13365c7a98"></a>

### `start`

```c
uint32_t sys_winstream::start
```

本数据类型文档由以下文件生成：

- `zephyr/sys/winstream.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/sys/winstream.h](https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sys_winstream](P019_sys_winstream_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_sys_mm_drv_region_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_k_object_data_联合体.md)
