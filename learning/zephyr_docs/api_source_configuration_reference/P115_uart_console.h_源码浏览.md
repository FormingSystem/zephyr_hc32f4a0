---
id: learning.zephyr-docs.api-source-configuration-reference.page-115
title: uart_console.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__console_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第115章\_uart\_console.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__console_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/uart__console_8h.html)。

## 115.1\_原始可见代码（Source Code）

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
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__fifo_html"></a>
<a id="auart__console_8h_html_a090eed88ce36e49ecea535d61746abd5"></a>

```c
/* uart_console.h - uart console driver */

/*
 * Copyright (c) 2011, 2014 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_CONSOLE_UART_CONSOLE_H_
#define ZEPHYR_INCLUDE_DRIVERS_CONSOLE_UART_CONSOLE_H_

#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

void uart_register_input(struct k_fifo *avail, struct k_fifo *lines,
                         uint8_t (*completion)(char *str, uint8_t len));

/*
 * Allows having debug hooks in the console driver for handling incoming
 * control characters, and letting other ones through.
 */
#ifdef CONFIG_UART_CONSOLE_DEBUG_SERVER_HOOKS
#define UART_CONSOLE_DEBUG_HOOK_HANDLED 1
#define UART_CONSOLE_OUT_DEBUG_HOOK_SIG(x) int(x)(char c)
typedef UART_CONSOLE_OUT_DEBUG_HOOK_SIG(uart_console_out_debug_hook_t);

void uart_console_out_debug_hook_install(
                                uart_console_out_debug_hook_t *hook);

typedef int (*uart_console_in_debug_hook_t) (uint8_t);

void uart_console_in_debug_hook_install(uart_console_in_debug_hook_t hook);

#endif

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_CONSOLE_UART_CONSOLE_H_ */
```

## 115.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`uart_console.h`：UART 控制台驱动（UART console driver）。

### 注释 2：原第 3 行

版权（Copyright）：© 2011, 2014 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 33 行

允许在控制台驱动中设置调试钩子（Debug hooks），以处理传入的控制字符，并让其他字符继续通过。

### 注释 4：原第 55 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CONSOLE_UART_CONSOLE_H_`。

## 115.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/uart__console_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [uart_register_input](https://docs.zephyrproject.org/latest/doxygen/html/uart__console_8h.html#a090eed88ce36e49ecea535d61746abd5)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P114_exception.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P116_unistd.h_源码浏览.md)
