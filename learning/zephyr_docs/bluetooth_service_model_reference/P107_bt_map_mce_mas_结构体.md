---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-107
title: bt_map_mce_mas_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mas.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第107章\_bt\_map\_mce\_mas\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mas.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（MAP）客户端的消息访问服务器（MAS）实例结构。

```c
#include <zephyr/bluetooth/classic/map.h>
```

<a id="details"></a>

消息访问规范（MAP）客户端的消息访问服务器（MAS）实例结构体。表示到消息访问服务器（Message Access Server）的客户端连接，用于浏览服务器上的文件夹和操作消息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 107.1\_数据成员（Data Fields）

<a id="r_a19563520b905384652950963fb3f8d65"></a>

```c
struct bt_goep_transport goep_transport
```

相关声明：[bt_goep_transport](P071_bt_goep_transport_结构体.md)、[goep_transport](#a19563520b905384652950963fb3f8d65)。

底层通用对象交换规范传输实例（GOEP transport instance）。

<a id="r_a546fc4ab58f8e8525f4030138db23911"></a>

```c
struct bt_goep goep
```

相关声明：[bt_goep](P070_bt_goep_结构体.md)、[goep](#a546fc4ab58f8e8525f4030138db23911)。

底层通用对象交换规范实例（GOEP instance）。

## 107.2\_详细说明（Detailed Documentation）

<a id="a546fc4ab58f8e8525f4030138db23911"></a>

### `goep`

```c
struct bt_goep bt_map_mce_mas::goep
```

底层通用对象交换规范实例（GOEP instance）。

<a id="a19563520b905384652950963fb3f8d65"></a>

### `goep_transport`

```c
struct bt_goep_transport bt_map_mce_mas::goep_transport
```

底层通用对象交换规范传输实例（GOEP transport instance）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/map.h`

## 107.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)
- [bt_goep_transport](P071_bt_goep_transport_结构体.md)
- [bt_goep](P070_bt_goep_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P106_bt_l2cap_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P108_bt_map_mce_mas_cb_结构体.md)
