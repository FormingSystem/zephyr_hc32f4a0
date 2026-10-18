---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-253
title: bt_hci_evt_le_direct_adv_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__direct__adv__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第253章\_bt\_hci\_evt\_le\_direct\_adv\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__direct__adv__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 253.1\_数据成员（Data Fields）

<a id="r_ae8d1f96739c8fda8827d1c0521f00f94"></a>

```c
uint8_t num_reports
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_reports](#ae8d1f96739c8fda8827d1c0521f00f94)。

<a id="r_a82800d58d4c3ed1fca49b6575bd8f957"></a>

```c
struct bt_hci_evt_le_direct_adv_info direct_adv_info [0]
```

相关声明：[bt_hci_evt_le_direct_adv_info](P252_bt_hci_evt_le_direct_adv_info_结构体.md)、[direct_adv_info](#a82800d58d4c3ed1fca49b6575bd8f957)。

## 253.2\_详细说明（Detailed Documentation）

<a id="a82800d58d4c3ed1fca49b6575bd8f957"></a>

### `direct_adv_info`

```c
struct bt_hci_evt_le_direct_adv_info bt_hci_evt_le_direct_adv_report::direct_adv_info[0]
```

<a id="ae8d1f96739c8fda8827d1c0521f00f94"></a>

### `num_reports`

```c
uint8_t bt_hci_evt_le_direct_adv_report::num_reports
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 253.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_evt_le_direct_adv_info](P252_bt_hci_evt_le_direct_adv_info_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P252_bt_hci_evt_le_direct_adv_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P254_bt_hci_evt_le_enh_conn_complete_结构体.md)
