---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-220
title: bt_hci_evt_io_capa_req_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__io__capa__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第220章\_bt\_hci\_evt\_io\_capa\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__io__capa__req.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 220.1\_数据成员（Data Fields）

<a id="r_a52412f7bd8f8dea391904b9f2444b50a"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a52412f7bd8f8dea391904b9f2444b50a)。

## 220.2\_详细说明（Detailed Documentation）

<a id="a52412f7bd8f8dea391904b9f2444b50a"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_evt_io_capa_req::bdaddr
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 220.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md) · [返回大纲](大纲.md) · [下一章](P221_bt_hci_evt_io_capa_resp_结构体.md)
