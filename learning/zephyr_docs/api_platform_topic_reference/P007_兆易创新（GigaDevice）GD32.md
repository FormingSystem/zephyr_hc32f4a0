---
id: learning.zephyr-docs.api-platform-topic-reference.page-7
title: 兆易创新（GigaDevice）GD32
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__gd32.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_兆易创新（GigaDevice）GD32

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__gd32.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_gd32_2Eh"></a>

```c
file gd32.h
```

相关声明：[gd32.h](../api_file_supplement_reference/P034_zephyr__drivers__clock_control__gd32.h_文件参考.md)。

GigaDevice GD32设备的时钟控制定义（Clock Control Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga5da7e516717cf6df2b5dde546de06f73"></a>

```c
#define GD32_CLOCK_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(cctl))
```

相关声明：[GD32_CLOCK_CONTROLLER](#ga5da7e516717cf6df2b5dde546de06f73)、[DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

获取 GD32 时钟控制器（Clock Controller）的引用（Reference）。

## 7.3\_详细说明（Detailed Documentation）

<a id="ga5da7e516717cf6df2b5dde546de06f73"></a>

### `GD32_CLOCK_CONTROLLER`

```c
#define GD32_CLOCK_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(cctl))
```

```c
#include <zephyr/drivers/clock_control/gd32.h>
```

获取 GD32 时钟控制器（Clock Controller）的引用（Reference）。

GD32 只有一个时钟控制器（Clock Controller）：`cctl`。该设备不包含可能失败的初始化代码（Initialization Code），因此无需检查其是否就绪（Ready）即可使用。


## 7.4\_原页交叉引用（Cross References）

- [gd32.h](../api_file_supplement_reference/P034_zephyr__drivers__clock_control__gd32.h_文件参考.md)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_Silicon Labs Series 2 和 Series 3 设备树辅助功能（Devicetree helpers）.md) · [返回大纲](大纲.md) · [下一章](P008_德州仪器（Texas Instruments）MSPM0.md)
