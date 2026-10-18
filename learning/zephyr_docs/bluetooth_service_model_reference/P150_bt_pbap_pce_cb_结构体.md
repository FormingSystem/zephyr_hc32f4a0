---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-150
title: bt_pbap_pce_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pce__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第150章\_bt\_pbap\_pce\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pce__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话簿访问配置文件（PBAP）的电话簿客户端设备（PCE）回调操作结构。

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

<a id="details"></a>

电话簿访问规范（PBAP）的电话簿客户端设备（Phone Book Client Equipment，PCE）回调操作结构体。此结构体必须在 PBAP 客户端的整个生命周期内保持有效且不变。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 150.1\_数据成员（Data Fields）

<a id="r_a22175f0418e8e58a8a09eccc37f4dfc3"></a>

```c
void(* rfcomm_connected )(struct bt_conn *conn, struct bt_pbap_pce *pbap_pce)
```

相关声明：[rfcomm_connected](#a22175f0418e8e58a8a09eccc37f4dfc3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)。

RFCOMM 传输连接建立回调。

<a id="r_aeb6cb005d085610ff73004ebf855e50d"></a>

```c
void(* rfcomm_disconnected )(struct bt_pbap_pce *pbap_pce)
```

相关声明：[rfcomm_disconnected](#aeb6cb005d085610ff73004ebf855e50d)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)。

RFCOMM 传输连接断开回调。

<a id="r_a7c912fe7083ffcb9944e103e8f9ff314"></a>

```c
void(* l2cap_connected )(struct bt_conn *conn, struct bt_pbap_pce *pbap_pce)
```

相关声明：[l2cap_connected](#a7c912fe7083ffcb9944e103e8f9ff314)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)。

L2CAP 传输连接建立回调。

<a id="r_aa9cab8cafac0fa94c1994b95498a3f76"></a>

```c
void(* l2cap_disconnected )(struct bt_pbap_pce *pbap_pce)
```

相关声明：[l2cap_disconnected](#aa9cab8cafac0fa94c1994b95498a3f76)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)。

L2CAP 传输连接断开回调。

<a id="r_a865670561310a210b6dd3c701d9b8e9c"></a>

```c
void(* connect )(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#a865670561310a210b6dd3c701d9b8e9c)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PCE 连接（connect）响应回调。

<a id="r_ac89246b832f6d548d41bf79b2059e3e2"></a>

```c
void(* disconnect )(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[disconnect](#ac89246b832f6d548d41bf79b2059e3e2)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PCE 断开连接（disconnect）响应回调。

<a id="r_a3fd377996356c7cf6b6e6f15f731f249"></a>

```c
void(* pull_phone_book )(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[pull_phone_book](#a3fd377996356c7cf6b6e6f15f731f249)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PCE 拉取电话簿（pull phone book）响应回调。

<a id="r_a3e643a024fa72df83836669d87803f95"></a>

```c
void(* pull_vcard_listing )(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[pull_vcard_listing](#a3e643a024fa72df83836669d87803f95)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PCE 拉取 vCard 列表（pull vCard listing）响应回调。

<a id="r_a3fd9b659366d8804e9b575c8146f2767"></a>

```c
void(* pull_vcard_entry )(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[pull_vcard_entry](#a3fd9b659366d8804e9b575c8146f2767)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PCE 拉取 vCard 条目（pull vCard entry）响应回调。

<a id="r_a6aab1615dc299ed1b9c37f6c89462c77"></a>

```c
void(* set_phone_book )(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[set_phone_book](#a6aab1615dc299ed1b9c37f6c89462c77)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PCE 设置电话簿（set phone book）响应回调。

<a id="r_adf7bef6a90e1db928a077d1db4955c07"></a>

```c
void(* abort )(struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[abort](#adf7bef6a90e1db928a077d1db4955c07)、[bt_pbap_pce](P149_bt_pbap_pce_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

PBAP PCE 中止（abort）响应回调。

## 150.2\_详细说明（Detailed Documentation）

<a id="adf7bef6a90e1db928a077d1db4955c07"></a>

### `abort`

```c
void(* bt_pbap_pce_cb::abort) (struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

PBAP PCE 中止（abort）响应回调。

收到 PCE 中止（abort）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 可选响应头缓冲区。 |

<a id="a865670561310a210b6dd3c701d9b8e9c"></a>

### `connect`

```c
void(* bt_pbap_pce_cb::connect) (struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

PBAP PCE 连接（connect）响应回调。

收到 PBAP 连接（connect）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `version` | 电话簿服务器设备（PSE）支持的 OBEX 版本。 |
| `mopl` | PSE 的最大 OBEX 数据包长度。 |
| `buf` | 可选响应头缓冲区。 |

<a id="ac89246b832f6d548d41bf79b2059e3e2"></a>

### `disconnect`

```c
void(* bt_pbap_pce_cb::disconnect) (struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

PBAP PCE 断开连接（disconnect）响应回调。

收到 PBAP 断开连接（disconnect）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 可选响应头缓冲区。 |

<a id="a7c912fe7083ffcb9944e103e8f9ff314"></a>

### `l2cap_connected`

```c
void(* bt_pbap_pce_cb::l2cap_connected) (struct bt_conn *conn, struct bt_pbap_pce *pbap_pce)
```

L2CAP 传输连接建立回调。

底层 L2CAP 传输连接建立时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接。 |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |

<a id="aa9cab8cafac0fa94c1994b95498a3f76"></a>

### `l2cap_disconnected`

```c
void(* bt_pbap_pce_cb::l2cap_disconnected) (struct bt_pbap_pce *pbap_pce)
```

L2CAP 传输连接断开回调。

底层 L2CAP 传输连接断开时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |

<a id="a3fd377996356c7cf6b6e6f15f731f249"></a>

### `pull_phone_book`

```c
void(* bt_pbap_pce_cb::pull_phone_book) (struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

PBAP PCE 拉取电话簿（pull phone book）响应回调。

收到 PCE 拉取电话簿（pull phone book）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 可选响应头。 |

<a id="a3fd9b659366d8804e9b575c8146f2767"></a>

### `pull_vcard_entry`

```c
void(* bt_pbap_pce_cb::pull_vcard_entry) (struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

PBAP PCE 拉取 vCard 条目（pull vCard entry）响应回调。

收到 PCE 拉取 vCard 条目（pull vCard entry）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 可选响应头。 |

<a id="a3e643a024fa72df83836669d87803f95"></a>

### `pull_vcard_listing`

```c
void(* bt_pbap_pce_cb::pull_vcard_listing) (struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

PBAP PCE 拉取 vCard 列表（pull vCard listing）响应回调。

收到 PCE 拉取 vCard 列表（pull vCard listing）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 可选响应头。 |

<a id="a22175f0418e8e58a8a09eccc37f4dfc3"></a>

### `rfcomm_connected`

```c
void(* bt_pbap_pce_cb::rfcomm_connected) (struct bt_conn *conn, struct bt_pbap_pce *pbap_pce)
```

RFCOMM 传输连接建立回调。

底层 RFCOMM 传输连接建立时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 异步无连接（ACL）连接。 |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |

<a id="aeb6cb005d085610ff73004ebf855e50d"></a>

### `rfcomm_disconnected`

```c
void(* bt_pbap_pce_cb::rfcomm_disconnected) (struct bt_pbap_pce *pbap_pce)
```

RFCOMM 传输连接断开回调。

底层 RFCOMM 传输连接断开时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |

<a id="a6aab1615dc299ed1b9c37f6c89462c77"></a>

### `set_phone_book`

```c
void(* bt_pbap_pce_cb::set_phone_book) (struct bt_pbap_pce *pbap_pce, uint8_t rsp_code, struct net_buf *buf)
```

PBAP PCE 设置电话簿（set phone book）响应回调。

收到 PCE 设置电话簿（set phone book）响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pbap_pce` | PBAP PCE 对象，类型为 `bt_pbap_pce`。 |
| `rsp_code` | 响应码，类型为 `bt_pbap_rsp_code`。 |
| `buf` | 可选响应头缓冲区。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/pbap.h`

## 150.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/pbap.h](https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_pbap_pce](P149_bt_pbap_pce_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_pbap_rsp_code](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html#ga9d9697d62b6bdbbc4feb0cf4b9776b58)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P149_bt_pbap_pce_结构体.md) · [返回大纲](大纲.md) · [下一章](P151_bt_pbap_pse_结构体.md)
