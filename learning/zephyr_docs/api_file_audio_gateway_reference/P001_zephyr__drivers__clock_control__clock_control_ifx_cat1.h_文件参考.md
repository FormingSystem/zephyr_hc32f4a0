---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-1
title: zephyr__drivers__clock_control__clock_control_ifx_cat1.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx__cat1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_clock\_control\_\_clock\_control\_ifx\_cat1.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx__cat1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon CAT1（PSoC 6系列）设备的时钟控制定义（Clock Control Definitions）。

<a id="details"></a>

```c
#include <cy_sysclk.h>
#include <cy_systick.h>
```

查看此文件的源码。

Infineon CAT1（PSoC 6系列）设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_ifx_5Fcat1_5Fclock"></a>

```c
struct ifx_cat1_clock
```

相关声明：[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)。

CAT1时钟描述符（Clock Descriptor）。

<a id="r_ifx_5Fcat1_5Fresource_5Finst"></a>

```c
struct ifx_cat1_resource_inst
```

相关声明：[ifx_cat1_resource_inst](../device_power_control_model_reference/P018_ifx_cat1_resource_inst_结构体.md)。

CAT1资源实例描述符（Resource Instance Descriptor）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 高频时钟索引（High Frequency Clock Indices，HF）

<a id="r_ga7585bc918f0435fcea3de69f5d2368c2"></a>

```c
#define CLK_HF0 (0U)
```

相关声明：[CLK_HF0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga7585bc918f0435fcea3de69f5d2368c2)。

高频时钟（HF Clock）0。

<a id="r_gab9ed6e703b1b98d5a713a8ec4cfbab79"></a>

```c
#define CLK_HF1 (1U)
```

相关声明：[CLK_HF1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab9ed6e703b1b98d5a713a8ec4cfbab79)。

高频时钟（HF Clock）1。

<a id="r_gab111d1af9166ca01d139b3e0512a811b"></a>

```c
#define CLK_HF2 (2U)
```

相关声明：[CLK_HF2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab111d1af9166ca01d139b3e0512a811b)。

高频时钟（HF Clock）2。

<a id="r_ga5deb0165e6f3e18acd4d3b841f96c50b"></a>

```c
#define CLK_HF3 (3U)
```

相关声明：[CLK_HF3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga5deb0165e6f3e18acd4d3b841f96c50b)。

高频时钟（HF Clock）3。

<a id="r_ga16cf7a3976d594e17bdcb595d024a6f7"></a>

```c
#define CLK_HF4 (4U)
```

相关声明：[CLK_HF4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga16cf7a3976d594e17bdcb595d024a6f7)。

高频时钟（HF Clock）4。

<a id="r_ga5516442b0c25b62024b765545fa2b18f"></a>

```c
#define CLK_HF5 (5U)
```

相关声明：[CLK_HF5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga5516442b0c25b62024b765545fa2b18f)。

高频时钟（HF Clock）5。

<a id="r_gad55fafafdec37c322f2faf036e955dcf"></a>

```c
#define CLK_HF6 (6U)
```

相关声明：[CLK_HF6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gad55fafafdec37c322f2faf036e955dcf)。

高频时钟（HF Clock）6。

<a id="r_gadf9e87e3582b2042993c3237afe20383"></a>

```c
#define CLK_HF7 (7U)
```

相关声明：[CLK_HF7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gadf9e87e3582b2042993c3237afe20383)。

高频时钟（HF Clock）7。

<a id="r_gae2c2ae8c1143a5d28a73508dcc423444"></a>

```c
#define CLK_HF8 (8U)
```

相关声明：[CLK_HF8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gae2c2ae8c1143a5d28a73508dcc423444)。

高频时钟（HF Clock）8。

<a id="r_ga4b7e7866dd86214ce5910c2d01dcf49c"></a>

```c
#define CLK_HF9 (9U)
```

相关声明：[CLK_HF9](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga4b7e7866dd86214ce5910c2d01dcf49c)。

高频时钟（HF Clock）9。

<a id="r_ga726332ad1db3729a208a2be1458478ec"></a>

```c
#define CLK_HF10 (10U)
```

相关声明：[CLK_HF10](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga726332ad1db3729a208a2be1458478ec)。

高频时钟（HF Clock）10。

<a id="r_gaf1b81772f3de1dfcd08b5eaf96b60b33"></a>

```c
#define CLK_HF11 (11U)
```

相关声明：[CLK_HF11](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gaf1b81772f3de1dfcd08b5eaf96b60b33)。

高频时钟（HF Clock）11。

