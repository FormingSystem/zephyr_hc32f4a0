---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-4
title: 连接管理器连接性实现 API（Connectivity Implementation API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_连接管理器连接性实现 API（Connectivity Implementation API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接管理器连接性实现 API（Connectivity Implementation API）

<a id="details"></a>

连接管理器连接实现 API（Connection Manager Connectivity Implementation API）。**引入版本（Since）：**3.4。**版本（Version）：**0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_conn_5Fmgr_5Fconn_5Fapi"></a>

```c
struct conn_mgr_conn_api
```

相关声明：[conn_mgr_conn_api](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md)。

连接管理器（Connectivity Manager）的连接API结构。

<a id="r_conn_5Fmgr_5Fconn_5Fimpl"></a>

```c
struct conn_mgr_conn_impl
```

相关声明：[conn_mgr_conn_impl](../modem_wireless_model_reference/P011_conn_mgr_conn_impl_结构体.md)。

连接实现（Connectivity Implementation）结构。

<a id="r_conn_5Fmgr_5Fconn_5Fbinding"></a>

```c
struct conn_mgr_conn_binding
```

相关声明：[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)。

连接管理器（Connectivity Manager）的网络接口绑定结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga3c2b01efd38ecbb9fbb33ac0fc7c88f3"></a>

```c
#define CONN_MGR_CONN_DEFINE(conn_id, conn_api)
```

