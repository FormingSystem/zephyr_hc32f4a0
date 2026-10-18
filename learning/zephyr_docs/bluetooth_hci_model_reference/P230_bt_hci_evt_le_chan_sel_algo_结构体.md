---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-230
title: bt_hci_evt_le_chan_sel_algo_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__chan__sel__algo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第230章\_bt\_hci\_evt\_le\_chan\_sel\_algo\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__chan__sel__algo.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 230.1\_数据成员（Data Fields）

<a id="r_a16393279e08073dad549e111e610c8e8"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a16393279e08073dad549e111e610c8e8)。

<a id="r_a976a62e81b094a59ce42cb6ad3ce45ac"></a>

```c
uint8_t chan_sel_algo
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[chan_sel_algo](#a976a62e81b094a59ce42cb6ad3ce45ac)。

## 230.2\_详细说明（Detailed Documentation）

<a id="a976a62e81b094a59ce42cb6ad3ce45ac"></a>

### `chan_sel_algo`

```c
uint8_t bt_hci_evt_le_chan_sel_algo::chan_sel_algo
```

<a id="a16393279e08073dad549e111e610c8e8"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_chan_sel_algo::handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 230.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P229_bt_hci_evt_le_biginfo_adv_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P231_bt_hci_evt_le_cis_established_结构体.md)
