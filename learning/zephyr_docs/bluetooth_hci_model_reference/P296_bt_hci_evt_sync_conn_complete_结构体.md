---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-296
title: bt_hci_evt_sync_conn_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__sync__conn__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第296章\_bt\_hci\_evt\_sync\_conn\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__sync__conn__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 296.1\_数据成员（Data Fields）

<a id="r_accd17a95f35ab1988122df7584830f60"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#accd17a95f35ab1988122df7584830f60)。

<a id="r_aa48aa29ff73e93e8d961013f066c1b5e"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#aa48aa29ff73e93e8d961013f066c1b5e)。

<a id="r_a78f5560783400f1d1a63b2c9d69fa7ed"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a78f5560783400f1d1a63b2c9d69fa7ed)。

<a id="r_aacf9919945e9b755913da145f0fe78ae"></a>

```c
uint8_t link_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[link_type](#aacf9919945e9b755913da145f0fe78ae)。

<a id="r_a4b93873ad6f5388657511d87fc0a8c85"></a>

```c
uint8_t tx_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_interval](#a4b93873ad6f5388657511d87fc0a8c85)。

<a id="r_a68a31880c8aab9245be043c1719464d3"></a>

```c
uint8_t retansmission_window
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retansmission_window](#a68a31880c8aab9245be043c1719464d3)。

<a id="r_a6a455f56da4666cb602e6c05157e166d"></a>

```c
uint16_t rx_pkt_length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rx_pkt_length](#a6a455f56da4666cb602e6c05157e166d)。

<a id="r_ab4d4106d5120f10e8300834db12740d8"></a>

```c
uint16_t tx_pkt_length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_pkt_length](#ab4d4106d5120f10e8300834db12740d8)。

<a id="r_a5f6068569bf649bcd1d13928f56f9703"></a>

```c
uint8_t air_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[air_mode](#a5f6068569bf649bcd1d13928f56f9703)。

## 296.2\_详细说明（Detailed Documentation）

<a id="a5f6068569bf649bcd1d13928f56f9703"></a>

### `air_mode`

```c
uint8_t bt_hci_evt_sync_conn_complete::air_mode
```

<a id="a78f5560783400f1d1a63b2c9d69fa7ed"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_evt_sync_conn_complete::bdaddr
```

<a id="aa48aa29ff73e93e8d961013f066c1b5e"></a>

### `handle`

```c
uint16_t bt_hci_evt_sync_conn_complete::handle
```

<a id="aacf9919945e9b755913da145f0fe78ae"></a>

### `link_type`

```c
uint8_t bt_hci_evt_sync_conn_complete::link_type
```

<a id="a68a31880c8aab9245be043c1719464d3"></a>

### `retansmission_window`

```c
uint8_t bt_hci_evt_sync_conn_complete::retansmission_window
```

<a id="a6a455f56da4666cb602e6c05157e166d"></a>

### `rx_pkt_length`

```c
uint16_t bt_hci_evt_sync_conn_complete::rx_pkt_length
```

<a id="accd17a95f35ab1988122df7584830f60"></a>

### `status`

```c
uint8_t bt_hci_evt_sync_conn_complete::status
```

<a id="a4b93873ad6f5388657511d87fc0a8c85"></a>

### `tx_interval`

```c
uint8_t bt_hci_evt_sync_conn_complete::tx_interval
```

<a id="ab4d4106d5120f10e8300834db12740d8"></a>

### `tx_pkt_length`

```c
uint16_t bt_hci_evt_sync_conn_complete::tx_pkt_length
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 296.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P295_bt_hci_evt_ssp_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P297_bt_hci_evt_user_confirm_req_结构体.md)
