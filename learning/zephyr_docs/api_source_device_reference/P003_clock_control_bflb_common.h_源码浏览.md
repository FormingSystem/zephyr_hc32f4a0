---
id: learning.zephyr-docs.api-source-device-reference.page-3
title: clock_control_bflb_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__bflb__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_clock\_control\_bflb\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__bflb__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__bflb__common_8h.html)。

## 3.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00046"></a>
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
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="agroup__clock__control__bflb_html_ga3f2549b3d7feb0693b140760fc5e7975"></a>
<a id="agroup__clock__control__bflb_html_ga56da89547422c68d755cae71ebc8213e"></a>
<a id="agroup__clock__control__bflb_html_ga62631545e2b11958a758dd19b0b585a9"></a>
<a id="agroup__clock__control__bflb_html_ga8d56227817defb1b5d442b499ad5a0aa"></a>
<a id="agroup__clock__control__bflb_html_gad8f2fcc97e98aad258410a97880abcfb"></a>
<a id="agroup__sys__io__mmio__apis_html_gac742e54d030b90f98400cb1248b14ca8"></a>
<a id="agroup__sys__io__mmio__apis_html_gafebb790883d604c1ddbdbbd8314876d7"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2025 MASSDRIVER EI (massdriver.space)
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_BFLB_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_BFLB_COMMON_H_


#define BFLB_MAIN_CLOCK_RC32M     0
#define BFLB_MAIN_CLOCK_XTAL      1
#define BFLB_MAIN_CLOCK_PLL_RC32M 2
#define BFLB_MAIN_CLOCK_PLL_XTAL  3

static inline void clock_bflb_settle(void)
{
        __asm__ volatile (".rept 20 ; nop ; .endr");
}

static inline void clock_bflb_set_root_clock(uint32_t clock)
{
        uint32_t tmp;

        /* invalid value, fallback to internal 32M */
        if (clock > BFLB_MAIN_CLOCK_PLL_XTAL) {
                clock = BFLB_MAIN_CLOCK_RC32M;
        }
        tmp = sys_read32(HBN_BASE + HBN_GLB_OFFSET);
        tmp = (tmp & HBN_ROOT_CLK_SEL_UMSK) | (clock << HBN_ROOT_CLK_SEL_POS);
        sys_write32(tmp, HBN_BASE + HBN_GLB_OFFSET);

        clock_bflb_settle();
}

static inline uint32_t clock_bflb_get_root_clock(void)
{
        uint32_t tmp;

        tmp = sys_read32(HBN_BASE + HBN_GLB_OFFSET);
        return ((tmp & HBN_ROOT_CLK_SEL_MSK) >> HBN_ROOT_CLK_SEL_POS);
}



/* Avoid overflow when calculating multipliers by reducing precision to 100 KHz
 * Every _value and _base should be a multiple of this to stay exact
 */
#define BFLB_MUL_CLK_UNIT       100000U

/* (_value * _top) / _base without 64-bit division. _top is evaluated twice. */
#define BFLB_MUL_CLK(_value, _top, _base) \
        ((((uint32_t)(_top) / ((uint32_t)(_base) / BFLB_MUL_CLK_UNIT)) * \
          ((uint32_t)(_value) / BFLB_MUL_CLK_UNIT)) + \
         ((((uint32_t)(_top) % ((uint32_t)(_base) / BFLB_MUL_CLK_UNIT)) * \
           ((uint32_t)(_value) / BFLB_MUL_CLK_UNIT)) / \
          ((uint32_t)(_base) / BFLB_MUL_CLK_UNIT)))

/* Runnable from XIP (__udivdi3 call from libgcc) */
#define BFLB_MUL_CLK_XIP(_value, _top, _base) \
        (((uint64_t)(_value) * (uint64_t)(_top)) / (uint64_t)(_base))



#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_BFLB_COMMON_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 MASSDRIVER EI (massdriver.space)。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 50 行

无效值（Invalid Value），回退到内部 32M 时钟（Internal 32M）。

### 注释 3：原第 77 行

将精度降低到 100 kHz，以避免计算乘数（Multipliers）时溢出（Overflow）。
每个 `_value` 和 `_base` 都应为该精度单位的整数倍，以保持结果精确。

### 注释 4：原第 82 行

计算 `(_value * _top) / _base`，而不使用 64 位除法（64-Bit Division）。`_top` 会求值两次。

### 注释 5：原第 90 行

可在就地执行（XIP）环境中运行，涉及对 libgcc 中 `__udivdi3` 的调用。

### 注释 6：原第 98 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_BFLB_COMMON_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__bflb__common_8h.html)
- [clock_bflb_settle](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bflb.html#ga56da89547422c68d755cae71ebc8213e)
- [clock_bflb_set_root_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bflb.html#gad8f2fcc97e98aad258410a97880abcfb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [BFLB_MAIN_CLOCK_PLL_XTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bflb.html#ga8d56227817defb1b5d442b499ad5a0aa)
- [BFLB_MAIN_CLOCK_RC32M](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bflb.html#ga62631545e2b11958a758dd19b0b585a9)
- [sys_read32](../device_reference/P019_内存映射寄存器IO接口.md#gac742e54d030b90f98400cb1248b14ca8)
- [sys_write32](../device_reference/P019_内存映射寄存器IO接口.md#gafebb790883d604c1ddbdbbd8314876d7)
- [clock_bflb_get_root_clock](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__bflb.html#ga3f2549b3d7feb0693b140760fc5e7975)

---

[上一章](P002_map.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_coap_service.h_源码浏览.md)
