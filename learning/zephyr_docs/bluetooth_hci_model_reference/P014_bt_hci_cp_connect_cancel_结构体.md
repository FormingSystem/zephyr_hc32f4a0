---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-14
title: bt_hci_cp_connect_cancel_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__connect__cancel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_bt\_hci\_cp\_connect\_cancel\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__connect__cancel.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a2adaf1b708689525e44e9a9572f5f357"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a2adaf1b708689525e44e9a9572f5f357)。

## 14.2\_详细说明（Detailed Documentation）

<a id="a2adaf1b708689525e44e9a9572f5f357"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_connect_cancel::bdaddr
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_bt_hci_cp_connect_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_bt_hci_cp_disconnect_结构体.md)
