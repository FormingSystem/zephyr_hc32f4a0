---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-66
title: peci_buf_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpeci__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_peci\_buf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpeci__buf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

平台环境控制接口（PECI）的缓冲区结构。

```c
#include <zephyr/drivers/peci.h>
```

<a id="details"></a>

平台环境控制接口（PECI）的缓冲区结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_aca55975957106666161da358b7f85db6"></a>

```c
uint8_t * buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#aca55975957106666161da358b7f85db6)。

指向数据缓冲区的有效指针，否则为 `NULL`。

<a id="r_a8e3fd0ef3f9141113214b89bb589a5e9"></a>

```c
size_t len
```

相关声明：[len](#a8e3fd0ef3f9141113214b89bb589a5e9)。

预期接收的数据缓冲区长度，不计入帧校验序列（Frame Check Sequence，FCS）字节。

## 66.2\_详细说明（Detailed Documentation）

<a id="aca55975957106666161da358b7f85db6"></a>

### `buf`

```c
uint8_t* peci_buf::buf
```

指向数据缓冲区的有效指针，否则为 `NULL`。

<a id="a8e3fd0ef3f9141113214b89bb589a5e9"></a>

### `len`

```c
size_t peci_buf::len
```

预期接收的数据缓冲区长度，不计入帧校验序列（Frame Check Sequence，FCS）字节。

**说明（Note）**：注意：帧校验序列字节会添加到接收缓冲区，因此必须为它在接收缓冲区中额外分配一个字节。

本数据类型文档由以下文件生成：

- `zephyr/drivers/peci.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/drivers/peci.h](https://docs.zephyrproject.org/latest/doxygen/html/peci_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_osdp_event_keypress_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_peci_driver_api_结构体.md)
