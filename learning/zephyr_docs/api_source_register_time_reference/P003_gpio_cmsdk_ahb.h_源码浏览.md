---
id: learning.zephyr-docs.api-source-register-time-reference.page-3
title: gpio_cmsdk_ahb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__cmsdk__ahb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_gpio\_cmsdk\_ahb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__cmsdk__ahb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P134_zephyr__drivers__gpio__gpio_cmsdk_ahb.h_文件参考.md)。

## 3.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="foldopen00016"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agpio__cmsdk__ahb_8h_html_aff8513705856d9a28013299a93649691"></a>
<a id="agroup__gpio__interface_html_ga5f5cb5e7dae6d58e072bb450af029d2e"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__cmsdk__ahb_html"></a>
<a id="astructgpio__cmsdk__ahb_html_a1cb9a3456c4e3c7a65c5132052f4605a"></a>
<a id="astructgpio__cmsdk__ahb_html_a20babd83013581d8273570c5b63658b4"></a>
<a id="astructgpio__cmsdk__ahb_html_a325a85d7d5fa3830ee9a7e922bed08ae"></a>
<a id="astructgpio__cmsdk__ahb_html_a5bc3851b26cb0340208f4b93ef475042"></a>
<a id="astructgpio__cmsdk__ahb_html_a5c79dd58c92ee471c86cf420a02a3afb"></a>
<a id="astructgpio__cmsdk__ahb_html_a5f70dc42911502ff96254f44ff385caa"></a>
<a id="astructgpio__cmsdk__ahb_html_a83a77418db66bd89bae093533a168617"></a>
<a id="astructgpio__cmsdk__ahb_html_a995563a125b425a4633f4d25ccaff0cd"></a>
<a id="astructgpio__cmsdk__ahb_html_aa3a3638d45f9dddd4f122b8081ac46cf"></a>
<a id="astructgpio__cmsdk__ahb_html_abf5caf8e369d4629aabe935f63bd8f7e"></a>
<a id="astructgpio__cmsdk__ahb_html_ac5de9ecb2427bdf0dfc78099253ce2de"></a>
<a id="astructgpio__cmsdk__ahb_html_accd586d346c6588ae93fc409159fa368"></a>
<a id="astructgpio__cmsdk__ahb_html_addc9f323303ed2888a047a54ff2d2092"></a>
<a id="astructgpio__cmsdk__ahb_html_ae8c9c5c849a45f86b84b21266eaca8af"></a>
<a id="astructgpio__cmsdk__ahb_html_aece662b5260db9a8b43fc61ebd7a288c"></a>
<a id="astructgpio__cmsdk__ahb_html_af548def1b32a28d043b4bbfdddc29662"></a>
<a id="astructgpio__cmsdk__ahb_html_af54ff4e5327fa86546166df38f76d3df"></a>
<a id="astructgpio__cmsdk__ahb_html_af76e1a0e03e7a1373a4029f9865a1abb"></a>

