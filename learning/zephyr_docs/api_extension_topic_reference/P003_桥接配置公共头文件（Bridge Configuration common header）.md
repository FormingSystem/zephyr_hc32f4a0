---
id: learning.zephyr-docs.api-extension-topic-reference.page-3
title: 桥接配置公共头文件（Bridge Configuration common header）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_桥接配置公共头文件（Bridge Configuration common header）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_brg_5Fcfg_2Eh"></a>

```c
file brg_cfg.h
```

相关声明：[brg_cfg.h](../api_file_supplement_reference/P011_zephyr__bluetooth__mesh__brg_cfg.h_文件参考.md)。

蓝牙Mesh桥接配置（Bridge Configuration）通用定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fbrg_5Fcfg_5Ftable_5Fentry"></a>

```c
struct bt_mesh_brg_cfg_table_entry
```

相关声明：[bt_mesh_brg_cfg_table_entry](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md)。

桥接表（Bridging Table）中某个条目对应的桥接表状态条目。

<a id="r_bt_5Fmesh_5Fbrg_5Fcfg_5Ftable_5Fstatus"></a>

```c
struct bt_mesh_brg_cfg_table_status
```

相关声明：[bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)。

桥接表状态（Bridging Table Status）的响应。

<a id="r_bt_5Fmesh_5Fbrg_5Fcfg_5Ffilter_5Fnetkey"></a>

```c
struct bt_mesh_brg_cfg_filter_netkey
```

相关声明：[bt_mesh_brg_cfg_filter_netkey](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)。

用于筛选桥接表（Bridging Table）中的网络密钥索引（NetKey Index）对集合。

<a id="r_bt_5Fmesh_5Fbrg_5Fcfg_5Fsubnets_5Flist"></a>

```c
struct bt_mesh_brg_cfg_subnets_list
```

相关声明：[bt_mesh_brg_cfg_subnets_list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md)。

已桥接子网列表（Bridged Subnets List）的响应。

<a id="r_bt_5Fmesh_5Fbrg_5Fcfg_5Ftable_5Flist"></a>

```c
struct bt_mesh_brg_cfg_table_list
```

相关声明：[bt_mesh_brg_cfg_table_list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md)。

桥接表列表（Bridging Table List）的响应。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.3\_宏定义（Macros）

<a id="r_ga054c4efc3fbe9ee7f05020b8c93129ed"></a>

```c
#define BT_MESH_BRG_CFG_DIR_ONEWAY 1
```

相关声明：[BT_MESH_BRG_CFG_DIR_ONEWAY](#ga054c4efc3fbe9ee7f05020b8c93129ed)。

<a id="r_ga7787b27b46160aa0943c4c70a4b8ab4b"></a>

```c
#define BT_MESH_BRG_CFG_DIR_TWOWAY 2
```

相关声明：[BT_MESH_BRG_CFG_DIR_TWOWAY](#ga7787b27b46160aa0943c4c70a4b8ab4b)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.4\_枚举（Enumerations）

<a id="r_ga7bddcbe2b1196df6a1c80d8c213866f9"></a>

```c
enum bt_mesh_brg_cfg_state { BT_MESH_BRG_CFG_DISABLED , BT_MESH_BRG_CFG_ENABLED }
```

相关声明：[bt_mesh_brg_cfg_state](#ga7bddcbe2b1196df6a1c80d8c213866f9)、[BT_MESH_BRG_CFG_DISABLED](#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4)、[BT_MESH_BRG_CFG_ENABLED](#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2)。

子网桥接状态（Subnet Bridge States）。

## 3.5\_详细说明（Detailed Documentation）

<a id="ga054c4efc3fbe9ee7f05020b8c93129ed"></a>

### `BT_MESH_BRG_CFG_DIR_ONEWAY`

```c
#define BT_MESH_BRG_CFG_DIR_ONEWAY 1
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg.h>
```

<a id="ga7787b27b46160aa0943c4c70a4b8ab4b"></a>

### `BT_MESH_BRG_CFG_DIR_TWOWAY`

```c
#define BT_MESH_BRG_CFG_DIR_TWOWAY 2
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg.h>
```

<a id="ga7bddcbe2b1196df6a1c80d8c213866f9"></a>

### `bt_mesh_brg_cfg_state`

```c
enum bt_mesh_brg_cfg_state
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg.h>
```

子网桥接状态（Subnet Bridge States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_BRG_CFG_DISABLED` | 子网桥接功能（Subnet Bridge Functionality）已禁用。 |
| `BT_MESH_BRG_CFG_ENABLED` | 子网桥接状态功能（Subnet Bridge State Functionality）已启用。 |


## 3.6\_原页交叉引用（Cross References）

- [brg_cfg.h](../api_file_supplement_reference/P011_zephyr__bluetooth__mesh__brg_cfg.h_文件参考.md)
- [bt_mesh_brg_cfg_table_entry](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md)
- [bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)
- [bt_mesh_brg_cfg_filter_netkey](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)
- [bt_mesh_brg_cfg_subnets_list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md)
- [bt_mesh_brg_cfg_table_list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4"></a>
<a id="gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2"></a>

---

[上一章](P002_蓝牙控制器（Bluetooth Controller）.md) · [返回大纲](大纲.md) · [下一章](P004_固件分发服务器模型（Firmware Distribution Server model）.md)
