---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-6
title: bt_conn_br_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__br__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_bt\_conn\_br\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__br__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BR/EDR 连接信息（Connection Info）结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

BR/EDR 连接信息（Connection Info）结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_aeef49f711872ccfec5dd558c4552b71e"></a>

```c
const bt_addr_t * dst
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[dst](#aeef49f711872ccfec5dd558c4552b71e)。

目的，即远端的基本速率／增强数据率地址（Destination／Remote BR/EDR address）。

## 6.2\_详细说明（Detailed Documentation）

<a id="aeef49f711872ccfec5dd558c4552b71e"></a>

### `dst`

```c
const bt_addr_t* bt_conn_br_info::dst
```

目的，即远端的基本速率／增强数据率地址（Destination／Remote BR/EDR address）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_bt_conn_br_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_bt_conn_br_remote_info_结构体.md)
