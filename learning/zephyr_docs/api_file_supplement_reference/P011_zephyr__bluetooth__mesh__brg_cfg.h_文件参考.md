---
id: learning.zephyr-docs.api-file-supplement-reference.page-11
title: zephyr__bluetooth__mesh__brg_cfg.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_bluetooth\_\_mesh\_\_brg\_cfg.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh桥接配置（Bridge Configuration）通用定义的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
```

查看此文件的源码。

蓝牙Mesh桥接配置（Bridge Configuration）通用定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

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

## 11.2\_宏定义（Macros）

<a id="r_ga054c4efc3fbe9ee7f05020b8c93129ed"></a>

```c
#define BT_MESH_BRG_CFG_DIR_ONEWAY 1
```

相关声明：[BT_MESH_BRG_CFG_DIR_ONEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#ga054c4efc3fbe9ee7f05020b8c93129ed)。

<a id="r_ga7787b27b46160aa0943c4c70a4b8ab4b"></a>

```c
#define BT_MESH_BRG_CFG_DIR_TWOWAY 2
```

相关声明：[BT_MESH_BRG_CFG_DIR_TWOWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#ga7787b27b46160aa0943c4c70a4b8ab4b)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.3\_枚举（Enumerations）

<a id="r_ga7bddcbe2b1196df6a1c80d8c213866f9"></a>

```c
enum bt_mesh_brg_cfg_state { BT_MESH_BRG_CFG_DISABLED , BT_MESH_BRG_CFG_ENABLED }
```

相关声明：[bt_mesh_brg_cfg_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#ga7bddcbe2b1196df6a1c80d8c213866f9)、[BT_MESH_BRG_CFG_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4)、[BT_MESH_BRG_CFG_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2)。

子网桥接状态（Subnet Bridge States）。


## 11.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h_source.html)
- [bt_mesh_brg_cfg_table_entry](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md)
- [bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)
- [bt_mesh_brg_cfg_filter_netkey](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)
- [bt_mesh_brg_cfg_subnets_list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md)
- [bt_mesh_brg_cfg_table_list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md)
- [BT_MESH_BRG_CFG_DIR_ONEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#ga054c4efc3fbe9ee7f05020b8c93129ed)
- [BT_MESH_BRG_CFG_DIR_TWOWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#ga7787b27b46160aa0943c4c70a4b8ab4b)
- [bt_mesh_brg_cfg_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#ga7bddcbe2b1196df6a1c80d8c213866f9)
- [BT_MESH_BRG_CFG_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4)
- [BT_MESH_BRG_CFG_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg.html#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2)

<a id="header-details"></a>

---

[上一章](P010_zephyr__bluetooth__controller.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__bluetooth__mesh__brg_cfg_srv.h_文件参考.md)
