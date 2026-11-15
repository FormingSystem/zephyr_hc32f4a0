---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-6
title: zephyr__drivers__interrupt_controller__intc_nxp_siul2_eirq.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_nxp\_siul2\_eirq.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.1\_类型定义（Typedefs）

<a id="r_ad8e4a39add66c073c73c58a37f347e6f"></a>

```c
typedef void(* nxp_siul2_eirq_callback_t) (uint8_t pin, void *arg)
```

相关声明：[nxp_siul2_eirq_callback_t](#ad8e4a39add66c073c73c58a37f347e6f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

NXP SIUL2 外部中断／事件控制器（External Interrupt/Event Controller）驱动。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.2\_枚举（Enumerations）

<a id="r_ae8a16d2e88c75e823638169b467f7d29"></a>

```c
enum nxp_siul2_eirq_trigger { NXP_SIUl2_EIRQ_RISING_EDGE , NXP_SIUl2_EIRQ_FALLING_EDGE , NXP_SIUl2_EIRQ_BOTH_EDGES }
```

相关声明：[nxp_siul2_eirq_trigger](#ae8a16d2e88c75e823638169b467f7d29)、[NXP_SIUl2_EIRQ_RISING_EDGE](#ae8a16d2e88c75e823638169b467f7d29a3430a77e48f7a96ef93a59eab4ba8d1c)、[NXP_SIUl2_EIRQ_FALLING_EDGE](#ae8a16d2e88c75e823638169b467f7d29abab4d5ba43ada8f041951d47665fcdaf)、[NXP_SIUl2_EIRQ_BOTH_EDGES](#ae8a16d2e88c75e823638169b467f7d29abdd4797bd8ece4c9a09e159edc8d2205)。

NXP SIUL2 EIRQ 引脚激活类型（Pin Activation Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.3\_函数（Functions）

<a id="r_aedfa3141aa28e62852ebc8cb60f1f1ff"></a>

```c
void nxp_siul2_eirq_unset_callback (const struct device *dev, uint8_t irq)
```

相关声明：[nxp_siul2_eirq_unset_callback](#aedfa3141aa28e62852ebc8cb60f1f1ff)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

取消中断回调（Interrupt Callback）的设置。

<a id="r_aed12dd6e76bb74f716b7f4c868b3bf28"></a>

```c
int nxp_siul2_eirq_set_callback (const struct device *dev, uint8_t irq, uint8_t pin, nxp_siul2_eirq_callback_t cb, void *arg)
```

相关声明：[nxp_siul2_eirq_set_callback](#aed12dd6e76bb74f716b7f4c868b3bf28)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nxp_siul2_eirq_callback_t](#ad8e4a39add66c073c73c58a37f347e6f)。

为关联到指定引脚（Pin）的中断设置回调。

<a id="r_aedfc2594ff5bc5e324464cbeb9c5ee8d"></a>

```c
void nxp_siul2_eirq_enable_interrupt (const struct device *dev, uint8_t irq, enum nxp_siul2_eirq_trigger trigger)
```

相关声明：[nxp_siul2_eirq_enable_interrupt](#aedfc2594ff5bc5e324464cbeb9c5ee8d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nxp_siul2_eirq_trigger](#ae8a16d2e88c75e823638169b467f7d29)。

在给定触发事件（Trigger Event）上启用中断。

<a id="r_a6fbebceceeaaf6f46be6bba383b2dd6c"></a>

```c
void nxp_siul2_eirq_disable_interrupt (const struct device *dev, uint8_t irq)
```

相关声明：[nxp_siul2_eirq_disable_interrupt](#a6fbebceceeaaf6f46be6bba383b2dd6c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

禁用中断。

<a id="r_ab54c32d27a6250745a2360a5bccc962d"></a>

```c
uint32_t nxp_siul2_eirq_get_pending (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[nxp_siul2_eirq_get_pending](#ab54c32d27a6250745a2360a5bccc962d)、[device](../device_reference/P002_设备对象结构.md)。

获取待处理中断（Pending Interrupts）。

## 6.4\_详细说明（Detailed Documentation）

<a id="ad8e4a39add66c073c73c58a37f347e6f"></a>

### `nxp_siul2_eirq_callback_t`

```c
typedef void(* nxp_siul2_eirq_callback_t) (uint8_t pin, void *arg)
```

NXP SIUL2 外部中断／事件控制器（External Interrupt/Event Controller）驱动。

NXP SIUL2 EIRQ 回调（Callback）。

<a id="ae8a16d2e88c75e823638169b467f7d29"></a>

### `nxp_siul2_eirq_trigger`

```c
enum nxp_siul2_eirq_trigger
```

NXP SIUL2 EIRQ 引脚激活类型（Pin Activation Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NXP_SIUl2_EIRQ_RISING_EDGE` | 上升沿触发的中断（Rising-edge Interrupt）。 |
| `NXP_SIUl2_EIRQ_FALLING_EDGE` | 下降沿触发的中断（Falling-edge Interrupt）。 |
| `NXP_SIUl2_EIRQ_BOTH_EDGES` | 在任一边沿（Either Edge）触发的中断。 |

<a id="a6fbebceceeaaf6f46be6bba383b2dd6c"></a>

### `nxp_siul2_eirq_disable_interrupt()`

```c
void nxp_siul2_eirq_disable_interrupt ( const struct device * dev, uint8_t irq )
```

禁用中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SIUL2 EIRQ 设备（Device）。 |
| `irq` | 中断编号（Interrupt Number）。 |

<a id="aedfc2594ff5bc5e324464cbeb9c5ee8d"></a>

### `nxp_siul2_eirq_enable_interrupt()`

```c
void nxp_siul2_eirq_enable_interrupt ( const struct device * dev, uint8_t irq, enum nxp_siul2_eirq_trigger trigger )
```

在给定触发事件（Trigger Event）上启用中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SIUL2 EIRQ 设备（Device）。 |
| `irq` | 中断编号（Interrupt Number）。 |
| `trigger` | 触发事件（Trigger Event）。 |

<a id="ab54c32d27a6250745a2360a5bccc962d"></a>

### `nxp_siul2_eirq_get_pending()`

```c
uint32_t nxp_siul2_eirq_get_pending ( const struct device * dev)
```

获取待处理中断（Pending Interrupts）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SIUL2 EIRQ 设备（Device）。 |

**返回（Returns）**：**返回值（Returns）：**包含待处理中断（Pending Interrupts）的位掩码（Bitmask）。

<a id="aed12dd6e76bb74f716b7f4c868b3bf28"></a>

### `nxp_siul2_eirq_set_callback()`

```c
int nxp_siul2_eirq_set_callback ( const struct device * dev, uint8_t irq, uint8_t pin, nxp_siul2_eirq_callback_t cb, void * arg )
```

为关联到指定引脚（Pin）的中断设置回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SIUL2 EIRQ 设备（Device）。 |
| `irq` | 中断编号（Interrupt Number）。 |
| `pin` | 与中断关联的 GPIO 引脚（Pin）。 |
| `cb` | 要安装的回调（Callback）。 |
| `arg` | 要包含在回调中的用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EBUSY` | 该中断已设置回调（Callback）时。 |

<a id="aedfa3141aa28e62852ebc8cb60f1f1ff"></a>

### `nxp_siul2_eirq_unset_callback()`

```c
void nxp_siul2_eirq_unset_callback ( const struct device * dev, uint8_t irq )
```

取消中断回调（Interrupt Callback）的设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SIUL2 EIRQ 设备（Device）。 |
| `irq` | 中断编号（Interrupt Number）。 |


## 6.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P398_intc_nxp_siul2_eirq.h_源码浏览.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ae8a16d2e88c75e823638169b467f7d29a3430a77e48f7a96ef93a59eab4ba8d1c"></a>
<a id="ae8a16d2e88c75e823638169b467f7d29abab4d5ba43ada8f041951d47665fcdaf"></a>
<a id="ae8a16d2e88c75e823638169b467f7d29abdd4797bd8ece4c9a09e159edc8d2205"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_zephyr__dt-bindings__sensor__icm45686.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__interrupt_controller__intc_wkpu_nxp_s32.h_文件参考.md)
