---
id: learning.zephyr-docs.platform-security-model-reference.page-61
title: tee_param_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtee__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_tee\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtee__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可信执行环境（TEE）的参数。

```c
#include <zephyr/drivers/tee.h>
```

<a id="details"></a>

TEE 参数（Parameter）。`attr & TEE_PARAM_ATTR_TYPE_MASK` 指示联合体使用 `memref` 还是 `value`。`TEE_PARAM_ATTR_TYPE_VALUE_*` 表示使用 `value`，`TEE_PARAM_ATTR_TYPE_MEMREF_*` 表示使用 `memref`。`TEE_PARAM_ATTR_TYPE_NONE` 表示不使用任何成员。

共享内存通过 `TEE_IOC_SHM_ALLOC` 分配，该操作返回表示共享内存对象的标识符。`memref` 可以通过指定对象内的偏移量 `(a)` 和大小 `(b)`，引用共享内存的一部分。要提供整个共享内存对象，应将偏移量 `(a)` 设为 `0`，将大小 `(b)` 设为先前返回的对象大小。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_ac8ced719ce993735e22d68ca50f54e5b"></a>

```c
uint64_t attr
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[attr](#ac8ced719ce993735e22d68ca50f54e5b)。

属性（Attributes）。

<a id="r_aea8916d1bc24ab5a56f59fa4608f1a38"></a>

```c
uint64_t a
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[a](#aea8916d1bc24ab5a56f59fa4608f1a38)。

若为内存引用（memref），则表示共享内存对象内的偏移量；否则为一个值。

<a id="r_a22785fe00950c3a7d6353c39b12d72a8"></a>

```c
uint64_t b
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[b](#a22785fe00950c3a7d6353c39b12d72a8)。

若为内存引用（memref），则表示缓冲区大小；否则为值参数。

<a id="r_a79b39571785949e32629216742e34d72"></a>

```c
uint64_t c
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[c](#a79b39571785949e32629216742e34d72)。

若为内存引用（memref），则表示共享内存标识符；否则为值参数。

## 61.2\_详细说明（Detailed Documentation）

<a id="aea8916d1bc24ab5a56f59fa4608f1a38"></a>

### `a`

```c
uint64_t tee_param::a
```

若为内存引用（memref），则表示共享内存对象内的偏移量；否则为一个值。

<a id="ac8ced719ce993735e22d68ca50f54e5b"></a>

### `attr`

```c
uint64_t tee_param::attr
```

属性（Attributes）。

<a id="a22785fe00950c3a7d6353c39b12d72a8"></a>

### `b`

```c
uint64_t tee_param::b
```

若为内存引用（memref），则表示缓冲区大小；否则为值参数。

<a id="a79b39571785949e32629216742e34d72"></a>

### `c`

```c
uint64_t tee_param::c
```

若为内存引用（memref），则表示共享内存标识符；否则为值参数。

本数据类型文档由以下文件生成：

- `zephyr/drivers/tee.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/drivers/tee.h](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_tee_open_session_arg_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_tee_shm_结构体.md)
