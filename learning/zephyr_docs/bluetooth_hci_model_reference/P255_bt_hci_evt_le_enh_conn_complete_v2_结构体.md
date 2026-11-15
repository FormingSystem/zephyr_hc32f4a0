---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-255
title: bt_hci_evt_le_enh_conn_complete_v2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__enh__conn__complete__v2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第255章\_bt\_hci\_evt\_le\_enh\_conn\_complete\_v2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__enh__conn__complete__v2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 255.1\_数据成员（Data Fields）

<a id="r_ad72ba07d766135a94474a9d004da1a66"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ad72ba07d766135a94474a9d004da1a66)。

<a id="r_affe2dba0634e0215579fb13d77016a8c"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#affe2dba0634e0215579fb13d77016a8c)。

<a id="r_a3343de57a24fa2ebdccf9411f388817d"></a>

```c
uint8_t role
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[role](#a3343de57a24fa2ebdccf9411f388817d)。

<a id="r_a7df28c9ddec607d5a84572bb421b7f5a"></a>

```c
bt_addr_le_t peer_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_addr](#a7df28c9ddec607d5a84572bb421b7f5a)。

<a id="r_a10a1cbf0e9e21bc127dc64adadd53773"></a>

```c
bt_addr_t local_rpa
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[local_rpa](#a10a1cbf0e9e21bc127dc64adadd53773)。

<a id="r_a014e8bf891684c4cd9e5ec53d986d412"></a>

```c
bt_addr_t peer_rpa
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[peer_rpa](#a014e8bf891684c4cd9e5ec53d986d412)。

<a id="r_a237b8313970cc63b7e57c0ce4913392e"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a237b8313970cc63b7e57c0ce4913392e)。

<a id="r_a3daa32ac19c4eda4a49bebb64f3145be"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#a3daa32ac19c4eda4a49bebb64f3145be)。

<a id="r_a2b2ac4890eb9604a3f5cd40f55c2c066"></a>

```c
uint16_t supv_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supv_timeout](#a2b2ac4890eb9604a3f5cd40f55c2c066)。

<a id="r_a7bb168061803d1122e8ee47dc8af3ae9"></a>

```c
uint8_t clock_accuracy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clock_accuracy](#a7bb168061803d1122e8ee47dc8af3ae9)。

<a id="r_a883ba3aed9aed00ec0ce425999d97180"></a>

```c
uint8_t adv_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adv_handle](#a883ba3aed9aed00ec0ce425999d97180)。

<a id="r_a81dca94a6f2a8ea3da7a5a316daa5941"></a>

```c
uint16_t sync_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sync_handle](#a81dca94a6f2a8ea3da7a5a316daa5941)。

## 255.2\_详细说明（Detailed Documentation）

<a id="a883ba3aed9aed00ec0ce425999d97180"></a>

### `adv_handle`

```c
uint8_t bt_hci_evt_le_enh_conn_complete_v2::adv_handle
```

<a id="a7bb168061803d1122e8ee47dc8af3ae9"></a>

### `clock_accuracy`

```c
uint8_t bt_hci_evt_le_enh_conn_complete_v2::clock_accuracy
```

<a id="affe2dba0634e0215579fb13d77016a8c"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_enh_conn_complete_v2::handle
```

<a id="a237b8313970cc63b7e57c0ce4913392e"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_enh_conn_complete_v2::interval
```

<a id="a3daa32ac19c4eda4a49bebb64f3145be"></a>

### `latency`

```c
uint16_t bt_hci_evt_le_enh_conn_complete_v2::latency
```

<a id="a10a1cbf0e9e21bc127dc64adadd53773"></a>

### `local_rpa`

```c
bt_addr_t bt_hci_evt_le_enh_conn_complete_v2::local_rpa
```

<a id="a7df28c9ddec607d5a84572bb421b7f5a"></a>

### `peer_addr`

```c
bt_addr_le_t bt_hci_evt_le_enh_conn_complete_v2::peer_addr
```

<a id="a014e8bf891684c4cd9e5ec53d986d412"></a>

### `peer_rpa`

```c
bt_addr_t bt_hci_evt_le_enh_conn_complete_v2::peer_rpa
```

<a id="a3343de57a24fa2ebdccf9411f388817d"></a>

### `role`

```c
uint8_t bt_hci_evt_le_enh_conn_complete_v2::role
```

<a id="ad72ba07d766135a94474a9d004da1a66"></a>

### `status`

```c
uint8_t bt_hci_evt_le_enh_conn_complete_v2::status
```

<a id="a2b2ac4890eb9604a3f5cd40f55c2c066"></a>

### `supv_timeout`

```c
uint16_t bt_hci_evt_le_enh_conn_complete_v2::supv_timeout
```

<a id="a81dca94a6f2a8ea3da7a5a316daa5941"></a>

### `sync_handle`

```c
uint16_t bt_hci_evt_le_enh_conn_complete_v2::sync_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 255.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P254_bt_hci_evt_le_enh_conn_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P256_bt_hci_evt_le_ext_advertising_info_结构体.md)
