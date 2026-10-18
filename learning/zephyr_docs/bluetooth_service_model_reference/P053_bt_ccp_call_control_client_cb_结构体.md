---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-53
title: bt_ccp_call_control_client_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ccp__call__control__client__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_bt\_ccp\_call\_control\_client\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ccp__call__control__client__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存电话承载服务（Telephone Bearer Service，TBS）客户端回调的结构体。

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

<a id="details"></a>

保存电话承载服务客户端回调（Telephone Bearer Service client callbacks）的结构。可使用 `bt_tbs_client_register_cb()` 注册。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_a4ad442e0f84327a7d02b5bfd5bbf09c7"></a>

```c
void(* discover )(struct bt_ccp_call_control_client *client, int err, struct bt_ccp_call_control_client_bearers *bearers, void *user_data)
```

相关声明：[discover](#a4ad442e0f84327a7d02b5bfd5bbf09c7)、[bt_ccp_call_control_client](P050_bt_ccp_call_control_client_结构体.md)、[bt_ccp_call_control_client_bearers](P052_bt_ccp_call_control_client_bearers_结构体.md)、[user_data](#a1d4af4ea50002e2f3d24ed0d4bf21d83)。

`bt_ccp_call_control_client_discover()` 的回调函数（Callback function）。

<a id="r_a3830ba768a1300df7aee272a2d3ec00e"></a>

```c
void(* bearer_provider_name )(struct bt_ccp_call_control_client_bearer *bearer, int err, const char *name, void *user_data)
```

相关声明：[bearer_provider_name](#a3830ba768a1300df7aee272a2d3ec00e)、[bt_ccp_call_control_client_bearer](P051_bt_ccp_call_control_client_bearer_结构体.md)、[user_data](#a1d4af4ea50002e2f3d24ed0d4bf21d83)。

`bt_ccp_call_control_client_read_bearer_provider_name()` 的回调函数（Callback function）。

<a id="r_aed9802f73963157a9f45ee35e50ad8ac"></a>

```c
void(* bearer_uci )(struct bt_ccp_call_control_client_bearer *bearer, int err, const char *uci, void *user_data)
```

相关声明：[bearer_uci](#aed9802f73963157a9f45ee35e50ad8ac)、[bt_ccp_call_control_client_bearer](P051_bt_ccp_call_control_client_bearer_结构体.md)、[user_data](#a1d4af4ea50002e2f3d24ed0d4bf21d83)。

`bt_ccp_call_control_client_read_bearer_uci()` 的回调函数（Callback function）。

<a id="r_aba44cdf2667ca7622d7a8c70164cd847"></a>

```c
void(* bearer_tech )(struct bt_ccp_call_control_client_bearer *bearer, int err, enum bt_bearer_tech tech, void *user_data)
```

相关声明：[bearer_tech](#aba44cdf2667ca7622d7a8c70164cd847)、[bt_ccp_call_control_client_bearer](P051_bt_ccp_call_control_client_bearer_结构体.md)、[bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)、[user_data](#a1d4af4ea50002e2f3d24ed0d4bf21d83)。

`bt_ccp_call_control_client_read_bearer_tech()` 的回调函数（Callback function）。

<a id="r_a3c6d22aefdbef40ac42fb05e9656789a"></a>

```c
void(* bearer_uri_schemes )(struct bt_ccp_call_control_client_bearer *bearer, int err, const char *uri_schemes, void *user_data)
```

相关声明：[bearer_uri_schemes](#a3c6d22aefdbef40ac42fb05e9656789a)、[bt_ccp_call_control_client_bearer](P051_bt_ccp_call_control_client_bearer_结构体.md)、[user_data](#a1d4af4ea50002e2f3d24ed0d4bf21d83)。

`bt_ccp_call_control_client_read_bearer_uri_schemes()` 的回调函数（Callback function）。

<a id="r_a1d4af4ea50002e2f3d24ed0d4bf21d83"></a>

```c
void * user_data
```

相关声明：[user_data](#a1d4af4ea50002e2f3d24ed0d4bf21d83)。

传给所有回调的用户数据（User data）。

## 53.2\_详细说明（Detailed Documentation）

<a id="a3830ba768a1300df7aee272a2d3ec00e"></a>

### `bearer_provider_name`

```c
void(* bt_ccp_call_control_client_cb::bearer_provider_name) (struct bt_ccp_call_control_client_bearer *bearer, int err, const char *name, void *user_data)
```

`bt_ccp_call_control_client_read_bearer_provider_name()` 的回调函数（Callback function）。

读取承载提供方名称过程（Read bearer provider name procedure）完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 呼叫控制客户端承载指针（Call Control Client bearer pointer）。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `name` | 承载提供方名称（Bearer provider name）。`err` 非 `0` 时为 `NULL`。若返回后仍要使用，必须复制该值。 |
| `user_data` | 存储于回调结构中的用户数据（User data）。未启用 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA` 时，始终为 `NULL`。 |

<a id="aba44cdf2667ca7622d7a8c70164cd847"></a>

### `bearer_tech`

```c
void(* bt_ccp_call_control_client_cb::bearer_tech) (struct bt_ccp_call_control_client_bearer *bearer, int err, enum bt_bearer_tech tech, void *user_data)
```

`bt_ccp_call_control_client_read_bearer_tech()` 的回调函数（Callback function）。

读取承载技术过程（Read bearer technology procedure）完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 呼叫控制客户端承载指针（Call Control Client bearer pointer）。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `tech` | 承载技术（Bearer technology）。此值可能超出枚举列出的取值范围。 |
| `user_data` | 存储于回调结构中的用户数据（User data）。未启用 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA` 时，始终为 `NULL`。 |

<a id="aed9802f73963157a9f45ee35e50ad8ac"></a>

### `bearer_uci`

```c
void(* bt_ccp_call_control_client_cb::bearer_uci) (struct bt_ccp_call_control_client_bearer *bearer, int err, const char *uci, void *user_data)
```

`bt_ccp_call_control_client_read_bearer_uci()` 的回调函数（Callback function）。

读取承载统一呼叫标识符过程（Read bearer UCI procedure）完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 呼叫控制客户端承载指针（Call Control Client bearer pointer）。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `uci` | 承载的统一呼叫标识符（UCI）。`err` 非 `0` 时为 `NULL`。 |
| `user_data` | 存储于回调结构中的用户数据（User data）。未启用 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA` 时，始终为 `NULL`。 |

<a id="a3c6d22aefdbef40ac42fb05e9656789a"></a>

### `bearer_uri_schemes`

```c
void(* bt_ccp_call_control_client_cb::bearer_uri_schemes) (struct bt_ccp_call_control_client_bearer *bearer, int err, const char *uri_schemes, void *user_data)
```

`bt_ccp_call_control_client_read_bearer_uri_schemes()` 的回调函数（Callback function）。

读取承载支持的 URI 方案列表过程（Read bearer URI schemes supported list procedure）完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 呼叫控制客户端承载指针（Call Control Client bearer pointer）。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `uri_schemes` | `err` 为 `0` 时，此项为承载支持的统一资源标识符方案列表（URI schemes supported list）。若返回后仍要使用，必须复制该值。 |
| `user_data` | 存储于回调结构中的用户数据（User data）。未启用 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA` 时，始终为 `NULL`。 |

<a id="a4ad442e0f84327a7d02b5bfd5bbf09c7"></a>

### `discover`

```c
void(* bt_ccp_call_control_client_cb::discover) (struct bt_ccp_call_control_client *client, int err, struct bt_ccp_call_control_client_bearers *bearers, void *user_data)
```

`bt_ccp_call_control_client_discover()` 的回调函数（Callback function）。

发现过程（Discovery procedure）完成时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 呼叫控制客户端指针（Call Control Client pointer）。 |
| `err` | 错误值。成功时为 0；正值表示 GATT 错误，负值表示 `errno` 错误。 |
| `bearers` | 找到的承载（Bearers）。若返回后仍要使用，必须复制该值。 |
| `user_data` | 存储于回调结构中的用户数据（User data）。未启用 `CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA` 时，始终为 `NULL`。 |

<a id="a1d4af4ea50002e2f3d24ed0d4bf21d83"></a>

### `user_data`

```c
void* bt_ccp_call_control_client_cb::user_data
```

传给所有回调的用户数据（User data）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/ccp.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/ccp.h](https://docs.zephyrproject.org/latest/doxygen/html/ccp_8h_source.html)
- [bt_ccp_call_control_client](P050_bt_ccp_call_control_client_结构体.md)
- [bt_ccp_call_control_client_bearers](P052_bt_ccp_call_control_client_bearers_结构体.md)
- [bt_ccp_call_control_client_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga2a5bce65e39ba05625423308f996021d)
- [bt_ccp_call_control_client_bearer](P051_bt_ccp_call_control_client_bearer_结构体.md)
- [bt_ccp_call_control_client_read_bearer_provider_name()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga31455b659d7b20053624f79c71cefa84)
- [bt_ccp_call_control_client_read_bearer_uci()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gac106a4de174d941e6390a1743d11f01d)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [bt_ccp_call_control_client_read_bearer_tech()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gaf8df0504479ac519328d98f2ddf6db15)
- [bt_ccp_call_control_client_read_bearer_uri_schemes()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga9b146acb76b6e40ae639da92c5d50941)
- [bt_tbs_client_register_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gabe2251d4ea88306793dc68ae683886bb)
- [CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CCP_CALL_CONTROL_CLIENT_CB_USER_DATA)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_bt_ccp_call_control_client_bearers_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_bt_ccp_call_control_server_bearer_结构体.md)
