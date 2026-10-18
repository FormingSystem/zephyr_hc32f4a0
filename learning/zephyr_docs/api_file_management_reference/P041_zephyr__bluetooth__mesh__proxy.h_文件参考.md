---
id: learning.zephyr-docs.api-file-management-reference.page-41
title: zephyr__bluetooth__mesh__proxy.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/proxy_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_zephyr\_\_bluetooth\_\_mesh\_\_proxy.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/proxy_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

代理（Proxy）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

代理（Proxy）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 41.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fproxy_5Fcb"></a>

```c
struct bt_mesh_proxy_cb
```

相关声明：[bt_mesh_proxy_cb](../bluetooth_mesh_model_reference/P089_bt_mesh_proxy_cb_结构体.md)。

代理功能（Proxy Feature）的回调。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 41.2\_宏定义（Macros）

<a id="r_ga325b71c3d7ed69952bf760c0288b28ef"></a>

```c
#define BT_MESH_PROXY_CB_DEFINE(_name)
```

相关声明：[BT_MESH_PROXY_CB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga325b71c3d7ed69952bf760c0288b28ef)。

为代理（Proxy）事件注册回调结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 41.3\_函数（Functions）

<a id="r_ga7fb3c76f1be6943dd4a18f26e8dd18e7"></a>

```c
int bt_mesh_proxy_identity_enable (void)
```

相关声明：[bt_mesh_proxy_identity_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga7fb3c76f1be6943dd4a18f26e8dd18e7)。

启用使用节点身份（Node Identity）的广播。

<a id="r_gaecd529a9fd0df83b3d775d32885802f1"></a>

```c
int bt_mesh_proxy_private_identity_enable (void)
```

相关声明：[bt_mesh_proxy_private_identity_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#gaecd529a9fd0df83b3d775d32885802f1)。

启用使用私有节点身份（Private Node Identity）的广播。

<a id="r_ga07d4edf80bdbc39f626f66720035c98b"></a>

```c
int bt_mesh_proxy_connect (uint16_t net_idx)
```

相关声明：[bt_mesh_proxy_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga07d4edf80bdbc39f626f66720035c98b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

允许代理客户端（Proxy Client）自动连接到网络。

<a id="r_gaa9978d460b31412c96c6c1685729ec4f"></a>

```c
int bt_mesh_proxy_disconnect (uint16_t net_idx)
```

相关声明：[bt_mesh_proxy_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#gaa9978d460b31412c96c6c1685729ec4f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

禁止代理客户端自动连接到网络。

<a id="r_ga9a72515992af4f93a34a6c1aaf69d8df"></a>

```c
int bt_mesh_proxy_solicit (uint16_t net_idx)
```

相关声明：[bt_mesh_proxy_solicit](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga9a72515992af4f93a34a6c1aaf69d8df)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

调度请求协议数据单元（Solicitation PDUs）的广播。


## 41.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P676_proxy.h_源码浏览.md)
- [bt_mesh_proxy_cb](../bluetooth_mesh_model_reference/P089_bt_mesh_proxy_cb_结构体.md)
- [BT_MESH_PROXY_CB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga325b71c3d7ed69952bf760c0288b28ef)
- [bt_mesh_proxy_identity_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga7fb3c76f1be6943dd4a18f26e8dd18e7)
- [bt_mesh_proxy_private_identity_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#gaecd529a9fd0df83b3d775d32885802f1)
- [bt_mesh_proxy_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga07d4edf80bdbc39f626f66720035c98b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_proxy_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#gaa9978d460b31412c96c6c1685729ec4f)
- [bt_mesh_proxy_solicit](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__proxy.html#ga9a72515992af4f93a34a6c1aaf69d8df)

<a id="header-details"></a>

---

[上一章](P040_zephyr__drivers__interrupt_controller__nxp_irqsteer.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P042_zephyr__bluetooth__mesh__sar_cfg_cli.h_文件参考.md)
