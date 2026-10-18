---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-61
title: bt_mesh_friend_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__friend__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_bt\_mesh\_friend\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__friend__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

好友节点（Friend Node）的回调函数。

```c
#include <zephyr/bluetooth/mesh/main.h>
```

<a id="details"></a>

好友节点（Friend Node）的回调函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_a824ed814a46a3954d2c6f669c8900156"></a>

```c
void(* established )(uint16_t net_idx, uint16_t lpn_addr, uint8_t recv_delay, uint32_t polltimeout)
```

相关声明：[established](#a824ed814a46a3954d2c6f669c8900156)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

已建立友谊关系（Friendship established）。

<a id="r_a1c0d570eb1b857c65b3b5b4ce31999d6"></a>

```c
void(* terminated )(uint16_t net_idx, uint16_t lpn_addr)
```

相关声明：[terminated](#a1c0d570eb1b857c65b3b5b4ce31999d6)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

友谊关系已终止（Friendship terminated）。

<a id="r_a7b904967d89173f82ac26216e3849d23"></a>

```c
void(* polled )(uint16_t net_idx, uint16_t lpn_addr)
```

相关声明：[polled](#a7b904967d89173f82ac26216e3849d23)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

友谊轮询请求（Friend Poll Request）。

## 61.2\_详细说明（Detailed Documentation）

<a id="a824ed814a46a3954d2c6f669c8900156"></a>

### `established`

```c
void(* bt_mesh_friend_cb::established) (uint16_t net_idx, uint16_t lpn_addr, uint8_t recv_delay, uint32_t polltimeout)
```

已建立友谊关系（Friendship established）。

此回调通知应用，友谊关系（Friendship）已成功建立。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 建立友谊关系时使用的网络密钥索引（NetKeyIndex）。 |
| `lpn_addr` | 低功耗节点地址（Low Power Node address）。 |
| `recv_delay` | 接收延迟（Receive Delay），以 1 毫秒为单位。 |
| `polltimeout` | 轮询超时（PollTimeout），以 1 毫秒为单位。 |

<a id="a7b904967d89173f82ac26216e3849d23"></a>

### `polled`

```c
void(* bt_mesh_friend_cb::polled) (uint16_t net_idx, uint16_t lpn_addr)
```

友谊轮询请求（Friend Poll Request）。

此回调通知应用，低功耗节点（Low Power Node）已轮询友谊节点（Friend node）。

尝试建立友谊关系（Friendship）时，此回调先于 `bt_mesh_friend_cb::established` 调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 建立友谊关系时使用的网络密钥索引（NetKeyIndex）。 |
| `lpn_addr` | 低功耗节点地址（LPN address）。 |

<a id="a1c0d570eb1b857c65b3b5b4ce31999d6"></a>

### `terminated`

```c
void(* bt_mesh_friend_cb::terminated) (uint16_t net_idx, uint16_t lpn_addr)
```

友谊关系已终止（Friendship terminated）。

此回调通知应用，友谊关系（Friendship）已终止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 建立友谊关系时使用的网络密钥索引（NetKeyIndex）。 |
| `lpn_addr` | 低功耗节点地址（Low Power Node address）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/main.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/main.h](https://docs.zephyrproject.org/latest/doxygen/html/main_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_bt_mesh_elem__bt_mesh_elem_rt_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_bt_mesh_hb_cb_结构体.md)
