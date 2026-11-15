---
id: learning.zephyr-docs.api-file-runtime-reference.page-57
title: zephyr__bluetooth__mesh__rpr.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_zephyr\_\_bluetooth\_\_mesh\_\_rpr.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh远程配网（Remote Provisioning）通用定义的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/bluetooth/mesh/main.h>
```

查看此文件的源码。

蓝牙Mesh远程配网（Remote Provisioning）通用定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 57.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Frpr_5Fnode"></a>

```c
struct bt_mesh_rpr_node
```

相关声明：[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)。

从整个Mesh网络角度看到的远程配网参与者（Remote Provisioning Actor）。

<a id="r_bt_5Fmesh_5Frpr_5Funprov"></a>

```c
struct bt_mesh_rpr_unprov
```

相关声明：[bt_mesh_rpr_unprov](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md)。

未配网设备（Unprovisioned Device）。

<a id="r_bt_5Fmesh_5Frpr_5Flink"></a>

```c
struct bt_mesh_rpr_link
```

相关声明：[bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)。

远程配网链路（Remote Provisioning Link）的状态。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 57.2\_宏定义（Macros）

<a id="r_ga94522cf0b3832b576100b787808474bd"></a>

```c
#define BT_MESH_RPR_UNPROV_HASH BIT(0)
```

相关声明：[BT_MESH_RPR_UNPROV_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga94522cf0b3832b576100b787808474bd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

未配置设备（Unprovisioned Device）具有统一资源标识符哈希值（URI Hash Value）。

<a id="r_ga31bbb1483d5bdd10e0a9da0978bd90c0"></a>

```c
#define BT_MESH_RPR_UNPROV_ACTIVE BIT(1)
```

相关声明：[BT_MESH_RPR_UNPROV_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga31bbb1483d5bdd10e0a9da0978bd90c0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_gac33ea72f94eb986592941ca10b7884f1"></a>

```c
#define BT_MESH_RPR_UNPROV_FOUND BIT(2)
```

相关声明：[BT_MESH_RPR_UNPROV_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gac33ea72f94eb986592941ca10b7884f1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_ga8121bae9a6158a5f2df4bc154237e05b"></a>

```c
#define BT_MESH_RPR_UNPROV_REPORTED BIT(3)
```

相关声明：[BT_MESH_RPR_UNPROV_REPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga8121bae9a6158a5f2df4bc154237e05b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_gac1eebae68c05d9e59599d0601055790d"></a>

```c
#define BT_MESH_RPR_UNPROV_EXT BIT(4)
```

相关声明：[BT_MESH_RPR_UNPROV_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gac1eebae68c05d9e59599d0601055790d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_ga8349a9af764b3e502bf5ecd8bb0ce203"></a>

```c
#define BT_MESH_RPR_UNPROV_HAS_LINK BIT(5)
```

相关声明：[BT_MESH_RPR_UNPROV_HAS_LINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga8349a9af764b3e502bf5ecd8bb0ce203)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_ga1dc95fc6baba79d9bc4007169fcfe55b"></a>

```c
#define BT_MESH_RPR_UNPROV_EXT_ADV_RXD BIT(6)
```

相关声明：[BT_MESH_RPR_UNPROV_EXT_ADV_RXD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga1dc95fc6baba79d9bc4007169fcfe55b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_ga2b7e2636da150f5c5cb4e3bdee13c745"></a>

```c
#define BT_MESH_RPR_EXT_SCAN_TIME_MIN 1
```

相关声明：[BT_MESH_RPR_EXT_SCAN_TIME_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga2b7e2636da150f5c5cb4e3bdee13c745)。

最短扩展扫描时长（Minimum Extended Scan Duration），单位为秒（Seconds）。

<a id="r_ga2a5241b2e87fec227740dd4f2de3a68a"></a>

```c
#define BT_MESH_RPR_EXT_SCAN_TIME_MAX 21
```

相关声明：[BT_MESH_RPR_EXT_SCAN_TIME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga2a5241b2e87fec227740dd4f2de3a68a)。

最长扩展扫描时长（Maximum Extended Scan Duration），单位为秒（Seconds）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 57.3\_枚举（Enumerations）

<a id="r_ga77d2f7158e7629dc54acafbf65e6af90"></a>

```c
enum bt_mesh_rpr_status { BT_MESH_RPR_SUCCESS , BT_MESH_RPR_ERR_SCANNING_CANNOT_START , BT_MESH_RPR_ERR_INVALID_STATE , BT_MESH_RPR_ERR_LIMITED_RESOURCES , BT_MESH_RPR_ERR_LINK_CANNOT_OPEN , BT_MESH_RPR_ERR_LINK_OPEN_FAILED , BT_MESH_RPR_ERR_LINK_CLOSED_BY_DEVICE , BT_MESH_RPR_ERR_LINK_CLOSED_BY_SERVER , BT_MESH_RPR_ERR_LINK_CLOSED_BY_CLIENT , BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_RECEIVE_PDU , BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_SEND_PDU , BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_DELIVER_PDU_REPORT }
```

相关声明：[bt_mesh_rpr_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga77d2f7158e7629dc54acafbf65e6af90)、[BT_MESH_RPR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117)、[BT_MESH_RPR_ERR_SCANNING_CANNOT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599)、[BT_MESH_RPR_ERR_INVALID_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26)、[BT_MESH_RPR_ERR_LIMITED_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82)、[BT_MESH_RPR_ERR_LINK_CANNOT_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3)、[BT_MESH_RPR_ERR_LINK_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4)、[BT_MESH_RPR_ERR_LINK_CLOSED_BY_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8)、[BT_MESH_RPR_ERR_LINK_CLOSED_BY_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095)、[BT_MESH_RPR_ERR_LINK_CLOSED_BY_CLIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3)、[BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_RECEIVE_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943)、[BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_SEND_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb)、[BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_DELIVER_PDU_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4)。

<a id="r_gabdc6782290a2c1652156e3f932e65291"></a>

```c
enum bt_mesh_rpr_scan { BT_MESH_RPR_SCAN_IDLE , BT_MESH_RPR_SCAN_MULTI , BT_MESH_RPR_SCAN_SINGLE }
```

相关声明：[bt_mesh_rpr_scan](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gabdc6782290a2c1652156e3f932e65291)、[BT_MESH_RPR_SCAN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079)、[BT_MESH_RPR_SCAN_MULTI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690)、[BT_MESH_RPR_SCAN_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd)。

<a id="r_gafef25a17e477638702ed742656b59573"></a>

```c
enum bt_mesh_rpr_node_refresh { BT_MESH_RPR_NODE_REFRESH_DEVKEY , BT_MESH_RPR_NODE_REFRESH_ADDR , BT_MESH_RPR_NODE_REFRESH_COMPOSITION }
```

相关声明：[bt_mesh_rpr_node_refresh](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gafef25a17e477638702ed742656b59573)、[BT_MESH_RPR_NODE_REFRESH_DEVKEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574)、[BT_MESH_RPR_NODE_REFRESH_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf)、[BT_MESH_RPR_NODE_REFRESH_COMPOSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6)。

<a id="r_ga0266611238d10f8e97f2b07156991f43"></a>

```c
enum bt_mesh_rpr_link_state { BT_MESH_RPR_LINK_IDLE , BT_MESH_RPR_LINK_OPENING , BT_MESH_RPR_LINK_ACTIVE , BT_MESH_RPR_LINK_SENDING , BT_MESH_RPR_LINK_CLOSING }
```

相关声明：[bt_mesh_rpr_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga0266611238d10f8e97f2b07156991f43)、[BT_MESH_RPR_LINK_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb)、[BT_MESH_RPR_LINK_OPENING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9)、[BT_MESH_RPR_LINK_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36)、[BT_MESH_RPR_LINK_SENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7)、[BT_MESH_RPR_LINK_CLOSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494)。


## 57.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/bluetooth/mesh/main.h](../api_source_supplement_reference/P102_main.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P731_rpr.h_源码浏览.md)
- [bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)
- [bt_mesh_rpr_unprov](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md)
- [bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)
- [BT_MESH_RPR_UNPROV_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga94522cf0b3832b576100b787808474bd)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_MESH_RPR_UNPROV_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga31bbb1483d5bdd10e0a9da0978bd90c0)
- [BT_MESH_RPR_UNPROV_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gac33ea72f94eb986592941ca10b7884f1)
- [BT_MESH_RPR_UNPROV_REPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga8121bae9a6158a5f2df4bc154237e05b)
- [BT_MESH_RPR_UNPROV_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gac1eebae68c05d9e59599d0601055790d)
- [BT_MESH_RPR_UNPROV_HAS_LINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga8349a9af764b3e502bf5ecd8bb0ce203)
- [BT_MESH_RPR_UNPROV_EXT_ADV_RXD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga1dc95fc6baba79d9bc4007169fcfe55b)
- [BT_MESH_RPR_EXT_SCAN_TIME_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga2b7e2636da150f5c5cb4e3bdee13c745)
- [BT_MESH_RPR_EXT_SCAN_TIME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga2a5241b2e87fec227740dd4f2de3a68a)
- [bt_mesh_rpr_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga77d2f7158e7629dc54acafbf65e6af90)
- [BT_MESH_RPR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117)
- [BT_MESH_RPR_ERR_SCANNING_CANNOT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599)
- [BT_MESH_RPR_ERR_INVALID_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26)
- [BT_MESH_RPR_ERR_LIMITED_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82)
- [BT_MESH_RPR_ERR_LINK_CANNOT_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3)
- [BT_MESH_RPR_ERR_LINK_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4)
- [BT_MESH_RPR_ERR_LINK_CLOSED_BY_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8)
- [BT_MESH_RPR_ERR_LINK_CLOSED_BY_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095)
- [BT_MESH_RPR_ERR_LINK_CLOSED_BY_CLIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3)
- [BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_RECEIVE_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943)
- [BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_SEND_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb)
- [BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_DELIVER_PDU_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4)
- [bt_mesh_rpr_scan](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gabdc6782290a2c1652156e3f932e65291)
- [BT_MESH_RPR_SCAN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079)
- [BT_MESH_RPR_SCAN_MULTI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690)
- [BT_MESH_RPR_SCAN_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd)
- [bt_mesh_rpr_node_refresh](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gafef25a17e477638702ed742656b59573)
- [BT_MESH_RPR_NODE_REFRESH_DEVKEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574)
- [BT_MESH_RPR_NODE_REFRESH_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf)
- [BT_MESH_RPR_NODE_REFRESH_COMPOSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6)
- [bt_mesh_rpr_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga0266611238d10f8e97f2b07156991f43)
- [BT_MESH_RPR_LINK_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb)
- [BT_MESH_RPR_LINK_OPENING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9)
- [BT_MESH_RPR_LINK_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36)
- [BT_MESH_RPR_LINK_SENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7)
- [BT_MESH_RPR_LINK_CLOSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494)

<a id="header-details"></a>

---

[上一章](P056_zephyr__dt-bindings__clock__renesas_rzg_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P058_zephyr__dt-bindings__pinctrl__rts5817_pinctrl.h_文件参考.md)
