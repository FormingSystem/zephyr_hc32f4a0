---
id: learning.zephyr-docs.api-source-http-wifi-reference.page-4
title: intc_esp32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_intc\_esp32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html)。

## 4.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00051"></a>
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
<a id="foldopen00081"></a>
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
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="aintc__esp32_8h_html_a04d0b19e3d87390cb7a25c3cdd339141"></a>
<a id="aintc__esp32_8h_html_a0eb3aaaa35ed6fb4c8b1732025683d81"></a>
<a id="aintc__esp32_8h_html_a0f0269bcfe40a5ff90586c6848cf71cd"></a>
<a id="aintc__esp32_8h_html_a3ac390e382c675364bca9e7cb5e3c322"></a>
<a id="aintc__esp32_8h_html_a63263dc3bf78c25b514f739e6381ee64"></a>
<a id="aintc__esp32_8h_html_a637aa0db4839d3e945e74c56e82218f2"></a>
<a id="aintc__esp32_8h_html_a703fcc25fcfd86afeb5097f527b1ebad"></a>
<a id="aintc__esp32_8h_html_a917f8af7f0c6af92dfbd1f7689c39cae"></a>
<a id="aintc__esp32_8h_html_aa1a0dcb6bf0156f102e4db31f5e200c3"></a>
<a id="aintc__esp32_8h_html_aa6eef593f8a838adec4d258346b087d0"></a>
<a id="aintc__esp32_8h_html_aab9a8a47e564d406fa9a36aa015a6831"></a>
<a id="aintc__esp32_8h_html_aafc6d38bb52a59bd024809efcb3b64f0"></a>
<a id="aintc__esp32_8h_html_ab011a236fc3c9318f38ae4cdb9a26105"></a>
<a id="aintc__esp32_8h_html_ac2f659fe4a54f1591e29ea4c1ce540e1"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructintr__handle__data__t_html"></a>
<a id="astructintr__handle__data__t_html_a54ce22a2f0818180fbe25d0e9edf2036"></a>
<a id="astructintr__handle__data__t_html_a86785e459328fac2f0758d588159bf3e"></a>
<a id="astructshared__vector__desc__t_html"></a>
<a id="astructshared__vector__desc__t_html_a36afb23eff0489280549ac96fea0ee41"></a>
<a id="astructshared__vector__desc__t_html_a4ab5f28adbb5115ca6a37a3ab6c5328e"></a>
<a id="astructshared__vector__desc__t_html_a9078649e1b33c0ad3ee624789fda95cb"></a>
<a id="astructshared__vector__desc__t_html_aa438daab7ce59980b664824142be8f84"></a>
<a id="astructshared__vector__desc__t_html_acb593daeddd30515742759a73fc7838f"></a>
<a id="astructshared__vector__desc__t_html_aee24289457fcde842c2b557bce5cd605"></a>
<a id="astructshared__vector__desc__t_html_af868d1b2bf579938907ef07f5b15d517"></a>
<a id="astructvector__desc__t_html"></a>
<a id="astructvector__desc__t_html_a08740a5225fef571398bbd91a42fc970"></a>
<a id="astructvector__desc__t_html_a4b3b6db584511e25407e187d4dbf6ac8"></a>
<a id="astructvector__desc__t_html_a74e81e89da2ca79df99911d0599e5f77"></a>
<a id="astructvector__desc__t_html_a853c50cd06725b9502fa14af262d76b9"></a>
<a id="astructvector__desc__t_html_a8adcec0946b8790de75af65a6ae03ccc"></a>
<a id="astructvector__desc__t_html_a9934f0a683b6f2145ce35a395a65b967"></a>

