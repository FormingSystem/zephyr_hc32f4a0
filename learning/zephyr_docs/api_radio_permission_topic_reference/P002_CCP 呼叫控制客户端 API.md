---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-2
title: CCP 呼叫控制客户端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_CCP 呼叫控制客户端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fccp_5Fcall_5Fcontrol_5Fclient_5Fbearers"></a>

```c
struct bt_ccp_call_control_client_bearers
```

相关声明：[bt_ccp_call_control_client_bearers](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md)。

包含客户端承载信息的结构体。

<a id="r_bt_5Fccp_5Fcall_5Fcontrol_5Fclient_5Fcb"></a>

```c
struct bt_ccp_call_control_client_cb
```

相关声明：[bt_ccp_call_control_client_cb](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md)。

保存电话承载服务（Telephone Bearer Service，TBS）客户端回调的结构体。

<a id="r_bt_5Fccp_5Fcall_5Fcontrol_5Fclient"></a>

```c
struct bt_ccp_call_control_client
```

相关声明：[bt_ccp_call_control_client](../bluetooth_service_model_reference/P050_bt_ccp_call_control_client_结构体.md)。

抽象呼叫控制客户端（Call Control Client）结构体。

<a id="r_bt_5Fccp_5Fcall_5Fcontrol_5Fclient_5Fbearer"></a>

```c
struct bt_ccp_call_control_client_bearer
```

相关声明：[bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)。

抽象呼叫控制客户端承载（Bearer）结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_ga2a5bce65e39ba05625423308f996021d"></a>

```c
int bt_ccp_call_control_client_discover (struct bt_conn *conn, struct bt_ccp_call_control_client **out_client)
```

