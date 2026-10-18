---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-6
title: SMP 传输（SMP transport）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_SMP 传输（SMP transport）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr SMP 传输 API

<a id="details"></a>

MCUmgr SMP 传输 API

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_smp_5Ftransport_5Fapi_5Ft"></a>

```c
struct smp_transport_api_t
```

相关声明：[smp_transport_api_t](../system_service_model_reference/P082_smp_transport_api_t_结构体.md)。

简单管理协议（SMP）传输函数的函数指针；处理函数为NULL表示不支持或尚未实现。

<a id="r_smp_5Ftransport"></a>

```c
struct smp_transport
```

相关声明：[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)。

用于发送简单管理协议（SMP）响应的传输对象。

<a id="r_smp_5Ftransport_5Fbridge"></a>

```c
struct smp_transport_bridge
```

相关声明：[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)。

桥接传输（Bridged Transport）的上下文。

<a id="r_smp_5Fclient_5Ftransport_5Fentry"></a>

```c
struct smp_client_transport_entry
```

相关声明：[smp_client_transport_entry](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md)。

简单管理协议（SMP）的客户端传输结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.2\_类型定义（Typedefs）

<a id="r_ga4da3579b031ba6a90448ad9248f52155"></a>

```c
typedef int(* smp_transport_out_fn) (struct net_buf *nb)
```

