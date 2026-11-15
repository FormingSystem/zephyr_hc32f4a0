---
id: learning.zephyr-docs.api-video-event-topic-reference.page-13
title: Xen 事件通道（Event channels）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_Xen 事件通道（Event channels）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

从 Zephyr 分配、绑定和处理 Xen 事件通道。

<a id="details"></a>

从 Zephyr 分配、绑定和处理 Xen 事件通道。

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_events_2Eh"></a>

```c
file events.h
```

相关声明：[events.h](../api_file_storage_event_reference/P008_zephyr__xen__events.h_文件参考.md)。

Xen事件通道（Event Channel）的服务。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 13.2\_类型定义（Typedefs）

<a id="r_ga1e631dcb6d0ab84d2b63cced85f28d47"></a>

```c
typedef void(* evtchn_cb_t) (void *priv)
```

相关声明：[evtchn_cb_t](#ga1e631dcb6d0ab84d2b63cced85f28d47)。

事件通道回调签名（Event-channel Callback Signature）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.3\_函数（Functions）

<a id="r_gae5391f2b67ddbd598f33d796ba591568"></a>

```c
int evtchn_status (evtchn_status_t *status)
```

相关声明：[evtchn_status](#gae5391f2b67ddbd598f33d796ba591568)。

查询事件通道状态（Event Channel Status）。

<a id="r_gabed06147ec0c0f9650ac7348a04ee430"></a>

```c
int evtchn_close (evtchn_port_t port)
```

相关声明：[evtchn_close](#gabed06147ec0c0f9650ac7348a04ee430)。

关闭本地事件通道（Local Event Channel）。

<a id="r_ga761efce6eab19f91b33391d4bf516fff"></a>

```c
int evtchn_set_priority (evtchn_port_t port, uint32_t priority)
```

相关声明：[evtchn_set_priority](#ga761efce6eab19f91b33391d4bf516fff)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置分配给事件通道（Event Channel）的 Xen 优先级（Priority）。

<a id="r_ga3d6fce57c67b5ad26532e3721de59328"></a>

```c
int notify_evtchn (evtchn_port_t port)
```

相关声明：[notify_evtchn](#ga3d6fce57c67b5ad26532e3721de59328)。

通过事件通道（Event Channel）发送通知（Notification）。

<a id="r_ga46ba842a0e4f518d03683253d35b7126"></a>

```c
int alloc_unbound_event_channel (domid_t remote_dom)
```

相关声明：[alloc_unbound_event_channel](#ga46ba842a0e4f518d03683253d35b7126)。

为调用域（Calling Domain）分配未绑定事件通道（Unbound Event Channel）。

<a id="r_ga76e7a069825b569709b1e5342a648598"></a>

```c
int alloc_unbound_event_channel_dom0 (domid_t dom, domid_t remote_dom)
```

相关声明：[alloc_unbound_event_channel_dom0](#ga76e7a069825b569709b1e5342a648598)。

在两个域（Domains）之间分配未绑定事件通道（Unbound Event Channel）。

<a id="r_gadc0a69c0205307e86458ada50aa0302d"></a>

```c
int bind_interdomain_event_channel (domid_t remote_dom, evtchn_port_t remote_port, evtchn_cb_t cb, void *data)
```

相关声明：[bind_interdomain_event_channel](#gadc0a69c0205307e86458ada50aa0302d)、[evtchn_cb_t](#ga1e631dcb6d0ab84d2b63cced85f28d47)。

绑定到远程事件通道（Remote Event Channel）并注册回调。

<a id="r_ga74e60b33dd93a62835e86b251a9cd43c"></a>

```c
int bind_event_channel (evtchn_port_t port, evtchn_cb_t cb, void *data)
```

相关声明：[bind_event_channel](#ga74e60b33dd93a62835e86b251a9cd43c)、[evtchn_cb_t](#ga1e631dcb6d0ab84d2b63cced85f28d47)。

为已分配的本地事件通道（Local Event Channel）附加回调。

<a id="r_gabad4417540bf329eca43842bf83549e9"></a>

```c
int unbind_event_channel (evtchn_port_t port)
```

相关声明：[unbind_event_channel](#gabad4417540bf329eca43842bf83549e9)。

移除绑定到事件通道（Event Channel）的回调。

<a id="r_ga2ac07d6eff7d3406716917578b5f7daf"></a>

```c
int get_missed_events (evtchn_port_t port)
```

相关声明：[get_missed_events](#ga2ac07d6eff7d3406716917578b5f7daf)。

获取并清除未绑定通道（Unbound Channel）的漏失事件状态（Missed-event State）。

<a id="r_ga4b07a630ef8286be5ab8b120393f5be0"></a>

```c
int mask_event_channel (evtchn_port_t port)
```

相关声明：[mask_event_channel](#ga4b07a630ef8286be5ab8b120393f5be0)。

屏蔽事件通道（Event Channel）的本地递送（Local Delivery）。

<a id="r_gac9ccbc6f134743ad39396712c47facf9"></a>

```c
int unmask_event_channel (evtchn_port_t port)
```

相关声明：[unmask_event_channel](#gac9ccbc6f134743ad39396712c47facf9)。

解除事件通道（Event Channel）本地递送（Local Delivery）的屏蔽。

<a id="r_ga0597d0e7f40eca8dd73a131c95e346d4"></a>

```c
void clear_event_channel (evtchn_port_t port)
```

相关声明：[clear_event_channel](#ga0597d0e7f40eca8dd73a131c95e346d4)。

清除事件通道（Event Channel）的待处理位（Pending Bit）。

<a id="r_gaf6542be4472fb2d1dc17deca6c323972"></a>

```c
int xen_events_init (void)
```

相关声明：[xen_events_init](#gaf6542be4472fb2d1dc17deca6c323972)。

为当前客户机（Guest）初始化 Xen 事件处理（Event Handling）。

## 13.4\_详细说明（Detailed Documentation）

<a id="ga1e631dcb6d0ab84d2b63cced85f28d47"></a>

### `evtchn_cb_t`

```c
typedef void(* evtchn_cb_t) (void *priv)
```

```c
#include <zephyr/xen/events.h>
```

事件通道回调签名（Event-channel Callback Signature）。

回调从 Xen 事件中断处理函数（Event Interrupt Handler）中执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `priv` | 随事件通道（Event Channel）注册的用户数据指针。 |

<a id="ga46ba842a0e4f518d03683253d35b7126"></a>

### `alloc_unbound_event_channel()`

```c
int alloc_unbound_event_channel ( domid_t remote_dom)
```

```c
#include <zephyr/xen/events.h>
```

为调用域（Calling Domain）分配未绑定事件通道（Unbound Event Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `remote_dom` | 可以绑定到所分配通道的域（Domain）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

**返回（Returns）**：返回值：成功返回本地事件通道端口（Local Event-channel Port），失败返回负 errno 值。

<a id="ga76e7a069825b569709b1e5342a648598"></a>

### `alloc_unbound_event_channel_dom0()`

```c
int alloc_unbound_event_channel_dom0 ( domid_t dom, domid_t remote_dom )
```

```c
#include <zephyr/xen/events.h>
```

在两个域（Domains）之间分配未绑定事件通道（Unbound Event Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dom` | 接收新本地端口的域（Domain），可以是 `DOMID_SELF`。 |
| `remote_dom` | 可以绑定到此端口的对端域（Peer Domain）。 |

**注意（Attention）**：注意：仅在同时启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 和 `CONFIG_XEN_DOM0` 时可用。

**返回（Returns）**：返回值：成功返回本地事件通道端口（Local Event-channel Port），失败返回负 errno 值。

<a id="ga74e60b33dd93a62835e86b251a9cd43c"></a>

### `bind_event_channel()`

```c
int bind_event_channel ( evtchn_port_t port, evtchn_cb_t cb, void * data )
```

```c
#include <zephyr/xen/events.h>
```

为已分配的本地事件通道（Local Event Channel）附加回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 本地事件通道端口号（Local Event-channel Port Number）。 |
| `cb` | 端口收到通知时调用的回调（Callback）。 |
| `data` | 传给 `cb` 的用户数据指针（User Data Pointer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

<a id="gadc0a69c0205307e86458ada50aa0302d"></a>

### `bind_interdomain_event_channel()`

```c
int bind_interdomain_event_channel ( domid_t remote_dom, evtchn_port_t remote_port, evtchn_cb_t cb, void * data )
```

```c
#include <zephyr/xen/events.h>
```

绑定到远程事件通道（Remote Event Channel）并注册回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `remote_dom` | 已拥有 `remote_port` 的对端域（Peer Domain）。 |
| `remote_port` | `remote_dom` 中的事件通道端口（Event-channel Port）。 |
| `cb` | 本地通道触发时调用的回调（Callback）。 |
| `data` | 传给 `cb` 的用户数据指针（User Data Pointer）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

**返回（Returns）**：返回值：成功返回本地事件通道端口（Local Event-channel Port），失败返回负 errno 值。

<a id="ga0597d0e7f40eca8dd73a131c95e346d4"></a>

### `clear_event_channel()`

```c
void clear_event_channel ( evtchn_port_t port)
```

```c
#include <zephyr/xen/events.h>
```

清除事件通道（Event Channel）的待处理位（Pending Bit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 本地事件通道端口号（Local Event-channel Port Number）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

<a id="gabed06147ec0c0f9650ac7348a04ee430"></a>

### `evtchn_close()`

```c
int evtchn_close ( evtchn_port_t port)
```

```c
#include <zephyr/xen/events.h>
```

关闭本地事件通道（Local Event Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 要关闭的本地事件通道端口（Local Event-channel Port）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga761efce6eab19f91b33391d4bf516fff"></a>

### `evtchn_set_priority()`

```c
int evtchn_set_priority ( evtchn_port_t port, uint32_t priority )
```

```c
#include <zephyr/xen/events.h>
```

设置分配给事件通道（Event Channel）的 Xen 优先级（Priority）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 要更新的本地事件通道端口（Local Event-channel Port）。 |
| `priority` | Xen 事件优先级值（Event Priority Value）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gae5391f2b67ddbd598f33d796ba591568"></a>

### `evtchn_status()`

```c
int evtchn_status ( evtchn_status_t * status)
```

```c
#include <zephyr/xen/events.h>
```

查询事件通道状态（Event Channel Status）。

调用方在 `status` 中提供输入域和端口，Xen 使用当前通道状态（Channel State）填充其余字段。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] status` | 事件通道状态请求与响应缓冲区（Event-channel Status Request and Response Buffer）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga2ac07d6eff7d3406716917578b5f7daf"></a>

### `get_missed_events()`

```c
int get_missed_events ( evtchn_port_t port)
```

```c
#include <zephyr/xen/events.h>
```

获取并清除未绑定通道（Unbound Channel）的漏失事件状态（Missed-event State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 本地事件通道端口号（Local Event-channel Port Number）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | 没有绑定回调期间，至少记录了一个事件。 |
| `0` | 其他情况。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

<a id="ga4b07a630ef8286be5ab8b120393f5be0"></a>

### `mask_event_channel()`

```c
int mask_event_channel ( evtchn_port_t port)
```

```c
#include <zephyr/xen/events.h>
```

屏蔽事件通道（Event Channel）的本地递送（Local Delivery）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 本地事件通道端口号（Local Event-channel Port Number）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 更新共享信息掩码位（Shared-info Mask Bit）后始终返回。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

<a id="ga3d6fce57c67b5ad26532e3721de59328"></a>

### `notify_evtchn()`

```c
int notify_evtchn ( evtchn_port_t port)
```

```c
#include <zephyr/xen/events.h>
```

通过事件通道（Event Channel）发送通知（Notification）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 要通知的本地事件通道端口（Local Event-channel Port）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gabad4417540bf329eca43842bf83549e9"></a>

### `unbind_event_channel()`

```c
int unbind_event_channel ( evtchn_port_t port)
```

```c
#include <zephyr/xen/events.h>
```

移除绑定到事件通道（Event Channel）的回调。

通道仍保持已分配状态，但后续通知会被记录为错过的事件（Missed Events），直到注册另一个回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 本地事件通道端口号（Local Event-channel Port Number）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

<a id="gac9ccbc6f134743ad39396712c47facf9"></a>

### `unmask_event_channel()`

```c
int unmask_event_channel ( evtchn_port_t port)
```

```c
#include <zephyr/xen/events.h>
```

解除事件通道（Event Channel）本地递送（Local Delivery）的屏蔽。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 本地事件通道端口号（Local Event-channel Port Number）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 更新共享信息掩码位（Shared-info Mask Bit）后始终返回。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

<a id="gaf6542be4472fb2d1dc17deca6c323972"></a>

### `xen_events_init()`

```c
int xen_events_init ( void )
```

```c
#include <zephyr/xen/events.h>
```

为当前客户机（Guest）初始化 Xen 事件处理（Event Handling）。

准备各端口的回调表（Per-port Callback Table），并将 Zephyr 中断服务例程（ISR）连接到设备树描述的 Xen 事件中断。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | Xen 共享信息页（Shared-info Page）尚未映射。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_EVENTS` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 13.5\_原页交叉引用（Cross References）

- [events.h](../api_file_storage_event_reference/P008_zephyr__xen__events.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [CONFIG_XEN_EVENTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_EVENTS)
- [CONFIG_XEN_DOM0](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_DOM0)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_Xen 设备模型（Device model）.md) · [返回大纲](大纲.md)
