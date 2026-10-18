---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-99
title: bt_mesh_send_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__send__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_bt\_mesh\_send\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__send__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

监测模型消息发送的回调结构（Callback Structure）。

```c
#include <zephyr/bluetooth/mesh/access.h>
```

<a id="details"></a>

监测模型消息发送的回调结构（Callback Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 99.1\_数据成员（Data Fields）

<a id="r_a2f84ef4cb2d28729cd98b844a3d25f55"></a>

```c
void(* start )(uint16_t duration, int err, void *cb_data)
```

相关声明：[start](#a2f84ef4cb2d28729cd98b844a3d25f55)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

传输开始时调用的处理函数（Transmission start handler）。

<a id="r_aa169dbec8c96fd41a35616c009604685"></a>

```c
void(* end )(int err, void *cb_data)
```

相关声明：[end](#aa169dbec8c96fd41a35616c009604685)。

传输结束时调用的处理函数（Transmission end handler）。

## 99.2\_详细说明（Detailed Documentation）

<a id="aa169dbec8c96fd41a35616c009604685"></a>

### `end`

```c
void(* bt_mesh_send_cb::end) (int err, void *cb_data)
```

传输结束时调用的处理函数（Transmission end handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `err` | 发送期间发生的错误（Sending error）。 |
| `cb_data` | 传给发送 API 的回调数据（Callback data）。 |

<a id="a2f84ef4cb2d28729cd98b844a3d25f55"></a>

### `start`

```c
void(* bt_mesh_send_cb::start) (uint16_t duration, int err, void *cb_data)
```

传输开始时调用的处理函数（Transmission start handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `duration` | 整个传输的持续时间（Full transmission duration）。 |
| `err` | 发送期间发生的错误（Sending error）。 |
| `cb_data` | 传给发送 API 的回调数据（Callback data）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/access.h`

## 99.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P098_bt_mesh_sar_tx_结构体.md) · [返回大纲](大纲.md) · [下一章](P100_bt_mesh_sol_pdu_rpl_cli_结构体.md)