相关声明：[smp_transport_out_fn](#ga4da3579b031ba6a90448ad9248f52155)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP 传输层发送回调（Transmit Callback）。

<a id="r_ga2085e89b99428a61596d90e084d7c5e2"></a>

```c
typedef uint16_t(* smp_transport_get_mtu_fn) (const struct net_buf *nb)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_transport_get_mtu_fn](#ga2085e89b99428a61596d90e084d7c5e2)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP 传输层最大传输单元查询回调（MTU Query Callback）。

<a id="r_ga840da7e00d590459b656dcbe0dd6f6f4"></a>

```c
typedef int(* smp_transport_ud_copy_fn) (struct net_buf *dst, const struct net_buf *src)
```

相关声明：[smp_transport_ud_copy_fn](#ga840da7e00d590459b656dcbe0dd6f6f4)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP `user_data` 复制回调（Copy Callback）。

<a id="r_ga0f249aa3fed3044d9bad811e92e4135c"></a>

```c
typedef void(* smp_transport_ud_free_fn) (void *ud)
```

相关声明：[smp_transport_ud_free_fn](#ga0f249aa3fed3044d9bad811e92e4135c)。

SMP `user_data` 释放回调（Free Callback）。

<a id="r_ga77d54c0bd6afc69f73613575b671e089"></a>

```c
typedef bool(* smp_transport_query_valid_check_fn) (struct net_buf *nb, void *arg)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_transport_query_valid_check_fn](#ga77d54c0bd6afc69f73613575b671e089)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

用于检查排队数据是否仍然有效的函数（Queued Data Validation）。

<a id="r_ga095edd916780b458e8cbd701969c0640"></a>

```c
typedef void(* smp_transport_ud_req_init_fn) (struct net_buf *nb, void *priv)
```

相关声明：[smp_transport_ud_req_init_fn](#ga095edd916780b458e8cbd701969c0640)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP 请求缓冲区初始化（Init Request Buffer）。

<a id="r_ga032db1c1b6f4d4212e6dc67fbd28c115"></a>

```c
typedef bool(* smp_transport_bridge_connect_fn) (struct smp_transport_bridge *bridge, bool direction, uint32_t mode, bool same_transport, zcbor_state_t *input_data, zcbor_state_t *output_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_transport_bridge_connect_fn](#ga032db1c1b6f4d4212e6dc67fbd28c115)、[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SMP 传输桥接连接（Transport Bridge Connect）。

<a id="r_ga50fcdcef18ae4c937ced9f323715e1e1"></a>

```c
typedef void(* smp_transport_bridge_disconnect_fn) (struct smp_transport_bridge *bridge, bool direction)
```

相关声明：[smp_transport_bridge_disconnect_fn](#ga50fcdcef18ae4c937ced9f323715e1e1)、[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SMP 传输桥接断开（Transport Bridge Disconnect）。

<a id="r_gadadf97eb50e871f5942b4774c643eba2"></a>

```c
typedef int(* smp_transport_bridge_out_fn) (const struct smp_transport_bridge *bridge, struct net_buf *nb, bool direction)
```

相关声明：[smp_transport_bridge_out_fn](#gadadf97eb50e871f5942b4774c643eba2)、[smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

SMP 传输桥接输出数据（Transport Bridge Output Data）。

<a id="r_ga477587b2b514bdc74560c5ab94ff792a"></a>

```c
typedef bool(* mgmt_client_transport_cb_t) (const struct smp_client_transport_entry *transport, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mgmt_client_transport_cb_t](#ga477587b2b514bdc74560c5ab94ff792a)、[smp_client_transport_entry](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md)。

SMP 客户端传输回调（Client Transport Callback）。

<a id="r_ga4570f81d545ae51e68f5a2c3ede4f170"></a>

```c
typedef bool(* smp_transport_bridge_modes_fn) (zcbor_state_t *output_data, int *rc)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_transport_bridge_modes_fn](#ga4570f81d545ae51e68f5a2c3ede4f170)。

SMP 传输桥接详情（Transport Bridge Details）。

<a id="r_ga0d8277e9da18c896749e2392c7ea1ac7"></a>

```c
typedef bool(* smp_transport_bridge_config_details_fn) (uint32_t mode, zcbor_state_t *output_data, int *rc)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_transport_bridge_config_details_fn](#ga0d8277e9da18c896749e2392c7ea1ac7)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

SMP 传输桥接配置详情（Transport Bridge Config Details）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.3\_枚举（Enumerations）

<a id="r_ga5d886a11df0c49ca18e23e246ab2fab9"></a>

```c
enum smp_transport_type { SMP_SERIAL_TRANSPORT = 0 , SMP_RAW_SERIAL_TRANSPORT , SMP_BLUETOOTH_TRANSPORT , SMP_SHELL_TRANSPORT , SMP_UDP_IPV4_TRANSPORT , SMP_UDP_IPV6_TRANSPORT , SMP_LORAWAN_TRANSPORT , SMP_SPI_TRANSPORT , SMP_USER_DEFINED_TRANSPORT = 64 }
```

相关声明：[smp_transport_type](#ga5d886a11df0c49ca18e23e246ab2fab9)、[SMP_SERIAL_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342)、[SMP_RAW_SERIAL_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9a06953c39575f3903299011cde915ac13)、[SMP_BLUETOOTH_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe)、[SMP_SHELL_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43)、[SMP_UDP_IPV4_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f)、[SMP_UDP_IPV6_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7)、[SMP_LORAWAN_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9addcf3d287f359bad85104d2a37b4e5c8)、[SMP_SPI_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9a3de5af5fe47980cdf749abc1694d84eb)、[SMP_USER_DEFINED_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863)。

用于客户端注册（Client Registration）的 SMP 传输类型（Transport Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_gaf275034765327b52b900046d71c411ee"></a>

```c
int smp_transport_init (struct smp_transport *smpt)
```

相关声明：[smp_transport_init](#gaf275034765327b52b900046d71c411ee)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)。

初始化 Zephyr SMP 传输对象（Transport Object）。

<a id="r_ga87ccc623b5907d7d65b24ed99bd57ec5"></a>

```c
void smp_rx_remove_invalid (struct smp_transport *zst, void *arg)
```

相关声明：[smp_rx_remove_invalid](#ga87ccc623b5907d7d65b24ed99bd57ec5)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)。

移除某个 SMP 传输中已不再有效的排队请求（Queued Requests）。

<a id="r_ga662f893037193923610de1e8793fd971"></a>

```c
void smp_rx_clear (struct smp_transport *zst)
```

相关声明：[smp_rx_clear](#ga662f893037193923610de1e8793fd971)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)。

清除某个 SMP 传输中待处理的排队请求（Pending Queued Requests）。

<a id="r_gafb488cd9854b74c8e5802db3c8fe6116"></a>

```c
void smp_client_transport_register (struct smp_client_transport_entry *entry)
```

相关声明：[smp_client_transport_register](#gafb488cd9854b74c8e5802db3c8fe6116)、[smp_client_transport_entry](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md)。

为客户端注册 Zephyr SMP 传输对象（Transport Object）。

<a id="r_ga67c3481cdc81c20e0c35b4eaa185619e"></a>

```c
struct smp_transport * smp_client_transport_get (int smpt_type)
```

相关声明：[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[smp_client_transport_get](#ga67c3481cdc81c20e0c35b4eaa185619e)。

查找已注册的 SMP 传输客户端对象（Transport Client Object）。

<a id="r_gae2531ab1dba2992b8465cd49349c5116"></a>

```c
bool smp_client_transport_foreach (mgmt_client_transport_cb_t user_cb, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_client_transport_foreach](#gae2531ab1dba2992b8465cd49349c5116)、[mgmt_client_transport_cb_t](#ga477587b2b514bdc74560c5ab94ff792a)。

遍历 SMP 客户端／传输对象（Clients/Transports）。

## 6.5\_详细说明（Detailed Documentation）

<a id="ga477587b2b514bdc74560c5ab94ff792a"></a>

### `mgmt_client_transport_cb_t`

```c
typedef bool(* mgmt_client_transport_cb_t) (const struct smp_client_transport_entry *transport, void *user_data)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP 客户端传输回调（Client Transport Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 简单管理协议客户端传输（SMP Client Transport）。 |
| `user_data` | 提供给 `smp_client_transport_foreach()` 函数的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：`true` 表示继续下一个传输（Transport），`false` 表示中止。

<a id="ga0d8277e9da18c896749e2392c7ea1ac7"></a>

### `smp_transport_bridge_config_details_fn`

```c
typedef bool(* smp_transport_bridge_config_details_fn) (uint32_t mode, zcbor_state_t *output_data, int *rc)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP 传输桥接配置详情（Transport Bridge Config Details）。

用于了解某种传输（Transport）建立连接时有哪些配置选项（Configuration Options）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mode` | 传输模式（Transport Mode）。 |
| `output_data` | 用于输出的 CBOR 数据。 |
| `rc` | 发生错误时要返回的 `mcumgr_err_t` 错误码。 |

**返回（Returns）**：返回值（Returns）：成功时为 `true`，失败时为 `false`。

<a id="ga032db1c1b6f4d4212e6dc67fbd28c115"></a>

### `smp_transport_bridge_connect_fn`

```c
typedef bool(* smp_transport_bridge_connect_fn) (struct smp_transport_bridge *bridge, bool direction, uint32_t mode, bool same_transport, zcbor_state_t *input_data, zcbor_state_t *output_data)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP 传输桥接连接（Transport Bridge Connect）。

与另一种传输（Transport）建立桥接（Bridge）时使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bridge` | 包含桥接上下文（Bridging Context）。 |
| `direction` | 指定传输方向（Transport Direction），为 `TRANSPORT_MGMT_DIRECTION_INCOMING` 或 `TRANSPORT_MGMT_DIRECTION_OUTGOING`。 |
| `mode` | 传输模式（Transport Mode）。 |
| `same_transport` | 传入和传出传输（Incoming/Outgoing Transport）都使用此传输时为 `true`。 |
| `input_data` | 来自输入的 CBOR 数据。 |
| `output_data` | 用于输出的 CBOR 数据，用于返回错误。 |

**返回（Returns）**：返回值（Returns）：成功时为 `true`，出错时为 `false`。

<a id="ga50fcdcef18ae4c937ced9f323715e1e1"></a>

### `smp_transport_bridge_disconnect_fn`

```c
typedef void(* smp_transport_bridge_disconnect_fn) (struct smp_transport_bridge *bridge, bool direction)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP 传输桥接断开（Transport Bridge Disconnect）。

断开与另一种传输（Transport）之间已建立的桥接（Bridge）时使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bridge` | 包含桥接上下文（Bridging Context）。 |
| `direction` | 指定传输方向（Transport Direction），为 `TRANSPORT_MGMT_DIRECTION_INCOMING` 或 `TRANSPORT_MGMT_DIRECTION_OUTGOING`。 |

<a id="ga4570f81d545ae51e68f5a2c3ede4f170"></a>

### `smp_transport_bridge_modes_fn`

```c
typedef bool(* smp_transport_bridge_modes_fn) (zcbor_state_t *output_data, int *rc)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP 传输桥接详情（Transport Bridge Details）。

用于获取传输模式数量（Number of Transport Modes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `output_data` | 用于输出的 CBOR 数据。 |
| `rc` | 发生错误时要返回的 `mcumgr_err_t` 错误码。 |

**返回（Returns）**：返回值（Returns）：成功时为 `true`，失败时为 `false`。

<a id="gadadf97eb50e871f5942b4774c643eba2"></a>

### `smp_transport_bridge_out_fn`

```c
typedef int(* smp_transport_bridge_out_fn) (const struct smp_transport_bridge *bridge, struct net_buf *nb, bool direction)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP 传输桥接输出数据（Transport Bridge Output Data）。

通过传输桥接（Transport Bridge）传递待输出数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bridge` | 包含桥接上下文（Bridging Context）。 |
| `nb` | 应输出的数据（Output Data）。 |
| `direction` | 指定传输方向（Transport Direction），为 `TRANSPORT_MGMT_DIRECTION_INCOMING` 或 `TRANSPORT_MGMT_DIRECTION_OUTGOING`。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 `mcumgr_err_t` 错误码。

<a id="ga2085e89b99428a61596d90e084d7c5e2"></a>

### `smp_transport_get_mtu_fn`

```c
typedef uint16_t(* smp_transport_get_mtu_fn) (const struct net_buf *nb)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP 传输层最大传输单元查询回调（MTU Query Callback）。

传入的 `net_buf` 应包含从相关对端（Peer）收到的请求，该对端正是要查询最大传输单元（MTU）的对端。本函数接收 `net_buf` 参数，是因为某些传输在 `net_buf` 用户头部（User Header）中保存连接特定信息，例如蓝牙传输保存对端地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb` | 包含来自相关对端（Peer）的请求。 |

**已弃用（Deprecated）**：已弃用（Deprecated）：SMP 层不调用本函数。传输（Transport）在自身的 `smp_transport_out_fn` 中对传出数据包进行分片（Fragmentation）。

**返回（Returns）**：返回值（Returns）：传输的最大传输单元（MTU）；当前无法发送时为 0。

<a id="ga4da3579b031ba6a90448ad9248f52155"></a>

### `smp_transport_out_fn`

```c
typedef int(* smp_transport_out_fn) (struct net_buf *nb)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP 传输层发送回调（Transmit Callback）。

传入的 `net_buf` 保存一个完整的 SMP 数据包，最大为 `CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE` 字节。如果数据包无法放入底层链路的单个帧（Frame），传输（Transport）负责对其分片（Fragmentation）。同样，在接收时，传输必须仅向 SMP 层提交完整的 SMP 数据包；通用重组辅助机制（Reassembly Helper）参见 `CONFIG_MCUMGR_TRANSPORT_REASSEMBLY`。

无论返回码为何，传入的 `net_buf` 都会被消费（Consumed）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb` | 要发送的 `net_buf`。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 `mcumgr_err_t` 错误码。

<a id="ga77d54c0bd6afc69f73613575b671e089"></a>

### `smp_transport_query_valid_check_fn`

```c
typedef bool(* smp_transport_query_valid_check_fn) (struct net_buf *nb, void *arg)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

用于检查排队数据是否仍然有效的函数（Queued Data Validation）。

本函数用于检查排队的 SMP 数据是否仍有效，例如远端设备断开连接时。调用 `smp_rx_remove_invalid()` 会触发此检查。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb` | 包含排队请求（Queued Request）的网络缓冲区（Net Buf）。 |
| `arg` | 调用 `smp_rx_remove_invalid()` 函数时提供的参数。 |

**返回（Returns）**：返回值（Returns）：数据已失效或应释放时为 `false`，否则为 `true`。

<a id="ga840da7e00d590459b656dcbe0dd6f6f4"></a>

### `smp_transport_ud_copy_fn`

```c
typedef int(* smp_transport_ud_copy_fn) (struct net_buf *dst, const struct net_buf *src)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP `user_data` 复制回调（Copy Callback）。

传入的源 `net_buf` 应包含无法用普通 `memcpy` 复制的 `user_data`。例如，蓝牙传输的 `net_buf user_data` 保存连接引用（Connection Reference）；另一个缓冲区将使用该引用时，必须增加引用计数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | 源缓冲区的 `user_data` 指针。 |
| `src` | 目标缓冲区的 `user_data` 指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 `mcumgr_err_t` 错误码。

<a id="ga0f249aa3fed3044d9bad811e92e4135c"></a>

### `smp_transport_ud_free_fn`

```c
typedef void(* smp_transport_ud_free_fn) (void *ud)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP `user_data` 释放回调（Free Callback）。

本函数释放 `net_buf` 用户数据（User Data），因为某些传输在其中保存连接特定信息。例如，蓝牙传输保存连接引用（Connection Reference），释放时必须减少其引用计数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ud` | 包含待释放的 `user_data` 指针。 |

<a id="ga095edd916780b458e8cbd701969c0640"></a>

### `smp_transport_ud_req_init_fn`

```c
typedef void(* smp_transport_ud_req_init_fn) (struct net_buf *nb, void *priv)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

SMP 请求缓冲区初始化（Init Request Buffer）。

传入的 `net_buf` 应用于 SMP 请求（SMP Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb` | 用于 SMP 请求（SMP Request）的网络缓冲区（Net Buf）。 |
| `priv` | SMP 传输私有数据（Transport Private Data）。 |

<a id="ga5d886a11df0c49ca18e23e246ab2fab9"></a>

### `smp_transport_type`

```c
enum smp_transport_type
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

用于客户端注册（Client Registration）的 SMP 传输类型（Transport Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SMP_SERIAL_TRANSPORT` | SMP 串行传输（Serial）。 |
| `SMP_RAW_SERIAL_TRANSPORT` | SMP 原始串行传输（Raw Serial），不使用控制台承载 SMP（SMP over Console）。 |
| `SMP_BLUETOOTH_TRANSPORT` | SMP 蓝牙传输（Bluetooth）。 |
| `SMP_SHELL_TRANSPORT` | SMP Shell 传输。 |
| `SMP_UDP_IPV4_TRANSPORT` | SMP UDP IPv4 传输。 |
| `SMP_UDP_IPV6_TRANSPORT` | SMP UDP IPv6 传输。 |
| `SMP_LORAWAN_TRANSPORT` | SMP LoRaWAN 传输。 |
| `SMP_SPI_TRANSPORT` | SMP SPI 传输。 |
| `SMP_USER_DEFINED_TRANSPORT` | 截至 63 的标识符（ID）保留给未来代码树内置的传输（In-tree Transport）。此处为 SMP 用户定义类型（User-defined Type）。 |

<a id="gae2531ab1dba2992b8465cd49349c5116"></a>

### `smp_client_transport_foreach()`

```c
bool smp_client_transport_foreach ( mgmt_client_transport_cb_t user_cb, void * user_data )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

遍历 SMP 客户端／传输对象（Clients/Transports）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `user_cb` | 回调函数（Callback function）。 |
| `user_data` | 提供给回调函数（Callback Function）的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：已遍历全部传输（Transport）时为 `true`，否则为 `false`。

<a id="ga67c3481cdc81c20e0c35b4eaa185619e"></a>

### `smp_client_transport_get()`

```c
struct smp_transport * smp_client_transport_get ( int smpt_type)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

查找已注册的 SMP 传输客户端对象（Transport Client Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `smpt_type` | 传输类型（Transport Type）。 |

**返回（Returns）**：返回值（Returns）：指向已注册对象（Registered Object）的指针；未知类型返回 `NULL`。

<a id="gafb488cd9854b74c8e5802db3c8fe6116"></a>

### `smp_client_transport_register()`

```c
void smp_client_transport_register ( struct smp_client_transport_entry * entry)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

为客户端注册 Zephyr SMP 传输对象（Transport Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `entry` | 要构造的传输（Transport）。 |

<a id="ga662f893037193923610de1e8793fd971"></a>

### `smp_rx_clear()`

```c
void smp_rx_clear ( struct smp_transport * zst)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

清除某个 SMP 传输中待处理的排队请求（Pending Queued Requests）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `zst` | 要使用的传输（Transport）。 |

<a id="ga87ccc623b5907d7d65b24ed99bd57ec5"></a>

### `smp_rx_remove_invalid()`

```c
void smp_rx_remove_invalid ( struct smp_transport * zst, void * arg )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

移除某个 SMP 传输中已不再有效的排队请求（Queued Requests）。

必须注册 `smp_transport_query_valid_check_fn()` 函数才能工作。如果该函数在回调期间返回 `false`，则被查询命令（Queried Command）会被判为无效并丢弃。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `zst` | 要使用的传输（Transport）。 |
| `arg` | 提供给回调函数 `smp_transport_query_valid_check_fn()` 的参数。 |

<a id="gaf275034765327b52b900046d71c411ee"></a>

### `smp_transport_init()`

```c
int smp_transport_init ( struct smp_transport * smpt)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

初始化 Zephyr SMP 传输对象（Transport Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `smpt` | 要构造的传输（Transport）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，失败时为负 `errno` 错误码。


## 6.6\_原页交叉引用（Cross References）

- [smp_transport_api_t](../system_service_model_reference/P082_smp_transport_api_t_结构体.md)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [smp_transport_bridge](../system_service_model_reference/P083_smp_transport_bridge_结构体.md)
- [smp_client_transport_entry](../system_service_model_reference/P079_smp_client_transport_entry_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/mgmt/mcumgr/transport/smp.h](../api_file_display_management_reference/P012_zephyr__mgmt__mcumgr__transport__smp.h_文件参考.md)
- [mcumgr_err_t](../api_usb_gnss_topic_reference/P011_管理（Management）.md#gac5d8757a7ca945c77f405764b85ad5c5)
- [TRANSPORT_MGMT_DIRECTION_INCOMING](../api_coap_trusted_topic_reference/P010_传输管理（Transport management）.md#ga9cdb0b588d6d3f12c8f845bc69ef9d13)
- [TRANSPORT_MGMT_DIRECTION_OUTGOING](../api_coap_trusted_topic_reference/P010_传输管理（Transport management）.md#ga22375d795b497134e20678d16352135d)
- [Deprecated](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000096)
- [CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE)
- [CONFIG_MCUMGR_TRANSPORT_REASSEMBLY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_REASSEMBLY)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342"></a>
<a id="gga5d886a11df0c49ca18e23e246ab2fab9a06953c39575f3903299011cde915ac13"></a>
<a id="gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe"></a>
<a id="gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43"></a>
<a id="gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f"></a>
<a id="gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7"></a>
<a id="gga5d886a11df0c49ca18e23e246ab2fab9addcf3d287f359bad85104d2a37b4e5c8"></a>
<a id="gga5d886a11df0c49ca18e23e246ab2fab9a3de5af5fe47980cdf749abc1694d84eb"></a>
<a id="gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_闪存区域接口（flash area Interface）.md) · [返回大纲](大纲.md) · [下一章](P007_调制解调器命令会话（Modem Chat）.md)
