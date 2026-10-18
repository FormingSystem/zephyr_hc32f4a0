---
id: learning.zephyr-docs.api-file-supplement-reference.page-7
title: zephyr__drivers__clock_control__bee_clock_control.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bee__clock__control_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_clock\_control\_\_bee\_clock\_control.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bee__clock__control_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek BEE时钟控制（Clock Control）驱动的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

Realtek BEE时钟控制（Clock Control）驱动的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_ga53e498c615522576d342141c50a4c2c1"></a>

```c
#define BEE_CLOCK_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(cctl))
```

相关声明：[BEE_CLOCK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bee.html#ga53e498c615522576d342141c50a4c2c1)、[DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

BEE 时钟控制器（Clock Controller）的全局设备句柄（Global Device Handle）。


## 7.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P058_bee_clock_control.h_源码浏览.md)
- [BEE_CLOCK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bee.html#ga53e498c615522576d342141c50a4c2c1)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

<a id="header-details"></a>

---

[上一章](P006_zephyr__dt-bindings__dma__bee-dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__retention__blinfo.h_文件参考.md)
