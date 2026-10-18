---
id: learning.zephyr-docs.api-file-service-interface-reference.page-21
title: zephyr__bluetooth__classic__goep.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_bluetooth\_\_classic\_\_goep.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/goep_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <string.h>
#include <errno.h>
#include <stdbool.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/l2cap.h>
#include <zephyr/bluetooth/classic/rfcomm.h>
#include <zephyr/bluetooth/classic/obex.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_bt_5Fgoep_5Ftransport_5Fops"></a>

```c
struct bt_goep_transport_ops
```

相关声明：[bt_goep_transport_ops](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md)。

GOEP 传输操作（Transport Operations）结构体。

<a id="r_bt_5Fgoep_5Ftransport_5Fv1"></a>

```c
struct bt_goep_transport_v1
```

相关声明：[bt_goep_transport_v1](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md)。

通用对象交换配置文件（GOEP）v1.1结构。

<a id="r_bt_5Fgoep_5Ftransport_5Fv2"></a>

```c
struct bt_goep_transport_v2
```

相关声明：[bt_goep_transport_v2](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md)。

通用对象交换配置文件（GOEP）v2结构。

<a id="r_bt_5Fgoep_5Ftransport"></a>

```c
struct bt_goep_transport
```

相关声明：[bt_goep_transport](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md)。

GOEP 传输统一结构体（Transport Unified Structure）。

<a id="r_bt_5Fgoep"></a>

```c
struct bt_goep
```

相关声明：[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)。

通用对象交换配置文件（Generic Object Exchange Profile，GOEP）结构体。

<a id="r_bt_5Fgoep_5Ftransport_5Frfcomm_5Fserver"></a>

```c
struct bt_goep_transport_rfcomm_server
```

相关声明：[bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)。

GOEP v1.1 的服务器结构体。

<a id="r_bt_5Fgoep_5Ftransport_5Fl2cap_5Fserver"></a>

```c
struct bt_goep_transport_l2cap_server
```

相关声明：[bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)。

GOEP v2.0 及更高版本的服务器结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="r_ga45d8102d365c1246e3bca097a2f5e39e"></a>

```c
#define BT_GOEP_INIT_V1(_goep, _v1)
```

