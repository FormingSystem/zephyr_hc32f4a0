---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-234
title: bt_hci_evt_le_conn_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__conn__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第234章\_bt\_hci\_evt\_le\_conn\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__conn__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 234.1\_数据成员（Data Fields）

<a id="r_a897981117139c0e53ea7275b689f3799"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a897981117139c0e53ea7275b689f3799)。

<a id="r_a67618a1efa0149fadc1063a719d5b674"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a67618a1efa0149fadc1063a719d5b674)。

<a id="r_a8455e714d4333d90c2f117892f3dcd6f"></a>

```c
uint8_t role
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[role](#a8455e714d4333d90c2f117892f3dcd6f)。

<a id="r_a97e1aaa10832292ddfe4ee6731ef8999"></a>

```c
bt_addr_le_t peer_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_addr](#a97e1aaa10832292ddfe4ee6731ef8999)。

<a id="r_abe4bc0407d0295329631cb14672a7ee7"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#abe4bc0407d0295329631cb14672a7ee7)。

<a id="r_ab60cb42ecc83632c61656cd352b71cbe"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#ab60cb42ecc83632c61656cd352b71cbe)。

<a id="r_a4a90c9824d167b6c45b301e18bfe7f17"></a>

```c
uint16_t supv_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supv_timeout](#a4a90c9824d167b6c45b301e18bfe7f17)。

<a id="r_a3fff4c3b30da5922f75d36d97fdeee33"></a>

```c
uint8_t clock_accuracy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clock_accuracy](#a3fff4c3b30da5922f75d36d97fdeee33)。

## 234.2\_详细说明（Detailed Documentation）

<a id="a3fff4c3b30da5922f75d36d97fdeee33"></a>

### `clock_accuracy`

```c
uint8_t bt_hci_evt_le_conn_complete::clock_accuracy
```

<a id="a67618a1efa0149fadc1063a719d5b674"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_conn_complete::handle
```

<a id="abe4bc0407d0295329631cb14672a7ee7"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_conn_complete::interval
```

<a id="ab60cb42ecc83632c61656cd352b71cbe"></a>

### `latency`

```c
uint16_t bt_hci_evt_le_conn_complete::latency
```

<a id="a97e1aaa10832292ddfe4ee6731ef8999"></a>

### `peer_addr`

```c
bt_addr_le_t bt_hci_evt_le_conn_complete::peer_addr
```

<a id="a8455e714d4333d90c2f117892f3dcd6f"></a>

### `role`

```c
uint8_t bt_hci_evt_le_conn_complete::role
```

<a id="a897981117139c0e53ea7275b689f3799"></a>

### `status`

```c
uint8_t bt_hci_evt_le_conn_complete::status
```

<a id="a4a90c9824d167b6c45b301e18bfe7f17"></a>

### `supv_timeout`

```c
uint16_t bt_hci_evt_le_conn_complete::supv_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 234.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P233_bt_hci_evt_le_cis_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P235_bt_hci_evt_le_conn_param_req_结构体.md)
