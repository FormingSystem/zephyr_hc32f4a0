---
id: learning.zephyr-docs.api-source-pin-register-fields-reference.page-1
title: esp-xtensa-intmux.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp-xtensa-intmux_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_esp-xtensa-intmux.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp-xtensa-intmux_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P085_zephyr__dt-bindings__interrupt-controller__esp-xtensa-intmux.h_文件参考.md)。

## 1.1\_原始可见代码（Source Code）

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
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>

```c
/*
 * Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_XTENSA_INTMUX_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_XTENSA_INTMUX_H_



#define WIFI_MAC_INTR_SOURCE                0   /* WiFi MAC, level */
#define WIFI_MAC_NMI_SOURCE                 1   /* WiFi MAC, NMI, use if MAC needs fix in NMI */
#define WIFI_BB_INTR_SOURCE                 2   /* WiFi BB, level, we can do some calibration */
#define BT_MAC_INTR_SOURCE                  3   /* will be cancelled */
#define BT_BB_INTR_SOURCE                   4   /* BB, level */
#define BT_BB_NMI_SOURCE                    5   /* BT BB, NMI, use if BB have bug to fix in NMI */
#define RWBT_INTR_SOURCE                    6   /* RWBT, level */
#define RWBLE_INTR_SOURCE                   7   /* RWBLE, level */
#define RWBT_NMI_SOURCE                     8   /* RWBT, NMI, use if RWBT has bug to fix in NMI */
#define RWBLE_NMI_SOURCE                    9   /* RWBLE, NMI, use if RWBT has bug to fix in NMI */
#define SLC0_INTR_SOURCE                    10  /* SLC0, level */
#define SLC1_INTR_SOURCE                    11  /* SLC1, level */
#define UHCI0_INTR_SOURCE                   12  /* UHCI0, level */
#define UHCI1_INTR_SOURCE                   13  /* UHCI1, level */
#define TG0_T0_LEVEL_INTR_SOURCE            14  /* TIMER_GROUP0, TIMER0, level */
#define TG0_T1_LEVEL_INTR_SOURCE            15  /* TIMER_GROUP0, TIMER1, level */
#define TG0_WDT_LEVEL_INTR_SOURCE           16  /* TIMER_GROUP0, WATCHDOG, level */
#define TG0_LACT_LEVEL_INTR_SOURCE          17  /* TIMER_GROUP0, LACT, level */
#define TG1_T0_LEVEL_INTR_SOURCE            18  /* TIMER_GROUP1, TIMER0, level */
#define TG1_T1_LEVEL_INTR_SOURCE            19  /* TIMER_GROUP1, TIMER1, level */
#define TG1_WDT_LEVEL_INTR_SOURCE           20  /* TIMER_GROUP1, WATCHDOG, level */
#define TG1_LACT_LEVEL_INTR_SOURCE          21  /* TIMER_GROUP1, LACT, level */
#define GPIO_INTR_SOURCE                    22  /* interrupt of GPIO, level */
#define GPIO_NMI_SOURCE                     23  /* interrupt of GPIO, NMI */
#define FROM_CPU_INTR0_SOURCE               24  /* int0 from a CPU, level */
#define FROM_CPU_INTR1_SOURCE               25  /* int1 from a CPU, level */
#define FROM_CPU_INTR2_SOURCE               26  /* int2 from a CPU, level, for DPORT Access */
#define FROM_CPU_INTR3_SOURCE               27  /* int3 from a CPU, level, for DPORT Access */
#define SPI0_INTR_SOURCE                    28  /* SPI0, level, for $ Access, do not use this */
#define SPI1_INTR_SOURCE                    29  /* SPI1, level, flash r/w, do not use this */
#define SPI2_INTR_SOURCE                    30  /* SPI2, level */
#define SPI3_INTR_SOURCE                    31  /* SPI3, level */
#define I2S0_INTR_SOURCE                    32  /* I2S0, level */
#define I2S1_INTR_SOURCE                    33  /* I2S1, level */
#define UART0_INTR_SOURCE                   34  /* UART0, level */
#define UART1_INTR_SOURCE                   35  /* UART1, level */
#define UART2_INTR_SOURCE                   36  /* UART2, level */
#define SDIO_HOST_INTR_SOURCE               37  /* SD/SDIO/MMC HOST, level */
#define ETH_MAC_INTR_SOURCE                 38  /* ethernet mac, level */
#define PWM0_INTR_SOURCE                    39  /* PWM0, level, Reserved */
#define PWM1_INTR_SOURCE                    40  /* PWM1, level, Reserved */
#define PWM2_INTR_SOURCE                    41  /* PWM2, level */
#define PWM3_INTR_SOURCE                    42  /* PWM3, level */
#define LEDC_INTR_SOURCE                    43  /* LED PWM, level */
#define EFUSE_INTR_SOURCE                   44  /* efuse, level, not likely to use */
#define TWAI_INTR_SOURCE                    45  /* twai, level */
#define CAN_INTR_SOURCE                     TWAI_INTR_SOURCE
#define RTC_CORE_INTR_SOURCE                46  /* rtc core, level, include rtc watchdog */
#define RMT_INTR_SOURCE                     47  /* remote controller, level */
#define PCNT_INTR_SOURCE                    48  /* pulse count, level */
#define I2C_EXT0_INTR_SOURCE                49  /* I2C controller1, level */
#define I2C_EXT1_INTR_SOURCE                50  /* I2C controller0, level */
#define RSA_INTR_SOURCE                     51  /* RSA accelerator, level */
#define SPI1_DMA_INTR_SOURCE                52  /* SPI1 DMA, for flash r/w, do not use it */
#define SPI2_DMA_INTR_SOURCE                53  /* SPI2 DMA, level */
#define SPI3_DMA_INTR_SOURCE                54  /* interrupt of SPI3 DMA, level */
#define WDT_INTR_SOURCE                     55  /* will be cancelled */
#define TIMER1_INTR_SOURCE                  56  /* will be cancelled */
#define TIMER2_INTR_SOURCE                  57  /* will be cancelled */
#define TG0_T0_EDGE_INTR_SOURCE             58  /* TIMER_GROUP0, TIMER0, EDGE */
#define TG0_T1_EDGE_INTR_SOURCE             59  /* TIMER_GROUP0, TIMER1, EDGE */
#define TG0_WDT_EDGE_INTR_SOURCE            60  /* TIMER_GROUP0, WATCH DOG, EDGE */
#define TG0_LACT_EDGE_INTR_SOURCE           61  /* TIMER_GROUP0, LACT, EDGE */
#define TG1_T0_EDGE_INTR_SOURCE             62  /* TIMER_GROUP1, TIMER0, EDGE */
#define TG1_T1_EDGE_INTR_SOURCE             63  /* TIMER_GROUP1, TIMER1, EDGE */
#define TG1_WDT_EDGE_INTR_SOURCE            64  /* TIMER_GROUP1, WATCHDOG, EDGE */
#define TG1_LACT_EDGE_INTR_SOURCE           65  /* TIMER_GROUP0, LACT, EDGE */
#define MMU_IA_INTR_SOURCE                  66  /* MMU Invalid Access, LEVEL */
#define MPU_IA_INTR_SOURCE                  67  /* MPU Invalid Access, LEVEL */
#define CACHE_IA_INTR_SOURCE                68  /* Cache Invalid Access, LEVEL */
#define MAX_INTR_SOURCE                     69  /* total number of interrupt sources */

/* Zero will allocate low/medium levels of priority (ESP_INTR_FLAG_LOWMED) */
#define IRQ_DEFAULT_PRIORITY    0

#define ESP_INTR_FLAG_SHARED    (1<<8)  /* Interrupt can be shared between ISRs */



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_XTENSA_INTMUX_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 36 行

Wi-Fi 媒体访问控制（MAC）电平触发中断（Level Interrupt）。

### 注释 3：原第 37 行

Wi-Fi 媒体访问控制（MAC）的不可屏蔽中断（NMI）；需要在 NMI 中修复 MAC 问题时使用。

### 注释 4：原第 38 行

Wi-Fi 基带（BB）电平触发中断，可用于进行一些校准（Calibration）。

### 注释 5：原第 39 行

将被取消（Will Be Cancelled）。

### 注释 6：原第 40 行

基带（BB）电平触发中断（Level Interrupt）。

### 注释 7：原第 41 行

蓝牙基带（BT BB）不可屏蔽中断（NMI）；需要在 NMI 中修复基带缺陷时使用。

### 注释 8：原第 42 行

RWBT 电平触发中断（Level Interrupt）。

### 注释 9：原第 43 行

RWBLE 电平触发中断（Level Interrupt）。

### 注释 10：原第 44 行

RWBT 不可屏蔽中断（NMI）；需要在 NMI 中修复 RWBT 缺陷时使用。

### 注释 11：原第 45 行

RWBLE 不可屏蔽中断（NMI）；需要在 NMI 中修复 RWBT 缺陷时使用。

> 译注：原文此处写的是 `RWBT`，按原文保留。

### 注释 12：原第 46 行

SLC0 电平触发中断（Level Interrupt）。

### 注释 13：原第 47 行

SLC1 电平触发中断（Level Interrupt）。

### 注释 14：原第 48 行

UHCI0 电平触发中断（Level Interrupt）。

### 注释 15：原第 49 行

UHCI1 电平触发中断（Level Interrupt）。

### 注释 16：原第 50 行

定时器组 0（TIMER_GROUP0）中定时器 0（TIMER0）的电平触发中断。

### 注释 17：原第 51 行

定时器组 0（TIMER_GROUP0）中定时器 1（TIMER1）的电平触发中断。

### 注释 18：原第 52 行

定时器组 0（TIMER_GROUP0）中看门狗（WATCHDOG）的电平触发中断。

### 注释 19：原第 53 行

定时器组 0（TIMER_GROUP0）中 LACT 的电平触发中断。

### 注释 20：原第 54 行

定时器组 1（TIMER_GROUP1）中定时器 0（TIMER0）的电平触发中断。

### 注释 21：原第 55 行

定时器组 1（TIMER_GROUP1）中定时器 1（TIMER1）的电平触发中断。

### 注释 22：原第 56 行

定时器组 1（TIMER_GROUP1）中看门狗（Watchdog）的电平触发中断。

### 注释 23：原第 57 行

定时器组 1（TIMER_GROUP1）中 LACT 的电平触发中断。

### 注释 24：原第 58 行

GPIO 电平触发中断（Level Interrupt）。

### 注释 25：原第 59 行

GPIO 不可屏蔽中断（NMI）。

### 注释 26：原第 60 行

来自 CPU 的中断 0（int0），电平触发。

### 注释 27：原第 61 行

来自 CPU 的中断 1（int1），电平触发。

### 注释 28：原第 62 行

来自 CPU 的中断 2（int2），电平触发，用于 DPORT 访问。

### 注释 29：原第 63 行

来自 CPU 的中断 3（int3），电平触发，用于 DPORT 访问。

### 注释 30：原第 64 行

SPI0 电平触发中断，用于 `$ Access`，请勿使用此中断。

> 译注：原文使用 `$ Access`，此处保留该写法。

### 注释 31：原第 65 行

SPI1 电平触发中断，用于闪存读写（Flash Read/Write），请勿使用此中断。

### 注释 32：原第 66 行

SPI2 电平触发中断（Level Interrupt）。

### 注释 33：原第 67 行

SPI3 电平触发中断（Level Interrupt）。

### 注释 34：原第 68 行

I2S0 电平触发中断（Level Interrupt）。

### 注释 35：原第 69 行

I2S1 电平触发中断（Level Interrupt）。

### 注释 36：原第 70 行

UART0 电平触发中断（Level Interrupt）。

### 注释 37：原第 71 行

UART1 电平触发中断（Level Interrupt）。

### 注释 38：原第 72 行

UART2 电平触发中断（Level Interrupt）。

### 注释 39：原第 73 行

SD/SDIO/MMC 主机（Host）电平触发中断。

### 注释 40：原第 74 行

以太网媒体访问控制（Ethernet MAC）的电平触发中断。

### 注释 41：原第 75 行

PWM0 电平触发中断，保留（Reserved）。

### 注释 42：原第 76 行

PWM1 电平触发中断，保留（Reserved）。

### 注释 43：原第 77 行

PWM2 电平触发中断（Level Interrupt）。

### 注释 44：原第 78 行

PWM3 电平触发中断（Level Interrupt）。

### 注释 45：原第 79 行

LED 脉宽调制（PWM）电平触发中断。

### 注释 46：原第 80 行

电子熔丝（eFuse）电平触发中断，通常不太可能使用。

### 注释 47：原第 81 行

双线汽车接口（TWAI）的电平触发中断。

### 注释 48：原第 83 行

实时时钟内核（RTC Core）电平触发中断，包含 RTC 看门狗（Watchdog）。

### 注释 49：原第 84 行

远程控制器（Remote Controller）电平触发中断。

### 注释 50：原第 85 行

脉冲计数（Pulse Count）电平触发中断。

### 注释 51：原第 86 行

I2C 控制器 1 的电平触发中断（Level Interrupt）。

### 注释 52：原第 87 行

I2C 控制器 0 电平触发中断（Level Interrupt）。

### 注释 53：原第 88 行

RSA 加速器（Accelerator）的电平触发中断。

### 注释 54：原第 89 行

SPI1 DMA，用于闪存读写（Flash Read/Write），请勿使用。

### 注释 55：原第 90 行

SPI2 DMA 电平触发中断（Level Interrupt）。

### 注释 56：原第 91 行

SPI3 DMA 电平触发中断（Level Interrupt）。

### 注释 57：原第 92 行

将被取消（Will Be Cancelled）。

### 注释 58：原第 93 行

将被取消（Will Be Cancelled）。

### 注释 59：原第 94 行

将被取消（Will Be Cancelled）。

### 注释 60：原第 95 行

定时器组 0（TIMER_GROUP0）中定时器 0（TIMER0）的边沿触发中断。

### 注释 61：原第 96 行

定时器组 0（TIMER_GROUP0）中定时器 1（TIMER1）的边沿触发中断。

### 注释 62：原第 97 行

定时器组 0（TIMER_GROUP0）中看门狗（Watchdog）的边沿触发中断。

### 注释 63：原第 98 行

定时器组 0（TIMER_GROUP0）中 LACT 的边沿触发中断。

### 注释 64：原第 99 行

定时器组 1（TIMER_GROUP1）中定时器 0（TIMER0）的边沿触发中断。

### 注释 65：原第 100 行

定时器组 1（TIMER_GROUP1）中定时器 1（TIMER1）的边沿触发中断。

### 注释 66：原第 101 行

定时器组 1（TIMER_GROUP1）中看门狗（Watchdog）的边沿触发中断。

### 注释 67：原第 102 行

定时器组 0（TIMER_GROUP0）中 LACT 的边沿触发中断。

### 注释 68：原第 103 行

内存管理单元（MMU）无效访问的电平触发中断。

### 注释 69：原第 104 行

内存保护单元（MPU）无效访问的电平触发中断。

### 注释 70：原第 105 行

无效缓存访问（Cache Invalid Access）的电平触发中断。

### 注释 71：原第 106 行

中断源总数（Total Number of Interrupt Sources）。

### 注释 72：原第 108 行

零值会分配低/中优先级（`ESP_INTR_FLAG_LOWMED`）。

### 注释 73：原第 111 行

中断可由多个中断服务程序（ISR）共享。

### 注释 74：原第 117 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_ESP_XTENSA_INTMUX_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P085_zephyr__dt-bindings__interrupt-controller__esp-xtensa-intmux.h_文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_pinctrl-rza-common.h_源码浏览.md)
