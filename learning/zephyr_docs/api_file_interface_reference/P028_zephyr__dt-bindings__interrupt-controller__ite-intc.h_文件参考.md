---
id: learning.zephyr-docs.api-file-interface-reference.page-28
title: zephyr__dt-bindings__interrupt-controller__ite-intc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ite-intc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_dt-bindings\_\_interrupt-controller\_\_ite-intc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ite-intc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ITE IT8XXX2中断控制器（Interrupt Controller）的设备树宏。

查看此文件的源码。

<a id="details"></a>

ITE IT8XXX2中断控制器（Interrupt Controller）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.1\_宏定义（Macros）

<a id="r_ga9290a5f35a4d3514237ba9fb00936859"></a>

```c
#define IRQ_TYPE_NONE 0
```

相关声明：[IRQ_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#ga9290a5f35a4d3514237ba9fb00936859)。

不触发（No Trigger）。

<a id="r_gac95cadb7e2fafe537f8be5274baa1e75"></a>

```c
#define IRQ_TYPE_EDGE_RISING 1
```

相关声明：[IRQ_TYPE_EDGE_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#gac95cadb7e2fafe537f8be5274baa1e75)。

上升沿触发（rising edge trigger）。

<a id="r_gaab03b1a63f7cd7f3a43353048655135a"></a>

```c
#define IRQ_TYPE_EDGE_FALLING 2
```

相关声明：[IRQ_TYPE_EDGE_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#gaab03b1a63f7cd7f3a43353048655135a)。

下降沿触发（falling edge trigger）。

<a id="r_ga377225dde978048e3d918cedba2c125e"></a>

```c
#define IRQ_TYPE_EDGE_BOTH (IRQ_TYPE_EDGE_FALLING | IRQ_TYPE_EDGE_RISING)
```

相关声明：[IRQ_TYPE_EDGE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#ga377225dde978048e3d918cedba2c125e)、[IRQ_TYPE_EDGE_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#gaab03b1a63f7cd7f3a43353048655135a)、[IRQ_TYPE_EDGE_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#gac95cadb7e2fafe537f8be5274baa1e75)。

双边沿（Both Edges）。

<a id="r_ga82fc9c68723b62cf4071203f54bd321b"></a>

```c
#define IRQ_TYPE_LEVEL_HIGH 4
```

相关声明：[IRQ_TYPE_LEVEL_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#ga82fc9c68723b62cf4071203f54bd321b)。

高电平有效触发（active-high level trigger）。

<a id="r_gadfb5a6f2364155f99a90fba88ff9a670"></a>

```c
#define IRQ_TYPE_LEVEL_LOW 8
```

相关声明：[IRQ_TYPE_LEVEL_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#gadfb5a6f2364155f99a90fba88ff9a670)。

低电平有效触发（active-low level trigger）。


## 28.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/ite-intc_8h_source.html)
- [IRQ_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#ga9290a5f35a4d3514237ba9fb00936859)
- [IRQ_TYPE_EDGE_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#gac95cadb7e2fafe537f8be5274baa1e75)
- [IRQ_TYPE_EDGE_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#gaab03b1a63f7cd7f3a43353048655135a)
- [IRQ_TYPE_EDGE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#ga377225dde978048e3d918cedba2c125e)
- [IRQ_TYPE_LEVEL_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#ga82fc9c68723b62cf4071203f54bd321b)
- [IRQ_TYPE_LEVEL_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__intc.html#gadfb5a6f2364155f99a90fba88ff9a670)

<a id="header-details"></a>

---

[上一章](P027_zephyr__drivers__interrupt_controller__intc_thejas32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__dt-bindings__interrupt-controller__ite-it51xxx-intc.h_文件参考.md)
