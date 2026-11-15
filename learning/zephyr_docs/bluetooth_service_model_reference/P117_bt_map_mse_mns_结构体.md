---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-117
title: bt_map_mse_mns_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mse__mns.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_bt\_map\_mse\_mns\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__map__mse__mns.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息访问配置文件（MAP）服务器的消息通知服务器（MNS）实例结构。

```c
#include <zephyr/bluetooth/classic/map.h>
```

<a id="details"></a>

MAP 服务器 MNS 实例结构体。表示到消息通知服务器（Message Notification Server）的客户端连接，用于向消息客户端设备（MCE）发送事件通知。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 117.1\_数据成员（Data Fields）

<a id="r_a524c23c6e1513bb641b103cb8fde37cb"></a>

```c
struct bt_goep_transport goep_transport
```

相关声明：[bt_goep_transport](P071_bt_goep_transport_结构体.md)、[goep_transport](#a524c23c6e1513bb641b103cb8fde37cb)。

底层通用对象交换规范传输实例（GOEP transport instance）。

<a id="r_a6815c3c6af06b8cf618e9cf83fead584"></a>

```c
struct bt_goep goep
```

相关声明：[bt_goep](P070_bt_goep_结构体.md)、[goep](#a6815c3c6af06b8cf618e9cf83fead584)。

底层通用对象交换规范实例（GOEP instance）。

## 117.2\_详细说明（Detailed Documentation）

<a id="a6815c3c6af06b8cf618e9cf83fead584"></a>

### `goep`

```c
struct bt_goep bt_map_mse_mns::goep
```

底层通用对象交换规范实例（GOEP instance）。

<a id="a524c23c6e1513bb641b103cb8fde37cb"></a>

### `goep_transport`

```c
struct bt_goep_transport bt_map_mse_mns::goep_transport
```

底层通用对象交换规范传输实例（GOEP transport instance）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/map.h`

## 117.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/map.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2map_8h_source.html)
- [bt_goep_transport](P071_bt_goep_transport_结构体.md)
- [bt_goep](P070_bt_goep_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P116_bt_map_mse_mas_rfcomm_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P118_bt_map_mse_mns_cb_结构体.md)
