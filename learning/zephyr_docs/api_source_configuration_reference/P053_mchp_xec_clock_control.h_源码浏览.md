---
id: learning.zephyr-docs.api-source-configuration-reference.page-53
title: mchp_xec_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_mchp\_xec\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__clock__control_8h.html)。

## 53.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00025"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
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
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="aclock__control_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="amchp__xec__pcr_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="aunionclock__mchp__xec__subsys_html"></a>
<a id="aunionclock__mchp__xec__subsys_html_a0aea2694dc278f2c71f33599f73bff9e"></a>
<a id="aunionclock__mchp__xec__subsys_html_a653526788db4739ec3ee878018d1c91b"></a>
<a id="aunionclock__mchp__xec__subsys_html_ab70cb665df85146d2cac2b34fb802419"></a>
<a id="aunionclock__mchp__xec__subsys_html_af4d56bf6d2f6a7344a9ef1af7ac659b5"></a>

```c
/*
 * Copyright (c) 2021 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_XEC_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_XEC_CLOCK_CONTROL_H_

#include <zephyr/device.h>
#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/mchp_xec_pcr.h>


union clock_mchp_xec_subsys {
        uint32_t val;

        struct {
                uint32_t pcr_data: 24;
                uint32_t bus: 8;
        } bits;
};


/* @brief set or clear Microchip XEC peripheral PCR sleep enable
 *
 * @param slp_idx is the peripheral's sleep enable zero based index (0 through 4)
 * @param slp_pos is the bit position in the 32-bit sleep enable register
 * @param slp_en is 0 to clear(disable) clock gating and non-zero to enable clock gating
 * @return 0 success or -EINVAL on error
 */
int z_mchp_xec_pcr_periph_sleep(uint8_t slp_idx, uint8_t slp_pos, uint8_t slp_en);

/* @brief Reset a single peripheral similar to chip reset
 *
 * @param rst_idx is the peripheral's reset enable register index (0 through 4).
 * @param rst_pos is the bit position in the 32-bit sleep enable register
 * @return 0 success or -EINVAL on error
 * @note This routine lock and unlocks IRQs to safely touch multiple PCR registers. The reset
 * index and bit position are the same as the peripheral's sleep index and bit position.
 */
int z_mchp_xec_pcr_periph_reset(uint8_t rst_idx, uint8_t rst_pos);



#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_XEC_CLOCK_CONTROL_H_ */
```

## 53.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

功能（Brief）：设置或清除 Microchip XEC 外设 PCR 睡眠使能。

参数（Parameters）：

- `slp_idx`：外设的睡眠使能索引，从零开始，范围为 0–4。
- `slp_pos`：32 位睡眠使能寄存器中的位位置。
- `slp_en`：0 表示清除，即禁用时钟门控（Clock gating）；非零表示启用时钟门控。

返回值（Return）：成功返回 0，错误返回 `-EINVAL`。

### 注释 3：原第 51 行

功能（Brief）：复位单个外设，效果类似芯片复位。

参数（Parameters）：

- `rst_idx`：外设复位使能寄存器索引，范围为 0–4。
- `rst_pos`：32 位睡眠使能寄存器中的位位置。

返回值（Return）：成功返回 0，错误返回 `-EINVAL`。

注意（Note）：此例程通过锁定和解锁中断（IRQ）来安全访问多个 PCR 寄存器。复位索引和位位置与该外设的睡眠索引和位位置相同。

### 注释 4：原第 65 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MCHP_XEC_CLOCK_CONTROL_H_`。

## 53.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__clock__control_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [zephyr/dt-bindings/clock/mchp_xec_pcr.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__pcr_8h.html)
- [clock_mchp_xec_subsys](../device_power_control_model_reference/P105_clock_mchp_xec_subsys_联合体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [val](../device_power_control_model_reference/P105_clock_mchp_xec_subsys_联合体.md#a653526788db4739ec3ee878018d1c91b)
- [pcr_data](../device_power_control_model_reference/P105_clock_mchp_xec_subsys_联合体.md#af4d56bf6d2f6a7344a9ef1af7ac659b5)
- [bus](../device_power_control_model_reference/P105_clock_mchp_xec_subsys_联合体.md#ab70cb665df85146d2cac2b34fb802419)
- [bits](../device_power_control_model_reference/P105_clock_mchp_xec_subsys_联合体.md#a0aea2694dc278f2c71f33599f73bff9e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [mchp_xec_pcr.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__xec__pcr_8h.html)
- [clock_mchp_xec_subsys::bits](../device_power_control_model_reference/P105_clock_mchp_xec_subsys_联合体.md#a0aea2694dc278f2c71f33599f73bff9e)
- [clock_mchp_xec_subsys::val](../device_power_control_model_reference/P105_clock_mchp_xec_subsys_联合体.md#a653526788db4739ec3ee878018d1c91b)
- [clock_mchp_xec_subsys::bus](../device_power_control_model_reference/P105_clock_mchp_xec_subsys_联合体.md#ab70cb665df85146d2cac2b34fb802419)
- [clock_mchp_xec_subsys::pcr_data](../device_power_control_model_reference/P105_clock_mchp_xec_subsys_联合体.md#af4d56bf6d2f6a7344a9ef1af7ac659b5)

---

[上一章](P052_mchp_pic32cm_pl_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P054_mctp_i2c_gpio_common.h_源码浏览.md)
