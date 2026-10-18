---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-8
title: bt_hci_cp_accept_sync_conn_req_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__accept__sync__conn__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_bt\_hci\_cp\_accept\_sync\_conn\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__accept__sync__conn__req.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_a6a5a56d3a9d1a6d1064e7bd4c9fd333e"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a6a5a56d3a9d1a6d1064e7bd4c9fd333e)。

<a id="r_a53fe4c6d61dbb99f99aa445b2c47a8ef"></a>

```c
uint32_t tx_bandwidth
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_bandwidth](#a53fe4c6d61dbb99f99aa445b2c47a8ef)。

<a id="r_aceda6dbd3e221ad080850e9635886a86"></a>

```c
uint32_t rx_bandwidth
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_bandwidth](#aceda6dbd3e221ad080850e9635886a86)。

<a id="r_a4ba6dffd840ef868524b490d227fd085"></a>

```c
uint16_t max_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_latency](#a4ba6dffd840ef868524b490d227fd085)。

<a id="r_adba31b588bf12e852cc43b85c006aaa3"></a>

```c
uint16_t content_format
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[content_format](#adba31b588bf12e852cc43b85c006aaa3)。

<a id="r_ab5ece67c5a1e62fc4124556eef743c26"></a>

```c
uint8_t retrans_effort
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retrans_effort](#ab5ece67c5a1e62fc4124556eef743c26)。

<a id="r_ab5d9c27ebdf45fb54b0c6330b5b095be"></a>

```c
uint16_t pkt_type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pkt_type](#ab5d9c27ebdf45fb54b0c6330b5b095be)。

## 8.2\_详细说明（Detailed Documentation）

<a id="a6a5a56d3a9d1a6d1064e7bd4c9fd333e"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_accept_sync_conn_req::bdaddr
```

<a id="adba31b588bf12e852cc43b85c006aaa3"></a>

### `content_format`

```c
uint16_t bt_hci_cp_accept_sync_conn_req::content_format
```

<a id="a4ba6dffd840ef868524b490d227fd085"></a>

### `max_latency`

```c
uint16_t bt_hci_cp_accept_sync_conn_req::max_latency
```

<a id="ab5d9c27ebdf45fb54b0c6330b5b095be"></a>

### `pkt_type`

```c
uint16_t bt_hci_cp_accept_sync_conn_req::pkt_type
```

<a id="ab5ece67c5a1e62fc4124556eef743c26"></a>

### `retrans_effort`

```c
uint8_t bt_hci_cp_accept_sync_conn_req::retrans_effort
```

<a id="aceda6dbd3e221ad080850e9635886a86"></a>

### `rx_bandwidth`

```c
uint32_t bt_hci_cp_accept_sync_conn_req::rx_bandwidth
```

<a id="a53fe4c6d61dbb99f99aa445b2c47a8ef"></a>

### `tx_bandwidth`

```c
uint32_t bt_hci_cp_accept_sync_conn_req::tx_bandwidth
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_bt_hci_cp_accept_conn_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_bt_hci_cp_auth_requested_结构体.md)
