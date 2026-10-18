---
id: learning.zephyr-docs.api-file-service-reference.page-53
title: zephyr__bluetooth__mesh__statistic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_zephyr\_\_bluetooth\_\_mesh\_\_statistic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh统计（Statistics）的API。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

蓝牙Mesh统计（Statistics）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 53.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fstatistic"></a>

```c
struct bt_mesh_statistic
```

相关声明：[bt_mesh_statistic](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md)。

保存Mesh帧处理统计信息的结构。

<a id="r_bt_5Fmesh_5Flpn_5Ftiming"></a>

```c
struct bt_mesh_lpn_timing
```

相关声明：[bt_mesh_lpn_timing](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md)。

根据时间戳得到的低功耗节点（LPN）好友关系时序测量值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 53.2\_函数（Functions）

<a id="r_ga8c1e9de2f323111ee95d0903b5ecb2fd"></a>

```c
void bt_mesh_stat_get (struct bt_mesh_statistic *st)
```

相关声明：[bt_mesh_stat_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#ga8c1e9de2f323111ee95d0903b5ecb2fd)、[bt_mesh_statistic](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md)。

获取网状网络帧处理统计（Mesh Frame Handling Statistic）。

<a id="r_gabe8c893466f24e9b75fe51ae5ea65132"></a>

```c
void bt_mesh_stat_reset (void)
```

相关声明：[bt_mesh_stat_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#gabe8c893466f24e9b75fe51ae5ea65132)。

重置网状网络帧处理统计（Mesh Frame Handling Statistic）。

<a id="r_ga240344c421ff810578b9d0e06a11fe56"></a>

```c
int bt_mesh_stat_lpn_timing_get (struct bt_mesh_lpn_timing *timing)
```

相关声明：[bt_mesh_stat_lpn_timing_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#ga240344c421ff810578b9d0e06a11fe56)、[bt_mesh_lpn_timing](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md)。

获取测得的低功耗节点友谊轮询时序（LPN Friendship Poll Timing）。

<a id="r_gaf4ca44edb393329569052707aa9a8f18"></a>

```c
void bt_mesh_stat_lpn_timing_reset (void)
```

相关声明：[bt_mesh_stat_lpn_timing_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#gaf4ca44edb393329569052707aa9a8f18)。

重置测得的低功耗节点友谊轮询时序统计（LPN Friendship Poll Timing Statistics）。


## 53.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P817_statistic.h_源码浏览.md)
- [bt_mesh_statistic](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md)
- [bt_mesh_lpn_timing](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md)
- [bt_mesh_stat_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#ga8c1e9de2f323111ee95d0903b5ecb2fd)
- [bt_mesh_stat_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#gabe8c893466f24e9b75fe51ae5ea65132)
- [bt_mesh_stat_lpn_timing_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#ga240344c421ff810578b9d0e06a11fe56)
- [bt_mesh_stat_lpn_timing_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#gaf4ca44edb393329569052707aa9a8f18)

<a id="header-details"></a>

---

[上一章](P052_zephyr__bluetooth__mesh__sol_pdu_rpl_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P054_zephyr__dt-bindings__power__stm32h7rs_iocell.h_文件参考.md)
