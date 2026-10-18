---
id: learning.zephyr-docs.api-source-configuration-reference.page-108
title: stm32f1-afio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-afio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_stm32f1-afio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-afio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-afio_8h.html)。

## 108.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>

```c
/*
 * Copyright (c) 2021 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32F1_AFIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32F1_AFIO_H_

#define STM32_REMAP_REG_MASK    0x1U
#define STM32_REMAP_REG_SHIFT   0U
#define STM32_REMAP_SHIFT_MASK  0x1FU
#define STM32_REMAP_SHIFT_SHIFT 1U
#define STM32_REMAP_MASK_MASK   0x3U
#define STM32_REMAP_MASK_SHIFT  6U
#define STM32_REMAP_VAL_MASK    0x3U
#define STM32_REMAP_VAL_SHIFT   8U

#define STM32_REMAP(val, mask, shift, reg)                                     \
        ((((reg) & STM32_REMAP_REG_MASK) << STM32_REMAP_REG_SHIFT) |           \
         (((shift) & STM32_REMAP_SHIFT_MASK) << STM32_REMAP_SHIFT_SHIFT) |     \
         (((mask) & STM32_REMAP_MASK_MASK) << STM32_REMAP_MASK_SHIFT) |        \
         (((val) & STM32_REMAP_VAL_MASK) << STM32_REMAP_VAL_SHIFT))


/* Accessors for remap value */

#define STM32_REMAP_REG_GET(remap) \
        (((remap) >> STM32_REMAP_REG_SHIFT) & STM32_REMAP_REG_MASK)

#define STM32_REMAP_SHIFT_GET(remap) \
        (((remap) >> STM32_REMAP_SHIFT_SHIFT) & STM32_REMAP_SHIFT_MASK)

#define STM32_REMAP_MASK_GET(remap) \
        (((remap) >> STM32_REMAP_MASK_SHIFT) & STM32_REMAP_MASK_MASK)

#define STM32_REMAP_VAL_GET(remap) \
        (((remap) >> STM32_REMAP_VAL_SHIFT) & STM32_REMAP_VAL_MASK)


/* Remap values definitions, according to RM0008.pdf */

#define STM32_AFIO_MAPR         0U
#define STM32_AFIO_MAPR2        1U

#define NO_REMAP                0

#define SPI1_REMAP0             STM32_REMAP(0U, 0x1U, 0U, STM32_AFIO_MAPR)
#define SPI1_REMAP1             STM32_REMAP(1U, 0x1U, 0U, STM32_AFIO_MAPR)

#define I2C1_REMAP0             STM32_REMAP(0U, 0x1U, 1U, STM32_AFIO_MAPR)
#define I2C1_REMAP1             STM32_REMAP(1U, 0x1U, 1U, STM32_AFIO_MAPR)

#define USART1_REMAP0           STM32_REMAP(0U, 0x1U, 2U, STM32_AFIO_MAPR)
#define USART1_REMAP1           STM32_REMAP(1U, 0x1U, 2U, STM32_AFIO_MAPR)

#define USART2_REMAP0           STM32_REMAP(0U, 0x1U, 3U, STM32_AFIO_MAPR)
#define USART2_REMAP1           STM32_REMAP(1U, 0x1U, 3U, STM32_AFIO_MAPR)

#define USART3_REMAP0           STM32_REMAP(0U, 0x3U, 4U, STM32_AFIO_MAPR)
#define USART3_REMAP1           STM32_REMAP(1U, 0x3U, 4U, STM32_AFIO_MAPR)
#define USART3_REMAP2           STM32_REMAP(3U, 0x3U, 4U, STM32_AFIO_MAPR)

#define TIM1_REMAP0             STM32_REMAP(0U, 0x3U, 6U, STM32_AFIO_MAPR)
#define TIM1_REMAP1             STM32_REMAP(1U, 0x3U, 6U, STM32_AFIO_MAPR)
#define TIM1_REMAP2             STM32_REMAP(3U, 0x3U, 6U, STM32_AFIO_MAPR)

#define TIM2_REMAP0             STM32_REMAP(0U, 0x3U, 8U, STM32_AFIO_MAPR)
#define TIM2_REMAP1             STM32_REMAP(1U, 0x3U, 8U, STM32_AFIO_MAPR)
#define TIM2_REMAP2             STM32_REMAP(2U, 0x3U, 8U, STM32_AFIO_MAPR)
#define TIM2_REMAP3             STM32_REMAP(3U, 0x3U, 8U, STM32_AFIO_MAPR)

#define TIM3_REMAP0             STM32_REMAP(0U, 0x3U, 10U, STM32_AFIO_MAPR)
#define TIM3_REMAP1             STM32_REMAP(1U, 0x3U, 10U, STM32_AFIO_MAPR)
#define TIM3_REMAP2             STM32_REMAP(2U, 0x3U, 10U, STM32_AFIO_MAPR)
#define TIM3_REMAP3             STM32_REMAP(3U, 0x3U, 10U, STM32_AFIO_MAPR)

#define TIM4_REMAP0             STM32_REMAP(0U, 0x1U, 12U, STM32_AFIO_MAPR)
#define TIM4_REMAP1             STM32_REMAP(1U, 0x1U, 12U, STM32_AFIO_MAPR)

#define CAN_REMAP0              STM32_REMAP(0U, 0x3U, 13U, STM32_AFIO_MAPR)
#define CAN_REMAP1              STM32_REMAP(2U, 0x3U, 13U, STM32_AFIO_MAPR)
#define CAN_REMAP2              STM32_REMAP(3U, 0x3U, 13U, STM32_AFIO_MAPR)

#define CAN1_REMAP0             CAN_REMAP0
#define CAN1_REMAP1             CAN_REMAP1
#define CAN1_REMAP2             CAN_REMAP2

#define ETH_REMAP0              STM32_REMAP(0U, 0x1U, 21U, STM32_AFIO_MAPR)
#define ETH_REMAP1              STM32_REMAP(1U, 0x1U, 21U, STM32_AFIO_MAPR)

#define CAN2_REMAP0             STM32_REMAP(0U, 0x1U, 22U, STM32_AFIO_MAPR)
#define CAN2_REMAP1             STM32_REMAP(1U, 0x1U, 22U, STM32_AFIO_MAPR)

#define SPI3_REMAP0             STM32_REMAP(0U, 0x1U, 28U, STM32_AFIO_MAPR)
#define SPI3_REMAP1             STM32_REMAP(1U, 0x1U, 28U, STM32_AFIO_MAPR)

#define I2S3_REMAP0             SPI3_REMAP0
#define I2S3_REMAP1             SPI3_REMAP1

#define TIM9_REMAP0             STM32_REMAP(0U, 0x1U, 5U, STM32_AFIO_MAPR2)
#define TIM9_REMAP1             STM32_REMAP(1U, 0x1U, 5U, STM32_AFIO_MAPR2)

#define TIM10_REMAP0            STM32_REMAP(0U, 0x1U, 6U, STM32_AFIO_MAPR2)
#define TIM10_REMAP1            STM32_REMAP(1U, 0x1U, 6U, STM32_AFIO_MAPR2)

#define TIM11_REMAP0            STM32_REMAP(0U, 0x1U, 7U, STM32_AFIO_MAPR2)
#define TIM11_REMAP1            STM32_REMAP(1U, 0x1U, 7U, STM32_AFIO_MAPR2)

#define TIM13_REMAP0            STM32_REMAP(0U, 0x1U, 8U, STM32_AFIO_MAPR2)
#define TIM13_REMAP1            STM32_REMAP(1U, 0x1U, 8U, STM32_AFIO_MAPR2)

#define TIM14_REMAP0            STM32_REMAP(0U, 0x1U, 9U, STM32_AFIO_MAPR2)
#define TIM14_REMAP1            STM32_REMAP(1U, 0x1U, 9U, STM32_AFIO_MAPR2)

#define TIM15_REMAP0            STM32_REMAP(0U, 0x1U, 0U, STM32_AFIO_MAPR2)
#define TIM15_REMAP1            STM32_REMAP(1U, 0x1U, 0U, STM32_AFIO_MAPR2)

#define TIM16_REMAP0            STM32_REMAP(0U, 0x1U, 1U, STM32_AFIO_MAPR2)
#define TIM16_REMAP1            STM32_REMAP(1U, 0x1U, 1U, STM32_AFIO_MAPR2)

#define TIM17_REMAP0            STM32_REMAP(0U, 0x1U, 2U, STM32_AFIO_MAPR2)
#define TIM17_REMAP1            STM32_REMAP(1U, 0x1U, 2U, STM32_AFIO_MAPR2)

#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32F1_AFIO_H_ */
```

## 108.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

重映射值（Remap value）的访问函数。

### 注释 3：原第 74 行

依据 `RM0008.pdf` 定义的重映射值。

### 注释 4：原第 211 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32F1_AFIO_H_`。

## 108.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-afio_8h.html)

---

[上一章](P107_stdlib.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P109_stm32f1-pinctrl.h_源码浏览.md)
