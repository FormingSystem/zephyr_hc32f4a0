---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-286
title: bt_hci_evt_mesh_scanning_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__mesh__scanning__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第286章\_bt\_hci\_evt\_mesh\_scanning\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__mesh__scanning__report.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 286.1\_数据成员（Data Fields）

<a id="r_a5daf719f2f5ec6e47f7a93d47d5c2b17"></a>

```c
uint8_t num_reports
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_reports](#a5daf719f2f5ec6e47f7a93d47d5c2b17)。

<a id="r_aa63b838e431b358bf1a3495998dfd952"></a>

```c
struct bt_hci_evt_mesh_scan_report reports [0]
```

相关声明：[bt_hci_evt_mesh_scan_report](P285_bt_hci_evt_mesh_scan_report_结构体.md)、[reports](#aa63b838e431b358bf1a3495998dfd952)。

## 286.2\_详细说明（Detailed Documentation）

<a id="a5daf719f2f5ec6e47f7a93d47d5c2b17"></a>

### `num_reports`

```c
uint8_t bt_hci_evt_mesh_scanning_report::num_reports
```

<a id="aa63b838e431b358bf1a3495998dfd952"></a>

### `reports`

```c
struct bt_hci_evt_mesh_scan_report bt_hci_evt_mesh_scanning_report::reports[0]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 286.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_evt_mesh_scan_report](P285_bt_hci_evt_mesh_scan_report_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P285_bt_hci_evt_mesh_scan_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P287_bt_hci_evt_mode_change_结构体.md)