<a id="r_gad3b7e5ef1f3c470006b5b9ffec0050f7"></a>

```c
#define CLK_HF12 (12U)
```

相关声明：[CLK_HF12](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gad3b7e5ef1f3c470006b5b9ffec0050f7)。

高频时钟（HF Clock）12。

<a id="r_ga4c10fa4f6073001fde1fd49fe3769181"></a>

```c
#define CLK_HF13 (13U)
```

相关声明：[CLK_HF13](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga4c10fa4f6073001fde1fd49fe3769181)。

高频时钟（HF Clock）13。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_gab62704a8cdfda5914cfb7dfe81afa8c0"></a>

```c
enum ifx_cat1_clock_block
```

相关声明：[ifx_cat1_clock_block](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab62704a8cdfda5914cfb7dfe81afa8c0)。

CAT1 时钟块选择器（Clock Block Selector），选择时钟源或时钟域。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga04bb0312c12347d0ceac9fc033993221"></a>

```c
int ifx_cat1_clock_control_get_frequency (uint32_t dt_ord, uint32_t *frequency)
```

相关声明：[ifx_cat1_clock_control_get_frequency](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga04bb0312c12347d0ceac9fc033993221)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取由设备树序号（Devicetree Ordinal）标识的时钟的频率。

<a id="r_ga0421e7b519bd9b829baa8a2e7b234931"></a>

```c
static uint32_t ifx_cat1_utils_peri_pclk_get_frequency (en_clk_dst_t clk_dest, const struct ifx_cat1_clock *peri_clock)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[ifx_cat1_utils_peri_pclk_get_frequency](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga0421e7b519bd9b829baa8a2e7b234931)、[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)。

获取外设时钟分频器（Peripheral Clock Divider）的频率。

<a id="r_gadda478f75d4546b4de8d978e56dba1fa"></a>

```c
static cy_rslt_t ifx_cat1_utils_peri_pclk_enable_divider (en_clk_dst_t clk_dest, const struct ifx_cat1_clock *peri_clock)
```

相关声明：[ifx_cat1_utils_peri_pclk_enable_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gadda478f75d4546b4de8d978e56dba1fa)、[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)。

启用与外设时钟关联的分频器（Divider）。

<a id="r_ga6bfb0915441740364a239ca3a68d6d8b"></a>

```c
static cy_rslt_t ifx_cat1_utils_peri_pclk_disable_divider (en_clk_dst_t clk_dest, const struct ifx_cat1_clock *peri_clock)
```

相关声明：[ifx_cat1_utils_peri_pclk_disable_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga6bfb0915441740364a239ca3a68d6d8b)、[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)。

禁用与外设时钟关联的分频器（Divider）。

<a id="r_gacacef8eba03b64537cbd0f09c3425089"></a>

```c
static bool ifx_cat1_utils_peri_is_fract_div (const struct ifx_cat1_clock *peri_clock)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ifx_cat1_utils_peri_is_fract_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gacacef8eba03b64537cbd0f09c3425089)、[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)。

检查外设时钟是否使用小数分频器（Fractional Divider，x.5 位）。

<a id="r_ga933b6bafae3eef87ac8e0a4ae7a849d4"></a>

```c
static cy_rslt_t ifx_cat1_utils_peri_pclk_set_divider (en_clk_dst_t clk_dest, const struct ifx_cat1_clock *peri_clock, uint32_t div)
```

