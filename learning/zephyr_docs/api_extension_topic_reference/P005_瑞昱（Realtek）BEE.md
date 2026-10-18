---
id: learning.zephyr-docs.api-extension-topic-reference.page-5
title: 瑞昱（Realtek）BEE
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bee.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_瑞昱（Realtek）BEE

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bee.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_bee_5Fclock_5Fcontrol_2Eh"></a>

```c
file bee_clock_control.h
```

相关声明：[bee_clock_control.h](../api_file_supplement_reference/P007_zephyr__drivers__clock_control__bee_clock_control.h_文件参考.md)。

Realtek BEE时钟控制（Clock Control）驱动的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga53e498c615522576d342141c50a4c2c1"></a>

```c
#define BEE_CLOCK_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(cctl))
```

相关声明：[BEE_CLOCK_CONTROLLER](#ga53e498c615522576d342141c50a4c2c1)、[DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

BEE 时钟控制器（Clock Controller）的全局设备句柄（Global Device Handle）。

## 5.3\_详细说明（Detailed Documentation）

<a id="ga53e498c615522576d342141c50a4c2c1"></a>

### `BEE_CLOCK_CONTROLLER`

```c
#define BEE_CLOCK_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(cctl))
```

```c
#include <zephyr/drivers/clock_control/bee_clock_control.h>
```

BEE 时钟控制器（Clock Controller）的全局设备句柄（Global Device Handle）。

本宏获取设备树（Devicetree）中以 `cctl` 为标签（Label）定义的主时钟控制器（Primary Clock Controller）的设备结构体（Device Structure）。

返回（Returns）：`const struct device*`，指向时钟控制器设备结构体（Clock Controller Device Structure）的指针。


## 5.4\_原页交叉引用（Cross References）

- [bee_clock_control.h](../api_file_supplement_reference/P007_zephyr__drivers__clock_control__bee_clock_control.h_文件参考.md)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_固件分发服务器模型（Firmware Distribution Server model）.md) · [返回大纲](大纲.md) · [下一章](P006_新唐（Nuvoton）NuMaker.md)
