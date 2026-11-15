---
id: learning.zephyr-docs.api-protocol-topic-reference.page-18
title: ITE IT51XXX中断控制器（Interrupt Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it51xxx__intc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_ITE IT51XXX中断控制器（Interrupt Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it51xxx__intc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ITE IT51XXX 中断控制器（Interrupt Controller，INTC）的设备树宏。

<a id="details"></a>

ITE IT51XXX 中断控制器（Interrupt Controller，INTC）的设备树宏。这些宏用于编码兼容 `ite,it51xxx-intc` 的中断控制器的中断单元（interrupt cells）。一个中断由两个单元描述：中断编号，以及触发类型（下方某个 `IRQ_TYPE_*` 标志）。中断编号遵循 `IT51XXX_IRQ_<source>` 命名模式，其中 `<source>` 为 IT51XXX 中断源名称，例如 `IT51XXX_IRQ_TIMER1` 或 `IT51XXX_IRQ_SMB_A`。下方保留原始配置示例。

```c
&timer {
        interrupts = <IT51XXX_IRQ_TIMER1 IRQ_TYPE_EDGE_RISING>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 18.1\_文件（Files）

<a id="r_ite-it51xxx-intc_2Eh"></a>

```c
file ite-it51xxx-intc.h
```

相关声明：[ite-it51xxx-intc.h](../api_file_interface_reference/P029_zephyr__dt-bindings__interrupt-controller__ite-it51xxx-intc.h_文件参考.md)。

ITE IT51XXX中断控制器（Interrupt Controller）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="r_ga9290a5f35a4d3514237ba9fb00936859"></a>

```c
#define IRQ_TYPE_NONE 0
```

相关声明：[IRQ_TYPE_NONE](#ga9290a5f35a4d3514237ba9fb00936859)。

不触发（No Trigger）。

<a id="r_gac95cadb7e2fafe537f8be5274baa1e75"></a>

```c
#define IRQ_TYPE_EDGE_RISING 1
```

相关声明：[IRQ_TYPE_EDGE_RISING](#gac95cadb7e2fafe537f8be5274baa1e75)。

上升沿触发（rising edge trigger）。

<a id="r_gaab03b1a63f7cd7f3a43353048655135a"></a>

```c
#define IRQ_TYPE_EDGE_FALLING 2
```

相关声明：[IRQ_TYPE_EDGE_FALLING](#gaab03b1a63f7cd7f3a43353048655135a)。

下降沿触发（falling edge trigger）。

<a id="r_ga377225dde978048e3d918cedba2c125e"></a>

```c
#define IRQ_TYPE_EDGE_BOTH (IRQ_TYPE_EDGE_FALLING | IRQ_TYPE_EDGE_RISING)
```

相关声明：[IRQ_TYPE_EDGE_BOTH](#ga377225dde978048e3d918cedba2c125e)、[IRQ_TYPE_EDGE_FALLING](#gaab03b1a63f7cd7f3a43353048655135a)、[IRQ_TYPE_EDGE_RISING](#gac95cadb7e2fafe537f8be5274baa1e75)。

双边沿（Both Edges）。

<a id="r_ga82fc9c68723b62cf4071203f54bd321b"></a>

```c
#define IRQ_TYPE_LEVEL_HIGH 4
```

相关声明：[IRQ_TYPE_LEVEL_HIGH](#ga82fc9c68723b62cf4071203f54bd321b)。

高电平有效触发（active-high level trigger）。

<a id="r_gadfb5a6f2364155f99a90fba88ff9a670"></a>

```c
#define IRQ_TYPE_LEVEL_LOW 8
```

相关声明：[IRQ_TYPE_LEVEL_LOW](#gadfb5a6f2364155f99a90fba88ff9a670)。

低电平有效触发（active-low level trigger）。

## 18.3\_详细说明（Detailed Documentation）

<a id="ga377225dde978048e3d918cedba2c125e"></a>

### `IRQ_TYPE_EDGE_BOTH`

```c
#define IRQ_TYPE_EDGE_BOTH (IRQ_TYPE_EDGE_FALLING | IRQ_TYPE_EDGE_RISING)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ite-it51xxx-intc.h>
```

双边沿（Both Edges）。

<a id="gaab03b1a63f7cd7f3a43353048655135a"></a>

### `IRQ_TYPE_EDGE_FALLING`

```c
#define IRQ_TYPE_EDGE_FALLING 2
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ite-it51xxx-intc.h>
```

下降沿触发（falling edge trigger）。

<a id="gac95cadb7e2fafe537f8be5274baa1e75"></a>

### `IRQ_TYPE_EDGE_RISING`

```c
#define IRQ_TYPE_EDGE_RISING 1
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ite-it51xxx-intc.h>
```

上升沿触发（rising edge trigger）。

<a id="ga82fc9c68723b62cf4071203f54bd321b"></a>

### `IRQ_TYPE_LEVEL_HIGH`

```c
#define IRQ_TYPE_LEVEL_HIGH 4
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ite-it51xxx-intc.h>
```

高电平有效触发（active-high level trigger）。

<a id="gadfb5a6f2364155f99a90fba88ff9a670"></a>

### `IRQ_TYPE_LEVEL_LOW`

```c
#define IRQ_TYPE_LEVEL_LOW 8
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ite-it51xxx-intc.h>
```

低电平有效触发（active-low level trigger）。

<a id="ga9290a5f35a4d3514237ba9fb00936859"></a>

### `IRQ_TYPE_NONE`

```c
#define IRQ_TYPE_NONE 0
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ite-it51xxx-intc.h>
```

不触发（No Trigger）。


## 18.4\_原页交叉引用（Cross References）

- [ite-it51xxx-intc.h](../api_file_interface_reference/P029_zephyr__dt-bindings__interrupt-controller__ite-it51xxx-intc.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P017_ITE IT8XXX2中断控制器（Interrupt Controller）.md) · [返回大纲](大纲.md) · [下一章](P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md)
