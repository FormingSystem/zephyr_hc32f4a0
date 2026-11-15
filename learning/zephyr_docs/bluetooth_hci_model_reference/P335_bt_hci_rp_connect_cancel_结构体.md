---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-335
title: bt_hci_rp_connect_cancel_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__connect__cancel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第335章\_bt\_hci\_rp\_connect\_cancel\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__connect__cancel.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 335.1\_数据成员（Data Fields）

<a id="r_a05d0c9e4163bc62a57dba8618294eb65"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a05d0c9e4163bc62a57dba8618294eb65)。

<a id="r_a0ccfcbd294aa067879ab8d7a41bc41c9"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a0ccfcbd294aa067879ab8d7a41bc41c9)。

## 335.2\_详细说明（Detailed Documentation）

<a id="a0ccfcbd294aa067879ab8d7a41bc41c9"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_rp_connect_cancel::bdaddr
```

<a id="a05d0c9e4163bc62a57dba8618294eb65"></a>

### `status`

```c
uint8_t bt_hci_rp_connect_cancel::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 335.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P334_bt_hci_rp_configure_data_path_结构体.md) · [返回大纲](大纲.md) · [下一章](P336_bt_hci_rp_le_big_terminate_sync_结构体.md)
