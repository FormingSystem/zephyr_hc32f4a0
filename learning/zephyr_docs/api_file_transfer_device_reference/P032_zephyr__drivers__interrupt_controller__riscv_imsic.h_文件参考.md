---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-32
title: zephyr__drivers__interrupt_controller__riscv_imsic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_riscv\_imsic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
#include <zephyr/types.h>
#include <zephyr/arch/riscv/csr.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 32.1\_宏定义（Macros）

<a id="r_a45dda5296a757e2a53b151e7e774f4e0"></a>

```c
#define CSR_MTOPEI 0x35C
```

相关声明：[CSR_MTOPEI](#a45dda5296a757e2a53b151e7e774f4e0)。

<a id="r_ae83343d5bd53df62b4e24ae21bc07929"></a>

```c
#define CSR_MTOPI 0xFB0
```

相关声明：[CSR_MTOPI](#ae83343d5bd53df62b4e24ae21bc07929)。

<a id="r_aea2af8fa5091c82d20a0532cb20da163"></a>

```c
#define CSR_MISELECT 0x350
```

相关声明：[CSR_MISELECT](#aea2af8fa5091c82d20a0532cb20da163)。

<a id="r_a2dc841a73b18bed68505b02da9376a78"></a>

```c
#define CSR_MIREG 0x351
```

相关声明：[CSR_MIREG](#a2dc841a73b18bed68505b02da9376a78)。

<a id="r_ac23e80fb7b4ce42ac1388ee08a11a08d"></a>

```c
#define CSR_SETEIPNUM_M 0xFC0 /* Write EIID to set pending bit */
```

相关声明：[CSR_SETEIPNUM_M](#ac23e80fb7b4ce42ac1388ee08a11a08d)。

<a id="r_a199c04e23e06cbdf9d69efb59e9718ca"></a>

```c
#define CSR_CLREIPNUM_M 0xFC1 /* Write EIID to clear pending bit */
```

相关声明：[CSR_CLREIPNUM_M](#a199c04e23e06cbdf9d69efb59e9718ca)。

<a id="r_a33326425b717dca3ab01371e224e2495"></a>

```c
#define MTOPEI_EIID_MASK 0x7FF /* Bits [10:0]: External Interrupt ID (0-2047) */
```

相关声明：[MTOPEI_EIID_MASK](#a33326425b717dca3ab01371e224e2495)。

<a id="r_a767e4c80aca2ae62c4687034c24a4039"></a>

```c
#define MTOPEI_PRIO_SHIFT 16 /* Bits [23:16]: Priority level */
```

相关声明：[MTOPEI_PRIO_SHIFT](#a767e4c80aca2ae62c4687034c24a4039)。

<a id="r_ae4a110ab82d244d53d7a0b81e2156f1a"></a>

```c
#define MTOPEI_PRIO_MASK (0xFF << MTOPEI_PRIO_SHIFT)
```

相关声明：[MTOPEI_PRIO_MASK](#ae4a110ab82d244d53d7a0b81e2156f1a)、[MTOPEI_PRIO_SHIFT](#a767e4c80aca2ae62c4687034c24a4039)。

<a id="r_a3c70581e268f9b82114f355a5428a093"></a>

```c
#define ICSR_EIDELIVERY 0x70
```

相关声明：[ICSR_EIDELIVERY](#a3c70581e268f9b82114f355a5428a093)。

<a id="r_aca7de63b4caba5ce950e5d0f399848c4"></a>

```c
#define ICSR_EITHRESH 0x72
```

相关声明：[ICSR_EITHRESH](#aca7de63b4caba5ce950e5d0f399848c4)。

<a id="r_af7761dfefb1ee23d18e17fba25c6ce9b"></a>

```c
#define ICSR_EIP0 0x80
```

相关声明：[ICSR_EIP0](#af7761dfefb1ee23d18e17fba25c6ce9b)。

<a id="r_a549e07bef1982a8ecc71dfb6ea04a715"></a>

```c
#define ICSR_EIP1 0x81
```

相关声明：[ICSR_EIP1](#a549e07bef1982a8ecc71dfb6ea04a715)。

<a id="r_a5110aec5ea16be097f89ad99e4458ce4"></a>

```c
#define ICSR_EIP2 0x82
```

相关声明：[ICSR_EIP2](#a5110aec5ea16be097f89ad99e4458ce4)。

<a id="r_a2bb9bfc7cc427810620904aac24a01ae"></a>

```c
#define ICSR_EIP3 0x83
```

相关声明：[ICSR_EIP3](#a2bb9bfc7cc427810620904aac24a01ae)。

<a id="r_a5c40f88cc697520a05627f318c7dbd22"></a>

```c
#define ICSR_EIP4 0x84
```

相关声明：[ICSR_EIP4](#a5c40f88cc697520a05627f318c7dbd22)。

<a id="r_aceab7b088c7a07bd2fc805c67420b5e3"></a>

```c
#define ICSR_EIP5 0x85
```

相关声明：[ICSR_EIP5](#aceab7b088c7a07bd2fc805c67420b5e3)。

<a id="r_a7176dd658d200fb6c883167093ce83dd"></a>

```c
#define ICSR_EIP6 0x86
```

相关声明：[ICSR_EIP6](#a7176dd658d200fb6c883167093ce83dd)。

<a id="r_adc114716a4c64dd87a4550775e971051"></a>

```c
#define ICSR_EIP7 0x87
```

相关声明：[ICSR_EIP7](#adc114716a4c64dd87a4550775e971051)。

<a id="r_adbb09b02e59c5d73c4583200abd6771e"></a>

```c
#define ICSR_EIE0 0xC0
```

相关声明：[ICSR_EIE0](#adbb09b02e59c5d73c4583200abd6771e)。

<a id="r_a5de9dfea426957e058ae99d897d90b20"></a>

```c
#define ICSR_EIE1 0xC1
```

相关声明：[ICSR_EIE1](#a5de9dfea426957e058ae99d897d90b20)。

<a id="r_a13e1c190b3420039312e2ea7f184be11"></a>

```c
#define ICSR_EIE2 0xC2
```

相关声明：[ICSR_EIE2](#a13e1c190b3420039312e2ea7f184be11)。

<a id="r_adee490aeb4aaced6bea1c98d9742de54"></a>

```c
#define ICSR_EIE3 0xC3
```

相关声明：[ICSR_EIE3](#adee490aeb4aaced6bea1c98d9742de54)。

<a id="r_a55d1201c07cdd813e5e84f6ea8c42cb8"></a>

```c
#define ICSR_EIE4 0xC4
```

相关声明：[ICSR_EIE4](#a55d1201c07cdd813e5e84f6ea8c42cb8)。

<a id="r_a1d5c3a862a7e9d97c2d275020d6a5096"></a>

```c
#define ICSR_EIE5 0xC5
```

相关声明：[ICSR_EIE5](#a1d5c3a862a7e9d97c2d275020d6a5096)。

<a id="r_a175b75deda965e1fd4021848c66c7311"></a>

```c
#define ICSR_EIE6 0xC6
```

相关声明：[ICSR_EIE6](#a175b75deda965e1fd4021848c66c7311)。

<a id="r_a73cdd4ed779d0d590bc1afa0a7072621"></a>

```c
#define ICSR_EIE7 0xC7
```

相关声明：[ICSR_EIE7](#a73cdd4ed779d0d590bc1afa0a7072621)。

<a id="r_aea72b1ce11f8f0469afd3c9374b2f918"></a>

```c
#define EIDELIVERY_ENABLE BIT(0)
```

相关声明：[EIDELIVERY_ENABLE](#aea72b1ce11f8f0469afd3c9374b2f918)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab6cf351d95e5f834598df746a939ed77"></a>

```c
#define EIDELIVERY_MODE_MMSI (0U << 29) /* MMSI only: 00 = 0x00000000 */
```

相关声明：[EIDELIVERY_MODE_MMSI](#ab6cf351d95e5f834598df746a939ed77)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 32.2\_函数（Functions）

<a id="r_a7673e9f4387c4af457d5ca9dad8b0530"></a>

```c
uint32_t riscv_imsic_claim (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[riscv_imsic_claim](#a7673e9f4387c4af457d5ca9dad8b0530)。

<a id="r_a88ef50b869732abc82f05e09d607d4a3"></a>

```c
void riscv_imsic_enable_eiid (uint32_t eiid)
```

相关声明：[riscv_imsic_enable_eiid](#a88ef50b869732abc82f05e09d607d4a3)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用**当前 CPU** 的 IMSIC 中的外部中断 ID（EIID）。

<a id="r_a66a14691a7401d228fbf4a9b2fa1a632"></a>

```c
void riscv_imsic_disable_eiid (uint32_t eiid)
```

相关声明：[riscv_imsic_disable_eiid](#a66a14691a7401d228fbf4a9b2fa1a632)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用**当前 CPU** 的 IMSIC 中的外部中断 ID（EIID）。

<a id="r_a17f09878019d36a36f4b0c22b0998388"></a>

```c
int riscv_imsic_is_enabled (uint32_t eiid)
```

相关声明：[riscv_imsic_is_enabled](#a17f09878019d36a36f4b0c22b0998388)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查**当前 CPU** 的 IMSIC 中的外部中断 ID（EIID）是否已启用。

## 32.3\_详细说明（Detailed Documentation）

<a id="a199c04e23e06cbdf9d69efb59e9718ca"></a>

### `CSR_CLREIPNUM_M`

```c
#define CSR_CLREIPNUM_M 0xFC1 /* Write EIID to clear pending bit */
```

<a id="a2dc841a73b18bed68505b02da9376a78"></a>

### `CSR_MIREG`

```c
#define CSR_MIREG 0x351
```

<a id="aea2af8fa5091c82d20a0532cb20da163"></a>

### `CSR_MISELECT`

```c
#define CSR_MISELECT 0x350
```

<a id="a45dda5296a757e2a53b151e7e774f4e0"></a>

### `CSR_MTOPEI`

```c
#define CSR_MTOPEI 0x35C
```

<a id="ae83343d5bd53df62b4e24ae21bc07929"></a>

### `CSR_MTOPI`

```c
#define CSR_MTOPI 0xFB0
```

<a id="ac23e80fb7b4ce42ac1388ee08a11a08d"></a>

### `CSR_SETEIPNUM_M`

```c
#define CSR_SETEIPNUM_M 0xFC0 /* Write EIID to set pending bit */
```

<a id="aea72b1ce11f8f0469afd3c9374b2f918"></a>

### `EIDELIVERY_ENABLE`

```c
#define EIDELIVERY_ENABLE BIT(0)
```

<a id="ab6cf351d95e5f834598df746a939ed77"></a>

### `EIDELIVERY_MODE_MMSI`

```c
#define EIDELIVERY_MODE_MMSI (0U << 29) /* MMSI only: 00 = 0x00000000 */
```

<a id="a3c70581e268f9b82114f355a5428a093"></a>

### `ICSR_EIDELIVERY`

```c
#define ICSR_EIDELIVERY 0x70
```

<a id="adbb09b02e59c5d73c4583200abd6771e"></a>

### `ICSR_EIE0`

```c
#define ICSR_EIE0 0xC0
```

<a id="a5de9dfea426957e058ae99d897d90b20"></a>

### `ICSR_EIE1`

```c
#define ICSR_EIE1 0xC1
```

<a id="a13e1c190b3420039312e2ea7f184be11"></a>

### `ICSR_EIE2`

```c
#define ICSR_EIE2 0xC2
```

<a id="adee490aeb4aaced6bea1c98d9742de54"></a>

### `ICSR_EIE3`

```c
#define ICSR_EIE3 0xC3
```

<a id="a55d1201c07cdd813e5e84f6ea8c42cb8"></a>

### `ICSR_EIE4`

```c
#define ICSR_EIE4 0xC4
```

<a id="a1d5c3a862a7e9d97c2d275020d6a5096"></a>

### `ICSR_EIE5`

```c
#define ICSR_EIE5 0xC5
```

<a id="a175b75deda965e1fd4021848c66c7311"></a>

### `ICSR_EIE6`

```c
#define ICSR_EIE6 0xC6
```

<a id="a73cdd4ed779d0d590bc1afa0a7072621"></a>

### `ICSR_EIE7`

```c
#define ICSR_EIE7 0xC7
```

<a id="af7761dfefb1ee23d18e17fba25c6ce9b"></a>

### `ICSR_EIP0`

```c
#define ICSR_EIP0 0x80
```

<a id="a549e07bef1982a8ecc71dfb6ea04a715"></a>

### `ICSR_EIP1`

```c
#define ICSR_EIP1 0x81
```

<a id="a5110aec5ea16be097f89ad99e4458ce4"></a>

### `ICSR_EIP2`

```c
#define ICSR_EIP2 0x82
```

<a id="a2bb9bfc7cc427810620904aac24a01ae"></a>

### `ICSR_EIP3`

```c
#define ICSR_EIP3 0x83
```

<a id="a5c40f88cc697520a05627f318c7dbd22"></a>

### `ICSR_EIP4`

```c
#define ICSR_EIP4 0x84
```

<a id="aceab7b088c7a07bd2fc805c67420b5e3"></a>

### `ICSR_EIP5`

```c
#define ICSR_EIP5 0x85
```

<a id="a7176dd658d200fb6c883167093ce83dd"></a>

### `ICSR_EIP6`

```c
#define ICSR_EIP6 0x86
```

<a id="adc114716a4c64dd87a4550775e971051"></a>

### `ICSR_EIP7`

```c
#define ICSR_EIP7 0x87
```

<a id="aca7de63b4caba5ce950e5d0f399848c4"></a>

### `ICSR_EITHRESH`

```c
#define ICSR_EITHRESH 0x72
```

<a id="a33326425b717dca3ab01371e224e2495"></a>

### `MTOPEI_EIID_MASK`

```c
#define MTOPEI_EIID_MASK 0x7FF /* Bits [10:0]: External Interrupt ID (0-2047) */
```

<a id="ae4a110ab82d244d53d7a0b81e2156f1a"></a>

### `MTOPEI_PRIO_MASK`

```c
#define MTOPEI_PRIO_MASK (0xFF << MTOPEI_PRIO_SHIFT)
```

<a id="a767e4c80aca2ae62c4687034c24a4039"></a>

### `MTOPEI_PRIO_SHIFT`

```c
#define MTOPEI_PRIO_SHIFT 16 /* Bits [23:16]: Priority level */
```

<a id="a7673e9f4387c4af457d5ca9dad8b0530"></a>

### `riscv_imsic_claim()`

```c
uint32_t riscv_imsic_claim ( void )
```

<a id="a66a14691a7401d228fbf4a9b2fa1a632"></a>

### `riscv_imsic_disable_eiid()`

```c
void riscv_imsic_disable_eiid ( uint32_t eiid)
```

禁用**当前 CPU** 的 IMSIC 中的外部中断 ID（EIID）。

本函数使用 CSR 指令，操作执行本代码的 CPU。要禁用特定硬件线程（Hart）上的外部中断 ID（EIID），**必须从该 Hart 调用本函数**。

遵循 PLIC 的方式：API 层不验证参数。无效外部中断 ID（EIID）触发中断时，会在中断服务例程（ISR）中被检测到。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `eiid` | 要禁用的外部中断 ID（External Interrupt ID），范围 `0–2047`。 |

<a id="a88ef50b869732abc82f05e09d607d4a3"></a>

### `riscv_imsic_enable_eiid()`

```c
void riscv_imsic_enable_eiid ( uint32_t eiid)
```

启用**当前 CPU** 的 IMSIC 中的外部中断 ID（EIID）。

本函数使用 CSR 指令，操作执行本代码的 CPU。要启用特定硬件线程（Hart）上的外部中断 ID（EIID），**必须从该 Hart 调用本函数**，例如使用 `k_thread_cpu_mask_enable`。

遵循 PLIC 的方式：API 层不验证参数。无效外部中断 ID（EIID）触发中断时，会在中断服务例程（ISR）中被检测到。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `eiid` | 要启用的外部中断 ID（External Interrupt ID），范围 `0–2047`。 |

<a id="a17f09878019d36a36f4b0c22b0998388"></a>

### `riscv_imsic_is_enabled()`

```c
int riscv_imsic_is_enabled ( uint32_t eiid)
```

检查**当前 CPU** 的 IMSIC 中的外部中断 ID（EIID）是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `eiid` | 要检查的外部中断 ID（External Interrupt ID），范围 `0–2047`。 |

**返回（Returns）**：**返回值（Returns）：**已启用（Enabled）返回 `1`，已禁用（Disabled）返回 `0`。


## 32.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_transport_clock_reference/P023_riscv_imsic.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P031_zephyr__modem__pipelink.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__dt-bindings__sensor__rm3100.h_文件参考.md)
