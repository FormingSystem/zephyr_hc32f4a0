---
id: learning.zephyr-docs.api-file-runtime-reference.page-49
title: zephyr__net__offloaded_netdev.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/offloaded__netdev_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_zephyr\_\_net\_\_offloaded\_netdev.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/offloaded__netdev_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

卸载网络设备（Offloaded Network Device）的接口API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/net/net_if.h>
```

查看此文件的源码。

卸载型网络设备接口 API（Offloaded Network Device Interface API）。应用程序不应包含此头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 49.1\_数据结构（Data Structures）

<a id="r_offloaded_5Fif_5Fapi"></a>

```c
struct offloaded_if_api
```

相关声明：[offloaded_if_api](../network_service_model_reference/P038_offloaded_if_api_结构体.md)。

供卸载接口/网络设备（Offloaded Interfaces / Network Devices）使用的扩展net_if_api，可处理管理启用/停用状态变化。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 49.2\_枚举（Enumerations）

<a id="r_gac1980977f6da3ace33ede7949d43f81f"></a>

```c
enum offloaded_net_if_types { L2_OFFLOADED_NET_IF_TYPE_UNKNOWN , L2_OFFLOADED_NET_IF_TYPE_ETHERNET , L2_OFFLOADED_NET_IF_TYPE_MODEM , L2_OFFLOADED_NET_IF_TYPE_WIFI }
```

相关声明：[offloaded_net_if_types](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#gac1980977f6da3ace33ede7949d43f81f)、[L2_OFFLOADED_NET_IF_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d)、[L2_OFFLOADED_NET_IF_TYPE_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a)、[L2_OFFLOADED_NET_IF_TYPE_MODEM](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21)、[L2_OFFLOADED_NET_IF_TYPE_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24)。

卸载型网络设备二层类型（Offloaded Netdev L2 Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 49.3\_函数（Functions）

<a id="r_gad1076eacf1b1e82f70759f9b54937ced"></a>

```c
static bool net_off_is_wifi_offloaded (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_off_is_wifi_offloaded](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#gad1076eacf1b1e82f70759f9b54937ced)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查卸载型网络接口（Offloaded Network Interface）是否支持 Wi-Fi。


## 49.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P139_offloaded_netdev.h_源码浏览.md)
- [offloaded_if_api](../network_service_model_reference/P038_offloaded_if_api_结构体.md)
- [offloaded_net_if_types](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#gac1980977f6da3ace33ede7949d43f81f)
- [L2_OFFLOADED_NET_IF_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d)
- [L2_OFFLOADED_NET_IF_TYPE_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a)
- [L2_OFFLOADED_NET_IF_TYPE_MODEM](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21)
- [L2_OFFLOADED_NET_IF_TYPE_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_off_is_wifi_offloaded](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html#gad1076eacf1b1e82f70759f9b54937ced)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)

<a id="header-details"></a>

---

[上一章](P048_zephyr__dt-bindings__gpio__nuvoton-npcx-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P050_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt_client.h_文件参考.md)