```c
/*
 * Copyright (c) 2016 Linaro Limited.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_CMSDK_AHB_H_
#define ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_CMSDK_AHB_H_

#include <zephyr/drivers/gpio.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ARM LTD CMSDK AHB General Purpose Input/Output (GPIO) */
struct gpio_cmsdk_ahb {
        /* Offset: 0x000 (r/w) data register */
        volatile uint32_t data;
        /* Offset: 0x004 (r/w) data output latch register */
        volatile uint32_t dataout;
        volatile uint32_t reserved0[2];
        /* Offset: 0x010 (r/w) output enable set register */
        volatile uint32_t outenableset;
        /* Offset: 0x014 (r/w) output enable clear register */
        volatile uint32_t outenableclr;
        /* Offset: 0x018 (r/w) alternate function set register */
        volatile uint32_t altfuncset;
        /* Offset: 0x01c (r/w) alternate function clear register */
        volatile uint32_t altfuncclr;
        /* Offset: 0x020 (r/w) interrupt enable set register */
        volatile uint32_t intenset;
        /* Offset: 0x024 (r/w) interrupt enable clear register */
        volatile uint32_t intenclr;
        /* Offset: 0x028 (r/w) interrupt type set register */
        volatile uint32_t inttypeset;
        /* Offset: 0x02c (r/w) interrupt type clear register */
        volatile uint32_t inttypeclr;
        /* Offset: 0x030 (r/w) interrupt polarity set register */
        volatile uint32_t intpolset;
        /* Offset: 0x034 (r/w) interrupt polarity clear register */
        volatile uint32_t intpolclr;
        union {
                /* Offset: 0x038 (r/ ) interrupt status register */
                volatile uint32_t intstatus;
                /* Offset: 0x038 ( /w) interrupt clear register */
                volatile uint32_t  intclear;
        };
        volatile uint32_t reserved1[241];
        /* Offset: 0x400 - 0x7fc lower byte masked access register (r/w) */
        volatile uint32_t lb_masked[256];
        /* Offset: 0x800 - 0xbfc upper byte masked access register (r/w) */
        volatile uint32_t ub_masked[256];
};

int cmsdk_ahb_gpio_config(const struct device *dev, uint32_t mask, gpio_flags_t flags);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_CMSDK_AHB_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Linaro Limited.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 15 行

ARM LTD Cortex-M 系统设计套件（CMSDK）的 AHB 通用输入／输出（GPIO）。

### 注释 3：原第 17 行

偏移量 `0x000`，可读写：数据寄存器（data register）。

### 注释 4：原第 19 行

偏移量 `0x004`，可读写：数据输出锁存寄存器（data output latch register）。

### 注释 5：原第 22 行

偏移量 `0x010`，可读写：输出使能置位寄存器（output enable set register）。

### 注释 6：原第 24 行

偏移量 `0x014`，可读写：输出使能清零寄存器（output enable clear register）。

### 注释 7：原第 26 行

偏移量 `0x018`，可读写：复用功能置位寄存器（alternate function set register）。

### 注释 8：原第 28 行

偏移量 `0x01c`，可读写：复用功能清零寄存器（alternate function clear register）。

### 注释 9：原第 30 行

偏移量 `0x020`，可读写：中断使能置位寄存器（interrupt enable set register）。

### 注释 10：原第 32 行

偏移量 `0x024`，可读写：中断使能清零寄存器（interrupt enable clear register）。

### 注释 11：原第 34 行

偏移量 `0x028`，可读写：中断类型置位寄存器（interrupt type set register）。

### 注释 12：原第 36 行

偏移量 `0x02c`，可读写：中断类型清零寄存器（interrupt type clear register）。

### 注释 13：原第 38 行

偏移量 `0x030`，可读写：中断极性置位寄存器（interrupt polarity set register）。

### 注释 14：原第 40 行

偏移量 `0x034`，可读写：中断极性清零寄存器（interrupt polarity clear register）。

### 注释 15：原第 43 行

偏移量 `0x038`，只读：中断状态寄存器（interrupt status register）。

### 注释 16：原第 45 行

偏移量 `0x038`，只写：中断清除寄存器（interrupt clear register）。

### 注释 17：原第 49 行

偏移量 `0x400`–`0x7fc`，可读写：低字节掩码访问寄存器（lower byte masked access register）。

### 注释 18：原第 51 行

偏移量 `0x800`–`0xbfc`，可读写：高字节掩码访问寄存器（upper byte masked access register）。

### 注释 19：原第 61 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_CMSDK_AHB_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P134_zephyr__drivers__gpio__gpio_cmsdk_ahb.h_文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio_cmsdk_ahb](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [data](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#accd586d346c6588ae93fc409159fa368)
- [dataout](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#af548def1b32a28d043b4bbfdddc29662)
- [reserved0](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a995563a125b425a4633f4d25ccaff0cd)
- [outenableset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#ac5de9ecb2427bdf0dfc78099253ce2de)
- [outenableclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a20babd83013581d8273570c5b63658b4)
- [altfuncset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a5f70dc42911502ff96254f44ff385caa)
- [altfuncclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a325a85d7d5fa3830ee9a7e922bed08ae)
- [intenset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a5c79dd58c92ee471c86cf420a02a3afb)
- [intenclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a83a77418db66bd89bae093533a168617)
- [inttypeset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#abf5caf8e369d4629aabe935f63bd8f7e)
- [inttypeclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#af54ff4e5327fa86546166df38f76d3df)
- [intpolset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#af76e1a0e03e7a1373a4029f9865a1abb)
- [intpolclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#addc9f323303ed2888a047a54ff2d2092)
- [intstatus](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a5bc3851b26cb0340208f4b93ef475042)
- [intclear](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#aa3a3638d45f9dddd4f122b8081ac46cf)
- [reserved1](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#ae8c9c5c849a45f86b84b21266eaca8af)
- [lb_masked](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a1cb9a3456c4e3c7a65c5132052f4605a)
- [ub_masked](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#aece662b5260db9a8b43fc61ebd7a288c)
- [cmsdk_ahb_gpio_config](../api_file_reference/P134_zephyr__drivers__gpio__gpio_cmsdk_ahb.h_文件参考.md#aff8513705856d9a28013299a93649691)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_flags_t](../hardware/P266_GPIO公共接口.md#ga5f5cb5e7dae6d58e072bb450af029d2e)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio_cmsdk_ahb::lb_masked](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a1cb9a3456c4e3c7a65c5132052f4605a)
- [gpio_cmsdk_ahb::outenableclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a20babd83013581d8273570c5b63658b4)
- [gpio_cmsdk_ahb::altfuncclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a325a85d7d5fa3830ee9a7e922bed08ae)
- [gpio_cmsdk_ahb::intstatus](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a5bc3851b26cb0340208f4b93ef475042)
- [gpio_cmsdk_ahb::intenset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a5c79dd58c92ee471c86cf420a02a3afb)
- [gpio_cmsdk_ahb::altfuncset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a5f70dc42911502ff96254f44ff385caa)
- [gpio_cmsdk_ahb::intenclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a83a77418db66bd89bae093533a168617)
- [gpio_cmsdk_ahb::reserved0](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#a995563a125b425a4633f4d25ccaff0cd)
- [gpio_cmsdk_ahb::intclear](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#aa3a3638d45f9dddd4f122b8081ac46cf)
- [gpio_cmsdk_ahb::inttypeset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#abf5caf8e369d4629aabe935f63bd8f7e)
- [gpio_cmsdk_ahb::outenableset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#ac5de9ecb2427bdf0dfc78099253ce2de)
- [gpio_cmsdk_ahb::data](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#accd586d346c6588ae93fc409159fa368)
- [gpio_cmsdk_ahb::intpolclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#addc9f323303ed2888a047a54ff2d2092)
- [gpio_cmsdk_ahb::reserved1](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#ae8c9c5c849a45f86b84b21266eaca8af)
- [gpio_cmsdk_ahb::ub_masked](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#aece662b5260db9a8b43fc61ebd7a288c)
- [gpio_cmsdk_ahb::dataout](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#af548def1b32a28d043b4bbfdddc29662)
- [gpio_cmsdk_ahb::inttypeclr](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#af54ff4e5327fa86546166df38f76d3df)
- [gpio_cmsdk_ahb::intpolset](../device_power_control_model_reference/P013_gpio_cmsdk_ahb_结构体.md#af76e1a0e03e7a1373a4029f9865a1abb)

---

[上一章](P002_conn.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_mcc.h_源码浏览.md)
