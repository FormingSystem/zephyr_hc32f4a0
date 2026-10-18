---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-274
title: bt_hci_evt_le_phy_update_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__phy__update__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第274章\_bt\_hci\_evt\_le\_phy\_update\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__phy__update__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 274.1\_数据成员（Data Fields）

<a id="r_a927a9e6982b29ecd4c3972b19a9bcdc2"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a927a9e6982b29ecd4c3972b19a9bcdc2)。

<a id="r_a70f472edef3b25fb23490ea6dcce9d43"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a70f472edef3b25fb23490ea6dcce9d43)。

<a id="r_ad184e10b7af71582db64ec5d3a66cff9"></a>

```c
uint8_t tx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_phy](#ad184e10b7af71582db64ec5d3a66cff9)。

<a id="r_ad792ffec08aa8e383009e2e353a03fcd"></a>

```c
uint8_t rx_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_phy](#ad792ffec08aa8e383009e2e353a03fcd)。

## 274.2\_详细说明（Detailed Documentation）

<a id="a70f472edef3b25fb23490ea6dcce9d43"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_phy_update_complete::handle
```

<a id="ad792ffec08aa8e383009e2e353a03fcd"></a>

### `rx_phy`

```c
uint8_t bt_hci_evt_le_phy_update_complete::rx_phy
```

<a id="a927a9e6982b29ecd4c3972b19a9bcdc2"></a>

### `status`

```c
uint8_t bt_hci_evt_le_phy_update_complete::status
```

<a id="ad184e10b7af71582db64ec5d3a66cff9"></a>

### `tx_phy`

```c
uint8_t bt_hci_evt_le_phy_update_complete::tx_phy
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 274.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md)
