---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-2
title: 代理（Proxy）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_代理（Proxy）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

代理（Proxy）

<a id="details"></a>

代理（Proxy）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fproxy_5Fcb"></a>

```c
struct bt_mesh_proxy_cb
```

相关声明：[bt_mesh_proxy_cb](../bluetooth_mesh_model_reference/P089_bt_mesh_proxy_cb_结构体.md)。

代理功能（Proxy Feature）的回调。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga325b71c3d7ed69952bf760c0288b28ef"></a>

```c
#define BT_MESH_PROXY_CB_DEFINE(_name)
```

相关声明：[BT_MESH_PROXY_CB_DEFINE](#ga325b71c3d7ed69952bf760c0288b28ef)。

为代理（Proxy）事件注册回调结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_ga7fb3c76f1be6943dd4a18f26e8dd18e7"></a>

```c
int bt_mesh_proxy_identity_enable (void)
```

相关声明：[bt_mesh_proxy_identity_enable](#ga7fb3c76f1be6943dd4a18f26e8dd18e7)。

启用使用节点身份（Node Identity）的广播。

<a id="r_gaecd529a9fd0df83b3d775d32885802f1"></a>

```c
int bt_mesh_proxy_private_identity_enable (void)
```

相关声明：[bt_mesh_proxy_private_identity_enable](#gaecd529a9fd0df83b3d775d32885802f1)。

启用使用私有节点身份（Private Node Identity）的广播。

<a id="r_ga07d4edf80bdbc39f626f66720035c98b"></a>

```c
int bt_mesh_proxy_connect (uint16_t net_idx)
```

相关声明：[bt_mesh_proxy_connect](#ga07d4edf80bdbc39f626f66720035c98b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

允许代理客户端（Proxy Client）自动连接到网络。

<a id="r_gaa9978d460b31412c96c6c1685729ec4f"></a>

```c
int bt_mesh_proxy_disconnect (uint16_t net_idx)
```

相关声明：[bt_mesh_proxy_disconnect](#gaa9978d460b31412c96c6c1685729ec4f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

禁止代理客户端自动连接到网络。

<a id="r_ga9a72515992af4f93a34a6c1aaf69d8df"></a>

```c
int bt_mesh_proxy_solicit (uint16_t net_idx)
```

相关声明：[bt_mesh_proxy_solicit](#ga9a72515992af4f93a34a6c1aaf69d8df)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

调度请求协议数据单元（Solicitation PDUs）的广播。

## 2.4\_详细说明（Detailed Documentation）

<a id="ga325b71c3d7ed69952bf760c0288b28ef"></a>

### `BT_MESH_PROXY_CB_DEFINE`

```c
#define BT_MESH_PROXY_CB_DEFINE ( _name)
```

```c
#include <zephyr/bluetooth/mesh/proxy.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(                                  \
        bt_mesh_proxy_cb, _CONCAT(bt_mesh_proxy_cb_, _name))
```

为代理（Proxy）事件注册回调结构体。

注册包含回调函数的结构体，这些函数会在各种代理（Proxy）事件发生时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 回调结构体名称（Callback Structure Name）。 |

<a id="ga07d4edf80bdbc39f626f66720035c98b"></a>

### `bt_mesh_proxy_connect()`

```c
int bt_mesh_proxy_connect ( uint16_t net_idx)
```

```c
#include <zephyr/bluetooth/mesh/proxy.h>
```

允许代理客户端（Proxy Client）自动连接到网络。

此 API 允许代理客户端（proxy client）自动连接指定网络。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络密钥索引（Network Key Index）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaa9978d460b31412c96c6c1685729ec4f"></a>

### `bt_mesh_proxy_disconnect()`

```c
int bt_mesh_proxy_disconnect ( uint16_t net_idx)
```

```c
#include <zephyr/bluetooth/mesh/proxy.h>
```

禁止代理客户端自动连接到网络。

此 API 禁止代理客户端连接指定网络。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络密钥索引（Network Key Index）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga7fb3c76f1be6943dd4a18f26e8dd18e7"></a>

### `bt_mesh_proxy_identity_enable()`

```c
int bt_mesh_proxy_identity_enable ( void )
```

```c
#include <zephyr/bluetooth/mesh/proxy.h>
```

启用使用节点身份（Node Identity）的广播。

此 API 要求已启用 GATT 代理（GATT Proxy）支持。调用后，每个子网将在接下来的 60 秒内使用节点身份（Node Identity）进行广播。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaecd529a9fd0df83b3d775d32885802f1"></a>

### `bt_mesh_proxy_private_identity_enable()`

```c
int bt_mesh_proxy_private_identity_enable ( void )
```

```c
#include <zephyr/bluetooth/mesh/proxy.h>
```

启用使用私有节点身份（Private Node Identity）的广播。

此 API 要求已启用 GATT 代理（GATT Proxy）支持。调用后，每个子网将在接下来的 60 秒内使用私有节点身份（Private Node Identity）进行广播。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga9a72515992af4f93a34a6c1aaf69d8df"></a>

### `bt_mesh_proxy_solicit()`

```c
int bt_mesh_proxy_solicit ( uint16_t net_idx)
```

```c
#include <zephyr/bluetooth/mesh/proxy.h>
```

调度请求协议数据单元（Solicitation PDUs）的广播。

调用后，设备将调度请求协议数据单元（Solicitation PDUs）的广播，持续时间为 `adv_int * (CONFIG_BT_MESH_SOL_ADV_XMIT + 1)`。Bluetooth v5.0 及更高版本的 `adv_int` 为 20 ms，其他版本为 100 ms。

已广播的 Solicitation PDU 数量达到 `0xFFFFFF` 后，将不再启动这些广播，直到节点重新完成配网（reprovisioned）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 网络密钥索引（Network Key Index）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。


## 2.5\_原页交叉引用（Cross References）

- [bt_mesh_proxy_cb](../bluetooth_mesh_model_reference/P089_bt_mesh_proxy_cb_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/bluetooth/mesh/proxy.h](../api_file_management_reference/P041_zephyr__bluetooth__mesh__proxy.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructbt__mesh__proxy__cb_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_BBRAM 驱动后端 API（Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P003_设备多路复用器（Devmux）.md)
