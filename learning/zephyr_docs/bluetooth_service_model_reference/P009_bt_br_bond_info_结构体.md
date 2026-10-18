---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-9
title: bt_br_bond_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__bond__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_bt\_br\_bond\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__bond__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与远端设备的绑定（Bond）信息。

```c
#include <zephyr/bluetooth/classic/classic.h>
```

<a id="details"></a>

与远端设备的绑定（Bond）信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_aaa0a6ec8d7010b795a48825df7a8c744"></a>

```c
bt_addr_t addr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[addr](#aaa0a6ec8d7010b795a48825df7a8c744)。

远端设备地址（Remote device address）。

## 9.2\_详细说明（Detailed Documentation）

<a id="aaa0a6ec8d7010b795a48825df7a8c744"></a>

### `addr`

```c
bt_addr_t bt_br_bond_info::addr
```

远端设备地址（Remote device address）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/classic.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/classic.h](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_bt_bip_transport_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_bt_br_conn_param_结构体.md)
