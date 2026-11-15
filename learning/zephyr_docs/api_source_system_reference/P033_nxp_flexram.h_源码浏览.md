---
id: learning.zephyr-docs.api-source-system-reference.page-33
title: nxp_flexram.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexram_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_nxp\_flexram.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexram_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexram_8h.html)。

## 33.1\_原始可见代码（Source Code）

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
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="adevicetree_8h_html"></a>
<a id="agroup__devicetree-generic-foreach_html_ga72d0b6859b4fc61cde518aee118d9ed8"></a>
<a id="agroup__devicetree-reg-prop_html_gac6d8279c32351ced4c0ac7f32270974e"></a>
<a id="anxp__flexram_8h_html_a374d43fc963ce2a7665f8c8bde58c7bf"></a>
<a id="anxp__flexram_8h_html_a89a618d3a7cce4eedd2520ddfa5cfe43"></a>
<a id="anxp__flexram_8h_html_ac4ed80d0460f7765e9b9f2b58a0ec7cb"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright 2023-2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_FLEXRAM_NXP_FLEXRAM_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_FLEXRAM_NXP_FLEXRAM_H_

#include <zephyr/devicetree.h>
#include <soc.h>


#define FLEXRAM_DT_NODE    DT_INST(0, nxp_flexram)
#define IOMUXC_GPR_DT_NODE DT_NODELABEL(iomuxcgpr)

#if defined(CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API) || \
        defined(CONFIG_NXP_FLEXRAM_ERROR_INTERRUPT)
#define FLEXRAM_INTERRUPTS_USED
#endif

#if DT_PROP_HAS_IDX(FLEXRAM_DT_NODE, flexram_bank_spec, 0)
#define FLEXRAM_RUNTIME_BANKS_USED 1
#endif

#ifdef FLEXRAM_INTERRUPTS_USED
enum flexram_interrupt_cause {
#ifdef CONFIG_NXP_FLEXRAM_ERROR_INTERRUPT
        flexram_ocram_access_error,
        flexram_itcm_access_error,
        flexram_dtcm_access_error,
#endif
#ifdef CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API
        flexram_ocram_magic_addr,
        flexram_itcm_magic_addr,
        flexram_dtcm_magic_addr,
#endif /* CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API */
};

typedef void (*flexram_callback_t)(enum flexram_interrupt_cause, void *user_data);

void flexram_register_callback(flexram_callback_t callback, void *user_data);
#endif /* FLEXRAM_INTERRUPTS_USED */

#ifdef FLEXRAM_RUNTIME_BANKS_USED

/*
 * call from platform_init to set up flexram if using runtime map
 * must be inlined because cannot use stack
 */
#define GPR_FLEXRAM_REG_FILL(node_id, prop, idx) \
        (((uint32_t)DT_PROP_BY_IDX(node_id, prop, idx)) << (2 * idx))
static inline void flexram_dt_partition(void)
{
        /* iomuxc_gpr must be const (in ROM region) because used in reconfiguring ram */
        static IOMUXC_GPR_Type *const iomuxc_gpr =
                (IOMUXC_GPR_Type *)DT_REG_ADDR(IOMUXC_GPR_DT_NODE);
        /* do not create stack variables or use any data from ram in this function */
#if defined(CONFIG_SOC_SERIES_IMXRT11XX)
        iomuxc_gpr->GPR17 = (DT_FOREACH_PROP_ELEM_SEP(FLEXRAM_DT_NODE, flexram_bank_spec,
                                                GPR_FLEXRAM_REG_FILL, (+))) & 0xFFFF;
        iomuxc_gpr->GPR18 = (((DT_FOREACH_PROP_ELEM_SEP(FLEXRAM_DT_NODE, flexram_bank_spec,
                                                GPR_FLEXRAM_REG_FILL, (+)))) >> 16) & 0xFFFF;
#elif defined(CONFIG_SOC_SERIES_IMXRT10XX)
        iomuxc_gpr->GPR17 = DT_FOREACH_PROP_ELEM_SEP(FLEXRAM_DT_NODE, flexram_bank_spec,
                                                GPR_FLEXRAM_REG_FILL, (+));
#endif
        iomuxc_gpr->GPR16 |= IOMUXC_GPR_GPR16_FLEXRAM_BANK_CFG_SEL_MASK;
}
#endif /* FLEXRAM_RUNTIME_BANKS_USED */


int flexram_set_ocram_magic_addr(uint32_t ocram_addr);

int flexram_set_itcm_magic_addr(uint32_t itcm_addr);

int flexram_set_dtcm_magic_addr(uint32_t dtcm_addr);

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_FLEXRAM_NXP_FLEXRAM_H_ */
```

## 33.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023-2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

条件编译配置（Configuration）标记：`CONFIG_NXP_FLEXRAM_MAGIC_ADDR_API`。

### 注释 3：原第 44 行

FLEXRAM 中断使用条件标识（Interrupt Usage Identifier）：`FLEXRAM_INTERRUPTS_USED`。

### 注释 4：原第 48 行

若采用运行时映射（Runtime Map），则从 `platform_init` 调用以配置 FlexRAM。由于不能使用栈（Stack），此函数必须内联（Inlined）。

### 注释 5：原第 56 行

`iomuxc_gpr` 必须为常量（Const）并位于 ROM 区域，因为它用于重新配置 RAM。

### 注释 6：原第 59 行

本函数不得创建栈变量（Stack Variables），也不得使用 RAM 中的任何数据。

### 注释 7：原第 71 行

FLEXRAM 运行时内存组使用条件标识（Runtime Bank Usage Identifier）：`FLEXRAM_RUNTIME_BANKS_USED`。

### 注释 8：原第 117 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_FLEXRAM_NXP_FLEXRAM_H_`。

## 33.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexram_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)
- [DT_FOREACH_PROP_ELEM_SEP](../dt_foreach_reference/P001_设备树遍历宏.md#ga72d0b6859b4fc61cde518aee118d9ed8)
- [flexram_set_ocram_magic_addr](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexram_8h.html#ac4ed80d0460f7765e9b9f2b58a0ec7cb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [flexram_set_itcm_magic_addr](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexram_8h.html#a374d43fc963ce2a7665f8c8bde58c7bf)
- [flexram_set_dtcm_magic_addr](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexram_8h.html#a89a618d3a7cce4eedd2520ddfa5cfe43)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)

---

[上一章](P032_numicro_m48x_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P034_posix_limits.h_源码浏览.md)