相关声明：[ifx_cat1_utils_peri_pclk_set_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga933b6bafae3eef87ac8e0a4ae7a849d4)、[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置外设时钟的整数分频器（Integer Divider）。

<a id="r_ga1dba84b96bf16b98d672369a4bbe58c8"></a>

```c
static cy_rslt_t ifx_cat1_utils_peri_pclk_set_frac_divider (en_clk_dst_t clk_dest, const struct ifx_cat1_clock *peri_clock, uint32_t div_int, uint32_t div_frac)
```

相关声明：[ifx_cat1_utils_peri_pclk_set_frac_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga1dba84b96bf16b98d672369a4bbe58c8)、[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置外设时钟的小数分频器（Fractional Divider）。

<a id="r_gafe5b77c891a50a08f364fa4d85af29ac"></a>

```c
static uint32_t ifx_cat1_utils_peri_pclk_get_divider (en_clk_dst_t clk_dest, const struct ifx_cat1_clock *peri_clock)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[ifx_cat1_utils_peri_pclk_get_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gafe5b77c891a50a08f364fa4d85af29ac)、[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)。

获取外设时钟的整数分频值（Integer Divider Value）。

<a id="r_ga1b13def736a7046ee628830ab686ef3a"></a>

```c
static void ifx_cat1_utils_peri_pclk_get_frac_divider (en_clk_dst_t clk_dest, const struct ifx_cat1_clock *peri_clock, uint32_t *div_int, uint32_t *div_frac)
```

相关声明：[ifx_cat1_utils_peri_pclk_get_frac_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga1b13def736a7046ee628830ab686ef3a)、[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取外设时钟的小数分频值（Fractional Divider Value）。

<a id="r_ga9ffa2a2c7427ea6049d7790f725ec185"></a>

```c
static cy_rslt_t ifx_cat1_utils_peri_pclk_assign_divider (en_clk_dst_t clk_dest, const struct ifx_cat1_clock *peri_clock)
```

相关声明：[ifx_cat1_utils_peri_pclk_assign_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga9ffa2a2c7427ea6049d7790f725ec185)、[ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)。

将分频器（Divider）分配给外设时钟目标（Destination）。

<a id="r_gaf8c74267c99cdebf0ae977555336f65c"></a>

```c
static uint8_t ifx_cat1_utils_peri_pclk_get_hfclk (uint8_t peri_group)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ifx_cat1_utils_peri_pclk_get_hfclk](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gaf8c74267c99cdebf0ae977555336f65c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将外设组索引（Peripheral Group Index）映射为向其供钟的高频时钟（HF Clock）。


## 1.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_network_reference/P002_clock_control_ifx_cat1.h_源码浏览.md)
- [ifx_cat1_clock](../device_power_control_model_reference/P017_ifx_cat1_clock_结构体.md)
- [ifx_cat1_resource_inst](../device_power_control_model_reference/P018_ifx_cat1_resource_inst_结构体.md)
- [CLK_HF0](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga7585bc918f0435fcea3de69f5d2368c2)
- [CLK_HF1](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab9ed6e703b1b98d5a713a8ec4cfbab79)
- [CLK_HF2](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab111d1af9166ca01d139b3e0512a811b)
- [CLK_HF3](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga5deb0165e6f3e18acd4d3b841f96c50b)
- [CLK_HF4](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga16cf7a3976d594e17bdcb595d024a6f7)
- [CLK_HF5](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga5516442b0c25b62024b765545fa2b18f)
- [CLK_HF6](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gad55fafafdec37c322f2faf036e955dcf)
- [CLK_HF7](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gadf9e87e3582b2042993c3237afe20383)
- [CLK_HF8](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gae2c2ae8c1143a5d28a73508dcc423444)
- [CLK_HF9](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga4b7e7866dd86214ce5910c2d01dcf49c)
- [CLK_HF10](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga726332ad1db3729a208a2be1458478ec)
- [CLK_HF11](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gaf1b81772f3de1dfcd08b5eaf96b60b33)
- [CLK_HF12](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gad3b7e5ef1f3c470006b5b9ffec0050f7)
- [CLK_HF13](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga4c10fa4f6073001fde1fd49fe3769181)
- [ifx_cat1_clock_block](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gab62704a8cdfda5914cfb7dfe81afa8c0)
- [ifx_cat1_clock_control_get_frequency](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga04bb0312c12347d0ceac9fc033993221)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ifx_cat1_utils_peri_pclk_get_frequency](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga0421e7b519bd9b829baa8a2e7b234931)
- [ifx_cat1_utils_peri_pclk_enable_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gadda478f75d4546b4de8d978e56dba1fa)
- [ifx_cat1_utils_peri_pclk_disable_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga6bfb0915441740364a239ca3a68d6d8b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ifx_cat1_utils_peri_is_fract_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gacacef8eba03b64537cbd0f09c3425089)
- [ifx_cat1_utils_peri_pclk_set_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga933b6bafae3eef87ac8e0a4ae7a849d4)
- [ifx_cat1_utils_peri_pclk_set_frac_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga1dba84b96bf16b98d672369a4bbe58c8)
- [ifx_cat1_utils_peri_pclk_get_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gafe5b77c891a50a08f364fa4d85af29ac)
- [ifx_cat1_utils_peri_pclk_get_frac_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga1b13def736a7046ee628830ab686ef3a)
- [ifx_cat1_utils_peri_pclk_assign_divider](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#ga9ffa2a2c7427ea6049d7790f725ec185)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ifx_cat1_utils_peri_pclk_get_hfclk](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ifx__cat1.html#gaf8c74267c99cdebf0ae977555336f65c)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__audio__codec.h_文件参考.md)
