---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-3
title: zephyr__net__conn_mgr_connectivity.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_net\_\_conn\_mgr\_connectivity.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于控制支持通用网络关联流程（Network Association Routines）的网络设备的API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/net/net_if.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/net_mgmt.h>
```

查看此文件的源码。

用于控制支持通用网络关联流程（Network Association Routines）的网络设备的API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_ga5ea6e37ca9eda2b6fd8b165b8182dd38"></a>

```c
#define NET_EVENT_CONN_IF_TIMEOUT (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_TIMEOUT)
```

相关声明：[NET_EVENT_CONN_IF_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga5ea6e37ca9eda2b6fd8b165b8182dd38)。

连接尝试超时（Connection Attempt Timeout）时产生的 `net_mgmt` 网络管理事件。

<a id="r_gae8f207559a7123bd2eca5ef08086d377"></a>

```c
#define NET_EVENT_CONN_IF_FATAL_ERROR (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_FATAL_ERROR)
```

相关声明：[NET_EVENT_CONN_IF_FATAL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gae8f207559a7123bd2eca5ef08086d377)。

接口发生不可恢复的连接错误（Non-recoverable Connectivity Error）时产生的 `net_mgmt` 事件。

<a id="r_gaaab7f33dcc175b4c9117d6c69a0c84c8"></a>

```c
#define NET_EVENT_CONN_IF_IDLE_TIMEOUT (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_IDLE_TIMEOUT)
```

相关声明：[NET_EVENT_CONN_IF_IDLE_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaaab7f33dcc175b4c9117d6c69a0c84c8)。

接口因不活动（Inactivity）而超时时产生的 `net_mgmt` 事件。

<a id="r_gaa4b57ac324a2ac090751919c89c3f0cd"></a>

```c
#define NET_EVENT_CONN_IF_NO_CONFIGURATION (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_NO_CONFIGURATION)
```

相关声明：[NET_EVENT_CONN_IF_NO_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaa4b57ac324a2ac090751919c89c3f0cd)。

接口因缺少配置而无法连接时产生的 `net_mgmt` 事件。

<a id="r_ga605eee24f4419b5cd6a50a0272979da7"></a>

```c
#define CONN_MGR_IF_NO_TIMEOUT 0
```

相关声明：[CONN_MGR_IF_NO_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga605eee24f4419b5cd6a50a0272979da7)。

用于 `conn_mgr_if_set_timeout` 和 `conn_mgr_conn_binding::timeout` 的值，表示不设超时（No Timeout）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.2\_枚举（Enumerations）

<a id="r_gaf10fb532a3dd07ec8c692a72643d0e3f"></a>

```c
enum conn_mgr_if_flag { CONN_MGR_IF_PERSISTENT , CONN_MGR_IF_NO_AUTO_CONNECT , CONN_MGR_IF_NO_AUTO_DOWN }
```

相关声明：[conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)、[CONN_MGR_IF_PERSISTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f)、[CONN_MGR_IF_NO_AUTO_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd)、[CONN_MGR_IF_NO_AUTO_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d)。

各接口的连接标志（Per-interface Connectivity Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga575d367c95592fd9f4ead694ff94543f"></a>

```c
int conn_mgr_if_connect (struct net_if *iface)
```

相关声明：[conn_mgr_if_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga575d367c95592fd9f4ead694ff94543f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

连接接口（Connect Interface）。

<a id="r_gada2b5271b3e5dbcab629e1538b3d8eb4"></a>

```c
int conn_mgr_if_disconnect (struct net_if *iface)
```

相关声明：[conn_mgr_if_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gada2b5271b3e5dbcab629e1538b3d8eb4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

断开接口连接（Disconnect Interface）。

<a id="r_ga09a1169a89eac1a3291185281952ce05"></a>

```c
bool conn_mgr_if_is_bound (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[conn_mgr_if_is_bound](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga09a1169a89eac1a3291185281952ce05)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查所给网络接口（Network Interface）是否支持连接管理，即是否已绑定到某个连接实现（Connectivity Implementation）。

<a id="r_ga2a2e6d7fbb7b1ed0327706a8c253d3e4"></a>

```c
int conn_mgr_if_set_opt (struct net_if *iface, int optname, const void *optval, size_t optlen)
```

相关声明：[conn_mgr_if_set_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga2a2e6d7fbb7b1ed0327706a8c253d3e4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置由具体实现定义的连接选项（Implementation-specific Connectivity Options）。

<a id="r_gaa79794ce9c773c0c3932121c931ac2d6"></a>

```c
int conn_mgr_if_get_opt (struct net_if *iface, int optname, void *optval, size_t *optlen)
```

相关声明：[conn_mgr_if_get_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaa79794ce9c773c0c3932121c931ac2d6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取由具体实现定义的连接选项（Implementation-specific Connectivity Options）。

<a id="r_ga465c9491106cba3c9cb1cf296090612b"></a>

```c
bool conn_mgr_if_get_flag (struct net_if *iface, enum conn_mgr_if_flag flag)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[conn_mgr_if_get_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga465c9491106cba3c9cb1cf296090612b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)。

检查连接标志（Connectivity Flags）的值。

<a id="r_gae86d1c808f31b8ca5e67bacbc844ef47"></a>

```c
int conn_mgr_if_set_flag (struct net_if *iface, enum conn_mgr_if_flag flag, bool value)
```

相关声明：[conn_mgr_if_set_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gae86d1c808f31b8ca5e67bacbc844ef47)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置连接标志（Connectivity Flag）的值。

<a id="r_gada9c37847acc604d82604351cbbb5e64"></a>

```c
int conn_mgr_if_get_timeout (struct net_if *iface)
```

相关声明：[conn_mgr_if_get_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gada9c37847acc604d82604351cbbb5e64)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取接口的连接超时（Connectivity Timeout）。

<a id="r_ga467ecbb330d21b8dfea3e0ce08448400"></a>

```c
int conn_mgr_if_set_timeout (struct net_if *iface, int timeout)
```

相关声明：[conn_mgr_if_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga467ecbb330d21b8dfea3e0ce08448400)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置接口的连接超时（Connectivity Timeout）。

<a id="r_ga5d22b2a44c3595a5b7b240c8fe7d0db1"></a>

```c
int conn_mgr_if_get_idle_timeout (struct net_if *iface)
```

相关声明：[conn_mgr_if_get_idle_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga5d22b2a44c3595a5b7b240c8fe7d0db1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取接口的空闲超时（Idle Timeout）。

<a id="r_ga93f333199c87b2d7668e94c92efd31ce"></a>

```c
int conn_mgr_if_set_idle_timeout (struct net_if *iface, int timeout)
```

相关声明：[conn_mgr_if_set_idle_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga93f333199c87b2d7668e94c92efd31ce)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置接口的空闲超时（Idle Timeout）。

<a id="r_ga4079113088236aede697538d79e5272f"></a>

```c
void conn_mgr_if_used (struct net_if *iface)
```

相关声明：[conn_mgr_if_used](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga4079113088236aede697538d79e5272f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

通知连接管理器（Connection Manager）：该接口刚刚被使用。

<a id="r_ga9e006b8b5095c223d77055fd619710c3"></a>

```c
int conn_mgr_all_if_up (bool skip_ignored)
```

相关声明：[conn_mgr_all_if_up](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md#ga9e006b8b5095c223d77055fd619710c3)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将所有可用网络接口设为管理启用（Admin-up）状态的便捷函数。

<a id="r_gabf6f8e5d8ce51b4c1cbf48f18a57efb2"></a>

```c
int conn_mgr_all_if_down (bool skip_ignored)
```

相关声明：[conn_mgr_all_if_down](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md#gabf6f8e5d8ce51b4c1cbf48f18a57efb2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将所有可用网络接口设为管理停用（Admin-down）状态的便捷函数。

<a id="r_ga48e3c1b98f505af9f8ac811a25f94e1b"></a>

```c
int conn_mgr_all_if_connect (bool skip_ignored)
```

相关声明：[conn_mgr_all_if_connect](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md#ga48e3c1b98f505af9f8ac811a25f94e1b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将所有可用网络接口设为管理启用（Admin-up）状态，并连接其中支持连接功能（Connectivity）的接口的便捷函数。

<a id="r_ga3ce45d9040d3799e1387776257dfa8b7"></a>

```c
int conn_mgr_all_if_disconnect (bool skip_ignored)
```

相关声明：[conn_mgr_all_if_disconnect](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md#ga3ce45d9040d3799e1387776257dfa8b7)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

断开所有支持连接功能（Connectivity）的可用网络接口的便捷函数；不会将接口置于管理停用（Admin-down）状态，除非该接口启用了自动停用（Auto-down）。


## 3.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/net_mgmt.h](../api_source_timing_sensor_reference/P009_net_mgmt.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P010_conn_mgr_connectivity.h_源码浏览.md)
- [NET_EVENT_CONN_IF_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga5ea6e37ca9eda2b6fd8b165b8182dd38)
- [NET_EVENT_CONN_IF_FATAL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gae8f207559a7123bd2eca5ef08086d377)
- [NET_EVENT_CONN_IF_IDLE_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaaab7f33dcc175b4c9117d6c69a0c84c8)
- [NET_EVENT_CONN_IF_NO_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaa4b57ac324a2ac090751919c89c3f0cd)
- [CONN_MGR_IF_NO_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga605eee24f4419b5cd6a50a0272979da7)
- [conn_mgr_if_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga467ecbb330d21b8dfea3e0ce08448400)
- [conn_mgr_conn_binding::timeout](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a8474461cf7b00132441227aae07511ab)
- [conn_mgr_if_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaf10fb532a3dd07ec8c692a72643d0e3f)
- [CONN_MGR_IF_PERSISTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f)
- [CONN_MGR_IF_NO_AUTO_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd)
- [CONN_MGR_IF_NO_AUTO_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d)
- [conn_mgr_if_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga575d367c95592fd9f4ead694ff94543f)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [conn_mgr_if_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gada2b5271b3e5dbcab629e1538b3d8eb4)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [conn_mgr_if_is_bound](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga09a1169a89eac1a3291185281952ce05)
- [conn_mgr_if_set_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga2a2e6d7fbb7b1ed0327706a8c253d3e4)
- [conn_mgr_if_get_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaa79794ce9c773c0c3932121c931ac2d6)
- [conn_mgr_if_get_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga465c9491106cba3c9cb1cf296090612b)
- [conn_mgr_if_set_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gae86d1c808f31b8ca5e67bacbc844ef47)
- [conn_mgr_if_get_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gada9c37847acc604d82604351cbbb5e64)
- [conn_mgr_if_get_idle_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga5d22b2a44c3595a5b7b240c8fe7d0db1)
- [conn_mgr_if_set_idle_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga93f333199c87b2d7668e94c92efd31ce)
- [conn_mgr_if_used](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga4079113088236aede697538d79e5272f)
- [conn_mgr_all_if_up](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md#ga9e006b8b5095c223d77055fd619710c3)
- [conn_mgr_all_if_down](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md#gabf6f8e5d8ce51b4c1cbf48f18a57efb2)
- [conn_mgr_all_if_connect](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md#ga48e3c1b98f505af9f8ac811a25f94e1b)
- [conn_mgr_all_if_disconnect](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md#ga3ce45d9040d3799e1387776257dfa8b7)

<a id="header-details"></a>

---

[上一章](P002_zephyr__dt-bindings__clock__alif-balletto-clocks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__drivers__sensor__mcp9600.h_文件参考.md)
