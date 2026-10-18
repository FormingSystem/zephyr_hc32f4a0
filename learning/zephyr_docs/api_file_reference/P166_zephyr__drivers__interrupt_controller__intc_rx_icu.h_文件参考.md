---
id: learning.zephyr-docs.api-file-reference.page-166
title: zephyr__drivers__interrupt_controller__intc_rx_icu.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第166章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_rx\_icu.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 166.1\_数据结构（Data Structures）

<a id="r_rx_5Firq_5Fdig_5Ffilt_5Fs"></a>

```c
struct rx_irq_dig_filt_s
```

相关声明：[rx_irq_dig_filt_s](../device_power_control_model_reference/P077_rx_irq_dig_filt_s_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 166.2\_宏定义（Macros）

<a id="r_a1f2e0aab110d6ad50ca923d97b7a5569"></a>

```c
#define IRQ_CFG_PCLK_DIV1 (0)
```

相关声明：[IRQ_CFG_PCLK_DIV1](#a1f2e0aab110d6ad50ca923d97b7a5569)。

<a id="r_a886edc20620e3b7e376df37e90b81c1a"></a>

```c
#define IRQ_CFG_PCLK_DIV8 (1)
```

相关声明：[IRQ_CFG_PCLK_DIV8](#a886edc20620e3b7e376df37e90b81c1a)。

<a id="r_adf9e7efaa66840f836a94ba6972b0dff"></a>

```c
#define IRQ_CFG_PCLK_DIV32 (2)
```

相关声明：[IRQ_CFG_PCLK_DIV32](#adf9e7efaa66840f836a94ba6972b0dff)。

<a id="r_a867e76951913679d9d1cd2ac5df79eda"></a>

```c
#define IRQ_CFG_PCLK_DIV64 (3)
```

相关声明：[IRQ_CFG_PCLK_DIV64](#a867e76951913679d9d1cd2ac5df79eda)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 166.3\_类型定义（Typedefs）

<a id="r_ae5e7618b4871363e4b9443cbe01ef86d"></a>

```c
typedef struct rx_irq_dig_filt_s rx_irq_dig_filt_t
```

相关声明：[rx_irq_dig_filt_s](../device_power_control_model_reference/P077_rx_irq_dig_filt_s_结构体.md)、[rx_irq_dig_filt_t](#ae5e7618b4871363e4b9443cbe01ef86d)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 166.4\_枚举（Enumerations）

<a id="r_aea25818bb1e7cf4bc3d1a6fce309207e"></a>

```c
enum icu_irq_mode { ICU_LOW_LEVEL , ICU_FALLING , ICU_RISING , ICU_BOTH_EDGE , ICU_MODE_NONE }
```

相关声明：[icu_irq_mode](#aea25818bb1e7cf4bc3d1a6fce309207e)、[ICU_LOW_LEVEL](#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4)、[ICU_FALLING](#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432)、[ICU_RISING](#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3)、[ICU_BOTH_EDGE](#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650)、[ICU_MODE_NONE](#aea25818bb1e7cf4bc3d1a6fce309207eaffba1ca9f0f29872c1381311465ac6e8)。

<a id="r_a4b89ff23dc526521af51a61f6d34431a"></a>

```c
enum icu_dig_filt { DISENABLE_DIG_FILT , ENABLE_DIG_FILT }
```

相关声明：[icu_dig_filt](#a4b89ff23dc526521af51a61f6d34431a)、[DISENABLE_DIG_FILT](#a4b89ff23dc526521af51a61f6d34431aad3a3540fce0ec8126751c4389993ba01)、[ENABLE_DIG_FILT](#a4b89ff23dc526521af51a61f6d34431aab7d4f4d93c7097db340059c2f786a81d)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 166.5\_函数（Functions）

<a id="r_a03cc2d22194251dd8942e2d95c3b3451"></a>

```c
void rx_icu_clear_ir_flag (unsigned int irqn)
```

相关声明：[rx_icu_clear_ir_flag](#a03cc2d22194251dd8942e2d95c3b3451)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a43836995901c04ab8c734f28c4e57e73"></a>

```c
int rx_icu_get_ir_flag (unsigned int irqn)
```

相关声明：[rx_icu_get_ir_flag](#a43836995901c04ab8c734f28c4e57e73)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a32aadebfbc450fa354d6d176289fec0d"></a>

```c
int rx_icu_set_irq_control (unsigned int pin_irqn, enum icu_irq_mode mode)
```

相关声明：[rx_icu_set_irq_control](#a32aadebfbc450fa354d6d176289fec0d)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[icu_irq_mode](#aea25818bb1e7cf4bc3d1a6fce309207e)。

<a id="r_ac9bdc620911c67f607cf9ec5a49fd1b1"></a>

```c
void rx_icu_set_irq_dig_filt (unsigned int pin_irqn, rx_irq_dig_filt_t dig_filt)
```

相关声明：[rx_icu_set_irq_dig_filt](#ac9bdc620911c67f607cf9ec5a49fd1b1)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[rx_irq_dig_filt_t](#ae5e7618b4871363e4b9443cbe01ef86d)。

## 166.6\_详细说明（Detailed Documentation）

<a id="a1f2e0aab110d6ad50ca923d97b7a5569"></a>

### `IRQ_CFG_PCLK_DIV1`

```c
#define IRQ_CFG_PCLK_DIV1 (0)
```

<a id="adf9e7efaa66840f836a94ba6972b0dff"></a>

### `IRQ_CFG_PCLK_DIV32`

```c
#define IRQ_CFG_PCLK_DIV32 (2)
```

<a id="a867e76951913679d9d1cd2ac5df79eda"></a>

### `IRQ_CFG_PCLK_DIV64`

```c
#define IRQ_CFG_PCLK_DIV64 (3)
```

<a id="a886edc20620e3b7e376df37e90b81c1a"></a>

### `IRQ_CFG_PCLK_DIV8`

```c
#define IRQ_CFG_PCLK_DIV8 (1)
```

<a id="ae5e7618b4871363e4b9443cbe01ef86d"></a>

### `rx_irq_dig_filt_t`

```c
typedef struct rx_irq_dig_filt_s rx_irq_dig_filt_t
```

<a id="a4b89ff23dc526521af51a61f6d34431a"></a>

### `icu_dig_filt`

```c
enum icu_dig_filt
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DISENABLE_DIG_FILT` |  |
| `ENABLE_DIG_FILT` |  |

<a id="aea25818bb1e7cf4bc3d1a6fce309207e"></a>

### `icu_irq_mode`

```c
enum icu_irq_mode
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ICU_LOW_LEVEL` |  |
| `ICU_FALLING` |  |
| `ICU_RISING` |  |
| `ICU_BOTH_EDGE` |  |
| `ICU_MODE_NONE` |  |

<a id="a03cc2d22194251dd8942e2d95c3b3451"></a>

### `rx_icu_clear_ir_flag()`

```c
void rx_icu_clear_ir_flag ( unsigned int irqn)
```

声明属性：`extern`。

<a id="a43836995901c04ab8c734f28c4e57e73"></a>

### `rx_icu_get_ir_flag()`

```c
int rx_icu_get_ir_flag ( unsigned int irqn)
```

声明属性：`extern`。

<a id="a32aadebfbc450fa354d6d176289fec0d"></a>

### `rx_icu_set_irq_control()`

```c
int rx_icu_set_irq_control ( unsigned int pin_irqn, enum icu_irq_mode mode )
```

声明属性：`extern`。

<a id="ac9bdc620911c67f607cf9ec5a49fd1b1"></a>

### `rx_icu_set_irq_dig_filt()`

```c
void rx_icu_set_irq_dig_filt ( unsigned int pin_irqn, rx_irq_dig_filt_t dig_filt )
```

声明属性：`extern`。


## 166.7\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P039_intc_rx_icu.h_源码浏览.md)
- [rx_irq_dig_filt_s](../device_power_control_model_reference/P077_rx_irq_dig_filt_s_结构体.md)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a4b89ff23dc526521af51a61f6d34431aad3a3540fce0ec8126751c4389993ba01"></a>
<a id="a4b89ff23dc526521af51a61f6d34431aab7d4f4d93c7097db340059c2f786a81d"></a>
<a id="aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4"></a>
<a id="aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432"></a>
<a id="aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3"></a>
<a id="aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650"></a>
<a id="aea25818bb1e7cf4bc3d1a6fce309207eaffba1ca9f0f29872c1381311465ac6e8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P165_zephyr__drivers__interrupt_controller__intc_mchp_aic_g1.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P167_zephyr__drivers__interrupt_controller__intc_vim.h_文件参考.md)
