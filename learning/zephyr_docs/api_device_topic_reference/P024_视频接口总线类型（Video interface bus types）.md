---
id: learning.zephyr-docs.api-device-topic-reference.page-24
title: 视频接口总线类型（Video interface bus types）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__bus__types.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_视频接口总线类型（Video interface bus types）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__bus__types.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备树 `bus-type` 属性使用的总线类型值。

<a id="details"></a>

设备树 `bus-type` 属性所用的总线类型值（bus type values）。这些值标识连接两个视频端点（video endpoints）的数据总线类型，应作为设备树视频端点节点的 `bus-type` 属性使用。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.1\_宏定义（Macros）

<a id="r_ga19f970d881586071a6408efd4c3eaf8f"></a>

```c
#define VIDEO_BUS_TYPE_CSI2_CPHY 1
```

相关声明：[VIDEO_BUS_TYPE_CSI2_CPHY](#ga19f970d881586071a6408efd4c3eaf8f)。

MIPI CSI-2 的 C-PHY 接口。

<a id="r_ga355e23d547b04dcdb7bb8f56ceaffe23"></a>

```c
#define VIDEO_BUS_TYPE_CSI1 2
```

相关声明：[VIDEO_BUS_TYPE_CSI1](#ga355e23d547b04dcdb7bb8f56ceaffe23)。

MIPI 摄像头串行接口 1（CSI-1）。

<a id="r_gad03a1f6823d78c9134f69b2436759975"></a>

```c
#define VIDEO_BUS_TYPE_CCP2 3
```

相关声明：[VIDEO_BUS_TYPE_CCP2](#gad03a1f6823d78c9134f69b2436759975)。

标准移动成像架构（SMIA）的紧凑摄像头端口 2（Compact Camera Port 2，CCP2）。

<a id="r_ga8845ccc1018d6b5e1974ecb6c3529641"></a>

```c
#define VIDEO_BUS_TYPE_CSI2_DPHY 4
```

相关声明：[VIDEO_BUS_TYPE_CSI2_DPHY](#ga8845ccc1018d6b5e1974ecb6c3529641)。

MIPI CSI-2 的 D-PHY 接口。

<a id="r_ga7c2d8ab4283d3881203059be91963b1e"></a>

```c
#define VIDEO_BUS_TYPE_PARALLEL 5
```

相关声明：[VIDEO_BUS_TYPE_PARALLEL](#ga7c2d8ab4283d3881203059be91963b1e)。

并行接口（Parallel）。

<a id="r_ga83e90c80864bb7e18a985b9ce0202107"></a>

```c
#define VIDEO_BUS_TYPE_BT656 6
```

相关声明：[VIDEO_BUS_TYPE_BT656](#ga83e90c80864bb7e18a985b9ce0202107)。

BT.656 接口。

## 24.2\_详细说明（Detailed Documentation）

<a id="ga83e90c80864bb7e18a985b9ce0202107"></a>

### `VIDEO_BUS_TYPE_BT656`

```c
#define VIDEO_BUS_TYPE_BT656 6
```

```c
#include <zephyr/dt-bindings/video/video-interfaces.h>
```

BT.656 接口。

<a id="gad03a1f6823d78c9134f69b2436759975"></a>

### `VIDEO_BUS_TYPE_CCP2`

```c
#define VIDEO_BUS_TYPE_CCP2 3
```

```c
#include <zephyr/dt-bindings/video/video-interfaces.h>
```

标准移动成像架构（SMIA）的紧凑摄像头端口 2（Compact Camera Port 2，CCP2）。

<a id="ga355e23d547b04dcdb7bb8f56ceaffe23"></a>

### `VIDEO_BUS_TYPE_CSI1`

```c
#define VIDEO_BUS_TYPE_CSI1 2
```

```c
#include <zephyr/dt-bindings/video/video-interfaces.h>
```

MIPI 摄像头串行接口 1（CSI-1）。

<a id="ga19f970d881586071a6408efd4c3eaf8f"></a>

### `VIDEO_BUS_TYPE_CSI2_CPHY`

```c
#define VIDEO_BUS_TYPE_CSI2_CPHY 1
```

```c
#include <zephyr/dt-bindings/video/video-interfaces.h>
```

MIPI CSI-2 的 C-PHY 接口。

<a id="ga8845ccc1018d6b5e1974ecb6c3529641"></a>

### `VIDEO_BUS_TYPE_CSI2_DPHY`

```c
#define VIDEO_BUS_TYPE_CSI2_DPHY 4
```

```c
#include <zephyr/dt-bindings/video/video-interfaces.h>
```

MIPI CSI-2 的 D-PHY 接口。

<a id="ga7c2d8ab4283d3881203059be91963b1e"></a>

### `VIDEO_BUS_TYPE_PARALLEL`

```c
#define VIDEO_BUS_TYPE_PARALLEL 5
```

```c
#include <zephyr/dt-bindings/video/video-interfaces.h>
```

并行接口（Parallel）。


## 24.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/video/video-interfaces.h](../api_file_management_reference/P047_zephyr__dt-bindings__video__video-interfaces.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P023_视频流（Video Stream）.md) · [返回大纲](大纲.md)
