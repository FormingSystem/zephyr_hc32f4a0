---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-10
title: bt_br_conn_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__conn__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_bt\_br\_conn\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__conn__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基本速率／增强数据速率（BR/EDR）连接的连接参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

基本速率／增强数据速率（BR/EDR）连接的连接参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a95454a74932a14b4137c3fe82821be49"></a>

```c
bool allow_role_switch
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[allow_role_switch](#a95454a74932a14b4137c3fe82821be49)。

## 10.2\_详细说明（Detailed Documentation）

<a id="a95454a74932a14b4137c3fe82821be49"></a>

### `allow_role_switch`

```c
bool bt_br_conn_param::allow_role_switch
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_bt_br_bond_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_bt_br_discovery_cb_结构体.md)
