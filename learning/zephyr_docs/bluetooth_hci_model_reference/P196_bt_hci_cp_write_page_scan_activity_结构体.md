---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-196
title: bt_hci_cp_write_page_scan_activity_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__page__scan__activity.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第196章\_bt\_hci\_cp\_write\_page\_scan\_activity\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__page__scan__activity.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

写入寻呼扫描活动参数（Write Page Scan Activity）的 HCI 命令参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

写入寻呼扫描活动参数（Write Page Scan Activity）的 HCI 命令参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 196.1\_数据成员（Data Fields）

<a id="r_a9b73713d2960e78a7d6cf1a96c611495"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a9b73713d2960e78a7d6cf1a96c611495)。

寻呼扫描间隔（Page Scan Interval），单位为 0.625 ms。

<a id="r_a8047c7b908154b23985c95a1d792007a"></a>

```c
uint16_t window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[window](#a8047c7b908154b23985c95a1d792007a)。

寻呼扫描窗口（Page Scan Window），单位为 0.625 ms。

## 196.2\_详细说明（Detailed Documentation）

<a id="a9b73713d2960e78a7d6cf1a96c611495"></a>

### `interval`

```c
uint16_t bt_hci_cp_write_page_scan_activity::interval
```

寻呼扫描间隔（Page Scan Interval），单位为 0.625 ms。

<a id="a8047c7b908154b23985c95a1d792007a"></a>

### `window`

```c
uint16_t bt_hci_cp_write_page_scan_activity::window
```

寻呼扫描窗口（Page Scan Window），单位为 0.625 ms。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 196.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P195_bt_hci_cp_write_link_supervision_timeout_结构体.md) · [返回大纲](大纲.md) · [下一章](P197_bt_hci_cp_write_page_scan_type_结构体.md)
