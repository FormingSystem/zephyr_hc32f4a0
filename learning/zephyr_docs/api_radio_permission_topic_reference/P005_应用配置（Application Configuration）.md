---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-5
title: 应用配置（Application Configuration）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__app.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_应用配置（Application Configuration）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__app.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

应用配置（Application Configuration）

<a id="details"></a>

应用配置（Application Configuration）

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.1\_函数（Functions）

<a id="r_ga0110ef750489af49a156a259c5a95c9b"></a>

```c
uint8_t bt_mesh_app_key_add (uint16_t app_idx, uint16_t net_idx, const uint8_t key[16])
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_app_key_add](#ga0110ef750489af49a156a259c5a95c9b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

添加应用密钥（Application Key）。

<a id="r_ga5ae73ef766f0e1c38c0414c0a34e4053"></a>

```c
uint8_t bt_mesh_app_key_update (uint16_t app_idx, uint16_t net_idx, const uint8_t key[16])
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_app_key_update](#ga5ae73ef766f0e1c38c0414c0a34e4053)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新应用密钥（Application Key）。

<a id="r_gaa0e80a19c14d47808fc11459bf5ea2eb"></a>

```c
uint8_t bt_mesh_app_key_del (uint16_t app_idx, uint16_t net_idx)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_app_key_del](#gaa0e80a19c14d47808fc11459bf5ea2eb)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除应用密钥（Application Key）。

<a id="r_ga42c46a936e589460225a1fa69598a1ac"></a>

```c
bool bt_mesh_app_key_exists (uint16_t app_idx)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_app_key_exists](#ga42c46a936e589460225a1fa69598a1ac)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查是否已知某个应用密钥（Application Key）。

<a id="r_gad7a949a0a814f6c9a26816c076d8b92a"></a>

```c
ssize_t bt_mesh_app_keys_get (uint16_t net_idx, uint16_t app_idxs[], size_t max, off_t skip)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[bt_mesh_app_keys_get](#gad7a949a0a814f6c9a26816c076d8b92a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

获取所有已知应用密钥索引（Application Key Indexes）的列表。

## 5.2\_详细说明（Detailed Documentation）

<a id="ga0110ef750489af49a156a259c5a95c9b"></a>

### `bt_mesh_app_key_add()`

```c
uint8_t bt_mesh_app_key_add ( uint16_t app_idx, uint16_t net_idx, const uint8_t key[16] )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

添加应用密钥（Application Key）。

将给定索引的应用（Application）添加到已知应用列表，使节点能够发送和接收由该应用密钥加密的模型消息（Model Messages）。

每个应用（Application）绑定到特定子网（Subnet）。添加应用之前，节点必须已知其绑定的子网。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_idx` | 应用索引（Application Index）。 |
| `net_idx` | 该应用绑定的网络索引（Network Index）。 |
| `key` | 应用密钥值（Application Key Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 成功添加应用（Application）。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |
| `STATUS_INSUFF_RESOURCES` | 没有空间存储此应用（Application）。 |
| `STATUS_INVALID_BINDING` | 此 AppIdx 已绑定到其他子网（Subnet）。 |
| `STATUS_IDX_ALREADY_STORED` | 此 AppIdx 已以不同的密钥值存储。 |
| `STATUS_CANNOT_SET` | 由于某种原因无法设置应用密钥（Application Key）。 |

<a id="gaa0e80a19c14d47808fc11459bf5ea2eb"></a>

### `bt_mesh_app_key_del()`

```c
uint8_t bt_mesh_app_key_del ( uint16_t app_idx, uint16_t net_idx )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

删除应用密钥（Application Key）。

绑定到此应用的所有模型都会移除此绑定；使用此应用发布的所有模型都会停止发布（Publishing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_idx` | 应用索引（Application Index）。 |
| `net_idx` | 网络索引（Network Index）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 成功删除应用密钥（Application Key）。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |
| `STATUS_INVALID_BINDING` | 此 AppIdx 未绑定到指定 NetIdx。 |

<a id="ga42c46a936e589460225a1fa69598a1ac"></a>

### `bt_mesh_app_key_exists()`

```c
bool bt_mesh_app_key_exists ( uint16_t app_idx)
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

检查是否已知某个应用密钥（Application Key）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_idx` | 应用索引（Application Index）。 |

**返回（Returns）**：返回值（Returns）：已知此应用（Application）时返回 true，否则返回 false。

<a id="ga5ae73ef766f0e1c38c0414c0a34e4053"></a>

### `bt_mesh_app_key_update()`

```c
uint8_t bt_mesh_app_key_update ( uint16_t app_idx, uint16_t net_idx, const uint8_t key[16] )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

更新应用密钥（Application Key）。

作为绑定子网密钥刷新过程（Key Refresh Procedure）的一部分，使用第二个应用密钥更新应用。在子网进入密钥刷新阶段 2 之前，节点继续使用旧应用密钥发送，但接收时接受新旧两种密钥。子网进入密钥刷新阶段 3 后，删除旧应用密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_idx` | 应用索引（Application Index）。 |
| `net_idx` | 应用绑定的网络索引（Network Index）；传 BT_MESH_KEY_ANY 可跳过绑定检查。 |
| `key` | 新密钥值（New Key Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `STATUS_SUCCESS` | 成功更新应用密钥（Application Key）。 |
| `STATUS_INVALID_NETKEY` | 未知的 NetIdx。 |
| `STATUS_INVALID_BINDING` | 此 AppIdx 未绑定到指定 NetIdx。 |
| `STATUS_CANNOT_UPDATE` | 由于某种原因无法更新应用密钥（Application Key）。 |
| `STATUS_IDX_ALREADY_STORED` | 此 AppIdx 已用不同的密钥值更新。 |

**说明（Note）**：注意（Note）：仅在所绑定子网处于密钥刷新阶段 1（Key Refresh Phase 1）时，才可更新应用密钥。

<a id="gad7a949a0a814f6c9a26816c076d8b92a"></a>

### `bt_mesh_app_keys_get()`

```c
ssize_t bt_mesh_app_keys_get ( uint16_t net_idx, uint16_t app_idxs[], size_t max, off_t skip )
```

```c
#include <zephyr/bluetooth/mesh/cfg.h>
```

获取所有已知应用密钥索引（Application Key Indexes）的列表。

在 app_idxs 数组中构建给定网络索引的全部应用索引（Application Indexes）列表。若数组无法容纳所有绑定应用，则填满所有可用条目并返回 -ENOMEM。此时，可通过以下调用读取列表接下来的 max 个条目：

原始示例（Example）：

```c
bt_mesh_app_keys_get(net_idx, list, max, max);
```

两次调用此函数之间若应用密钥列表发生变化，可能改变列表条目的顺序和数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 要获取其应用的网络索引（Network Index）；传 BT_MESH_KEY_ANY 获取全部应用。 |
| `app_idxs` | 待填充的数组（Array）。 |
| `max` | 返回索引的最大数量。 |
| `skip` | 要跳过的索引数量，用于对列表分批处理（Batched Processing）。 |

**返回（Returns）**：返回值（Returns）：添加到 app_idxs 数组的索引数量；已知应用数量超过 max 参数时返回 -ENOMEM。


## 5.3\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [zephyr/bluetooth/mesh/cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg_8h.html)
- [BT_MESH_KEY_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga7718cce0713be98a08420c7eab1b40ee)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__bt__mesh__cfg__app_html_gad7a949a0a814f6c9a26816c076d8b92a"></a>
<a id="aminmax_8h_html_affe776513b24d84b39af8ab0930fef7f"></a>

---

[上一章](P004_蓝牙 HID 主机（Host）.md) · [返回大纲](大纲.md) · [下一章](P006_固件更新客户端模型（原文：Firmware Uppdate Client model）.md)
