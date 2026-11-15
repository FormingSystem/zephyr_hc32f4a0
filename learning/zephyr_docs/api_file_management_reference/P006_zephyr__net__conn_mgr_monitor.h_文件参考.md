---
id: learning.zephyr-docs.api-file-management-reference.page-6
title: zephyr__net__conn_mgr_monitor.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__monitor_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_net\_\_conn\_mgr\_monitor.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__monitor_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于监测网络连接与接口（Network Connections and Interfaces）的API。

查看此文件的源码。

<a id="details"></a>

用于监测网络连接与接口（Network Connections and Interfaces）的API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.1\_函数（Functions）

<a id="r_gacdde95f41f32e7a829d8cd3a6d0e2277"></a>

```c
void conn_mgr_mon_resend_status (void)
```

相关声明：[conn_mgr_mon_resend_status](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gacdde95f41f32e7a829d8cd3a6d0e2277)。

根据当前是否具备网络连通性（connectivity），重新发送 `NET_L4_CONNECTED` 或 `NET_L4_DISCONNECTED`。

<a id="r_ga7bad393c43a24df7a03176830b05b288"></a>

```c
void conn_mgr_ignore_iface (struct net_if *iface)
```

相关声明：[conn_mgr_ignore_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#ga7bad393c43a24df7a03176830b05b288)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将网络接口（iface）标记为由 `conn_mgr` 忽略。

<a id="r_gacc8735b835dea9b31531fcca9fe8a979"></a>

```c
void conn_mgr_watch_iface (struct net_if *iface)
```

相关声明：[conn_mgr_watch_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gacc8735b835dea9b31531fcca9fe8a979)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

监视网络接口，即停止忽略该接口。

<a id="r_gada16a88ec2c1db71fc39782b0696dac2"></a>

```c
bool conn_mgr_is_iface_ignored (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[conn_mgr_is_iface_ignored](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gada16a88ec2c1db71fc39782b0696dac2)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查所提供网络接口当前是否被忽略。

<a id="r_ga6bd1ee46dc2e3dae554fce49e82c6187"></a>

```c
void conn_mgr_ignore_l2 (const struct net_l2 *l2)
```

相关声明：[conn_mgr_ignore_l2](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#ga6bd1ee46dc2e3dae554fce49e82c6187)、[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)。

将第二层（L2）标记为由 `conn_mgr` 忽略。

<a id="r_gad96056478dcbcb568dd2ef8d5d2ad50b"></a>

```c
void conn_mgr_watch_l2 (const struct net_l2 *l2)
```

相关声明：[conn_mgr_watch_l2](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gad96056478dcbcb568dd2ef8d5d2ad50b)、[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)。

监视 L2，即停止忽略该 L2。


## 6.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P113_conn_mgr_monitor.h_源码浏览.md)
- [conn_mgr_mon_resend_status](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gacdde95f41f32e7a829d8cd3a6d0e2277)
- [conn_mgr_ignore_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#ga7bad393c43a24df7a03176830b05b288)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [conn_mgr_watch_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gacc8735b835dea9b31531fcca9fe8a979)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [conn_mgr_is_iface_ignored](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gada16a88ec2c1db71fc39782b0696dac2)
- [conn_mgr_ignore_l2](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#ga6bd1ee46dc2e3dae554fce49e82c6187)
- [net_l2](../network_core_model_reference/P103_net_l2_结构体.md)
- [conn_mgr_watch_l2](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html#gad96056478dcbcb568dd2ef8d5d2ad50b)

<a id="header-details"></a>

---

[上一章](P005_zephyr__drivers__display__color_dither.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__haptics__cs40l5x.h_文件参考.md)
