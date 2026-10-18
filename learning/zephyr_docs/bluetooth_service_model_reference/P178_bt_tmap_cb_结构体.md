---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-178
title: bt_tmap_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__tmap__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第178章\_bt\_tmap\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__tmap__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话与媒体音频配置文件（TMAP）的回调结构。

```c
#include <zephyr/bluetooth/audio/tmap.h>
```

<a id="details"></a>

电话与媒体音频配置文件（TMAP）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 178.1\_数据成员（Data Fields）

<a id="r_a22ee1b605448a3707d8086de30572def"></a>

```c
void(* discovery_complete )(enum bt_tmap_role role, struct bt_conn *conn, int err)
```

相关声明：[discovery_complete](#a22ee1b605448a3707d8086de30572def)、[bt_tmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga4ef8a550bb374a5f257860082e1411d4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

电话与媒体音频规范（TMAP）发现完成回调。

## 178.2\_详细说明（Detailed Documentation）

<a id="a22ee1b605448a3707d8086de30572def"></a>

### `discovery_complete`

```c
void(* bt_tmap_cb::discovery_complete) (enum bt_tmap_role role, struct bt_conn *conn, int err)
```

电话与媒体音频规范（TMAP）发现完成回调。

此回调向应用通知对端 TMAP 角色（Role）特征的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `role` | 对端的 TMAP 角色，可同时有多个。 |
| `conn` | 指向连接的指针。 |
| `err` | 成功时为 0，否则为从服务器收到的属性协议（ATT）错误。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/tmap.h`

## 178.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/tmap.h](https://docs.zephyrproject.org/latest/doxygen/html/tmap_8h_source.html)
- [bt_tmap_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html#ga4ef8a550bb374a5f257860082e1411d4)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P177_bt_tbs_register_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P179_bt_vcp_included_结构体.md)
