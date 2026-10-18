---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-91
title: bt_mesh_rpr_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_bt\_mesh\_rpr\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

远程配网客户端（Remote Provisioning Client）的模型实例。

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

<a id="details"></a>

远程配网客户端（Remote Provisioning Client）的模型实例。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 91.1\_数据成员（Data Fields）

<a id="r_a32b3c63218b506d1bc5759640cb3fb81"></a>

```c
void(* scan_report )(struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_unprov *unprov, struct net_buf_simple *adv_data)
```

相关声明：[scan_report](#a32b3c63218b506d1bc5759640cb3fb81)、[bt_mesh_rpr_cli](P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](P093_bt_mesh_rpr_node_结构体.md)、[srv](#a8f5eea4cbb042f8a83050ad4ebfc64b7)、[bt_mesh_rpr_unprov](P095_bt_mesh_rpr_unprov_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

扫描报告回调（Scan report callback）。

<a id="r_a9cc5b67937ec8e0ff93ddfb55cb11528"></a>

```c
struct bt_mesh_msg_ack_ctx scan_ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[scan_ack_ctx](#a9cc5b67937ec8e0ff93ddfb55cb11528)。

<a id="r_a0e5a8d697b87f5f05bbce0aaa8c1fb1a"></a>

```c
struct bt_mesh_msg_ack_ctx prov_ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[prov_ack_ctx](#a0e5a8d697b87f5f05bbce0aaa8c1fb1a)。

```c
struct {
```

<a id="r_a0e4b00c6b59978b81e97ff58440db8a1"></a>

```c
struct k_work_delayable timeout
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[timeout](#a64b12ca2ef9e47723c77a8af41eb0f89)。

<a id="r_a14cf5fa332727456686b2bf3086d63d1"></a>

```c
struct bt_mesh_rpr_node srv
```

相关声明：[bt_mesh_rpr_node](P093_bt_mesh_rpr_node_结构体.md)、[srv](#a8f5eea4cbb042f8a83050ad4ebfc64b7)。

<a id="r_a4477e68cdbb50868775ebf2ba2621427"></a>

```c
uint8_t time
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[time](#af03b9edb0a205e92182234c7a1355e0c)。

<a id="r_ab07520f3b09c62d04a38fe1ad4dcd228"></a>

```c
uint8_t tx_pdu
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_pdu](#a68eaadc451224e155227d14102ff0a54)。

<a id="r_a50ebc81c2646c700477ff0455ee47031"></a>

```c
uint8_t rx_pdu
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_pdu](#a8493c4b3c1e30cc0a6f58b765adb2e37)。

<a id="r_a011ba84296a6103e7e5a84dd16b279e7"></a>

```c
enum bt_mesh_rpr_link_state state
```

相关声明：[bt_mesh_rpr_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga0266611238d10f8e97f2b07156991f43)、[state](#aa29cbb7e19cc659ce13b0b98604c93d5)。

<a id="r_ad69049681d611aa48be4942745fb89a7"></a>

```c
} link
```

相关声明：[link](#ad69049681d611aa48be4942745fb89a7)。

<a id="r_a188c9e610035b7225411b45733be5a85"></a>

```c
const struct bt_mesh_model * mod
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[mod](#a188c9e610035b7225411b45733be5a85)。

## 91.2\_详细说明（Detailed Documentation）

<a id="ad69049681d611aa48be4942745fb89a7"></a>

### `[struct]`

```c
struct { ... } bt_mesh_rpr_cli::link
```

<a id="a188c9e610035b7225411b45733be5a85"></a>

### `mod`

```c
const struct bt_mesh_model* bt_mesh_rpr_cli::mod
```

<a id="a0e5a8d697b87f5f05bbce0aaa8c1fb1a"></a>

### `prov_ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_rpr_cli::prov_ack_ctx
```

<a id="a8493c4b3c1e30cc0a6f58b765adb2e37"></a>

### `rx_pdu`

```c
uint8_t bt_mesh_rpr_cli::rx_pdu
```

<a id="a9cc5b67937ec8e0ff93ddfb55cb11528"></a>

### `scan_ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_rpr_cli::scan_ack_ctx
```

<a id="a32b3c63218b506d1bc5759640cb3fb81"></a>

### `scan_report`

```c
void(* bt_mesh_rpr_cli::scan_report) (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_unprov *unprov, struct net_buf_simple *adv_data)
```

扫描报告回调（Scan report callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 远程配网客户端（Remote Provisioning Client）。 |
| `srv` | 远程配网服务器（Remote Provisioning Server）。 |
| `unprov` | 未配网设备（Unprovisioned Device）。 |
| `adv_data` | 未配网设备的广播数据（Advertisement data）；若未启用扩展扫描（Extended scanning），则为 `NULL`。空缓冲区表示扩展扫描已结束，但未收集到附加信息。 |

<a id="a8f5eea4cbb042f8a83050ad4ebfc64b7"></a>

### `srv`

```c
struct bt_mesh_rpr_node bt_mesh_rpr_cli::srv
```

<a id="aa29cbb7e19cc659ce13b0b98604c93d5"></a>

### `state`

```c
enum bt_mesh_rpr_link_state bt_mesh_rpr_cli::state
```

<a id="af03b9edb0a205e92182234c7a1355e0c"></a>

### `time`

```c
uint8_t bt_mesh_rpr_cli::time
```

<a id="a64b12ca2ef9e47723c77a8af41eb0f89"></a>

### `timeout`

```c
struct k_work_delayable bt_mesh_rpr_cli::timeout
```

<a id="a68eaadc451224e155227d14102ff0a54"></a>

### `tx_pdu`

```c
uint8_t bt_mesh_rpr_cli::tx_pdu
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/rpr_cli.h`

## 91.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/rpr_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h_source.html)
- [bt_mesh_rpr_cli](P091_bt_mesh_rpr_cli_结构体.md)
- [bt_mesh_rpr_node](P093_bt_mesh_rpr_node_结构体.md)
- [bt_mesh_rpr_unprov](P095_bt_mesh_rpr_unprov_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_rpr_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga0266611238d10f8e97f2b07156991f43)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P090_bt_mesh_rpr_caps_结构体.md) · [返回大纲](大纲.md) · [下一章](P092_bt_mesh_rpr_link_结构体.md)
