---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-10
title: clock_mchp_subsys_dpll_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__dpll__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_clock\_mchp\_subsys\_dpll\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__dpll__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

数字锁相环（Digital Phase-Locked Loop，DPLL）配置结构体。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h>
```

<a id="details"></a>

数字锁相环（Digital Phase-Locked Loop，DPLL）配置结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a945f0d0e331b4512cfcea6f298b03fd2"></a>

```c
uint16_t feedback_divider_factor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[feedback_divider_factor](#a945f0d0e331b4512cfcea6f298b03fd2)。

PLL 压控振荡器（Voltage-Controlled Oscillator，VCO）输出频率与参考输入频率的比值。

<a id="r_a4b54b6abcdc5ddb4c6321affcb0110dc"></a>

```c
uint8_t ref_division_factor
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ref_division_factor](#a4b54b6abcdc5ddb4c6321affcb0110dc)。

确定 PLL 输入参考频率的分频因子，范围为 `1 ≤ REFDIV ≤ 63`。

<a id="r_ae1009bd26ecd41f2f751e14366eb5701"></a>

```c
bool on_demand_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[on_demand_en](#ae1009bd26ecd41f2f751e14366eb5701)。

外设请求将振荡器用作时钟源时，配置振荡器开启。

<a id="r_a40cc0b64d8a2feaa59a231f7d8d05bb2"></a>

```c
enum clock_mchp_dpll_src_clock src
```

相关声明：[clock_mchp_dpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gad4a3719300474b36067b86dad7611d33)、[src](#a40cc0b64d8a2feaa59a231f7d8d05bb2)。

参考源时钟选择（Reference Source Clock Selection）。

## 10.2\_详细说明（Detailed Documentation）

<a id="a945f0d0e331b4512cfcea6f298b03fd2"></a>

### `feedback_divider_factor`

```c
uint16_t clock_mchp_subsys_dpll_config::feedback_divider_factor
```

PLL 压控振荡器（Voltage-Controlled Oscillator，VCO）输出频率与参考输入频率的比值。

<a id="ae1009bd26ecd41f2f751e14366eb5701"></a>

### `on_demand_en`

```c
bool clock_mchp_subsys_dpll_config::on_demand_en
```

外设请求将振荡器用作时钟源时，配置振荡器开启。

<a id="a4b54b6abcdc5ddb4c6321affcb0110dc"></a>

### `ref_division_factor`

```c
uint8_t clock_mchp_subsys_dpll_config::ref_division_factor
```

确定 PLL 输入参考频率的分频因子，范围为 `1 ≤ REFDIV ≤ 63`。

<a id="a40cc0b64d8a2feaa59a231f7d8d05bb2"></a>

### `src`

```c
enum clock_mchp_dpll_src_clock clock_mchp_subsys_dpll_config::src
```

参考源时钟选择（Reference Source Clock Selection）。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [clock_mchp_dpll_src_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gad4a3719300474b36067b86dad7611d33)
- [mchp_clock_pic32cz_ca.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_clock_mchp_subsys_dfll_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_clock_mchp_subsys_dpll_out_config_结构体.md)
