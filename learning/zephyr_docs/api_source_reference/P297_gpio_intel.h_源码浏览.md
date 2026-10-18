---
id: learning.zephyr-docs.api-source-reference.page-297
title: gpio_intel.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__intel_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第297章\_gpio\_intel.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intel_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intel_8h.html)。

## 297.1\_原始可见代码（Source Code）

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
<a id="foldopen00014"></a>
<a id="l00014"></a>
<a id="l00015"></a>
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
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructgpio__acpi__res_html"></a>
<a id="astructgpio__acpi__res_html_a53c789cbddde23ec54c39af61ee433fa"></a>
<a id="astructgpio__acpi__res_html_a82ef9374bee9aeda5b825cf5179057e8"></a>
<a id="astructgpio__acpi__res_html_a85c88312042b134a2f80f63853c086fa"></a>
<a id="astructgpio__acpi__res_html_aa912c56ae09d4ef0fc0467b03091b8ef"></a>
<a id="astructgpio__acpi__res_html_ac0f83a85d2ff41fbc9f1b598d1ca4036"></a>
<a id="astructgpio__acpi__res_html_ad4738c083000ac8f4aa6770082c2ddbb"></a>
<a id="astructgpio__acpi__res_html_af89b2304ea9cfabeddc487d84c2297a9"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_INTEL_H_
#define ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_INTEL_H_

#ifdef __cplusplus
extern "C" {
#endif

struct gpio_acpi_res {
        uint8_t num_pins;
        uint32_t pad_base;
        uint32_t host_owner_reg;
        uint32_t pad_owner_reg;
        uint32_t intr_stat_reg;
        uint16_t base_num;
        uintptr_t reg_base;
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_INTEL_H_ */
```

## 297.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_INTEL_H_`。

## 297.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intel_8h.html)
- [gpio_acpi_res](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [num_pins](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#af89b2304ea9cfabeddc487d84c2297a9)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pad_base](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#a85c88312042b134a2f80f63853c086fa)
- [host_owner_reg](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#ac0f83a85d2ff41fbc9f1b598d1ca4036)
- [pad_owner_reg](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#a53c789cbddde23ec54c39af61ee433fa)
- [intr_stat_reg](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#aa912c56ae09d4ef0fc0467b03091b8ef)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [base_num](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#a82ef9374bee9aeda5b825cf5179057e8)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [reg_base](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#ad4738c083000ac8f4aa6770082c2ddbb)
- [gpio_acpi_res::pad_owner_reg](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#a53c789cbddde23ec54c39af61ee433fa)
- [gpio_acpi_res::base_num](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#a82ef9374bee9aeda5b825cf5179057e8)
- [gpio_acpi_res::pad_base](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#a85c88312042b134a2f80f63853c086fa)
- [gpio_acpi_res::intr_stat_reg](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#aa912c56ae09d4ef0fc0467b03091b8ef)
- [gpio_acpi_res::host_owner_reg](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#ac0f83a85d2ff41fbc9f1b598d1ca4036)
- [gpio_acpi_res::reg_base](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#ad4738c083000ac8f4aa6770082c2ddbb)
- [gpio_acpi_res::num_pins](../device_power_control_model_reference/P012_gpio_acpi_res_结构体.md#af89b2304ea9cfabeddc487d84c2297a9)

---

[上一章](P296_gpio_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P298_gpio_mcux_lpc.h_源码浏览.md)
