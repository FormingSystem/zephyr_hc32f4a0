---
id: learning.zephyr-docs.api-file-storage-event-reference.page-8
title: zephyr__xen__events.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/events_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_xen\_\_events.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/events_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen事件通道（Event Channel）的服务。

<a id="details"></a>

```c
#include <xen/public/event_channel.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

Xen事件通道（Event Channel）的服务。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.1\_类型定义（Typedefs）

<a id="r_ga1e631dcb6d0ab84d2b63cced85f28d47"></a>

```c
typedef void(* evtchn_cb_t) (void *priv)
```

相关声明：[evtchn_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga1e631dcb6d0ab84d2b63cced85f28d47)。

事件通道回调签名（Event-channel Callback Signature）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.2\_函数（Functions）

<a id="r_gae5391f2b67ddbd598f33d796ba591568"></a>

```c
int evtchn_status (evtchn_status_t *status)
```

相关声明：[evtchn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gae5391f2b67ddbd598f33d796ba591568)。

查询事件通道状态（Event Channel Status）。

<a id="r_gabed06147ec0c0f9650ac7348a04ee430"></a>

```c
int evtchn_close (evtchn_port_t port)
```

相关声明：[evtchn_close](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gabed06147ec0c0f9650ac7348a04ee430)。

关闭本地事件通道（Local Event Channel）。

<a id="r_ga761efce6eab19f91b33391d4bf516fff"></a>

```c
int evtchn_set_priority (evtchn_port_t port, uint32_t priority)
```

相关声明：[evtchn_set_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga761efce6eab19f91b33391d4bf516fff)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置分配给事件通道（Event Channel）的 Xen 优先级（Priority）。

<a id="r_ga3d6fce57c67b5ad26532e3721de59328"></a>

```c
int notify_evtchn (evtchn_port_t port)
```

相关声明：[notify_evtchn](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga3d6fce57c67b5ad26532e3721de59328)。

通过事件通道（Event Channel）发送通知（Notification）。

<a id="r_ga46ba842a0e4f518d03683253d35b7126"></a>

```c
int alloc_unbound_event_channel (domid_t remote_dom)
```

相关声明：[alloc_unbound_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga46ba842a0e4f518d03683253d35b7126)。

为调用域（Calling Domain）分配未绑定事件通道（Unbound Event Channel）。

<a id="r_ga76e7a069825b569709b1e5342a648598"></a>

```c
int alloc_unbound_event_channel_dom0 (domid_t dom, domid_t remote_dom)
```

相关声明：[alloc_unbound_event_channel_dom0](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga76e7a069825b569709b1e5342a648598)。

在两个域（Domains）之间分配未绑定事件通道（Unbound Event Channel）。

<a id="r_gadc0a69c0205307e86458ada50aa0302d"></a>

```c
int bind_interdomain_event_channel (domid_t remote_dom, evtchn_port_t remote_port, evtchn_cb_t cb, void *data)
```

相关声明：[bind_interdomain_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gadc0a69c0205307e86458ada50aa0302d)、[evtchn_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga1e631dcb6d0ab84d2b63cced85f28d47)。

绑定到远程事件通道（Remote Event Channel）并注册回调。

<a id="r_ga74e60b33dd93a62835e86b251a9cd43c"></a>

```c
int bind_event_channel (evtchn_port_t port, evtchn_cb_t cb, void *data)
```

相关声明：[bind_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga74e60b33dd93a62835e86b251a9cd43c)、[evtchn_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga1e631dcb6d0ab84d2b63cced85f28d47)。

为已分配的本地事件通道（Local Event Channel）附加回调。

<a id="r_gabad4417540bf329eca43842bf83549e9"></a>

```c
int unbind_event_channel (evtchn_port_t port)
```

相关声明：[unbind_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gabad4417540bf329eca43842bf83549e9)。

移除绑定到事件通道（Event Channel）的回调。

<a id="r_ga2ac07d6eff7d3406716917578b5f7daf"></a>

```c
int get_missed_events (evtchn_port_t port)
```

相关声明：[get_missed_events](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga2ac07d6eff7d3406716917578b5f7daf)。

获取并清除未绑定通道（Unbound Channel）的漏失事件状态（Missed-event State）。

<a id="r_ga4b07a630ef8286be5ab8b120393f5be0"></a>

```c
int mask_event_channel (evtchn_port_t port)
```

相关声明：[mask_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga4b07a630ef8286be5ab8b120393f5be0)。

屏蔽事件通道（Event Channel）的本地递送（Local Delivery）。

<a id="r_gac9ccbc6f134743ad39396712c47facf9"></a>

```c
int unmask_event_channel (evtchn_port_t port)
```

相关声明：[unmask_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gac9ccbc6f134743ad39396712c47facf9)。

解除事件通道（Event Channel）本地递送（Local Delivery）的屏蔽。

<a id="r_ga0597d0e7f40eca8dd73a131c95e346d4"></a>

```c
void clear_event_channel (evtchn_port_t port)
```

相关声明：[clear_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga0597d0e7f40eca8dd73a131c95e346d4)。

清除事件通道（Event Channel）的待处理位（Pending Bit）。

<a id="r_gaf6542be4472fb2d1dc17deca6c323972"></a>

```c
int xen_events_init (void)
```

相关声明：[xen_events_init](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gaf6542be4472fb2d1dc17deca6c323972)。

为当前客户机（Guest）初始化 Xen 事件处理（Event Handling）。


## 8.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P067_events.h_源码浏览.md)
- [evtchn_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga1e631dcb6d0ab84d2b63cced85f28d47)
- [evtchn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gae5391f2b67ddbd598f33d796ba591568)
- [evtchn_close](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gabed06147ec0c0f9650ac7348a04ee430)
- [evtchn_set_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga761efce6eab19f91b33391d4bf516fff)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [notify_evtchn](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga3d6fce57c67b5ad26532e3721de59328)
- [alloc_unbound_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga46ba842a0e4f518d03683253d35b7126)
- [alloc_unbound_event_channel_dom0](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga76e7a069825b569709b1e5342a648598)
- [bind_interdomain_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gadc0a69c0205307e86458ada50aa0302d)
- [bind_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga74e60b33dd93a62835e86b251a9cd43c)
- [unbind_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gabad4417540bf329eca43842bf83549e9)
- [get_missed_events](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga2ac07d6eff7d3406716917578b5f7daf)
- [mask_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga4b07a630ef8286be5ab8b120393f5be0)
- [unmask_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gac9ccbc6f134743ad39396712c47facf9)
- [clear_event_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#ga0597d0e7f40eca8dd73a131c95e346d4)
- [xen_events_init](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__event__channels.html#gaf6542be4472fb2d1dc17deca6c323972)

<a id="header-details"></a>

---

[上一章](P007_zephyr__drivers__wifi__esp_wifi__esp_wifi_mesh.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__bluetooth__audio__gmap_lc3_preset.h_文件参考.md)
