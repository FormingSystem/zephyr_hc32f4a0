---
id: learning.zephyr-docs.api-protocol-topic-reference.page-8
title: 统计（Statistic）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_统计（Statistic）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

统计（Statistic）

<a id="details"></a>

统计（Statistic）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

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

## 8.2\_函数（Functions）

<a id="r_ga8c1e9de2f323111ee95d0903b5ecb2fd"></a>

```c
void bt_mesh_stat_get (struct bt_mesh_statistic *st)
```

相关声明：[bt_mesh_stat_get](#ga8c1e9de2f323111ee95d0903b5ecb2fd)、[bt_mesh_statistic](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md)。

获取网状网络帧处理统计（Mesh Frame Handling Statistic）。

<a id="r_gabe8c893466f24e9b75fe51ae5ea65132"></a>

```c
void bt_mesh_stat_reset (void)
```

相关声明：[bt_mesh_stat_reset](#gabe8c893466f24e9b75fe51ae5ea65132)。

重置网状网络帧处理统计（Mesh Frame Handling Statistic）。

<a id="r_ga240344c421ff810578b9d0e06a11fe56"></a>

```c
int bt_mesh_stat_lpn_timing_get (struct bt_mesh_lpn_timing *timing)
```

相关声明：[bt_mesh_stat_lpn_timing_get](#ga240344c421ff810578b9d0e06a11fe56)、[bt_mesh_lpn_timing](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md)。

获取测得的低功耗节点友谊轮询时序（LPN Friendship Poll Timing）。

<a id="r_gaf4ca44edb393329569052707aa9a8f18"></a>

```c
void bt_mesh_stat_lpn_timing_reset (void)
```

相关声明：[bt_mesh_stat_lpn_timing_reset](#gaf4ca44edb393329569052707aa9a8f18)。

重置测得的低功耗节点友谊轮询时序统计（LPN Friendship Poll Timing Statistics）。

## 8.3\_详细说明（Detailed Documentation）

<a id="ga8c1e9de2f323111ee95d0903b5ecb2fd"></a>

### `bt_mesh_stat_get()`

```c
void bt_mesh_stat_get ( struct bt_mesh_statistic * st)
```

```c
#include <zephyr/bluetooth/mesh/statistic.h>
```

获取网状网络帧处理统计（Mesh Frame Handling Statistic）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `st` | 蓝牙网状网络（Bluetooth Mesh）统计信息。 |

<a id="ga240344c421ff810578b9d0e06a11fe56"></a>

### `bt_mesh_stat_lpn_timing_get()`

```c
int bt_mesh_stat_lpn_timing_get ( struct bt_mesh_lpn_timing * timing)
```

```c
#include <zephyr/bluetooth/mesh/statistic.h>
```

获取测得的低功耗节点友谊轮询时序（LPN Friendship Poll Timing）。

返回根据时间戳得到的测量值，反映空中实际观察到的接收延迟（ReceiveDelay）和接收窗口（ReceiveWindow）。分别在轮询发送完成、扫描器启用以及响应接收时使用 `k_uptime_get()` 采集时间戳。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timing` | 指向待填充结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOTSUP` | 低功耗节点（LPN）或统计功能未启用。 |
| `-EINVAL` | 空指针（NULL pointer）。 |

<a id="gaf4ca44edb393329569052707aa9a8f18"></a>

### `bt_mesh_stat_lpn_timing_reset()`

```c
void bt_mesh_stat_lpn_timing_reset ( void )
```

```c
#include <zephyr/bluetooth/mesh/statistic.h>
```

重置测得的低功耗节点友谊轮询时序统计（LPN Friendship Poll Timing Statistics）。

<a id="gabe8c893466f24e9b75fe51ae5ea65132"></a>

### `bt_mesh_stat_reset()`

```c
void bt_mesh_stat_reset ( void )
```

```c
#include <zephyr/bluetooth/mesh/statistic.h>
```

重置网状网络帧处理统计（Mesh Frame Handling Statistic）。


## 8.4\_原页交叉引用（Cross References）

- [bt_mesh_statistic](../bluetooth_mesh_model_reference/P101_bt_mesh_statistic_结构体.md)
- [bt_mesh_lpn_timing](../bluetooth_mesh_model_reference/P073_bt_mesh_lpn_timing_结构体.md)
- [zephyr/bluetooth/mesh/statistic.h](../api_file_service_reference/P053_zephyr__bluetooth__mesh__statistic.h_文件参考.md)
- [k_uptime_get()](../timer_reference/P086_系统时钟公共接口.md#gae3e992cd3257c23d5b26d765fcbb2b69)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_远程配网模型（Remote Provisioning models）.md) · [返回大纲](大纲.md) · [下一章](P009_ARM CMSDK API主题.md)
