---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-62
title: bt_hci_cp_le_read_local_rpa_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__read__local__rpa.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_bt\_hci\_cp\_le\_read\_local\_rpa\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__read__local__rpa.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_aa96cd60066003e4a7a1f482fb81557f8"></a>

```c
bt_addr_le_t peer_id_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_id_addr](#aa96cd60066003e4a7a1f482fb81557f8)。

## 62.2\_详细说明（Detailed Documentation）

<a id="aa96cd60066003e4a7a1f482fb81557f8"></a>

### `peer_id_addr`

```c
bt_addr_le_t bt_hci_cp_le_read_local_rpa::peer_id_addr
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_bt_hci_cp_le_read_iso_tx_sync_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_bt_hci_cp_le_read_peer_rpa_结构体.md)