相关声明：[BT_GOEP_INIT_V1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#ga45d8102d365c1246e3bca097a2f5e39e)。

初始化通用对象交换配置文件（GOEP）及 GOEP v1（RFCOMM）传输结构体。

<a id="r_gade38e613cc7a4c2c43c16e2ac9fc7335"></a>

```c
#define BT_GOEP_INIT_V2(_goep, _v2)
```

相关声明：[BT_GOEP_INIT_V2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gade38e613cc7a4c2c43c16e2ac9fc7335)。

初始化通用对象交换配置文件（GOEP）及 GOEP v2（L2CAP）传输结构体。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 21.3\_枚举（Enumerations）

<a id="r_ga75294425d3da6d10ec5e591508be211c"></a>

```c
enum bt_goep_transport_state { BT_GOEP_TRANSPORT_DISCONNECTED , BT_GOEP_TRANSPORT_CONNECTING , BT_GOEP_TRANSPORT_CONNECTED , BT_GOEP_TRANSPORT_DISCONNECTING }
```

相关声明：[bt_goep_transport_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#ga75294425d3da6d10ec5e591508be211c)、[BT_GOEP_TRANSPORT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211cab221e071b255925006edba23221dd060)、[BT_GOEP_TRANSPORT_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211ca10d39d8b2b808a47998b05baeaf03cfe)、[BT_GOEP_TRANSPORT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211cabe00a5c73a264c014b7e25983aed9a43)、[BT_GOEP_TRANSPORT_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211ca8f060690ba88c7e944d2f4a0e6a7db79)。

GOEP 传输的生命周期状态（Life-span States）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.4\_函数（Functions）

<a id="r_ga781dc33ffa086753319c84f59b8e977f"></a>

```c
int bt_goep_transport_rfcomm_server_register (struct bt_goep_transport_rfcomm_server *server)
```

相关声明：[bt_goep_transport_rfcomm_server_register](../api_vector_pipeline_topic_reference/P002_GOEP 的 RFCOMM 传输.md#ga781dc33ffa086753319c84f59b8e977f)、[bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)。

注册 GOEP RFCOMM 服务器。

<a id="r_ga924d103e3556e274a4cb7ba16d0589c7"></a>

```c
int bt_goep_transport_rfcomm_connect (struct bt_conn *conn, struct bt_goep *goep, uint8_t channel)
```

相关声明：[bt_goep_transport_rfcomm_connect](../api_vector_pipeline_topic_reference/P002_GOEP 的 RFCOMM 传输.md#ga924d103e3556e274a4cb7ba16d0589c7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过串行端口仿真协议（RFCOMM）连接 GOEP 传输。

<a id="r_ga22f4502e4eb56dab71ca478dee474e55"></a>

```c
int bt_goep_transport_rfcomm_disconnect (struct bt_goep *goep)
```

相关声明：[bt_goep_transport_rfcomm_disconnect](../api_vector_pipeline_topic_reference/P002_GOEP 的 RFCOMM 传输.md#ga22f4502e4eb56dab71ca478dee474e55)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)。

断开 GOEP RFCOMM 传输。

<a id="r_ga5f7a699eb8c857c6b6b99c506953f176"></a>

```c
int bt_goep_transport_l2cap_server_register (struct bt_goep_transport_l2cap_server *server)
```

相关声明：[bt_goep_transport_l2cap_server_register](../api_vector_pipeline_topic_reference/P001_GOEP 的 L2CAP 传输.md#ga5f7a699eb8c857c6b6b99c506953f176)、[bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)。

注册 GOEP L2CAP 服务器。

<a id="r_ga4730911b9e0ddb5c66575d0529128aee"></a>

```c
int bt_goep_transport_l2cap_connect (struct bt_conn *conn, struct bt_goep *goep, uint16_t psm)
```

相关声明：[bt_goep_transport_l2cap_connect](../api_vector_pipeline_topic_reference/P001_GOEP 的 L2CAP 传输.md#ga4730911b9e0ddb5c66575d0529128aee)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过逻辑链路控制与适配协议（L2CAP）连接 GOEP 传输。

<a id="r_ga48b039f1f5fa1a8c15449a061396c668"></a>

```c
int bt_goep_transport_l2cap_disconnect (struct bt_goep *goep)
```

相关声明：[bt_goep_transport_l2cap_disconnect](../api_vector_pipeline_topic_reference/P001_GOEP 的 L2CAP 传输.md#ga48b039f1f5fa1a8c15449a061396c668)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)。

从 L2CAP 信道断开 GOEP 传输。

<a id="r_ga7d751335e777b84a319626e50f43ffe9"></a>

```c
struct net_buf * bt_goep_create_pdu (struct bt_goep *goep, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_goep_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#ga7d751335e777b84a319626e50f43ffe9)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

在为 GOEP 预留头部空间（Head Room）后，从指定池分配缓冲区。


## 21.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/l2cap.h](../api_source_system_reference/P016_l2cap.h_源码浏览.md)
- [zephyr/bluetooth/classic/rfcomm.h](../api_source_runtime_reference/P053_rfcomm.h_源码浏览.md)
- [zephyr/bluetooth/classic/obex.h](../api_source_configuration_reference/P062_obex.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P081_goep.h_源码浏览.md)
- [bt_goep_transport_ops](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md)
- [bt_goep_transport_v1](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md)
- [bt_goep_transport_v2](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md)
- [bt_goep_transport](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md)
- [bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)
- [bt_goep_transport_rfcomm_server](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md)
- [bt_goep_transport_l2cap_server](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md)
- [BT_GOEP_INIT_V1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#ga45d8102d365c1246e3bca097a2f5e39e)
- [BT_GOEP_INIT_V2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gade38e613cc7a4c2c43c16e2ac9fc7335)
- [bt_goep_transport_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#ga75294425d3da6d10ec5e591508be211c)
- [BT_GOEP_TRANSPORT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211cab221e071b255925006edba23221dd060)
- [BT_GOEP_TRANSPORT_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211ca10d39d8b2b808a47998b05baeaf03cfe)
- [BT_GOEP_TRANSPORT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211cabe00a5c73a264c014b7e25983aed9a43)
- [BT_GOEP_TRANSPORT_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#gga75294425d3da6d10ec5e591508be211ca8f060690ba88c7e944d2f4a0e6a7db79)
- [bt_goep_transport_rfcomm_server_register](../api_vector_pipeline_topic_reference/P002_GOEP 的 RFCOMM 传输.md#ga781dc33ffa086753319c84f59b8e977f)
- [bt_goep_transport_rfcomm_connect](../api_vector_pipeline_topic_reference/P002_GOEP 的 RFCOMM 传输.md#ga924d103e3556e274a4cb7ba16d0589c7)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_goep_transport_rfcomm_disconnect](../api_vector_pipeline_topic_reference/P002_GOEP 的 RFCOMM 传输.md#ga22f4502e4eb56dab71ca478dee474e55)
- [bt_goep_transport_l2cap_server_register](../api_vector_pipeline_topic_reference/P001_GOEP 的 L2CAP 传输.md#ga5f7a699eb8c857c6b6b99c506953f176)
- [bt_goep_transport_l2cap_connect](../api_vector_pipeline_topic_reference/P001_GOEP 的 L2CAP 传输.md#ga4730911b9e0ddb5c66575d0529128aee)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_goep_transport_l2cap_disconnect](../api_vector_pipeline_topic_reference/P001_GOEP 的 L2CAP 传输.md#ga48b039f1f5fa1a8c15449a061396c668)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_goep_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html#ga7d751335e777b84a319626e50f43ffe9)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)

---

[上一章](P020_zephyr__authentication__fido2__fido2.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__drivers__gpio__gpio_bl61x_wo.h_文件参考.md)
