---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-4
title: bt_conn_auth_info_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__auth__info__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_bt\_conn\_auth\_info\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__auth__info__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

认证配对信息回调结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

带认证的配对信息回调结构（Authenticated pairing information callback structure）。注意（Note）：回调在线程上下文（Thread context）中执行，绝不会从中断服务程序（ISR）调用。回调是在协议栈内部上下文中调用，还是在触发它的 API 调用中同步执行，以及具体使用哪个上下文，都不是 API 契约的一部分，可能随版本变化。有关在回调中阻塞的风险及缓解方法，参见回调执行上下文（Callback execution contexts）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_aea737700f2760de1ed26a721b5e860d2"></a>

```c
void(* pairing_complete )(struct bt_conn *conn, bool bonded)
```

相关声明：[pairing_complete](#aea737700f2760de1ed26a721b5e860d2)、[bt_conn](P002_bt_conn_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

通知配对过程（Pairing procedure）已完成。

<a id="r_ae7228bb82889eacebf67e1d4b3b23375"></a>

```c
void(* pairing_failed )(struct bt_conn *conn, enum bt_security_err reason)
```

相关声明：[pairing_failed](#ae7228bb82889eacebf67e1d4b3b23375)、[bt_conn](P002_bt_conn_结构体.md)、[bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)。

通知配对过程（Pairing process）已失败。

<a id="r_af20b0d7fc5fd8399ad9368b3ef7067f8"></a>

```c
void(* bond_deleted )(uint8_t id, const bt_addr_le_t *peer)
```

相关声明：[bond_deleted](#af20b0d7fc5fd8399ad9368b3ef7067f8)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

通知绑定（Bond）已删除。

<a id="r_a44896258f0221d4f0a55cc1fb785b06c"></a>

```c
void(* addr_res_support_read )(struct bt_conn *conn, enum bt_le_addr_res_support support)
```

相关声明：[addr_res_support_read](#a44896258f0221d4f0a55cc1fb785b06c)、[bt_conn](P002_bt_conn_结构体.md)、[bt_le_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad0039d4b524a0eef31158dc9b24a497)。

已读取对等设备对地址解析（Address resolution）的支持情况。

<a id="r_afcb8dae77f7b4df3ed0741de65f7f5d0"></a>

```c
void(* br_bond_deleted )(const bt_addr_t *peer)
```

相关声明：[br_bond_deleted](#afcb8dae77f7b4df3ed0741de65f7f5d0)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

通知经典蓝牙绑定（Classic bond）已删除。

<a id="r_afde62f2cdfb40b4154208f3c1c3dadc1"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#afde62f2cdfb40b4154208f3c1c3dadc1)。

用于链表处理（List handling）的内部字段。

## 4.2\_详细说明（Detailed Documentation）

<a id="a44896258f0221d4f0a55cc1fb785b06c"></a>

### `addr_res_support_read`

```c
void(* bt_conn_auth_info_cb::addr_res_support_read) (struct bt_conn *conn, enum bt_le_addr_res_support support)
```

已读取对等设备对地址解析（Address resolution）的支持情况。

此回调通知应用，已完成自动读取已绑定对等设备的中心设备地址解析特征（Central Address Resolution characteristic）。该自动读取功能由 `CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES` 启用。也可以通过 `bt_le_bond_addr_res_support()` 获取结果；如果读取失败，支持情况仍为未知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 读取此特征（Characteristic）所使用的连接。 |
| `support` | 对等设备对地址解析（Address resolution）的支持情况。 |

<a id="af20b0d7fc5fd8399ad9368b3ef7067f8"></a>

### `bond_deleted`

```c
void(* bt_conn_auth_info_cb::bond_deleted) (uint8_t id, const bt_addr_le_t *peer)
```

通知绑定（Bond）已删除。

此回调通知应用，远端对等设备（Remote peer）的绑定信息（Bond information）已删除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 拥有该绑定（Bond）的本地身份（Local identity）。 |
| `peer` | 远端地址（Remote address）。 |

<a id="afcb8dae77f7b4df3ed0741de65f7f5d0"></a>

### `br_bond_deleted`

```c
void(* bt_conn_auth_info_cb::br_bond_deleted) (const bt_addr_t *peer)
```

通知经典蓝牙绑定（Classic bond）已删除。

此回调通知应用，远端对等设备（Remote peer）的经典蓝牙绑定信息（Classic bond information）已删除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `peer` | 远端地址（Remote address）。 |

<a id="afde62f2cdfb40b4154208f3c1c3dadc1"></a>

### `node`

```c
sys_snode_t bt_conn_auth_info_cb::node
```

用于链表处理（List handling）的内部字段。

<a id="aea737700f2760de1ed26a721b5e860d2"></a>

### `pairing_complete`

```c
void(* bt_conn_auth_info_cb::pairing_complete) (struct bt_conn *conn, bool bonded)
```

通知配对过程（Pairing procedure）已完成。

此回调通知应用，配对过程（Pairing procedure）已完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `bonded` | 配对过程中已分发绑定信息（Bond information）。 |

<a id="ae7228bb82889eacebf67e1d4b3b23375"></a>

### `pairing_failed`

```c
void(* bt_conn_auth_info_cb::pairing_failed) (struct bt_conn *conn, enum bt_security_err reason)
```

通知配对过程（Pairing process）已失败。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `reason` | 配对失败原因（Pairing failure reason）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_conn](P002_bt_conn_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_le_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad0039d4b524a0eef31158dc9b24a497)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES)
- [bt_le_bond_addr_res_support()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5b5e51f79896d674bf6b70b2251e79d4)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_bt_conn_auth_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_bt_conn_br_cb_结构体.md)
