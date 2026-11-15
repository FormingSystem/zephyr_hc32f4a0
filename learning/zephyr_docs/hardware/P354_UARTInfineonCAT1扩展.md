---
id: learning.zephyr-docs.hardware.uartext-1
title: UARTInfineonCAT1扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__ifx__cat1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第354章\_UARTInfineonCAT1扩展

原文：[uart__ifx__cat1_8h](https://docs.zephyrproject.org/latest/doxygen/html/uart__ifx__cat1_8h.html)。读取日期：2026-10-13，`latest`。

## 354.1\_驱动头文件范围

`zephyr/drivers/serial/uart_ifx_cat1.h` 为 Infineon CAT1 系列通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）驱动头文件。Infineon、CAT1 和宏前缀 IFX 是厂商及系列名称，本页不将它们扩写为额外缩写。

原页列出的包含文件如下：

```c
#include <zephyr/drivers/uart.h>
#include <string.h>
#include <cy_scb_uart.h>
#include <cy_gpio.h>
#include <cy_syslib.h>
#include <cy_sysint.h>
```

## 354.2\_中断配置宏

中断服务程序（Interrupt Service Routine，ISR）处理硬件中断请求（Interrupt Request，IRQ）。原生成页面仅列出下列宏表达式，没有进一步行为说明；条件中 Cortex-M0+ 和 `CY_*` 等名称均为厂商配置标识符。

| 宏 | 原定义 |
| --- | --- |
| [`IFX_CAT1_ISR_PRIORITY_DEFAULT`](https://docs.zephyrproject.org/latest/doxygen/html/uart__ifx__cat1_8h.html#aebed73fb7d617c8b5b672406c8df85cb) | `(7)` |
| [`IFX_CAT1_IRQ_MUXING`](https://docs.zephyrproject.org/latest/doxygen/html/uart__ifx__cat1_8h.html#aded1c35b47b7352b6445341735a3b588) | `(CY_CPU_CORTEX_M0P || CPUSS_SYSTEM_IRQ_PRESENT)` |
| [`IFX_CAT1_IRQ_LEGACY_M0`](https://docs.zephyrproject.org/latest/doxygen/html/uart__ifx__cat1_8h.html#a6a8692c7e42f877851a44843f8a234d6) | `(CY_CPU_CORTEX_M0P && (1u == CY_IP_M4CPUSS_VERSION))` |

宏名分别表示默认 ISR 优先级、IRQ 复用（Multiplexing）条件及旧式 M0 IRQ 条件；具体逻辑保持原表达式，不把某个厂商配置符的名字推测为通用接口能力。

---

[上一章：UARTAltera扩展](P353_UARTAltera扩展.md) · [下一章：UARTIntelLW扩展](P355_UARTIntelLW扩展.md) · [返回大纲](大纲.md)
