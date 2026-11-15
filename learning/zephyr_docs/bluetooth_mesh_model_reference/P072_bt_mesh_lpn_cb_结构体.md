---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-72
title: bt_mesh_lpn_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__lpn__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_bt\_mesh\_lpn\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__lpn__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗节点（Low Power Node，LPN）的回调函数。

```c
#include <zephyr/bluetooth/mesh/main.h>
```

<a id="details"></a>

低功耗节点（Low Power Node，LPN）的回调函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_a74b8b398b383518af069266cf3b0be91"></a>

```c
void(* established )(uint16_t net_idx, uint16_t friend_addr, uint8_t queue_size, uint8_t recv_window)
```

相关声明：[established](#a74b8b398b383518af069266cf3b0be91)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

已建立友谊关系（Friendship established）。

<a id="r_af2e2f5043503c62926f96a5fcb48890c"></a>

```c
void(* terminated )(uint16_t net_idx, uint16_t friend_addr)
```

相关声明：[terminated](#af2e2f5043503c62926f96a5fcb48890c)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

友谊关系已终止（Friendship terminated）。

<a id="r_a9805ad8578faec5b371d6f39178332ef"></a>

```c
void(* polled )(uint16_t net_idx, uint16_t friend_addr, bool retry)
```

相关声明：[polled](#a9805ad8578faec5b371d6f39178332ef)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

本地轮询请求（Local Poll Request）。

## 72.2\_详细说明（Detailed Documentation）

<a id="a74b8b398b383518af069266cf3b0be91"></a>

### `established`

```c
void(* bt_mesh_lpn_cb::established) (uint16_t net_idx, uint16_t friend_addr, uint8_t queue_size, uint8_t recv_window)
```

已建立友谊关系（Friendship established）。

此回调通知应用，友谊关系（Friendship）已成功建立。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 建立友谊关系时使用的网络密钥索引（NetKeyIndex）。 |
| `friend_addr` | 友谊节点地址（Friend address）。 |
| `queue_size` | 友谊节点队列大小（Friend queue size）。 |
| `recv_window` | 低功耗节点等待友谊节点响应的监听时长（Listening duration for Friend response）。 |

<a id="a9805ad8578faec5b371d6f39178332ef"></a>

### `polled`

```c
void(* bt_mesh_lpn_cb::polled) (uint16_t net_idx, uint16_t friend_addr, bool retry)
```

本地轮询请求（Local Poll Request）。

此回调通知应用，本地节点已轮询友谊节点（Friend node）。

尝试建立友谊关系（Friendship）时，此回调先于 `bt_mesh_lpn_cb::established` 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 建立友谊关系时使用的网络密钥索引（NetKeyIndex）。 |
| `friend_addr` | 友谊节点地址（Friend address）。 |
| `retry` | 每个事务的重试或首次轮询请求（Retry or first poll request）。 |

<a id="af2e2f5043503c62926f96a5fcb48890c"></a>

### `terminated`

```c
void(* bt_mesh_lpn_cb::terminated) (uint16_t net_idx, uint16_t friend_addr)
```

友谊关系已终止（Friendship terminated）。

此回调通知应用，友谊关系（Friendship）已终止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 建立友谊关系时使用的网络密钥索引（NetKeyIndex）。 |
| `friend_addr` | 友谊节点地址（Friend address）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/main.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/main.h](https://docs.zephyrproject.org/latest/doxygen/html/main_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_bt_mesh_large_comp_data_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_bt_mesh_lpn_timing_结构体.md)
