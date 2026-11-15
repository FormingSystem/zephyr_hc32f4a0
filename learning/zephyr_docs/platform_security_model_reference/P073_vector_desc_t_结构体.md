---
id: learning.zephyr-docs.platform-security-model-reference.page-73
title: vector_desc_t_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvector__desc__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_vector\_desc\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvector__desc__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/interrupt_controller/intc_esp32.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 73.1\_数据成员（Data Fields）

<a id="r_a08740a5225fef571398bbd91a42fc970"></a>

```c
int flags: 16
```

相关声明：[flags](#a08740a5225fef571398bbd91a42fc970)。

<a id="r_a853c50cd06725b9502fa14af262d76b9"></a>

```c
unsigned int cpu: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[cpu](#a853c50cd06725b9502fa14af262d76b9)。

<a id="r_a74e81e89da2ca79df99911d0599e5f77"></a>

```c
unsigned int intno: 5
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[intno](#a74e81e89da2ca79df99911d0599e5f77)。

<a id="r_a8adcec0946b8790de75af65a6ae03ccc"></a>

```c
int source: 16
```

相关声明：[source](#a8adcec0946b8790de75af65a6ae03ccc)。

<a id="r_a9934f0a683b6f2145ce35a395a65b967"></a>

```c
struct shared_vector_desc_t * shared_vec_info
```

相关声明：[shared_vector_desc_t](P055_shared_vector_desc_t_结构体.md)、[shared_vec_info](#a9934f0a683b6f2145ce35a395a65b967)。

<a id="r_a4b3b6db584511e25407e187d4dbf6ac8"></a>

```c
struct vector_desc_t * next
```

相关声明：[vector_desc_t](P073_vector_desc_t_结构体.md)、[next](#a4b3b6db584511e25407e187d4dbf6ac8)。

## 73.2\_详细说明（Detailed Documentation）

<a id="a853c50cd06725b9502fa14af262d76b9"></a>

### `cpu`

```c
unsigned int vector_desc_t::cpu
```

<a id="a08740a5225fef571398bbd91a42fc970"></a>

### `flags`

```c
int vector_desc_t::flags
```

<a id="a74e81e89da2ca79df99911d0599e5f77"></a>

### `intno`

```c
unsigned int vector_desc_t::intno
```

<a id="a4b3b6db584511e25407e187d4dbf6ac8"></a>

### `next`

```c
struct vector_desc_t* vector_desc_t::next
```

<a id="a9934f0a683b6f2145ce35a395a65b967"></a>

### `shared_vec_info`

```c
struct shared_vector_desc_t* vector_desc_t::shared_vec_info
```

<a id="a8adcec0946b8790de75af65a6ae03ccc"></a>

### `source`

```c
int vector_desc_t::source
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/interrupt_controller/intc_esp32.h`

## 73.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/intc_esp32.h](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [shared_vector_desc_t](P055_shared_vector_desc_t_结构体.md)
- [vector_desc_t](P073_vector_desc_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P072_tisci_version_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P074_vtd_driver_api_结构体.md)
