---
id: learning.zephyr-docs.api-source-architecture-reference.page-18
title: sam0_eic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_sam0\_eic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html)。

## 18.1\_原始可见代码（Source Code）

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
<a id="foldopen00019"></a>
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
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="asam0__eic_8h_html_a5019df444a31531292fbf2fe5af160ef"></a>
<a id="asam0__eic_8h_html_a679adca86ca5da9a49b88bd3110f2f34"></a>
<a id="asam0__eic_8h_html_a679adca86ca5da9a49b88bd3110f2f34a1c8d428daca3fb7b76bae9ecb5427511"></a>
<a id="asam0__eic_8h_html_a679adca86ca5da9a49b88bd3110f2f34a207804f632e291be19b237dde2fd15a9"></a>
<a id="asam0__eic_8h_html_a679adca86ca5da9a49b88bd3110f2f34a61aac8fcb51758fd69b77c3b938d6486"></a>
<a id="asam0__eic_8h_html_a679adca86ca5da9a49b88bd3110f2f34a7fb8fbeb7d3300080b1e54d656b990bc"></a>
<a id="asam0__eic_8h_html_a679adca86ca5da9a49b88bd3110f2f34ad5a9871d1afcbd200a0b3e2e2b7e9871"></a>
<a id="asam0__eic_8h_html_a689981657e7012bca040dac40c5bf28f"></a>
<a id="asam0__eic_8h_html_a6b6009bc8a688ac395ec579d52c25359"></a>
<a id="asam0__eic_8h_html_a7a65e580827b8e0d3f788cc1aaba7ea7"></a>
<a id="asam0__eic_8h_html_a7dd3052cd7fb8074ad0b1233ecaa5708"></a>
<a id="asam0__eic_8h_html_aa6e652726d154e5cda1108aa31d60f26"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2019 Derek Hageman <hageman@inthat.cloud>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_SAM0_EIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_SAM0_EIC_H_

#include <zephyr/types.h>

/* callback for EIC interrupt */
typedef void (*sam0_eic_callback_t)(uint32_t pins, void *data);

enum sam0_eic_trigger {
        /* Rising edge */
        SAM0_EIC_RISING,
        /* Falling edge */
        SAM0_EIC_FALLING,
        /* Both edges */
        SAM0_EIC_BOTH,
        /* High level detection */
        SAM0_EIC_HIGH,
        /* Low level detection */
        SAM0_EIC_LOW,
};

int sam0_eic_acquire(int port, int pin, enum sam0_eic_trigger trigger,
                     bool filter, sam0_eic_callback_t cb, void *data);

int sam0_eic_release(int port, int pin);

int sam0_eic_enable_interrupt(int port, int pin);

int sam0_eic_disable_interrupt(int port, int pin);

uint32_t sam0_eic_interrupt_pending(int port);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_SAM0_EIC_H_ */
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Derek Hageman <hageman@inthat.cloud>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

外部中断控制器中断（EIC Interrupt）的回调（Callback）。

### 注释 3：原第 20 行

上升沿（Rising Edge）。

### 注释 4：原第 22 行

下降沿（Falling Edge）。

### 注释 5：原第 24 行

双边沿（Both Edges）。

### 注释 6：原第 26 行

高电平检测（High Level Detection）。

### 注释 7：原第 28 行

低电平检测（Low Level Detection）。

### 注释 8：原第 85 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_SAM0_EIC_H_`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [sam0_eic_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a689981657e7012bca040dac40c5bf28f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sam0_eic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a679adca86ca5da9a49b88bd3110f2f34)
- [SAM0_EIC_RISING](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a679adca86ca5da9a49b88bd3110f2f34a1c8d428daca3fb7b76bae9ecb5427511)
- [SAM0_EIC_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a679adca86ca5da9a49b88bd3110f2f34a7fb8fbeb7d3300080b1e54d656b990bc)
- [SAM0_EIC_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a679adca86ca5da9a49b88bd3110f2f34ad5a9871d1afcbd200a0b3e2e2b7e9871)
- [SAM0_EIC_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a679adca86ca5da9a49b88bd3110f2f34a61aac8fcb51758fd69b77c3b938d6486)
- [SAM0_EIC_LOW](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a679adca86ca5da9a49b88bd3110f2f34a207804f632e291be19b237dde2fd15a9)
- [sam0_eic_acquire](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a6b6009bc8a688ac395ec579d52c25359)
- [sam0_eic_release](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#aa6e652726d154e5cda1108aa31d60f26)
- [sam0_eic_enable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a7a65e580827b8e0d3f788cc1aaba7ea7)
- [sam0_eic_disable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a5019df444a31531292fbf2fe5af160ef)
- [sam0_eic_interrupt_pending](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html#a7dd3052cd7fb8074ad0b1233ecaa5708)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)

---

[上一章](P017_pinctrl_nxp_port_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P019_sdp.h_源码浏览.md)
