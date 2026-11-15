---
id: learning.zephyr-docs.api-device-topic-reference.page-5
title: 蓝牙 Mesh 分段与重组配置客户端模型（SAR Configuration Client Model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_蓝牙 Mesh 分段与重组配置客户端模型（SAR Configuration Client Model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙网状网络（Bluetooth Mesh）

<a id="details"></a>

蓝牙网状网络（Bluetooth Mesh）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fsar_5Fcfg_5Fcli"></a>

```c
struct bt_mesh_sar_cfg_cli
```

相关声明：[bt_mesh_sar_cfg_cli](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md)。

Mesh分段与重组配置客户端（SAR Configuration Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga742d31e7175e472f1a096ffa6a5acdc5"></a>

```c
#define BT_MESH_MODEL_SAR_CFG_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_SAR_CFG_CLI](#ga742d31e7175e472f1a096ffa6a5acdc5)。

分段与重组配置客户端（SAR Configuration Client）模型的组成数据条目（composition data entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_ga893ef5861708bec12f87b9f9cc64b9fc"></a>

```c
int bt_mesh_sar_cfg_cli_transmitter_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_sar_tx *rsp)
```

相关声明：[bt_mesh_sar_cfg_cli_transmitter_get](#ga893ef5861708bec12f87b9f9cc64b9fc)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)。

获取目标节点的 SAR 发送端（SAR Transmitter）状态。

<a id="r_ga32e2a580b24a41761911e88413e9664e"></a>

```c
int bt_mesh_sar_cfg_cli_transmitter_set (uint16_t net_idx, uint16_t addr, const struct bt_mesh_sar_tx *set, struct bt_mesh_sar_tx *rsp)
```

相关声明：[bt_mesh_sar_cfg_cli_transmitter_set](#ga32e2a580b24a41761911e88413e9664e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)、[bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)。

设置目标节点的 SAR 发送端状态。

<a id="r_ga444c99254ef2ccdd10dac08a94219d79"></a>

```c
int bt_mesh_sar_cfg_cli_receiver_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_sar_rx *rsp)
```

相关声明：[bt_mesh_sar_cfg_cli_receiver_get](#ga444c99254ef2ccdd10dac08a94219d79)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)。

获取目标节点的 SAR 接收端（SAR Receiver）状态。

<a id="r_ga884025b2baf8559950ba6dc83e9ef486"></a>

```c
int bt_mesh_sar_cfg_cli_receiver_set (uint16_t net_idx, uint16_t addr, const struct bt_mesh_sar_rx *set, struct bt_mesh_sar_rx *rsp)
```

相关声明：[bt_mesh_sar_cfg_cli_receiver_set](#ga884025b2baf8559950ba6dc83e9ef486)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)、[bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)。

设置目标节点的 SAR 接收端状态。

<a id="r_ga998846e5735676dc5f79b387d02630d4"></a>

```c
int32_t bt_mesh_sar_cfg_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_sar_cfg_cli_timeout_get](#ga998846e5735676dc5f79b387d02630d4)。

获取当前传输超时值（transmission timeout）。

<a id="r_ga57d7c6a973b35f53689cbf8a065a538f"></a>

```c
void bt_mesh_sar_cfg_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_sar_cfg_cli_timeout_set](#ga57d7c6a973b35f53689cbf8a065a538f)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。

## 5.4\_详细说明（Detailed Documentation）

<a id="ga742d31e7175e472f1a096ffa6a5acdc5"></a>

### `BT_MESH_MODEL_SAR_CFG_CLI`

```c
#define BT_MESH_MODEL_SAR_CFG_CLI ( _cli)
```

```c
#include <zephyr/bluetooth/mesh/sar_cfg_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_SAR_CFG_CLI,                         \
                 _bt_mesh_sar_cfg_cli_op, _cli.pub, _cli,                  \
                 &_bt_mesh_sar_cfg_cli_cb)
```

分段与重组配置客户端（SAR Configuration Client）模型的组成数据条目（composition data entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _cli` | 指向蓝牙 Mesh 分段与重组配置客户端模型（SAR Configuration Client Model）实例的指针。 |