相关声明：[bt_ccp_call_control_client_discover](#ga2a5bce65e39ba05625423308f996021d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_ccp_call_control_client](../bluetooth_service_model_reference/P050_bt_ccp_call_control_client_结构体.md)。

发现远程设备对电话承载服务（Telephone Bearer Service，TBS）的支持。

<a id="r_ga8c5c3907759fe02745339b9456cca05f"></a>

```c
int bt_ccp_call_control_client_register_cb (struct bt_ccp_call_control_client_cb *cb)
```

相关声明：[bt_ccp_call_control_client_register_cb](#ga8c5c3907759fe02745339b9456cca05f)、[bt_ccp_call_control_client_cb](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md)。

注册呼叫控制客户端（Call Control Client）的回调。

<a id="r_ga534a15db3e87d63942de6ba4bd8377db"></a>

```c
int bt_ccp_call_control_client_unregister_cb (struct bt_ccp_call_control_client_cb *cb)
```

相关声明：[bt_ccp_call_control_client_unregister_cb](#ga534a15db3e87d63942de6ba4bd8377db)、[bt_ccp_call_control_client_cb](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md)。

注销呼叫控制客户端（Call Control Client）的回调。

<a id="r_gac8aa850b1e77bff1058e63be8c07c4c8"></a>

```c
int bt_ccp_call_control_client_get_bearers (struct bt_ccp_call_control_client *client, struct bt_ccp_call_control_client_bearers *bearers)
```

相关声明：[bt_ccp_call_control_client_get_bearers](#gac8aa850b1e77bff1058e63be8c07c4c8)、[bt_ccp_call_control_client](../bluetooth_service_model_reference/P050_bt_ccp_call_control_client_结构体.md)、[bt_ccp_call_control_client_bearers](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md)。

获取客户端实例（Client Instance）的承载（Bearers）。

<a id="r_ga31455b659d7b20053624f79c71cefa84"></a>

```c
int bt_ccp_call_control_client_read_bearer_provider_name (struct bt_ccp_call_control_client_bearer *bearer)
```

相关声明：[bt_ccp_call_control_client_read_bearer_provider_name](#ga31455b659d7b20053624f79c71cefa84)、[bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)。

读取远程 TBS 承载的提供方名称（Bearer Provider Name）。

<a id="r_gac106a4de174d941e6390a1743d11f01d"></a>

```c
int bt_ccp_call_control_client_read_bearer_uci (struct bt_ccp_call_control_client_bearer *bearer)
```

相关声明：[bt_ccp_call_control_client_read_bearer_uci](#gac106a4de174d941e6390a1743d11f01d)、[bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)。

读取远程 TBS 承载的统一呼叫者标识符（Uniform Caller Identifier，UCI）。

<a id="r_gaf8df0504479ac519328d98f2ddf6db15"></a>

```c
int bt_ccp_call_control_client_read_bearer_tech (struct bt_ccp_call_control_client_bearer *bearer)
```

相关声明：[bt_ccp_call_control_client_read_bearer_tech](#gaf8df0504479ac519328d98f2ddf6db15)、[bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)。

读取远程 TBS 承载的技术（Bearer Technology）。

<a id="r_ga9b146acb76b6e40ae639da92c5d50941"></a>

```c
int bt_ccp_call_control_client_read_bearer_uri_schemes (struct bt_ccp_call_control_client_bearer *bearer)
```

相关声明：[bt_ccp_call_control_client_read_bearer_uri_schemes](#ga9b146acb76b6e40ae639da92c5d50941)、[bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)。

读取远程 TBS 承载所支持的 URI 方案列表（URI Schemes Supported List）。

## 2.3\_详细说明（Detailed Documentation）

<a id="ga2a5bce65e39ba05625423308f996021d"></a>

### `bt_ccp_call_control_client_discover()`

```c
int bt_ccp_call_control_client_discover ( struct bt_conn * conn, struct bt_ccp_call_control_client ** out_client )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

发现远程设备对电话承载服务（Telephone Bearer Service，TBS）的支持。

在远端设备上发现电话承载服务（Telephone Bearer Service，TBS）与通用电话承载服务（Generic Telephone Bearer Service，GTBS）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 与远端服务器的连接（Connection）。 |
| `out_client` | 成功时指向客户端实例（Client Instance）的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | conn 或 out_client 为 NULL。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存。 |
| `-EBUSY` | 已在对 conn 执行发现（Discovery）。 |
| `-ENOEXEC` | 底层 TBS 客户端返回了意外错误。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_BT_CCP_CALL_CONTROL_CLIENT 时可用。

<a id="gac8aa850b1e77bff1058e63be8c07c4c8"></a>

### `bt_ccp_call_control_client_get_bearers()`

```c
int bt_ccp_call_control_client_get_bearers ( struct bt_ccp_call_control_client * client, struct bt_ccp_call_control_client_bearers * bearers )
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

获取客户端实例（Client Instance）的承载（Bearers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 要获取其承载（Bearers）的客户端。 |
| `[out] bearers` | 用于填入 client 的承载（Bearers）的结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | client 或 bearers 为 NULL。 |

<a id="ga31455b659d7b20053624f79c71cefa84"></a>

### `bt_ccp_call_control_client_read_bearer_provider_name()`

```c
int bt_ccp_call_control_client_read_bearer_provider_name ( struct bt_ccp_call_control_client_bearer * bearer)
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

读取远程 TBS 承载的提供方名称（Bearer Provider Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 要从中读取名称的承载（Bearer） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 为 NULL。 |
| `-EFAULT` | 尚未发现 bearer。 |
| `-EEXIST` | 无法为 bearer 确定对应的 CCP 呼叫控制客户端 API（Call Control Client APIs）。 |
| `-EBUSY` | bearer 标识的 CCP 呼叫控制客户端 API（Call Control Client APIs）正忙，或 bearer 的 TBS 实例正忙。 |
| `-ENOTCONN` | bearer 标识的 CCP 呼叫控制客户端 API（Call Control Client APIs）未连接。 |
| `-ENOEXEC` | 底层 TBS 客户端返回了意外错误。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME 时可用。

<a id="gaf8df0504479ac519328d98f2ddf6db15"></a>

### `bt_ccp_call_control_client_read_bearer_tech()`

```c
int bt_ccp_call_control_client_read_bearer_tech ( struct bt_ccp_call_control_client_bearer * bearer)
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

读取远程 TBS 承载的技术（Bearer Technology）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 要从中读取技术类型（Technology）的承载（Bearer） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 为 NULL。 |
| `-EFAULT` | 尚未发现 bearer。 |
| `-EEXIST` | 无法为 bearer 确定对应的 CCP 呼叫控制客户端 API（Call Control Client APIs）。 |
| `-EBUSY` | bearer 标识的 CCP 呼叫控制客户端 API（Call Control Client APIs）正忙，或 bearer 的 TBS 实例正忙。 |
| `-ENOTCONN` | bearer 标识的 CCP 呼叫控制客户端 API（Call Control Client APIs）未连接。 |
| `-ENOEXEC` | 底层 TBS 客户端返回了意外错误。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY 时可用。

<a id="gac106a4de174d941e6390a1743d11f01d"></a>

### `bt_ccp_call_control_client_read_bearer_uci()`

```c
int bt_ccp_call_control_client_read_bearer_uci ( struct bt_ccp_call_control_client_bearer * bearer)
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

读取远程 TBS 承载的统一呼叫者标识符（Uniform Caller Identifier，UCI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 要从中读取 UCI 的承载（Bearer） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 为 NULL。 |
| `-EFAULT` | 尚未发现 bearer。 |
| `-EEXIST` | 无法为 bearer 确定对应的 CCP 呼叫控制客户端 API（Call Control Client APIs）。 |
| `-EBUSY` | bearer 标识的 CCP 呼叫控制客户端 API（Call Control Client APIs）正忙，或 bearer 的 TBS 实例正忙。 |
| `-ENOTCONN` | bearer 标识的 CCP 呼叫控制客户端 API（Call Control Client APIs）未连接。 |
| `-ENOEXEC` | 底层 TBS 客户端返回了意外错误。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_BT_TBS_CLIENT_BEARER_UCI 时可用。

<a id="ga9b146acb76b6e40ae639da92c5d50941"></a>

### `bt_ccp_call_control_client_read_bearer_uri_schemes()`

```c
int bt_ccp_call_control_client_read_bearer_uri_schemes ( struct bt_ccp_call_control_client_bearer * bearer)
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

读取远程 TBS 承载所支持的 URI 方案列表（URI Schemes Supported List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearer` | 要从中读取支持的 URI 方案列表（URI Schemes Supported List）的承载（Bearer） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | bearer 为 NULL。 |
| `-EFAULT` | 尚未发现 bearer。 |
| `-EEXIST` | 无法为 bearer 确定对应的 CCP 呼叫控制客户端 API（Call Control Client APIs）。 |
| `-EBUSY` | bearer 标识的 CCP 呼叫控制客户端 API（Call Control Client APIs）正忙，或 bearer 的 TBS 实例正忙。 |
| `-ENOTCONN` | bearer 标识的 CCP 呼叫控制客户端 API（Call Control Client APIs）未连接。 |
| `-ENOEXEC` | 底层 TBS 客户端返回了意外错误。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST 时可用。

<a id="ga8c5c3907759fe02745339b9456cca05f"></a>

### `bt_ccp_call_control_client_register_cb()`

```c
int bt_ccp_call_control_client_register_cb ( struct bt_ccp_call_control_client_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

注册呼叫控制客户端（Call Control Client）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | cb 为 NULL。 |
| `-EEXISTS` | cb 已注册。 |

<a id="ga534a15db3e87d63942de6ba4bd8377db"></a>

### `bt_ccp_call_control_client_unregister_cb()`

```c
int bt_ccp_call_control_client_unregister_cb ( struct bt_ccp_call_control_client_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

注销呼叫控制客户端（Call Control Client）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | cb 为 NULL。 |
| `-EALREADY` | cb 未注册。 |


## 2.4\_原页交叉引用（Cross References）

- [bt_ccp_call_control_client_bearers](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md)
- [bt_ccp_call_control_client_cb](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md)
- [bt_ccp_call_control_client](../bluetooth_service_model_reference/P050_bt_ccp_call_control_client_结构体.md)
- [bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/audio/ccp.h](../api_file_signal_device_reference/P002_zephyr__bluetooth__audio__ccp.h_文件参考.md)
- [CONFIG_BT_CCP_CALL_CONTROL_CLIENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CCP_CALL_CONTROL_CLIENT)
- [CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME)
- [CCP 呼叫控制客户端 API](P002_CCP 呼叫控制客户端 API.md)
- [CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY)
- [CONFIG_BT_TBS_CLIENT_BEARER_UCI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_UCI)
- [CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_Andes QSPI-NOR 原地执行（XIP）.md) · [返回大纲](大纲.md) · [下一章](P003_蓝牙HCI锁步命令（Lockstep Command）的辅助接口。.md)
