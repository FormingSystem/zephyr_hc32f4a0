---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-103
title: bt_l2cap_fixed_chan_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__fixed__chan.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第103章\_bt\_l2cap\_fixed\_chan\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__fixed__chan.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固定L2CAP信道（Fixed L2CAP Channel）结构。

```c
#include <zephyr/bluetooth/l2cap.h>
```

<a id="details"></a>

固定 L2CAP 通道（Fixed L2CAP Channel）结构体。应使用 `BT_L2CAP_FIXED_CHANNEL_DEFINE` 宏定义。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 103.1\_数据成员（Data Fields）

<a id="r_a5fd07168ff8a38d6b393ef82a41af9db"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#a5fd07168ff8a38d6b393ef82a41af9db)。

通道标识符（Channel Identifier，CID）。

<a id="r_a83f7dc42454778eed6f446a3875d7663"></a>

```c
int(* accept )(struct bt_conn *conn, struct bt_l2cap_chan **chan)
```

相关声明：[accept](#a83f7dc42454778eed6f446a3875d7663)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)。

通道接受（accept）回调。

## 103.2\_详细说明（Detailed Documentation）

<a id="a83f7dc42454778eed6f446a3875d7663"></a>

### `accept`

```c
int(* bt_l2cap_fixed_chan::accept) (struct bt_conn *conn, struct bt_l2cap_chan **chan)
```

通道接受（accept）回调。

应用必须提供此回调；新连接建立时会调用它。如果接受连接，用户应为一个零初始化的 `bt_l2cap_le_chan` 类型对象分配内存，并更新通道引用 `chan`，使其指向所分配对象的 `bt_l2cap_le_chan::chan` 成员。应按如下方式为 `bt_l2cap_chan_ops` 字段分配回调，以初始化通道：

原始示例（Example）：

```c
static int accept(struct bt_conn *conn, struct bt_l2cap_chan **chan)
{
    // Allocation of fixed_chan and definition of the ops are assumed done prior.
    fixed_chan = (struct bt_l2cap_le_chan){
        .chan.ops = &ops,
    };

    *chan = &fixed_chan.chan;

    return 0;
}
```

所分配的上下文必须在通道的整个生命周期内保持有效，即可以在 `bt_l2cap_chan_ops::released` 回调中释放此内存。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 已建立的连接。 |
| `chan` | L2CAP 通道引用。 |

**警告（Warning）**：警告：虽然通过 `chan` 传回的引用类型是 `bt_l2cap_chan`，但它必须是某个 `bt_l2cap_le_chan` 对象的 `bt_l2cap_le_chan::chan` 成员。协议栈会使用包含它的对象，因此返回一个独立的 `bt_l2cap_chan` 会导致越界访问。

**返回（Returns）**：返回值：返回 0 表示接受此通道连接，否则返回负值错误码。

<a id="a5fd07168ff8a38d6b393ef82a41af9db"></a>

### `cid`

```c
uint16_t bt_l2cap_fixed_chan::cid
```

通道标识符（Channel Identifier，CID）。

**说明（Note）**：注意：取值必须在 `0x0001` 至 `0x003F` 范围内，参见核心规范（Core）v6.0 的 3.A.2.1 节。此范围内的 CID 由协议栈保留，因此应用需要确保所选 CID 尚未被占用。Core 3.A.2.1 的表 2.1 及“L2CAP 通道标识符（L2CAP channel identifiers）”列出了协议栈使用的 CID。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/l2cap.h`

## 103.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)
- [BT_L2CAP_FIXED_CHANNEL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga334ced39f199394971d1600fac42abc8)
- [bt_l2cap_le_chan](P104_bt_l2cap_le_chan_结构体.md)
- [bt_l2cap_le_chan::chan](P104_bt_l2cap_le_chan_结构体.md#a980126cabc3824ab623d634d91f7d761)
- [bt_l2cap_chan_ops](P102_bt_l2cap_chan_ops_结构体.md)
- [bt_l2cap_chan_ops::released](P102_bt_l2cap_chan_ops_结构体.md#a6d974d0e472626cb1e5cd898a3dcbca6)
- [L2CAP 通道标识符（L2CAP channel identifiers）](https://docs.zephyrproject.org/latest/doxygen/html/group__l2cap__cid.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__l2cap__chan_html"></a>
<a id="astructbt__l2cap__fixed__chan_html_a83f7dc42454778eed6f446a3875d7663"></a>
<a id="astructbt__l2cap__le__chan_html"></a>

---

[上一章](P102_bt_l2cap_chan_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P104_bt_l2cap_le_chan_结构体.md)
