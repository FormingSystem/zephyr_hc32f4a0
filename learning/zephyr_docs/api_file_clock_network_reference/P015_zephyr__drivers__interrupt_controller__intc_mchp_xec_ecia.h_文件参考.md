---
id: learning.zephyr-docs.api-file-clock-network-reference.page-15
title: zephyr__drivers__interrupt_controller__intc_mchp_xec_ecia.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_mchp\_xec\_ecia.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__xec__ecia_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
#include <zephyr/irq.h>
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.1\_类型定义（Typedefs）

<a id="r_a946f876915453dd27eccc24d3e39210a"></a>

```c
typedef void(* mchp_xec_ecia_callback_t) (int girq_id, int src, void *user)
```

相关声明：[mchp_xec_ecia_callback_t](#a946f876915453dd27eccc24d3e39210a)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.2\_函数（Functions）

<a id="r_a91e7ab27d1b62f72a392ebbb5c38a4d8"></a>

```c
int mchp_xec_ecia_enable (int girq_id, int src)
```

相关声明：[mchp_xec_ecia_enable](#a91e7ab27d1b62f72a392ebbb5c38a4d8)。

Microchip XEC 设备的外部中断控制器驱动（External Interrupt Controller Driver）。

<a id="r_a9026ff2f7a60f8e244537cbab4a0e891"></a>

```c
int mchp_xec_ecia_info_enable (int ecia_info)
```

相关声明：[mchp_xec_ecia_info_enable](#a9026ff2f7a60f8e244537cbab4a0e891)。

启用由 MCHP_XEC_ECIA 宏编码参数指定线路的外部中断（EXTI）。

<a id="r_a6432ee01ae43598bc7ee8387f38ce5de"></a>

```c
int mchp_xec_ecia_disable (int girq_id, int src)
```

相关声明：[mchp_xec_ecia_disable](#a6432ee01ae43598bc7ee8387f38ce5de)。

禁用特定线路的外部中断（EXTI）。

<a id="r_a363949f5b133f05b94dd8f17d572bbac"></a>

```c
int mchp_xec_ecia_info_disable (int ecia_info)
```

相关声明：[mchp_xec_ecia_info_disable](#a363949f5b133f05b94dd8f17d572bbac)。

禁用由 MCHP_XEC_ECIA 宏编码参数指定线路的外部中断（EXTI）。

<a id="r_a980dfa5d5751cdefd5c911e6cac6075d"></a>

```c
int mchp_xec_ecia_set_callback (int girq_id, int src, mchp_xec_ecia_callback_t cb, void *data)
```

相关声明：[mchp_xec_ecia_set_callback](#a980dfa5d5751cdefd5c911e6cac6075d)、[mchp_xec_ecia_callback_t](#a946f876915453dd27eccc24d3e39210a)。

设置 GIRQn 中断源回调（Interrupt Source Callback）。

<a id="r_a1b75b3213eace2931bfee965bb2bc1b9"></a>

```c
int mchp_xec_ecia_info_set_callback (int ecia_info, mchp_xec_ecia_callback_t cb, void *data)
```

相关声明：[mchp_xec_ecia_info_set_callback](#a1b75b3213eace2931bfee965bb2bc1b9)、[mchp_xec_ecia_callback_t](#a946f876915453dd27eccc24d3e39210a)。

设置 GIRQn 中断源回调（Interrupt Source Callback）。

<a id="r_a65d91d241885c1b8ff7bdc7bd92e2a13"></a>

```c
int mchp_xec_ecia_set_callback_by_dev (const struct device *dev_girq, int src, mchp_xec_ecia_callback_t cb, void *data)
```

相关声明：[mchp_xec_ecia_set_callback_by_dev](#a65d91d241885c1b8ff7bdc7bd92e2a13)、[device](../device_reference/P002_设备对象结构.md)、[mchp_xec_ecia_callback_t](#a946f876915453dd27eccc24d3e39210a)。

设置 GIRQn 中断源回调（Interrupt Source Callback）。

<a id="r_a636a559083647193d154076c8d901bb5"></a>

```c
int mchp_ecia_unset_callback (int girq_id, int src)
```

相关声明：[mchp_ecia_unset_callback](#a636a559083647193d154076c8d901bb5)。

取消 GIRQn 中断源回调（Interrupt Source Callback）。

<a id="r_a756f04d2ad6680d4324326244f0b84b0"></a>

```c
int mchp_ecia_unset_callback_by_dev (const struct device *dev_girq, int src)
```

相关声明：[mchp_ecia_unset_callback_by_dev](#a756f04d2ad6680d4324326244f0b84b0)、[device](../device_reference/P002_设备对象结构.md)。

取消 GIRQn 中断源回调（Interrupt Source Callback）。

<a id="r_aa0acc2a2f6fe2c21e385aeb650d4e195"></a>

```c
void mchp_xec_ecia_girq_aggr_en (uint8_t girq_id, uint8_t enable)
```

相关声明：[mchp_xec_ecia_girq_aggr_en](#aa0acc2a2f6fe2c21e385aeb650d4e195)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用或禁用聚合 GIRQ 输出（Aggregated GIRQ Output）。

<a id="r_a042b0afeb07493d13b068b26bc20c4f3"></a>

```c
void mchp_xec_ecia_girq_src_clr (uint8_t girq_id, uint8_t src_bit)
```

相关声明：[mchp_xec_ecia_girq_src_clr](#a042b0afeb07493d13b068b26bc20c4f3)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

清除 GIRQ 锁存源状态位（Latched Source Status Bit）。

<a id="r_afce3bbeeb977efc4349d58e676c17fbe"></a>

```c
void mchp_xec_ecia_girq_src_en (uint8_t girq_id, uint8_t src_bit)
```

相关声明：[mchp_xec_ecia_girq_src_en](#afce3bbeeb977efc4349d58e676c17fbe)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用 GIRQ 中的一个中断源（Source）。

<a id="r_a4335e0f409723ffef63198b4ec026fe7"></a>

```c
void mchp_xec_ecia_girq_src_dis (uint8_t girq_id, uint8_t src_bit)
```

相关声明：[mchp_xec_ecia_girq_src_dis](#a4335e0f409723ffef63198b4ec026fe7)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

禁用 GIRQ 中的一个中断源（Source）。

<a id="r_a61c65d98a3781449fcb2363029fa0856"></a>

```c
void mchp_xec_ecia_girq_src_clr_bitmap (uint8_t girq_id, uint32_t bitmap)
```

相关声明：[mchp_xec_ecia_girq_src_clr_bitmap](#a61c65d98a3781449fcb2363029fa0856)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

清除位图（Bitmap）指定的 GIRQ 锁存源。

<a id="r_ab6d12794d0c1762efc2fdeb1a337580b"></a>

```c
void mchp_xec_ecia_girq_src_en_bitmap (uint8_t girq_id, uint32_t bitmap)
```

相关声明：[mchp_xec_ecia_girq_src_en_bitmap](#ab6d12794d0c1762efc2fdeb1a337580b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用 GIRQ 中的多个中断源（Sources）。

<a id="r_a44d6bffbe40f09fc063580f9bb936cd8"></a>

```c
void mchp_xec_ecia_girq_src_dis_bitmap (uint8_t girq_id, uint32_t bitmap)
```

相关声明：[mchp_xec_ecia_girq_src_dis_bitmap](#a44d6bffbe40f09fc063580f9bb936cd8)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用 GIRQ 中的多个中断源（Sources）。

<a id="r_a96a9db2c2a7e650c87457a1f5b1b395a"></a>

```c
uint32_t mchp_xec_ecia_girq_result (uint8_t girq_id)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mchp_xec_ecia_girq_result](#a96a9db2c2a7e650c87457a1f5b1b395a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 GIRQ 结果寄存器（Result Register），原文定义为使能与源的按位或（Bit-wise OR）。

<a id="r_ac563ac5fcc47e2b3b375ce4d3ade897b"></a>

```c
void mchp_xec_ecia_nvic_clr_pend (uint32_t nvic_num)
```

相关声明：[mchp_xec_ecia_nvic_clr_pend](#ac563ac5fcc47e2b3b375ce4d3ade897b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

清除外部嵌套向量中断控制器输入的挂起状态（NVIC Input Pending Status）。

<a id="r_a4dab0aa1c6f77906ecd618d4269cf764"></a>

```c
void mchp_xec_ecia_info_girq_aggr_en (int ecia_info, uint8_t enable)
```

相关声明：[mchp_xec_ecia_info_girq_aggr_en](#a4dab0aa1c6f77906ecd618d4269cf764)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用或禁用聚合 GIRQ 输出（Aggregated GIRQ Output）。

<a id="r_a73c19286d1f406aef34a4bda562d933b"></a>

```c
void mchp_xec_ecia_info_girq_src_clr (int ecia_info)
```

相关声明：[mchp_xec_ecia_info_girq_src_clr](#a73c19286d1f406aef34a4bda562d933b)。

清除 GIRQ 锁存源状态位（Latched Source Status Bit）。

<a id="r_a5a4b9d83a396438e22f1c694b7e7c82a"></a>

```c
void mchp_xec_ecia_info_girq_src_en (int ecia_info)
```

相关声明：[mchp_xec_ecia_info_girq_src_en](#a5a4b9d83a396438e22f1c694b7e7c82a)。

启用 GIRQ 中的一个中断源（Source）。

<a id="r_af90b2ce499b8109bae272d5bac444f51"></a>

```c
void mchp_xec_ecia_info_girq_src_dis (int ecia_info)
```

相关声明：[mchp_xec_ecia_info_girq_src_dis](#af90b2ce499b8109bae272d5bac444f51)。

禁用 GIRQ 中的一个中断源（Source）。

<a id="r_a38ce7498c75d5f8c44facc3a625edbe9"></a>

```c
uint32_t mchp_xec_ecia_info_girq_result (int ecia_info)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mchp_xec_ecia_info_girq_result](#a38ce7498c75d5f8c44facc3a625edbe9)。

读取 GIRQ 结果寄存器（Result Register），原文定义为使能与源的按位或（Bit-wise OR）。

<a id="r_a94b5aa34aaacb1e59ba2dffd625b200c"></a>

```c
void mchp_xec_ecia_info_nvic_clr_pend (int ecia_info)
```

相关声明：[mchp_xec_ecia_info_nvic_clr_pend](#a94b5aa34aaacb1e59ba2dffd625b200c)。

根据编码后的 ECIA 信息，清除外部 NVIC 输入挂起状态（Pending Status）。

## 15.3\_详细说明（Detailed Documentation）

<a id="a946f876915453dd27eccc24d3e39210a"></a>

### `mchp_xec_ecia_callback_t`

```c
typedef void(* mchp_xec_ecia_callback_t) (int girq_id, int src, void *user)
```

<a id="a636a559083647193d154076c8d901bb5"></a>

### `mchp_ecia_unset_callback()`

```c
int mchp_ecia_unset_callback ( int girq_id, int src )
```

取消 GIRQn 中断源回调（Interrupt Source Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `src` | GIRQ 中的中断源，范围为 0～31。 |

<a id="a756f04d2ad6680d4324326244f0b84b0"></a>

### `mchp_ecia_unset_callback_by_dev()`

```c
int mchp_ecia_unset_callback_by_dev ( const struct device * dev_girq, int src )
```

取消 GIRQn 中断源回调（Interrupt Source Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_girq` | GIRQn 设备的句柄（Handle）。 |
| `src` | GIRQ 中的中断源，范围为 0～31。 |

<a id="a6432ee01ae43598bc7ee8387f38ce5de"></a>

### `mchp_xec_ecia_disable()`

```c
int mchp_xec_ecia_disable ( int girq_id, int src )
```

禁用特定线路的外部中断（EXTI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `src` | GIRQ 中的中断源，范围为 0～31。 |

<a id="a91e7ab27d1b62f72a392ebbb5c38a4d8"></a>

### `mchp_xec_ecia_enable()`

```c
int mchp_xec_ecia_enable ( int girq_id, int src )
```

Microchip XEC 设备的外部中断控制器驱动（External Interrupt Controller Driver）。

依据参考手册（Reference Manuals）：MEC152x 与 MEC172x Arm 32 位微控制器参考手册。

章节：嵌入式控制器中断聚合器（EC Interrupt Aggregator，ECIA）。

启用 GIRQn 的指定中断源（Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `src` | GIRQ 中的中断源，范围为 0～31。 |

<a id="aa0acc2a2f6fe2c21e385aeb650d4e195"></a>

### `mchp_xec_ecia_girq_aggr_en()`

```c
void mchp_xec_ecia_girq_aggr_en ( uint8_t girq_id, uint8_t enable )
```

启用或禁用聚合 GIRQ 输出（Aggregated GIRQ Output）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `enable` | 非零值启用聚合输出（Aggregated Output），否则禁用。 |

<a id="a96a9db2c2a7e650c87457a1f5b1b395a"></a>

### `mchp_xec_ecia_girq_result()`

```c
uint32_t mchp_xec_ecia_girq_result ( uint8_t girq_id)
```

读取 GIRQ 结果寄存器（Result Register），原文定义为使能与源的按位或（Bit-wise OR）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |

**返回（Returns）**：返回值（Returns）：32 位无符号结果寄存器值（Result Register Value）。

<a id="a042b0afeb07493d13b068b26bc20c4f3"></a>

### `mchp_xec_ecia_girq_src_clr()`

```c
void mchp_xec_ecia_girq_src_clr ( uint8_t girq_id, uint8_t src_bit )
```

清除 GIRQ 锁存源状态位（Latched Source Status Bit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `src_bit` | 源在 GIRQ 寄存器中的位位置（Bit Position），范围为 0～31。 |

<a id="a61c65d98a3781449fcb2363029fa0856"></a>

### `mchp_xec_ecia_girq_src_clr_bitmap()`

```c
void mchp_xec_ecia_girq_src_clr_bitmap ( uint8_t girq_id, uint32_t bitmap )
```

清除位图（Bitmap）指定的 GIRQ 锁存源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `bitmap` | 包含要清除的源位（Source Bits）。 |

<a id="a4335e0f409723ffef63198b4ec026fe7"></a>

### `mchp_xec_ecia_girq_src_dis()`

```c
void mchp_xec_ecia_girq_src_dis ( uint8_t girq_id, uint8_t src_bit )
```

禁用 GIRQ 中的一个中断源（Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `src_bit` | 源在 GIRQ 寄存器中的位位置（Bit Position），范围为 0～31。 |

<a id="a44d6bffbe40f09fc063580f9bb936cd8"></a>

### `mchp_xec_ecia_girq_src_dis_bitmap()`

```c
void mchp_xec_ecia_girq_src_dis_bitmap ( uint8_t girq_id, uint32_t bitmap )
```

禁用 GIRQ 中的多个中断源（Sources）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `bitmap` | 包含要禁用的源位（Source Bits）。 |

<a id="afce3bbeeb977efc4349d58e676c17fbe"></a>

### `mchp_xec_ecia_girq_src_en()`

```c
void mchp_xec_ecia_girq_src_en ( uint8_t girq_id, uint8_t src_bit )
```

启用 GIRQ 中的一个中断源（Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `src_bit` | 源在 GIRQ 寄存器中的位位置（Bit Position），范围为 0～31。 |

<a id="ab6d12794d0c1762efc2fdeb1a337580b"></a>

### `mchp_xec_ecia_girq_src_en_bitmap()`

```c
void mchp_xec_ecia_girq_src_en_bitmap ( uint8_t girq_id, uint32_t bitmap )
```

启用 GIRQ 中的多个中断源（Sources）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `bitmap` | 包含要启用的源位（Source Bits）。 |

<a id="a363949f5b133f05b94dd8f17d572bbac"></a>

### `mchp_xec_ecia_info_disable()`

```c
int mchp_xec_ecia_info_disable ( int ecia_info)
```

禁用由 MCHP_XEC_ECIA 宏编码参数指定线路的外部中断（EXTI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ecia_info` | 使用 MCHP_XEC_ECIA 编码的 GIRQ 连接（Connection）。 |

<a id="a9026ff2f7a60f8e244537cbab4a0e891"></a>

### `mchp_xec_ecia_info_enable()`

```c
int mchp_xec_ecia_info_enable ( int ecia_info)
```

启用由 MCHP_XEC_ECIA 宏编码参数指定线路的外部中断（EXTI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ecia_info` | 使用 MCHP_XEC_ECIA 编码的 GIRQ 连接（Connection）。 |

<a id="a4dab0aa1c6f77906ecd618d4269cf764"></a>

### `mchp_xec_ecia_info_girq_aggr_en()`

```c
void mchp_xec_ecia_info_girq_aggr_en ( int ecia_info, uint8_t enable )
```

启用或禁用聚合 GIRQ 输出（Aggregated GIRQ Output）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ecia_info` | 使用 MCHP_XEC_ECIA 编码的 GIRQ 连接（Connection）。 |
| `enable` | 指示启用（1）或禁用（0）的标志（Flag）。 |

<a id="a38ce7498c75d5f8c44facc3a625edbe9"></a>

### `mchp_xec_ecia_info_girq_result()`

```c
uint32_t mchp_xec_ecia_info_girq_result ( int ecia_info)
```

读取 GIRQ 结果寄存器（Result Register），原文定义为使能与源的按位或（Bit-wise OR）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ecia_info` | 使用 MCHP_XEC_ECIA 编码的 GIRQ 连接（Connection）。 |

**返回（Returns）**：返回值（Returns）：32 位无符号结果寄存器值（Result Register Value）。

<a id="a73c19286d1f406aef34a4bda562d933b"></a>

### `mchp_xec_ecia_info_girq_src_clr()`

```c
void mchp_xec_ecia_info_girq_src_clr ( int ecia_info)
```

清除 GIRQ 锁存源状态位（Latched Source Status Bit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ecia_info` | 使用 MCHP_XEC_ECIA 编码的 GIRQ 连接（Connection）。 |

<a id="af90b2ce499b8109bae272d5bac444f51"></a>

### `mchp_xec_ecia_info_girq_src_dis()`

```c
void mchp_xec_ecia_info_girq_src_dis ( int ecia_info)
```

禁用 GIRQ 中的一个中断源（Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ecia_info` | 使用 MCHP_XEC_ECIA 编码的 GIRQ 连接（Connection）。 |

<a id="a5a4b9d83a396438e22f1c694b7e7c82a"></a>

### `mchp_xec_ecia_info_girq_src_en()`

```c
void mchp_xec_ecia_info_girq_src_en ( int ecia_info)
```

启用 GIRQ 中的一个中断源（Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ecia_info` | 使用 MCHP_XEC_ECIA 编码的 GIRQ 连接（Connection）。 |

<a id="a94b5aa34aaacb1e59ba2dffd625b200c"></a>

### `mchp_xec_ecia_info_nvic_clr_pend()`

```c
void mchp_xec_ecia_info_nvic_clr_pend ( int ecia_info)
```

根据编码后的 ECIA 信息，清除外部 NVIC 输入挂起状态（Pending Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ecia_info` | 使用 MCHP_XEC_ECIA 编码的 GIRQ 连接（Connection）。 |

<a id="a1b75b3213eace2931bfee965bb2bc1b9"></a>

### `mchp_xec_ecia_info_set_callback()`

```c
int mchp_xec_ecia_info_set_callback ( int ecia_info, mchp_xec_ecia_callback_t cb, void * data )
```

设置 GIRQn 中断源回调（Interrupt Source Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ecia_info` | 使用 MCHP_XEC_ECIA 编码的 GIRQ 连接（Connection）。 |
| `cb` | 用户回调（User Callback） |
| `data` | 用户数据（User Data）。 |

<a id="ac563ac5fcc47e2b3b375ce4d3ade897b"></a>

### `mchp_xec_ecia_nvic_clr_pend()`

```c
void mchp_xec_ecia_nvic_clr_pend ( uint32_t nvic_num)
```

清除外部嵌套向量中断控制器输入的挂起状态（NVIC Input Pending Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nvic_num` | 范围为 0 到该芯片的最大 NVIC 输入数量。 |

<a id="a980dfa5d5751cdefd5c911e6cac6075d"></a>

### `mchp_xec_ecia_set_callback()`

```c
int mchp_xec_ecia_set_callback ( int girq_id, int src, mchp_xec_ecia_callback_t cb, void * data )
```

设置 GIRQn 中断源回调（Interrupt Source Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `girq_id` | GIRQ 编号，范围为 8～26。 |
| `src` | GIRQ 中的中断源，范围为 0～31。 |
| `cb` | 用户回调（User Callback） |
| `data` | 用户数据（User Data）。 |

<a id="a65d91d241885c1b8ff7bdc7bd92e2a13"></a>

### `mchp_xec_ecia_set_callback_by_dev()`

```c
int mchp_xec_ecia_set_callback_by_dev ( const struct device * dev_girq, int src, mchp_xec_ecia_callback_t cb, void * data )
```

设置 GIRQn 中断源回调（Interrupt Source Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_girq` | GIRQn 设备的句柄（Handle）。 |
| `src` | GIRQ 中的中断源，范围为 0～31。 |
| `cb` | 用户回调（User Callback） |
| `data` | 用户数据（User Data）。 |


## 15.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/irq.h](../api_source_system_reference/P014_irq.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P034_intc_mchp_xec_ecia.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_zephyr__dt-bindings__sensor__ina237.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__bluetooth__l2cap.h_文件参考.md)
