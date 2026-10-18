---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-63
title: bt_hci_cp_le_read_peer_rpa_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__read__peer__rpa.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_bt\_hci\_cp\_le\_read\_peer\_rpa\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__read__peer__rpa.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_ab0c70a1dbe5152b1fc926b90ec3387b3"></a>

```c
bt_addr_le_t peer_id_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_id_addr](#ab0c70a1dbe5152b1fc926b90ec3387b3)。

## 63.2\_详细说明（Detailed Documentation）

<a id="ab0c70a1dbe5152b1fc926b90ec3387b3"></a>

### `peer_id_addr`

```c
bt_addr_le_t bt_hci_cp_le_read_peer_rpa::peer_id_addr
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_bt_hci_cp_le_read_local_rpa_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_bt_hci_cp_le_read_phy_结构体.md)
