---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-7
title: zephyr__drivers__interrupt_controller__intc_wkpu_nxp_s32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_wkpu\_nxp\_s32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.1\_类型定义（Typedefs）

<a id="r_af465c77abcefe103e4d3de6c864513b9"></a>

```c
typedef void(* wkpu_nxp_s32_callback_t) (uint8_t pin, void *arg)
```

相关声明：[wkpu_nxp_s32_callback_t](#af465c77abcefe103e4d3de6c864513b9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

NXP S32 MCU 唤醒中断／事件控制器（Wake-up Interrupt/Event Controller）驱动。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.2\_枚举（Enumerations）

<a id="r_a7440f457f38303fdc829933f897ebbd6"></a>

```c
enum wkpu_nxp_s32_trigger { WKPU_NXP_S32_RISING_EDGE , WKPU_NXP_S32_FALLING_EDGE , WKPU_NXP_S32_BOTH_EDGES }
```

相关声明：[wkpu_nxp_s32_trigger](#a7440f457f38303fdc829933f897ebbd6)、[WKPU_NXP_S32_RISING_EDGE](#a7440f457f38303fdc829933f897ebbd6a1aa475b8f106d699419b85c226075207)、[WKPU_NXP_S32_FALLING_EDGE](#a7440f457f38303fdc829933f897ebbd6a8aa0f7310ec4a6a87d6e50366dbf2ec3)、[WKPU_NXP_S32_BOTH_EDGES](#a7440f457f38303fdc829933f897ebbd6a24ed3d6d41e75d8f97acf883d91301de)。

NXP WKPU 引脚激活类型（Pin Activation Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_a3a62c3d569d106117713c307838bdbe5"></a>

```c
void wkpu_nxp_s32_unset_callback (const struct device *dev, uint8_t irq)
```

相关声明：[wkpu_nxp_s32_unset_callback](#a3a62c3d569d106117713c307838bdbe5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

取消线路（Line）的 WKPU 回调设置。

<a id="r_a64c7cee403cb060a5dfe4dc9ef9a9f2f"></a>

```c
int wkpu_nxp_s32_set_callback (const struct device *dev, uint8_t irq, uint8_t pin, wkpu_nxp_s32_callback_t cb, void *arg)
```

相关声明：[wkpu_nxp_s32_set_callback](#a64c7cee403cb060a5dfe4dc9ef9a9f2f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[wkpu_nxp_s32_callback_t](#af465c77abcefe103e4d3de6c864513b9)。

设置线路（Line）的 WKPU 回调。

<a id="r_a6717ad2b39f6dcd91ebb16271f8bd103"></a>

```c
void wkpu_nxp_s32_enable_interrupt (const struct device *dev, uint8_t irq, enum wkpu_nxp_s32_trigger trigger)
```

相关声明：[wkpu_nxp_s32_enable_interrupt](#a6717ad2b39f6dcd91ebb16271f8bd103)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[wkpu_nxp_s32_trigger](#a7440f457f38303fdc829933f897ebbd6)。

为 WKPU 线路（Line）设置边沿事件（Edge Event）并启用中断。

<a id="r_af79abeafd030150ec908a868ab2cad15"></a>

```c
void wkpu_nxp_s32_disable_interrupt (const struct device *dev, uint8_t irq)
```

相关声明：[wkpu_nxp_s32_disable_interrupt](#af79abeafd030150ec908a868ab2cad15)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

禁用 WKPU 线路（Line）的中断。

<a id="r_ae9a4815602689b1543d83d45929735a7"></a>

```c
uint64_t wkpu_nxp_s32_get_pending (const struct device *dev)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[wkpu_nxp_s32_get_pending](#ae9a4815602689b1543d83d45929735a7)、[device](../device_reference/P002_设备对象结构.md)。

获取 WKPU 设备的待处理中断（Pending Interrupt）。

## 7.4\_详细说明（Detailed Documentation）

<a id="af465c77abcefe103e4d3de6c864513b9"></a>

### `wkpu_nxp_s32_callback_t`

```c
typedef void(* wkpu_nxp_s32_callback_t) (uint8_t pin, void *arg)
```

NXP S32 MCU 唤醒中断／事件控制器（Wake-up Interrupt/Event Controller）驱动。

NXP WKPU 回调（Callback）。

<a id="a7440f457f38303fdc829933f897ebbd6"></a>

### `wkpu_nxp_s32_trigger`

```c
enum wkpu_nxp_s32_trigger
```

NXP WKPU 引脚激活类型（Pin Activation Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WKPU_NXP_S32_RISING_EDGE` | 上升沿触发的中断（Rising-edge Interrupt）。 |
| `WKPU_NXP_S32_FALLING_EDGE` | 下降沿触发的中断（Falling-edge Interrupt）。 |
| `WKPU_NXP_S32_BOTH_EDGES` | 在任一边沿（Either Edge）触发的中断。 |

<a id="af79abeafd030150ec908a868ab2cad15"></a>

### `wkpu_nxp_s32_disable_interrupt()`

```c
void wkpu_nxp_s32_disable_interrupt ( const struct device * dev, uint8_t irq )
```

禁用 WKPU 线路（Line）的中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | WKPU 设备（Device）。 |
| `irq` | WKPU 中断编号（Interrupt Number）。 |

<a id="a6717ad2b39f6dcd91ebb16271f8bd103"></a>

### `wkpu_nxp_s32_enable_interrupt()`

```c
void wkpu_nxp_s32_enable_interrupt ( const struct device * dev, uint8_t irq, enum wkpu_nxp_s32_trigger trigger )
```

为 WKPU 线路（Line）设置边沿事件（Edge Event）并启用中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | WKPU 设备（Device）。 |
| `irq` | WKPU 中断编号（Interrupt Number）。 |
| `trigger` | 引脚激活触发条件（Pin Activation Trigger）。 |

<a id="ae9a4815602689b1543d83d45929735a7"></a>

### `wkpu_nxp_s32_get_pending()`

```c
uint64_t wkpu_nxp_s32_get_pending ( const struct device * dev)
```

获取 WKPU 设备的待处理中断（Pending Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | WKPU 设备（Device）。 |

**返回（Returns）**：**返回值（Returns）：**包含待处理中断（Pending Interrupts）的位掩码（Bitmask）。

<a id="a64c7cee403cb060a5dfe4dc9ef9a9f2f"></a>

### `wkpu_nxp_s32_set_callback()`

```c
int wkpu_nxp_s32_set_callback ( const struct device * dev, uint8_t irq, uint8_t pin, wkpu_nxp_s32_callback_t cb, void * arg )
```

设置线路（Line）的 WKPU 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | WKPU 设备（Device）。 |
| `irq` | WKPU 中断编号（Interrupt Number）。 |
| `pin` | GPIO 引脚（Pin）。 |
| `cb` | 回调（Callback）。 |
| `arg` | 回调数据（Callback Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时（On Success）。 |
| `-EBUSY` | 该线路（Line）已设置回调时。 |

<a id="a3a62c3d569d106117713c307838bdbe5"></a>

### `wkpu_nxp_s32_unset_callback()`

```c
void wkpu_nxp_s32_unset_callback ( const struct device * dev, uint8_t irq )
```

取消线路（Line）的 WKPU 回调设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | WKPU 设备（Device）。 |
| `irq` | WKPU 中断编号（Interrupt Number）。 |


## 7.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P404_intc_wkpu_nxp_s32.h_源码浏览.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device](../device_reference/P002_设备对象结构.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a7440f457f38303fdc829933f897ebbd6a1aa475b8f106d699419b85c226075207"></a>
<a id="a7440f457f38303fdc829933f897ebbd6a8aa0f7310ec4a6a87d6e50366dbf2ec3"></a>
<a id="a7440f457f38303fdc829933f897ebbd6a24ed3d6d41e75d8f97acf883d91301de"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_zephyr__drivers__interrupt_controller__intc_nxp_siul2_eirq.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__dt-bindings__sensor__lsm6dso.h_文件参考.md)
