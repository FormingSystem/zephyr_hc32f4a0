---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-62
title: bt_mesh_hb_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__hb__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_bt\_mesh\_hb\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__hb__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

心跳（Heartbeat）的回调结构。

```c
#include <zephyr/bluetooth/mesh/heartbeat.h>
```

<a id="details"></a>

心跳（Heartbeat）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_aa3b85249e1a40842c0f937385a72103f"></a>

```c
void(* recv )(const struct bt_mesh_hb_sub *sub, uint8_t hops, uint16_t feat)
```

相关声明：[recv](#aa3b85249e1a40842c0f937385a72103f)、[bt_mesh_hb_sub](P064_bt_mesh_hb_sub_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

心跳接收回调（Heartbeat receive callback）。

<a id="r_aa979e024174fa19f047a26f94b54a9d3"></a>

```c
void(* sub_end )(const struct bt_mesh_hb_sub *sub)
```

相关声明：[sub_end](#aa979e024174fa19f047a26f94b54a9d3)、[bt_mesh_hb_sub](P064_bt_mesh_hb_sub_结构体.md)。

心跳订阅结束回调（Heartbeat subscription end callback）。

<a id="r_acc5559541f53e2987899433d4d434557"></a>

```c
void(* pub_sent )(const struct bt_mesh_hb_pub *pub)
```

相关声明：[pub_sent](#acc5559541f53e2987899433d4d434557)、[bt_mesh_hb_pub](P063_bt_mesh_hb_pub_结构体.md)。

心跳发布发送完成回调（Heartbeat publication sent callback）。

## 62.2\_详细说明（Detailed Documentation）

<a id="acc5559541f53e2987899433d4d434557"></a>

### `pub_sent`

```c
void(* bt_mesh_hb_cb::pub_sent) (const struct bt_mesh_hb_pub *pub)
```

心跳发布发送完成回调（Heartbeat publication sent callback）。

心跳（Heartbeat）发布成功时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pub` | 当前心跳发布参数（Heartbeat publication parameters）。 |

<a id="aa3b85249e1a40842c0f937385a72103f"></a>

### `recv`

```c
void(* bt_mesh_hb_cb::recv) (const struct bt_mesh_hb_sub *sub, uint8_t hops, uint16_t feat)
```

心跳接收回调（Heartbeat receive callback）。

每次收到与当前心跳订阅参数（Heartbeat subscription parameters）匹配的心跳消息时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sub` | 当前心跳订阅参数（Heartbeat subscription parameters）。 |
| `hops` | 接收此心跳（Heartbeat）时的跳数（Hops）。 |
| `feat` | 发布节点的特性集合（Feature set）。此值是由 `BT_MESH_FEAT_RELAY`、`BT_MESH_FEAT_PROXY`、`BT_MESH_FEAT_FRIEND` 和 `BT_MESH_FEAT_LOW_POWER` 构成的位图。 |

<a id="aa979e024174fa19f047a26f94b54a9d3"></a>

### `sub_end`

```c
void(* bt_mesh_hb_cb::sub_end) (const struct bt_mesh_hb_sub *sub)
```

心跳订阅结束回调（Heartbeat subscription end callback）。

订阅周期（Subscription period）结束时调用，提供所接收心跳消息（Heartbeat messages）的汇总信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sub` | 当前心跳订阅参数（Heartbeat subscription parameters）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/heartbeat.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/heartbeat.h](https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h_source.html)
- [bt_mesh_hb_sub](P064_bt_mesh_hb_sub_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_hb_pub](P063_bt_mesh_hb_pub_结构体.md)
- [BT_MESH_FEAT_RELAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gac588eefe83db94784a420ce063f02b55)
- [BT_MESH_FEAT_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gaee648ce202316c56d4d588cb0ad5aeb4)
- [BT_MESH_FEAT_FRIEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga8f27086b3bc3c4a6e14621836f9f8e80)
- [BT_MESH_FEAT_LOW_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gaad71a36c82b4e4d3fa334ecff5cc0171)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_bt_mesh_friend_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_bt_mesh_hb_pub_结构体.md)
