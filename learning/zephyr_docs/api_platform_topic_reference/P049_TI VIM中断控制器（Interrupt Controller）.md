---
id: learning.zephyr-docs.api-platform-topic-reference.page-49
title: TI VIM中断控制器（Interrupt Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_TI VIM中断控制器（Interrupt Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments 向量中断管理器（Vectored Interrupt Manager，VIM）的设备树标志。

<a id="details"></a>

Texas Instruments 向量中断管理器（Vectored Interrupt Manager，VIM）的设备树标志（Devicetree Flags）。与 `ti,vim` 兼容中断控制器配合使用的触发类型标志（Trigger-Type Flags）和优先级标志（Priority Flags）。一个中断由四个单元（Cells）描述：中断组（Interrupt Group）、中断编号（Interrupt Number）、触发类型（`IRQ_TYPE_LEVEL` 或 `IRQ_TYPE_EDGE`）及优先级（Priority）。

```c
&some_device {
        interrupts = <0 64 IRQ_TYPE_EDGE IRQ_DEFAULT_PRIORITY>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 49.1\_文件（Files）

<a id="r_ti-vim_2Eh"></a>

```c
file ti-vim.h
```

相关声明：[ti-vim.h](../api_file_runtime_reference/P070_zephyr__dt-bindings__interrupt-controller__ti-vim.h_文件参考.md)。

TI向量中断管理器（VIM）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 49.2\_宏定义（Macros）

<a id="r_ga296e915831223a614a6ea87dbe7735e7"></a>

```c
#define IRQ_TYPE_LEVEL BIT(1)
```

相关声明：[IRQ_TYPE_LEVEL](#ga296e915831223a614a6ea87dbe7735e7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电平触发中断（Level-Triggered Interrupt）。

<a id="r_gaff68b0efbc719bc28f0d56c9ba8607bc"></a>

```c
#define IRQ_TYPE_EDGE BIT(2)
```

相关声明：[IRQ_TYPE_EDGE](#gaff68b0efbc719bc28f0d56c9ba8607bc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

边沿触发中断（Edge-Triggered Interrupt）。

<a id="r_ga2dbeaa0c017cdff0982b381cc96f0a6c"></a>

```c
#define IRQ_DEFAULT_PRIORITY 0xf
```

相关声明：[IRQ_DEFAULT_PRIORITY](#ga2dbeaa0c017cdff0982b381cc96f0a6c)。

默认中断优先级（Default Interrupt Priority）。

## 49.3\_详细说明（Detailed Documentation）

<a id="ga2dbeaa0c017cdff0982b381cc96f0a6c"></a>

### `IRQ_DEFAULT_PRIORITY`

```c
#define IRQ_DEFAULT_PRIORITY 0xf
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ti-vim.h>
```

默认中断优先级（Default Interrupt Priority）。

<a id="gaff68b0efbc719bc28f0d56c9ba8607bc"></a>

### `IRQ_TYPE_EDGE`

```c
#define IRQ_TYPE_EDGE BIT(2)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ti-vim.h>
```

边沿触发中断（Edge-Triggered Interrupt）。

<a id="ga296e915831223a614a6ea87dbe7735e7"></a>

### `IRQ_TYPE_LEVEL`

```c
#define IRQ_TYPE_LEVEL BIT(1)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ti-vim.h>
```

电平触发中断（Level-Triggered Interrupt）。


## 49.4\_原页交叉引用（Cross References）

- [ti-vim.h](../api_file_runtime_reference/P070_zephyr__dt-bindings__interrupt-controller__ti-vim.h_文件参考.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [IRQ_TYPE_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__arm__gic.html#ga296e915831223a614a6ea87dbe7735e7)
- [IRQ_TYPE_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__arm__gic.html#gaff68b0efbc719bc28f0d56c9ba8607bc)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P048_Renesas RA8T1 事件链接控制器（ELC）的设备树宏.md) · [返回大纲](大纲.md) · [下一章](P050_虚拟二层_驱动支持函数（Dummy L2_driver Support Functions）.md)
