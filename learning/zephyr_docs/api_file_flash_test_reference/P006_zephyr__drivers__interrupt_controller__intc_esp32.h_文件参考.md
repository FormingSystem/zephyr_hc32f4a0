---
id: learning.zephyr-docs.api-file-flash-test-reference.page-6
title: zephyr__drivers__interrupt_controller__intc_esp32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_esp32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <stdbool.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_shared_5Fvector_5Fdesc_5Ft"></a>

```c
struct shared_vector_desc_t
```

相关声明：[shared_vector_desc_t](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md)。

<a id="r_vector_5Fdesc_5Ft"></a>

```c
struct vector_desc_t
```

相关声明：[vector_desc_t](../platform_security_model_reference/P073_vector_desc_t_结构体.md)。

<a id="r_intr_5Fhandle_5Fdata_5Ft"></a>

```c
struct intr_handle_data_t
```

相关声明：[intr_handle_data_t](../platform_security_model_reference/P015_intr_handle_data_t_结构体.md)。

中断处理程序（Interrupt Handler）的关联数据结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ab1ef5952bffcb1811d4f831b98ecf42a"></a>

```c
#define ESP_INTR_FLAG_LEVEL1 (1<<1) /* Accept a Level 1 int vector, lowest priority */
```

相关声明：[ESP_INTR_FLAG_LEVEL1](#ab1ef5952bffcb1811d4f831b98ecf42a)。

<a id="r_a8e4478d65d49a4f17fb77599764239e2"></a>

```c
#define ESP_INTR_FLAG_LEVEL2 (1<<2) /* Accept a Level 2 int vector */
```

相关声明：[ESP_INTR_FLAG_LEVEL2](#a8e4478d65d49a4f17fb77599764239e2)。

<a id="r_a88ed1ea08351b07086a6e73a0487b0d8"></a>

```c
#define ESP_INTR_FLAG_LEVEL3 (1<<3) /* Accept a Level 3 int vector */
```

相关声明：[ESP_INTR_FLAG_LEVEL3](#a88ed1ea08351b07086a6e73a0487b0d8)。

<a id="r_abb43226aa7d32763f17ee6a56090b322"></a>

```c
#define ESP_INTR_FLAG_LEVEL4 (1<<4) /* Accept a Level 4 int vector */
```

相关声明：[ESP_INTR_FLAG_LEVEL4](#abb43226aa7d32763f17ee6a56090b322)。

<a id="r_a44a1013070e7d9a06e8f08ed3f2cbca9"></a>

```c
#define ESP_INTR_FLAG_LEVEL5 (1<<5) /* Accept a Level 5 int vector */
```

相关声明：[ESP_INTR_FLAG_LEVEL5](#a44a1013070e7d9a06e8f08ed3f2cbca9)。

<a id="r_a8defb5130273462e32ed399dece67024"></a>

```c
#define ESP_INTR_FLAG_LEVEL6 (1<<6) /* Accept a Level 6 int vector */
```

相关声明：[ESP_INTR_FLAG_LEVEL6](#a8defb5130273462e32ed399dece67024)。

<a id="r_a9e57c700cf362161d807657571280abe"></a>

```c
#define ESP_INTR_FLAG_NMI (1<<7) /* Accept a Level 7 int vector, highest priority */
```

相关声明：[ESP_INTR_FLAG_NMI](#a9e57c700cf362161d807657571280abe)。

<a id="r_afc7bfcea2e621d81336ea6dd23310363"></a>

```c
#define ESP_INTR_FLAG_SHARED (1<<8) /* Interrupt can be shared between ISRs */
```

相关声明：[ESP_INTR_FLAG_SHARED](#afc7bfcea2e621d81336ea6dd23310363)。

<a id="r_a0ab957dd5055fe20725624db223f9535"></a>

```c
#define ESP_INTR_FLAG_EDGE (1<<9) /* Edge-triggered interrupt */
```

相关声明：[ESP_INTR_FLAG_EDGE](#a0ab957dd5055fe20725624db223f9535)。

<a id="r_a3fb8d6fa8b5e33b3503e86917bc8367b"></a>

```c
#define ESP_INTR_FLAG_IRAM (1<<10) /* ISR can be called if cache is disabled */
```

相关声明：[ESP_INTR_FLAG_IRAM](#a3fb8d6fa8b5e33b3503e86917bc8367b)。

<a id="r_a76d024609ecd48dc17b586b91e779b88"></a>

```c
#define ESP_INTR_FLAG_INTRDISABLED (1<<11) /* Return with this interrupt disabled */
```

相关声明：[ESP_INTR_FLAG_INTRDISABLED](#a76d024609ecd48dc17b586b91e779b88)。

<a id="r_a9b0bc1a2b5cc22b499e041742ae1b17b"></a>

```c
#define ESP_INTR_FLAG_LOWMED (ESP_INTR_FLAG_LEVEL1|ESP_INTR_FLAG_LEVEL2|ESP_INTR_FLAG_LEVEL3)
```

相关声明：[ESP_INTR_FLAG_LOWMED](#a9b0bc1a2b5cc22b499e041742ae1b17b)、[ESP_INTR_FLAG_LEVEL1](#ab1ef5952bffcb1811d4f831b98ecf42a)、[ESP_INTR_FLAG_LEVEL2](#a8e4478d65d49a4f17fb77599764239e2)、[ESP_INTR_FLAG_LEVEL3](#a88ed1ea08351b07086a6e73a0487b0d8)。

<a id="r_a63b4eee1d70d2e9cb1dc0ecb41f40aa4"></a>

```c
#define ESP_INTR_FLAG_HIGH
```

相关声明：[ESP_INTR_FLAG_HIGH](#a63b4eee1d70d2e9cb1dc0ecb41f40aa4)。

<a id="r_a610949ce2bf8d7adae528f816acc5725"></a>

```c
#define ESP_INTR_FLAG_LEVELMASK
```

相关声明：[ESP_INTR_FLAG_LEVELMASK](#a610949ce2bf8d7adae528f816acc5725)。

<a id="r_a447e94d9632ed5c38f1ea36cbc283c4a"></a>

```c
#define ESP_PRIO_TO_FLAGS(priority)
```

相关声明：[ESP_PRIO_TO_FLAGS](#a447e94d9632ed5c38f1ea36cbc283c4a)。

<a id="r_a4dac251442759ec39f07862b435e3dc1"></a>

```c
#define ESP_INT_FLAGS_CHECK(int_flags)
```

相关声明：[ESP_INT_FLAGS_CHECK](#a4dac251442759ec39f07862b435e3dc1)。

<a id="r_a2ff354dc48600b4dcbce4569c5d15bc1"></a>

```c
#define ETS_INTERNAL_TIMER0_INTR_SOURCE -1 /* Xtensa timer 0 interrupt source */
```

相关声明：[ETS_INTERNAL_TIMER0_INTR_SOURCE](#a2ff354dc48600b4dcbce4569c5d15bc1)。

<a id="r_ad28849af2335d2c6d9e07949f8ea953d"></a>

```c
#define ETS_INTERNAL_TIMER1_INTR_SOURCE -2 /* Xtensa timer 1 interrupt source */
```

相关声明：[ETS_INTERNAL_TIMER1_INTR_SOURCE](#ad28849af2335d2c6d9e07949f8ea953d)。

<a id="r_ad94487ae3c0ae2b9e4bccad6ce26d761"></a>

```c
#define ETS_INTERNAL_TIMER2_INTR_SOURCE -3 /* Xtensa timer 2 interrupt source */
```

相关声明：[ETS_INTERNAL_TIMER2_INTR_SOURCE](#ad94487ae3c0ae2b9e4bccad6ce26d761)。

<a id="r_a7cd02abe5015f1be30d77e1be15bd448"></a>

```c
#define ETS_INTERNAL_SW0_INTR_SOURCE -4 /* Software int source 1 */
```

相关声明：[ETS_INTERNAL_SW0_INTR_SOURCE](#a7cd02abe5015f1be30d77e1be15bd448)。

<a id="r_aa81d606c0199b91aba7633270ca314e6"></a>

```c
#define ETS_INTERNAL_SW1_INTR_SOURCE -5 /* Software int source 2 */
```

相关声明：[ETS_INTERNAL_SW1_INTR_SOURCE](#aa81d606c0199b91aba7633270ca314e6)。

<a id="r_a6cac8d828d3ec24b9bb58fe0cb3d59fc"></a>

```c
#define ETS_INTERNAL_PROFILING_INTR_SOURCE -6 /* Int source for profiling */
```

相关声明：[ETS_INTERNAL_PROFILING_INTR_SOURCE](#a6cac8d828d3ec24b9bb58fe0cb3d59fc)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_a637aa0db4839d3e945e74c56e82218f2"></a>

```c
typedef void(* intr_handler_t) (void *arg)
```

相关声明：[intr_handler_t](#a637aa0db4839d3e945e74c56e82218f2)。

<a id="r_a3d8b814c26ba94933e16bc264bdbb7f8"></a>

```c
typedef struct intr_handle_data_t intr_handle_data_t
```

相关声明：[intr_handle_data_t](#a3d8b814c26ba94933e16bc264bdbb7f8)。

<a id="r_ab011a236fc3c9318f38ae4cdb9a26105"></a>

```c
typedef intr_handle_data_t * intr_handle_t
```

相关声明：[intr_handle_data_t](../platform_security_model_reference/P015_intr_handle_data_t_结构体.md)、[intr_handle_t](#ab011a236fc3c9318f38ae4cdb9a26105)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_aafc6d38bb52a59bd024809efcb3b64f0"></a>

```c
int esp_intr_mark_shared (int intno, int cpu, bool is_in_iram)
```

相关声明：[esp_intr_mark_shared](#aafc6d38bb52a59bd024809efcb3b64f0)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将中断标记为共享中断（Shared Interrupt）。

<a id="r_aa6eef593f8a838adec4d258346b087d0"></a>

```c
int esp_intr_reserve (int intno, int cpu)
```

相关声明：[esp_intr_reserve](#aa6eef593f8a838adec4d258346b087d0)。

预留一个中断，供本框架之外使用。

<a id="r_a3ac390e382c675364bca9e7cb5e3c322"></a>

```c
int esp_intr_alloc (int source, int flags, intr_handler_t handler, void *arg, intr_handle_t *ret_handle)
```

相关声明：[esp_intr_alloc](#a3ac390e382c675364bca9e7cb5e3c322)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[intr_handler_t](#a637aa0db4839d3e945e74c56e82218f2)、[intr_handle_t](#ab011a236fc3c9318f38ae4cdb9a26105)。

按给定参数分配中断（Allocate Interrupt）。

<a id="r_aab9a8a47e564d406fa9a36aa015a6831"></a>

```c
int esp_intr_alloc_intrstatus (int source, int flags, uint32_t intrstatusreg, uint32_t intrstatusmask, intr_handler_t handler, void *arg, intr_handle_t *ret_handle)
```

相关声明：[esp_intr_alloc_intrstatus](#aab9a8a47e564d406fa9a36aa015a6831)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[intr_handler_t](#a637aa0db4839d3e945e74c56e82218f2)、[intr_handle_t](#ab011a236fc3c9318f38ae4cdb9a26105)。

按给定参数分配中断（Allocate Interrupt）。

<a id="r_ac2f659fe4a54f1591e29ea4c1ce540e1"></a>

```c
int esp_intr_free (intr_handle_t handle)
```

相关声明：[esp_intr_free](#ac2f659fe4a54f1591e29ea4c1ce540e1)、[intr_handle_t](#ab011a236fc3c9318f38ae4cdb9a26105)。

禁用并释放中断（Disable and Free Interrupt）。

<a id="r_a04d0b19e3d87390cb7a25c3cdd339141"></a>

```c
int esp_intr_get_cpu (intr_handle_t handle)
```

相关声明：[esp_intr_get_cpu](#a04d0b19e3d87390cb7a25c3cdd339141)、[intr_handle_t](#ab011a236fc3c9318f38ae4cdb9a26105)。

获取中断所绑定的 CPU 编号。

<a id="r_a0f0269bcfe40a5ff90586c6848cf71cd"></a>

```c
int esp_intr_get_intno (intr_handle_t handle)
```

相关声明：[esp_intr_get_intno](#a0f0269bcfe40a5ff90586c6848cf71cd)、[intr_handle_t](#ab011a236fc3c9318f38ae4cdb9a26105)。

获取某个句柄对应的已分配中断（Allocated Interrupt）。

<a id="r_aa1a0dcb6bf0156f102e4db31f5e200c3"></a>

```c
int esp_intr_disable (intr_handle_t handle)
```

相关声明：[esp_intr_disable](#aa1a0dcb6bf0156f102e4db31f5e200c3)、[intr_handle_t](#ab011a236fc3c9318f38ae4cdb9a26105)。

禁用与句柄关联的中断（Interrupt）。

<a id="r_a703fcc25fcfd86afeb5097f527b1ebad"></a>

```c
int esp_intr_enable (intr_handle_t handle)
```

相关声明：[esp_intr_enable](#a703fcc25fcfd86afeb5097f527b1ebad)、[intr_handle_t](#ab011a236fc3c9318f38ae4cdb9a26105)。

启用与句柄关联的中断（Interrupt）。

<a id="r_a0eb3aaaa35ed6fb4c8b1732025683d81"></a>

```c
int esp_intr_set_in_iram (intr_handle_t handle, bool is_in_iram)
```

相关声明：[esp_intr_set_in_iram](#a0eb3aaaa35ed6fb4c8b1732025683d81)、[intr_handle_t](#ab011a236fc3c9318f38ae4cdb9a26105)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置处理程序的“位于 IRAM”状态（In IRAM Status）。

<a id="r_a63263dc3bf78c25b514f739e6381ee64"></a>

```c
void esp_intr_noniram_disable (void)
```

相关声明：[esp_intr_noniram_disable](#a63263dc3bf78c25b514f739e6381ee64)。

禁用未被明确标记为从 IRAM 运行的中断。

<a id="r_a917f8af7f0c6af92dfbd1f7689c39cae"></a>

```c
void esp_intr_noniram_enable (void)
```

相关声明：[esp_intr_noniram_enable](#a917f8af7f0c6af92dfbd1f7689c39cae)。

重新启用被 esp_intr_noniram_disable 禁用的中断。

## 6.5\_详细说明（Detailed Documentation）

<a id="a4dac251442759ec39f07862b435e3dc1"></a>

### `ESP_INT_FLAGS_CHECK`

```c
#define ESP_INT_FLAGS_CHECK ( int_flags)
```

展开值（Value）：

```c
((int_flags) & ESP_INTR_FLAG_SHARED)
```

<a id="a0ab957dd5055fe20725624db223f9535"></a>

### `ESP_INTR_FLAG_EDGE`

```c
#define ESP_INTR_FLAG_EDGE (1<<9) /* Edge-triggered interrupt */
```

<a id="a63b4eee1d70d2e9cb1dc0ecb41f40aa4"></a>

### `ESP_INTR_FLAG_HIGH`

```c
#define ESP_INTR_FLAG_HIGH
```

展开值（Value）：

```c
(ESP_INTR_FLAG_LEVEL4|ESP_INTR_FLAG_LEVEL5|ESP_INTR_FLAG_LEVEL6| \
ESP_INTR_FLAG_NMI)
```

<a id="a76d024609ecd48dc17b586b91e779b88"></a>

### `ESP_INTR_FLAG_INTRDISABLED`

```c
#define ESP_INTR_FLAG_INTRDISABLED (1<<11) /* Return with this interrupt disabled */
```

<a id="a3fb8d6fa8b5e33b3503e86917bc8367b"></a>

### `ESP_INTR_FLAG_IRAM`

```c
#define ESP_INTR_FLAG_IRAM (1<<10) /* ISR can be called if cache is disabled */
```

<a id="ab1ef5952bffcb1811d4f831b98ecf42a"></a>

### `ESP_INTR_FLAG_LEVEL1`

```c
#define ESP_INTR_FLAG_LEVEL1 (1<<1) /* Accept a Level 1 int vector, lowest priority */
```

<a id="a8e4478d65d49a4f17fb77599764239e2"></a>

### `ESP_INTR_FLAG_LEVEL2`

```c
#define ESP_INTR_FLAG_LEVEL2 (1<<2) /* Accept a Level 2 int vector */
```

<a id="a88ed1ea08351b07086a6e73a0487b0d8"></a>

### `ESP_INTR_FLAG_LEVEL3`

```c
#define ESP_INTR_FLAG_LEVEL3 (1<<3) /* Accept a Level 3 int vector */
```

<a id="abb43226aa7d32763f17ee6a56090b322"></a>

### `ESP_INTR_FLAG_LEVEL4`

```c
#define ESP_INTR_FLAG_LEVEL4 (1<<4) /* Accept a Level 4 int vector */
```

<a id="a44a1013070e7d9a06e8f08ed3f2cbca9"></a>

### `ESP_INTR_FLAG_LEVEL5`

```c
#define ESP_INTR_FLAG_LEVEL5 (1<<5) /* Accept a Level 5 int vector */
```

<a id="a8defb5130273462e32ed399dece67024"></a>

### `ESP_INTR_FLAG_LEVEL6`

```c
#define ESP_INTR_FLAG_LEVEL6 (1<<6) /* Accept a Level 6 int vector */
```

<a id="a610949ce2bf8d7adae528f816acc5725"></a>

### `ESP_INTR_FLAG_LEVELMASK`

```c
#define ESP_INTR_FLAG_LEVELMASK
```

展开值（Value）：

```c
(ESP_INTR_FLAG_LEVEL1|ESP_INTR_FLAG_LEVEL2|ESP_INTR_FLAG_LEVEL3| \
ESP_INTR_FLAG_LEVEL4|ESP_INTR_FLAG_LEVEL5|ESP_INTR_FLAG_LEVEL6| \
ESP_INTR_FLAG_NMI)
```

<a id="a9b0bc1a2b5cc22b499e041742ae1b17b"></a>

### `ESP_INTR_FLAG_LOWMED`

```c
#define ESP_INTR_FLAG_LOWMED (ESP_INTR_FLAG_LEVEL1|ESP_INTR_FLAG_LEVEL2|ESP_INTR_FLAG_LEVEL3)
```

<a id="a9e57c700cf362161d807657571280abe"></a>

### `ESP_INTR_FLAG_NMI`

```c
#define ESP_INTR_FLAG_NMI (1<<7) /* Accept a Level 7 int vector, highest priority */
```

<a id="afc7bfcea2e621d81336ea6dd23310363"></a>

### `ESP_INTR_FLAG_SHARED`

```c
#define ESP_INTR_FLAG_SHARED (1<<8) /* Interrupt can be shared between ISRs */
```

<a id="a447e94d9632ed5c38f1ea36cbc283c4a"></a>

### `ESP_PRIO_TO_FLAGS`

```c
#define ESP_PRIO_TO_FLAGS ( priority)
```

展开值（Value）：

```c
((priority) > 0 ? ((1 << (priority)) & ESP_INTR_FLAG_LEVELMASK) : 0)
```

<a id="a6cac8d828d3ec24b9bb58fe0cb3d59fc"></a>

### `ETS_INTERNAL_PROFILING_INTR_SOURCE`

```c
#define ETS_INTERNAL_PROFILING_INTR_SOURCE -6 /* Int source for profiling */
```

<a id="a7cd02abe5015f1be30d77e1be15bd448"></a>

### `ETS_INTERNAL_SW0_INTR_SOURCE`

```c
#define ETS_INTERNAL_SW0_INTR_SOURCE -4 /* Software int source 1 */
```

<a id="aa81d606c0199b91aba7633270ca314e6"></a>

### `ETS_INTERNAL_SW1_INTR_SOURCE`

```c
#define ETS_INTERNAL_SW1_INTR_SOURCE -5 /* Software int source 2 */
```

<a id="a2ff354dc48600b4dcbce4569c5d15bc1"></a>

### `ETS_INTERNAL_TIMER0_INTR_SOURCE`

```c
#define ETS_INTERNAL_TIMER0_INTR_SOURCE -1 /* Xtensa timer 0 interrupt source */
```

<a id="ad28849af2335d2c6d9e07949f8ea953d"></a>

### `ETS_INTERNAL_TIMER1_INTR_SOURCE`

```c
#define ETS_INTERNAL_TIMER1_INTR_SOURCE -2 /* Xtensa timer 1 interrupt source */
```

<a id="ad94487ae3c0ae2b9e4bccad6ce26d761"></a>

### `ETS_INTERNAL_TIMER2_INTR_SOURCE`

```c
#define ETS_INTERNAL_TIMER2_INTR_SOURCE -3 /* Xtensa timer 2 interrupt source */
```

<a id="a3d8b814c26ba94933e16bc264bdbb7f8"></a>

### `intr_handle_data_t`

```c
typedef struct intr_handle_data_t intr_handle_data_t
```

<a id="ab011a236fc3c9318f38ae4cdb9a26105"></a>

### `intr_handle_t`

```c
typedef intr_handle_data_t* intr_handle_t
```

<a id="a637aa0db4839d3e945e74c56e82218f2"></a>

### `intr_handler_t`

```c
typedef void(* intr_handler_t) (void *arg)
```

<a id="a3ac390e382c675364bca9e7cb5e3c322"></a>

### `esp_intr_alloc()`

```c
int esp_intr_alloc ( int source, int flags, intr_handler_t handler, void * arg, intr_handle_t * ret_handle )
```

按给定参数分配中断（Allocate Interrupt）。

查找满足 flags 参数所给限制的中断，将给定中断源（Interrupt Source）映射到它，并关联所给中断处理程序（Interrupt Handler）及其可选参数。需要时，也可以返回中断句柄（Handle）。

中断始终分配在运行此函数的处理器核（Core）上。

使用 ESP_INTR_FLAG_IRAM 标志但处理程序地址不在 IRAM 或 RTC_FAST_MEM 中时，返回 ESP_ERR_INVALID_ARG。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 中断源（Interrupt Source），为 esp-xtensa-intmux.h 中定义的 INTR_SOURCE 中断复用器源之一，或本头文件中定义的内部 ETS_INTERNAL_INTR_SOURCE 源之一。 |
| `flags` | 由 `ESP_INTR_FLAG_*` 定义按位或组合的掩码（ORred Mask），用于限制此例程可选择的中断。值为 0 时，默认分配第 1、2 或 3 级非共享中断；值为 ESP_INTR_FLAG_SHARED 时，分配第 1 级共享中断。设置 ESP_INTR_FLAG_INTRDISABLED 会使函数返回时中断保持禁用。 |
| `handler` | 中断处理程序（Interrupt Handler）。请求高于第 3 级的中断时必须为 NULL，因为这类中断不能通过 C 调用。 |
| `arg` | 传给中断处理程序（Interrupt Handler）的可选参数。 |
| `ret_handle` | 指向 intr_handle_t 指针的指针，用于存储句柄（Handle），以后可用该句柄查询详情或释放中断。不需要句柄时可以为 NULL。 |

返回（Returns）：参数组合无效时为 -EINVAL；找不到满足指定标志的空闲中断时为 -ENODEV；其他情况为 0。

<a id="aab9a8a47e564d406fa9a36aa015a6831"></a>

### `esp_intr_alloc_intrstatus()`

```c
int esp_intr_alloc_intrstatus ( int source, int flags, uint32_t intrstatusreg, uint32_t intrstatusmask, intr_handler_t handler, void * arg, intr_handle_t * ret_handle )
```

按给定参数分配中断（Allocate Interrupt）。

功能基本与 esp_intr_alloc 相同，但允许指定寄存器与掩码组合。对于共享中断（Shared Interrupt），只有读取指定寄存器并与掩码按位与后结果非零时，才调用处理程序。传入中断状态寄存器地址和适当掩码，可加快共享中断触发时的处理：先检查中断状态，代码就能判断哪些中断服务例程（ISRs）可以跳过。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 中断源（Interrupt Source），为 esp-xtensa-intmux.h 中定义的 INTR_SOURCE 中断复用器源之一，或本头文件中定义的内部 ETS_INTERNAL_INTR_SOURCE 源之一。 |
| `flags` | 由 `ESP_INTR_FLAG_*` 定义按位或组合的掩码（ORred Mask），用于限制此例程可选择的中断。值为 0 时，默认分配第 1、2 或 3 级非共享中断；值为 ESP_INTR_FLAG_SHARED 时，分配第 1 级共享中断。设置 ESP_INTR_FLAG_INTRDISABLED 会使函数返回时中断保持禁用。 |
| `intrstatusreg` | 中断状态寄存器（Interrupt Status Register）的地址。 |
| `intrstatusmask` | 掩码（Mask）。如果读取 intrstatusreg 地址所得值在掩码为 1 的任意位上也为 1，则调用中断服务例程（ISR）；否则跳过。 |
| `handler` | 中断处理程序（Interrupt Handler）。请求高于第 3 级的中断时必须为 NULL，因为这类中断不能通过 C 调用。 |
| `arg` | 传给中断处理程序（Interrupt Handler）的可选参数。 |
| `ret_handle` | 指向 intr_handle_t 指针的指针，用于存储句柄（Handle），以后可用该句柄查询详情或释放中断。不需要句柄时可以为 NULL。 |

返回（Returns）：参数组合无效时为 -EINVAL；找不到满足指定标志的空闲中断时为 -ENODEV；其他情况为 0。

<a id="aa1a0dcb6bf0156f102e4db31f5e200c3"></a>

### `esp_intr_disable()`

```c
int esp_intr_disable ( intr_handle_t handle)
```

禁用与句柄关联的中断（Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 通过 esp_intr_alloc 或 esp_intr_alloc_intrstatus 获取的句柄（Handle）。 |

**说明（Note）**：注意（Note）：本地中断（`ESP_INTERNAL_*` 源）必须在分配该中断的 CPU 上调用此函数，其他中断没有此限制。多个处理程序共享同一中断源时，即将被禁用的处理程序负责处理中断状态位，应在禁用前屏蔽这些位，或由其他已启用的中断妥善处理。遗漏中断状态处理会导致无限次中断调用，最终使系统崩溃。

返回（Returns）：参数组合无效时为 -EINVAL，其他情况为 0。

<a id="a703fcc25fcfd86afeb5097f527b1ebad"></a>

### `esp_intr_enable()`

```c
int esp_intr_enable ( intr_handle_t handle)
```

启用与句柄关联的中断（Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 通过 esp_intr_alloc 或 esp_intr_alloc_intrstatus 获取的句柄（Handle）。 |

**说明（Note）**：注意（Note）：本地中断（`ESP_INTERNAL_*` 源）必须在分配该中断的 CPU 上调用此函数，其他中断没有此限制。

返回（Returns）：参数组合无效时为 -EINVAL，其他情况为 0。

<a id="ac2f659fe4a54f1591e29ea4c1ce540e1"></a>

### `esp_intr_free()`

```c
int esp_intr_free ( intr_handle_t handle)
```

禁用并释放中断（Disable and Free Interrupt）。

使用中断句柄（Interrupt Handle）禁用中断并释放其关联资源。如果当前处理器核不是注册此中断的核，此例程会被交由分配该中断的核执行，并阻塞等待资源成功释放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 通过 esp_intr_alloc 或 esp_intr_alloc_intrstatus 获取的句柄（Handle）。 |

**说明（Note）**：注意（Note）：处理程序与其他处理程序共享中断源时，必须先妥善处理其负责的中断状态位，再释放它。详情参见 esp_intr_disable。请勿在 esp_ipc_call_blocking 中调用此函数。

返回（Returns）：句柄为 NULL 时为 -EINVAL，其他情况为 0。

<a id="a04d0b19e3d87390cb7a25c3cdd339141"></a>

### `esp_intr_get_cpu()`

```c
int esp_intr_get_cpu ( intr_handle_t handle)
```

获取中断所绑定的 CPU 编号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 通过 esp_intr_alloc 或 esp_intr_alloc_intrstatus 获取的句柄（Handle）。 |

返回（Returns）：分配该中断的处理器核编号（Core Number）。

<a id="a0f0269bcfe40a5ff90586c6848cf71cd"></a>

### `esp_intr_get_intno()`

```c
int esp_intr_get_intno ( intr_handle_t handle)
```

获取某个句柄对应的已分配中断（Allocated Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 通过 esp_intr_alloc 或 esp_intr_alloc_intrstatus 获取的句柄（Handle）。 |

返回（Returns）：中断编号（Interrupt Number）。

<a id="aafc6d38bb52a59bd024809efcb3b64f0"></a>

### `esp_intr_mark_shared()`

```c
int esp_intr_mark_shared ( int intno, int cpu, bool is_in_iram )
```

将中断标记为共享中断（Shared Interrupt）。

将指定 CPU 上的某个中断标记为可用于挂接共享中断处理程序（Shared Interrupt Handlers）的中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `intno` | 中断编号（Interrupt Number），范围为 0–31。 |
| `cpu` | 要在其上将中断标记为共享的 CPU，取值为 0 或 1。 |
| `is_in_iram` | 共享中断（Shared Interrupt）供位于 IRAM 的处理程序使用；禁用闪存缓存（Flash Cache）时，此中断可以保持启用。 |

返回（Returns）：cpu 或 intno 无效时为 -EINVAL，其他情况为 0。

<a id="a63263dc3bf78c25b514f739e6381ee64"></a>

### `esp_intr_noniram_disable()`

```c
void esp_intr_noniram_disable ( void )
```

禁用未被明确标记为从 IRAM 运行的中断。

<a id="a917f8af7f0c6af92dfbd1f7689c39cae"></a>

### `esp_intr_noniram_enable()`

```c
void esp_intr_noniram_enable ( void )
```

重新启用被 esp_intr_noniram_disable 禁用的中断。

<a id="aa6eef593f8a838adec4d258346b087d0"></a>

### `esp_intr_reserve()`

```c
int esp_intr_reserve ( int intno, int cpu )
```

预留一个中断，供本框架之外使用。

将指定 CPU 上的某个中断标记为保留（Reserved），禁止因任何原因分配它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `intno` | 中断编号（Interrupt Number），范围为 0–31。 |
| `cpu` | 要在其上将中断标记为共享的 CPU，取值为 0 或 1。 |

返回（Returns）：cpu 或 intno 无效时为 -EINVAL，其他情况为 0。

<a id="a0eb3aaaa35ed6fb4c8b1732025683d81"></a>

### `esp_intr_set_in_iram()`

```c
int esp_intr_set_in_iram ( intr_handle_t handle, bool is_in_iram )
```

设置处理程序的“位于 IRAM”状态（In IRAM Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 通过 esp_intr_alloc 或 esp_intr_alloc_intrstatus 获取的句柄（Handle）。 |
| `is_in_iram` | 与此句柄关联的处理程序是否位于 IRAM。位于 IRAM 的处理程序可以在缓存（Cache）禁用时被调用。 |

**说明（Note）**：注意（Note）：不适用于共享中断（Shared Interrupts）。

返回（Returns）：参数组合无效时为 -EINVAL，其他情况为 0。


## 6.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_http_wifi_reference/P004_intc_esp32.h_源码浏览.md)
- [shared_vector_desc_t](../platform_security_model_reference/P055_shared_vector_desc_t_结构体.md)
- [vector_desc_t](../platform_security_model_reference/P073_vector_desc_t_结构体.md)
- [intr_handle_data_t](../platform_security_model_reference/P015_intr_handle_data_t_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [esp-xtensa-intmux.h](../api_file_reference/P085_zephyr__dt-bindings__interrupt-controller__esp-xtensa-intmux.h_文件参考.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aintc__esp32_8h_html_afc7bfcea2e621d81336ea6dd23310363"></a>
<a id="aintc__esp32_8h_html_a44a1013070e7d9a06e8f08ed3f2cbca9"></a>
<a id="aintc__esp32_8h_html_a8defb5130273462e32ed399dece67024"></a>
<a id="aintc__esp32_8h_html_a9e57c700cf362161d807657571280abe"></a>
<a id="aintc__esp32_8h_html_abb43226aa7d32763f17ee6a56090b322"></a>
<a id="aintc__esp32_8h_html_a88ed1ea08351b07086a6e73a0487b0d8"></a>
<a id="aintc__esp32_8h_html_a8e4478d65d49a4f17fb77599764239e2"></a>
<a id="aintc__esp32_8h_html_ab1ef5952bffcb1811d4f831b98ecf42a"></a>
<a id="aintc__esp32_8h_html_a610949ce2bf8d7adae528f816acc5725"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_zephyr__net__ieee802154_radio_openthread.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dt-bindings__clock__lpc84x-clock.h_文件参考.md)
