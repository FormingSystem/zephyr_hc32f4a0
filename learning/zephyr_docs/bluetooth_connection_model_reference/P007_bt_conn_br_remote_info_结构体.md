---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-7
title: bt_conn_br_remote_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__br__remote__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_bt\_conn\_br\_remote\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__br__remote__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BR/EDR 连接的远端信息（Remote Info）结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

BR/EDR 连接的远端信息（Remote Info）结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_afa19f7db400bb0de234e8cda61f3deaf"></a>

```c
const uint8_t * features
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[features](#afa19f7db400bb0de234e8cda61f3deaf)。

远端特性集合（Remote feature set），由若干页位掩码组成。

<a id="r_a798c179c803e709182a1b0c3594f4a0a"></a>

```c
uint8_t num_pages
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_pages](#a798c179c803e709182a1b0c3594f4a0a)。

远端特性集合（Remote feature set）的页数。

## 7.2\_详细说明（Detailed Documentation）

<a id="afa19f7db400bb0de234e8cda61f3deaf"></a>

### `features`

```c
const uint8_t* bt_conn_br_remote_info::features
```

远端特性集合（Remote feature set），由若干页位掩码组成。

<a id="a798c179c803e709182a1b0c3594f4a0a"></a>

### `num_pages`

```c
uint8_t bt_conn_br_remote_info::num_pages
```

远端特性集合（Remote feature set）的页数。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_bt_conn_br_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_bt_conn_cb_结构体.md)
