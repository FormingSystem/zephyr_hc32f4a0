---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-2
title: 通用对象交换规范（Generic Object Exchange Profile，GOEP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_通用对象交换规范（Generic Object Exchange Profile，GOEP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用对象交换规范（Generic Object Exchange Profile，GOEP）

<a id="details"></a>

通用对象交换规范（Generic Object Exchange Profile，GOEP）

<a id="header-groups"></a>
<a id="groups"></a>

## 2.1\_主题（Topics）

<a id="r_bt_5Fgoep_5Ftransport_5Fl2cap"></a>

相关声明：[GOEP 的 L2CAP 传输](../api_vector_pipeline_topic_reference/P001_GOEP 的 L2CAP 传输.md)。

<a id="r_bt_5Fgoep_5Ftransport_5Frfcomm"></a>

相关声明：[GOEP 的 RFCOMM 传输](../api_vector_pipeline_topic_reference/P002_GOEP 的 RFCOMM 传输.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.2\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.3\_宏定义（Macros）

<a id="r_ga45d8102d365c1246e3bca097a2f5e39e"></a>

```c
#define BT_GOEP_INIT_V1(_goep, _v1)
```

相关声明：[BT_GOEP_INIT_V1](#ga45d8102d365c1246e3bca097a2f5e39e)。

初始化通用对象交换配置文件（GOEP）及 GOEP v1（RFCOMM）传输结构体。

<a id="r_gade38e613cc7a4c2c43c16e2ac9fc7335"></a>

```c
#define BT_GOEP_INIT_V2(_goep, _v2)
```

相关声明：[BT_GOEP_INIT_V2](#gade38e613cc7a4c2c43c16e2ac9fc7335)。

初始化通用对象交换配置文件（GOEP）及 GOEP v2（L2CAP）传输结构体。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_ga75294425d3da6d10ec5e591508be211c"></a>

```c
enum bt_goep_transport_state { BT_GOEP_TRANSPORT_DISCONNECTED , BT_GOEP_TRANSPORT_CONNECTING , BT_GOEP_TRANSPORT_CONNECTED , BT_GOEP_TRANSPORT_DISCONNECTING }
```

相关声明：[bt_goep_transport_state](#ga75294425d3da6d10ec5e591508be211c)、[BT_GOEP_TRANSPORT_DISCONNECTED](#gga75294425d3da6d10ec5e591508be211cab221e071b255925006edba23221dd060)、[BT_GOEP_TRANSPORT_CONNECTING](#gga75294425d3da6d10ec5e591508be211ca10d39d8b2b808a47998b05baeaf03cfe)、[BT_GOEP_TRANSPORT_CONNECTED](#gga75294425d3da6d10ec5e591508be211cabe00a5c73a264c014b7e25983aed9a43)、[BT_GOEP_TRANSPORT_DISCONNECTING](#gga75294425d3da6d10ec5e591508be211ca8f060690ba88c7e944d2f4a0e6a7db79)。

GOEP 传输的生命周期状态（Life-span States）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_ga7d751335e777b84a319626e50f43ffe9"></a>

```c
struct net_buf * bt_goep_create_pdu (struct bt_goep *goep, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_goep_create_pdu](#ga7d751335e777b84a319626e50f43ffe9)、[bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

在为 GOEP 预留头部空间（Head Room）后，从指定池分配缓冲区。

## 2.6\_详细说明（Detailed Documentation）

<a id="ga45d8102d365c1246e3bca097a2f5e39e"></a>

### `BT_GOEP_INIT_V1`

```c
#define BT_GOEP_INIT_V1 ( _goep, _v1 )
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

展开值（Value）：

```c
do { \
        BUILD_ASSERT(SAME_TYPE(*(_goep), struct bt_goep) && \
                     SAME_TYPE(*(_v1), struct bt_goep_transport_v1), \
                     "pointer type mismatch in BT_GOEP_INIT_V1"); \
        (_v1)->goep = (_goep); \
        (_goep)->v1 = (_v1); \
        (_goep)->v2 = NULL; \
} while (0)
```

初始化通用对象交换配置文件（GOEP）及 GOEP v1（RFCOMM）传输结构体。

在通用对象交换配置文件（Generic Object Exchange Profile，GOEP）实例与其传输实例 `bt_goep_transport_v1` 之间建立相互指向的反向指针（Back-pointer），并清除未使用的 v2 指针，避免 GOEP 版本不匹配。

等价于（Equivalent to）：

原始示例（Example）：

```c
(_v1)->goep = (_goep);
(_goep)->v1 = (_v1);
(_goep)->v2 = NULL;
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_goep` | 指向要初始化的通用对象交换配置文件（GOEP）结构体的指针。 |
| `_v1` | 指向要关联的 `bt_goep_transport_v1` 结构体的指针。 |

<a id="gade38e613cc7a4c2c43c16e2ac9fc7335"></a>

### `BT_GOEP_INIT_V2`

```c
#define BT_GOEP_INIT_V2 ( _goep, _v2 )
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

展开值（Value）：

```c
do { \
        BUILD_ASSERT(SAME_TYPE(*(_goep), struct bt_goep) && \
                     SAME_TYPE(*(_v2), struct bt_goep_transport_v2), \
                     "pointer type mismatch in BT_GOEP_INIT_V2"); \
        (_v2)->goep = (_goep); \
        (_goep)->v2 = (_v2); \
        (_goep)->v1 = NULL; \
} while (0)
```

初始化通用对象交换配置文件（GOEP）及 GOEP v2（L2CAP）传输结构体。

在通用对象交换配置文件（Generic Object Exchange Profile，GOEP）实例与其传输实例 `bt_goep_transport_v2` 之间建立相互指向的反向指针（Back-pointer），并清除未使用的 v1 指针，避免 GOEP 版本不匹配。

等价于（Equivalent to）：

原始示例（Example）：

```c
(_v2)->goep = (_goep);
(_goep)->v2 = (_v2);
(_goep)->v1 = NULL;
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_goep` | 指向要初始化的通用对象交换配置文件（GOEP）结构体的指针。 |
| `_v2` | 指向要关联的 `bt_goep_transport_v2` 结构体的指针。 |

<a id="ga75294425d3da6d10ec5e591508be211c"></a>

### `bt_goep_transport_state`

```c
enum bt_goep_transport_state
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

GOEP 传输的生命周期状态（Life-span States）。

仅供内部 API 使用，用于根据操作上下文（Operational Context）将 GOEP 设置为适当的传输状态（Transport State）。

调用 `bt_goep_transport_l2cap_connect`、`bt_goep_transport_rfcomm_connect`，或从 `bt_goep_transport_rfcomm_server::accept`、`bt_goep_transport_l2cap_server::accept` 返回时，GOEP 传输进入 `BT_GOEP_TRANSPORT_CONNECTING` 状态。

GOEP 传输离开 `BT_GOEP_TRANSPORT_CONNECTING` 并进入 `BT_GOEP_TRANSPORT_CONNECTED` 状态时，调用 `bt_goep_transport_ops::connected`。

GOEP 传输从其他状态进入 `BT_GOEP_TRANSPORT_DISCONNECTED` 时，调用 `bt_goep_transport_ops::disconnected`。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_GOEP_TRANSPORT_DISCONNECTED` | GOEP 已断开（Disconnected）。 |
| `BT_GOEP_TRANSPORT_CONNECTING` | GOEP 正在连接（Connecting）。 |
| `BT_GOEP_TRANSPORT_CONNECTED` | GOEP 已就绪，可承载上层流量（Upper Layer Traffic）。 |
| `BT_GOEP_TRANSPORT_DISCONNECTING` | GOEP 正在断开（Disconnecting）。 |

<a id="ga7d751335e777b84a319626e50f43ffe9"></a>

### `bt_goep_create_pdu()`

```c
struct net_buf * bt_goep_create_pdu ( struct bt_goep * goep, struct net_buf_pool * pool )
```

```c
#include <zephyr/bluetooth/classic/goep.h>
```

在为 GOEP 预留头部空间（Head Room）后，从指定池分配缓冲区。

通过 RFCOMM 建立 GOEP 连接时，预留头部空间（Head Room）包含 OBEX、RFCOMM、L2CAP 和 ACL 头。通过 L2CAP 建立 GOEP 连接时，预留头部空间包含 OBEX、L2CAP 和 ACL 头。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `goep` | 通用对象交换配置文件（Generic Object Exchange Profile，GOEP）对象。 |
| `pool` | 应从哪个缓冲池取得缓冲区。 |

**返回（Returns）**：**返回值（Returns）：**新缓冲区（New Buffer）。


## 2.7\_原页交叉引用（Cross References）

- [GOEP 的 L2CAP 传输](../api_vector_pipeline_topic_reference/P001_GOEP 的 L2CAP 传输.md)
- [GOEP 的 RFCOMM 传输](../api_vector_pipeline_topic_reference/P002_GOEP 的 RFCOMM 传输.md)
- [bt_goep_transport_ops](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md)
- [bt_goep_transport_v1](../bluetooth_service_model_reference/P075_bt_goep_transport_v1_结构体.md)
- [bt_goep_transport_v2](../bluetooth_service_model_reference/P076_bt_goep_transport_v2_结构体.md)
- [bt_goep_transport](../bluetooth_service_model_reference/P071_bt_goep_transport_结构体.md)
- [bt_goep](../bluetooth_service_model_reference/P070_bt_goep_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [zephyr/bluetooth/classic/goep.h](../api_file_service_interface_reference/P021_zephyr__bluetooth__classic__goep.h_文件参考.md)
- [SAME_TYPE](../util_reference/P001_通用工具公共接口.md#ga78e587047fe4af679141595363c07179)
- [通用对象交换规范（Generic Object Exchange Profile，GOEP）](P002_通用对象交换规范（Generic Object Exchange Profile，GOEP）.md)
- [bt_goep_transport_l2cap_connect](../api_vector_pipeline_topic_reference/P001_GOEP 的 L2CAP 传输.md#ga4730911b9e0ddb5c66575d0529128aee)
- [bt_goep_transport_rfcomm_connect](../api_vector_pipeline_topic_reference/P002_GOEP 的 RFCOMM 传输.md#ga924d103e3556e274a4cb7ba16d0589c7)
- [bt_goep_transport_rfcomm_server::accept](../bluetooth_service_model_reference/P074_bt_goep_transport_rfcomm_server_结构体.md#a66c433a47c20018f9f0a018b4fbc8048)
- [bt_goep_transport_l2cap_server::accept](../bluetooth_service_model_reference/P072_bt_goep_transport_l2cap_server_结构体.md#a7441985cb5ce8e2f961dcd5c5175f9c8)
- [bt_goep_transport_ops::connected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a46068be01ea341e1b74163bea0003e2e)
- [bt_goep_transport_ops::disconnected](../bluetooth_service_model_reference/P073_bt_goep_transport_ops_结构体.md#a5f8ce2be1a4c87f4e36d47dcc3aa6f3c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga78e587047fe4af679141595363c07179"></a>
<a id="astructbt__goep__transport__v1_html"></a>
<a id="astructbt__goep_html"></a>
<a id="astructbt__goep__transport__v2_html"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga75294425d3da6d10ec5e591508be211cab221e071b255925006edba23221dd060"></a>
<a id="gga75294425d3da6d10ec5e591508be211ca10d39d8b2b808a47998b05baeaf03cfe"></a>
<a id="gga75294425d3da6d10ec5e591508be211cabe00a5c73a264c014b7e25983aed9a43"></a>
<a id="gga75294425d3da6d10ec5e591508be211ca8f060690ba88c7e944d2f4a0e6a7db79"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_BSD 套接字服务 API.md) · [返回大纲](大纲.md) · [下一章](P003_蓝牙 LC3 编解码器（Bluetooth LC3 codec）.md)
