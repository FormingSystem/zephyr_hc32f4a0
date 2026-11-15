---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-20
title: zephyr__dt-bindings__clock__kinetis_sim.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kinetis__sim_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_dt-bindings\_\_clock\_\_kinetis\_sim.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/kinetis__sim_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.1\_宏定义（Macros）

<a id="r_a0684d47ba26fd4908fa10bb2c40894b9"></a>

```c
#define KINETIS_SIM_CORESYS_CLK 0
```

相关声明：[KINETIS_SIM_CORESYS_CLK](#a0684d47ba26fd4908fa10bb2c40894b9)。

<a id="r_ac083afde9dfc09d77be337ccec8613c6"></a>

```c
#define KINETIS_SIM_PLATFORM_CLK 1
```

相关声明：[KINETIS_SIM_PLATFORM_CLK](#ac083afde9dfc09d77be337ccec8613c6)。

<a id="r_a2fde3204425c877c1e0e409cac4d3f2c"></a>

```c
#define KINETIS_SIM_BUS_CLK 2
```

相关声明：[KINETIS_SIM_BUS_CLK](#a2fde3204425c877c1e0e409cac4d3f2c)。

<a id="r_a3b8468dcc04b28ec8c8e08c80848d9a1"></a>

```c
#define KINETIS_SIM_FAST_PERIPHERAL_CLK 5
```

相关声明：[KINETIS_SIM_FAST_PERIPHERAL_CLK](#a3b8468dcc04b28ec8c8e08c80848d9a1)。

<a id="r_aa1c209ae87c6971eb0f737baa768516b"></a>

```c
#define KINETIS_SIM_LPO_CLK 19
```

相关声明：[KINETIS_SIM_LPO_CLK](#aa1c209ae87c6971eb0f737baa768516b)。

<a id="r_a504e4baefda2add7e54aac44cadb428d"></a>

```c
#define KINETIS_SIM_DMAMUX_CLK KINETIS_SIM_BUS_CLK
```

相关声明：[KINETIS_SIM_DMAMUX_CLK](#a504e4baefda2add7e54aac44cadb428d)、[KINETIS_SIM_BUS_CLK](#a2fde3204425c877c1e0e409cac4d3f2c)。

<a id="r_a236c80919664e4d41414beab57ec1fea"></a>

```c
#define KINETIS_SIM_DMA_CLK KINETIS_SIM_CORESYS_CLK
```

相关声明：[KINETIS_SIM_DMA_CLK](#a236c80919664e4d41414beab57ec1fea)、[KINETIS_SIM_CORESYS_CLK](#a0684d47ba26fd4908fa10bb2c40894b9)。

<a id="r_aef35b68542fef8df938f4a7238299ae7"></a>

```c
#define KINETIS_SIM_SIM_SOPT7 7
```

相关声明：[KINETIS_SIM_SIM_SOPT7](#aef35b68542fef8df938f4a7238299ae7)。

<a id="r_ae5df2683a08aa500a911767f2a6c3b2c"></a>

```c
#define KINETIS_SIM_OSCERCLK 8
```

相关声明：[KINETIS_SIM_OSCERCLK](#ae5df2683a08aa500a911767f2a6c3b2c)。

<a id="r_aa6e2ca052a353c8ce8ba01d3373107c7"></a>

```c
#define KINETIS_SIM_MCGIRCLK 12
```

相关声明：[KINETIS_SIM_MCGIRCLK](#aa6e2ca052a353c8ce8ba01d3373107c7)。

<a id="r_a683b44ad7ce67bf22eedcd489a839e7c"></a>

```c
#define KINETIS_SIM_MCGPCLK 18
```

相关声明：[KINETIS_SIM_MCGPCLK](#a683b44ad7ce67bf22eedcd489a839e7c)。

<a id="r_a02aa044f83da5dca652327df3dbce5d8"></a>

```c
#define KINETIS_SIM_PLLFLLSEL_MCGFLLCLK 0
```

相关声明：[KINETIS_SIM_PLLFLLSEL_MCGFLLCLK](#a02aa044f83da5dca652327df3dbce5d8)。

<a id="r_a3b28905b525cde569f367e17274accf8"></a>

```c
#define KINETIS_SIM_PLLFLLSEL_MCGPLLCLK 1
```

相关声明：[KINETIS_SIM_PLLFLLSEL_MCGPLLCLK](#a3b28905b525cde569f367e17274accf8)。

<a id="r_a04fcbc9ade8eb94807dbf78922ee3177"></a>

```c
#define KINETIS_SIM_PLLFLLSEL_IRC48MHZ 3
```

相关声明：[KINETIS_SIM_PLLFLLSEL_IRC48MHZ](#a04fcbc9ade8eb94807dbf78922ee3177)。

<a id="r_ad107887d2ac9f8fed754889548a7ee92"></a>

```c
#define KINETIS_SIM_ER32KSEL_OSC32KCLK 0
```

相关声明：[KINETIS_SIM_ER32KSEL_OSC32KCLK](#ad107887d2ac9f8fed754889548a7ee92)。

<a id="r_a12c607155d49c7a83fce3619e63048a8"></a>

```c
#define KINETIS_SIM_ER32KSEL_RTC 2
```

相关声明：[KINETIS_SIM_ER32KSEL_RTC](#a12c607155d49c7a83fce3619e63048a8)。

<a id="r_a31926a82e92f3e7f9df4438661bdc381"></a>

```c
#define KINETIS_SIM_ER32KSEL_LPO1KHZ 3
```

相关声明：[KINETIS_SIM_ER32KSEL_LPO1KHZ](#a31926a82e92f3e7f9df4438661bdc381)。

<a id="r_a0ccfe586de3c6ab968c1440263fcd858"></a>

```c
#define KINETIS_SIM_ENET_CLK 4321
```

相关声明：[KINETIS_SIM_ENET_CLK](#a0ccfe586de3c6ab968c1440263fcd858)。

<a id="r_a61306e18fafbb5491db88600ab03ded5"></a>

```c
#define KINETIS_SIM_ENET_1588_CLK 4322
```

相关声明：[KINETIS_SIM_ENET_1588_CLK](#a61306e18fafbb5491db88600ab03ded5)。

<a id="r_a3a8c755702c4d9be4061d03a642c1f17"></a>

```c
#define KINETIS_SIM_CMP_CLK 4323
```

相关声明：[KINETIS_SIM_CMP_CLK](#a3a8c755702c4d9be4061d03a642c1f17)。

<a id="r_a7b08cb803f2791926e64838395a2023c"></a>

```c
#define KINETIS_SIM_VREF_CLK 4324
```

相关声明：[KINETIS_SIM_VREF_CLK](#a7b08cb803f2791926e64838395a2023c)。

<a id="r_a602fd24d5700e74aac914d0d15053b9e"></a>

```c
#define KINETIS_SIM_CLOCK(name, offset, bits)
```

相关声明：[KINETIS_SIM_CLOCK](#a602fd24d5700e74aac914d0d15053b9e)。

构造包含 3 个单元（Cell）的 SIM 时钟说明符（Clock Specifier）。

<a id="r_a9133025af86dcbbaa0a9794433e927c8"></a>

```c
#define KINETIS_SIM_CLOCK_MUX(name, offset, bits, mux_shift, mux_val)
```

相关声明：[KINETIS_SIM_CLOCK_MUX](#a9133025af86dcbbaa0a9794433e927c8)。

构造带有多路复用配置（Mux Configuration）、包含 3 个单元（Cell）的 SIM 时钟说明符（Clock Specifier）。

## 20.2\_详细说明（Detailed Documentation）

<a id="a2fde3204425c877c1e0e409cac4d3f2c"></a>

### `KINETIS_SIM_BUS_CLK`

```c
#define KINETIS_SIM_BUS_CLK 2
```

<a id="a602fd24d5700e74aac914d0d15053b9e"></a>

### `KINETIS_SIM_CLOCK`

```c
#define KINETIS_SIM_CLOCK ( name, offset, bits )
```

展开值（Value）：

```c
KINETIS_SIM_CLOCK_ID(name, offset, bits) offset bits
```

构造包含 3 个单元（Cell）的 SIM 时钟说明符（Clock Specifier）。

展开为 `<id offset bits>`，其中 `id` 编码门控与速率信息（Gate and Rate Information），`offset`／`bits` 保持显式形式，以便阅读，并供 ADC16 等使用者将它们作为独立单元（Cell）读取。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 时钟名称选择器（Clock Name Selector），即 `KINETIS_SIM_*_CLK`。 |
| `offset` | 门控寄存器偏移量（Gate Register Offset），例如 `0x1034`。 |
| `bits` | 门控位索引（Gate Bit Index），范围 `0..31`。 |

<a id="a9133025af86dcbbaa0a9794433e927c8"></a>

### `KINETIS_SIM_CLOCK_MUX`

```c
#define KINETIS_SIM_CLOCK_MUX ( name, offset, bits, mux_shift, mux_val )
```

展开值（Value）：

```c
KINETIS_SIM_CLOCK_ID_MUX(name, offset, bits, mux_shift, mux_val) offset bits
```

构造带有多路复用配置（Mux Configuration）、包含 3 个单元（Cell）的 SIM 时钟说明符（Clock Specifier）。

与 `KINETIS_SIM_CLOCK` 类似，但还编码多路复用寄存器字段及其值（Mux Register Field and Value），以支持 `clock_control_configure()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 时钟名称选择器（Clock Name Selector），即 `KINETIS_SIM_*_CLK`。 |
| `offset` | 门控寄存器偏移量（Gate Register Offset）。 |
| `bits` | 门控位索引（Gate Bit Index），范围 `0..31`。 |
| `mux_shift` | 多路复用字段（Mux Field）在多路复用寄存器（例如 SOPT2）中的位移。 |
| `mux_val` | 要写入多路复用字段（Mux Field）的值。 |

<a id="a3a8c755702c4d9be4061d03a642c1f17"></a>

### `KINETIS_SIM_CMP_CLK`

```c
#define KINETIS_SIM_CMP_CLK 4323
```

<a id="a0684d47ba26fd4908fa10bb2c40894b9"></a>

### `KINETIS_SIM_CORESYS_CLK`

```c
#define KINETIS_SIM_CORESYS_CLK 0
```

<a id="a236c80919664e4d41414beab57ec1fea"></a>

### `KINETIS_SIM_DMA_CLK`

```c
#define KINETIS_SIM_DMA_CLK KINETIS_SIM_CORESYS_CLK
```

<a id="a504e4baefda2add7e54aac44cadb428d"></a>

### `KINETIS_SIM_DMAMUX_CLK`

```c
#define KINETIS_SIM_DMAMUX_CLK KINETIS_SIM_BUS_CLK
```

<a id="a61306e18fafbb5491db88600ab03ded5"></a>

### `KINETIS_SIM_ENET_1588_CLK`

```c
#define KINETIS_SIM_ENET_1588_CLK 4322
```

<a id="a0ccfe586de3c6ab968c1440263fcd858"></a>

### `KINETIS_SIM_ENET_CLK`

```c
#define KINETIS_SIM_ENET_CLK 4321
```

<a id="a31926a82e92f3e7f9df4438661bdc381"></a>

### `KINETIS_SIM_ER32KSEL_LPO1KHZ`

```c
#define KINETIS_SIM_ER32KSEL_LPO1KHZ 3
```

<a id="ad107887d2ac9f8fed754889548a7ee92"></a>

### `KINETIS_SIM_ER32KSEL_OSC32KCLK`

```c
#define KINETIS_SIM_ER32KSEL_OSC32KCLK 0
```

<a id="a12c607155d49c7a83fce3619e63048a8"></a>

### `KINETIS_SIM_ER32KSEL_RTC`

```c
#define KINETIS_SIM_ER32KSEL_RTC 2
```

<a id="a3b8468dcc04b28ec8c8e08c80848d9a1"></a>

### `KINETIS_SIM_FAST_PERIPHERAL_CLK`

```c
#define KINETIS_SIM_FAST_PERIPHERAL_CLK 5
```

<a id="aa1c209ae87c6971eb0f737baa768516b"></a>

### `KINETIS_SIM_LPO_CLK`

```c
#define KINETIS_SIM_LPO_CLK 19
```

<a id="aa6e2ca052a353c8ce8ba01d3373107c7"></a>

### `KINETIS_SIM_MCGIRCLK`

```c
#define KINETIS_SIM_MCGIRCLK 12
```

<a id="a683b44ad7ce67bf22eedcd489a839e7c"></a>

### `KINETIS_SIM_MCGPCLK`

```c
#define KINETIS_SIM_MCGPCLK 18
```

<a id="ae5df2683a08aa500a911767f2a6c3b2c"></a>

### `KINETIS_SIM_OSCERCLK`

```c
#define KINETIS_SIM_OSCERCLK 8
```

<a id="ac083afde9dfc09d77be337ccec8613c6"></a>

### `KINETIS_SIM_PLATFORM_CLK`

```c
#define KINETIS_SIM_PLATFORM_CLK 1
```

<a id="a04fcbc9ade8eb94807dbf78922ee3177"></a>

### `KINETIS_SIM_PLLFLLSEL_IRC48MHZ`

```c
#define KINETIS_SIM_PLLFLLSEL_IRC48MHZ 3
```

<a id="a02aa044f83da5dca652327df3dbce5d8"></a>

### `KINETIS_SIM_PLLFLLSEL_MCGFLLCLK`

```c
#define KINETIS_SIM_PLLFLLSEL_MCGFLLCLK 0
```

<a id="a3b28905b525cde569f367e17274accf8"></a>

### `KINETIS_SIM_PLLFLLSEL_MCGPLLCLK`

```c
#define KINETIS_SIM_PLLFLLSEL_MCGPLLCLK 1
```

<a id="aef35b68542fef8df938f4a7238299ae7"></a>

### `KINETIS_SIM_SIM_SOPT7`

```c
#define KINETIS_SIM_SIM_SOPT7 7
```

<a id="a7b08cb803f2791926e64838395a2023c"></a>

### `KINETIS_SIM_VREF_CLK`

```c
#define KINETIS_SIM_VREF_CLK 4324
```


## 20.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P047_kinetis_sim.h_源码浏览.md)
- [clock_control_configure()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaf5e4b13798955fcc891c080b9967ab06)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P019_zephyr__dt-bindings__pwm__it51xxx_pwm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__sys__linear_range.h_文件参考.md)
