---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-94
title: bt_mesh_rpr_scan_status_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__scan__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_bt\_mesh\_rpr\_scan\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__scan__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

扫描状态（Scan Status）的响应。

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

<a id="details"></a>

扫描状态（Scan Status）的响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 94.1\_数据成员（Data Fields）

<a id="r_a2e2023bc7dcb31ae8716203b726f7ebb"></a>

```c
enum bt_mesh_rpr_status status
```

相关声明：[bt_mesh_rpr_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga77d2f7158e7629dc54acafbf65e6af90)、[status](#a2e2023bc7dcb31ae8716203b726f7ebb)。

当前扫描状态码（Current scan status）。

<a id="r_ac9e5f2e4db9fc9b04dddd2687a712ff8"></a>

```c
enum bt_mesh_rpr_scan scan
```

相关声明：[bt_mesh_rpr_scan](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gabdc6782290a2c1652156e3f932e65291)、[scan](#ac9e5f2e4db9fc9b04dddd2687a712ff8)。

当前扫描状态（Current scan state）。

<a id="r_ac7fc9a15127dc1eae44d2ec610efd5be"></a>

```c
uint8_t max_devs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_devs](#ac7fc9a15127dc1eae44d2ec610efd5be)。

当前扫描最多报告的设备数量（Max devices to report）。

<a id="r_a8d062579fb074ded769bf367e0287052"></a>

```c
uint8_t timeout
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[timeout](#a8d062579fb074ded769bf367e0287052)。

扫描剩余时间（Scan time remaining），单位为秒。

## 94.2\_详细说明（Detailed Documentation）

<a id="ac7fc9a15127dc1eae44d2ec610efd5be"></a>

### `max_devs`

```c
uint8_t bt_mesh_rpr_scan_status::max_devs
```

当前扫描最多报告的设备数量（Max devices to report）。

<a id="ac9e5f2e4db9fc9b04dddd2687a712ff8"></a>

### `scan`

```c
enum bt_mesh_rpr_scan bt_mesh_rpr_scan_status::scan
```

当前扫描状态（Current scan state）。

<a id="a2e2023bc7dcb31ae8716203b726f7ebb"></a>

### `status`

```c
enum bt_mesh_rpr_status bt_mesh_rpr_scan_status::status
```

当前扫描状态码（Current scan status）。

<a id="a8d062579fb074ded769bf367e0287052"></a>

### `timeout`

```c
uint8_t bt_mesh_rpr_scan_status::timeout
```

扫描剩余时间（Scan time remaining），单位为秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/rpr_cli.h`

## 94.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/rpr_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h_source.html)
- [bt_mesh_rpr_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga77d2f7158e7629dc54acafbf65e6af90)
- [bt_mesh_rpr_scan](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gabdc6782290a2c1652156e3f932e65291)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P093_bt_mesh_rpr_node_结构体.md) · [返回大纲](大纲.md) · [下一章](P095_bt_mesh_rpr_unprov_结构体.md)
