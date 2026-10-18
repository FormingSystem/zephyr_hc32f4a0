---
id: learning.zephyr-docs.network-application-model-reference.page-69
title: mqtt_sn_data_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_mqtt\_sn\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内存缓冲区（Memory Buffers）的抽象。

```c
#include <zephyr/net/mqtt_sn.h>
```

<a id="details"></a>

内存缓冲区（Memory Buffers）的抽象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_ae3726684337ee8175224d11dfcf4a7c6"></a>

```c
const uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ae3726684337ee8175224d11dfcf4a7c6)。

数据指针。

<a id="r_a3ceba49fc5a2a1cafe2d8dc0a2b56dae"></a>

```c
size_t size
```

相关声明：[size](#a3ceba49fc5a2a1cafe2d8dc0a2b56dae)。

数据大小，单位为字节。

## 69.2\_详细说明（Detailed Documentation）

<a id="ae3726684337ee8175224d11dfcf4a7c6"></a>

### `data`

```c
const uint8_t* mqtt_sn_data::data
```

数据指针。

<a id="a3ceba49fc5a2a1cafe2d8dc0a2b56dae"></a>

### `size`

```c
size_t mqtt_sn_data::size
```

数据大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/net/mqtt_sn.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/net/mqtt_sn.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt__sn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_mqtt_sn_connect_retry_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_mqtt_sn_evt_结构体.md)
