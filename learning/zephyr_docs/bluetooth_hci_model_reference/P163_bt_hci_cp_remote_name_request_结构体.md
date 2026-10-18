---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-163
title: bt_hci_cp_remote_name_request_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__remote__name__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第163章\_bt\_hci\_cp\_remote\_name\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__remote__name__request.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 163.1\_数据成员（Data Fields）

<a id="r_a5093f7bb70fa36f4948039d02d594e27"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a5093f7bb70fa36f4948039d02d594e27)。

<a id="r_aed0aea58ca6f5dc15220083d377cbf5c"></a>

```c
uint8_t pscan_rep_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pscan_rep_mode](#aed0aea58ca6f5dc15220083d377cbf5c)。

<a id="r_ab1883aa2b08d89f9c3190f338808a43c"></a>

```c
uint8_t reserved
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#ab1883aa2b08d89f9c3190f338808a43c)。

<a id="r_a5d7ea30052f8e4e2b3564659ca187c48"></a>

```c
uint16_t clock_offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[clock_offset](#a5d7ea30052f8e4e2b3564659ca187c48)。

## 163.2\_详细说明（Detailed Documentation）

<a id="a5093f7bb70fa36f4948039d02d594e27"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_remote_name_request::bdaddr
```

<a id="a5d7ea30052f8e4e2b3564659ca187c48"></a>

### `clock_offset`

```c
uint16_t bt_hci_cp_remote_name_request::clock_offset
```

<a id="aed0aea58ca6f5dc15220083d377cbf5c"></a>

### `pscan_rep_mode`

```c
uint8_t bt_hci_cp_remote_name_request::pscan_rep_mode
```

<a id="ab1883aa2b08d89f9c3190f338808a43c"></a>

### `reserved`

```c
uint8_t bt_hci_cp_remote_name_request::reserved
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 163.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P162_bt_hci_cp_remote_name_cancel_结构体.md) · [返回大纲](大纲.md) · [下一章](P164_bt_hci_cp_set_conn_encrypt_结构体.md)
