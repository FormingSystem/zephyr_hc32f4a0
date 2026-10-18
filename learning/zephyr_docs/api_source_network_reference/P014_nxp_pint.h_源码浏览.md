---
id: learning.zephyr-docs.api-source-network-reference.page-14
title: nxp_pint.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_nxp\_pint.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html)。

## 14.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="foldopen00029"></a>
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
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="anxp__pint_8h_html_a086336be48bc780034f74dbd5aff0bd9"></a>
<a id="anxp__pint_8h_html_a45daffb706e6e51fb805d1bfbd1c4144"></a>
<a id="anxp__pint_8h_html_a5ceee20d9c423fe9f80e1d72540b4c73"></a>
<a id="anxp__pint_8h_html_aaa54294fced53ad82eefe02f8c4250e2"></a>
<a id="anxp__pint_8h_html_abdfe420166b4d28fd7be112b561228bc"></a>
<a id="anxp__pint_8h_html_ad7ec8dddcc5a404f38d8d5bb16775a9a"></a>
<a id="anxp__pint_8h_html_aea62e6522d0de4c0ce63ae04b2d36f7c"></a>
<a id="anxp__pint_8h_html_aea62e6522d0de4c0ce63ae04b2d36f7ca115385d1645fa1901b7ffeab07ff6ce7"></a>
<a id="anxp__pint_8h_html_aea62e6522d0de4c0ce63ae04b2d36f7ca20ed11aa9c65c91d30b169ae8a754d40"></a>
<a id="anxp__pint_8h_html_aea62e6522d0de4c0ce63ae04b2d36f7ca8594c4bbe2858dd19a176d851a6175c5"></a>
<a id="anxp__pint_8h_html_aea62e6522d0de4c0ce63ae04b2d36f7caabce56e3c8a6ba8801b0700bfbf52ec2"></a>
<a id="anxp__pint_8h_html_aea62e6522d0de4c0ce63ae04b2d36f7cad94f208bdf7029063172c88673d28b24"></a>
<a id="anxp__pint_8h_html_aea62e6522d0de4c0ce63ae04b2d36f7caf77211604686c8e8f16616b25b9ada9e"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_NXP_PINT_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_NXP_PINT_H_

#include <fsl_pint.h>

enum nxp_pint_trigger {
        /* Do not generate Pin Interrupt */
        NXP_PINT_NONE = kPINT_PinIntEnableNone,
        /* Generate Pin Interrupt on rising edge */
        NXP_PINT_RISING  = kPINT_PinIntEnableRiseEdge,
        /* Generate Pin Interrupt on falling edge */
        NXP_PINT_FALLING  = kPINT_PinIntEnableFallEdge,
        /* Generate Pin Interrupt on both edges */
        NXP_PINT_BOTH = kPINT_PinIntEnableBothEdges,
        /* Generate Pin Interrupt on low level */
        NXP_PINT_LOW  = kPINT_PinIntEnableLowLevel,
        /* Generate Pin Interrupt on high level */
        NXP_PINT_HIGH = kPINT_PinIntEnableHighLevel
};

/* Callback for NXP PINT interrupt */
typedef void (*nxp_pint_cb_t) (uint8_t pin, void *user);

int nxp_pint_pin_enable(uint8_t pin, enum nxp_pint_trigger trigger, bool wake);


void nxp_pint_pin_disable(uint8_t pin);

int nxp_pint_pin_set_callback(uint8_t pin, nxp_pint_cb_t cb, void *data);

void nxp_pint_pin_unset_callback(uint8_t pin);

int nxp_pint_pin_get_slot_index(uint8_t pin);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_NXP_PINT_H_ */
```

## 14.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 30 行

不产生引脚中断（Pin Interrupt）。

### 注释 3：原第 32 行

在上升沿（rising edge）产生引脚中断。

### 注释 4：原第 34 行

在下降沿（falling edge）产生引脚中断。

### 注释 5：原第 36 行

在双边沿（both edges）产生引脚中断。

### 注释 6：原第 38 行

在低电平（low level）产生引脚中断。

### 注释 7：原第 40 行

在高电平（high level）产生引脚中断。

### 注释 8：原第 44 行

NXP PINT 引脚中断的回调（callback）。

### 注释 9：原第 90 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_NXP_PINT_H_`。

## 14.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html)
- [nxp_pint_trigger](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#aea62e6522d0de4c0ce63ae04b2d36f7c)
- [NXP_PINT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#aea62e6522d0de4c0ce63ae04b2d36f7ca8594c4bbe2858dd19a176d851a6175c5)
- [NXP_PINT_RISING](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#aea62e6522d0de4c0ce63ae04b2d36f7ca20ed11aa9c65c91d30b169ae8a754d40)
- [NXP_PINT_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#aea62e6522d0de4c0ce63ae04b2d36f7caf77211604686c8e8f16616b25b9ada9e)
- [NXP_PINT_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#aea62e6522d0de4c0ce63ae04b2d36f7caabce56e3c8a6ba8801b0700bfbf52ec2)
- [NXP_PINT_LOW](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#aea62e6522d0de4c0ce63ae04b2d36f7ca115385d1645fa1901b7ffeab07ff6ce7)
- [NXP_PINT_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#aea62e6522d0de4c0ce63ae04b2d36f7cad94f208bdf7029063172c88673d28b24)
- [nxp_pint_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#a5ceee20d9c423fe9f80e1d72540b4c73)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [nxp_pint_pin_enable](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#abdfe420166b4d28fd7be112b561228bc)
- [nxp_pint_pin_disable](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#a45daffb706e6e51fb805d1bfbd1c4144)
- [nxp_pint_pin_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#a086336be48bc780034f74dbd5aff0bd9)
- [nxp_pint_pin_unset_callback](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#ad7ec8dddcc5a404f38d8d5bb16775a9a)
- [nxp_pint_pin_get_slot_index](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html#aaa54294fced53ad82eefe02f8c4250e2)

---

[上一章](P013_net_if.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P015_parser_url.h_源码浏览.md)
