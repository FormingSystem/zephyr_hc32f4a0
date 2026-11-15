---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-71
title: bt_goep_transport_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_bt\_goep\_transport\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__goep__transport.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GOEP 传输统一结构体（Transport Unified Structure）。

```c
#include <zephyr/bluetooth/classic/goep.h>
```

<a id="details"></a>

GOEP 传输统一结构体（Transport Unified Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_adcf88fd5c75b25f9b43fc6432f4ed41e"></a>

```c
struct bt_goep_transport_v1 v1
```

相关声明：[bt_goep_transport_v1](P075_bt_goep_transport_v1_结构体.md)、[v1](#adcf88fd5c75b25f9b43fc6432f4ed41e)。

通用对象交换规范 v1.1 传输（GOEP v1.1 transport）。

<a id="r_a607ceb28a77f1cb74cfa5188c9cc8ce4"></a>

```c
struct bt_goep_transport_v2 v2
```

相关声明：[bt_goep_transport_v2](P076_bt_goep_transport_v2_结构体.md)、[v2](#a607ceb28a77f1cb74cfa5188c9cc8ce4)。

通用对象交换规范 v2 传输（GOEP v2 transport）。

## 71.2\_详细说明（Detailed Documentation）

<a id="adcf88fd5c75b25f9b43fc6432f4ed41e"></a>

### `v1`

```c
struct bt_goep_transport_v1 bt_goep_transport::v1
```

通用对象交换规范 v1.1 传输（GOEP v1.1 transport）。

<a id="a607ceb28a77f1cb74cfa5188c9cc8ce4"></a>

### `v2`

```c
struct bt_goep_transport_v2 bt_goep_transport::v2
```

通用对象交换规范 v2 传输（GOEP v2 transport）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/goep.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h_source.html)
- [bt_goep_transport_v1](P075_bt_goep_transport_v1_结构体.md)
- [bt_goep_transport_v2](P076_bt_goep_transport_v2_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_bt_goep_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_bt_goep_transport_l2cap_server_结构体.md)
