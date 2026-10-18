---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-175
title: bt_tbs_client_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__client__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第175章\_bt\_tbs\_client\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__client__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存电话承载服务（Telephone Bearer Service，TBS）客户端回调的结构体。

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

<a id="details"></a>

保存电话承载服务客户端回调（Telephone Bearer Service client callbacks）的结构。可使用 `bt_tbs_client_register_cb()` 注册。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 175.1\_数据成员（Data Fields）

<a id="r_abfd4542a0781ff5676a191249f121e91"></a>

```c
bt_tbs_client_discover_cb discover
```

相关声明：[bt_tbs_client_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga9cac11cc696be9fb387f2f7685e0d8a7)、[discover](#abfd4542a0781ff5676a191249f121e91)。

发现（Discovery）过程已完成。

<a id="r_a0bc51181f188a1249407f2e50431d9fd"></a>

```c
bt_tbs_client_cp_cb originate_call
```

相关声明：[bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)、[originate_call](#a0bc51181f188a1249407f2e50431d9fd)。

发起通话（Originate call）操作已完成。

<a id="r_aa78425597fe7fd0db09d69c3ed757293"></a>

```c
bt_tbs_client_cp_cb terminate_call
```

相关声明：[bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)、[terminate_call](#aa78425597fe7fd0db09d69c3ed757293)。

终止通话（Terminate call）操作已完成。

<a id="r_a304a5fd373f1ba5ccb2eb77fcdbbd380"></a>

```c
bt_tbs_client_cp_cb hold_call
```

相关声明：[bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)、[hold_call](#a304a5fd373f1ba5ccb2eb77fcdbbd380)。

保持通话（Hold call）操作已完成。

<a id="r_a41242d76c976eef102d480965f977537"></a>

```c
bt_tbs_client_cp_cb accept_call
```

相关声明：[bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)、[accept_call](#a41242d76c976eef102d480965f977537)。

接受通话（Accept call）操作已完成。

<a id="r_a2a5fb7de5c3c4aab290c0163c0b40858"></a>

```c
bt_tbs_client_cp_cb retrieve_call
```

相关声明：[bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)、[retrieve_call](#a2a5fb7de5c3c4aab290c0163c0b40858)。

恢复通话（Retrieve call）操作已完成。

<a id="r_a2d6b7acd90d05c61f60f27236ab6f1ee"></a>

```c
bt_tbs_client_cp_cb join_calls
```

相关声明：[bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)、[join_calls](#a2d6b7acd90d05c61f60f27236ab6f1ee)。

合并通话（Join calls）操作已完成。

<a id="r_a36d8ea1717e57b9440e9b58e9411422a"></a>

```c
bt_tbs_client_read_string_cb bearer_provider_name
```

相关声明：[bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)、[bearer_provider_name](#a36d8ea1717e57b9440e9b58e9411422a)。

已读取承载提供方名称（Bearer provider name）。

<a id="r_a15ccb7de457631620983e7d2d0372967"></a>

```c
bt_tbs_client_read_string_cb bearer_uci
```

相关声明：[bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)、[bearer_uci](#a15ccb7de457631620983e7d2d0372967)。

已读取承载的统一呼叫方标识符（UCI）。

<a id="r_a596b31583975c416aa9cb6d64301c55f"></a>

```c
void(* technology )(struct bt_conn *conn, int err, uint8_t inst_index, enum bt_bearer_tech tech)
```

相关声明：[technology](#a596b31583975c416aa9cb6d64301c55f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)。

已读取承载技术（Bearer technology）。

<a id="r_a7f64cf8e3d0bc4ec21c44bd4fea6d7ee"></a>

```c
bt_tbs_client_read_string_cb uri_list
```

相关声明：[bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)、[uri_list](#a7f64cf8e3d0bc4ec21c44bd4fea6d7ee)。

已读取承载 URI 列表（Bearer URI list）。

<a id="r_a96df90461159f97f5dc8cbb72cd0cbc4"></a>

```c
bt_tbs_client_read_value_cb signal_strength
```

相关声明：[bt_tbs_client_read_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga600051910ed538a2da823554df23dd20)、[signal_strength](#a96df90461159f97f5dc8cbb72cd0cbc4)。

已读取承载信号强度（Bearer signal strength）。

<a id="r_a01426c4a84e71a9395cce2963e2e83a3"></a>

```c
bt_tbs_client_read_value_cb signal_interval
```

相关声明：[bt_tbs_client_read_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga600051910ed538a2da823554df23dd20)、[signal_interval](#a01426c4a84e71a9395cce2963e2e83a3)。

已读取承载信号间隔（Bearer signal interval）。

<a id="r_a10dc9404533db388b3ae1058542efd66"></a>

```c
bt_tbs_client_current_calls_cb current_calls
```

相关声明：[bt_tbs_client_current_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga7b31e1c30fa96081a3ef38e1a481b64f)、[current_calls](#a10dc9404533db388b3ae1058542efd66)。

已读取承载的当前通话（Bearer current calls）。

<a id="r_a90acde153f8893b5cba891884529d86c"></a>

```c
bt_tbs_client_read_value_cb ccid
```

相关声明：[bt_tbs_client_read_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga600051910ed538a2da823554df23dd20)、[ccid](#a90acde153f8893b5cba891884529d86c)。

已读取承载的内容控制 ID（CCID）。

<a id="r_ae95494a76e1f3275f48204dcd4798712"></a>

```c
bt_tbs_client_read_string_cb call_uri
```

相关声明：[bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)、[call_uri](#ae95494a76e1f3275f48204dcd4798712)。

已读取承载通话 URI（Bearer call URI）。

<a id="r_a94c3bfc1e88518de9e29e947064ec8dc"></a>

```c
bt_tbs_client_read_value_cb status_flags
```

相关声明：[bt_tbs_client_read_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga600051910ed538a2da823554df23dd20)、[status_flags](#a94c3bfc1e88518de9e29e947064ec8dc)。

已读取承载状态标志（Bearer status flags）。

<a id="r_a88cb69ef54c9399bceb5641202eeabce"></a>

```c
bt_tbs_client_call_states_cb call_state
```

相关声明：[bt_tbs_client_call_states_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga262ca74b7ae2f0c52657066549fa4f92)、[call_state](#a88cb69ef54c9399bceb5641202eeabce)。

已读取承载通话状态（Bearer call states）。

<a id="r_a91c61b29c16a43fd3f781fd7e0ab4618"></a>

```c
bt_tbs_client_read_value_cb optional_opcodes
```

相关声明：[bt_tbs_client_read_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga600051910ed538a2da823554df23dd20)、[optional_opcodes](#a91c61b29c16a43fd3f781fd7e0ab4618)。

已读取承载可选操作码（Bearer optional opcodes）。

<a id="r_ae8e5cbe52cbb300e1cd919d24c85c4df"></a>

```c
bt_tbs_client_termination_reason_cb termination_reason
```

相关声明：[bt_tbs_client_termination_reason_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab881b3caaaa4425e52afd84e53adee78)、[termination_reason](#ae8e5cbe52cbb300e1cd919d24c85c4df)。

已读取承载终止原因（Bearer terminate reason）。

<a id="r_a354ba5d21376813adc5c9765a5da1a09"></a>

```c
bt_tbs_client_read_string_cb remote_uri
```

相关声明：[bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)、[remote_uri](#a354ba5d21376813adc5c9765a5da1a09)。

已读取承载远端 URI（Bearer remote URI）。

<a id="r_ad2089050db76453b7f9c51c3d2fa4d17"></a>

```c
bt_tbs_client_read_string_cb friendly_name
```

相关声明：[bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)、[friendly_name](#ad2089050db76453b7f9c51c3d2fa4d17)。

已读取承载友好名称（Bearer friendly name）。

## 175.2\_详细说明（Detailed Documentation）

<a id="a41242d76c976eef102d480965f977537"></a>

### `accept_call`

```c
bt_tbs_client_cp_cb bt_tbs_client_cb::accept_call
```

接受通话（Accept call）操作已完成。

<a id="a36d8ea1717e57b9440e9b58e9411422a"></a>

### `bearer_provider_name`

```c
bt_tbs_client_read_string_cb bt_tbs_client_cb::bearer_provider_name
```

已读取承载提供方名称（Bearer provider name）。

<a id="a15ccb7de457631620983e7d2d0372967"></a>

### `bearer_uci`

```c
bt_tbs_client_read_string_cb bt_tbs_client_cb::bearer_uci
```

已读取承载的统一呼叫方标识符（UCI）。

<a id="a88cb69ef54c9399bceb5641202eeabce"></a>

### `call_state`

```c
bt_tbs_client_call_states_cb bt_tbs_client_cb::call_state
```

已读取承载通话状态（Bearer call states）。

<a id="ae95494a76e1f3275f48204dcd4798712"></a>

### `call_uri`

```c
bt_tbs_client_read_string_cb bt_tbs_client_cb::call_uri
```

已读取承载通话 URI（Bearer call URI）。

<a id="a90acde153f8893b5cba891884529d86c"></a>

### `ccid`

```c
bt_tbs_client_read_value_cb bt_tbs_client_cb::ccid
```

已读取承载的内容控制 ID（CCID）。

<a id="a10dc9404533db388b3ae1058542efd66"></a>

### `current_calls`

```c
bt_tbs_client_current_calls_cb bt_tbs_client_cb::current_calls
```

已读取承载的当前通话（Bearer current calls）。

<a id="abfd4542a0781ff5676a191249f121e91"></a>

### `discover`

```c
bt_tbs_client_discover_cb bt_tbs_client_cb::discover
```

发现（Discovery）过程已完成。

<a id="ad2089050db76453b7f9c51c3d2fa4d17"></a>

### `friendly_name`

```c
bt_tbs_client_read_string_cb bt_tbs_client_cb::friendly_name
```

已读取承载友好名称（Bearer friendly name）。

<a id="a304a5fd373f1ba5ccb2eb77fcdbbd380"></a>

### `hold_call`

```c
bt_tbs_client_cp_cb bt_tbs_client_cb::hold_call
```

保持通话（Hold call）操作已完成。

<a id="a2d6b7acd90d05c61f60f27236ab6f1ee"></a>

### `join_calls`

```c
bt_tbs_client_cp_cb bt_tbs_client_cb::join_calls
```

合并通话（Join calls）操作已完成。

<a id="a91c61b29c16a43fd3f781fd7e0ab4618"></a>

### `optional_opcodes`

```c
bt_tbs_client_read_value_cb bt_tbs_client_cb::optional_opcodes
```

已读取承载可选操作码（Bearer optional opcodes）。

<a id="a0bc51181f188a1249407f2e50431d9fd"></a>

### `originate_call`

```c
bt_tbs_client_cp_cb bt_tbs_client_cb::originate_call
```

发起通话（Originate call）操作已完成。

<a id="a354ba5d21376813adc5c9765a5da1a09"></a>

### `remote_uri`

```c
bt_tbs_client_read_string_cb bt_tbs_client_cb::remote_uri
```

已读取承载远端 URI（Bearer remote URI）。

<a id="a2a5fb7de5c3c4aab290c0163c0b40858"></a>

### `retrieve_call`

```c
bt_tbs_client_cp_cb bt_tbs_client_cb::retrieve_call
```

恢复通话（Retrieve call）操作已完成。

<a id="a01426c4a84e71a9395cce2963e2e83a3"></a>

### `signal_interval`

```c
bt_tbs_client_read_value_cb bt_tbs_client_cb::signal_interval
```

已读取承载信号间隔（Bearer signal interval）。

<a id="a96df90461159f97f5dc8cbb72cd0cbc4"></a>

### `signal_strength`

```c
bt_tbs_client_read_value_cb bt_tbs_client_cb::signal_strength
```

已读取承载信号强度（Bearer signal strength）。

<a id="a94c3bfc1e88518de9e29e947064ec8dc"></a>

### `status_flags`

```c
bt_tbs_client_read_value_cb bt_tbs_client_cb::status_flags
```

已读取承载状态标志（Bearer status flags）。

<a id="a596b31583975c416aa9cb6d64301c55f"></a>

### `technology`

```c
void(* bt_tbs_client_cb::technology) (struct bt_conn *conn, int err, uint8_t inst_index, enum bt_bearer_tech tech)
```

已读取承载技术（Bearer technology）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 函数中使用的连接。 |
| `err` | 错误值：`BT_TBS_CLIENT_RESULT_CODE_*` 或 GATT 错误。 |
| `inst_index` | 已更新的 TBS 实例索引。 |
| `tech` | 读取到的技术类型（technology）。其值可能超出枚举定义的取值范围。 |

<a id="aa78425597fe7fd0db09d69c3ed757293"></a>

### `terminate_call`

```c
bt_tbs_client_cp_cb bt_tbs_client_cb::terminate_call
```

终止通话（Terminate call）操作已完成。

<a id="ae8e5cbe52cbb300e1cd919d24c85c4df"></a>

### `termination_reason`

```c
bt_tbs_client_termination_reason_cb bt_tbs_client_cb::termination_reason
```

已读取承载终止原因（Bearer terminate reason）。

<a id="a7f64cf8e3d0bc4ec21c44bd4fea6d7ee"></a>

### `uri_list`

```c
bt_tbs_client_read_string_cb bt_tbs_client_cb::uri_list
```

已读取承载 URI 列表（Bearer URI list）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/tbs.h`

## 175.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/tbs.h](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h_source.html)
- [bt_tbs_client_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga9cac11cc696be9fb387f2f7685e0d8a7)
- [bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)
- [bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [bt_tbs_client_read_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga600051910ed538a2da823554df23dd20)
- [bt_tbs_client_current_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga7b31e1c30fa96081a3ef38e1a481b64f)
- [bt_tbs_client_call_states_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga262ca74b7ae2f0c52657066549fa4f92)
- [bt_tbs_client_termination_reason_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab881b3caaaa4425e52afd84e53adee78)
- [bt_tbs_client_register_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gabe2251d4ea88306793dc68ae683886bb)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P174_bt_tbs_client_call_state_结构体.md) · [返回大纲](大纲.md) · [下一章](P176_bt_tbs_instance_结构体.md)
