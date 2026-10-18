---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-68
title: bt_gmap_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gmap__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_bt\_gmap\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gmap__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

游戏音频配置文件（Gaming Audio Profile，GMAP）的回调结构体。

```c
#include <zephyr/bluetooth/audio/gmap.h>
```

<a id="details"></a>

游戏音频配置文件（Gaming Audio Profile，GMAP）的回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_a72c25ae277e04d419f41733d0b11aefc"></a>

```c
void(* discover )(struct bt_conn *conn, int err, enum bt_gmap_role role, struct bt_gmap_feat features)
```

相关声明：[discover](#a72c25ae277e04d419f41733d0b11aefc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_gmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga55ecab78bcd6de6c294abdc20ad10e56)、[bt_gmap_feat](P069_bt_gmap_feat_结构体.md)。

`bt_gmap_discover()` 的回调函数（Callback function）。

## 68.2\_详细说明（Detailed Documentation）

<a id="a72c25ae277e04d419f41733d0b11aefc"></a>

### `discover`

```c
void(* bt_gmap_cb::discover) (struct bt_conn *conn, int err, enum bt_gmap_role role, struct bt_gmap_feat features)
```

`bt_gmap_discover()` 的回调函数（Callback function）。

发现过程（Discovery procedure）完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 蓝牙连接对象（Bluetooth connection object）。 |
| `err` | 成功时为 `0`，否则为属性协议错误（ATT error）或负的错误编号（errno）。 |
| `role` | 远端设备角色（Role）。失败时为 `0`。 |
| `features` | 远端特性（Remote features）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/gmap.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/gmap.h](https://docs.zephyrproject.org/latest/doxygen/html/gmap_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_gmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#ga55ecab78bcd6de6c294abdc20ad10e56)
- [bt_gmap_feat](P069_bt_gmap_feat_结构体.md)
- [bt_gmap_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html#gab54963e226753d44085a7d1f5dccdef6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_bt_ets_elapsed_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_bt_gmap_feat_结构体.md)
