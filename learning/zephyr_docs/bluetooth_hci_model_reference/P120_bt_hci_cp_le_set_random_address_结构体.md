---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-120
title: bt_hci_cp_le_set_random_address_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__random__address.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第120章\_bt\_hci\_cp\_le\_set\_random\_address\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__random__address.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 120.1\_数据成员（Data Fields）

<a id="r_a919ef74473f4f86d00595ec8606789d0"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a919ef74473f4f86d00595ec8606789d0)。

## 120.2\_详细说明（Detailed Documentation）

<a id="a919ef74473f4f86d00595ec8606789d0"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_le_set_random_address::bdaddr
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 120.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P119_bt_hci_cp_le_set_procedure_parameters_结构体.md) · [返回大纲](大纲.md) · [下一章](P121_bt_hci_cp_le_set_rpa_timeout_结构体.md)
