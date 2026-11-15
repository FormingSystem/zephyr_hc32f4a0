---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-369
title: bt_hci_rp_le_read_peer_rpa_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__peer__rpa.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第369章\_bt\_hci\_rp\_le\_read\_peer\_rpa\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__peer__rpa.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 369.1\_数据成员（Data Fields）

<a id="r_a9c8c799e8c9fbb9f64865e55cdb1f9ef"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a9c8c799e8c9fbb9f64865e55cdb1f9ef)。

<a id="r_a4eeee179819865ba5d5171d9bd33e5e9"></a>

```c
bt_addr_t peer_rpa
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[peer_rpa](#a4eeee179819865ba5d5171d9bd33e5e9)。

## 369.2\_详细说明（Detailed Documentation）

<a id="a4eeee179819865ba5d5171d9bd33e5e9"></a>

### `peer_rpa`

```c
bt_addr_t bt_hci_rp_le_read_peer_rpa::peer_rpa
```

<a id="a9c8c799e8c9fbb9f64865e55cdb1f9ef"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_peer_rpa::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 369.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P368_bt_hci_rp_le_read_num_adv_sets_结构体.md) · [返回大纲](大纲.md) · [下一章](P370_bt_hci_rp_le_read_per_adv_list_size_结构体.md)
