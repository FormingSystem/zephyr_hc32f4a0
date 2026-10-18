---
id: learning.zephyr-docs.api-source-supplement-reference.page-52
title: esp-esp32c5-intmux.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c5-intmux_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_esp-esp32c5-intmux.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c5-intmux_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c5-intmux_8h.html)。

## 52.1\_原始可见代码（Source Code）

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
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00142"></a>

```c
/*
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32C5_INTMUX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32C5_INTMUX_H_



#define WIFI_MAC_INTR_SOURCE           0
#define WIFI_MAC_NMI_SOURCE            1
#define WIFI_PWR_INTR_SOURCE           2
#define WIFI_BB_INTR_SOURCE            3
#define BT_MAC_INTR_SOURCE             4
#define BT_BB_INTR_SOURCE              5
#define BT_BB_NMI_SOURCE               6
#define LP_TIMER_INTR_SOURCE           7
#define COEX_INTR_SOURCE               8
#define BLE_TIMER_INTR_SOURCE          9
#define BLE_SEC_INTR_SOURCE            10
#define I2C_MASTER_SOURCE              11
#define ZB_MAC_SOURCE                  12
#define PMU_INTR_SOURCE                13
#define EFUSE_INTR_SOURCE              14
#define LP_RTC_TIMER_INTR_SOURCE       15
#define LP_UART_INTR_SOURCE            16
#define LP_I2C_INTR_SOURCE             17
#define LP_WDT_INTR_SOURCE             18
#define LP_PERI_TIMEOUT_INTR_SOURCE    19
#define LP_APM_M0_INTR_SOURCE          20
#define LP_APM_M1_INTR_SOURCE          21
#define HUK_INTR_SOURCE                22
#define FROM_CPU_INTR0_SOURCE          23
#define FROM_CPU_INTR1_SOURCE          24
#define FROM_CPU_INTR2_SOURCE          25
#define FROM_CPU_INTR3_SOURCE          26
#define ASSIST_DEBUG_INTR_SOURCE       27
#define TRACE_INTR_SOURCE              28
#define CACHE_INTR_SOURCE              29
#define CPU_PERI_TIMEOUT_INTR_SOURCE   30
#define GPIO_INTR_SOURCE               31
#define GPIO_EXT_SOURCE                32
#define PAU_INTR_SOURCE                33
#define HP_PERI_TIMEOUT_INTR_SOURCE    34
#define MODEM_PERI_TIMEOUT_INTR_SOURCE 35
#define HP_APM_M0_INTR_SOURCE          36
#define HP_APM_M1_INTR_SOURCE          37
#define HP_APM_M2_INTR_SOURCE          38
#define HP_APM_M3_INTR_SOURCE          39
#define HP_APM_M4_INTR_SOURCE          40
#define LP_APM0_INTR_SOURCE            41
#define CPU_APM_M0_INTR_SOURCE         42
#define CPU_APM_M1_INTR_SOURCE         43
#define MSPI_INTR_SOURCE               44
#define I2S0_INTR_SOURCE               45
#define UHCI0_INTR_SOURCE              46
#define UART0_INTR_SOURCE              47
#define UART1_INTR_SOURCE              48
#define LEDC_INTR_SOURCE               49
#define TWAI0_INTR_SOURCE              50
#define TWAI0_TIMER_INTR_SOURCE        51
#define TWAI1_INTR_SOURCE              52
#define TWAI1_TIMER_INTR_SOURCE        53
#define USB_SERIAL_JTAG_INTR_SOURCE    54
#define RMT_INTR_SOURCE                55
#define I2C_EXT0_INTR_SOURCE           56
#define TG0_T0_LEVEL_INTR_SOURCE       57
#define TG0_WDT_LEVEL_INTR_SOURCE      58
#define TG1_T0_LEVEL_INTR_SOURCE       59
#define TG1_WDT_LEVEL_INTR_SOURCE      60
#define SYSTIMER_TARGET0_INTR_SOURCE   61
#define SYSTIMER_TARGET1_INTR_SOURCE   62
#define SYSTIMER_TARGET2_INTR_SOURCE   63
#define APB_ADC_INTR_SOURCE            64
#define MCPWM0_INTR_SOURCE             65
#define PCNT_INTR_SOURCE               66
#define PARL_IO_TX_INTR_SOURCE         67
#define PARL_IO_RX_INTR_SOURCE         68
#define SLC0_INTR_SOURCE               69
#define SLC1_INTR_SOURCE               70
#define DMA_IN_CH0_INTR_SOURCE         71
#define DMA_IN_CH1_INTR_SOURCE         72
#define DMA_IN_CH2_INTR_SOURCE         73
#define DMA_OUT_CH0_INTR_SOURCE        74
#define DMA_OUT_CH1_INTR_SOURCE        75
#define DMA_OUT_CH2_INTR_SOURCE        76
#define GSPI2_INTR_SOURCE              77
#define AES_INTR_SOURCE                78
#define SHA_INTR_SOURCE                79
#define RSA_INTR_SOURCE                80
#define ECC_INTR_SOURCE                81
#define ECDSA_INTR_SOURCE              82
#define KM_INTR_SOURCE                 83
#define MAX_INTR_SOURCE                84

#define IRQ_DEFAULT_PRIORITY 0

#define ESP_INTR_FLAG_SHARED (1 << 8)

/* LP Core intmux */
#define LP_CORE_IO_INTR_SOURCE    0
#define LP_CORE_I2C_INTR_SOURCE   1
#define LP_CORE_UART_INTR_SOURCE  2
#define LP_CORE_TIMER_INTR_SOURCE 3
#define LP_CORE_PMU_INTR_SOURCE   5



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32C5_INTMUX_H_ */
```

## 52.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 131 行

低功耗核（LP Core）的中断多路复用器（intmux）。

### 注释 3：原第 142 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32C5_INTMUX_H_`。

## 52.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c5-intmux_8h.html)

---

[上一章](P051_ene-kb1200-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P053_esp-esp32p4-intmux.h_源码浏览.md)
