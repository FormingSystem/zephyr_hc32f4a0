---
id: learning.zephyr-docs.system-service-model-reference.page-78
title: smp_client_object_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmp__client__object.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_smp\_client\_object\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmp__client__object.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单管理协议（SMP）的客户端对象。

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

<a id="details"></a>

简单管理协议（SMP）的客户端对象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 78.1\_数据成员（Data Fields）

<a id="r_ae4c73b23b90ef9f6cb8a93efde992c8a"></a>

```c
struct k_work work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[work](#ae4c73b23b90ef9f6cb8a93efde992c8a)。

必须是第一个成员。

<a id="r_a5d3cf1e109692112bf52b0b8514bab9f"></a>

```c
struct k_fifo tx_fifo
```

相关声明：[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[tx_fifo](#a5d3cf1e109692112bf52b0b8514bab9f)。

客户端发送（TX）队列使用的 FIFO。

<a id="r_a01507d6fa5a75751b39ccda82d0836ef"></a>

```c
struct smp_transport * smpt
```

相关声明：[smp_transport](P081_smp_transport_结构体.md)、[smpt](#a01507d6fa5a75751b39ccda82d0836ef)。

简单管理协议（SMP）传输对象。

<a id="r_a0de9e7ee538b84cf1a6065b7b8b0bc53"></a>

```c
uint8_t smp_seq
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[smp_seq](#a0de9e7ee538b84cf1a6065b7b8b0bc53)。

SMP 序号（SEQ）。

<a id="r_a9623a174f2be0f73903ee860b2ea374e"></a>

```c
void * priv
```

相关声明：[priv](#a9623a174f2be0f73903ee860b2ea374e)。

SMP 传输数据。

## 78.2\_详细说明（Detailed Documentation）

<a id="a9623a174f2be0f73903ee860b2ea374e"></a>

### `priv`

```c
void* smp_client_object::priv
```

SMP 传输数据。

允许单个 `smp_transport` 关联多个 `client_object`。

<a id="a0de9e7ee538b84cf1a6065b7b8b0bc53"></a>

### `smp_seq`

```c
uint8_t smp_client_object::smp_seq
```

SMP 序号（SEQ）。

<a id="a01507d6fa5a75751b39ccda82d0836ef"></a>

### `smpt`

```c
struct smp_transport* smp_client_object::smpt
```

简单管理协议（SMP）传输对象。

<a id="a5d3cf1e109692112bf52b0b8514bab9f"></a>

### `tx_fifo`

```c
struct k_fifo smp_client_object::tx_fifo
```

客户端发送（TX）队列使用的 FIFO。

<a id="ae4c73b23b90ef9f6cb8a93efde992c8a"></a>

### `work`

```c
struct k_work smp_client_object::work
```

必须是第一个成员。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/smp/smp_client.h`

## 78.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/smp/smp_client.h](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h_source.html)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [smp_transport](P081_smp_transport_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P077_settings_mgmt_access_结构体.md) · [返回大纲](大纲.md) · [下一章](P079_smp_client_transport_entry_结构体.md)
