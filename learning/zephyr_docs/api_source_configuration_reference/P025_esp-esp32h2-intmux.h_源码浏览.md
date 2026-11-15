---
id: learning.zephyr-docs.api-source-configuration-reference.page-25
title: esp-esp32h2-intmux.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32h2-intmux_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_esp-esp32h2-intmux.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32h2-intmux_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32h2-intmux_8h.html)。

## 25.1\_原始可见代码（Source Code）

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
<a id="l00033"></a>
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
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
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
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>

```c
/*
 * Copyright (c) 2025 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32H2_INTMUX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32H2_INTMUX_H_



#define PMU_INTR_SOURCE                   0
#define EFUSE_INTR_SOURCE                 1
#define LP_RTC_TIMER_INTR_SOURCE          2
#define LP_BLE_TIMER_INTR_SOURCE          3
#define LP_WDT_INTR_SOURCE                4
#define LP_PERI_TIMEOUT_INTR_SOURCE       5
#define LP_APM_M0_INTR_SOURCE             6
#define FROM_CPU_INTR0_SOURCE             7
#define FROM_CPU_INTR1_SOURCE             8
#define FROM_CPU_INTR2_SOURCE             9
#define FROM_CPU_INTR3_SOURCE             10
#define ASSIST_DEBUG_INTR_SOURCE          11
#define TRACE_INTR_SOURCE                 12
#define CACHE_INTR_SOURCE                 13
#define CPU_PERI_TIMEOUT_INTR_SOURCE      14
#define BT_MAC_INTR_SOURCE                15
#define BT_BB_INTR_SOURCE                 16
#define BT_BB_NMI_INTR_SOURCE             17
#define COEX_INTR_SOURCE                  18
#define BLE_TIMER_INTR_SOURCE             19
#define BLE_SEC_INTR_SOURCE               20
#define ZB_MAC_INTR_SOURCE                21
#define GPIO_INTR_SOURCE                  22
#define GPIO_NMI_SOURCE                   23
#define PAU_INTR_SOURCE                   24
#define HP_PERI_TIMEOUT_INTR_SOURCE       25
#define HP_APM_M0_INTR_SOURCE             26
#define HP_APM_M1_INTR_SOURCE             27
#define HP_APM_M2_INTR_SOURCE             28
#define HP_APM_M3_INTR_SOURCE             29
#define MSPI_INTR_SOURCE                  30
#define I2S1_INTR_SOURCE                  31
#define UHCI0_INTR_SOURCE                 32
#define UART0_INTR_SOURCE                 33
#define UART1_INTR_SOURCE                 34
#define LEDC_INTR_SOURCE                  35
#define TWAI0_INTR_SOURCE                 36
#define USB_SERIAL_JTAG_INTR_SOURCE       37
#define RMT_INTR_SOURCE                   38
#define I2C_EXT0_INTR_SOURCE              39
#define I2C_EXT1_INTR_SOURCE              40
#define TG0_T0_LEVEL_INTR_SOURCE          41
#define TG0_WDT_LEVEL_INTR_SOURCE         42
#define TG1_T0_LEVEL_INTR_SOURCE          43
#define TG1_WDT_LEVEL_INTR_SOURCE         44
#define SYSTIMER_TARGET0_EDGE_INTR_SOURCE 45
#define SYSTIMER_TARGET1_EDGE_INTR_SOURCE 46
#define SYSTIMER_TARGET2_EDGE_INTR_SOURCE 47
#define APB_ADC_INTR_SOURCE               48
#define MCPWM0_INTR_SOURCE                49
#define PCNT_INTR_SOURCE                  50
#define PARL_IO_TX_INTR_SOURCE            51
#define PARL_IO_RX_INTR_SOURCE            52
#define DMA_IN_CH0_INTR_SOURCE            53
#define DMA_IN_CH1_INTR_SOURCE            54
#define DMA_IN_CH2_INTR_SOURCE            55
#define DMA_OUT_CH0_INTR_SOURCE           56
#define DMA_OUT_CH1_INTR_SOURCE           57
#define DMA_OUT_CH2_INTR_SOURCE           58
#define GSPI2_INTR_SOURCE                 59
#define AES_INTR_SOURCE                   60
#define SHA_INTR_SOURCE                   61
#define RSA_INTR_SOURCE                   62
#define ECC_INTR_SOURCE                   63
#define ECDSA_INTR_SOURCE                 64
#define MAX_INTR_SOURCE                   65

/* Zero will allocate low/medium levels of priority (ESP_INTR_FLAG_LOWMED) */
#define IRQ_DEFAULT_PRIORITY 0

#define ESP_INTR_FLAG_SHARED (1 << 8) /* Interrupt can be shared between ISRs */



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32H2_INTMUX_H_ */
```

## 25.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 103 行

零值会分配低/中优先级（`ESP_INTR_FLAG_LOWMED`）。

### 注释 3：原第 106 行

中断可由多个中断服务程序（ISR）共享。

### 注释 4：原第 112 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32H2_INTMUX_H_`。

## 25.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32h2-intmux_8h.html)

---

[上一章](P024_esp-esp32c3-intmux.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P026_espi_emul.h_源码浏览.md)
