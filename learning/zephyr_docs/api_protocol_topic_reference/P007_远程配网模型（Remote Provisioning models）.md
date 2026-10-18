---
id: learning.zephyr-docs.api-protocol-topic-reference.page-7
title: 远程配网模型（Remote Provisioning models）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_远程配网模型（Remote Provisioning models）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_rpr_2Eh"></a>

```c
file rpr.h
```

相关声明：[rpr.h](../api_file_runtime_reference/P057_zephyr__bluetooth__mesh__rpr.h_文件参考.md)。

蓝牙Mesh远程配网（Remote Provisioning）通用定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.2\_数据结构（Data Structures）

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

## 7.3\_宏定义（Macros）

<a id="r_ga94522cf0b3832b576100b787808474bd"></a>

```c
#define BT_MESH_RPR_UNPROV_HASH BIT(0)
```

相关声明：[BT_MESH_RPR_UNPROV_HASH](#ga94522cf0b3832b576100b787808474bd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

未配置设备（Unprovisioned Device）具有统一资源标识符哈希值（URI Hash Value）。

<a id="r_ga31bbb1483d5bdd10e0a9da0978bd90c0"></a>

```c
#define BT_MESH_RPR_UNPROV_ACTIVE BIT(1)
```

相关声明：[BT_MESH_RPR_UNPROV_ACTIVE](#ga31bbb1483d5bdd10e0a9da0978bd90c0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_gac33ea72f94eb986592941ca10b7884f1"></a>

```c
#define BT_MESH_RPR_UNPROV_FOUND BIT(2)
```

相关声明：[BT_MESH_RPR_UNPROV_FOUND](#gac33ea72f94eb986592941ca10b7884f1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_ga8121bae9a6158a5f2df4bc154237e05b"></a>

```c
#define BT_MESH_RPR_UNPROV_REPORTED BIT(3)
```

相关声明：[BT_MESH_RPR_UNPROV_REPORTED](#ga8121bae9a6158a5f2df4bc154237e05b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_gac1eebae68c05d9e59599d0601055790d"></a>

```c
#define BT_MESH_RPR_UNPROV_EXT BIT(4)
```

相关声明：[BT_MESH_RPR_UNPROV_EXT](#gac1eebae68c05d9e59599d0601055790d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_ga8349a9af764b3e502bf5ecd8bb0ce203"></a>

```c
#define BT_MESH_RPR_UNPROV_HAS_LINK BIT(5)
```

相关声明：[BT_MESH_RPR_UNPROV_HAS_LINK](#ga8349a9af764b3e502bf5ecd8bb0ce203)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_ga1dc95fc6baba79d9bc4007169fcfe55b"></a>

```c
#define BT_MESH_RPR_UNPROV_EXT_ADV_RXD BIT(6)
```

相关声明：[BT_MESH_RPR_UNPROV_EXT_ADV_RXD](#ga1dc95fc6baba79d9bc4007169fcfe55b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

内部使用（Internal）。

<a id="r_ga2b7e2636da150f5c5cb4e3bdee13c745"></a>

```c
#define BT_MESH_RPR_EXT_SCAN_TIME_MIN 1
```

相关声明：[BT_MESH_RPR_EXT_SCAN_TIME_MIN](#ga2b7e2636da150f5c5cb4e3bdee13c745)。

最短扩展扫描时长（Minimum Extended Scan Duration），单位为秒（Seconds）。

<a id="r_ga2a5241b2e87fec227740dd4f2de3a68a"></a>

```c
#define BT_MESH_RPR_EXT_SCAN_TIME_MAX 21
```

相关声明：[BT_MESH_RPR_EXT_SCAN_TIME_MAX](#ga2a5241b2e87fec227740dd4f2de3a68a)。

最长扩展扫描时长（Maximum Extended Scan Duration），单位为秒（Seconds）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.4\_枚举（Enumerations）

<a id="r_ga77d2f7158e7629dc54acafbf65e6af90"></a>

```c
enum bt_mesh_rpr_status { BT_MESH_RPR_SUCCESS , BT_MESH_RPR_ERR_SCANNING_CANNOT_START , BT_MESH_RPR_ERR_INVALID_STATE , BT_MESH_RPR_ERR_LIMITED_RESOURCES , BT_MESH_RPR_ERR_LINK_CANNOT_OPEN , BT_MESH_RPR_ERR_LINK_OPEN_FAILED , BT_MESH_RPR_ERR_LINK_CLOSED_BY_DEVICE , BT_MESH_RPR_ERR_LINK_CLOSED_BY_SERVER , BT_MESH_RPR_ERR_LINK_CLOSED_BY_CLIENT , BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_RECEIVE_PDU , BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_SEND_PDU , BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_DELIVER_PDU_REPORT }
```

相关声明：[bt_mesh_rpr_status](#ga77d2f7158e7629dc54acafbf65e6af90)、[BT_MESH_RPR_SUCCESS](#gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117)、[BT_MESH_RPR_ERR_SCANNING_CANNOT_START](#gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599)、[BT_MESH_RPR_ERR_INVALID_STATE](#gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26)、[BT_MESH_RPR_ERR_LIMITED_RESOURCES](#gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82)、[BT_MESH_RPR_ERR_LINK_CANNOT_OPEN](#gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3)、[BT_MESH_RPR_ERR_LINK_OPEN_FAILED](#gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4)、[BT_MESH_RPR_ERR_LINK_CLOSED_BY_DEVICE](#gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8)、[BT_MESH_RPR_ERR_LINK_CLOSED_BY_SERVER](#gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095)、[BT_MESH_RPR_ERR_LINK_CLOSED_BY_CLIENT](#gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3)、[BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_RECEIVE_PDU](#gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943)、[BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_SEND_PDU](#gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb)、[BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_DELIVER_PDU_REPORT](#gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4)。

<a id="r_gabdc6782290a2c1652156e3f932e65291"></a>

```c
enum bt_mesh_rpr_scan { BT_MESH_RPR_SCAN_IDLE , BT_MESH_RPR_SCAN_MULTI , BT_MESH_RPR_SCAN_SINGLE }
```

相关声明：[bt_mesh_rpr_scan](#gabdc6782290a2c1652156e3f932e65291)、[BT_MESH_RPR_SCAN_IDLE](#ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079)、[BT_MESH_RPR_SCAN_MULTI](#ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690)、[BT_MESH_RPR_SCAN_SINGLE](#ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd)。

<a id="r_gafef25a17e477638702ed742656b59573"></a>

```c
enum bt_mesh_rpr_node_refresh { BT_MESH_RPR_NODE_REFRESH_DEVKEY , BT_MESH_RPR_NODE_REFRESH_ADDR , BT_MESH_RPR_NODE_REFRESH_COMPOSITION }
```

相关声明：[bt_mesh_rpr_node_refresh](#gafef25a17e477638702ed742656b59573)、[BT_MESH_RPR_NODE_REFRESH_DEVKEY](#ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574)、[BT_MESH_RPR_NODE_REFRESH_ADDR](#ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf)、[BT_MESH_RPR_NODE_REFRESH_COMPOSITION](#ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6)。

<a id="r_ga0266611238d10f8e97f2b07156991f43"></a>

```c
enum bt_mesh_rpr_link_state { BT_MESH_RPR_LINK_IDLE , BT_MESH_RPR_LINK_OPENING , BT_MESH_RPR_LINK_ACTIVE , BT_MESH_RPR_LINK_SENDING , BT_MESH_RPR_LINK_CLOSING }
```

相关声明：[bt_mesh_rpr_link_state](#ga0266611238d10f8e97f2b07156991f43)、[BT_MESH_RPR_LINK_IDLE](#gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb)、[BT_MESH_RPR_LINK_OPENING](#gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9)、[BT_MESH_RPR_LINK_ACTIVE](#gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36)、[BT_MESH_RPR_LINK_SENDING](#gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7)、[BT_MESH_RPR_LINK_CLOSING](#gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494)。

## 7.5\_详细说明（Detailed Documentation）

<a id="ga2a5241b2e87fec227740dd4f2de3a68a"></a>

### `BT_MESH_RPR_EXT_SCAN_TIME_MAX`

```c
#define BT_MESH_RPR_EXT_SCAN_TIME_MAX 21
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

最长扩展扫描时长（Maximum Extended Scan Duration），单位为秒（Seconds）。

<a id="ga2b7e2636da150f5c5cb4e3bdee13c745"></a>

### `BT_MESH_RPR_EXT_SCAN_TIME_MIN`

```c
#define BT_MESH_RPR_EXT_SCAN_TIME_MIN 1
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

最短扩展扫描时长（Minimum Extended Scan Duration），单位为秒（Seconds）。

<a id="ga31bbb1483d5bdd10e0a9da0978bd90c0"></a>

### `BT_MESH_RPR_UNPROV_ACTIVE`

```c
#define BT_MESH_RPR_UNPROV_ACTIVE BIT(1)
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

内部使用（Internal）。

<a id="gac1eebae68c05d9e59599d0601055790d"></a>

### `BT_MESH_RPR_UNPROV_EXT`

```c
#define BT_MESH_RPR_UNPROV_EXT BIT(4)
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

内部使用（Internal）。

<a id="ga1dc95fc6baba79d9bc4007169fcfe55b"></a>

### `BT_MESH_RPR_UNPROV_EXT_ADV_RXD`

```c
#define BT_MESH_RPR_UNPROV_EXT_ADV_RXD BIT(6)
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

内部使用（Internal）。

<a id="gac33ea72f94eb986592941ca10b7884f1"></a>

### `BT_MESH_RPR_UNPROV_FOUND`

```c
#define BT_MESH_RPR_UNPROV_FOUND BIT(2)
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

内部使用（Internal）。

<a id="ga8349a9af764b3e502bf5ecd8bb0ce203"></a>

### `BT_MESH_RPR_UNPROV_HAS_LINK`

```c
#define BT_MESH_RPR_UNPROV_HAS_LINK BIT(5)
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

内部使用（Internal）。

<a id="ga94522cf0b3832b576100b787808474bd"></a>

### `BT_MESH_RPR_UNPROV_HASH`

```c
#define BT_MESH_RPR_UNPROV_HASH BIT(0)
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

未配置设备（Unprovisioned Device）具有统一资源标识符哈希值（URI Hash Value）。

<a id="ga8121bae9a6158a5f2df4bc154237e05b"></a>

### `BT_MESH_RPR_UNPROV_REPORTED`

```c
#define BT_MESH_RPR_UNPROV_REPORTED BIT(3)
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

内部使用（Internal）。

<a id="ga0266611238d10f8e97f2b07156991f43"></a>

### `bt_mesh_rpr_link_state`

```c
enum bt_mesh_rpr_link_state
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_RPR_LINK_IDLE` |  |
| `BT_MESH_RPR_LINK_OPENING` |  |
| `BT_MESH_RPR_LINK_ACTIVE` |  |
| `BT_MESH_RPR_LINK_SENDING` |  |
| `BT_MESH_RPR_LINK_CLOSING` |  |

<a id="gafef25a17e477638702ed742656b59573"></a>

### `bt_mesh_rpr_node_refresh`

```c
enum bt_mesh_rpr_node_refresh
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_RPR_NODE_REFRESH_DEVKEY` | 更改设备密钥（Device key）。 |
| `BT_MESH_RPR_NODE_REFRESH_ADDR` | 更改设备密钥和地址。设备组成可能变化。 |
| `BT_MESH_RPR_NODE_REFRESH_COMPOSITION` | 更改设备密钥和组成。 |

<a id="gabdc6782290a2c1652156e3f932e65291"></a>

### `bt_mesh_rpr_scan`

```c
enum bt_mesh_rpr_scan
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_RPR_SCAN_IDLE` |  |
| `BT_MESH_RPR_SCAN_MULTI` |  |
| `BT_MESH_RPR_SCAN_SINGLE` |  |

<a id="ga77d2f7158e7629dc54acafbf65e6af90"></a>

### `bt_mesh_rpr_status`

```c
enum bt_mesh_rpr_status
```

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_RPR_SUCCESS` |  |
| `BT_MESH_RPR_ERR_SCANNING_CANNOT_START` |  |
| `BT_MESH_RPR_ERR_INVALID_STATE` |  |
| `BT_MESH_RPR_ERR_LIMITED_RESOURCES` |  |
| `BT_MESH_RPR_ERR_LINK_CANNOT_OPEN` |  |
| `BT_MESH_RPR_ERR_LINK_OPEN_FAILED` |  |
| `BT_MESH_RPR_ERR_LINK_CLOSED_BY_DEVICE` |  |
| `BT_MESH_RPR_ERR_LINK_CLOSED_BY_SERVER` |  |
| `BT_MESH_RPR_ERR_LINK_CLOSED_BY_CLIENT` |  |
| `BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_RECEIVE_PDU` |  |
| `BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_SEND_PDU` |  |
| `BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_DELIVER_PDU_REPORT` |  |


## 7.6\_原页交叉引用（Cross References）

- [rpr.h](../api_file_runtime_reference/P057_zephyr__bluetooth__mesh__rpr.h_文件参考.md)
- [bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)
- [bt_mesh_rpr_unprov](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md)
- [bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb"></a>
<a id="gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9"></a>
<a id="gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36"></a>
<a id="gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7"></a>
<a id="gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494"></a>
<a id="ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574"></a>
<a id="ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf"></a>
<a id="ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6"></a>
<a id="ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079"></a>
<a id="ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690"></a>
<a id="ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb"></a>
<a id="gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4"></a>

---

[上一章](P006_蓝牙 Mesh 按需私有 GATT 代理客户端（On-Demand Private GATT Proxy Client）.md) · [返回大纲](大纲.md) · [下一章](P008_统计（Statistic）.md)