```c
/*
 * Copyright (c) 2021-2025 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_ESP32_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_ESP32_H_

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Interrupt allocation flags - These flags can be used to specify
 * which interrupt qualities the code calling esp_intr_alloc* needs.
 *
 */

/* Keep the LEVELx values as they are here; they match up with (1<<level) */
#define ESP_INTR_FLAG_LEVEL1            (1<<1)  /* Accept a Level 1 int vector, lowest priority */
#define ESP_INTR_FLAG_LEVEL2            (1<<2)  /* Accept a Level 2 int vector */
#define ESP_INTR_FLAG_LEVEL3            (1<<3)  /* Accept a Level 3 int vector */
#define ESP_INTR_FLAG_LEVEL4            (1<<4)  /* Accept a Level 4 int vector */
#define ESP_INTR_FLAG_LEVEL5            (1<<5)  /* Accept a Level 5 int vector */
#define ESP_INTR_FLAG_LEVEL6            (1<<6)  /* Accept a Level 6 int vector */
#define ESP_INTR_FLAG_NMI               (1<<7)  /* Accept a Level 7 int vector, highest priority */
#define ESP_INTR_FLAG_SHARED            (1<<8)  /* Interrupt can be shared between ISRs */
#define ESP_INTR_FLAG_EDGE              (1<<9)  /* Edge-triggered interrupt */
#define ESP_INTR_FLAG_IRAM              (1<<10) /* ISR can be called if cache is disabled */
#define ESP_INTR_FLAG_INTRDISABLED      (1<<11) /* Return with this interrupt disabled */

/* Low and medium prio interrupts. These can be handled in C. */
#define ESP_INTR_FLAG_LOWMED    (ESP_INTR_FLAG_LEVEL1|ESP_INTR_FLAG_LEVEL2|ESP_INTR_FLAG_LEVEL3)

/* High level interrupts. Need to be handled in assembly. */
#define ESP_INTR_FLAG_HIGH      (ESP_INTR_FLAG_LEVEL4|ESP_INTR_FLAG_LEVEL5|ESP_INTR_FLAG_LEVEL6| \
                                 ESP_INTR_FLAG_NMI)

/* Mask for all level flags */
#define ESP_INTR_FLAG_LEVELMASK (ESP_INTR_FLAG_LEVEL1|ESP_INTR_FLAG_LEVEL2|ESP_INTR_FLAG_LEVEL3| \
                                 ESP_INTR_FLAG_LEVEL4|ESP_INTR_FLAG_LEVEL5|ESP_INTR_FLAG_LEVEL6| \
                                 ESP_INTR_FLAG_NMI)

/*
 * Get the interrupt flags from the supplied priority.
 */
#define ESP_PRIO_TO_FLAGS(priority) \
        ((priority) > 0 ? ((1 << (priority)) & ESP_INTR_FLAG_LEVELMASK) : 0)

/*
 * Check interrupt flags from input and filter unallowed values.
 */
#define ESP_INT_FLAGS_CHECK(int_flags) ((int_flags) & ESP_INTR_FLAG_SHARED)

/*
 * The esp_intr_alloc* functions can allocate an int for all *_INTR_SOURCE int sources that
 * are routed through the interrupt mux. Apart from these sources, each core also has some internal
 * sources that do not pass through the interrupt mux. To allocate an interrupt for these sources,
 * pass these pseudo-sources to the functions.
 */
#define ETS_INTERNAL_TIMER0_INTR_SOURCE         -1 /* Xtensa timer 0 interrupt source */
#define ETS_INTERNAL_TIMER1_INTR_SOURCE         -2 /* Xtensa timer 1 interrupt source */
#define ETS_INTERNAL_TIMER2_INTR_SOURCE         -3 /* Xtensa timer 2 interrupt source */
#define ETS_INTERNAL_SW0_INTR_SOURCE            -4 /* Software int source 1 */
#define ETS_INTERNAL_SW1_INTR_SOURCE            -5 /* Software int source 2 */
#define ETS_INTERNAL_PROFILING_INTR_SOURCE      -6 /* Int source for profiling */

/* Function prototype for interrupt handler function */
typedef void (*intr_handler_t)(void *arg);

/* Interrupt handler associated data structure */
typedef struct intr_handle_data_t intr_handle_data_t;

/* Handle to an interrupt handler */
typedef intr_handle_data_t *intr_handle_t;

struct shared_vector_desc_t {
        int disabled: 1;
        int source: 16;
        volatile uint32_t *statusreg;
        uint32_t statusmask;
        intr_handler_t isr;
        void *arg;
        struct shared_vector_desc_t *next;
};

/* Pack using bitfields for better memory use */
struct vector_desc_t {
        int flags: 16; /* OR of VECDESC_FLAG_* defines */
        unsigned int cpu: 1;
        unsigned int intno: 5;
        int source: 16;                               /* Int mux flags, used when not shared */
        struct shared_vector_desc_t *shared_vec_info; /* used when VECDESC_FL_SHARED */
        struct vector_desc_t *next;
};

struct intr_handle_data_t {
        struct vector_desc_t *vector_desc;
        struct shared_vector_desc_t *shared_vector_desc;
};

int esp_intr_mark_shared(int intno, int cpu, bool is_in_iram);

int esp_intr_reserve(int intno, int cpu);

int esp_intr_alloc(int source,
                int flags,
                intr_handler_t handler,
                void *arg,
                intr_handle_t *ret_handle);


int esp_intr_alloc_intrstatus(int source,
                int flags,
                uint32_t intrstatusreg,
                uint32_t intrstatusmask,
                intr_handler_t handler,
                void *arg,
                intr_handle_t *ret_handle);


int esp_intr_free(intr_handle_t handle);


int esp_intr_get_cpu(intr_handle_t handle);

int esp_intr_get_intno(intr_handle_t handle);

int esp_intr_disable(intr_handle_t handle);

int esp_intr_enable(intr_handle_t handle);

int esp_intr_set_in_iram(intr_handle_t handle, bool is_in_iram);

void esp_intr_noniram_disable(void);

void esp_intr_noniram_enable(void);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_ESP32_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021-2025 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

中断分配标志（Interrupt Allocation Flags），调用 `esp_intr_alloc*` 的代码可使用这些标志指定所需的中断特性。

### 注释 3：原第 23 行

保持此处 `LEVELx` 值不变，它们与 `(1<<level)` 对应。

### 注释 4：原第 24 行

接受级别 1 中断向量（Interrupt Vector），优先级最低。

### 注释 5：原第 25 行

接受级别 2 中断向量（Interrupt Vector）。

### 注释 6：原第 26 行

接受级别 3 中断向量（Interrupt Vector）。

### 注释 7：原第 27 行

接受级别 4 中断向量（Interrupt Vector）。

### 注释 8：原第 28 行

接受级别 5 中断向量（Interrupt Vector）。

### 注释 9：原第 29 行

接受级别 6 中断向量（Interrupt Vector）。

### 注释 10：原第 30 行

接受级别 7 中断向量（Interrupt Vector），优先级最高。

### 注释 11：原第 31 行

中断可由多个中断服务程序（ISR）共享。

### 注释 12：原第 32 行

边沿触发中断（Edge-Triggered Interrupt）。

### 注释 13：原第 33 行

禁用缓存（Cache）时仍可调用中断服务程序（ISR）。

### 注释 14：原第 34 行

返回时保持该中断禁用。

### 注释 15：原第 36 行

低、中优先级中断（Low and Medium Priority Interrupts），可使用 C 语言处理。

### 注释 16：原第 39 行

高级别中断（High-level Interrupts），需要使用汇编语言处理。

### 注释 17：原第 43 行

所有中断级别标志的掩码（Mask）。

### 注释 18：原第 48 行

根据指定优先级获取中断标志（Interrupt Flags）。

### 注释 19：原第 54 行

检查输入中断标志并滤除不允许的值。

### 注释 20：原第 59 行

`esp_intr_alloc*` 可为经过中断多路复用器（Interrupt Mux）路由的所有 `*_INTR_SOURCE` 中断源分配中断。除此之外，每个内核还有一些不经过该多路复用器的内部中断源。若要为它们分配中断，应将这些伪中断源（Pseudo-sources）传给上述函数。

### 注释 21：原第 65 行

Xtensa 定时器 0 中断源（Interrupt Source）。

### 注释 22：原第 66 行

Xtensa 定时器 1 中断源（Interrupt Source）。

### 注释 23：原第 67 行

Xtensa 定时器 2 中断源（Interrupt Source）。

### 注释 24：原第 68 行

软件中断源 1（Software Interrupt Source 1）。

### 注释 25：原第 69 行

软件中断源 2（Software Interrupt Source 2）。

### 注释 26：原第 70 行

性能分析（Profiling）中断源。

### 注释 27：原第 72 行

中断处理函数（Interrupt Handler）的函数原型。

### 注释 28：原第 75 行

中断处理程序（Interrupt Handler）的关联数据结构。

### 注释 29：原第 78 行

中断处理程序句柄（Interrupt Handler Handle）。

### 注释 30：原第 91 行

使用位域（Bitfields）打包，以提高内存利用率。

### 注释 31：原第 93 行

各 `VECDESC_FLAG_*` 定义按位或（OR）后的组合。

### 注释 32：原第 96 行

非共享时使用的中断多路复用器标志（Interrupt Mux Flags）。

### 注释 33：原第 97 行

使用 `VECDESC_FL_SHARED` 时采用。

### 注释 34：原第 320 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_ESP32_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [intr_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a637aa0db4839d3e945e74c56e82218f2)
- [intr_handle_data_t](../platform_security_model_reference/P015_intr_handle_data_t_结构体.md)
- [intr_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#ab011a236fc3c9318f38ae4cdb9a26105)
- [shared_vector_desc_t](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md)
- [disabled](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#a36afb23eff0489280549ac96fea0ee41)
- [source](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#af868d1b2bf579938907ef07f5b15d517)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [statusreg](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#acb593daeddd30515742759a73fc7838f)
- [statusmask](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#a9078649e1b33c0ad3ee624789fda95cb)
- [isr](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#aa438daab7ce59980b664824142be8f84)
- [arg](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#a4ab5f28adbb5115ca6a37a3ab6c5328e)
- [next](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#aee24289457fcde842c2b557bce5cd605)
- [vector_desc_t](../platform_security_model_reference/P073_vector_desc_t_结构体.md)
- [flags](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a08740a5225fef571398bbd91a42fc970)
- [cpu](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a853c50cd06725b9502fa14af262d76b9)
- [intno](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a74e81e89da2ca79df99911d0599e5f77)
- [source](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a8adcec0946b8790de75af65a6ae03ccc)
- [shared_vec_info](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a9934f0a683b6f2145ce35a395a65b967)
- [next](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a4b3b6db584511e25407e187d4dbf6ac8)
- [vector_desc](../platform_security_model_reference/P015_intr_handle_data_t_结构体.md#a54ce22a2f0818180fbe25d0e9edf2036)
- [shared_vector_desc](../platform_security_model_reference/P015_intr_handle_data_t_结构体.md#a86785e459328fac2f0758d588159bf3e)
- [esp_intr_mark_shared](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#aafc6d38bb52a59bd024809efcb3b64f0)
- [esp_intr_reserve](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#aa6eef593f8a838adec4d258346b087d0)
- [esp_intr_alloc](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a3ac390e382c675364bca9e7cb5e3c322)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [esp_intr_alloc_intrstatus](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#aab9a8a47e564d406fa9a36aa015a6831)
- [esp_intr_free](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#ac2f659fe4a54f1591e29ea4c1ce540e1)
- [esp_intr_get_cpu](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a04d0b19e3d87390cb7a25c3cdd339141)
- [esp_intr_get_intno](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a0f0269bcfe40a5ff90586c6848cf71cd)
- [esp_intr_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#aa1a0dcb6bf0156f102e4db31f5e200c3)
- [esp_intr_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a703fcc25fcfd86afeb5097f527b1ebad)
- [esp_intr_set_in_iram](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a0eb3aaaa35ed6fb4c8b1732025683d81)
- [esp_intr_noniram_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a63263dc3bf78c25b514f739e6381ee64)
- [esp_intr_noniram_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a917f8af7f0c6af92dfbd1f7689c39cae)
- [intr_handle_data_t::vector_desc](../platform_security_model_reference/P015_intr_handle_data_t_结构体.md#a54ce22a2f0818180fbe25d0e9edf2036)
- [intr_handle_data_t::shared_vector_desc](../platform_security_model_reference/P015_intr_handle_data_t_结构体.md#a86785e459328fac2f0758d588159bf3e)
- [shared_vector_desc_t::disabled](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#a36afb23eff0489280549ac96fea0ee41)
- [shared_vector_desc_t::arg](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#a4ab5f28adbb5115ca6a37a3ab6c5328e)
- [shared_vector_desc_t::statusmask](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#a9078649e1b33c0ad3ee624789fda95cb)
- [shared_vector_desc_t::isr](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#aa438daab7ce59980b664824142be8f84)
- [shared_vector_desc_t::statusreg](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#acb593daeddd30515742759a73fc7838f)
- [shared_vector_desc_t::next](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#aee24289457fcde842c2b557bce5cd605)
- [shared_vector_desc_t::source](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md#af868d1b2bf579938907ef07f5b15d517)
- [vector_desc_t::flags](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a08740a5225fef571398bbd91a42fc970)
- [vector_desc_t::next](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a4b3b6db584511e25407e187d4dbf6ac8)
- [vector_desc_t::intno](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a74e81e89da2ca79df99911d0599e5f77)
- [vector_desc_t::cpu](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a853c50cd06725b9502fa14af262d76b9)
- [vector_desc_t::source](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a8adcec0946b8790de75af65a6ae03ccc)
- [vector_desc_t::shared_vec_info](../platform_security_model_reference/P073_vector_desc_t_结构体.md#a9934f0a683b6f2145ce35a395a65b967)

---

[上一章](P003_ifx_clock_source_cyt4dnxx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_inttypes.h_源码浏览.md)
