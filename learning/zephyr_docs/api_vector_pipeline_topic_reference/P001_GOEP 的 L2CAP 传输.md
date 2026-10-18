---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-1
title: GOEP 的 L2CAP 传输
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__l2cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_GOEP 的 L2CAP 传输

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep__transport__l2cap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fgoep_5Ftransport_5Fl2cap_5Fserver"></a>

```c
struct bt_goep_transport_l2cap_server
```

相关声明：[bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)。

GOEP v2.0 及更高版本的服务器结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.2\_函数（Functions）

<a id="r_ga5f7a699eb8c857c6b6b99c506953f176"></a>

```c
int bt_goep_transport_l2cap_server_register (struct bt_goep_transport_l2cap_server *server)
```

相关声明：[bt_goep_transport_l2cap_server_register](#ga5f7a699eb8c857c6b6b99c506953f176)、[bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)。

注册 GOEP L2CAP 服务器。

<a id="r_ga4730911b9e0ddb5c66575d0529128aee"></a>

```c
int bt_goep_transport_l2cap_connect (struct bt_conn *conn, struct bt_goep *goep, uint16_t psm)
```

相关声明：[bt_goep_transport_l2cap_connect](#ga4730911b9e0ddb5c66575d0529128aee)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过逻辑链路控制与适配协议（L2CAP）连接 GOEP 传输。

<a id="r_ga48b039f1f5fa1a8c15449a061396c668"></a>

```c
int bt_goep_transport_l2cap_disconnect (struct bt_goep *goep)
```

相关声明：[bt_goep_transport_l2cap_disconnect](#ga48b039f1f5fa1a8c15449a061396c668)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)。

从 L2CAP 信道断开 GOEP 传输。

## 1.3\_详细说明（Detailed Documentation）

<a id="ga4730911b9e0ddb5c66575d0529128aee"></a>

### `bt_goep_transport_l2cap_connect()`

```c
int bt_goep_transport_l2cap_connect ( struct bt_conn * conn, struct bt_goep * goep, uint16_t psm )
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

通过逻辑链路控制与适配协议（L2CAP）连接 GOEP 传输。

通过 L2CAP 连接 GOEP 传输。连接完成后调用 `bt_goep_transport_ops::connected` 回调；若连接被拒绝，则调用 `bt_goep_transport_ops::disconnected` 回调。第二个参数为 GOEP 对象的地址：应用程序应创建专用于此传输的通用对象交换配置文件（Generic Object Exchange Profile，GOEP）对象，然后将其位置（地址）传给本 API。调用前必须将 `bt_goep::transport_ops` 初始化为有效的 `bt_goep_transport_ops` 对象地址。第三个参数为 L2CAP 协议／服务多路复用器（PSM）值，即从对端设备发现的 OBEX SDP 记录中的 L2CAP PSM。

忽略 `bt_obex::rx` 的 `mtu` 字段值，改用依据 `CONFIG_BT_GOEP_L2CAP_MTU` 计算出的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `goep` | 通用对象交换配置文件（Generic Object Exchange Profile，GOEP）对象。 |
| `psm` | 要连接的 L2CAP 协议／服务多路复用器（PSM）值。 |

**警告（Warning）**：警告（Warning）：调用者负责将通用对象交换规范对象（GOEP object）的父对象清零。

**说明（Note）**：注意（Note）：接受回调（Accept callback）必须按以下方式初始化返回的 GOEP 实例：将 `bt_goep::transport_ops` 设置为有效的操作表；通过 `bt_goep::v2` 提供所指向的 `bt_goep_transport_v2` 实例，该实例在传输连接整个生命周期内必须有效且地址稳定，同时将 `bt_goep::v1` 设为 `NULL`；将版本专用对象的反向指针 `bt_goep_transport_v2::goep` 初始化为指向父通用对象交换规范对象（GOEP）。版本专用对象必须在整个传输生命周期内保持有效。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga48b039f1f5fa1a8c15449a061396c668"></a>

### `bt_goep_transport_l2cap_disconnect()`

```c
int bt_goep_transport_l2cap_disconnect ( struct bt_goep * goep)
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

从 L2CAP 信道断开 GOEP 传输。

断开 GOEP L2CAP 传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `goep` | 通用对象交换配置文件（Generic Object Exchange Profile，GOEP）对象。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga5f7a699eb8c857c6b6b99c506953f176"></a>

### `bt_goep_transport_l2cap_server_register()`

```c
int bt_goep_transport_l2cap_server_register ( struct bt_goep_transport_l2cap_server * server)
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

注册 GOEP L2CAP 服务器。

为 L2CAP PSM `bt_l2cap_server::psm` 注册 GOEP 服务器。每个新连接均由 `bt_goep_transport_l2cap_server::accept` 回调授权；授权成功时，该回调必须分配供新 GOEP 连接使用的通用对象交换配置文件（Generic Object Exchange Profile，GOEP）结构体。

对于 L2CAP PSM，不应使用 SIG 分配的固定 PSM（范围为 `0x0001–0x0eff`）。对于动态 PSM（范围为 `0x1000–0xffff`），可将 `bt_l2cap_server::psm` 预设为指定值，但不推荐这样做。其最高有效八位组的最低有效位必须为 0，其余八位组的最低有效位必须为 1。也可将其保留为 0，由 L2CAP 自动分配信道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 服务器结构体（Server Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 1.4\_原页交叉引用（Cross References）

- [bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/bluetooth/classic/goep.h](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)
- [bt_goep_transport_ops::connected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a46068be01ea341e1b74163bea0003e2e)
- [bt_goep_transport_ops::disconnected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a5f8ce2be1a4c87f4e36d47dcc3aa6f3c)
- [通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)
- [bt_goep::transport_ops](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#abca52709a4b2535eccecb632a1a6f29d)
- [bt_goep_transport_ops](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md)
- [bt_obex::rx](../bluetooth_service_model_reference/P127_bt_obex_结构体.md#ac2bc4ebc3b440c1be71c033b7c051c98)
- [CONFIG_BT_GOEP_L2CAP_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GOEP_L2CAP_MTU)
- [bt_goep::v2](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a6d341f018f6e7dc9187eab11cea9bc53)
- [bt_goep_transport_v2](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md)
- [bt_goep::v1](../bluetooth_service_model_reference/P070_bt_goep_结构体.md#a9820cd834fb77847110b0c0f490b637e)
- [bt_goep_transport_v2::goep](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md#a5d3086e35bd244810e87d4bd0023e7bc)
- [bt_l2cap_server::psm](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#a07925dda8566ee7518b1809725e1b110)
- [bt_goep_transport_l2cap_server::accept](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md#a7441985cb5ce8e2f961dcd5c5175f9c8)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_GOEP 的 RFCOMM 传输.md)