<a id="ga444c99254ef2ccdd10dac08a94219d79"></a>

### `bt_mesh_sar_cfg_cli_receiver_get()`

```c
int bt_mesh_sar_cfg_cli_receiver_get ( uint16_t net_idx, uint16_t addr, struct bt_mesh_sar_rx * rsp )
```

```c
#include <zephyr/bluetooth/mesh/sar_cfg_cli.h>
```

获取目标节点的 SAR 接收端（SAR Receiver）状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `rsp` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga884025b2baf8559950ba6dc83e9ef486"></a>

### `bt_mesh_sar_cfg_cli_receiver_set()`

```c
int bt_mesh_sar_cfg_cli_receiver_set ( uint16_t net_idx, uint16_t addr, const struct bt_mesh_sar_rx * set, struct bt_mesh_sar_rx * rsp )
```

```c
#include <zephyr/bluetooth/mesh/sar_cfg_cli.h>
```

设置目标节点的 SAR 接收端状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `set` | 要在目标节点上设置的新 SAR 接收端（SAR Receiver）状态。 |
| `rsp` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga998846e5735676dc5f79b387d02630d4"></a>

### `bt_mesh_sar_cfg_cli_timeout_get()`

```c
int32_t bt_mesh_sar_cfg_cli_timeout_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/sar_cfg_cli.h>
```

获取当前传输超时值（transmission timeout）。

**返回（Returns）**：返回值：配置的传输超时（transmission timeout），单位为毫秒。

<a id="ga57d7c6a973b35f53689cbf8a065a538f"></a>

### `bt_mesh_sar_cfg_cli_timeout_set()`

```c
void bt_mesh_sar_cfg_cli_timeout_set ( int32_t timeout)
```

```c
#include <zephyr/bluetooth/mesh/sar_cfg_cli.h>
```

设置传输超时值（Transmission Timeout Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 新的传输超时。 |

<a id="ga893ef5861708bec12f87b9f9cc64b9fc"></a>

### `bt_mesh_sar_cfg_cli_transmitter_get()`

```c
int bt_mesh_sar_cfg_cli_transmitter_get ( uint16_t net_idx, uint16_t addr, struct bt_mesh_sar_tx * rsp )
```

```c
#include <zephyr/bluetooth/mesh/sar_cfg_cli.h>
```

获取目标节点的 SAR 发送端（SAR Transmitter）状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `rsp` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga32e2a580b24a41761911e88413e9664e"></a>

### `bt_mesh_sar_cfg_cli_transmitter_set()`

```c
int bt_mesh_sar_cfg_cli_transmitter_set ( uint16_t net_idx, uint16_t addr, const struct bt_mesh_sar_tx * set, struct bt_mesh_sar_tx * rsp )
```

```c
#include <zephyr/bluetooth/mesh/sar_cfg_cli.h>
```

设置目标节点的 SAR 发送端状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点地址（Target node address）。 |
| `set` | 要在目标节点上设置的新 SAR 发送端（SAR Transmitter）状态。 |
| `rsp` | 状态响应参数（status response parameter）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。


## 5.5\_原页交叉引用（Cross References）

- [bt_mesh_sar_cfg_cli](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)
- [bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/bluetooth/mesh/sar_cfg_cli.h](../api_file_management_reference/P042_zephyr__bluetooth__mesh__sar_cfg_cli.h_文件参考.md)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_SAR_CFG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gaf214eb7eef3530919432b62ff9b353c3)
- [蓝牙 Mesh 分段与重组配置客户端模型（SAR Configuration Client Model）](P005_蓝牙 Mesh 分段与重组配置客户端模型（SAR Configuration Client Model）.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gaf214eb7eef3530919432b62ff9b353c3"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_即时警报服务（Immediate Alert Service，IAS）.md) · [返回大纲](大纲.md) · [下一章](P006_蓝牙 Mesh 请求 PDU 重放保护列表客户端（Solicitation PDU RPL Client）.md)
