---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-191
title: bt_hci_cp_write_inquiry_scan_activity_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__inquiry__scan__activity.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第191章\_bt\_hci\_cp\_write\_inquiry\_scan\_activity\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__write__inquiry__scan__activity.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

写入查询扫描活动参数（Write Inquiry Scan Activity）的 HCI 命令参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

写入查询扫描活动参数（Write Inquiry Scan Activity）的 HCI 命令参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 191.1\_数据成员（Data Fields）

<a id="r_affe95468faed405a95073b5ba811a053"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#affe95468faed405a95073b5ba811a053)。

查询扫描间隔（Inquiry Scan Interval），单位为 0.625 ms。

<a id="r_aca01d404676b965f2a03ae16080b8fae"></a>

```c
uint16_t window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[window](#aca01d404676b965f2a03ae16080b8fae)。

查询扫描窗口（Inquiry Scan Window），单位为 0.625 ms。

## 191.2\_详细说明（Detailed Documentation）

<a id="affe95468faed405a95073b5ba811a053"></a>

### `interval`

```c
uint16_t bt_hci_cp_write_inquiry_scan_activity::interval
```

查询扫描间隔（Inquiry Scan Interval），单位为 0.625 ms。

<a id="aca01d404676b965f2a03ae16080b8fae"></a>

### `window`

```c
uint16_t bt_hci_cp_write_inquiry_scan_activity::window
```

查询扫描窗口（Inquiry Scan Window），单位为 0.625 ms。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 191.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P190_bt_hci_cp_write_inquiry_mode_结构体.md) · [返回大纲](大纲.md) · [下一章](P192_bt_hci_cp_write_inquiry_scan_type_结构体.md)
