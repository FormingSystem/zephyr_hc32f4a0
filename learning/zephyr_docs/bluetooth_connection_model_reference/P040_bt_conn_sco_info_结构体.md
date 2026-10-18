---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-40
title: bt_conn_sco_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__sco__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_bt\_conn\_sco\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__sco__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

同步面向连接（SCO）连接信息结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

同步面向连接（SCO）连接信息结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_aad5fc309d1ffccda38c07b40ac028dd1"></a>

```c
uint8_t link_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[link_type](#aad5fc309d1ffccda38c07b40ac028dd1)。

同步面向连接链路类型（SCO link type）。

<a id="r_ae4474ebfe0129eb6214987a31430d4f7"></a>

```c
uint8_t air_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[air_mode](#ae4474ebfe0129eb6214987a31430d4f7)。

同步面向连接链路空中模式（SCO air mode），即编解码器类型（Codec type）。

## 40.2\_详细说明（Detailed Documentation）

<a id="ae4474ebfe0129eb6214987a31430d4f7"></a>

### `air_mode`

```c
uint8_t bt_conn_sco_info::air_mode
```

同步面向连接链路空中模式（SCO air mode），即编解码器类型（Codec type）。

<a id="aad5fc309d1ffccda38c07b40ac028dd1"></a>

### `link_type`

```c
uint8_t bt_conn_sco_info::link_type
```

同步面向连接链路类型（SCO link type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_bt_conn_remote_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_bt_data_结构体.md)