相关声明：[CONN_MGR_CONN_DEFINE](#ga3c2b01efd38ecbb9fbb33ac0fc7c88f3)。

定义可绑定到网络设备的 `conn_mgr` 连接功能实现（Connectivity Implementation）。

<a id="r_ga519cfa66e1a1f0b769ce2bf61a61887f"></a>

```c
#define CONN_MGR_CONN_DECLARE_PUBLIC(conn_id)
```

相关声明：[CONN_MGR_CONN_DECLARE_PUBLIC](#ga519cfa66e1a1f0b769ce2bf61a61887f)。

将 `conn_mgr` 连接功能实现（Connectivity Implementation）公开可用的辅助宏。

<a id="r_ga1ac9fb870cd2d698451d896113b723d1"></a>

```c
#define CONN_MGR_BIND_CONN_INST(dev_id, inst, conn_id)
```

相关声明：[CONN_MGR_BIND_CONN_INST](#ga1ac9fb870cd2d698451d896113b723d1)。

将连接功能实现（Connectivity Implementation）关联到现有网络设备实例。

<a id="r_ga16633bf29ebac6850b8c511b33bd189f"></a>

```c
#define CONN_MGR_BIND_CONN(dev_id, conn_id)
```

相关声明：[CONN_MGR_BIND_CONN](#ga16633bf29ebac6850b8c511b33bd189f)。

将连接功能实现（Connectivity Implementation）关联到现有网络设备。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga5fc0ba9d7bf365352e665d1c9a055889"></a>

```c
static struct conn_mgr_conn_binding * conn_mgr_if_get_binding (struct net_if *iface)
```

相关声明：[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)、[conn_mgr_if_get_binding](#ga5fc0ba9d7bf365352e665d1c9a055889)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

若存在，则获取指定网络接口（Interface）的 `conn_mgr` 绑定结构体（Binding Struct）。

<a id="r_ga27be6dec40356facce7da18a31a2c12a"></a>

```c
static void conn_mgr_binding_lock (struct conn_mgr_conn_binding *binding)
```

相关声明：[conn_mgr_binding_lock](#ga27be6dec40356facce7da18a31a2c12a)、[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)。

锁定传入的绑定（Binding），使其可安全访问。

<a id="r_ga94a4930a6d7c4db4427dfdfad8f3c154"></a>

```c
static void conn_mgr_binding_unlock (struct conn_mgr_conn_binding *binding)
```

相关声明：[conn_mgr_binding_unlock](#ga94a4930a6d7c4db4427dfdfad8f3c154)、[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)。

解锁传入的绑定（Binding）。

<a id="r_ga4f0f3244f48c5e0204faf8278c2bd94f"></a>

```c
static void conn_mgr_binding_set_flag (struct conn_mgr_conn_binding *binding, enum conn_mgr_if_flag flag, bool value)
```

相关声明：[conn_mgr_binding_set_flag](#ga4f0f3244f48c5e0204faf8278c2bd94f)、[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)、[conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为指定绑定设置指定连接功能标志（Connectivity Flag）的值。

<a id="r_ga128931a6fabce79829af5aebecd59985"></a>

```c
static bool conn_mgr_binding_get_flag (struct conn_mgr_conn_binding *binding, enum conn_mgr_if_flag flag)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[conn_mgr_binding_get_flag](#ga128931a6fabce79829af5aebecd59985)、[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)、[conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)。

检查指定绑定的指定连接功能标志（Connectivity Flag）的值。

## 4.4\_详细说明（Detailed Documentation）

<a id="ga16633bf29ebac6850b8c511b33bd189f"></a>

### `CONN_MGR_BIND_CONN`

```c
#define CONN_MGR_BIND_CONN ( dev_id, conn_id )
```

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

展开值（Value）：

```c
CONN_MGR_BIND_CONN_INST(dev_id, 0, conn_id)
```

将连接功能实现（Connectivity Implementation）关联到现有网络设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_id` | 网络设备标识（Network Device ID）。 |
| `conn_id` | 要关联的连接实现（Connectivity Implementation）的名称。 |

<a id="ga1ac9fb870cd2d698451d896113b723d1"></a>

### `CONN_MGR_BIND_CONN_INST`

```c
#define CONN_MGR_BIND_CONN_INST ( dev_id, inst, conn_id )
```

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

展开值（Value）：

```c
K_MUTEX_DEFINE(CONN_MGR_CONN_BINDING_GET_MUTEX(dev_id, inst));                          \
static CONN_MGR_CONN_IMPL_GET_CTX_TYPE(conn_id)                                         \
                                CONN_MGR_CONN_BINDING_GET_DATA(dev_id, inst);           \
static STRUCT_SECTION_ITERABLE(conn_mgr_conn_binding,                                   \
                                CONN_MGR_CONN_BINDING_GET_NAME(dev_id, inst)) = {       \
        .iface = NET_IF_GET(dev_id, inst),                                              \
        .impl = &(CONN_MGR_CONN_IMPL_GET_NAME(conn_id)),                                \
        .ctx = &(CONN_MGR_CONN_BINDING_GET_DATA(dev_id, inst)),                         \
        .mutex = &(CONN_MGR_CONN_BINDING_GET_MUTEX(dev_id, inst))                       \
};
```

将连接功能实现（Connectivity Implementation）关联到现有网络设备实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_id` | 网络设备标识（Network Device ID）。 |
| `inst` | 网络设备实例（Network Device Instance）。 |
| `conn_id` | 要关联的连接实现（Connectivity Implementation）的名称。 |

<a id="ga519cfa66e1a1f0b769ce2bf61a61887f"></a>

### `CONN_MGR_CONN_DECLARE_PUBLIC`

```c
#define CONN_MGR_CONN_DECLARE_PUBLIC ( conn_id)
```

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

展开值（Value）：

```c
extern const struct conn_mgr_conn_impl CONN_MGR_CONN_IMPL_GET_NAME(conn_id)
```

将 `conn_mgr` 连接功能实现（Connectivity Implementation）公开可用的辅助宏。

<a id="ga3c2b01efd38ecbb9fbb33ac0fc7c88f3"></a>

### `CONN_MGR_CONN_DEFINE`

```c
#define CONN_MGR_CONN_DEFINE ( conn_id, conn_api )
```

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

展开值（Value）：

```c
const struct conn_mgr_conn_impl CONN_MGR_CONN_IMPL_GET_NAME(conn_id) = {        \
        .api = conn_api,                                                        \
};
```

定义可绑定到网络设备的 `conn_mgr` 连接功能实现（Connectivity Implementation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn_id` | 新连接实现（Connectivity Implementation）的名称。 |
| `conn_api` | 指向 `conn_mgr_conn_api` 结构体的指针。 |

<a id="ga128931a6fabce79829af5aebecd59985"></a>

### `conn_mgr_binding_get_flag()`

```c
bool conn_mgr_binding_get_flag ( struct conn_mgr_conn_binding * binding, enum conn_mgr_if_flag flag )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

检查指定绑定的指定连接功能标志（Connectivity Flag）的值。

可从任意线程或回调调用，无需调用 `conn_mgr_binding_lock`。

仅供连接实现（Connectivity Implementations）使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `binding` | 要检查的绑定（Binding）。 |
| `flag` | 要检查的标志（Flag）。 |

**返回（Returns）**：**返回值（Returns）：**`bool`，指定标志（Flag）的值。

<a id="ga27be6dec40356facce7da18a31a2c12a"></a>

### `conn_mgr_binding_lock()`

```c
void conn_mgr_binding_lock ( struct conn_mgr_conn_binding * binding)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

锁定传入的绑定（Binding），使其可安全访问。

访问绑定数据（Binding Data）时都应调用此接口；位于 `conn_mgr_conn_api` 回调内时除外，因为此时 `conn_mgr` 已自动调用。

可重入（Reentrant）。

仅供连接实现（Connectivity Implementations）使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `binding` | 要锁定的绑定（Binding）。 |

<a id="ga4f0f3244f48c5e0204faf8278c2bd94f"></a>

### `conn_mgr_binding_set_flag()`

```c
void conn_mgr_binding_set_flag ( struct conn_mgr_conn_binding * binding, enum conn_mgr_if_flag flag, bool value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

为指定绑定设置指定连接功能标志（Connectivity Flag）的值。

可从任意线程或回调调用，无需调用 `conn_mgr_binding_lock`。

仅供连接实现（Connectivity Implementations）使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `binding` | 要检查的绑定（Binding）。 |
| `flag` | 要检查的标志（Flag）。 |
| `value` | 指定标志（Flag）的新值。 |

<a id="ga94a4930a6d7c4db4427dfdfad8f3c154"></a>

### `conn_mgr_binding_unlock()`

```c
void conn_mgr_binding_unlock ( struct conn_mgr_conn_binding * binding)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

解锁传入的绑定（Binding）。

每次调用 `conn_mgr_binding_lock` 后，在完成绑定数据（Binding Data）访问时调用此接口。

可重入（Reentrant）。

仅供连接实现（Connectivity Implementations）使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `binding` | 要解锁的绑定（Binding）。 |

<a id="ga5fc0ba9d7bf365352e665d1c9a055889"></a>

### `conn_mgr_if_get_binding()`

```c
struct conn_mgr_conn_binding * conn_mgr_if_get_binding ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

若存在，则获取指定网络接口（Interface）的 `conn_mgr` 绑定结构体（Binding Struct）。

缺少 API 结构体（Structs）的连接实现所对应的绑定将被忽略。

仅供连接实现（Connectivity Implementations）使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要获取其绑定结构体（Binding Struct）的已绑定网络接口。 |

**返回（Returns）**：**返回值（Returns）：**`struct conn_mgr_conn_binding *`；存在时返回获取到的绑定结构体指针，否则为 `NULL`。


## 4.5\_原页交叉引用（Cross References）

- [conn_mgr_conn_api](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md)
- [conn_mgr_conn_impl](../modem_wireless_model_reference/P011_conn_mgr_conn_impl_结构体.md)
- [conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/conn_mgr_connectivity_impl.h](../api_file_network_device_reference/P004_zephyr__net__conn_mgr_connectivity_impl.h_文件参考.md)
- [K_MUTEX_DEFINE](../synchronization_reference/P006_互斥量公共接口.md#gab6f3d98fabbdc0918bbc9934d61d63f3)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__conn__mgr__connectivity__impl_html_ga1ac9fb870cd2d698451d896113b723d1"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="agroup__mutex__apis_html_gab6f3d98fabbdc0918bbc9934d61d63f3"></a>
<a id="astructconn__mgr__conn__binding_html"></a>
<a id="astructconn__mgr__conn__impl_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_桥接配置客户端模型（Bridge Configuration Client Model）.md) · [返回大纲](大纲.md) · [下一章](P005_控制台 API（Console API）.md)
