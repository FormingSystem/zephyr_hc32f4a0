---
id: learning.zephyr-docs.api-file-network-device-reference.page-4
title: zephyr__net__conn_mgr_connectivity_impl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_net\_\_conn\_mgr\_connectivity\_impl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity__impl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于定义conn_mgr连接实现（Connectivity Implementations）的API，使网络接口可与conn_mgr_connectivity配合使用。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/net/net_if.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/net_mgmt.h>
#include <zephyr/net/conn_mgr_connectivity.h>
```

查看此文件的源码。

用于定义conn_mgr连接实现（Connectivity Implementations）的API，使网络接口可与conn_mgr_connectivity配合使用。

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

相关声明：[CONN_MGR_CONN_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga3c2b01efd38ecbb9fbb33ac0fc7c88f3)。

定义可绑定到网络设备的 `conn_mgr` 连接功能实现（Connectivity Implementation）。

<a id="r_ga519cfa66e1a1f0b769ce2bf61a61887f"></a>

```c
#define CONN_MGR_CONN_DECLARE_PUBLIC(conn_id)
```

相关声明：[CONN_MGR_CONN_DECLARE_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga519cfa66e1a1f0b769ce2bf61a61887f)。

将 `conn_mgr` 连接功能实现（Connectivity Implementation）公开可用的辅助宏。

<a id="r_ga1ac9fb870cd2d698451d896113b723d1"></a>

```c
#define CONN_MGR_BIND_CONN_INST(dev_id, inst, conn_id)
```

相关声明：[CONN_MGR_BIND_CONN_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga1ac9fb870cd2d698451d896113b723d1)。

将连接功能实现（Connectivity Implementation）关联到现有网络设备实例。

<a id="r_ga16633bf29ebac6850b8c511b33bd189f"></a>

```c
#define CONN_MGR_BIND_CONN(dev_id, conn_id)
```

相关声明：[CONN_MGR_BIND_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga16633bf29ebac6850b8c511b33bd189f)。

将连接功能实现（Connectivity Implementation）关联到现有网络设备。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga5fc0ba9d7bf365352e665d1c9a055889"></a>

```c
static struct conn_mgr_conn_binding * conn_mgr_if_get_binding (struct net_if *iface)
```

相关声明：[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)、[conn_mgr_if_get_binding](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga5fc0ba9d7bf365352e665d1c9a055889)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

若存在，则获取指定网络接口（Interface）的 `conn_mgr` 绑定结构体（Binding Struct）。

<a id="r_ga27be6dec40356facce7da18a31a2c12a"></a>

```c
static void conn_mgr_binding_lock (struct conn_mgr_conn_binding *binding)
```

相关声明：[conn_mgr_binding_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga27be6dec40356facce7da18a31a2c12a)、[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)。

锁定传入的绑定（Binding），使其可安全访问。

<a id="r_ga94a4930a6d7c4db4427dfdfad8f3c154"></a>

```c
static void conn_mgr_binding_unlock (struct conn_mgr_conn_binding *binding)
```

相关声明：[conn_mgr_binding_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga94a4930a6d7c4db4427dfdfad8f3c154)、[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)。

解锁传入的绑定（Binding）。

<a id="r_ga4f0f3244f48c5e0204faf8278c2bd94f"></a>

```c
static void conn_mgr_binding_set_flag (struct conn_mgr_conn_binding *binding, enum conn_mgr_if_flag flag, bool value)
```

相关声明：[conn_mgr_binding_set_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga4f0f3244f48c5e0204faf8278c2bd94f)、[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)、[conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为指定绑定设置指定连接功能标志（Connectivity Flag）的值。

<a id="r_ga128931a6fabce79829af5aebecd59985"></a>

```c
static bool conn_mgr_binding_get_flag (struct conn_mgr_conn_binding *binding, enum conn_mgr_if_flag flag)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[conn_mgr_binding_get_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga128931a6fabce79829af5aebecd59985)、[conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)、[conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)。

检查指定绑定的指定连接功能标志（Connectivity Flag）的值。


## 4.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/net_mgmt.h](../api_source_timing_sensor_reference/P009_net_mgmt.h_源码浏览.md)
- [zephyr/net/conn_mgr_connectivity.h](../api_source_runtime_reference/P010_conn_mgr_connectivity.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P011_conn_mgr_connectivity_impl.h_源码浏览.md)
- [conn_mgr_conn_api](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md)
- [conn_mgr_conn_impl](../modem_wireless_model_reference/P011_conn_mgr_conn_impl_结构体.md)
- [conn_mgr_conn_binding](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md)
- [CONN_MGR_CONN_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga3c2b01efd38ecbb9fbb33ac0fc7c88f3)
- [CONN_MGR_CONN_DECLARE_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga519cfa66e1a1f0b769ce2bf61a61887f)
- [CONN_MGR_BIND_CONN_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga1ac9fb870cd2d698451d896113b723d1)
- [CONN_MGR_BIND_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga16633bf29ebac6850b8c511b33bd189f)
- [conn_mgr_if_get_binding](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga5fc0ba9d7bf365352e665d1c9a055889)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [conn_mgr_binding_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga27be6dec40356facce7da18a31a2c12a)
- [conn_mgr_binding_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga94a4930a6d7c4db4427dfdfad8f3c154)
- [conn_mgr_binding_set_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga4f0f3244f48c5e0204faf8278c2bd94f)
- [conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [conn_mgr_binding_get_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga128931a6fabce79829af5aebecd59985)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__buzzer.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__console__console.h_文件参考.md)
