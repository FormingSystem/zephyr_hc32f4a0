---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-5
title: 子网配置（Subnet Configuration）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_子网配置（Subnet Configuration）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__subnet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

子网配置（Subnet Configuration）

<a id="details"></a>

子网配置（Subnet Configuration）

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.1\_函数（Functions）

<a id="r_ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f"></a>

```c
uint8_t bt_mesh_subnet_add (uint16_t net_idx, const uint8_t key[16])
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_add](#ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加子网（Subnet）。

<a id="r_ga47236f48940303be27fa6af4797424c2"></a>

```c
uint8_t bt_mesh_subnet_update (uint16_t net_idx, const uint8_t key[16])
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_update](#ga47236f48940303be27fa6af4797424c2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新给定子网（Subnet）。

<a id="r_gaec9d827d5f026b473f3ac88988d3c842"></a>

```c
uint8_t bt_mesh_subnet_del (uint16_t net_idx)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_del](#gaec9d827d5f026b473f3ac88988d3c842)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除子网（Subnet）。

<a id="r_gad48780acaae085350a8b48d033717bfa"></a>

```c
bool bt_mesh_subnet_exists (uint16_t net_idx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_subnet_exists](#gad48780acaae085350a8b48d033717bfa)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查子网（Subnet）是否已知。

<a id="r_gaef15af43e74e3c71590c63c5f1e3ea55"></a>

```c
uint8_t bt_mesh_subnet_kr_phase_set (uint16_t net_idx, uint8_t *phase)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_kr_phase_set](#gaef15af43e74e3c71590c63c5f1e3ea55)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置子网的密钥刷新阶段（Key Refresh Phase）。

<a id="r_gad251907892150649f3f1ae6b4112cd84"></a>

```c
uint8_t bt_mesh_subnet_kr_phase_get (uint16_t net_idx, uint8_t *phase)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_kr_phase_get](#gad251907892150649f3f1ae6b4112cd84)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取子网的密钥刷新阶段（Key Refresh Phase）。

<a id="r_ga59bf9f022665edc0ad03267e4bd16632"></a>

```c
uint8_t bt_mesh_subnet_node_id_set (uint16_t net_idx, enum bt_mesh_feat_state node_id)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_node_id_set](#ga59bf9f022665edc0ad03267e4bd16632)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

设置子网的节点身份（Node Identity）状态。

<a id="r_ga683d1f9abe82649a774b3d53dcaced8e"></a>

```c
uint8_t bt_mesh_subnet_node_id_get (uint16_t net_idx, enum bt_mesh_feat_state *node_id)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_node_id_get](#ga683d1f9abe82649a774b3d53dcaced8e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

获取子网的节点身份（Node Identity）状态。

<a id="r_ga5aa3e7f6b64e1b8b98f9737606d5d1ec"></a>

```c
uint8_t bt_mesh_subnet_priv_node_id_set (uint16_t net_idx, enum bt_mesh_feat_state priv_node_id)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_priv_node_id_set](#ga5aa3e7f6b64e1b8b98f9737606d5d1ec)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

设置子网的私有节点身份（Private Node Identity）状态。

<a id="r_ga555b4a7127869355fdf6040b8d14f999"></a>

```c
uint8_t bt_mesh_subnet_priv_node_id_get (uint16_t net_idx, enum bt_mesh_feat_state *priv_node_id)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_subnet_priv_node_id_get](#ga555b4a7127869355fdf6040b8d14f999)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)。

获取子网的私有节点身份（Private Node Identity）状态。

<a id="r_ga0fd04bff5423a36b013089a4ba351d67"></a>

```c
ssize_t bt_mesh_subnets_get (uint16_t net_idxs[], size_t max, off_t skip)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_mesh_subnets_get](#ga0fd04bff5423a36b013089a4ba351d67)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

获取所有已知子网索引（Subnet Indexes）的列表。

## 5.2\_详细说明（Detailed Documentation）

<a id="ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f"></a>

### `bt_mesh_subnet_add()`

```c
uint8_t bt_mesh_subnet_add ( uint16_t net_idx, const uint8_t key[16] )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

添加子网（Subnet）。

将具有给定网络索引（Network Index）和网络密钥（Network Key）的子网添加到已知子网（Subnets）列表。本节点会处理在该子网上发送的所有消息，也可以在该子网上发送和接收网络信标（Network Beacons）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |
| `key` | 子网的根网络密钥（Root Network Key），其他所有密钥均由它派生。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 子网（Subnet）添加成功。 |
| `STATUS_INSUFF_RESOURCES` | 没有空间容纳此子网（Subnet）。 |
| `STATUS_UNSPECIFIED` | 由于某种原因无法创建子网（Subnet）。 |

<a id="gaec9d827d5f026b473f3ac88988d3c842"></a>

### `bt_mesh_subnet_del()`

```c
uint8_t bt_mesh_subnet_del ( uint16_t net_idx)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

删除子网（Subnet）。

从节点移除给定网络索引（Network Index）的子网。节点将停止在该子网上发送网络信标（Network Beacons），也不能再处理该子网上的消息。

绑定到此子网（Subnet）的所有应用（Applications）也会被删除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 子网（Subnet）已删除。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |

<a id="gad48780acaae085350a8b48d033717bfa"></a>

### `bt_mesh_subnet_exists()`

```c
bool bt_mesh_subnet_exists ( uint16_t net_idx)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

检查子网（Subnet）是否已知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |

返回（Returns）：存在给定索引的子网（Subnet）时为 true，否则为 false。

<a id="gad251907892150649f3f1ae6b4112cd84"></a>

### `bt_mesh_subnet_kr_phase_get()`

```c
uint8_t bt_mesh_subnet_kr_phase_get ( uint16_t net_idx, uint8_t * phase )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取子网的密钥刷新阶段（Key Refresh Phase）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |
| `phase` | 指向待填充的密钥刷新变量（Key Refresh Variable）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 成功填充 phase 变量。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |

<a id="gaef15af43e74e3c71590c63c5f1e3ea55"></a>

### `bt_mesh_subnet_kr_phase_set()`

```c
uint8_t bt_mesh_subnet_kr_phase_set ( uint16_t net_idx, uint8_t * phase )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

设置子网的密钥刷新阶段（Key Refresh Phase）。

通过 bt_mesh_subnet_update 更新子网密钥，可启动密钥刷新过程（Key Refresh Procedure），使子网进入密钥刷新阶段 1（Phase 1）。所有节点收到新子网密钥后，可通过本函数激活阶段 2（Phase 2），开始使用新网络密钥发送。最后，将密钥刷新阶段设为 3，即可撤销旧密钥：这会从节点移除旧密钥，并使子网恢复使用新密钥集的正常单密钥运行（Single-key Operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |
| `phase` | 指向新密钥刷新阶段（Key Refresh Phase）的指针；更新后返回实际的密钥刷新阶段。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 成功更改子网的密钥刷新阶段（Key Refresh Phase）。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |
| `STATUS_CANNOT_UPDATE` | 给定的阶段切换（Phase Change）无效。 |

<a id="ga683d1f9abe82649a774b3d53dcaced8e"></a>

### `bt_mesh_subnet_node_id_get()`

```c
uint8_t bt_mesh_subnet_node_id_get ( uint16_t net_idx, enum bt_mesh_feat_state * node_id )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取子网的节点身份（Node Identity）状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |
| `node_id` | 待填充的节点身份变量（Node Identity Variable）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 成功填充 node_id 变量。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |

<a id="ga59bf9f022665edc0ad03267e4bd16632"></a>

### `bt_mesh_subnet_node_id_set()`

```c
uint8_t bt_mesh_subnet_node_id_set ( uint16_t net_idx, enum bt_mesh_feat_state node_id )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

设置子网的节点身份（Node Identity）状态。

子网的节点身份状态（Node Identity State）决定它是否广播可连接的节点身份信标（Node Identity Beacons），供代理客户端（Proxy Clients）连接。节点身份信标启动后运行 60 秒，或运行到被停止为止。

此函数的用途与 bt_mesh_proxy_identity_enable 相同，但仅作用于单个子网（Subnet）。

必须通过 CONFIG_BT_MESH_GATT_PROXY 启用 GATT 代理支持（GATT Proxy Support）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |
| `node_id` | 新的节点身份状态（Node Identity State），必须为 BT_MESH_FEATURE_ENABLED 或 BT_MESH_FEATURE_DISABLED。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 成功设置子网的节点身份状态（Node Identity State）。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |
| `STATUS_FEAT_NOT_SUPP` | 不支持节点身份特性（Node Identity Feature）。 |
| `STATUS_CANNOT_SET` | 无法设置节点身份状态（Node Identity State）。 |

<a id="ga555b4a7127869355fdf6040b8d14f999"></a>

### `bt_mesh_subnet_priv_node_id_get()`

```c
uint8_t bt_mesh_subnet_priv_node_id_get ( uint16_t net_idx, enum bt_mesh_feat_state * priv_node_id )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取子网的私有节点身份（Private Node Identity）状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |
| `priv_node_id` | 待填充的私有节点身份变量（Private Node Identity Variable）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 成功填充 priv_node_id 变量。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |

<a id="ga5aa3e7f6b64e1b8b98f9737606d5d1ec"></a>

### `bt_mesh_subnet_priv_node_id_set()`

```c
uint8_t bt_mesh_subnet_priv_node_id_set ( uint16_t net_idx, enum bt_mesh_feat_state priv_node_id )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

设置子网的私有节点身份（Private Node Identity）状态。

子网的私有节点身份状态（Private Node Identity State）决定它是否广播可连接的私有节点身份信标（Private Node Identity Beacons），供代理客户端（Proxy Clients）连接。节点身份信标启动后运行 60 秒，或运行到被停止为止。

只有所有子网均未启用普通节点身份（Node Identity）时，才能启用私有节点身份（Private Node Identity）。

必须分别通过 CONFIG_BT_MESH_GATT_PROXY 和 CONFIG_BT_MESH_PRIV_BEACONS 启用 GATT 代理（GATT Proxy）与私有信标（Private Beacon）支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |
| `priv_node_id` | 新的私有节点身份状态（Private Node Identity State），必须为 BT_MESH_FEATURE_ENABLED 或 BT_MESH_FEATURE_DISABLED。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 成功设置子网的私有节点身份状态（Private Node Identity State）。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |
| `STATUS_FEAT_NOT_SUPP` | 不支持私有节点身份特性（Private Node Identity Feature）。 |
| `STATUS_TEMP_STATE_CHG_FAIL` | 无法启用私有节点身份状态（Private Node Identity State），因为节点身份状态（Node Identity State）已启用。 |
| `STATUS_CANNOT_SET` | 无法设置私有节点身份状态（Private Node Identity State）。 |

<a id="ga47236f48940303be27fa6af4797424c2"></a>

### `bt_mesh_subnet_update()`

```c
uint8_t bt_mesh_subnet_update ( uint16_t net_idx, const uint8_t key[16] )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

更新给定子网（Subnet）。

通过添加第二组加密密钥（Encryption Keys）启动此子网的密钥刷新过程（Key Refresh Procedure）。子网继续使用旧密钥发送，但可以使用两组密钥接收消息，直到进入密钥刷新阶段 2。

这使网络配置器（Network Configurator）能够替换整个网络的旧网络密钥和应用密钥，从而有效地移除未获发新密钥的所有节点的访问权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络索引（Network Index）。 |
| `key` | 子网的新根网络密钥（Root Network Key）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 已为子网更新第二个密钥（Second Key）。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |
| `STATUS_IDX_ALREADY_STORED` | 密钥值与当前密钥相同。 |
| `STATUS_CANNOT_UPDATE` | 由于某种原因无法更新子网（Subnet）。 |

<a id="ga0fd04bff5423a36b013089a4ba351d67"></a>

### `bt_mesh_subnets_get()`

```c
ssize_t bt_mesh_subnets_get ( uint16_t net_idxs[], size_t max, off_t skip )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取所有已知子网索引（Subnet Indexes）的列表。

在 net_idxs 数组中构建所有已知子网索引（Subnet Indexes）的列表。如果 net_idxs 数组小于已知子网列表，函数会填满所有可用条目并返回 -ENOMEM。此时，可通过以下调用读取列表中接下来的 max 个条目：

原始示例（Example）：

```c
bt_mesh_subnets_get(list, max, max);
```

注意：两次调用此函数之间对子网列表（Subnet List）的任何更改，都可能改变列表中条目的顺序和数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idxs` | 待填充的数组（Array）。 |
| `max` | 返回索引的最大数量。 |
| `skip` | 要跳过的索引数量，用于对列表分批处理（Batched Processing）。 |

返回（Returns）：添加到 net_idxs 数组的索引数量；已知子网数量超过 max 参数时返回 -ENOMEM。


## 5.3\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_feat_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#ga0a3557a71597885a31cf209c6b83cedb)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [zephyr/bluetooth/mesh/cfg.h](../api_file_display_chat_reference/P003_zephyr__bluetooth__mesh__cfg.h_文件参考.md)
- [bt_mesh_proxy_identity_enable](../api_auxiliary_topic_reference/P002_代理（Proxy）.md#ga7fb3c76f1be6943dd4a18f26e8dd18e7)
- [CONFIG_BT_MESH_GATT_PROXY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_PROXY)
- [BT_MESH_FEATURE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275)
- [BT_MESH_FEATURE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg.html#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729)
- [CONFIG_BT_MESH_PRIV_BEACONS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PRIV_BEACONS)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__bt__mesh__cfg__subnet_html_ga0fd04bff5423a36b013089a4ba351d67"></a>
<a id="aminmax_8h_html_affe776513b24d84b39af8ab0930fef7f"></a>

---

[上一章](P004_助听接入服务（Hearing Access Service，HAS）.md) · [返回大纲](大纲.md) · [下一章](P006_清理辅助接口（Cleanup Helper Interface）.md)
