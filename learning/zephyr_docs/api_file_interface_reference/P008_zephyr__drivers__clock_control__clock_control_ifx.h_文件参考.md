---
id: learning.zephyr-docs.api-file-interface-reference.page-8
title: zephyr__drivers__clock_control__clock_control_ifx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_clock\_control\_\_clock\_control\_ifx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon时钟控制（Clock Control）驱动的公共API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/devicetree.h>
```

查看此文件的源码。

Infineon时钟控制（Clock Control）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_ifx_5Fclk"></a>

```c
struct ifx_clk
```

相关声明：[ifx_clk](../device_power_control_model_reference/P019_ifx_clk_结构体.md)。

Infineon时钟说明符（Clock Specifier）。

<a id="r_ifx_5Fclk_5Fperi"></a>

```c
struct ifx_clk_peri
```

相关声明：[ifx_clk_peri](../device_power_control_model_reference/P020_ifx_clk_peri_结构体.md)。

Infineon外设时钟说明符（Peripheral Clock Specifier）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_a84782615816292ebedece0ab383b9cac"></a>

```c
#define IFX_CLK_PLL 0
```

相关声明：[IFX_CLK_PLL](#a84782615816292ebedece0ab383b9cac)。

锁相环（PLL）时钟类型。

<a id="r_a799c03939ef0ec79d0c67d9a42e75b1e"></a>

```c
#define IFX_CLK_HF 1
```

相关声明：[IFX_CLK_HF](#a799c03939ef0ec79d0c67d9a42e75b1e)。

高频（high-frequency）时钟类型。

<a id="r_a5dc6f30e8a3904a8b55442a79e96ca70"></a>

```c
#define IFX_CLK_LF 2
```

相关声明：[IFX_CLK_LF](#a5dc6f30e8a3904a8b55442a79e96ca70)。

低频（low-frequency）时钟类型。

<a id="r_a7ead625127fa9a9196dd99434f180535"></a>

```c
#define IFX_CLK_PERI_DT_SPEC_GET(node_id)
```

相关声明：[IFX_CLK_PERI_DT_SPEC_GET](#a7ead625127fa9a9196dd99434f180535)。

根据外设的 `clocks` 属性及时钟目标属性（外设时钟 ID），构造 `struct ifx_clk_peri`。

<a id="r_a0a25f5bd30632c2b0efea7b91eac61a9"></a>

```c
#define IFX_CLK_PERI_DT_INST_SPEC_GET(inst)
```

相关声明：[IFX_CLK_PERI_DT_INST_SPEC_GET](#a0a25f5bd30632c2b0efea7b91eac61a9)。

与 `IFX_CLK_PERI_DT_SPEC_GET()` 类似，但使用 `DT_DRV_COMPAT` 实例编号。

## 8.3\_详细说明（Detailed Documentation）

<a id="a799c03939ef0ec79d0c67d9a42e75b1e"></a>

### `IFX_CLK_HF`

```c
#define IFX_CLK_HF 1
```

高频（high-frequency）时钟类型。

<a id="a5dc6f30e8a3904a8b55442a79e96ca70"></a>

### `IFX_CLK_LF`

```c
#define IFX_CLK_LF 2
```

低频（low-frequency）时钟类型。

<a id="a0a25f5bd30632c2b0efea7b91eac61a9"></a>

### `IFX_CLK_PERI_DT_INST_SPEC_GET`

```c
#define IFX_CLK_PERI_DT_INST_SPEC_GET ( inst)
```

展开值（Value）：

```c
IFX_CLK_PERI_DT_SPEC_GET(DT_DRV_INST(inst))
```

与 `IFX_CLK_PERI_DT_SPEC_GET()` 类似，但使用 `DT_DRV_COMPAT` 实例编号。

<a id="a7ead625127fa9a9196dd99434f180535"></a>

### `IFX_CLK_PERI_DT_SPEC_GET`

```c
#define IFX_CLK_PERI_DT_SPEC_GET ( node_id)
```

展开值（Value）：

```c
{                                                       \
        .rootclk_id = DT_PROP(node_id, clk_dst),        \
        .div_ord = DT_DEP_ORD(DT_CLOCKS_CTLR(node_id)), \
}
```

根据外设的 `clocks` 属性及时钟目标属性（外设时钟 ID），构造 `struct ifx_clk_peri`。

<a id="a84782615816292ebedece0ab383b9cac"></a>

### `IFX_CLK_PLL`

```c
#define IFX_CLK_PLL 0
```

锁相环（PLL）时钟类型。


## 8.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P100_clock_control_ifx.h_源码浏览.md)
- [ifx_clk](../device_power_control_model_reference/P019_ifx_clk_结构体.md)
- [ifx_clk_peri](../device_power_control_model_reference/P020_ifx_clk_peri_结构体.md)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_DEP_ORD](../dt_node_reference/P004_设备树依赖顺序宏.md#ga5b96dccfd349dd0ddba1812aa942c1bd)
- [DT_CLOCKS_CTLR](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga69795ece1f4a46e2c26a8e2dbb452f23)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aclock__control__ifx_8h_html_a7ead625127fa9a9196dd99434f180535"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__devicetree-clocks_html_ga69795ece1f4a46e2c26a8e2dbb452f23"></a>
<a id="agroup__devicetree-dep-ord_html_ga5b96dccfd349dd0ddba1812aa942c1bd"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>

---

[上一章](P007_zephyr__bluetooth__audio__ccid.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__net__coap_oscore.h_文件参考.md)
