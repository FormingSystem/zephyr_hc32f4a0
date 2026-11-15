---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-2
title: GOEP 的 RFCOMM 传输
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__rfcomm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_GOEP 的 RFCOMM 传输

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__rfcomm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fgoep_5Ftransport_5Frfcomm_5Fserver"></a>

```c
struct bt_goep_transport_rfcomm_server
```

相关声明：[bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)。

GOEP v1.1 的服务器结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_ga781dc33ffa086753319c84f59b8e977f"></a>

```c
int bt_goep_transport_rfcomm_server_register (struct bt_goep_transport_rfcomm_server *server)
```

相关声明：[bt_goep_transport_rfcomm_server_register](#ga781dc33ffa086753319c84f59b8e977f)、[bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)。

注册 GOEP RFCOMM 服务器。

<a id="r_ga924d103e3556e274a4cb7ba16d0589c7"></a>

```c
int bt_goep_transport_rfcomm_connect (struct bt_conn *conn, struct bt_goep *goep, uint8_t channel)
```

相关声明：[bt_goep_transport_rfcomm_connect](#ga924d103e3556e274a4cb7ba16d0589c7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过串行端口仿真协议（RFCOMM）连接 GOEP 传输。

<a id="r_ga22f4502e4eb56dab71ca478dee474e55"></a>

```c
int bt_goep_transport_rfcomm_disconnect (struct bt_goep *goep)
```

相关声明：[bt_goep_transport_rfcomm_disconnect](#ga22f4502e4eb56dab71ca478dee474e55)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)。

断开 GOEP RFCOMM 传输。

## 2.3\_详细说明（Detailed Documentation）

<a id="ga924d103e3556e274a4cb7ba16d0589c7"></a>

### `bt_goep_transport_rfcomm_connect()`

```c
int bt_goep_transport_rfcomm_connect ( struct bt_conn * conn, struct bt_goep * goep, uint8_t channel )
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

通过串行端口仿真协议（RFCOMM）连接 GOEP 传输。

通过 RFCOMM 连接 GOEP 传输。连接完成后调用 `bt_goep_transport_ops::connected` 回调；若连接被拒绝，则调用 `bt_goep_transport_ops::disconnected` 回调。第二个参数为 GOEP 对象的地址：应用程序应创建专用于此传输的通用对象交换配置文件（Generic Object Exchange Profile，GOEP）对象，然后将其位置（地址）传给本 API。调用前必须将 `bt_goep::transport_ops` 初始化为有效的 `bt_goep_transport_ops` 对象地址。第三个参数为 RFCOMM 信道，即从对端设备发现的 RFCOMM 服务器信道。

忽略 `bt_obex::rx` 的 `mtu` 字段值，改用依据 `CONFIG_BT_GOEP_RFCOMM_MTU` 计算出的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `goep` | 通用对象交换配置文件（Generic Object Exchange Profile，GOEP）对象。 |
| `channel` | 要连接的 RFCOMM 信道（Channel）。 |

**警告（Warning）**：警告（Warning）：调用者负责将通用对象交换规范对象（GOEP object）的父对象清零。

**说明（Note）**：注意（Note）：接受回调（Accept callback）必须按以下方式初始化返回的 GOEP 实例：将 `bt_goep::transport_ops` 设置为有效的操作表；通过 `bt_goep::v1` 提供所指向的 `bt_goep_transport_v1` 实例，该实例在传输连接整个生命周期内必须有效且地址稳定，同时将 `bt_goep::v2` 设为 `NULL`；将版本专用对象的反向指针 `bt_goep_transport_v1::goep` 初始化为指向父通用对象交换规范对象（GOEP）。版本专用对象必须在整个传输生命周期内保持有效。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga22f4502e4eb56dab71ca478dee474e55"></a>

### `bt_goep_transport_rfcomm_disconnect()`

```c
int bt_goep_transport_rfcomm_disconnect ( struct bt_goep * goep)
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

断开 GOEP RFCOMM 传输。

断开 GOEP RFCOMM 传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `goep` | 通用对象交换配置文件（Generic Object Exchange Profile，GOEP）对象。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga781dc33ffa086753319c84f59b8e977f"></a>

### `bt_goep_transport_rfcomm_server_register()`

```c
int bt_goep_transport_rfcomm_server_register ( struct bt_goep_transport_rfcomm_server * server)
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

注册 GOEP RFCOMM 服务器。

为 RFCOMM 信道 `bt_rfcomm_server::channel` 注册 GOEP 服务器。每个新连接均由 `bt_goep_transport_rfcomm_server::accept` 回调授权；授权成功时，该回调必须分配供新 GOEP 连接使用的通用对象交换配置文件（Generic Object Exchange Profile，GOEP）结构体。

可将 `bt_rfcomm_server::channel` 预设为指定值，但不推荐这样做。也可将其保留为 0，由 RFCOMM 自动分配信道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 服务器结构体（Server Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 2.4\_原页交叉引用（Cross References）

- [bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)
- [bt_goep_transport_ops::connected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a46068be01ea341e1b74163bea0003e2e)
- [bt_goep_transport_ops::disconnected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a5f8ce2be1a4c87f4e36d47dcc3aa6f3c)
- [通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)
- [bt_goep::transport_ops](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#abca52709a4b2535eccecb632a1a6f29d)
- [bt_goep_transport_ops](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md)
- [bt_obex::rx](../bluetooth_service_model_reference/P127_bt_obex_结构体.md#ac2bc4ebc3b440c1be71c033b7c051c98)
- [CONFIG_BT_GOEP_RFCOMM_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GOEP_RFCOMM_MTU)
- [bt_goep::v1](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a9820cd834fb77847110b0c0f490b637e)
- [bt_goep_transport_v1](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md)
- [bt_goep::v2](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a6d341f018f6e7dc9187eab11cea9bc53)
- [bt_goep_transport_v1::goep](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md#a82ed6f11432432f051c705bddfd7a53b)
- [bt_rfcomm_server::channel](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md#a30b22ea64c0fdd7130e8aaa79519e776)
- [bt_goep_transport_rfcomm_server::accept](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md#a66c433a47c20018f9f0a018b4fbc8048)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_GOEP 的 L2CAP 传输.md) · [返回大纲](大纲.md) · [下一章](P003_蓝牙 HCI 驱动后端 API.md)
