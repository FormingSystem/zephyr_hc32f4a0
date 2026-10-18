---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-65
title: bt_mesh_health_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_bt\_mesh\_health\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

健康客户端（Health Client）的模型上下文。

```c
#include <zephyr/bluetooth/mesh/health_cli.h>
```

<a id="details"></a>

健康客户端（Health Client）的模型上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_ae472c161f7da7c1cb646102ca78f262b"></a>

```c
const struct bt_mesh_model * model
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[model](#ae472c161f7da7c1cb646102ca78f262b)。

组成数据模型条目指针（Composition data model entry pointer）。

<a id="r_ae33ffa14689438b39166f4d90386f329"></a>

```c
struct bt_mesh_model_pub pub
```

相关声明：[bt_mesh_model_pub](P079_bt_mesh_model_pub_结构体.md)、[pub](#ae33ffa14689438b39166f4d90386f329)。

发布结构实例（Publication structure instance）。

<a id="r_a9ae3415b328b25c6206dacdad874c2aa"></a>

```c
struct net_buf_simple pub_buf
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[pub_buf](#a9ae3415b328b25c6206dacdad874c2aa)。

发布缓冲区（Publication buffer）。

<a id="r_a103d110c6cccd69a9e48619668fc60bc"></a>

```c
uint8_t pub_data [BT_MESH_MODEL_BUF_LEN(BT_MESH_MODEL_OP_2(0x80, 0x32), 3)]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pub_data](#a103d110c6cccd69a9e48619668fc60bc)、[BT_MESH_MODEL_BUF_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga5352d6fa05808722eba8a76e2446eddb)、[BT_MESH_MODEL_OP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa52a40ef5972c4f34cf5ff5a10e21289)。

发布数据（Publication data）。

<a id="r_a395f525d846ef029bf5ff9fdde6e7c61"></a>

```c
void(* period_status )(struct bt_mesh_health_cli *cli, uint16_t addr, uint8_t divisor)
```

相关声明：[period_status](#a395f525d846ef029bf5ff9fdde6e7c61)、[bt_mesh_health_cli](P065_bt_mesh_health_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

健康周期状态消息（Health Period Status）的可选回调。

<a id="r_ae8d023ac56beb39c0d73a3b9e75f6c96"></a>

```c
void(* attention_status )(struct bt_mesh_health_cli *cli, uint16_t addr, uint8_t attention)
```

相关声明：[attention_status](#ae8d023ac56beb39c0d73a3b9e75f6c96)、[bt_mesh_health_cli](P065_bt_mesh_health_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

健康关注状态消息（Health Attention Status）的可选回调。

<a id="r_a4cbf24a2407df9bb80e19c1da1558294"></a>

```c
void(* fault_status )(struct bt_mesh_health_cli *cli, uint16_t addr, uint8_t test_id, uint16_t cid, uint8_t *faults, size_t fault_count)
```

相关声明：[fault_status](#a4cbf24a2407df9bb80e19c1da1558294)、[bt_mesh_health_cli](P065_bt_mesh_health_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

健康故障状态消息（Health Fault Status）的可选回调。

<a id="r_a6246d36f8110f401f55003661ab15c86"></a>

```c
void(* current_status )(struct bt_mesh_health_cli *cli, uint16_t addr, uint8_t test_id, uint16_t cid, uint8_t *faults, size_t fault_count)
```

相关声明：[current_status](#a6246d36f8110f401f55003661ab15c86)、[bt_mesh_health_cli](P065_bt_mesh_health_cli_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

健康当前状态消息（Health Current Status）的可选回调。

<a id="r_ae1b396cb99a32a96762d4435629b1ba5"></a>

```c
int(* update )(struct bt_mesh_health_cli *cli, struct net_buf_simple *pub_buf)
```

相关声明：[update](#ae1b396cb99a32a96762d4435629b1ba5)、[bt_mesh_health_cli](P065_bt_mesh_health_cli_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[pub_buf](#a9ae3415b328b25c6206dacdad874c2aa)。

用于更新周期发布消息（Periodic publication message）的可选回调。

<a id="r_ac2ef6ae4fd8e14ad854a9f2c5c80fc43"></a>

```c
struct bt_mesh_msg_ack_ctx ack_ctx
```

相关声明：[bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)、[ack_ctx](#ac2ef6ae4fd8e14ad854a9f2c5c80fc43)。

## 65.2\_详细说明（Detailed Documentation）

<a id="ac2ef6ae4fd8e14ad854a9f2c5c80fc43"></a>

### `ack_ctx`

```c
struct bt_mesh_msg_ack_ctx bt_mesh_health_cli::ack_ctx
```

<a id="ae8d023ac56beb39c0d73a3b9e75f6c96"></a>

### `attention_status`

```c
void(* bt_mesh_health_cli::attention_status) (struct bt_mesh_health_cli *cli, uint16_t addr, uint8_t attention)
```

健康关注状态消息（Health Attention Status）的可选回调。

处理从健康服务器（Health server）收到的健康关注状态消息（Health Attention Status）。`attention` 参数表示当前关注值（Attention value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收状态消息的健康客户端（Health client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `attention` | 当前关注值（Current attention value）。 |

<a id="a6246d36f8110f401f55003661ab15c86"></a>

### `current_status`

```c
void(* bt_mesh_health_cli::current_status) (struct bt_mesh_health_cli *cli, uint16_t addr, uint8_t test_id, uint16_t cid, uint8_t *faults, size_t fault_count)
```

健康当前状态消息（Health Current Status）的可选回调。

处理从健康服务器（Health server）收到的健康当前状态消息（Health Current Status）。故障数组（Fault array）表示服务器所在元素当前存在的全部故障。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收状态消息的健康客户端（Health client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `test_id` | 最近执行的测试的标识符（Test identifier）。 |
| `cid` | 节点的公司标识符（Company Identifier）。 |
| `faults` | 故障数组（Array of faults）。 |
| `fault_count` | 故障数组中的故障数量（Number of faults）。 |

**参阅（See Also）**：另见（See also）：健康故障（Health faults）。

<a id="a4cbf24a2407df9bb80e19c1da1558294"></a>

### `fault_status`

```c
void(* bt_mesh_health_cli::fault_status) (struct bt_mesh_health_cli *cli, uint16_t addr, uint8_t test_id, uint16_t cid, uint8_t *faults, size_t fault_count)
```

健康故障状态消息（Health Fault Status）的可选回调。

处理从健康服务器（Health server）收到的健康故障状态消息（Health Fault Status）。故障数组（Fault array）表示服务器所在元素当前存在的全部故障。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收状态消息的健康客户端（Health client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `test_id` | 最近执行的测试的标识符（Test identifier）。 |
| `cid` | 节点的公司标识符（Company Identifier）。 |
| `faults` | 故障数组（Array of faults）。 |
| `fault_count` | 故障数组中的故障数量（Number of faults）。 |

**参阅（See Also）**：另见（See also）：健康故障（Health faults）。

<a id="ae472c161f7da7c1cb646102ca78f262b"></a>

### `model`

```c
const struct bt_mesh_model* bt_mesh_health_cli::model
```

组成数据模型条目指针（Composition data model entry pointer）。

<a id="a395f525d846ef029bf5ff9fdde6e7c61"></a>

### `period_status`

```c
void(* bt_mesh_health_cli::period_status) (struct bt_mesh_health_cli *cli, uint16_t addr, uint8_t divisor)
```

健康周期状态消息（Health Period Status）的可选回调。

处理从健康服务器（Health server）收到的健康周期状态消息（Health Period Status）。`divisor` 参数表示周期除数值（Period divisor value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 接收状态消息的健康客户端（Health client）。 |
| `addr` | 发送方地址（Address of sender）。 |
| `divisor` | 健康周期除数值（Health Period Divisor value）。 |

<a id="ae33ffa14689438b39166f4d90386f329"></a>

### `pub`

```c
struct bt_mesh_model_pub bt_mesh_health_cli::pub
```

发布结构实例（Publication structure instance）。

<a id="a9ae3415b328b25c6206dacdad874c2aa"></a>

### `pub_buf`

```c
struct net_buf_simple bt_mesh_health_cli::pub_buf
```

发布缓冲区（Publication buffer）。

<a id="a103d110c6cccd69a9e48619668fc60bc"></a>

### `pub_data`

```c
uint8_t bt_mesh_health_cli::pub_data[BT_MESH_MODEL_BUF_LEN(BT_MESH_MODEL_OP_2(0x80, 0x32), 3)]
```

发布数据（Publication data）。

<a id="ae1b396cb99a32a96762d4435629b1ba5"></a>

### `update`

```c
int(* bt_mesh_health_cli::update) (struct bt_mesh_health_cli *cli, struct net_buf_simple *pub_buf)
```

用于更新周期发布消息（Periodic publication message）的可选回调。

此回调在发送周期发布消息（Periodic publication message）前调用，可用于更新待发送的消息。

即使不实现此回调，也可以启用周期发布（Periodic publication），但不会发送任何消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 发送周期发布消息的健康客户端（Health client）。 |
| `pub_buf` | 要更新的发布消息缓冲区（Publication message buffer）。 |

**返回（Returns）**：返回值（Returns）：`pub_buf` 更新成功时为 `0`，失败时返回负错误码。若返回错误，则不会发送该消息。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/health_cli.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/health_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/health__cli_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_model_pub](P079_bt_mesh_model_pub_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_MESH_MODEL_BUF_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga5352d6fa05808722eba8a76e2446eddb)
- [BT_MESH_MODEL_OP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaa52a40ef5972c4f34cf5ff5a10e21289)
- [bt_mesh_health_cli](P065_bt_mesh_health_cli_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_msg_ack_ctx](P081_bt_mesh_msg_ack_ctx_结构体.md)
- [健康故障（Health faults）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__faults.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_bt_mesh_hb_sub_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_bt_mesh_health_srv_结构体.md)
