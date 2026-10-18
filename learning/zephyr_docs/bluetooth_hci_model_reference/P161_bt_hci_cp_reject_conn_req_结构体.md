---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-161
title: bt_hci_cp_reject_conn_req_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__reject__conn__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第161章\_bt\_hci\_cp\_reject\_conn\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__reject__conn__req.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 161.1\_数据成员（Data Fields）

<a id="r_a9a1cb4173367c6f018fbd30a47c590b4"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a9a1cb4173367c6f018fbd30a47c590b4)。

<a id="r_a1c2e234d6d00296bc01962b95e849df0"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#a1c2e234d6d00296bc01962b95e849df0)。

## 161.2\_详细说明（Detailed Documentation）

<a id="a9a1cb4173367c6f018fbd30a47c590b4"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_reject_conn_req::bdaddr
```

<a id="a1c2e234d6d00296bc01962b95e849df0"></a>

### `reason`

```c
uint8_t bt_hci_cp_reject_conn_req::reason
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 161.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P160_bt_hci_cp_read_tx_power_level_结构体.md) · [返回大纲](大纲.md) · [下一章](P162_bt_hci_cp_remote_name_cancel_结构体.md)
