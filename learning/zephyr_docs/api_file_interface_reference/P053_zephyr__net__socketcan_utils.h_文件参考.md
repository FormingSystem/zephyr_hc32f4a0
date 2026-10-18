---
id: learning.zephyr-docs.api-file-interface-reference.page-53
title: zephyr__net__socketcan_utils.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socketcan__utils_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_zephyr\_\_net\_\_socketcan\_utils.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/socketcan__utils_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SocketCAN工具（Utilities）。

<a id="details"></a>

```c
#include <zephyr/drivers/can.h>
#include <zephyr/net/socketcan.h>
#include <zephyr/sys/minmax.h>
```

查看此文件的源码。

SocketCAN 工具函数（utilities）：用于提供 SocketCAN 支持。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 53.1\_函数（Functions）

<a id="r_gaccedf1d7bf2131797e53a16dc93cd7e1"></a>

```c
static void socketcan_to_can_frame (const struct socketcan_frame *sframe, struct can_frame *zframe)
```

相关声明：[socketcan_to_can_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gaccedf1d7bf2131797e53a16dc93cd7e1)、[socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)、[can_frame](../hardware/P363_CAN帧结构.md)。

将 `socketcan_frame` 结构体转换为 `can_frame` 结构体。

<a id="r_ga49ffbe49124fdc472946fd0978f9a6d5"></a>

```c
static void socketcan_from_can_frame (const struct can_frame *zframe, struct socketcan_frame *sframe)
```

相关声明：[socketcan_from_can_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga49ffbe49124fdc472946fd0978f9a6d5)、[can_frame](../hardware/P363_CAN帧结构.md)、[socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)。

将 `can_frame` 结构体转换为 `socketcan_frame` 结构体。

<a id="r_ga040c4882d349cdc3c568f3580e823cba"></a>

```c
static void socketcan_to_can_filter (const struct socketcan_filter *sfilter, struct can_filter *zfilter)
```

相关声明：[socketcan_to_can_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga040c4882d349cdc3c568f3580e823cba)、[socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)、[can_filter](../hardware/P364_CAN过滤器结构.md)。

将 `socketcan_filter` 结构体转换为 `can_filter` 结构体。

<a id="r_gaf5cee7f0d6385c6fc4736e9399ed06b3"></a>

```c
static void socketcan_from_can_filter (const struct can_filter *zfilter, struct socketcan_filter *sfilter)
```

相关声明：[socketcan_from_can_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gaf5cee7f0d6385c6fc4736e9399ed06b3)、[can_filter](../hardware/P364_CAN过滤器结构.md)、[socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)。

将 `can_filter` 结构体转换为 `socketcan_filter` 结构体。


## 53.2\_原页交叉引用（Cross References）

- [zephyr/drivers/can.h](../can_driver_reference/P002_CAN驱动头文件源码.md)
- [zephyr/net/socketcan.h](../api_source_system_reference/P041_socketcan.h_源码浏览.md)
- [zephyr/sys/minmax.h](../numeric_reference/P002_最小最大值与限幅宏源码.md)
- [查看此文件的源码。](../api_source_reference/P803_socketcan_utils.h_源码浏览.md)
- [socketcan_to_can_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gaccedf1d7bf2131797e53a16dc93cd7e1)
- [socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)
- [can_frame](../hardware/P363_CAN帧结构.md)
- [socketcan_from_can_frame](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga49ffbe49124fdc472946fd0978f9a6d5)
- [socketcan_to_can_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga040c4882d349cdc3c568f3580e823cba)
- [socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)
- [can_filter](../hardware/P364_CAN过滤器结构.md)
- [socketcan_from_can_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#gaf5cee7f0d6385c6fc4736e9399ed06b3)

<a id="header-details"></a>

---

[上一章](P052_zephyr__mgmt__mcumgr__grp__settings_mgmt__settings_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P054_zephyr__net__ssh__client.h_文件参考.md)
