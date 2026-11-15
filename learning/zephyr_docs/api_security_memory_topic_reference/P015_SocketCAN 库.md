---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-15
title: SocketCAN 库
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_SocketCAN 库

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SocketCAN 库

<a id="details"></a>

SocketCAN 库及实用工具（Utilities）。**引入版本（Since）：**1.14。**版本（Version）：**0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_socketcan_5Fframe"></a>

```c
struct socketcan_frame
```

相关声明：[socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)。

与Linux SocketCAN兼容的CAN帧（Frame）。

<a id="r_socketcan_5Ffilter"></a>

```c
struct socketcan_filter
```

相关声明：[socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)。

与Linux SocketCAN兼容的CAN过滤器（Filter）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga73214ba92fc9df9cf1af83b8d41626c5"></a>

```c
#define NET_CAN_RAW 1
```

相关声明：[NET_CAN_RAW](#ga73214ba92fc9df9cf1af83b8d41626c5)。

协议族（Protocol Family）`PF_CAN` 中的协议。

<a id="r_ga3ec3e39a63684e78a52cf9160c82c257"></a>

```c
#define SOCKETCAN_MAX_DLEN 8U
```

相关声明：[SOCKETCAN_MAX_DLEN](#ga3ec3e39a63684e78a52cf9160c82c257)。

SocketCAN 最大数据长度（Maximum Data Length）。

<a id="r_ga7d1f583cdc56ead407496713f3f22ac8"></a>

```c
#define CAN_MTU (sizeof(struct socketcan_frame))
```

相关声明：[CAN_MTU](#ga7d1f583cdc56ead407496713f3f22ac8)、[socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)。

CAN 帧的最大传输单元（MTU）。

<a id="r_gace1d124719f8eac5f59788811c4afaf4"></a>

```c
#define CANFD_BRS 0x01
```

相关声明：[CANFD_BRS](#gace1d124719f8eac5f59788811c4afaf4)。

比特率切换（Bit Rate Switch），即载荷数据使用第二种比特率。

<a id="r_gacfc1bf4466d32189a1708b4351df0794"></a>

```c
#define CANFD_ESI 0x02
```

相关声明：[CANFD_ESI](#gacfc1bf4466d32189a1708b4351df0794)。

发送节点的错误状态指示位（Error State Indicator）。

<a id="r_ga409cae306f00226ef192320f4f01f51c"></a>

```c
#define CANFD_FDF 0x04
```

相关声明：[CANFD_FDF](#ga409cae306f00226ef192320f4f01f51c)。

标记 CAN FD，以支持 `struct canfd_frame` 的双重用途（Dual Use）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.3\_函数（Functions）

<a id="r_gaccedf1d7bf2131797e53a16dc93cd7e1"></a>

```c
static void socketcan_to_can_frame (const struct socketcan_frame *sframe, struct can_frame *zframe)
```

相关声明：[socketcan_to_can_frame](#gaccedf1d7bf2131797e53a16dc93cd7e1)、[socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)、[can_frame](../hardware/P363_CAN帧结构.md)。

将 `socketcan_frame` 结构体转换为 `can_frame` 结构体。

<a id="r_ga49ffbe49124fdc472946fd0978f9a6d5"></a>

```c
static void socketcan_from_can_frame (const struct can_frame *zframe, struct socketcan_frame *sframe)
```

相关声明：[socketcan_from_can_frame](#ga49ffbe49124fdc472946fd0978f9a6d5)、[can_frame](../hardware/P363_CAN帧结构.md)、[socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)。

将 `can_frame` 结构体转换为 `socketcan_frame` 结构体。

<a id="r_ga040c4882d349cdc3c568f3580e823cba"></a>

```c
static void socketcan_to_can_filter (const struct socketcan_filter *sfilter, struct can_filter *zfilter)
```

相关声明：[socketcan_to_can_filter](#ga040c4882d349cdc3c568f3580e823cba)、[socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)、[can_filter](../hardware/P364_CAN过滤器结构.md)。

将 `socketcan_filter` 结构体转换为 `can_filter` 结构体。

<a id="r_gaf5cee7f0d6385c6fc4736e9399ed06b3"></a>

```c
static void socketcan_from_can_filter (const struct can_filter *zfilter, struct socketcan_filter *sfilter)
```

相关声明：[socketcan_from_can_filter](#gaf5cee7f0d6385c6fc4736e9399ed06b3)、[can_filter](../hardware/P364_CAN过滤器结构.md)、[socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)。

将 `can_filter` 结构体转换为 `socketcan_filter` 结构体。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 15.4\_Linux SocketCAN 兼容性（Compatibility）

以下结构体和函数提供与 Linux SocketCAN 所用 CAN 帧（CAN Frame）及 CAN 过滤器（CAN Filter）格式的兼容性。

<a id="r_ga35a7941726d1e22defd8c3098391ca8e"></a>

```c
typedef uint32_t socketcan_id_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[socketcan_id_t](#ga35a7941726d1e22defd8c3098391ca8e)。

为兼容 Linux SocketCAN 而提供的 CAN 标识符结构体（Identifier Structure）。

## 15.5\_详细说明（Detailed Documentation）

<a id="ga7d1f583cdc56ead407496713f3f22ac8"></a>

### `CAN_MTU`

```c
#define CAN_MTU (sizeof(struct socketcan_frame))
```

```c
#include <zephyr/net/socketcan.h>
```

CAN 帧的最大传输单元（MTU）。

<a id="gace1d124719f8eac5f59788811c4afaf4"></a>

### `CANFD_BRS`

```c
#define CANFD_BRS 0x01
```

```c
#include <zephyr/net/socketcan.h>
```

比特率切换（Bit Rate Switch），即载荷数据使用第二种比特率。

<a id="gacfc1bf4466d32189a1708b4351df0794"></a>

### `CANFD_ESI`

```c
#define CANFD_ESI 0x02
```

```c
#include <zephyr/net/socketcan.h>
```

发送节点的错误状态指示位（Error State Indicator）。

<a id="ga409cae306f00226ef192320f4f01f51c"></a>

### `CANFD_FDF`

```c
#define CANFD_FDF 0x04
```

```c
#include <zephyr/net/socketcan.h>
```

标记 CAN FD，以支持 `struct canfd_frame` 的双重用途（Dual Use）。

<a id="ga73214ba92fc9df9cf1af83b8d41626c5"></a>

### `NET_CAN_RAW`

```c
#define NET_CAN_RAW 1
```

```c
#include <zephyr/net/socketcan.h>
```

协议族（Protocol Family）`PF_CAN` 中的协议。

<a id="ga3ec3e39a63684e78a52cf9160c82c257"></a>

### `SOCKETCAN_MAX_DLEN`

```c
#define SOCKETCAN_MAX_DLEN 8U
```

```c
#include <zephyr/net/socketcan.h>
```

SocketCAN 最大数据长度（Maximum Data Length）。

<a id="ga35a7941726d1e22defd8c3098391ca8e"></a>

### `socketcan_id_t`

```c
typedef uint32_t socketcan_id_t
```

```c
#include <zephyr/net/socketcan.h>
```

为兼容 Linux SocketCAN 而提供的 CAN 标识符结构体（Identifier Structure）。

此类型包含以下字段（Fields）：

原始示例（Example）：

```c
+------+--------------------------------------------------------------+
| Bits | Description                                                  |
+======+==============================================================+
| 0-28 | CAN identifier (11/29 bit)                                   |
+------+--------------------------------------------------------------+
|  29  | Error message frame flag (0 = data frame, 1 = error message) |
+------+--------------------------------------------------------------+
|  30  | Remote transmission request flag (1 = RTR frame)             |
+------+--------------------------------------------------------------+
|  31  | Frame format flag (0 = standard 11 bit, 1 = extended 29 bit) |
+------+--------------------------------------------------------------+
```

<a id="gaf5cee7f0d6385c6fc4736e9399ed06b3"></a>

### `socketcan_from_can_filter()`

```c
void socketcan_from_can_filter ( const struct can_filter * zfilter, struct socketcan_filter * sfilter )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socketcan_utils.h>
```

将 `can_filter` 结构体转换为 `socketcan_filter` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `zfilter` | 指向 `can_filter` 结构体的指针。 |
| `sfilter` | 指向 `socketcan_filter` 结构体的指针。 |

<a id="ga49ffbe49124fdc472946fd0978f9a6d5"></a>

### `socketcan_from_can_frame()`

```c
void socketcan_from_can_frame ( const struct can_frame * zframe, struct socketcan_frame * sframe )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socketcan_utils.h>
```

将 `can_frame` 结构体转换为 `socketcan_frame` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `zframe` | 指向 `can_frame` 结构体的指针。 |
| `sframe` | 指向 `socketcan_frame` 结构体的指针。 |

<a id="ga040c4882d349cdc3c568f3580e823cba"></a>

### `socketcan_to_can_filter()`

```c
void socketcan_to_can_filter ( const struct socketcan_filter * sfilter, struct can_filter * zfilter )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socketcan_utils.h>
```

将 `socketcan_filter` 结构体转换为 `can_filter` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sfilter` | 指向 `socketcan_filter` 结构体的指针。 |
| `zfilter` | 指向 `can_filter` 结构体的指针。 |

<a id="gaccedf1d7bf2131797e53a16dc93cd7e1"></a>

### `socketcan_to_can_frame()`

```c
void socketcan_to_can_frame ( const struct socketcan_frame * sframe, struct can_frame * zframe )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/socketcan_utils.h>
```

将 `socketcan_frame` 结构体转换为 `can_frame` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sframe` | 指向 `sockecan_frame` 结构体的指针。

> 译注：原文此处拼写为 `sockecan_frame`，按原文保留。 |
| `zframe` | 指向 `can_frame` 结构体的指针。 |


## 15.6\_原页交叉引用（Cross References）

- [socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)
- [socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)
- [can_frame](../hardware/P363_CAN帧结构.md)
- [can_filter](../hardware/P364_CAN过滤器结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/net/socketcan.h](../api_file_network_device_reference/P036_zephyr__net__socketcan.h_文件参考.md)
- [zephyr/net/socketcan_utils.h](../api_file_interface_reference/P053_zephyr__net__socketcan_utils.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_复位域管理协议（Reset domain management Protocol）.md) · [返回大纲](大纲.md) · [下一章](P016_VL53L0X API主题.md)
