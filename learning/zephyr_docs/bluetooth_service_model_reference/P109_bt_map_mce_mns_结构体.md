---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-109
title: bt_map_mce_mns_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mns.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_bt\_map\_mce\_mns\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mce__mns.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（MAP）客户端的消息通知服务器（MNS）实例结构。

```c
#include <zephyr/bluetooth/classic/map.h>
```

<a id="details"></a>

MAP 客户端的消息通知服务器（MNS）实例结构体。表示接收消息通知服务器（Message Notification Server）事件通知的服务器。消息客户端设备（MCE）在 MNS 连接中充当服务器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 109.1\_数据成员（Data Fields）

<a id="r_a89d9f42721e0b5045120f4a7279e0ffb"></a>

```c
struct bt_goep_transport goep_transport
```

相关声明：[bt_goep_transport](P071_bt_goep_transport_结构体.md)、[goep_transport](#a89d9f42721e0b5045120f4a7279e0ffb)。

底层通用对象交换规范传输实例（GOEP transport instance）。

<a id="r_af403bfc88cdd300b27e96cacb477ba42"></a>

```c
struct bt_goep goep
```

相关声明：[bt_goep](P070_bt_goep_结构体.md)、[goep](#af403bfc88cdd300b27e96cacb477ba42)。

底层通用对象交换规范实例（GOEP instance）。

## 109.2\_详细说明（Detailed Documentation）

<a id="af403bfc88cdd300b27e96cacb477ba42"></a>

### `goep`

```c
struct bt_goep bt_map_mce_mns::goep
```

底层通用对象交换规范实例（GOEP instance）。

<a id="a89d9f42721e0b5045120f4a7279e0ffb"></a>

### `goep_transport`

```c
struct bt_goep_transport bt_map_mce_mns::goep_transport
```

底层通用对象交换规范传输实例（GOEP transport instance）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/map.h`

## 109.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)
- [bt_goep_transport](P071_bt_goep_transport_结构体.md)
- [bt_goep](P070_bt_goep_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P108_bt_map_mce_mas_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P110_bt_map_mce_mns_cb_结构体.md)
