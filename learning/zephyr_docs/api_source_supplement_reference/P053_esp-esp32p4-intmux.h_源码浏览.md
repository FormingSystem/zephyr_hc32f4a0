---
id: learning.zephyr-docs.api-source-supplement-reference.page-53
title: esp-esp32p4-intmux.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32p4-intmux_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_esp-esp32p4-intmux.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32p4-intmux_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32p4-intmux_8h.html)。

## 53.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00036"></a>
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
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
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
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00168"></a>

```c
/*
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32P4_INTMUX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32P4_INTMUX_H_



/* Derived from components/soc/esp32p4/include/soc/interrupts.h */
#define LP_RTC_INTR_SOURCE                  0
#define LP_WDT_INTR_SOURCE                  1
#define LP_TIMER_REG0_INTR_SOURCE           2
#define LP_TIMER_REG1_INTR_SOURCE           3
#define MB_HP_INTR_SOURCE                   4
#define MB_LP_INTR_SOURCE                   5
#define PMU_0_INTR_SOURCE                   6
#define PMU_1_INTR_SOURCE                   7
#define LP_ANAPERI_INTR_SOURCE              8
#define LP_ADC_INTR_SOURCE                  9
#define LP_GPIO_INTR_SOURCE                 10
#define LP_I2C_INTR_SOURCE                  11
#define LP_I2S_INTR_SOURCE                  12
#define LP_SPI_INTR_SOURCE                  13
#define LP_TOUCH_INTR_SOURCE                14
#define LP_TSENS_INTR_SOURCE                15
#define LP_UART_INTR_SOURCE                 16
#define LP_EFUSE_INTR_SOURCE                17
#define LP_SW_INTR_SOURCE                   18
#define LP_SYSREG_INTR_SOURCE               19
#define LP_HUK_INTR_SOURCE                  20
#define SYS_ICM_INTR_SOURCE                 21
#define USB_SERIAL_JTAG_INTR_SOURCE         22
#define SDIO_HOST_INTR_SOURCE               23
#define DW_GDMA_INTR_SOURCE                 24
#define SPI2_INTR_SOURCE                    25
#define SPI3_INTR_SOURCE                    26
#define I2S0_INTR_SOURCE                    27
#define I2S1_INTR_SOURCE                    28
#define I2S2_INTR_SOURCE                    29
#define UHCI0_INTR_SOURCE                   30
#define UART0_INTR_SOURCE                   31
#define UART1_INTR_SOURCE                   32
#define UART2_INTR_SOURCE                   33
#define UART3_INTR_SOURCE                   34
#define UART4_INTR_SOURCE                   35
#define LCD_CAM_INTR_SOURCE                 36
#define ADC_INTR_SOURCE                     37
#define PWM0_INTR_SOURCE                    38
#define PWM1_INTR_SOURCE                    39
#define TWAI0_INTR_SOURCE                   40
#define TWAI1_INTR_SOURCE                   41
#define TWAI2_INTR_SOURCE                   42
#define RMT_INTR_SOURCE                     43
#define I2C0_INTR_SOURCE                    44
#define I2C1_INTR_SOURCE                    45
#define TG0_T0_LEVEL_INTR_SOURCE            46
#define TG0_T1_LEVEL_INTR_SOURCE            47
#define TG0_WDT_LEVEL_INTR_SOURCE           48
#define TG1_T0_LEVEL_INTR_SOURCE            49
#define TG1_T1_LEVEL_INTR_SOURCE            50
#define TG1_WDT_LEVEL_INTR_SOURCE           51
#define LEDC_INTR_SOURCE                    52
#define SYSTIMER_TARGET0_INTR_SOURCE        53
#define SYSTIMER_TARGET1_INTR_SOURCE        54
#define SYSTIMER_TARGET2_INTR_SOURCE        55
#define AHB_PDMA_IN_CH0_INTR_SOURCE         56
#define AHB_PDMA_IN_CH1_INTR_SOURCE         57
#define AHB_PDMA_IN_CH2_INTR_SOURCE         58
#define AHB_PDMA_OUT_CH0_INTR_SOURCE        59
#define AHB_PDMA_OUT_CH1_INTR_SOURCE        60
#define AHB_PDMA_OUT_CH2_INTR_SOURCE        61
#define AXI_PDMA_IN_CH0_INTR_SOURCE         62
#define AXI_PDMA_IN_CH1_INTR_SOURCE         63
#define AXI_PDMA_IN_CH2_INTR_SOURCE         64
#define AXI_PDMA_OUT_CH0_INTR_SOURCE        65
#define AXI_PDMA_OUT_CH1_INTR_SOURCE        66
#define AXI_PDMA_OUT_CH2_INTR_SOURCE        67
#define RSA_INTR_SOURCE                     68
#define AES_INTR_SOURCE                     69
#define SHA_INTR_SOURCE                     70
#define ECC_INTR_SOURCE                     71
#define ECDSA_INTR_SOURCE                   72
#define KM_INTR_SOURCE                      73
#define GPIO_INTR0_SOURCE                   74
#define GPIO_INTR1_SOURCE                   75
#define GPIO_INTR2_SOURCE                   76
#define GPIO_INTR3_SOURCE                   77
#define GPIO_PAD_COMP_INTR_SOURCE           78
#define FROM_CPU_INTR0_SOURCE               79
#define FROM_CPU_INTR1_SOURCE               80
#define FROM_CPU_INTR2_SOURCE               81
#define FROM_CPU_INTR3_SOURCE               82
#define CACHE_INTR_SOURCE                   83
#define MSPI_INTR_SOURCE                    84
#define CSI_BRIDGE_INTR_SOURCE              85
#define DSI_BRIDGE_INTR_SOURCE              86
#define CSI_INTR_SOURCE                     87
#define DSI_INTR_SOURCE                     88
#define GMII_PHY_INTR_SOURCE                89
#define LPI_INTR_SOURCE                     90
#define PMT_INTR_SOURCE                     91
#define ETH_MAC_INTR_SOURCE                 92
#define USB_OTG_INTR_SOURCE                 93
#define USB_OTG_ENDP_MULTI_PROC_INTR_SOURCE 94
#define JPEG_INTR_SOURCE                    95
#define PPA_INTR_SOURCE                     96
#define CORE0_TRACE_INTR_SOURCE             97
#define CORE1_TRACE_INTR_SOURCE             98
#define HP_CORE_CTRL_INTR_SOURCE            99
#define ISP_INTR_SOURCE                     100
#define I3C_MST_INTR_SOURCE                 101
#define I3C_SLV_INTR_SOURCE                 102
#define USB_OTG11_CH0_INTR_SOURCE           103
#define DMA2D_IN_CH0_INTR_SOURCE            104
#define DMA2D_IN_CH1_INTR_SOURCE            105
#define DMA2D_OUT_CH0_INTR_SOURCE           106
#define DMA2D_OUT_CH1_INTR_SOURCE           107
#define DMA2D_OUT_CH2_INTR_SOURCE           108
#define PSRAM_MSPI_INTR_SOURCE              109
#define HP_SYSREG_INTR_SOURCE               110
#define PCNT_INTR_SOURCE                    111
#define HP_PAU_INTR_SOURCE                  112
#define HP_PARLIO_RX_INTR_SOURCE            113
#define HP_PARLIO_TX_INTR_SOURCE            114
#define ASSIST_DEBUG_INTR_SOURCE            120

#define IRQ_DEFAULT_PRIORITY 0



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32P4_INTMUX_H_ */
```

## 53.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

派生自 `components/soc/esp32p4/include/soc/interrupts.h`。

### 注释 3：原第 168 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32P4_INTMUX_H_`。

## 53.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32p4-intmux_8h.html)

---

[上一章](P052_esp-esp32c5-intmux.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P054_esp32-gpio-sigmap.h_源码浏览.md)
