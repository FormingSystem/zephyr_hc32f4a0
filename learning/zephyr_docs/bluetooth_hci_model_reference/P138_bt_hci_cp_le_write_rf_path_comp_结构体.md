---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-138
title: bt_hci_cp_le_write_rf_path_comp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__write__rf__path__comp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第138章\_bt\_hci\_cp\_le\_write\_rf\_path\_comp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__write__rf__path__comp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 138.1\_数据成员（Data Fields）

<a id="r_a5f99b131f3fba91706bdc8277c1abba1"></a>

```c
int16_t tx_path_comp
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[tx_path_comp](#a5f99b131f3fba91706bdc8277c1abba1)。

<a id="r_a11aad5607e444cf55dd5878f1f6f9436"></a>

```c
int16_t rx_path_comp
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rx_path_comp](#a11aad5607e444cf55dd5878f1f6f9436)。

## 138.2\_详细说明（Detailed Documentation）

<a id="a11aad5607e444cf55dd5878f1f6f9436"></a>

### `rx_path_comp`

```c
int16_t bt_hci_cp_le_write_rf_path_comp::rx_path_comp
```

<a id="a5f99b131f3fba91706bdc8277c1abba1"></a>

### `tx_path_comp`

```c
int16_t bt_hci_cp_le_write_rf_path_comp::tx_path_comp
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 138.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P137_bt_hci_cp_le_write_default_data_len_结构体.md) · [返回大纲](大纲.md) · [下一章](P139_bt_hci_cp_link_key_neg_reply_结构体.md)
