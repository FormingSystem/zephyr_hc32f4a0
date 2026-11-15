---
id: learning.zephyr-docs.api-source-scheduler-interrupt-reference.page-2
title: esp-esp32c6-intmux.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c6-intmux_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_esp-esp32c6-intmux.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c6-intmux_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P082_zephyr__dt-bindings__interrupt-controller__esp-esp32c6-intmux.h_文件参考.md)。

## 2.1\_原始可见代码（Source Code）

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
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>

```c
/*
 * Copyright (c) 2023 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32C6_INTMUX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32C6_INTMUX_H_



#define WIFI_MAC_INTR_SOURCE                0  /* interrupt of WiFi MAC, level*/
#define WIFI_MAC_NMI_SOURCE                 1  /* interrupt of WiFi MAC, NMI*/
#define WIFI_PWR_INTR_SOURCE                2
#define WIFI_BB_INTR_SOURCE                 3  /* interrupt of WiFi BB, level*/
#define BT_MAC_INTR_SOURCE                  4  /* will be cancelled*/
#define BT_BB_INTR_SOURCE                   5  /* interrupt of BT BB, level*/
#define BT_BB_NMI_SOURCE                    6  /* interrupt of BT BB, NMI*/
#define LP_TIMER_INTR_SOURCE                7
#define COEX_INTR_SOURCE                    8
#define BLE_TIMER_INTR_SOURCE               9
#define BLE_SEC_INTR_SOURCE                10
#define I2C_MASTER_SOURCE                  11  /* interrupt of I2C Master, level*/
#define ZB_MAC_SOURCE                      12
#define PMU_INTR_SOURCE                    13
#define EFUSE_INTR_SOURCE                  14  /* interrupt of efuse, level, not likely to use*/
#define LP_RTC_TIMER_INTR_SOURCE           15
#define LP_UART_INTR_SOURCE                16
#define LP_I2C_INTR_SOURCE                 17
#define LP_WDT_INTR_SOURCE                 18
#define LP_PERI_TIMEOUT_INTR_SOURCE        19
#define LP_APM_M0_INTR_SOURCE              20
#define LP_APM_M1_INTR_SOURCE              21
#define FROM_CPU_INTR0_SOURCE              22  /* interrupt0 generated from a CPU, level*/
#define FROM_CPU_INTR1_SOURCE              23  /* interrupt1 generated from a CPU, level*/
#define FROM_CPU_INTR2_SOURCE              24  /* interrupt2 generated from a CPU, level*/
#define FROM_CPU_INTR3_SOURCE              25  /* interrupt3 generated from a CPU, level*/
#define ASSIST_DEBUG_INTR_SOURCE           26  /* interrupt of Assist debug module, LEVEL*/
#define TRACE_INTR_SOURCE                  27
#define CACHE_INTR_SOURCE                  28
#define CPU_PERI_TIMEOUT_INTR_SOURCE       29
#define GPIO_INTR_SOURCE                   30  /* interrupt of GPIO, level*/
#define GPIO_NMI_SOURCE                    31  /* interrupt of GPIO, NMI*/
#define PAU_INTR_SOURCE                    32
#define HP_PERI_TIMEOUT_INTR_SOURCE        33
#define MODEM_PERI_TIMEOUT_INTR_SOURCE     34
#define HP_APM_M0_INTR_SOURCE              35
#define HP_APM_M1_INTR_SOURCE              36
#define HP_APM_M2_INTR_SOURCE              37
#define HP_APM_M3_INTR_SOURCE              38
#define LP_APM0_INTR_SOURCE                39
#define MSPI_INTR_SOURCE                   40
#define I2S1_INTR_SOURCE                   41  /* interrupt of I2S1, level*/
#define UHCI0_INTR_SOURCE                  42  /* interrupt of UHCI0, level*/
#define UART0_INTR_SOURCE                  43  /* interrupt of UART0, level*/
#define UART1_INTR_SOURCE                  44  /* interrupt of UART1, level*/
#define LEDC_INTR_SOURCE                   45  /* interrupt of LED PWM, level*/
#define TWAI0_INTR_SOURCE                  46  /* interrupt of can0, level*/
#define TWAI1_INTR_SOURCE                  47  /* interrupt of can1, level*/
#define USB_SERIAL_JTAG_INTR_SOURCE        48  /* interrupt of USB, level*/
#define RMT_INTR_SOURCE                    49  /* interrupt of remote controller, level*/
#define I2C_EXT0_INTR_SOURCE               50  /* interrupt of I2C controller1, level*/
#define TG0_T0_LEVEL_INTR_SOURCE           51  /* interrupt of TIMER_GROUP0, TIMER0, level*/
#define TG0_T1_LEVEL_INTR_SOURCE           52  /* interrupt of TIMER_GROUP0, TIMER1, level*/
#define TG0_WDT_LEVEL_INTR_SOURCE          53  /* interrupt of TIMER_GROUP0, WATCH DOG, level*/
#define TG1_T0_LEVEL_INTR_SOURCE           54  /* interrupt of TIMER_GROUP1, TIMER0, level*/
#define TG1_T1_LEVEL_INTR_SOURCE           55  /* interrupt of TIMER_GROUP1, TIMER1, level*/
#define TG1_WDT_LEVEL_INTR_SOURCE          56  /* interrupt of TIMER_GROUP1, WATCHDOG, level*/
#define SYSTIMER_TARGET0_EDGE_INTR_SOURCE  57  /* interrupt of system timer 0, EDGE*/
#define SYSTIMER_TARGET1_EDGE_INTR_SOURCE  58  /* interrupt of system timer 1, EDGE*/
#define SYSTIMER_TARGET2_EDGE_INTR_SOURCE  59  /* interrupt of system timer 2, EDGE*/
#define APB_ADC_INTR_SOURCE                60  /* interrupt of APB ADC, LEVEL*/
#define MCPWM0_INTR_SOURCE                 61  /* interrupt of MCPWM0, LEVEL*/
#define PCNT_INTR_SOURCE                   62
#define PARL_IO_INTR_SOURCE                63
#define SLC0_INTR_SOURCE                   64
#define SLC_INTR_SOURCE                    65
#define DMA_IN_CH0_INTR_SOURCE             66  /* interrupt of general DMA IN channel 0, LEVEL*/
#define DMA_IN_CH1_INTR_SOURCE             67  /* interrupt of general DMA IN channel 1, LEVEL*/
#define DMA_IN_CH2_INTR_SOURCE             68  /* interrupt of general DMA IN channel 2, LEVEL*/
#define DMA_OUT_CH0_INTR_SOURCE            69  /* interrupt of general DMA OUT channel 0, LEVEL*/
#define DMA_OUT_CH1_INTR_SOURCE            70  /* interrupt of general DMA OUT channel 1, LEVEL*/
#define DMA_OUT_CH2_INTR_SOURCE            71  /* interrupt of general DMA OUT channel 2, LEVEL*/
#define GSPI2_INTR_SOURCE                  72
#define AES_INTR_SOURCE                    73  /* interrupt of AES accelerator, level*/
#define SHA_INTR_SOURCE                    74  /* interrupt of SHA accelerator, level*/
#define RSA_INTR_SOURCE                    75  /* interrupt of RSA accelerator, level*/
#define ECC_INTR_SOURCE                    76  /* interrupt of ECC accelerator, level*/
#define MAX_INTR_SOURCE                    77

/* Zero will allocate low/medium levels of priority (ESP_INTR_FLAG_LOWMED) */
#define IRQ_DEFAULT_PRIORITY    0

#define ESP_INTR_FLAG_SHARED    (1<<8)  /* Interrupt can be shared between ISRs */

/* LP Core intmux */
#define LP_CORE_IO_INTR_SOURCE    0
#define LP_CORE_I2C_INTR_SOURCE   1
#define LP_CORE_UART_INTR_SOURCE  2
#define LP_CORE_TIMER_INTR_SOURCE 3
#define LP_CORE_PMU_INTR_SOURCE   5



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32C6_INTMUX_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 36 行

Wi-Fi 媒体访问控制（MAC）电平触发中断（Level Interrupt）。

### 注释 3：原第 37 行

Wi-Fi 媒体访问控制（MAC）不可屏蔽中断（NMI）。

### 注释 4：原第 39 行

Wi-Fi 基带（BB）电平触发中断（Level Interrupt）。

### 注释 5：原第 40 行

将被取消（Will Be Cancelled）。

### 注释 6：原第 41 行

蓝牙基带（BT BB）电平触发中断（Level Interrupt）。

### 注释 7：原第 42 行

蓝牙基带（BT BB）不可屏蔽中断（NMI）。

### 注释 8：原第 47 行

I2C 主机（Master）电平触发中断（Level Interrupt）。

### 注释 9：原第 50 行

电子熔丝（eFuse）电平触发中断，通常不太可能使用。

### 注释 10：原第 58 行

由 CPU 生成的中断 0，电平触发（Level）。

### 注释 11：原第 59 行

由 CPU 生成的中断 1，电平触发（Level）。

### 注释 12：原第 60 行

由 CPU 生成的中断 2，电平触发（Level）。

### 注释 13：原第 61 行

由 CPU 生成的中断 3，电平触发（Level）。

### 注释 14：原第 62 行

辅助调试模块（Assist Debug Module）的电平触发中断。

### 注释 15：原第 66 行

GPIO 电平触发中断（Level Interrupt）。

### 注释 16：原第 67 行

GPIO 不可屏蔽中断（NMI）。

### 注释 17：原第 77 行

I2S1 电平触发中断（Level Interrupt）。

### 注释 18：原第 78 行

UHCI0 电平触发中断（Level Interrupt）。

### 注释 19：原第 79 行

UART0 电平触发中断（Level Interrupt）。

### 注释 20：原第 80 行

UART1 电平触发中断（Level Interrupt）。

### 注释 21：原第 81 行

LED 脉宽调制（PWM）电平触发中断。

### 注释 22：原第 82 行

CAN0 电平触发中断（Level Interrupt）。

### 注释 23：原第 83 行

CAN1 电平触发中断（Level Interrupt）。

### 注释 24：原第 84 行

USB 电平触发中断（Level Interrupt）。

### 注释 25：原第 85 行

远程控制器（Remote Controller）电平触发中断。

### 注释 26：原第 86 行

I2C 控制器 1 的电平触发中断（Level Interrupt）。

### 注释 27：原第 87 行

定时器组 0（TIMER_GROUP0）中定时器 0（TIMER0）的电平触发中断。

### 注释 28：原第 88 行

定时器组 0（TIMER_GROUP0）中定时器 1（TIMER1）的电平触发中断。

### 注释 29：原第 89 行

定时器组 0（TIMER_GROUP0）中看门狗（Watchdog）的电平触发中断。

### 注释 30：原第 90 行

定时器组 1（TIMER_GROUP1）中定时器 0（TIMER0）的电平触发中断。

### 注释 31：原第 91 行

定时器组 1（TIMER_GROUP1）中定时器 1（TIMER1）的电平触发中断。

### 注释 32：原第 92 行

定时器组 1（TIMER_GROUP1）中看门狗（Watchdog）的电平触发中断。

### 注释 33：原第 93 行

系统定时器 0 的边沿触发中断（Edge Interrupt）。

### 注释 34：原第 94 行

系统定时器 1 的边沿触发中断（Edge Interrupt）。

### 注释 35：原第 95 行

系统定时器 2 的边沿触发中断（Edge Interrupt）。

### 注释 36：原第 96 行

APB 模数转换器（ADC）的电平触发中断。

### 注释 37：原第 97 行

电机控制脉宽调制模块 MCPWM0 的电平触发中断。

### 注释 38：原第 102 行

通用 DMA 输入通道 0（IN Channel 0）的电平触发中断。

### 注释 39：原第 103 行

通用 DMA 输入通道 1（IN Channel 1）的电平触发中断。

### 注释 40：原第 104 行

通用 DMA 输入通道 2（IN Channel 2）的电平触发中断。

### 注释 41：原第 105 行

通用 DMA 输出通道 0（OUT Channel 0）的电平触发中断。

### 注释 42：原第 106 行

通用 DMA 输出通道 1（OUT Channel 1）的电平触发中断。

### 注释 43：原第 107 行

通用 DMA 输出通道 2（OUT Channel 2）的电平触发中断。

### 注释 44：原第 109 行

AES 加速器（Accelerator）的电平触发中断。

### 注释 45：原第 110 行

SHA 加速器（Accelerator）的电平触发中断。

### 注释 46：原第 111 行

RSA 加速器（Accelerator）的电平触发中断。

### 注释 47：原第 112 行

ECC 加速器（Accelerator）的电平触发中断。

### 注释 48：原第 115 行

零值会分配低/中优先级（`ESP_INTR_FLAG_LOWMED`）。

### 注释 49：原第 118 行

中断可由多个中断服务程序（ISR）共享。

### 注释 50：原第 120 行

低功耗核（LP Core）的中断多路复用器（intmux）。

### 注释 51：原第 131 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_ESP32C6_INTMUX_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P082_zephyr__dt-bindings__interrupt-controller__esp-esp32c6-intmux.h_文件参考.md)

---

[上一章](P001_amebag2_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_gic.h_源码浏览.md)
