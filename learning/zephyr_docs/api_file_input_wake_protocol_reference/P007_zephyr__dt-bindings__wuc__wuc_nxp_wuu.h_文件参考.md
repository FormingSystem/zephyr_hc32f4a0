---
id: learning.zephyr-docs.api-file-input-wake-protocol-reference.page-7
title: zephyr__dt-bindings__wuc__wuc_nxp_wuu.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__wuu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_dt-bindings\_\_wuc\_\_wuc\_nxp\_wuu.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__wuu_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP唤醒单元（Wakeup Unit，WUU）的唤醒源编码辅助接口。

查看此文件的源码。

<a id="details"></a>

NXP 唤醒单元（Wakeup Unit，WUU）的唤醒源编码辅助功能。定义将 WUU 唤醒源编码为单个 32 位值时使用的位域布局，并提供构造和解码此类值的辅助宏，供 NXP WUU 驱动及设备树 `wakeup-source` 属性使用。唤醒源编码如下：位 [31:24] 为源类型（Source Type），0 表示引脚（PIN），1 表示模块（MODULE）；位 [23:16] 为索引（Index），即引脚／模块编号；位 [15:8] 为边沿类型（Edge Type），1 表示上升沿（RISING），2 表示下降沿（FALLING），3 表示任意边沿（ANY），仅用于 PIN；位 [7:0] 为事件类型（Event Type），0 表示中断（INT），1 表示 DMA，2 表示触发输出（TRIGGER）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_a769e1ef3d9e96a6afad8ea17828cc050"></a>

```c
#define NXP_WUU_SOURCE_TYPE_POS 24
```

相关声明：[NXP_WUU_SOURCE_TYPE_POS](#a769e1ef3d9e96a6afad8ea17828cc050)。

编码唤醒源中源类型字段（Source-type Field）的位位置。

<a id="r_a81cb0ae5e3e2f756c1ffa512df55cc84"></a>

```c
#define NXP_WUU_SOURCE_INDEX_POS 16
```

相关声明：[NXP_WUU_SOURCE_INDEX_POS](#a81cb0ae5e3e2f756c1ffa512df55cc84)。

索引字段（Index Field）的位位置，即引脚或模块编号所在字段。

<a id="r_a73731f505cb4a94a4b34fd428734c70b"></a>

```c
#define NXP_WUU_SOURCE_EDGE_POS 8
```

相关声明：[NXP_WUU_SOURCE_EDGE_POS](#a73731f505cb4a94a4b34fd428734c70b)。

边沿类型字段（Edge-type Field）的位位置，仅用于 PIN 源。

<a id="r_a6eb529e0f845770faa06b88454ca09e5"></a>

```c
#define NXP_WUU_SOURCE_EVENT_POS 0
```

相关声明：[NXP_WUU_SOURCE_EVENT_POS](#a6eb529e0f845770faa06b88454ca09e5)。

事件类型字段（Event-type Field）的位位置。

<a id="r_a0507ef26fd272e9cbe32a610493c53ce"></a>

```c
#define NXP_WUU_SOURCE_MASK 0xFF
```

相关声明：[NXP_WUU_SOURCE_MASK](#a0507ef26fd272e9cbe32a610493c53ce)。

覆盖编码唤醒源中一个 8 位字段的掩码（Mask）。

<a id="r_a855b0d5f35a46702544758ed3a5b6f3f"></a>

```c
#define NXP_WUU_SOURCE_TYPE_PIN 0
```

相关声明：[NXP_WUU_SOURCE_TYPE_PIN](#a855b0d5f35a46702544758ed3a5b6f3f)。

源类型值（Source-type Value）：外部 WUU 引脚。

<a id="r_a890e5418a2e669f6244cd5004c68367a"></a>

```c
#define NXP_WUU_SOURCE_TYPE_MODULE 1
```

相关声明：[NXP_WUU_SOURCE_TYPE_MODULE](#a890e5418a2e669f6244cd5004c68367a)。

源类型值（Source-type Value）：内部外设模块。

<a id="r_a86b796473da951cea7729ccee32bc7fe"></a>

```c
#define NXP_WUU_EDGE_RISING 1
```

相关声明：[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)。

边沿类型值（Edge-type Value）：上升沿触发。

<a id="r_aebd1e16cc9fc9b95d4fcbfd01ff29bb7"></a>

```c
#define NXP_WUU_EDGE_FALLING 2
```

相关声明：[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)。

边沿类型值（Edge-type Value）：下降沿触发。

<a id="r_a6bb0fc2b85ec01be981e88851522a968"></a>

```c
#define NXP_WUU_EDGE_ANY 3
```

相关声明：[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)。

边沿类型值（Edge-type Value）：任意边沿触发。

<a id="r_af49b722882785c60e2b88997b1dac2b9"></a>

```c
#define NXP_WUU_EVENT_INT 0
```

相关声明：[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

事件类型值（Event-type Value）：以中断形式传递。

<a id="r_a07bbe18c99de81f08ae2ea3e99a6cb6a"></a>

```c
#define NXP_WUU_EVENT_DMA 1
```

相关声明：[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

事件类型值（Event-type Value）：以 DMA 请求形式传递。

<a id="r_a7a870a5d4b66572d17017ceae38214b4"></a>

```c
#define NXP_WUU_EVENT_TRIGGER 2
```

相关声明：[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

事件类型值（Event-type Value）：以触发输出形式传递。

<a id="r_ad39e976e86b11e57096e46d781f83c17"></a>

```c
#define NXP_WUU_WAKEUP_SOURCE_ENCODE(type, index, edge, event)
```

相关声明：[NXP_WUU_WAKEUP_SOURCE_ENCODE](#ad39e976e86b11e57096e46d781f83c17)。

将 WUU 唤醒源（Wakeup Source）编码为单个 32 位值。

<a id="r_ad7bc71c642cc4124e11c73a88dd6aa4f"></a>

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE(source, pos)
```

相关声明：[NXP_WUU_WAKEUP_SOURCE_DECODE](#ad7bc71c642cc4124e11c73a88dd6aa4f)。

从编码唤醒源（Encoded Wakeup Source）中提取一个 8 位字段。

<a id="r_af35ec75d34b9df3fe74f939376b4f99d"></a>

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE_TYPE(source)
```

相关声明：[NXP_WUU_WAKEUP_SOURCE_DECODE_TYPE](#af35ec75d34b9df3fe74f939376b4f99d)。

解码唤醒源的源类型字段（Source-type Field）。

<a id="r_ac8164cc2868fc8edea50395064a6757b"></a>

```c
#define NXP_WUU_IS_PIN_SOURCE(source)
```

相关声明：[NXP_WUU_IS_PIN_SOURCE](#ac8164cc2868fc8edea50395064a6757b)。

判断编码唤醒源是否描述引脚源（PIN Source）。

<a id="r_a332d40d6fbb7cab51791d74f34ed40da"></a>

```c
#define NXP_WUU_IS_MODULE_SOURCE(source)
```

相关声明：[NXP_WUU_IS_MODULE_SOURCE](#a332d40d6fbb7cab51791d74f34ed40da)。

判断编码唤醒源是否描述模块源（MODULE Source）。

<a id="r_abfe9ad605f2bcc78b96358cf092c7274"></a>

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE_INDEX(source)
```

相关声明：[NXP_WUU_WAKEUP_SOURCE_DECODE_INDEX](#abfe9ad605f2bcc78b96358cf092c7274)。

解码索引字段（Index Field），即引脚或模块编号。

<a id="r_a4c6d253dd543e140f48eb1bca57a84af"></a>

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE_EDGE(source)
```

相关声明：[NXP_WUU_WAKEUP_SOURCE_DECODE_EDGE](#a4c6d253dd543e140f48eb1bca57a84af)。

解码边沿类型字段（Edge-type Field），仅对 PIN 源有意义。

<a id="r_acc2c876066de244451ac99027f686e7a"></a>

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE_EVENT(source)
```

相关声明：[NXP_WUU_WAKEUP_SOURCE_DECODE_EVENT](#acc2c876066de244451ac99027f686e7a)。

解码唤醒源的事件类型字段（Event-type Field）。

<a id="r_a454f7e196452951dcbc613d9f556c0df"></a>

```c
#define NXP_WUU_PIN(index, edge, event)
```

相关声明：[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)。

引脚唤醒源（PIN Wakeup Sources）的辅助宏。

<a id="r_afaff4a945c102da5d4abf0e04b13e6db"></a>

```c
#define NXP_WUU_MODULE(index, event)
```

相关声明：[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)。

模块唤醒源（MODULE Wakeup Sources）的辅助宏。

<a id="r_aeb2b5d1be20f3d7039542df5aa7efb81"></a>

```c
#define NXP_WUU_MODULE_0_INT NXP_WUU_MODULE(0, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_MODULE_0_INT](#aeb2b5d1be20f3d7039542df5aa7efb81)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

WUU 支持的内部模块（Internal Modules）。

<a id="r_a5cb70820614b17bd8abcc529e887c1ed"></a>

```c
#define NXP_WUU_MODULE_0_DMA NXP_WUU_MODULE(0, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_MODULE_0_DMA](#a5cb70820614b17bd8abcc529e887c1ed)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

模块 0 的直接存储器访问请求事件（Module 0 DMA event）。

<a id="r_ac2f3a4f24d4ca6daa73d57ac0b683d45"></a>

```c
#define NXP_WUU_MODULE_1_INT NXP_WUU_MODULE(1, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_MODULE_1_INT](#ac2f3a4f24d4ca6daa73d57ac0b683d45)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

模块 1 的中断事件（Module 1 interrupt event）。

<a id="r_a12dacee6e2133b8acb605b445b07166f"></a>

```c
#define NXP_WUU_MODULE_1_DMA NXP_WUU_MODULE(1, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_MODULE_1_DMA](#a12dacee6e2133b8acb605b445b07166f)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

模块 1 的直接存储器访问请求事件（Module 1 DMA event）。

<a id="r_a3ec96a49fd44b5ea9c33c82836f6a098"></a>

```c
#define NXP_WUU_MODULE_2_INT NXP_WUU_MODULE(2, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_MODULE_2_INT](#a3ec96a49fd44b5ea9c33c82836f6a098)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

模块 2 的中断事件（Module 2 interrupt event）。

<a id="r_a08893ac4841a0ee78f5f288d53712d3d"></a>

```c
#define NXP_WUU_MODULE_2_DMA NXP_WUU_MODULE(2, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_MODULE_2_DMA](#a08893ac4841a0ee78f5f288d53712d3d)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

模块 2 的直接存储器访问请求事件（Module 2 DMA event）。

<a id="r_a8f0c44f30e63ae6d3e1453bb18bb8646"></a>

```c
#define NXP_WUU_MODULE_3_INT NXP_WUU_MODULE(3, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_MODULE_3_INT](#a8f0c44f30e63ae6d3e1453bb18bb8646)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

模块 3 的中断事件（Module 3 interrupt event）。

<a id="r_a55b29249adf66470825dc044b0246b85"></a>

```c
#define NXP_WUU_MODULE_3_DMA NXP_WUU_MODULE(3, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_MODULE_3_DMA](#a55b29249adf66470825dc044b0246b85)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

模块 3 的直接存储器访问请求事件（Module 3 DMA event）。

<a id="r_a0b548b00c2bae479ccb64dfca49096d3"></a>

```c
#define NXP_WUU_MODULE_4_INT NXP_WUU_MODULE(4, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_MODULE_4_INT](#a0b548b00c2bae479ccb64dfca49096d3)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

模块 4 的中断事件（Module 4 interrupt event）。

<a id="r_a8df95e502cf1ce7fe512e422c2a7a883"></a>

```c
#define NXP_WUU_MODULE_4_DMA NXP_WUU_MODULE(4, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_MODULE_4_DMA](#a8df95e502cf1ce7fe512e422c2a7a883)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

模块 4 的直接存储器访问请求事件（Module 4 DMA event）。

<a id="r_a97bcc7c02461cdbc7e45ad16cd6584f1"></a>

```c
#define NXP_WUU_MODULE_5_INT NXP_WUU_MODULE(5, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_MODULE_5_INT](#a97bcc7c02461cdbc7e45ad16cd6584f1)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

模块 5 的中断事件（Module 5 interrupt event）。

<a id="r_add2dc5d80f1b479e3f746565bc8bc966"></a>

```c
#define NXP_WUU_MODULE_5_DMA NXP_WUU_MODULE(5, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_MODULE_5_DMA](#add2dc5d80f1b479e3f746565bc8bc966)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

模块 5 的直接存储器访问请求事件（Module 5 DMA event）。

<a id="r_ad75f431f6530daef607df0b66a3ca55e"></a>

```c
#define NXP_WUU_MODULE_6_INT NXP_WUU_MODULE(6, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_MODULE_6_INT](#ad75f431f6530daef607df0b66a3ca55e)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

模块 6 的中断事件（Module 6 interrupt event）。

<a id="r_a4b1b3295f21a1f302a8c3021c44af333"></a>

```c
#define NXP_WUU_MODULE_6_DMA NXP_WUU_MODULE(6, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_MODULE_6_DMA](#a4b1b3295f21a1f302a8c3021c44af333)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

模块 6 的直接存储器访问请求事件（Module 6 DMA event）。

<a id="r_a67067fe3faf13b176c031b168aafe8eb"></a>

```c
#define NXP_WUU_MODULE_7_INT NXP_WUU_MODULE(7, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_MODULE_7_INT](#a67067fe3faf13b176c031b168aafe8eb)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

模块 7 的中断事件（Module 7 interrupt event）。

<a id="r_a361dd458bd1f5301d0545d811725b6f6"></a>

```c
#define NXP_WUU_MODULE_7_DMA NXP_WUU_MODULE(7, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_MODULE_7_DMA](#a361dd458bd1f5301d0545d811725b6f6)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

模块 7 的直接存储器访问请求事件（Module 7 DMA event）。

<a id="r_aa2770d71d20d9020fe3c3a9e5fb5aefa"></a>

```c
#define NXP_WUU_MODULE_8_INT NXP_WUU_MODULE(8, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_MODULE_8_INT](#aa2770d71d20d9020fe3c3a9e5fb5aefa)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

模块 8 的中断事件（Module 8 interrupt event）。

<a id="r_aa2335d42e9540087a553c12004103d65"></a>

```c
#define NXP_WUU_MODULE_8_DMA NXP_WUU_MODULE(8, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_MODULE_8_DMA](#aa2335d42e9540087a553c12004103d65)、[NXP_WUU_MODULE](#afaff4a945c102da5d4abf0e04b13e6db)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

模块 8 的直接存储器访问请求事件（Module 8 DMA event）。

<a id="r_a45864288bc9595f24b31c07669cb7677"></a>

```c
#define NXP_WUU_PIN_0_RISING_INT NXP_WUU_PIN(0, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_0_RISING_INT](#a45864288bc9595f24b31c07669cb7677)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

WUU 引脚唤醒源（PIN Wakeup Sources）。

<a id="r_a892bedc667e76defef7cc16404bb3a38"></a>

```c
#define NXP_WUU_PIN_0_RISING_DMA NXP_WUU_PIN(0, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_0_RISING_DMA](#a892bedc667e76defef7cc16404bb3a38)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 0 的上升沿直接存储器访问请求（Pin 0 rising edge DMA）。

<a id="r_ae57af895036fef4497730cd13318cbf4"></a>

```c
#define NXP_WUU_PIN_0_RISING_TRIGGER NXP_WUU_PIN(0, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_0_RISING_TRIGGER](#ae57af895036fef4497730cd13318cbf4)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 0 的上升沿触发输出（Pin 0 rising edge trigger）。

<a id="r_a0b46e5fd76565651af24a69d8f3d399d"></a>

```c
#define NXP_WUU_PIN_0_FALLING_INT NXP_WUU_PIN(0, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_0_FALLING_INT](#a0b46e5fd76565651af24a69d8f3d399d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 0 的下降沿中断（Pin 0 falling edge interrupt）。

<a id="r_adee8759a9241a0f7af2476c52471e552"></a>

```c
#define NXP_WUU_PIN_0_FALLING_DMA NXP_WUU_PIN(0, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_0_FALLING_DMA](#adee8759a9241a0f7af2476c52471e552)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 0 的下降沿直接存储器访问请求（Pin 0 falling edge DMA）。

<a id="r_ab6b631213c89af5dda08e98f5d915cf2"></a>

```c
#define NXP_WUU_PIN_0_FALLING_TRIGGER NXP_WUU_PIN(0, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_0_FALLING_TRIGGER](#ab6b631213c89af5dda08e98f5d915cf2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 0 的下降沿触发输出（Pin 0 falling edge trigger）。

<a id="r_a84566bb8afb43b70f438ba31a3ddabe1"></a>

```c
#define NXP_WUU_PIN_0_ANY_INT NXP_WUU_PIN(0, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_0_ANY_INT](#a84566bb8afb43b70f438ba31a3ddabe1)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 0 的任意边沿中断（Pin 0 any edge interrupt）。

<a id="r_afe9e7a04f92034a4d9288e2b49e595ab"></a>

```c
#define NXP_WUU_PIN_0_ANY_DMA NXP_WUU_PIN(0, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_0_ANY_DMA](#afe9e7a04f92034a4d9288e2b49e595ab)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 0 的任意边沿直接存储器访问请求（Pin 0 any edge DMA）。

<a id="r_a05f73c8cb789760efcc6d076552fb00f"></a>

```c
#define NXP_WUU_PIN_0_ANY_TRIGGER NXP_WUU_PIN(0, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_0_ANY_TRIGGER](#a05f73c8cb789760efcc6d076552fb00f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 0 的任意边沿触发输出（Pin 0 any edge trigger）。

<a id="r_af6c68e8fa486d668d8ef2d5f1d375c14"></a>

```c
#define NXP_WUU_PIN_1_RISING_INT NXP_WUU_PIN(1, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_1_RISING_INT](#af6c68e8fa486d668d8ef2d5f1d375c14)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 1 的上升沿中断（Pin 1 rising edge interrupt）。

<a id="r_a545a4416464829a915fd94cd8d83adc5"></a>

```c
#define NXP_WUU_PIN_1_RISING_DMA NXP_WUU_PIN(1, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_1_RISING_DMA](#a545a4416464829a915fd94cd8d83adc5)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 1 的上升沿直接存储器访问请求（Pin 1 rising edge DMA）。

<a id="r_a5090f5949511fd8db1bc4221cc4da47f"></a>

```c
#define NXP_WUU_PIN_1_RISING_TRIGGER NXP_WUU_PIN(1, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_1_RISING_TRIGGER](#a5090f5949511fd8db1bc4221cc4da47f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 1 的上升沿触发输出（Pin 1 rising edge trigger）。

<a id="r_ad7874c8b597433427225dfb715310f9f"></a>

```c
#define NXP_WUU_PIN_1_FALLING_INT NXP_WUU_PIN(1, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_1_FALLING_INT](#ad7874c8b597433427225dfb715310f9f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 1 的下降沿中断（Pin 1 falling edge interrupt）。

<a id="r_afd3d2a168c2bc1443b427c044bd7c23c"></a>

```c
#define NXP_WUU_PIN_1_FALLING_DMA NXP_WUU_PIN(1, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_1_FALLING_DMA](#afd3d2a168c2bc1443b427c044bd7c23c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 1 的下降沿直接存储器访问请求（Pin 1 falling edge DMA）。

<a id="r_ae72c2cefea5ca77ea80f01eccf757ab6"></a>

```c
#define NXP_WUU_PIN_1_FALLING_TRIGGER NXP_WUU_PIN(1, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_1_FALLING_TRIGGER](#ae72c2cefea5ca77ea80f01eccf757ab6)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 1 的下降沿触发输出（Pin 1 falling edge trigger）。

<a id="r_a4322d9c1add84c779e93f0f6c0a72581"></a>

```c
#define NXP_WUU_PIN_1_ANY_INT NXP_WUU_PIN(1, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_1_ANY_INT](#a4322d9c1add84c779e93f0f6c0a72581)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 1 的任意边沿中断（Pin 1 any edge interrupt）。

<a id="r_a3714e4b51f69f6c81f4beef8be9c7662"></a>

```c
#define NXP_WUU_PIN_1_ANY_DMA NXP_WUU_PIN(1, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_1_ANY_DMA](#a3714e4b51f69f6c81f4beef8be9c7662)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 1 的任意边沿直接存储器访问请求（Pin 1 any edge DMA）。

<a id="r_a155a73ef138aeaaddcaf6c3fc6f26f13"></a>

```c
#define NXP_WUU_PIN_1_ANY_TRIGGER NXP_WUU_PIN(1, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_1_ANY_TRIGGER](#a155a73ef138aeaaddcaf6c3fc6f26f13)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 1 的任意边沿触发输出（Pin 1 any edge trigger）。

<a id="r_a065e54fcd117c45abfdef2b34e012dbc"></a>

```c
#define NXP_WUU_PIN_2_RISING_INT NXP_WUU_PIN(2, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_2_RISING_INT](#a065e54fcd117c45abfdef2b34e012dbc)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 2 的上升沿中断（Pin 2 rising edge interrupt）。

<a id="r_a84d9e6be844a6900e828f8985fe51f02"></a>

```c
#define NXP_WUU_PIN_2_RISING_DMA NXP_WUU_PIN(2, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_2_RISING_DMA](#a84d9e6be844a6900e828f8985fe51f02)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 2 的上升沿直接存储器访问请求（Pin 2 rising edge DMA）。

<a id="r_a88e4dd24b7fbf8133808822fac85d0b3"></a>

```c
#define NXP_WUU_PIN_2_RISING_TRIGGER NXP_WUU_PIN(2, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_2_RISING_TRIGGER](#a88e4dd24b7fbf8133808822fac85d0b3)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 2 的上升沿触发输出（Pin 2 rising edge trigger）。

<a id="r_a829b2582b7bda3f86b53118691bbf9ad"></a>

```c
#define NXP_WUU_PIN_2_FALLING_INT NXP_WUU_PIN(2, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_2_FALLING_INT](#a829b2582b7bda3f86b53118691bbf9ad)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 2 的下降沿中断（Pin 2 falling edge interrupt）。

<a id="r_ad094c074f68621557b20f692c10f7852"></a>

```c
#define NXP_WUU_PIN_2_FALLING_DMA NXP_WUU_PIN(2, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_2_FALLING_DMA](#ad094c074f68621557b20f692c10f7852)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 2 的下降沿直接存储器访问请求（Pin 2 falling edge DMA）。

<a id="r_a85246cda06850b9c7470710b50fcb067"></a>

```c
#define NXP_WUU_PIN_2_FALLING_TRIGGER NXP_WUU_PIN(2, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_2_FALLING_TRIGGER](#a85246cda06850b9c7470710b50fcb067)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 2 的下降沿触发输出（Pin 2 falling edge trigger）。

<a id="r_ad3c929fd00d7ef13d4fce5bf05354d42"></a>

```c
#define NXP_WUU_PIN_2_ANY_INT NXP_WUU_PIN(2, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_2_ANY_INT](#ad3c929fd00d7ef13d4fce5bf05354d42)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 2 的任意边沿中断（Pin 2 any edge interrupt）。

<a id="r_a189200efbd1d8a32222b626643cc9aa0"></a>

```c
#define NXP_WUU_PIN_2_ANY_DMA NXP_WUU_PIN(2, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_2_ANY_DMA](#a189200efbd1d8a32222b626643cc9aa0)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 2 的任意边沿直接存储器访问请求（Pin 2 any edge DMA）。

<a id="r_ae002d606053d5dfc818cc6decd0f5344"></a>

```c
#define NXP_WUU_PIN_2_ANY_TRIGGER NXP_WUU_PIN(2, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_2_ANY_TRIGGER](#ae002d606053d5dfc818cc6decd0f5344)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 2 的任意边沿触发输出（Pin 2 any edge trigger）。

<a id="r_a35ae0792e0b716d46b82bab627965116"></a>

```c
#define NXP_WUU_PIN_3_RISING_INT NXP_WUU_PIN(3, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_3_RISING_INT](#a35ae0792e0b716d46b82bab627965116)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 3 的上升沿中断（Pin 3 rising edge interrupt）。

<a id="r_a156b3b7b038161a5757ea6945fe6f7cd"></a>

```c
#define NXP_WUU_PIN_3_RISING_DMA NXP_WUU_PIN(3, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_3_RISING_DMA](#a156b3b7b038161a5757ea6945fe6f7cd)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 3 的上升沿直接存储器访问请求（Pin 3 rising edge DMA）。

<a id="r_a4574d79575dabc93c3afca157e0bdeb8"></a>

```c
#define NXP_WUU_PIN_3_RISING_TRIGGER NXP_WUU_PIN(3, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_3_RISING_TRIGGER](#a4574d79575dabc93c3afca157e0bdeb8)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 3 的上升沿触发输出（Pin 3 rising edge trigger）。

<a id="r_af7134ed647faed2cf54849fb5829bcd1"></a>

```c
#define NXP_WUU_PIN_3_FALLING_INT NXP_WUU_PIN(3, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_3_FALLING_INT](#af7134ed647faed2cf54849fb5829bcd1)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 3 的下降沿中断（Pin 3 falling edge interrupt）。

<a id="r_aec1e5d52cd412af5a559472ee40e5807"></a>

```c
#define NXP_WUU_PIN_3_FALLING_DMA NXP_WUU_PIN(3, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_3_FALLING_DMA](#aec1e5d52cd412af5a559472ee40e5807)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 3 的下降沿直接存储器访问请求（Pin 3 falling edge DMA）。

<a id="r_a8a20192b0b8972eb651043634844affa"></a>

```c
#define NXP_WUU_PIN_3_FALLING_TRIGGER NXP_WUU_PIN(3, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_3_FALLING_TRIGGER](#a8a20192b0b8972eb651043634844affa)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 3 的下降沿触发输出（Pin 3 falling edge trigger）。

<a id="r_a737c61948f5a33d352ed0f356239da0a"></a>

```c
#define NXP_WUU_PIN_3_ANY_INT NXP_WUU_PIN(3, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_3_ANY_INT](#a737c61948f5a33d352ed0f356239da0a)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 3 的任意边沿中断（Pin 3 any edge interrupt）。

<a id="r_aabbd3a817a790f26c62b6e2174fe07ca"></a>

```c
#define NXP_WUU_PIN_3_ANY_DMA NXP_WUU_PIN(3, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_3_ANY_DMA](#aabbd3a817a790f26c62b6e2174fe07ca)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 3 的任意边沿直接存储器访问请求（Pin 3 any edge DMA）。

<a id="r_aa24891983beba114925065478cdb0d02"></a>

```c
#define NXP_WUU_PIN_3_ANY_TRIGGER NXP_WUU_PIN(3, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_3_ANY_TRIGGER](#aa24891983beba114925065478cdb0d02)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 3 的任意边沿触发输出（Pin 3 any edge trigger）。

<a id="r_a03ffa3bf5c3edd6d91dff43ca2538b9b"></a>

```c
#define NXP_WUU_PIN_4_RISING_INT NXP_WUU_PIN(4, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_4_RISING_INT](#a03ffa3bf5c3edd6d91dff43ca2538b9b)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 4 的上升沿中断（Pin 4 rising edge interrupt）。

<a id="r_a0d5228f868cb0a56a5d5b74006b1223e"></a>

```c
#define NXP_WUU_PIN_4_RISING_DMA NXP_WUU_PIN(4, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_4_RISING_DMA](#a0d5228f868cb0a56a5d5b74006b1223e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 4 的上升沿直接存储器访问请求（Pin 4 rising edge DMA）。

<a id="r_a04b515a0005e1662a864a05ccc0e04b8"></a>

```c
#define NXP_WUU_PIN_4_RISING_TRIGGER NXP_WUU_PIN(4, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_4_RISING_TRIGGER](#a04b515a0005e1662a864a05ccc0e04b8)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 4 的上升沿触发输出（Pin 4 rising edge trigger）。

<a id="r_a221d7a4d5e96e7c8202fe51bf630a626"></a>

```c
#define NXP_WUU_PIN_4_FALLING_INT NXP_WUU_PIN(4, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_4_FALLING_INT](#a221d7a4d5e96e7c8202fe51bf630a626)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 4 的下降沿中断（Pin 4 falling edge interrupt）。

<a id="r_a53c4b1d915699ee902639539954e9bca"></a>

```c
#define NXP_WUU_PIN_4_FALLING_DMA NXP_WUU_PIN(4, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_4_FALLING_DMA](#a53c4b1d915699ee902639539954e9bca)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 4 的下降沿直接存储器访问请求（Pin 4 falling edge DMA）。

<a id="r_aedfec85e539e3f2001fb0290c43ed422"></a>

```c
#define NXP_WUU_PIN_4_FALLING_TRIGGER NXP_WUU_PIN(4, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_4_FALLING_TRIGGER](#aedfec85e539e3f2001fb0290c43ed422)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 4 的下降沿触发输出（Pin 4 falling edge trigger）。

<a id="r_a0679a44abb91b4404142fe0abc2c9f0d"></a>

```c
#define NXP_WUU_PIN_4_ANY_INT NXP_WUU_PIN(4, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_4_ANY_INT](#a0679a44abb91b4404142fe0abc2c9f0d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 4 的任意边沿中断（Pin 4 any edge interrupt）。

<a id="r_a1de265d095d774fec9fa26820cb90e2e"></a>

```c
#define NXP_WUU_PIN_4_ANY_DMA NXP_WUU_PIN(4, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_4_ANY_DMA](#a1de265d095d774fec9fa26820cb90e2e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 4 的任意边沿直接存储器访问请求（Pin 4 any edge DMA）。

<a id="r_a64ab721b978a687974af47dadb5c9779"></a>

```c
#define NXP_WUU_PIN_4_ANY_TRIGGER NXP_WUU_PIN(4, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_4_ANY_TRIGGER](#a64ab721b978a687974af47dadb5c9779)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 4 的任意边沿触发输出（Pin 4 any edge trigger）。

<a id="r_acaaa8970ac212cb84264eb4171684c62"></a>

```c
#define NXP_WUU_PIN_5_RISING_INT NXP_WUU_PIN(5, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_5_RISING_INT](#acaaa8970ac212cb84264eb4171684c62)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 5 的上升沿中断（Pin 5 rising edge interrupt）。

<a id="r_a7fdc593f1390bff7b96e0cfaa2824dbf"></a>

```c
#define NXP_WUU_PIN_5_RISING_DMA NXP_WUU_PIN(5, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_5_RISING_DMA](#a7fdc593f1390bff7b96e0cfaa2824dbf)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 5 的上升沿直接存储器访问请求（Pin 5 rising edge DMA）。

<a id="r_a7f302101a226e9288223a3b62ed3ab24"></a>

```c
#define NXP_WUU_PIN_5_RISING_TRIGGER NXP_WUU_PIN(5, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_5_RISING_TRIGGER](#a7f302101a226e9288223a3b62ed3ab24)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 5 的上升沿触发输出（Pin 5 rising edge trigger）。

<a id="r_a20855781ffe40aadb8909da13d175bab"></a>

```c
#define NXP_WUU_PIN_5_FALLING_INT NXP_WUU_PIN(5, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_5_FALLING_INT](#a20855781ffe40aadb8909da13d175bab)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 5 的下降沿中断（Pin 5 falling edge interrupt）。

<a id="r_aba5b3ed4b607afc26d0d16e923a2b7f2"></a>

```c
#define NXP_WUU_PIN_5_FALLING_DMA NXP_WUU_PIN(5, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_5_FALLING_DMA](#aba5b3ed4b607afc26d0d16e923a2b7f2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 5 的下降沿直接存储器访问请求（Pin 5 falling edge DMA）。

<a id="r_ac00de1cc83661c503630f8add5763f62"></a>

```c
#define NXP_WUU_PIN_5_FALLING_TRIGGER NXP_WUU_PIN(5, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_5_FALLING_TRIGGER](#ac00de1cc83661c503630f8add5763f62)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 5 的下降沿触发输出（Pin 5 falling edge trigger）。

<a id="r_a26841234d383fbfee40a1f30d23882ba"></a>

```c
#define NXP_WUU_PIN_5_ANY_INT NXP_WUU_PIN(5, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_5_ANY_INT](#a26841234d383fbfee40a1f30d23882ba)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 5 的任意边沿中断（Pin 5 any edge interrupt）。

<a id="r_a5f98a8f759dbab2c7e55e9b8a3fe4efe"></a>

```c
#define NXP_WUU_PIN_5_ANY_DMA NXP_WUU_PIN(5, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_5_ANY_DMA](#a5f98a8f759dbab2c7e55e9b8a3fe4efe)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 5 的任意边沿直接存储器访问请求（Pin 5 any edge DMA）。

<a id="r_a90fee494887f96b13ccaf091bc583a3e"></a>

```c
#define NXP_WUU_PIN_5_ANY_TRIGGER NXP_WUU_PIN(5, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_5_ANY_TRIGGER](#a90fee494887f96b13ccaf091bc583a3e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 5 的任意边沿触发输出（Pin 5 any edge trigger）。

<a id="r_aedd93d9766b02eb9b9ad88240dde6602"></a>

```c
#define NXP_WUU_PIN_6_RISING_INT NXP_WUU_PIN(6, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_6_RISING_INT](#aedd93d9766b02eb9b9ad88240dde6602)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 6 的上升沿中断（Pin 6 rising edge interrupt）。

<a id="r_ac6f14a518aeb2d0312cde5eef8a1d27f"></a>

```c
#define NXP_WUU_PIN_6_RISING_DMA NXP_WUU_PIN(6, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_6_RISING_DMA](#ac6f14a518aeb2d0312cde5eef8a1d27f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 6 的上升沿直接存储器访问请求（Pin 6 rising edge DMA）。

<a id="r_af0749213c8d920cd41347f90891b1bd1"></a>

```c
#define NXP_WUU_PIN_6_RISING_TRIGGER NXP_WUU_PIN(6, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_6_RISING_TRIGGER](#af0749213c8d920cd41347f90891b1bd1)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 6 的上升沿触发输出（Pin 6 rising edge trigger）。

<a id="r_a036c6d65349a3abf5fcebf990d9e63e0"></a>

```c
#define NXP_WUU_PIN_6_FALLING_INT NXP_WUU_PIN(6, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_6_FALLING_INT](#a036c6d65349a3abf5fcebf990d9e63e0)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 6 的下降沿中断（Pin 6 falling edge interrupt）。

<a id="r_a4bba8ac0ac94dc3248639b542bc4596f"></a>

```c
#define NXP_WUU_PIN_6_FALLING_DMA NXP_WUU_PIN(6, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_6_FALLING_DMA](#a4bba8ac0ac94dc3248639b542bc4596f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 6 的下降沿直接存储器访问请求（Pin 6 falling edge DMA）。

<a id="r_acf56e5732e701ddad7f21595b13f33f6"></a>

```c
#define NXP_WUU_PIN_6_FALLING_TRIGGER NXP_WUU_PIN(6, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_6_FALLING_TRIGGER](#acf56e5732e701ddad7f21595b13f33f6)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 6 的下降沿触发输出（Pin 6 falling edge trigger）。

<a id="r_a752d52864160dc25cc25874871dcba6c"></a>

```c
#define NXP_WUU_PIN_6_ANY_INT NXP_WUU_PIN(6, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_6_ANY_INT](#a752d52864160dc25cc25874871dcba6c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 6 的任意边沿中断（Pin 6 any edge interrupt）。

<a id="r_af7a115cb95d28d7195cce12155a35f9e"></a>

```c
#define NXP_WUU_PIN_6_ANY_DMA NXP_WUU_PIN(6, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_6_ANY_DMA](#af7a115cb95d28d7195cce12155a35f9e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 6 的任意边沿直接存储器访问请求（Pin 6 any edge DMA）。

<a id="r_ac1b311ddfc3000eec9df3b82cd14704b"></a>

```c
#define NXP_WUU_PIN_6_ANY_TRIGGER NXP_WUU_PIN(6, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_6_ANY_TRIGGER](#ac1b311ddfc3000eec9df3b82cd14704b)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 6 的任意边沿触发输出（Pin 6 any edge trigger）。

<a id="r_a8b21a3c4f017be5430eeecdc2d641cb8"></a>

```c
#define NXP_WUU_PIN_7_RISING_INT NXP_WUU_PIN(7, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_7_RISING_INT](#a8b21a3c4f017be5430eeecdc2d641cb8)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 7 的上升沿中断（Pin 7 rising edge interrupt）。

<a id="r_a50ebf181f3be451a10615450efcb251b"></a>

```c
#define NXP_WUU_PIN_7_RISING_DMA NXP_WUU_PIN(7, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_7_RISING_DMA](#a50ebf181f3be451a10615450efcb251b)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 7 的上升沿直接存储器访问请求（Pin 7 rising edge DMA）。

<a id="r_ae0c98281fd53d8f03a533c7a4460700a"></a>

```c
#define NXP_WUU_PIN_7_RISING_TRIGGER NXP_WUU_PIN(7, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_7_RISING_TRIGGER](#ae0c98281fd53d8f03a533c7a4460700a)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 7 的上升沿触发输出（Pin 7 rising edge trigger）。

<a id="r_acb5ab244dad84bb053bcf74bb6a6c81f"></a>

```c
#define NXP_WUU_PIN_7_FALLING_INT NXP_WUU_PIN(7, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_7_FALLING_INT](#acb5ab244dad84bb053bcf74bb6a6c81f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 7 的下降沿中断（Pin 7 falling edge interrupt）。

<a id="r_add18fd6736de55936cc29571a51754c6"></a>

```c
#define NXP_WUU_PIN_7_FALLING_DMA NXP_WUU_PIN(7, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_7_FALLING_DMA](#add18fd6736de55936cc29571a51754c6)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 7 的下降沿直接存储器访问请求（Pin 7 falling edge DMA）。

<a id="r_a7fabee54875e2ca9be3b5a5a03851173"></a>

```c
#define NXP_WUU_PIN_7_FALLING_TRIGGER NXP_WUU_PIN(7, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_7_FALLING_TRIGGER](#a7fabee54875e2ca9be3b5a5a03851173)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 7 的下降沿触发输出（Pin 7 falling edge trigger）。

<a id="r_aee7ae97ed373dbd8bc3d315260eb3e5c"></a>

```c
#define NXP_WUU_PIN_7_ANY_INT NXP_WUU_PIN(7, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_7_ANY_INT](#aee7ae97ed373dbd8bc3d315260eb3e5c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 7 的任意边沿中断（Pin 7 any edge interrupt）。

<a id="r_ad13c89d41a3cf9c9e971cb3a8ef4c1e4"></a>

```c
#define NXP_WUU_PIN_7_ANY_DMA NXP_WUU_PIN(7, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_7_ANY_DMA](#ad13c89d41a3cf9c9e971cb3a8ef4c1e4)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 7 的任意边沿直接存储器访问请求（Pin 7 any edge DMA）。

<a id="r_abb5df8e6ff7af5e4a0a4f08e61a47d97"></a>

```c
#define NXP_WUU_PIN_7_ANY_TRIGGER NXP_WUU_PIN(7, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_7_ANY_TRIGGER](#abb5df8e6ff7af5e4a0a4f08e61a47d97)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 7 的任意边沿触发输出（Pin 7 any edge trigger）。

<a id="r_a191fa35fc706ffb26703a48fd0cdcddf"></a>

```c
#define NXP_WUU_PIN_8_RISING_INT NXP_WUU_PIN(8, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_8_RISING_INT](#a191fa35fc706ffb26703a48fd0cdcddf)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 8 的上升沿中断（Pin 8 rising edge interrupt）。

<a id="r_a8620ba95a59f4817c28b9987bddee80d"></a>

```c
#define NXP_WUU_PIN_8_RISING_DMA NXP_WUU_PIN(8, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_8_RISING_DMA](#a8620ba95a59f4817c28b9987bddee80d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 8 的上升沿直接存储器访问请求（Pin 8 rising edge DMA）。

<a id="r_af7cf40dbc62bea416bd94ee894e978f2"></a>

```c
#define NXP_WUU_PIN_8_RISING_TRIGGER NXP_WUU_PIN(8, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_8_RISING_TRIGGER](#af7cf40dbc62bea416bd94ee894e978f2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 8 的上升沿触发输出（Pin 8 rising edge trigger）。

<a id="r_a1f8e0e7b12c2a3f8e0bdc60f1c219f5f"></a>

```c
#define NXP_WUU_PIN_8_FALLING_INT NXP_WUU_PIN(8, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_8_FALLING_INT](#a1f8e0e7b12c2a3f8e0bdc60f1c219f5f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 8 的下降沿中断（Pin 8 falling edge interrupt）。

<a id="r_a66cb9726ac60da282bcfa7be7e041ff7"></a>

```c
#define NXP_WUU_PIN_8_FALLING_DMA NXP_WUU_PIN(8, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_8_FALLING_DMA](#a66cb9726ac60da282bcfa7be7e041ff7)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 8 的下降沿直接存储器访问请求（Pin 8 falling edge DMA）。

<a id="r_adb784db06fa54157da7fc09f848a8d83"></a>

```c
#define NXP_WUU_PIN_8_FALLING_TRIGGER NXP_WUU_PIN(8, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_8_FALLING_TRIGGER](#adb784db06fa54157da7fc09f848a8d83)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 8 的下降沿触发输出（Pin 8 falling edge trigger）。

<a id="r_ab15c905cc40563b658ec1522af9887e9"></a>

```c
#define NXP_WUU_PIN_8_ANY_INT NXP_WUU_PIN(8, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_8_ANY_INT](#ab15c905cc40563b658ec1522af9887e9)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 8 的任意边沿中断（Pin 8 any edge interrupt）。

<a id="r_a392a466f5148cb8eb32f0b12bd38904e"></a>

```c
#define NXP_WUU_PIN_8_ANY_DMA NXP_WUU_PIN(8, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_8_ANY_DMA](#a392a466f5148cb8eb32f0b12bd38904e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 8 的任意边沿直接存储器访问请求（Pin 8 any edge DMA）。

<a id="r_a29d76ec9b7ae3f611944b140d6fc6aa2"></a>

```c
#define NXP_WUU_PIN_8_ANY_TRIGGER NXP_WUU_PIN(8, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_8_ANY_TRIGGER](#a29d76ec9b7ae3f611944b140d6fc6aa2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 8 的任意边沿触发输出（Pin 8 any edge trigger）。

<a id="r_ad465da00c578d048d17f1d0383ac27b2"></a>

```c
#define NXP_WUU_PIN_9_RISING_INT NXP_WUU_PIN(9, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_9_RISING_INT](#ad465da00c578d048d17f1d0383ac27b2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 9 的上升沿中断（Pin 9 rising edge interrupt）。

<a id="r_a9e91e5cf898c0a4e722b4a7414cef455"></a>

```c
#define NXP_WUU_PIN_9_RISING_DMA NXP_WUU_PIN(9, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_9_RISING_DMA](#a9e91e5cf898c0a4e722b4a7414cef455)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 9 的上升沿直接存储器访问请求（Pin 9 rising edge DMA）。

<a id="r_a458a8c7e2c108a7ec044d900bc3fdde2"></a>

```c
#define NXP_WUU_PIN_9_RISING_TRIGGER NXP_WUU_PIN(9, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_9_RISING_TRIGGER](#a458a8c7e2c108a7ec044d900bc3fdde2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 9 的上升沿触发输出（Pin 9 rising edge trigger）。

<a id="r_abbb695600abf970fbbc1f69fed0ade4c"></a>

```c
#define NXP_WUU_PIN_9_FALLING_INT NXP_WUU_PIN(9, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_9_FALLING_INT](#abbb695600abf970fbbc1f69fed0ade4c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 9 的下降沿中断（Pin 9 falling edge interrupt）。

<a id="r_a97fecb5180baa34818e5993ea876cd73"></a>

```c
#define NXP_WUU_PIN_9_FALLING_DMA NXP_WUU_PIN(9, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_9_FALLING_DMA](#a97fecb5180baa34818e5993ea876cd73)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 9 的下降沿直接存储器访问请求（Pin 9 falling edge DMA）。

<a id="r_af44aba7a609b0e1fc7ac6aac9db5f5a4"></a>

```c
#define NXP_WUU_PIN_9_FALLING_TRIGGER NXP_WUU_PIN(9, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_9_FALLING_TRIGGER](#af44aba7a609b0e1fc7ac6aac9db5f5a4)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 9 的下降沿触发输出（Pin 9 falling edge trigger）。

<a id="r_af757f93d5d859727a7018163cb1cbbc2"></a>

```c
#define NXP_WUU_PIN_9_ANY_INT NXP_WUU_PIN(9, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_9_ANY_INT](#af757f93d5d859727a7018163cb1cbbc2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 9 的任意边沿中断（Pin 9 any edge interrupt）。

<a id="r_aa9750dfe149398cc3bdb992b8fe17d0c"></a>

```c
#define NXP_WUU_PIN_9_ANY_DMA NXP_WUU_PIN(9, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_9_ANY_DMA](#aa9750dfe149398cc3bdb992b8fe17d0c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 9 的任意边沿直接存储器访问请求（Pin 9 any edge DMA）。

<a id="r_a40b12fedf163e1e3ff5100bbcf487561"></a>

```c
#define NXP_WUU_PIN_9_ANY_TRIGGER NXP_WUU_PIN(9, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_9_ANY_TRIGGER](#a40b12fedf163e1e3ff5100bbcf487561)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 9 的任意边沿触发输出（Pin 9 any edge trigger）。

<a id="r_a8447381ee6c0599fb994fb3f5db3beda"></a>

```c
#define NXP_WUU_PIN_10_RISING_INT NXP_WUU_PIN(10, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_10_RISING_INT](#a8447381ee6c0599fb994fb3f5db3beda)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 10 的上升沿中断（Pin 10 rising edge interrupt）。

<a id="r_ab539e1019273d63bb8d270f3c1a0956a"></a>

```c
#define NXP_WUU_PIN_10_RISING_DMA NXP_WUU_PIN(10, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_10_RISING_DMA](#ab539e1019273d63bb8d270f3c1a0956a)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 10 的上升沿直接存储器访问请求（Pin 10 rising edge DMA）。

<a id="r_a0c66facf2f0bffe4015bf4c30bf617d0"></a>

```c
#define NXP_WUU_PIN_10_RISING_TRIGGER NXP_WUU_PIN(10, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_10_RISING_TRIGGER](#a0c66facf2f0bffe4015bf4c30bf617d0)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 10 的上升沿触发输出（Pin 10 rising edge trigger）。

<a id="r_a44fc0203ca3f908027e1da3a006c219d"></a>

```c
#define NXP_WUU_PIN_10_FALLING_INT NXP_WUU_PIN(10, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_10_FALLING_INT](#a44fc0203ca3f908027e1da3a006c219d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 10 的下降沿中断（Pin 10 falling edge interrupt）。

<a id="r_a36c7b24f0f53a1ed0601773bc47a0e37"></a>

```c
#define NXP_WUU_PIN_10_FALLING_DMA NXP_WUU_PIN(10, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_10_FALLING_DMA](#a36c7b24f0f53a1ed0601773bc47a0e37)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 10 的下降沿直接存储器访问请求（Pin 10 falling edge DMA）。

<a id="r_a5181167cba5b94fb7e075d615bb01040"></a>

```c
#define NXP_WUU_PIN_10_FALLING_TRIGGER NXP_WUU_PIN(10, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_10_FALLING_TRIGGER](#a5181167cba5b94fb7e075d615bb01040)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 10 的下降沿触发输出（Pin 10 falling edge trigger）。

<a id="r_a668ec7bafdbe61838dfee115e0e86208"></a>

```c
#define NXP_WUU_PIN_10_ANY_INT NXP_WUU_PIN(10, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_10_ANY_INT](#a668ec7bafdbe61838dfee115e0e86208)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 10 的任意边沿中断（Pin 10 any edge interrupt）。

<a id="r_ac5486ff7b60fdf52ff4c7b327eb6c2bd"></a>

```c
#define NXP_WUU_PIN_10_ANY_DMA NXP_WUU_PIN(10, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_10_ANY_DMA](#ac5486ff7b60fdf52ff4c7b327eb6c2bd)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 10 的任意边沿直接存储器访问请求（Pin 10 any edge DMA）。

<a id="r_a7c3057491ef9f1d8487f96bd766bedc9"></a>

```c
#define NXP_WUU_PIN_10_ANY_TRIGGER NXP_WUU_PIN(10, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_10_ANY_TRIGGER](#a7c3057491ef9f1d8487f96bd766bedc9)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 10 的任意边沿触发输出（Pin 10 any edge trigger）。

<a id="r_af8db9d843713d811f292739fd6d0bfd2"></a>

```c
#define NXP_WUU_PIN_11_RISING_INT NXP_WUU_PIN(11, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_11_RISING_INT](#af8db9d843713d811f292739fd6d0bfd2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 11 的上升沿中断（Pin 11 rising edge interrupt）。

<a id="r_a18654f13ee61ea9978a5a4cacbaf7cd1"></a>

```c
#define NXP_WUU_PIN_11_RISING_DMA NXP_WUU_PIN(11, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_11_RISING_DMA](#a18654f13ee61ea9978a5a4cacbaf7cd1)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 11 的上升沿直接存储器访问请求（Pin 11 rising edge DMA）。

<a id="r_acf0865bd22e6e34f7c756df522ec2f10"></a>

```c
#define NXP_WUU_PIN_11_RISING_TRIGGER NXP_WUU_PIN(11, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_11_RISING_TRIGGER](#acf0865bd22e6e34f7c756df522ec2f10)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 11 的上升沿触发输出（Pin 11 rising edge trigger）。

<a id="r_afb3ceace195d922f281453b98e614b8a"></a>

```c
#define NXP_WUU_PIN_11_FALLING_INT NXP_WUU_PIN(11, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_11_FALLING_INT](#afb3ceace195d922f281453b98e614b8a)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 11 的下降沿中断（Pin 11 falling edge interrupt）。

<a id="r_a79a3941da6becd8574f5dfa9ecef7f68"></a>

```c
#define NXP_WUU_PIN_11_FALLING_DMA NXP_WUU_PIN(11, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_11_FALLING_DMA](#a79a3941da6becd8574f5dfa9ecef7f68)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 11 的下降沿直接存储器访问请求（Pin 11 falling edge DMA）。

<a id="r_a23fa65ed5cc4da49c4c0629d26cab10c"></a>

```c
#define NXP_WUU_PIN_11_FALLING_TRIGGER NXP_WUU_PIN(11, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_11_FALLING_TRIGGER](#a23fa65ed5cc4da49c4c0629d26cab10c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 11 的下降沿触发输出（Pin 11 falling edge trigger）。

<a id="r_ab12bbe55fea8a0bfafe71b59d8e320c1"></a>

```c
#define NXP_WUU_PIN_11_ANY_INT NXP_WUU_PIN(11, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_11_ANY_INT](#ab12bbe55fea8a0bfafe71b59d8e320c1)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 11 的任意边沿中断（Pin 11 any edge interrupt）。

<a id="r_af94fd967bca069c116239a3cc471bb56"></a>

```c
#define NXP_WUU_PIN_11_ANY_DMA NXP_WUU_PIN(11, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_11_ANY_DMA](#af94fd967bca069c116239a3cc471bb56)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 11 的任意边沿直接存储器访问请求（Pin 11 any edge DMA）。

<a id="r_aa3d45d4578fcaaffd4a63eafe5fcbc27"></a>

```c
#define NXP_WUU_PIN_11_ANY_TRIGGER NXP_WUU_PIN(11, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_11_ANY_TRIGGER](#aa3d45d4578fcaaffd4a63eafe5fcbc27)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 11 的任意边沿触发输出（Pin 11 any edge trigger）。

<a id="r_a8c80f3d6e04df6097e991564a640a354"></a>

```c
#define NXP_WUU_PIN_12_RISING_INT NXP_WUU_PIN(12, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_12_RISING_INT](#a8c80f3d6e04df6097e991564a640a354)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 12 的上升沿中断（Pin 12 rising edge interrupt）。

<a id="r_a6294c8eec90daf5ceab3732ef4c5b54c"></a>

```c
#define NXP_WUU_PIN_12_RISING_DMA NXP_WUU_PIN(12, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_12_RISING_DMA](#a6294c8eec90daf5ceab3732ef4c5b54c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 12 的上升沿直接存储器访问请求（Pin 12 rising edge DMA）。

<a id="r_ae880986b6ee18f176b71cc9f28949662"></a>

```c
#define NXP_WUU_PIN_12_RISING_TRIGGER NXP_WUU_PIN(12, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_12_RISING_TRIGGER](#ae880986b6ee18f176b71cc9f28949662)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 12 的上升沿触发输出（Pin 12 rising edge trigger）。

<a id="r_a78658be45b157759cbf79e6843d10159"></a>

```c
#define NXP_WUU_PIN_12_FALLING_INT NXP_WUU_PIN(12, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_12_FALLING_INT](#a78658be45b157759cbf79e6843d10159)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 12 的下降沿中断（Pin 12 falling edge interrupt）。

<a id="r_a8e7e3f4786dfe612f08a0719dc356821"></a>

```c
#define NXP_WUU_PIN_12_FALLING_DMA NXP_WUU_PIN(12, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_12_FALLING_DMA](#a8e7e3f4786dfe612f08a0719dc356821)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 12 的下降沿直接存储器访问请求（Pin 12 falling edge DMA）。

<a id="r_a76fe883b827814f97028c211d2178041"></a>

```c
#define NXP_WUU_PIN_12_FALLING_TRIGGER NXP_WUU_PIN(12, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_12_FALLING_TRIGGER](#a76fe883b827814f97028c211d2178041)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 12 的下降沿触发输出（Pin 12 falling edge trigger）。

<a id="r_a0fcf797c4f587d5e09c19b975363d5b4"></a>

```c
#define NXP_WUU_PIN_12_ANY_INT NXP_WUU_PIN(12, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_12_ANY_INT](#a0fcf797c4f587d5e09c19b975363d5b4)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 12 的任意边沿中断（Pin 12 any edge interrupt）。

<a id="r_a48125bf1480f0cf0ced7a9e1744a8fc2"></a>

```c
#define NXP_WUU_PIN_12_ANY_DMA NXP_WUU_PIN(12, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_12_ANY_DMA](#a48125bf1480f0cf0ced7a9e1744a8fc2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 12 的任意边沿直接存储器访问请求（Pin 12 any edge DMA）。

<a id="r_adf0f44a76fa64137bfd769e7739e452f"></a>

```c
#define NXP_WUU_PIN_12_ANY_TRIGGER NXP_WUU_PIN(12, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_12_ANY_TRIGGER](#adf0f44a76fa64137bfd769e7739e452f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 12 的任意边沿触发输出（Pin 12 any edge trigger）。

<a id="r_abad94246db6369148c0fb1a3cf139a68"></a>

```c
#define NXP_WUU_PIN_13_RISING_INT NXP_WUU_PIN(13, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_13_RISING_INT](#abad94246db6369148c0fb1a3cf139a68)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 13 的上升沿中断（Pin 13 rising edge interrupt）。

<a id="r_a5c63c8669751a21f102f1e724bbbdaaf"></a>

```c
#define NXP_WUU_PIN_13_RISING_DMA NXP_WUU_PIN(13, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_13_RISING_DMA](#a5c63c8669751a21f102f1e724bbbdaaf)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 13 的上升沿直接存储器访问请求（Pin 13 rising edge DMA）。

<a id="r_aa85c1f075d31c57640d7c484b4a82586"></a>

```c
#define NXP_WUU_PIN_13_RISING_TRIGGER NXP_WUU_PIN(13, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_13_RISING_TRIGGER](#aa85c1f075d31c57640d7c484b4a82586)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 13 的上升沿触发输出（Pin 13 rising edge trigger）。

<a id="r_a6e4d6c89560f48f34052d59b05573630"></a>

```c
#define NXP_WUU_PIN_13_FALLING_INT NXP_WUU_PIN(13, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_13_FALLING_INT](#a6e4d6c89560f48f34052d59b05573630)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 13 的下降沿中断（Pin 13 falling edge interrupt）。

<a id="r_a12ac0088e1eed430adbc0f8e532b4c48"></a>

```c
#define NXP_WUU_PIN_13_FALLING_DMA NXP_WUU_PIN(13, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_13_FALLING_DMA](#a12ac0088e1eed430adbc0f8e532b4c48)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 13 的下降沿直接存储器访问请求（Pin 13 falling edge DMA）。

<a id="r_aec1b861704f490734e8befd3cf913a6e"></a>

```c
#define NXP_WUU_PIN_13_FALLING_TRIGGER NXP_WUU_PIN(13, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_13_FALLING_TRIGGER](#aec1b861704f490734e8befd3cf913a6e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 13 的下降沿触发输出（Pin 13 falling edge trigger）。

<a id="r_a1c7336fa2c11bf50cfee5a6b4e3842c9"></a>

```c
#define NXP_WUU_PIN_13_ANY_INT NXP_WUU_PIN(13, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_13_ANY_INT](#a1c7336fa2c11bf50cfee5a6b4e3842c9)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 13 的任意边沿中断（Pin 13 any edge interrupt）。

<a id="r_a0e70b987fd03139f436f7b53f723adcf"></a>

```c
#define NXP_WUU_PIN_13_ANY_DMA NXP_WUU_PIN(13, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_13_ANY_DMA](#a0e70b987fd03139f436f7b53f723adcf)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 13 的任意边沿直接存储器访问请求（Pin 13 any edge DMA）。

<a id="r_a8ebfd18a7979d0828d4683e02e1a2724"></a>

```c
#define NXP_WUU_PIN_13_ANY_TRIGGER NXP_WUU_PIN(13, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_13_ANY_TRIGGER](#a8ebfd18a7979d0828d4683e02e1a2724)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 13 的任意边沿触发输出（Pin 13 any edge trigger）。

<a id="r_adc38f6e93991725760cfef6758079c89"></a>

```c
#define NXP_WUU_PIN_14_RISING_INT NXP_WUU_PIN(14, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_14_RISING_INT](#adc38f6e93991725760cfef6758079c89)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 14 的上升沿中断（Pin 14 rising edge interrupt）。

<a id="r_a8698ee619dc97e7e5e10177b373d3d37"></a>

```c
#define NXP_WUU_PIN_14_RISING_DMA NXP_WUU_PIN(14, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_14_RISING_DMA](#a8698ee619dc97e7e5e10177b373d3d37)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 14 的上升沿直接存储器访问请求（Pin 14 rising edge DMA）。

<a id="r_aad6dc6a44a8051cd064d7949d6eb0c11"></a>

```c
#define NXP_WUU_PIN_14_RISING_TRIGGER NXP_WUU_PIN(14, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_14_RISING_TRIGGER](#aad6dc6a44a8051cd064d7949d6eb0c11)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 14 的上升沿触发输出（Pin 14 rising edge trigger）。

<a id="r_a4f69e11960adab498586507a9e7c3fb2"></a>

```c
#define NXP_WUU_PIN_14_FALLING_INT NXP_WUU_PIN(14, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_14_FALLING_INT](#a4f69e11960adab498586507a9e7c3fb2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 14 的下降沿中断（Pin 14 falling edge interrupt）。

<a id="r_a136e1a20fe6f29ba8a779c36b12f5884"></a>

```c
#define NXP_WUU_PIN_14_FALLING_DMA NXP_WUU_PIN(14, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_14_FALLING_DMA](#a136e1a20fe6f29ba8a779c36b12f5884)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 14 的下降沿直接存储器访问请求（Pin 14 falling edge DMA）。

<a id="r_a066fe7df5fd40e31d0d205a5084fc3dd"></a>

```c
#define NXP_WUU_PIN_14_FALLING_TRIGGER NXP_WUU_PIN(14, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_14_FALLING_TRIGGER](#a066fe7df5fd40e31d0d205a5084fc3dd)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 14 的下降沿触发输出（Pin 14 falling edge trigger）。

<a id="r_a7b4335ee8dd7af40e69bbf7ea2583c85"></a>

```c
#define NXP_WUU_PIN_14_ANY_INT NXP_WUU_PIN(14, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_14_ANY_INT](#a7b4335ee8dd7af40e69bbf7ea2583c85)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 14 的任意边沿中断（Pin 14 any edge interrupt）。

<a id="r_a62d9134ec2f2c8ea79bc8f9d1ee30047"></a>

```c
#define NXP_WUU_PIN_14_ANY_DMA NXP_WUU_PIN(14, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_14_ANY_DMA](#a62d9134ec2f2c8ea79bc8f9d1ee30047)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 14 的任意边沿直接存储器访问请求（Pin 14 any edge DMA）。

<a id="r_aed863aef549034f8eeafdb3d119afcec"></a>

```c
#define NXP_WUU_PIN_14_ANY_TRIGGER NXP_WUU_PIN(14, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_14_ANY_TRIGGER](#aed863aef549034f8eeafdb3d119afcec)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 14 的任意边沿触发输出（Pin 14 any edge trigger）。

<a id="r_a9db1b076129d3a63a30fbde70f3d7377"></a>

```c
#define NXP_WUU_PIN_15_RISING_INT NXP_WUU_PIN(15, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_15_RISING_INT](#a9db1b076129d3a63a30fbde70f3d7377)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 15 的上升沿中断（Pin 15 rising edge interrupt）。

<a id="r_aa0ddff16c6fd56eb67dec54c4e9c628f"></a>

```c
#define NXP_WUU_PIN_15_RISING_DMA NXP_WUU_PIN(15, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_15_RISING_DMA](#aa0ddff16c6fd56eb67dec54c4e9c628f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 15 的上升沿直接存储器访问请求（Pin 15 rising edge DMA）。

<a id="r_aa5eb7875891b2936c0a7c5f5a4c2584a"></a>

```c
#define NXP_WUU_PIN_15_RISING_TRIGGER NXP_WUU_PIN(15, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_15_RISING_TRIGGER](#aa5eb7875891b2936c0a7c5f5a4c2584a)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 15 的上升沿触发输出（Pin 15 rising edge trigger）。

<a id="r_a9071b46613aa5347323db173e9508d21"></a>

```c
#define NXP_WUU_PIN_15_FALLING_INT NXP_WUU_PIN(15, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_15_FALLING_INT](#a9071b46613aa5347323db173e9508d21)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 15 的下降沿中断（Pin 15 falling edge interrupt）。

<a id="r_a2b0d50f454fafa5813137f25ec74fb9b"></a>

```c
#define NXP_WUU_PIN_15_FALLING_DMA NXP_WUU_PIN(15, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_15_FALLING_DMA](#a2b0d50f454fafa5813137f25ec74fb9b)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 15 的下降沿直接存储器访问请求（Pin 15 falling edge DMA）。

<a id="r_a7bcd6009425bf5bd432109c03a7f7f7a"></a>

```c
#define NXP_WUU_PIN_15_FALLING_TRIGGER NXP_WUU_PIN(15, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_15_FALLING_TRIGGER](#a7bcd6009425bf5bd432109c03a7f7f7a)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 15 的下降沿触发输出（Pin 15 falling edge trigger）。

<a id="r_ad771a9eaf7825f54e54cee7755a9967a"></a>

```c
#define NXP_WUU_PIN_15_ANY_INT NXP_WUU_PIN(15, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_15_ANY_INT](#ad771a9eaf7825f54e54cee7755a9967a)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 15 的任意边沿中断（Pin 15 any edge interrupt）。

<a id="r_a81b0a064eed11059563734244b4808e7"></a>

```c
#define NXP_WUU_PIN_15_ANY_DMA NXP_WUU_PIN(15, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_15_ANY_DMA](#a81b0a064eed11059563734244b4808e7)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 15 的任意边沿直接存储器访问请求（Pin 15 any edge DMA）。

<a id="r_ad57084c076a2d90fe5a7038822d51e92"></a>

```c
#define NXP_WUU_PIN_15_ANY_TRIGGER NXP_WUU_PIN(15, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_15_ANY_TRIGGER](#ad57084c076a2d90fe5a7038822d51e92)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 15 的任意边沿触发输出（Pin 15 any edge trigger）。

<a id="r_adfcf294a24063a9931efa25df317732b"></a>

```c
#define NXP_WUU_PIN_16_RISING_INT NXP_WUU_PIN(16, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_16_RISING_INT](#adfcf294a24063a9931efa25df317732b)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 16 的上升沿中断（Pin 16 rising edge interrupt）。

<a id="r_a5dc27bc0fe120ae5c1cca98f2a4cdcfc"></a>

```c
#define NXP_WUU_PIN_16_RISING_DMA NXP_WUU_PIN(16, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_16_RISING_DMA](#a5dc27bc0fe120ae5c1cca98f2a4cdcfc)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 16 的上升沿直接存储器访问请求（Pin 16 rising edge DMA）。

<a id="r_a4a9c35ae2b4277edbbbb08b741c68fa6"></a>

```c
#define NXP_WUU_PIN_16_RISING_TRIGGER NXP_WUU_PIN(16, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_16_RISING_TRIGGER](#a4a9c35ae2b4277edbbbb08b741c68fa6)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 16 的上升沿触发输出（Pin 16 rising edge trigger）。

<a id="r_a450baf91b13cf9f27fd2ac012c7edabe"></a>

```c
#define NXP_WUU_PIN_16_FALLING_INT NXP_WUU_PIN(16, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_16_FALLING_INT](#a450baf91b13cf9f27fd2ac012c7edabe)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 16 的下降沿中断（Pin 16 falling edge interrupt）。

<a id="r_ad4bc82fd63883f02d34798a5712a46c5"></a>

```c
#define NXP_WUU_PIN_16_FALLING_DMA NXP_WUU_PIN(16, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_16_FALLING_DMA](#ad4bc82fd63883f02d34798a5712a46c5)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 16 的下降沿直接存储器访问请求（Pin 16 falling edge DMA）。

<a id="r_a728ac5704ab4594d71918f33871378ce"></a>

```c
#define NXP_WUU_PIN_16_FALLING_TRIGGER NXP_WUU_PIN(16, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_16_FALLING_TRIGGER](#a728ac5704ab4594d71918f33871378ce)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 16 的下降沿触发输出（Pin 16 falling edge trigger）。

<a id="r_ab897fe96ec5635bc19aaefa716551afa"></a>

```c
#define NXP_WUU_PIN_16_ANY_INT NXP_WUU_PIN(16, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_16_ANY_INT](#ab897fe96ec5635bc19aaefa716551afa)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 16 的任意边沿中断（Pin 16 any edge interrupt）。

<a id="r_a1e3156e7786f2968072d03d7ddf8757c"></a>

```c
#define NXP_WUU_PIN_16_ANY_DMA NXP_WUU_PIN(16, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_16_ANY_DMA](#a1e3156e7786f2968072d03d7ddf8757c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 16 的任意边沿直接存储器访问请求（Pin 16 any edge DMA）。

<a id="r_a5d840552a98bd57d478693fa898268ef"></a>

```c
#define NXP_WUU_PIN_16_ANY_TRIGGER NXP_WUU_PIN(16, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_16_ANY_TRIGGER](#a5d840552a98bd57d478693fa898268ef)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 16 的任意边沿触发输出（Pin 16 any edge trigger）。

<a id="r_a31540908b47a3bc950d07ea769e2417e"></a>

```c
#define NXP_WUU_PIN_17_RISING_INT NXP_WUU_PIN(17, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_17_RISING_INT](#a31540908b47a3bc950d07ea769e2417e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 17 的上升沿中断（Pin 17 rising edge interrupt）。

<a id="r_ad9c1dbacbc7a9ca82619e852d6226d01"></a>

```c
#define NXP_WUU_PIN_17_RISING_DMA NXP_WUU_PIN(17, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_17_RISING_DMA](#ad9c1dbacbc7a9ca82619e852d6226d01)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 17 的上升沿直接存储器访问请求（Pin 17 rising edge DMA）。

<a id="r_a427b957b4e32f43d7b9af0873c452fb0"></a>

```c
#define NXP_WUU_PIN_17_RISING_TRIGGER NXP_WUU_PIN(17, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_17_RISING_TRIGGER](#a427b957b4e32f43d7b9af0873c452fb0)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 17 的上升沿触发输出（Pin 17 rising edge trigger）。

<a id="r_a48c1840fa1c5cced807e030deee4200f"></a>

```c
#define NXP_WUU_PIN_17_FALLING_INT NXP_WUU_PIN(17, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_17_FALLING_INT](#a48c1840fa1c5cced807e030deee4200f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 17 的下降沿中断（Pin 17 falling edge interrupt）。

<a id="r_abf11fb64eb14a15507618780fe45b33e"></a>

```c
#define NXP_WUU_PIN_17_FALLING_DMA NXP_WUU_PIN(17, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_17_FALLING_DMA](#abf11fb64eb14a15507618780fe45b33e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 17 的下降沿直接存储器访问请求（Pin 17 falling edge DMA）。

<a id="r_a3532a13150ce817ad8766363241c6208"></a>

```c
#define NXP_WUU_PIN_17_FALLING_TRIGGER NXP_WUU_PIN(17, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_17_FALLING_TRIGGER](#a3532a13150ce817ad8766363241c6208)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 17 的下降沿触发输出（Pin 17 falling edge trigger）。

<a id="r_a78cfe7f65e765dec76141aba513e0102"></a>

```c
#define NXP_WUU_PIN_17_ANY_INT NXP_WUU_PIN(17, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_17_ANY_INT](#a78cfe7f65e765dec76141aba513e0102)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 17 的任意边沿中断（Pin 17 any edge interrupt）。

<a id="r_a46f0f287973dc5b750e7cf0514a2b9db"></a>

```c
#define NXP_WUU_PIN_17_ANY_DMA NXP_WUU_PIN(17, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_17_ANY_DMA](#a46f0f287973dc5b750e7cf0514a2b9db)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 17 的任意边沿直接存储器访问请求（Pin 17 any edge DMA）。

<a id="r_a6629f49862fd75b780ac775e529a6b7c"></a>

```c
#define NXP_WUU_PIN_17_ANY_TRIGGER NXP_WUU_PIN(17, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_17_ANY_TRIGGER](#a6629f49862fd75b780ac775e529a6b7c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 17 的任意边沿触发输出（Pin 17 any edge trigger）。

<a id="r_a506ccb796cfed8bd48999be92c41d0a5"></a>

```c
#define NXP_WUU_PIN_18_RISING_INT NXP_WUU_PIN(18, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_18_RISING_INT](#a506ccb796cfed8bd48999be92c41d0a5)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 18 的上升沿中断（Pin 18 rising edge interrupt）。

<a id="r_ae5df884ff42594d73630a479c7ed5cd9"></a>

```c
#define NXP_WUU_PIN_18_RISING_DMA NXP_WUU_PIN(18, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_18_RISING_DMA](#ae5df884ff42594d73630a479c7ed5cd9)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 18 的上升沿直接存储器访问请求（Pin 18 rising edge DMA）。

<a id="r_ab4a5ea49ce2a5afe63821f4b7aa241ed"></a>

```c
#define NXP_WUU_PIN_18_RISING_TRIGGER NXP_WUU_PIN(18, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_18_RISING_TRIGGER](#ab4a5ea49ce2a5afe63821f4b7aa241ed)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 18 的上升沿触发输出（Pin 18 rising edge trigger）。

<a id="r_ac978c583bd32dc45ec87b581f422562d"></a>

```c
#define NXP_WUU_PIN_18_FALLING_INT NXP_WUU_PIN(18, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_18_FALLING_INT](#ac978c583bd32dc45ec87b581f422562d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 18 的下降沿中断（Pin 18 falling edge interrupt）。

<a id="r_a8567faff46474b71fc45c12ec2a3ef44"></a>

```c
#define NXP_WUU_PIN_18_FALLING_DMA NXP_WUU_PIN(18, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_18_FALLING_DMA](#a8567faff46474b71fc45c12ec2a3ef44)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 18 的下降沿直接存储器访问请求（Pin 18 falling edge DMA）。

<a id="r_a7adcc876c2a608ade50e2b46c02c3236"></a>

```c
#define NXP_WUU_PIN_18_FALLING_TRIGGER NXP_WUU_PIN(18, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_18_FALLING_TRIGGER](#a7adcc876c2a608ade50e2b46c02c3236)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 18 的下降沿触发输出（Pin 18 falling edge trigger）。

<a id="r_a3fca4746d56e2c3fb231d3f5fe2161fb"></a>

```c
#define NXP_WUU_PIN_18_ANY_INT NXP_WUU_PIN(18, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_18_ANY_INT](#a3fca4746d56e2c3fb231d3f5fe2161fb)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 18 的任意边沿中断（Pin 18 any edge interrupt）。

<a id="r_aae7bce9ef1e499cc75c5902f58dbb2cc"></a>

```c
#define NXP_WUU_PIN_18_ANY_DMA NXP_WUU_PIN(18, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_18_ANY_DMA](#aae7bce9ef1e499cc75c5902f58dbb2cc)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 18 的任意边沿直接存储器访问请求（Pin 18 any edge DMA）。

<a id="r_a13ba376dcc47a4fe533aecd6bf185093"></a>

```c
#define NXP_WUU_PIN_18_ANY_TRIGGER NXP_WUU_PIN(18, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_18_ANY_TRIGGER](#a13ba376dcc47a4fe533aecd6bf185093)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 18 的任意边沿触发输出（Pin 18 any edge trigger）。

<a id="r_acefad14e0dd0c79ac4a8941980b26ccb"></a>

```c
#define NXP_WUU_PIN_19_RISING_INT NXP_WUU_PIN(19, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_19_RISING_INT](#acefad14e0dd0c79ac4a8941980b26ccb)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 19 的上升沿中断（Pin 19 rising edge interrupt）。

<a id="r_ae89a87ad6d8dae7d923594b414ce2a1b"></a>

```c
#define NXP_WUU_PIN_19_RISING_DMA NXP_WUU_PIN(19, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_19_RISING_DMA](#ae89a87ad6d8dae7d923594b414ce2a1b)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 19 的上升沿直接存储器访问请求（Pin 19 rising edge DMA）。

<a id="r_aa3f5fff1f2baf23834b71d849ae2aa36"></a>

```c
#define NXP_WUU_PIN_19_RISING_TRIGGER NXP_WUU_PIN(19, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_19_RISING_TRIGGER](#aa3f5fff1f2baf23834b71d849ae2aa36)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 19 的上升沿触发输出（Pin 19 rising edge trigger）。

<a id="r_aa150b69aa5c9806bf34267cc77b1ea68"></a>

```c
#define NXP_WUU_PIN_19_FALLING_INT NXP_WUU_PIN(19, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_19_FALLING_INT](#aa150b69aa5c9806bf34267cc77b1ea68)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 19 的下降沿中断（Pin 19 falling edge interrupt）。

<a id="r_ae5cf777820d6fae0bde68e642646c5f1"></a>

```c
#define NXP_WUU_PIN_19_FALLING_DMA NXP_WUU_PIN(19, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_19_FALLING_DMA](#ae5cf777820d6fae0bde68e642646c5f1)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 19 的下降沿直接存储器访问请求（Pin 19 falling edge DMA）。

<a id="r_a14f90ae893427011f3c797c5e28eae71"></a>

```c
#define NXP_WUU_PIN_19_FALLING_TRIGGER NXP_WUU_PIN(19, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_19_FALLING_TRIGGER](#a14f90ae893427011f3c797c5e28eae71)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 19 的下降沿触发输出（Pin 19 falling edge trigger）。

<a id="r_a17c194f87dcf310e80644e23c3cf2741"></a>

```c
#define NXP_WUU_PIN_19_ANY_INT NXP_WUU_PIN(19, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_19_ANY_INT](#a17c194f87dcf310e80644e23c3cf2741)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 19 的任意边沿中断（Pin 19 any edge interrupt）。

<a id="r_ac86a2430bd0204e4b742248f90f4e15c"></a>

```c
#define NXP_WUU_PIN_19_ANY_DMA NXP_WUU_PIN(19, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_19_ANY_DMA](#ac86a2430bd0204e4b742248f90f4e15c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 19 的任意边沿直接存储器访问请求（Pin 19 any edge DMA）。

<a id="r_a2da00e28b0cc91a12c3d3ca9dc4f0625"></a>

```c
#define NXP_WUU_PIN_19_ANY_TRIGGER NXP_WUU_PIN(19, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_19_ANY_TRIGGER](#a2da00e28b0cc91a12c3d3ca9dc4f0625)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 19 的任意边沿触发输出（Pin 19 any edge trigger）。

<a id="r_a7d46cccd96904d0136a1a1f345b1cf51"></a>

```c
#define NXP_WUU_PIN_20_RISING_INT NXP_WUU_PIN(20, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_20_RISING_INT](#a7d46cccd96904d0136a1a1f345b1cf51)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 20 的上升沿中断（Pin 20 rising edge interrupt）。

<a id="r_af44689b24c5a9f7edd05aa239d7b2bb6"></a>

```c
#define NXP_WUU_PIN_20_RISING_DMA NXP_WUU_PIN(20, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_20_RISING_DMA](#af44689b24c5a9f7edd05aa239d7b2bb6)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 20 的上升沿直接存储器访问请求（Pin 20 rising edge DMA）。

<a id="r_aacc61ba8c492295a9222d4adfa856d68"></a>

```c
#define NXP_WUU_PIN_20_RISING_TRIGGER NXP_WUU_PIN(20, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_20_RISING_TRIGGER](#aacc61ba8c492295a9222d4adfa856d68)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 20 的上升沿触发输出（Pin 20 rising edge trigger）。

<a id="r_a50d8e0138b11164b307efe9e8235d97e"></a>

```c
#define NXP_WUU_PIN_20_FALLING_INT NXP_WUU_PIN(20, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_20_FALLING_INT](#a50d8e0138b11164b307efe9e8235d97e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 20 的下降沿中断（Pin 20 falling edge interrupt）。

<a id="r_a465dcff3b9abe6ffed79c0929a187387"></a>

```c
#define NXP_WUU_PIN_20_FALLING_DMA NXP_WUU_PIN(20, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_20_FALLING_DMA](#a465dcff3b9abe6ffed79c0929a187387)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 20 的下降沿直接存储器访问请求（Pin 20 falling edge DMA）。

<a id="r_a8b48e7713c41a96a994a5f987cc00568"></a>

```c
#define NXP_WUU_PIN_20_FALLING_TRIGGER NXP_WUU_PIN(20, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_20_FALLING_TRIGGER](#a8b48e7713c41a96a994a5f987cc00568)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 20 的下降沿触发输出（Pin 20 falling edge trigger）。

<a id="r_a21faa14e3950d7af7105ab64f1643e25"></a>

```c
#define NXP_WUU_PIN_20_ANY_INT NXP_WUU_PIN(20, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_20_ANY_INT](#a21faa14e3950d7af7105ab64f1643e25)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 20 的任意边沿中断（Pin 20 any edge interrupt）。

<a id="r_af9b12c5aed07b9a498501108a2adfc77"></a>

```c
#define NXP_WUU_PIN_20_ANY_DMA NXP_WUU_PIN(20, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_20_ANY_DMA](#af9b12c5aed07b9a498501108a2adfc77)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 20 的任意边沿直接存储器访问请求（Pin 20 any edge DMA）。

<a id="r_a55df2b0445f30c848a667c73bebdd53d"></a>

```c
#define NXP_WUU_PIN_20_ANY_TRIGGER NXP_WUU_PIN(20, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_20_ANY_TRIGGER](#a55df2b0445f30c848a667c73bebdd53d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 20 的任意边沿触发输出（Pin 20 any edge trigger）。

<a id="r_a4e6e9c5c37d8aa2c4626ffb545d9278d"></a>

```c
#define NXP_WUU_PIN_21_RISING_INT NXP_WUU_PIN(21, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_21_RISING_INT](#a4e6e9c5c37d8aa2c4626ffb545d9278d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 21 的上升沿中断（Pin 21 rising edge interrupt）。

<a id="r_a16e1fc6e2a38348c0c2ce7c865015363"></a>

```c
#define NXP_WUU_PIN_21_RISING_DMA NXP_WUU_PIN(21, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_21_RISING_DMA](#a16e1fc6e2a38348c0c2ce7c865015363)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 21 的上升沿直接存储器访问请求（Pin 21 rising edge DMA）。

<a id="r_ac398816bd7222ceb960c3fe4d7830f58"></a>

```c
#define NXP_WUU_PIN_21_RISING_TRIGGER NXP_WUU_PIN(21, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_21_RISING_TRIGGER](#ac398816bd7222ceb960c3fe4d7830f58)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 21 的上升沿触发输出（Pin 21 rising edge trigger）。

<a id="r_ad51871d2a3e3e25e48663c4827e096a4"></a>

```c
#define NXP_WUU_PIN_21_FALLING_INT NXP_WUU_PIN(21, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_21_FALLING_INT](#ad51871d2a3e3e25e48663c4827e096a4)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 21 的下降沿中断（Pin 21 falling edge interrupt）。

<a id="r_a5b9ccb859e9534e2c5f020e8d52cb935"></a>

```c
#define NXP_WUU_PIN_21_FALLING_DMA NXP_WUU_PIN(21, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_21_FALLING_DMA](#a5b9ccb859e9534e2c5f020e8d52cb935)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 21 的下降沿直接存储器访问请求（Pin 21 falling edge DMA）。

<a id="r_afcda5e8e65a534d5203653460b328d3e"></a>

```c
#define NXP_WUU_PIN_21_FALLING_TRIGGER NXP_WUU_PIN(21, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_21_FALLING_TRIGGER](#afcda5e8e65a534d5203653460b328d3e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 21 的下降沿触发输出（Pin 21 falling edge trigger）。

<a id="r_ac09bc5380153996e43eff1d2fc5f5039"></a>

```c
#define NXP_WUU_PIN_21_ANY_INT NXP_WUU_PIN(21, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_21_ANY_INT](#ac09bc5380153996e43eff1d2fc5f5039)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 21 的任意边沿中断（Pin 21 any edge interrupt）。

<a id="r_a9a6d1a5da9984f594037d4835dc0ea83"></a>

```c
#define NXP_WUU_PIN_21_ANY_DMA NXP_WUU_PIN(21, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_21_ANY_DMA](#a9a6d1a5da9984f594037d4835dc0ea83)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 21 的任意边沿直接存储器访问请求（Pin 21 any edge DMA）。

<a id="r_ae4947d1f4d99207a272cfeb4f796ccdd"></a>

```c
#define NXP_WUU_PIN_21_ANY_TRIGGER NXP_WUU_PIN(21, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_21_ANY_TRIGGER](#ae4947d1f4d99207a272cfeb4f796ccdd)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 21 的任意边沿触发输出（Pin 21 any edge trigger）。

<a id="r_ab2c03c05bdc6f379d40f66b598d2da59"></a>

```c
#define NXP_WUU_PIN_22_RISING_INT NXP_WUU_PIN(22, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_22_RISING_INT](#ab2c03c05bdc6f379d40f66b598d2da59)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 22 的上升沿中断（Pin 22 rising edge interrupt）。

<a id="r_a7e1b24e4ed605b59479563c02ac0b880"></a>

```c
#define NXP_WUU_PIN_22_RISING_DMA NXP_WUU_PIN(22, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_22_RISING_DMA](#a7e1b24e4ed605b59479563c02ac0b880)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 22 的上升沿直接存储器访问请求（Pin 22 rising edge DMA）。

<a id="r_a3f2c4f4794d4a9fb4b8afa7753e4f4a6"></a>

```c
#define NXP_WUU_PIN_22_RISING_TRIGGER NXP_WUU_PIN(22, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_22_RISING_TRIGGER](#a3f2c4f4794d4a9fb4b8afa7753e4f4a6)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 22 的上升沿触发输出（Pin 22 rising edge trigger）。

<a id="r_a1295040c63fd36098b23f0b23d9cb6fc"></a>

```c
#define NXP_WUU_PIN_22_FALLING_INT NXP_WUU_PIN(22, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_22_FALLING_INT](#a1295040c63fd36098b23f0b23d9cb6fc)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 22 的下降沿中断（Pin 22 falling edge interrupt）。

<a id="r_af1290b944be74262979a8a961ef113c3"></a>

```c
#define NXP_WUU_PIN_22_FALLING_DMA NXP_WUU_PIN(22, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_22_FALLING_DMA](#af1290b944be74262979a8a961ef113c3)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 22 的下降沿直接存储器访问请求（Pin 22 falling edge DMA）。

<a id="r_a970eb9293924f98fae733a5868573ebe"></a>

```c
#define NXP_WUU_PIN_22_FALLING_TRIGGER NXP_WUU_PIN(22, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_22_FALLING_TRIGGER](#a970eb9293924f98fae733a5868573ebe)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 22 的下降沿触发输出（Pin 22 falling edge trigger）。

<a id="r_a1254db7ec52aeee3d2cd92750cc90792"></a>

```c
#define NXP_WUU_PIN_22_ANY_INT NXP_WUU_PIN(22, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_22_ANY_INT](#a1254db7ec52aeee3d2cd92750cc90792)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 22 的任意边沿中断（Pin 22 any edge interrupt）。

<a id="r_a0afc2d32673e4af3c311f1cf82f70533"></a>

```c
#define NXP_WUU_PIN_22_ANY_DMA NXP_WUU_PIN(22, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_22_ANY_DMA](#a0afc2d32673e4af3c311f1cf82f70533)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 22 的任意边沿直接存储器访问请求（Pin 22 any edge DMA）。

<a id="r_a354a1e9768d6a461868675bd29ba92ed"></a>

```c
#define NXP_WUU_PIN_22_ANY_TRIGGER NXP_WUU_PIN(22, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_22_ANY_TRIGGER](#a354a1e9768d6a461868675bd29ba92ed)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 22 的任意边沿触发输出（Pin 22 any edge trigger）。

<a id="r_a64016990a9468d96d4b8fc79f8e6bd29"></a>

```c
#define NXP_WUU_PIN_23_RISING_INT NXP_WUU_PIN(23, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_23_RISING_INT](#a64016990a9468d96d4b8fc79f8e6bd29)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 23 的上升沿中断（Pin 23 rising edge interrupt）。

<a id="r_ac46430498dea7d33e0ec4ef90da00ae5"></a>

```c
#define NXP_WUU_PIN_23_RISING_DMA NXP_WUU_PIN(23, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_23_RISING_DMA](#ac46430498dea7d33e0ec4ef90da00ae5)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 23 的上升沿直接存储器访问请求（Pin 23 rising edge DMA）。

<a id="r_ab5702a24d851ccd2e11c07a2ff755e4c"></a>

```c
#define NXP_WUU_PIN_23_RISING_TRIGGER NXP_WUU_PIN(23, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_23_RISING_TRIGGER](#ab5702a24d851ccd2e11c07a2ff755e4c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 23 的上升沿触发输出（Pin 23 rising edge trigger）。

<a id="r_a8e10c62976dce2224806798f0bd6e583"></a>

```c
#define NXP_WUU_PIN_23_FALLING_INT NXP_WUU_PIN(23, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_23_FALLING_INT](#a8e10c62976dce2224806798f0bd6e583)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 23 的下降沿中断（Pin 23 falling edge interrupt）。

<a id="r_ab58a65207d587a3d84d5cb872c053d88"></a>

```c
#define NXP_WUU_PIN_23_FALLING_DMA NXP_WUU_PIN(23, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_23_FALLING_DMA](#ab58a65207d587a3d84d5cb872c053d88)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 23 的下降沿直接存储器访问请求（Pin 23 falling edge DMA）。

<a id="r_a630d67e605e582eb0304f8cf9e0981b6"></a>

```c
#define NXP_WUU_PIN_23_FALLING_TRIGGER NXP_WUU_PIN(23, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_23_FALLING_TRIGGER](#a630d67e605e582eb0304f8cf9e0981b6)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 23 的下降沿触发输出（Pin 23 falling edge trigger）。

<a id="r_a5c4237c33652de5c60d14dd48fdd0f58"></a>

```c
#define NXP_WUU_PIN_23_ANY_INT NXP_WUU_PIN(23, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_23_ANY_INT](#a5c4237c33652de5c60d14dd48fdd0f58)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 23 的任意边沿中断（Pin 23 any edge interrupt）。

<a id="r_acf0bb6d2f6e77565dc41da3c111eba51"></a>

```c
#define NXP_WUU_PIN_23_ANY_DMA NXP_WUU_PIN(23, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_23_ANY_DMA](#acf0bb6d2f6e77565dc41da3c111eba51)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 23 的任意边沿直接存储器访问请求（Pin 23 any edge DMA）。

<a id="r_a7cfb8765eb6f361a6f5e66504f4a2815"></a>

```c
#define NXP_WUU_PIN_23_ANY_TRIGGER NXP_WUU_PIN(23, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_23_ANY_TRIGGER](#a7cfb8765eb6f361a6f5e66504f4a2815)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 23 的任意边沿触发输出（Pin 23 any edge trigger）。

<a id="r_a1ab5e383b924a0fef3f9aed083151d6c"></a>

```c
#define NXP_WUU_PIN_24_RISING_INT NXP_WUU_PIN(24, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_24_RISING_INT](#a1ab5e383b924a0fef3f9aed083151d6c)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 24 的上升沿中断（Pin 24 rising edge interrupt）。

<a id="r_a7751f13409941a48e903cc5a7bba0966"></a>

```c
#define NXP_WUU_PIN_24_RISING_DMA NXP_WUU_PIN(24, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_24_RISING_DMA](#a7751f13409941a48e903cc5a7bba0966)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 24 的上升沿直接存储器访问请求（Pin 24 rising edge DMA）。

<a id="r_aa0e41affe7b3ea661e13663833f5e928"></a>

```c
#define NXP_WUU_PIN_24_RISING_TRIGGER NXP_WUU_PIN(24, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_24_RISING_TRIGGER](#aa0e41affe7b3ea661e13663833f5e928)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 24 的上升沿触发输出（Pin 24 rising edge trigger）。

<a id="r_a99f1ae94248003598c12ce11b2b2c550"></a>

```c
#define NXP_WUU_PIN_24_FALLING_INT NXP_WUU_PIN(24, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_24_FALLING_INT](#a99f1ae94248003598c12ce11b2b2c550)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 24 的下降沿中断（Pin 24 falling edge interrupt）。

<a id="r_aa94fb06fd5e80386cb0ee7a1dd1d29b7"></a>

```c
#define NXP_WUU_PIN_24_FALLING_DMA NXP_WUU_PIN(24, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_24_FALLING_DMA](#aa94fb06fd5e80386cb0ee7a1dd1d29b7)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 24 的下降沿直接存储器访问请求（Pin 24 falling edge DMA）。

<a id="r_ae8876a7cb177ac376769375ca96a364b"></a>

```c
#define NXP_WUU_PIN_24_FALLING_TRIGGER NXP_WUU_PIN(24, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_24_FALLING_TRIGGER](#ae8876a7cb177ac376769375ca96a364b)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 24 的下降沿触发输出（Pin 24 falling edge trigger）。

<a id="r_ac32c55886098d01cebe5cabafa6c1c68"></a>

```c
#define NXP_WUU_PIN_24_ANY_INT NXP_WUU_PIN(24, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_24_ANY_INT](#ac32c55886098d01cebe5cabafa6c1c68)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 24 的任意边沿中断（Pin 24 any edge interrupt）。

<a id="r_a5c7cd136b67cd5b7e08ceeaeea4bfb76"></a>

```c
#define NXP_WUU_PIN_24_ANY_DMA NXP_WUU_PIN(24, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_24_ANY_DMA](#a5c7cd136b67cd5b7e08ceeaeea4bfb76)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 24 的任意边沿直接存储器访问请求（Pin 24 any edge DMA）。

<a id="r_a605894f98f993c88183710279574366e"></a>

```c
#define NXP_WUU_PIN_24_ANY_TRIGGER NXP_WUU_PIN(24, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_24_ANY_TRIGGER](#a605894f98f993c88183710279574366e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 24 的任意边沿触发输出（Pin 24 any edge trigger）。

<a id="r_a0786c00ff54c6f408fcc3ff842eac328"></a>

```c
#define NXP_WUU_PIN_25_RISING_INT NXP_WUU_PIN(25, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_25_RISING_INT](#a0786c00ff54c6f408fcc3ff842eac328)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 25 的上升沿中断（Pin 25 rising edge interrupt）。

<a id="r_a9587fc89dee2b403f9a1d3dc68130ccf"></a>

```c
#define NXP_WUU_PIN_25_RISING_DMA NXP_WUU_PIN(25, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_25_RISING_DMA](#a9587fc89dee2b403f9a1d3dc68130ccf)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 25 的上升沿直接存储器访问请求（Pin 25 rising edge DMA）。

<a id="r_aba6865f7ce26ae506d38900d7dc88a92"></a>

```c
#define NXP_WUU_PIN_25_RISING_TRIGGER NXP_WUU_PIN(25, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_25_RISING_TRIGGER](#aba6865f7ce26ae506d38900d7dc88a92)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 25 的上升沿触发输出（Pin 25 rising edge trigger）。

<a id="r_ac1fd771014c83ce5ef7e29a15fbdb64b"></a>

```c
#define NXP_WUU_PIN_25_FALLING_INT NXP_WUU_PIN(25, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_25_FALLING_INT](#ac1fd771014c83ce5ef7e29a15fbdb64b)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 25 的下降沿中断（Pin 25 falling edge interrupt）。

<a id="r_a0940391b22b5d240e3734a7f9b398587"></a>

```c
#define NXP_WUU_PIN_25_FALLING_DMA NXP_WUU_PIN(25, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_25_FALLING_DMA](#a0940391b22b5d240e3734a7f9b398587)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 25 的下降沿直接存储器访问请求（Pin 25 falling edge DMA）。

<a id="r_adc98eed33ab6fcbda8d85f1685aa974f"></a>

```c
#define NXP_WUU_PIN_25_FALLING_TRIGGER NXP_WUU_PIN(25, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_25_FALLING_TRIGGER](#adc98eed33ab6fcbda8d85f1685aa974f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 25 的下降沿触发输出（Pin 25 falling edge trigger）。

<a id="r_a139e6518f84f66824db9828f6487f9d2"></a>

```c
#define NXP_WUU_PIN_25_ANY_INT NXP_WUU_PIN(25, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_25_ANY_INT](#a139e6518f84f66824db9828f6487f9d2)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 25 的任意边沿中断（Pin 25 any edge interrupt）。

<a id="r_af17e95c7f7e74e995038066f9bc4ba6f"></a>

```c
#define NXP_WUU_PIN_25_ANY_DMA NXP_WUU_PIN(25, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_25_ANY_DMA](#af17e95c7f7e74e995038066f9bc4ba6f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 25 的任意边沿直接存储器访问请求（Pin 25 any edge DMA）。

<a id="r_afd282674c01bc2218a84cbe8b551cd04"></a>

```c
#define NXP_WUU_PIN_25_ANY_TRIGGER NXP_WUU_PIN(25, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_25_ANY_TRIGGER](#afd282674c01bc2218a84cbe8b551cd04)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 25 的任意边沿触发输出（Pin 25 any edge trigger）。

<a id="r_a4d8f9a42d5a9f22033f48d3ff3deb574"></a>

```c
#define NXP_WUU_PIN_26_RISING_INT NXP_WUU_PIN(26, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_26_RISING_INT](#a4d8f9a42d5a9f22033f48d3ff3deb574)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 26 的上升沿中断（Pin 26 rising edge interrupt）。

<a id="r_a260eeba3c8c0882c045d036fc469fc5d"></a>

```c
#define NXP_WUU_PIN_26_RISING_DMA NXP_WUU_PIN(26, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_26_RISING_DMA](#a260eeba3c8c0882c045d036fc469fc5d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 26 的上升沿直接存储器访问请求（Pin 26 rising edge DMA）。

<a id="r_a32b96187402f13717c590b3d595b66e4"></a>

```c
#define NXP_WUU_PIN_26_RISING_TRIGGER NXP_WUU_PIN(26, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_26_RISING_TRIGGER](#a32b96187402f13717c590b3d595b66e4)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 26 的上升沿触发输出（Pin 26 rising edge trigger）。

<a id="r_a7cb27974779a15abcb6f7ef2ca584fc0"></a>

```c
#define NXP_WUU_PIN_26_FALLING_INT NXP_WUU_PIN(26, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_26_FALLING_INT](#a7cb27974779a15abcb6f7ef2ca584fc0)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 26 的下降沿中断（Pin 26 falling edge interrupt）。

<a id="r_af2f6c44e0a4f87b095c849244d7bc591"></a>

```c
#define NXP_WUU_PIN_26_FALLING_DMA NXP_WUU_PIN(26, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_26_FALLING_DMA](#af2f6c44e0a4f87b095c849244d7bc591)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 26 的下降沿直接存储器访问请求（Pin 26 falling edge DMA）。

<a id="r_a6136f467e9c3045e4c2b5cb53e5f6c33"></a>

```c
#define NXP_WUU_PIN_26_FALLING_TRIGGER NXP_WUU_PIN(26, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_26_FALLING_TRIGGER](#a6136f467e9c3045e4c2b5cb53e5f6c33)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 26 的下降沿触发输出（Pin 26 falling edge trigger）。

<a id="r_a8732cc560348b8b6a8887bd1689a1c91"></a>

```c
#define NXP_WUU_PIN_26_ANY_INT NXP_WUU_PIN(26, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_26_ANY_INT](#a8732cc560348b8b6a8887bd1689a1c91)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 26 的任意边沿中断（Pin 26 any edge interrupt）。

<a id="r_ad38b8b9c677732abbea0e203c4d48496"></a>

```c
#define NXP_WUU_PIN_26_ANY_DMA NXP_WUU_PIN(26, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_26_ANY_DMA](#ad38b8b9c677732abbea0e203c4d48496)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 26 的任意边沿直接存储器访问请求（Pin 26 any edge DMA）。

<a id="r_a5a9f75686c4bd3072b24a7ccebe35c96"></a>

```c
#define NXP_WUU_PIN_26_ANY_TRIGGER NXP_WUU_PIN(26, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_26_ANY_TRIGGER](#a5a9f75686c4bd3072b24a7ccebe35c96)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 26 的任意边沿触发输出（Pin 26 any edge trigger）。

<a id="r_a8f087bc8cecd70c7c0d9d10bddef9f6f"></a>

```c
#define NXP_WUU_PIN_27_RISING_INT NXP_WUU_PIN(27, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_27_RISING_INT](#a8f087bc8cecd70c7c0d9d10bddef9f6f)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 27 的上升沿中断（Pin 27 rising edge interrupt）。

<a id="r_a389b6e9c46ff420a8ca3a902b4743b3e"></a>

```c
#define NXP_WUU_PIN_27_RISING_DMA NXP_WUU_PIN(27, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_27_RISING_DMA](#a389b6e9c46ff420a8ca3a902b4743b3e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 27 的上升沿直接存储器访问请求（Pin 27 rising edge DMA）。

<a id="r_ae1666594469d6bef7bf295b9c5d42f3d"></a>

```c
#define NXP_WUU_PIN_27_RISING_TRIGGER NXP_WUU_PIN(27, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_27_RISING_TRIGGER](#ae1666594469d6bef7bf295b9c5d42f3d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 27 的上升沿触发输出（Pin 27 rising edge trigger）。

<a id="r_ab19c0a16839e7f71715fe97e54a31cfc"></a>

```c
#define NXP_WUU_PIN_27_FALLING_INT NXP_WUU_PIN(27, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_27_FALLING_INT](#ab19c0a16839e7f71715fe97e54a31cfc)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 27 的下降沿中断（Pin 27 falling edge interrupt）。

<a id="r_ae5cc3af8b9457232d775a1afb3e45efa"></a>

```c
#define NXP_WUU_PIN_27_FALLING_DMA NXP_WUU_PIN(27, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_27_FALLING_DMA](#ae5cc3af8b9457232d775a1afb3e45efa)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 27 的下降沿直接存储器访问请求（Pin 27 falling edge DMA）。

<a id="r_ab5559e1f172eec039d58c1df7fd9b648"></a>

```c
#define NXP_WUU_PIN_27_FALLING_TRIGGER NXP_WUU_PIN(27, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_27_FALLING_TRIGGER](#ab5559e1f172eec039d58c1df7fd9b648)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 27 的下降沿触发输出（Pin 27 falling edge trigger）。

<a id="r_a7b69faca62fc98fddb82729372cda153"></a>

```c
#define NXP_WUU_PIN_27_ANY_INT NXP_WUU_PIN(27, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_27_ANY_INT](#a7b69faca62fc98fddb82729372cda153)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 27 的任意边沿中断（Pin 27 any edge interrupt）。

<a id="r_af2f89438834c13f535e22cfdfbcddd60"></a>

```c
#define NXP_WUU_PIN_27_ANY_DMA NXP_WUU_PIN(27, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_27_ANY_DMA](#af2f89438834c13f535e22cfdfbcddd60)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 27 的任意边沿直接存储器访问请求（Pin 27 any edge DMA）。

<a id="r_a72448223dd0baaa22f5a2e37482e8d90"></a>

```c
#define NXP_WUU_PIN_27_ANY_TRIGGER NXP_WUU_PIN(27, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_27_ANY_TRIGGER](#a72448223dd0baaa22f5a2e37482e8d90)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 27 的任意边沿触发输出（Pin 27 any edge trigger）。

<a id="r_ae61a7794b5274fc6b0fddd24b3786f79"></a>

```c
#define NXP_WUU_PIN_28_RISING_INT NXP_WUU_PIN(28, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_28_RISING_INT](#ae61a7794b5274fc6b0fddd24b3786f79)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 28 的上升沿中断（Pin 28 rising edge interrupt）。

<a id="r_ac147e54729e572ac5740a1fb2132c822"></a>

```c
#define NXP_WUU_PIN_28_RISING_DMA NXP_WUU_PIN(28, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_28_RISING_DMA](#ac147e54729e572ac5740a1fb2132c822)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 28 的上升沿直接存储器访问请求（Pin 28 rising edge DMA）。

<a id="r_aa9397ac0890139885bc6b23615082215"></a>

```c
#define NXP_WUU_PIN_28_RISING_TRIGGER NXP_WUU_PIN(28, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_28_RISING_TRIGGER](#aa9397ac0890139885bc6b23615082215)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 28 的上升沿触发输出（Pin 28 rising edge trigger）。

<a id="r_a90df0c72e3dc2dca3a57ea50c47e64dd"></a>

```c
#define NXP_WUU_PIN_28_FALLING_INT NXP_WUU_PIN(28, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_28_FALLING_INT](#a90df0c72e3dc2dca3a57ea50c47e64dd)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 28 的下降沿中断（Pin 28 falling edge interrupt）。

<a id="r_aa06cba2ca497e50592bef33a20e387ea"></a>

```c
#define NXP_WUU_PIN_28_FALLING_DMA NXP_WUU_PIN(28, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_28_FALLING_DMA](#aa06cba2ca497e50592bef33a20e387ea)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 28 的下降沿直接存储器访问请求（Pin 28 falling edge DMA）。

<a id="r_ad1094a23e6b230e43da3f2c40928d406"></a>

```c
#define NXP_WUU_PIN_28_FALLING_TRIGGER NXP_WUU_PIN(28, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_28_FALLING_TRIGGER](#ad1094a23e6b230e43da3f2c40928d406)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 28 的下降沿触发输出（Pin 28 falling edge trigger）。

<a id="r_adfb27b752ecd7c96a9ab2fcf855e024e"></a>

```c
#define NXP_WUU_PIN_28_ANY_INT NXP_WUU_PIN(28, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_28_ANY_INT](#adfb27b752ecd7c96a9ab2fcf855e024e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 28 的任意边沿中断（Pin 28 any edge interrupt）。

<a id="r_a347c8dad3efc35f5ff3376c987713461"></a>

```c
#define NXP_WUU_PIN_28_ANY_DMA NXP_WUU_PIN(28, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_28_ANY_DMA](#a347c8dad3efc35f5ff3376c987713461)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 28 的任意边沿直接存储器访问请求（Pin 28 any edge DMA）。

<a id="r_a602c954cc1a534f75601d821d1059b8d"></a>

```c
#define NXP_WUU_PIN_28_ANY_TRIGGER NXP_WUU_PIN(28, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_28_ANY_TRIGGER](#a602c954cc1a534f75601d821d1059b8d)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 28 的任意边沿触发输出（Pin 28 any edge trigger）。

<a id="r_ae038b3a246101fa06346d4d6c409306e"></a>

```c
#define NXP_WUU_PIN_29_RISING_INT NXP_WUU_PIN(29, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_29_RISING_INT](#ae038b3a246101fa06346d4d6c409306e)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 29 的上升沿中断（Pin 29 rising edge interrupt）。

<a id="r_aa8aa9d173cb3d631d02d56fc1633f948"></a>

```c
#define NXP_WUU_PIN_29_RISING_DMA NXP_WUU_PIN(29, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_29_RISING_DMA](#aa8aa9d173cb3d631d02d56fc1633f948)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 29 的上升沿直接存储器访问请求（Pin 29 rising edge DMA）。

<a id="r_a0531e427d93d586fa8d959c5d8550d56"></a>

```c
#define NXP_WUU_PIN_29_RISING_TRIGGER NXP_WUU_PIN(29, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_29_RISING_TRIGGER](#a0531e427d93d586fa8d959c5d8550d56)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 29 的上升沿触发输出（Pin 29 rising edge trigger）。

<a id="r_a943872b62aef9bcb3fb1c9ffcc227535"></a>

```c
#define NXP_WUU_PIN_29_FALLING_INT NXP_WUU_PIN(29, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_29_FALLING_INT](#a943872b62aef9bcb3fb1c9ffcc227535)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 29 的下降沿中断（Pin 29 falling edge interrupt）。

<a id="r_a24c5047eedac8ea7317f21b5a187c508"></a>

```c
#define NXP_WUU_PIN_29_FALLING_DMA NXP_WUU_PIN(29, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_29_FALLING_DMA](#a24c5047eedac8ea7317f21b5a187c508)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 29 的下降沿直接存储器访问请求（Pin 29 falling edge DMA）。

<a id="r_abe948ad4554aaba19d1acaedc28ac9eb"></a>

```c
#define NXP_WUU_PIN_29_FALLING_TRIGGER NXP_WUU_PIN(29, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_29_FALLING_TRIGGER](#abe948ad4554aaba19d1acaedc28ac9eb)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 29 的下降沿触发输出（Pin 29 falling edge trigger）。

<a id="r_a2294c7fcf8124f0e97f461dba7a459fe"></a>

```c
#define NXP_WUU_PIN_29_ANY_INT NXP_WUU_PIN(29, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_29_ANY_INT](#a2294c7fcf8124f0e97f461dba7a459fe)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 29 的任意边沿中断（Pin 29 any edge interrupt）。

<a id="r_a36a0c5f7e40f432348a1119d5772d5ec"></a>

```c
#define NXP_WUU_PIN_29_ANY_DMA NXP_WUU_PIN(29, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_29_ANY_DMA](#a36a0c5f7e40f432348a1119d5772d5ec)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 29 的任意边沿直接存储器访问请求（Pin 29 any edge DMA）。

<a id="r_ae938a8480eecd7aff325dbadef529fbf"></a>

```c
#define NXP_WUU_PIN_29_ANY_TRIGGER NXP_WUU_PIN(29, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_29_ANY_TRIGGER](#ae938a8480eecd7aff325dbadef529fbf)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 29 的任意边沿触发输出（Pin 29 any edge trigger）。

<a id="r_a66ccadf7c0cc89fd90f559c28efe6f8a"></a>

```c
#define NXP_WUU_PIN_30_RISING_INT NXP_WUU_PIN(30, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_30_RISING_INT](#a66ccadf7c0cc89fd90f559c28efe6f8a)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 30 的上升沿中断（Pin 30 rising edge interrupt）。

<a id="r_a656177c37d72970453a788b931f27f30"></a>

```c
#define NXP_WUU_PIN_30_RISING_DMA NXP_WUU_PIN(30, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_30_RISING_DMA](#a656177c37d72970453a788b931f27f30)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 30 的上升沿直接存储器访问请求（Pin 30 rising edge DMA）。

<a id="r_a99b22a9abb8a1b5cd76dad1cce2566fc"></a>

```c
#define NXP_WUU_PIN_30_RISING_TRIGGER NXP_WUU_PIN(30, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_30_RISING_TRIGGER](#a99b22a9abb8a1b5cd76dad1cce2566fc)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 30 的上升沿触发输出（Pin 30 rising edge trigger）。

<a id="r_a0ca83ab747500f453b0e88a918482546"></a>

```c
#define NXP_WUU_PIN_30_FALLING_INT NXP_WUU_PIN(30, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_30_FALLING_INT](#a0ca83ab747500f453b0e88a918482546)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 30 的下降沿中断（Pin 30 falling edge interrupt）。

<a id="r_a10f8ad477d538497b07923b2dd3d4d6a"></a>

```c
#define NXP_WUU_PIN_30_FALLING_DMA NXP_WUU_PIN(30, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_30_FALLING_DMA](#a10f8ad477d538497b07923b2dd3d4d6a)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 30 的下降沿直接存储器访问请求（Pin 30 falling edge DMA）。

<a id="r_ae457b538bc805cd2a25202457efd4ecf"></a>

```c
#define NXP_WUU_PIN_30_FALLING_TRIGGER NXP_WUU_PIN(30, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_30_FALLING_TRIGGER](#ae457b538bc805cd2a25202457efd4ecf)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 30 的下降沿触发输出（Pin 30 falling edge trigger）。

<a id="r_ab922f612cafced3392ec6d8809c5f8ee"></a>

```c
#define NXP_WUU_PIN_30_ANY_INT NXP_WUU_PIN(30, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_30_ANY_INT](#ab922f612cafced3392ec6d8809c5f8ee)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 30 的任意边沿中断（Pin 30 any edge interrupt）。

<a id="r_a3eea2af7b44504449adf6e19dce9a591"></a>

```c
#define NXP_WUU_PIN_30_ANY_DMA NXP_WUU_PIN(30, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_30_ANY_DMA](#a3eea2af7b44504449adf6e19dce9a591)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 30 的任意边沿直接存储器访问请求（Pin 30 any edge DMA）。

<a id="r_ad984888d667e38c0d527da6b848554b3"></a>

```c
#define NXP_WUU_PIN_30_ANY_TRIGGER NXP_WUU_PIN(30, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_30_ANY_TRIGGER](#ad984888d667e38c0d527da6b848554b3)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 30 的任意边沿触发输出（Pin 30 any edge trigger）。

<a id="r_abeb326af95c992cb7a4777e80c069e11"></a>

```c
#define NXP_WUU_PIN_31_RISING_INT NXP_WUU_PIN(31, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_31_RISING_INT](#abeb326af95c992cb7a4777e80c069e11)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 31 的上升沿中断（Pin 31 rising edge interrupt）。

<a id="r_abdbc6eae346325c5bde7267425951dce"></a>

```c
#define NXP_WUU_PIN_31_RISING_DMA NXP_WUU_PIN(31, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_31_RISING_DMA](#abdbc6eae346325c5bde7267425951dce)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 31 的上升沿直接存储器访问请求（Pin 31 rising edge DMA）。

<a id="r_a780acac9ae801d0fa9470d8779dfe399"></a>

```c
#define NXP_WUU_PIN_31_RISING_TRIGGER NXP_WUU_PIN(31, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_31_RISING_TRIGGER](#a780acac9ae801d0fa9470d8779dfe399)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_RISING](#a86b796473da951cea7729ccee32bc7fe)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 31 的上升沿触发输出（Pin 31 rising edge trigger）。

<a id="r_a4e442cd96c8ab316262369f3d5fdb979"></a>

```c
#define NXP_WUU_PIN_31_FALLING_INT NXP_WUU_PIN(31, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_31_FALLING_INT](#a4e442cd96c8ab316262369f3d5fdb979)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 31 的下降沿中断（Pin 31 falling edge interrupt）。

<a id="r_a2bad33398fd39840a96814846ee09bf0"></a>

```c
#define NXP_WUU_PIN_31_FALLING_DMA NXP_WUU_PIN(31, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_31_FALLING_DMA](#a2bad33398fd39840a96814846ee09bf0)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 31 的下降沿直接存储器访问请求（Pin 31 falling edge DMA）。

<a id="r_a8f0010fbc10ba1db35c14688a9acfd25"></a>

```c
#define NXP_WUU_PIN_31_FALLING_TRIGGER NXP_WUU_PIN(31, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_31_FALLING_TRIGGER](#a8f0010fbc10ba1db35c14688a9acfd25)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_FALLING](#aebd1e16cc9fc9b95d4fcbfd01ff29bb7)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 31 的下降沿触发输出（Pin 31 falling edge trigger）。

<a id="r_aa2000a701abe50eaed661369cb766a86"></a>

```c
#define NXP_WUU_PIN_31_ANY_INT NXP_WUU_PIN(31, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

相关声明：[NXP_WUU_PIN_31_ANY_INT](#aa2000a701abe50eaed661369cb766a86)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_INT](#af49b722882785c60e2b88997b1dac2b9)。

引脚 31 的任意边沿中断（Pin 31 any edge interrupt）。

<a id="r_a517f82f1fbcdfa4e21e7053bad48adad"></a>

```c
#define NXP_WUU_PIN_31_ANY_DMA NXP_WUU_PIN(31, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

相关声明：[NXP_WUU_PIN_31_ANY_DMA](#a517f82f1fbcdfa4e21e7053bad48adad)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_DMA](#a07bbe18c99de81f08ae2ea3e99a6cb6a)。

引脚 31 的任意边沿直接存储器访问请求（Pin 31 any edge DMA）。

<a id="r_a532c12001131d9de5f8acecce5c095b5"></a>

```c
#define NXP_WUU_PIN_31_ANY_TRIGGER NXP_WUU_PIN(31, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

相关声明：[NXP_WUU_PIN_31_ANY_TRIGGER](#a532c12001131d9de5f8acecce5c095b5)、[NXP_WUU_PIN](#a454f7e196452951dcbc613d9f556c0df)、[NXP_WUU_EDGE_ANY](#a6bb0fc2b85ec01be981e88851522a968)、[NXP_WUU_EVENT_TRIGGER](#a7a870a5d4b66572d17017ceae38214b4)。

引脚 31 的任意边沿触发输出（Pin 31 any edge trigger）。

## 7.2\_详细说明（Detailed Documentation）

<a id="a6bb0fc2b85ec01be981e88851522a968"></a>

### `NXP_WUU_EDGE_ANY`

```c
#define NXP_WUU_EDGE_ANY 3
```

边沿类型值（Edge-type Value）：任意边沿触发。

<a id="aebd1e16cc9fc9b95d4fcbfd01ff29bb7"></a>

### `NXP_WUU_EDGE_FALLING`

```c
#define NXP_WUU_EDGE_FALLING 2
```

边沿类型值（Edge-type Value）：下降沿触发。

<a id="a86b796473da951cea7729ccee32bc7fe"></a>

### `NXP_WUU_EDGE_RISING`

```c
#define NXP_WUU_EDGE_RISING 1
```

边沿类型值（Edge-type Value）：上升沿触发。

<a id="a07bbe18c99de81f08ae2ea3e99a6cb6a"></a>

### `NXP_WUU_EVENT_DMA`

```c
#define NXP_WUU_EVENT_DMA 1
```

事件类型值（Event-type Value）：以 DMA 请求形式传递。

<a id="af49b722882785c60e2b88997b1dac2b9"></a>

### `NXP_WUU_EVENT_INT`

```c
#define NXP_WUU_EVENT_INT 0
```

事件类型值（Event-type Value）：以中断形式传递。

<a id="a7a870a5d4b66572d17017ceae38214b4"></a>

### `NXP_WUU_EVENT_TRIGGER`

```c
#define NXP_WUU_EVENT_TRIGGER 2
```

事件类型值（Event-type Value）：以触发输出形式传递。

<a id="a332d40d6fbb7cab51791d74f34ed40da"></a>

### `NXP_WUU_IS_MODULE_SOURCE`

```c
#define NXP_WUU_IS_MODULE_SOURCE ( source)
```

展开值（Value）：

```c
(NXP_WUU_WAKEUP_SOURCE_DECODE_TYPE(source) == NXP_WUU_SOURCE_TYPE_MODULE)
```

判断编码唤醒源是否描述模块源（MODULE Source）。

<a id="ac8164cc2868fc8edea50395064a6757b"></a>

### `NXP_WUU_IS_PIN_SOURCE`

```c
#define NXP_WUU_IS_PIN_SOURCE ( source)
```

展开值（Value）：

```c
(NXP_WUU_WAKEUP_SOURCE_DECODE_TYPE(source) == NXP_WUU_SOURCE_TYPE_PIN)
```

判断编码唤醒源是否描述引脚源（PIN Source）。

<a id="afaff4a945c102da5d4abf0e04b13e6db"></a>

### `NXP_WUU_MODULE`

```c
#define NXP_WUU_MODULE ( index, event )
```

展开值（Value）：

```c
NXP_WUU_WAKEUP_SOURCE_ENCODE(NXP_WUU_SOURCE_TYPE_MODULE, index, 0, event)
```

模块唤醒源（MODULE Wakeup Sources）的辅助宏。

<a id="a5cb70820614b17bd8abcc529e887c1ed"></a>

### `NXP_WUU_MODULE_0_DMA`

```c
#define NXP_WUU_MODULE_0_DMA NXP_WUU_MODULE(0, NXP_WUU_EVENT_DMA)
```

模块 0 的直接存储器访问请求事件（Module 0 DMA event）。

<a id="aeb2b5d1be20f3d7039542df5aa7efb81"></a>

### `NXP_WUU_MODULE_0_INT`

```c
#define NXP_WUU_MODULE_0_INT NXP_WUU_MODULE(0, NXP_WUU_EVENT_INT)
```

WUU 支持的内部模块（Internal Modules）。

模块 0 的中断事件（Module 0 interrupt event）。

<a id="a12dacee6e2133b8acb605b445b07166f"></a>

### `NXP_WUU_MODULE_1_DMA`

```c
#define NXP_WUU_MODULE_1_DMA NXP_WUU_MODULE(1, NXP_WUU_EVENT_DMA)
```

模块 1 的直接存储器访问请求事件（Module 1 DMA event）。

<a id="ac2f3a4f24d4ca6daa73d57ac0b683d45"></a>

### `NXP_WUU_MODULE_1_INT`

```c
#define NXP_WUU_MODULE_1_INT NXP_WUU_MODULE(1, NXP_WUU_EVENT_INT)
```

模块 1 的中断事件（Module 1 interrupt event）。

<a id="a08893ac4841a0ee78f5f288d53712d3d"></a>

### `NXP_WUU_MODULE_2_DMA`

```c
#define NXP_WUU_MODULE_2_DMA NXP_WUU_MODULE(2, NXP_WUU_EVENT_DMA)
```

模块 2 的直接存储器访问请求事件（Module 2 DMA event）。

<a id="a3ec96a49fd44b5ea9c33c82836f6a098"></a>

### `NXP_WUU_MODULE_2_INT`

```c
#define NXP_WUU_MODULE_2_INT NXP_WUU_MODULE(2, NXP_WUU_EVENT_INT)
```

模块 2 的中断事件（Module 2 interrupt event）。

<a id="a55b29249adf66470825dc044b0246b85"></a>

### `NXP_WUU_MODULE_3_DMA`

```c
#define NXP_WUU_MODULE_3_DMA NXP_WUU_MODULE(3, NXP_WUU_EVENT_DMA)
```

模块 3 的直接存储器访问请求事件（Module 3 DMA event）。

<a id="a8f0c44f30e63ae6d3e1453bb18bb8646"></a>

### `NXP_WUU_MODULE_3_INT`

```c
#define NXP_WUU_MODULE_3_INT NXP_WUU_MODULE(3, NXP_WUU_EVENT_INT)
```

模块 3 的中断事件（Module 3 interrupt event）。

<a id="a8df95e502cf1ce7fe512e422c2a7a883"></a>

### `NXP_WUU_MODULE_4_DMA`

```c
#define NXP_WUU_MODULE_4_DMA NXP_WUU_MODULE(4, NXP_WUU_EVENT_DMA)
```

模块 4 的直接存储器访问请求事件（Module 4 DMA event）。

<a id="a0b548b00c2bae479ccb64dfca49096d3"></a>

### `NXP_WUU_MODULE_4_INT`

```c
#define NXP_WUU_MODULE_4_INT NXP_WUU_MODULE(4, NXP_WUU_EVENT_INT)
```

模块 4 的中断事件（Module 4 interrupt event）。

<a id="add2dc5d80f1b479e3f746565bc8bc966"></a>

### `NXP_WUU_MODULE_5_DMA`

```c
#define NXP_WUU_MODULE_5_DMA NXP_WUU_MODULE(5, NXP_WUU_EVENT_DMA)
```

模块 5 的直接存储器访问请求事件（Module 5 DMA event）。

<a id="a97bcc7c02461cdbc7e45ad16cd6584f1"></a>

### `NXP_WUU_MODULE_5_INT`

```c
#define NXP_WUU_MODULE_5_INT NXP_WUU_MODULE(5, NXP_WUU_EVENT_INT)
```

模块 5 的中断事件（Module 5 interrupt event）。

<a id="a4b1b3295f21a1f302a8c3021c44af333"></a>

### `NXP_WUU_MODULE_6_DMA`

```c
#define NXP_WUU_MODULE_6_DMA NXP_WUU_MODULE(6, NXP_WUU_EVENT_DMA)
```

模块 6 的直接存储器访问请求事件（Module 6 DMA event）。

<a id="ad75f431f6530daef607df0b66a3ca55e"></a>

### `NXP_WUU_MODULE_6_INT`

```c
#define NXP_WUU_MODULE_6_INT NXP_WUU_MODULE(6, NXP_WUU_EVENT_INT)
```

模块 6 的中断事件（Module 6 interrupt event）。

<a id="a361dd458bd1f5301d0545d811725b6f6"></a>

### `NXP_WUU_MODULE_7_DMA`

```c
#define NXP_WUU_MODULE_7_DMA NXP_WUU_MODULE(7, NXP_WUU_EVENT_DMA)
```

模块 7 的直接存储器访问请求事件（Module 7 DMA event）。

<a id="a67067fe3faf13b176c031b168aafe8eb"></a>

### `NXP_WUU_MODULE_7_INT`

```c
#define NXP_WUU_MODULE_7_INT NXP_WUU_MODULE(7, NXP_WUU_EVENT_INT)
```

模块 7 的中断事件（Module 7 interrupt event）。

<a id="aa2335d42e9540087a553c12004103d65"></a>

### `NXP_WUU_MODULE_8_DMA`

```c
#define NXP_WUU_MODULE_8_DMA NXP_WUU_MODULE(8, NXP_WUU_EVENT_DMA)
```

模块 8 的直接存储器访问请求事件（Module 8 DMA event）。

<a id="aa2770d71d20d9020fe3c3a9e5fb5aefa"></a>

### `NXP_WUU_MODULE_8_INT`

```c
#define NXP_WUU_MODULE_8_INT NXP_WUU_MODULE(8, NXP_WUU_EVENT_INT)
```

模块 8 的中断事件（Module 8 interrupt event）。

<a id="a454f7e196452951dcbc613d9f556c0df"></a>

### `NXP_WUU_PIN`

```c
#define NXP_WUU_PIN ( index, edge, event )
```

展开值（Value）：

```c
NXP_WUU_WAKEUP_SOURCE_ENCODE(NXP_WUU_SOURCE_TYPE_PIN, index, edge, event)
```

引脚唤醒源（PIN Wakeup Sources）的辅助宏。

<a id="afe9e7a04f92034a4d9288e2b49e595ab"></a>

### `NXP_WUU_PIN_0_ANY_DMA`

```c
#define NXP_WUU_PIN_0_ANY_DMA NXP_WUU_PIN(0, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 0 的任意边沿直接存储器访问请求（Pin 0 any edge DMA）。

<a id="a84566bb8afb43b70f438ba31a3ddabe1"></a>

### `NXP_WUU_PIN_0_ANY_INT`

```c
#define NXP_WUU_PIN_0_ANY_INT NXP_WUU_PIN(0, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 0 的任意边沿中断（Pin 0 any edge interrupt）。

<a id="a05f73c8cb789760efcc6d076552fb00f"></a>

### `NXP_WUU_PIN_0_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_0_ANY_TRIGGER NXP_WUU_PIN(0, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 0 的任意边沿触发输出（Pin 0 any edge trigger）。

<a id="adee8759a9241a0f7af2476c52471e552"></a>

### `NXP_WUU_PIN_0_FALLING_DMA`

```c
#define NXP_WUU_PIN_0_FALLING_DMA NXP_WUU_PIN(0, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 0 的下降沿直接存储器访问请求（Pin 0 falling edge DMA）。

<a id="a0b46e5fd76565651af24a69d8f3d399d"></a>

### `NXP_WUU_PIN_0_FALLING_INT`

```c
#define NXP_WUU_PIN_0_FALLING_INT NXP_WUU_PIN(0, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 0 的下降沿中断（Pin 0 falling edge interrupt）。

<a id="ab6b631213c89af5dda08e98f5d915cf2"></a>

### `NXP_WUU_PIN_0_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_0_FALLING_TRIGGER NXP_WUU_PIN(0, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 0 的下降沿触发输出（Pin 0 falling edge trigger）。

<a id="a892bedc667e76defef7cc16404bb3a38"></a>

### `NXP_WUU_PIN_0_RISING_DMA`

```c
#define NXP_WUU_PIN_0_RISING_DMA NXP_WUU_PIN(0, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 0 的上升沿直接存储器访问请求（Pin 0 rising edge DMA）。

<a id="a45864288bc9595f24b31c07669cb7677"></a>

### `NXP_WUU_PIN_0_RISING_INT`

```c
#define NXP_WUU_PIN_0_RISING_INT NXP_WUU_PIN(0, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

WUU 引脚唤醒源（PIN Wakeup Sources）。

引脚 0 的上升沿中断（Pin 0 rising edge interrupt）。

<a id="ae57af895036fef4497730cd13318cbf4"></a>

### `NXP_WUU_PIN_0_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_0_RISING_TRIGGER NXP_WUU_PIN(0, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 0 的上升沿触发输出（Pin 0 rising edge trigger）。

<a id="ac5486ff7b60fdf52ff4c7b327eb6c2bd"></a>

### `NXP_WUU_PIN_10_ANY_DMA`

```c
#define NXP_WUU_PIN_10_ANY_DMA NXP_WUU_PIN(10, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 10 的任意边沿直接存储器访问请求（Pin 10 any edge DMA）。

<a id="a668ec7bafdbe61838dfee115e0e86208"></a>

### `NXP_WUU_PIN_10_ANY_INT`

```c
#define NXP_WUU_PIN_10_ANY_INT NXP_WUU_PIN(10, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 10 的任意边沿中断（Pin 10 any edge interrupt）。

<a id="a7c3057491ef9f1d8487f96bd766bedc9"></a>

### `NXP_WUU_PIN_10_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_10_ANY_TRIGGER NXP_WUU_PIN(10, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 10 的任意边沿触发输出（Pin 10 any edge trigger）。

<a id="a36c7b24f0f53a1ed0601773bc47a0e37"></a>

### `NXP_WUU_PIN_10_FALLING_DMA`

```c
#define NXP_WUU_PIN_10_FALLING_DMA NXP_WUU_PIN(10, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 10 的下降沿直接存储器访问请求（Pin 10 falling edge DMA）。

<a id="a44fc0203ca3f908027e1da3a006c219d"></a>

### `NXP_WUU_PIN_10_FALLING_INT`

```c
#define NXP_WUU_PIN_10_FALLING_INT NXP_WUU_PIN(10, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 10 的下降沿中断（Pin 10 falling edge interrupt）。

<a id="a5181167cba5b94fb7e075d615bb01040"></a>

### `NXP_WUU_PIN_10_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_10_FALLING_TRIGGER NXP_WUU_PIN(10, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 10 的下降沿触发输出（Pin 10 falling edge trigger）。

<a id="ab539e1019273d63bb8d270f3c1a0956a"></a>

### `NXP_WUU_PIN_10_RISING_DMA`

```c
#define NXP_WUU_PIN_10_RISING_DMA NXP_WUU_PIN(10, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 10 的上升沿直接存储器访问请求（Pin 10 rising edge DMA）。

<a id="a8447381ee6c0599fb994fb3f5db3beda"></a>

### `NXP_WUU_PIN_10_RISING_INT`

```c
#define NXP_WUU_PIN_10_RISING_INT NXP_WUU_PIN(10, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 10 的上升沿中断（Pin 10 rising edge interrupt）。

<a id="a0c66facf2f0bffe4015bf4c30bf617d0"></a>

### `NXP_WUU_PIN_10_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_10_RISING_TRIGGER NXP_WUU_PIN(10, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 10 的上升沿触发输出（Pin 10 rising edge trigger）。

<a id="af94fd967bca069c116239a3cc471bb56"></a>

### `NXP_WUU_PIN_11_ANY_DMA`

```c
#define NXP_WUU_PIN_11_ANY_DMA NXP_WUU_PIN(11, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 11 的任意边沿直接存储器访问请求（Pin 11 any edge DMA）。

<a id="ab12bbe55fea8a0bfafe71b59d8e320c1"></a>

### `NXP_WUU_PIN_11_ANY_INT`

```c
#define NXP_WUU_PIN_11_ANY_INT NXP_WUU_PIN(11, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 11 的任意边沿中断（Pin 11 any edge interrupt）。

<a id="aa3d45d4578fcaaffd4a63eafe5fcbc27"></a>

### `NXP_WUU_PIN_11_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_11_ANY_TRIGGER NXP_WUU_PIN(11, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 11 的任意边沿触发输出（Pin 11 any edge trigger）。

<a id="a79a3941da6becd8574f5dfa9ecef7f68"></a>

### `NXP_WUU_PIN_11_FALLING_DMA`

```c
#define NXP_WUU_PIN_11_FALLING_DMA NXP_WUU_PIN(11, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 11 的下降沿直接存储器访问请求（Pin 11 falling edge DMA）。

<a id="afb3ceace195d922f281453b98e614b8a"></a>

### `NXP_WUU_PIN_11_FALLING_INT`

```c
#define NXP_WUU_PIN_11_FALLING_INT NXP_WUU_PIN(11, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 11 的下降沿中断（Pin 11 falling edge interrupt）。

<a id="a23fa65ed5cc4da49c4c0629d26cab10c"></a>

### `NXP_WUU_PIN_11_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_11_FALLING_TRIGGER NXP_WUU_PIN(11, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 11 的下降沿触发输出（Pin 11 falling edge trigger）。

<a id="a18654f13ee61ea9978a5a4cacbaf7cd1"></a>

### `NXP_WUU_PIN_11_RISING_DMA`

```c
#define NXP_WUU_PIN_11_RISING_DMA NXP_WUU_PIN(11, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 11 的上升沿直接存储器访问请求（Pin 11 rising edge DMA）。

<a id="af8db9d843713d811f292739fd6d0bfd2"></a>

### `NXP_WUU_PIN_11_RISING_INT`

```c
#define NXP_WUU_PIN_11_RISING_INT NXP_WUU_PIN(11, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 11 的上升沿中断（Pin 11 rising edge interrupt）。

<a id="acf0865bd22e6e34f7c756df522ec2f10"></a>

### `NXP_WUU_PIN_11_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_11_RISING_TRIGGER NXP_WUU_PIN(11, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 11 的上升沿触发输出（Pin 11 rising edge trigger）。

<a id="a48125bf1480f0cf0ced7a9e1744a8fc2"></a>

### `NXP_WUU_PIN_12_ANY_DMA`

```c
#define NXP_WUU_PIN_12_ANY_DMA NXP_WUU_PIN(12, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 12 的任意边沿直接存储器访问请求（Pin 12 any edge DMA）。

<a id="a0fcf797c4f587d5e09c19b975363d5b4"></a>

### `NXP_WUU_PIN_12_ANY_INT`

```c
#define NXP_WUU_PIN_12_ANY_INT NXP_WUU_PIN(12, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 12 的任意边沿中断（Pin 12 any edge interrupt）。

<a id="adf0f44a76fa64137bfd769e7739e452f"></a>

### `NXP_WUU_PIN_12_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_12_ANY_TRIGGER NXP_WUU_PIN(12, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 12 的任意边沿触发输出（Pin 12 any edge trigger）。

<a id="a8e7e3f4786dfe612f08a0719dc356821"></a>

### `NXP_WUU_PIN_12_FALLING_DMA`

```c
#define NXP_WUU_PIN_12_FALLING_DMA NXP_WUU_PIN(12, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 12 的下降沿直接存储器访问请求（Pin 12 falling edge DMA）。

<a id="a78658be45b157759cbf79e6843d10159"></a>

### `NXP_WUU_PIN_12_FALLING_INT`

```c
#define NXP_WUU_PIN_12_FALLING_INT NXP_WUU_PIN(12, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 12 的下降沿中断（Pin 12 falling edge interrupt）。

<a id="a76fe883b827814f97028c211d2178041"></a>

### `NXP_WUU_PIN_12_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_12_FALLING_TRIGGER NXP_WUU_PIN(12, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 12 的下降沿触发输出（Pin 12 falling edge trigger）。

<a id="a6294c8eec90daf5ceab3732ef4c5b54c"></a>

### `NXP_WUU_PIN_12_RISING_DMA`

```c
#define NXP_WUU_PIN_12_RISING_DMA NXP_WUU_PIN(12, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 12 的上升沿直接存储器访问请求（Pin 12 rising edge DMA）。

<a id="a8c80f3d6e04df6097e991564a640a354"></a>

### `NXP_WUU_PIN_12_RISING_INT`

```c
#define NXP_WUU_PIN_12_RISING_INT NXP_WUU_PIN(12, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 12 的上升沿中断（Pin 12 rising edge interrupt）。

<a id="ae880986b6ee18f176b71cc9f28949662"></a>

### `NXP_WUU_PIN_12_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_12_RISING_TRIGGER NXP_WUU_PIN(12, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 12 的上升沿触发输出（Pin 12 rising edge trigger）。

<a id="a0e70b987fd03139f436f7b53f723adcf"></a>

### `NXP_WUU_PIN_13_ANY_DMA`

```c
#define NXP_WUU_PIN_13_ANY_DMA NXP_WUU_PIN(13, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 13 的任意边沿直接存储器访问请求（Pin 13 any edge DMA）。

<a id="a1c7336fa2c11bf50cfee5a6b4e3842c9"></a>

### `NXP_WUU_PIN_13_ANY_INT`

```c
#define NXP_WUU_PIN_13_ANY_INT NXP_WUU_PIN(13, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 13 的任意边沿中断（Pin 13 any edge interrupt）。

<a id="a8ebfd18a7979d0828d4683e02e1a2724"></a>

### `NXP_WUU_PIN_13_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_13_ANY_TRIGGER NXP_WUU_PIN(13, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 13 的任意边沿触发输出（Pin 13 any edge trigger）。

<a id="a12ac0088e1eed430adbc0f8e532b4c48"></a>

### `NXP_WUU_PIN_13_FALLING_DMA`

```c
#define NXP_WUU_PIN_13_FALLING_DMA NXP_WUU_PIN(13, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 13 的下降沿直接存储器访问请求（Pin 13 falling edge DMA）。

<a id="a6e4d6c89560f48f34052d59b05573630"></a>

### `NXP_WUU_PIN_13_FALLING_INT`

```c
#define NXP_WUU_PIN_13_FALLING_INT NXP_WUU_PIN(13, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 13 的下降沿中断（Pin 13 falling edge interrupt）。

<a id="aec1b861704f490734e8befd3cf913a6e"></a>

### `NXP_WUU_PIN_13_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_13_FALLING_TRIGGER NXP_WUU_PIN(13, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 13 的下降沿触发输出（Pin 13 falling edge trigger）。

<a id="a5c63c8669751a21f102f1e724bbbdaaf"></a>

### `NXP_WUU_PIN_13_RISING_DMA`

```c
#define NXP_WUU_PIN_13_RISING_DMA NXP_WUU_PIN(13, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 13 的上升沿直接存储器访问请求（Pin 13 rising edge DMA）。

<a id="abad94246db6369148c0fb1a3cf139a68"></a>

### `NXP_WUU_PIN_13_RISING_INT`

```c
#define NXP_WUU_PIN_13_RISING_INT NXP_WUU_PIN(13, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 13 的上升沿中断（Pin 13 rising edge interrupt）。

<a id="aa85c1f075d31c57640d7c484b4a82586"></a>

### `NXP_WUU_PIN_13_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_13_RISING_TRIGGER NXP_WUU_PIN(13, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 13 的上升沿触发输出（Pin 13 rising edge trigger）。

<a id="a62d9134ec2f2c8ea79bc8f9d1ee30047"></a>

### `NXP_WUU_PIN_14_ANY_DMA`

```c
#define NXP_WUU_PIN_14_ANY_DMA NXP_WUU_PIN(14, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 14 的任意边沿直接存储器访问请求（Pin 14 any edge DMA）。

<a id="a7b4335ee8dd7af40e69bbf7ea2583c85"></a>

### `NXP_WUU_PIN_14_ANY_INT`

```c
#define NXP_WUU_PIN_14_ANY_INT NXP_WUU_PIN(14, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 14 的任意边沿中断（Pin 14 any edge interrupt）。

<a id="aed863aef549034f8eeafdb3d119afcec"></a>

### `NXP_WUU_PIN_14_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_14_ANY_TRIGGER NXP_WUU_PIN(14, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 14 的任意边沿触发输出（Pin 14 any edge trigger）。

<a id="a136e1a20fe6f29ba8a779c36b12f5884"></a>

### `NXP_WUU_PIN_14_FALLING_DMA`

```c
#define NXP_WUU_PIN_14_FALLING_DMA NXP_WUU_PIN(14, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 14 的下降沿直接存储器访问请求（Pin 14 falling edge DMA）。

<a id="a4f69e11960adab498586507a9e7c3fb2"></a>

### `NXP_WUU_PIN_14_FALLING_INT`

```c
#define NXP_WUU_PIN_14_FALLING_INT NXP_WUU_PIN(14, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 14 的下降沿中断（Pin 14 falling edge interrupt）。

<a id="a066fe7df5fd40e31d0d205a5084fc3dd"></a>

### `NXP_WUU_PIN_14_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_14_FALLING_TRIGGER NXP_WUU_PIN(14, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 14 的下降沿触发输出（Pin 14 falling edge trigger）。

<a id="a8698ee619dc97e7e5e10177b373d3d37"></a>

### `NXP_WUU_PIN_14_RISING_DMA`

```c
#define NXP_WUU_PIN_14_RISING_DMA NXP_WUU_PIN(14, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 14 的上升沿直接存储器访问请求（Pin 14 rising edge DMA）。

<a id="adc38f6e93991725760cfef6758079c89"></a>

### `NXP_WUU_PIN_14_RISING_INT`

```c
#define NXP_WUU_PIN_14_RISING_INT NXP_WUU_PIN(14, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 14 的上升沿中断（Pin 14 rising edge interrupt）。

<a id="aad6dc6a44a8051cd064d7949d6eb0c11"></a>

### `NXP_WUU_PIN_14_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_14_RISING_TRIGGER NXP_WUU_PIN(14, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 14 的上升沿触发输出（Pin 14 rising edge trigger）。

<a id="a81b0a064eed11059563734244b4808e7"></a>

### `NXP_WUU_PIN_15_ANY_DMA`

```c
#define NXP_WUU_PIN_15_ANY_DMA NXP_WUU_PIN(15, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 15 的任意边沿直接存储器访问请求（Pin 15 any edge DMA）。

<a id="ad771a9eaf7825f54e54cee7755a9967a"></a>

### `NXP_WUU_PIN_15_ANY_INT`

```c
#define NXP_WUU_PIN_15_ANY_INT NXP_WUU_PIN(15, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 15 的任意边沿中断（Pin 15 any edge interrupt）。

<a id="ad57084c076a2d90fe5a7038822d51e92"></a>

### `NXP_WUU_PIN_15_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_15_ANY_TRIGGER NXP_WUU_PIN(15, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 15 的任意边沿触发输出（Pin 15 any edge trigger）。

<a id="a2b0d50f454fafa5813137f25ec74fb9b"></a>

### `NXP_WUU_PIN_15_FALLING_DMA`

```c
#define NXP_WUU_PIN_15_FALLING_DMA NXP_WUU_PIN(15, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 15 的下降沿直接存储器访问请求（Pin 15 falling edge DMA）。

<a id="a9071b46613aa5347323db173e9508d21"></a>

### `NXP_WUU_PIN_15_FALLING_INT`

```c
#define NXP_WUU_PIN_15_FALLING_INT NXP_WUU_PIN(15, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 15 的下降沿中断（Pin 15 falling edge interrupt）。

<a id="a7bcd6009425bf5bd432109c03a7f7f7a"></a>

### `NXP_WUU_PIN_15_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_15_FALLING_TRIGGER NXP_WUU_PIN(15, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 15 的下降沿触发输出（Pin 15 falling edge trigger）。

<a id="aa0ddff16c6fd56eb67dec54c4e9c628f"></a>

### `NXP_WUU_PIN_15_RISING_DMA`

```c
#define NXP_WUU_PIN_15_RISING_DMA NXP_WUU_PIN(15, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 15 的上升沿直接存储器访问请求（Pin 15 rising edge DMA）。

<a id="a9db1b076129d3a63a30fbde70f3d7377"></a>

### `NXP_WUU_PIN_15_RISING_INT`

```c
#define NXP_WUU_PIN_15_RISING_INT NXP_WUU_PIN(15, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 15 的上升沿中断（Pin 15 rising edge interrupt）。

<a id="aa5eb7875891b2936c0a7c5f5a4c2584a"></a>

### `NXP_WUU_PIN_15_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_15_RISING_TRIGGER NXP_WUU_PIN(15, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 15 的上升沿触发输出（Pin 15 rising edge trigger）。

<a id="a1e3156e7786f2968072d03d7ddf8757c"></a>

### `NXP_WUU_PIN_16_ANY_DMA`

```c
#define NXP_WUU_PIN_16_ANY_DMA NXP_WUU_PIN(16, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 16 的任意边沿直接存储器访问请求（Pin 16 any edge DMA）。

<a id="ab897fe96ec5635bc19aaefa716551afa"></a>

### `NXP_WUU_PIN_16_ANY_INT`

```c
#define NXP_WUU_PIN_16_ANY_INT NXP_WUU_PIN(16, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 16 的任意边沿中断（Pin 16 any edge interrupt）。

<a id="a5d840552a98bd57d478693fa898268ef"></a>

### `NXP_WUU_PIN_16_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_16_ANY_TRIGGER NXP_WUU_PIN(16, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 16 的任意边沿触发输出（Pin 16 any edge trigger）。

<a id="ad4bc82fd63883f02d34798a5712a46c5"></a>

### `NXP_WUU_PIN_16_FALLING_DMA`

```c
#define NXP_WUU_PIN_16_FALLING_DMA NXP_WUU_PIN(16, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 16 的下降沿直接存储器访问请求（Pin 16 falling edge DMA）。

<a id="a450baf91b13cf9f27fd2ac012c7edabe"></a>

### `NXP_WUU_PIN_16_FALLING_INT`

```c
#define NXP_WUU_PIN_16_FALLING_INT NXP_WUU_PIN(16, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 16 的下降沿中断（Pin 16 falling edge interrupt）。

<a id="a728ac5704ab4594d71918f33871378ce"></a>

### `NXP_WUU_PIN_16_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_16_FALLING_TRIGGER NXP_WUU_PIN(16, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 16 的下降沿触发输出（Pin 16 falling edge trigger）。

<a id="a5dc27bc0fe120ae5c1cca98f2a4cdcfc"></a>

### `NXP_WUU_PIN_16_RISING_DMA`

```c
#define NXP_WUU_PIN_16_RISING_DMA NXP_WUU_PIN(16, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 16 的上升沿直接存储器访问请求（Pin 16 rising edge DMA）。

<a id="adfcf294a24063a9931efa25df317732b"></a>

### `NXP_WUU_PIN_16_RISING_INT`

```c
#define NXP_WUU_PIN_16_RISING_INT NXP_WUU_PIN(16, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 16 的上升沿中断（Pin 16 rising edge interrupt）。

<a id="a4a9c35ae2b4277edbbbb08b741c68fa6"></a>

### `NXP_WUU_PIN_16_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_16_RISING_TRIGGER NXP_WUU_PIN(16, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 16 的上升沿触发输出（Pin 16 rising edge trigger）。

<a id="a46f0f287973dc5b750e7cf0514a2b9db"></a>

### `NXP_WUU_PIN_17_ANY_DMA`

```c
#define NXP_WUU_PIN_17_ANY_DMA NXP_WUU_PIN(17, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 17 的任意边沿直接存储器访问请求（Pin 17 any edge DMA）。

<a id="a78cfe7f65e765dec76141aba513e0102"></a>

### `NXP_WUU_PIN_17_ANY_INT`

```c
#define NXP_WUU_PIN_17_ANY_INT NXP_WUU_PIN(17, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 17 的任意边沿中断（Pin 17 any edge interrupt）。

<a id="a6629f49862fd75b780ac775e529a6b7c"></a>

### `NXP_WUU_PIN_17_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_17_ANY_TRIGGER NXP_WUU_PIN(17, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 17 的任意边沿触发输出（Pin 17 any edge trigger）。

<a id="abf11fb64eb14a15507618780fe45b33e"></a>

### `NXP_WUU_PIN_17_FALLING_DMA`

```c
#define NXP_WUU_PIN_17_FALLING_DMA NXP_WUU_PIN(17, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 17 的下降沿直接存储器访问请求（Pin 17 falling edge DMA）。

<a id="a48c1840fa1c5cced807e030deee4200f"></a>

### `NXP_WUU_PIN_17_FALLING_INT`

```c
#define NXP_WUU_PIN_17_FALLING_INT NXP_WUU_PIN(17, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 17 的下降沿中断（Pin 17 falling edge interrupt）。

<a id="a3532a13150ce817ad8766363241c6208"></a>

### `NXP_WUU_PIN_17_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_17_FALLING_TRIGGER NXP_WUU_PIN(17, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 17 的下降沿触发输出（Pin 17 falling edge trigger）。

<a id="ad9c1dbacbc7a9ca82619e852d6226d01"></a>

### `NXP_WUU_PIN_17_RISING_DMA`

```c
#define NXP_WUU_PIN_17_RISING_DMA NXP_WUU_PIN(17, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 17 的上升沿直接存储器访问请求（Pin 17 rising edge DMA）。

<a id="a31540908b47a3bc950d07ea769e2417e"></a>

### `NXP_WUU_PIN_17_RISING_INT`

```c
#define NXP_WUU_PIN_17_RISING_INT NXP_WUU_PIN(17, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 17 的上升沿中断（Pin 17 rising edge interrupt）。

<a id="a427b957b4e32f43d7b9af0873c452fb0"></a>

### `NXP_WUU_PIN_17_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_17_RISING_TRIGGER NXP_WUU_PIN(17, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 17 的上升沿触发输出（Pin 17 rising edge trigger）。

<a id="aae7bce9ef1e499cc75c5902f58dbb2cc"></a>

### `NXP_WUU_PIN_18_ANY_DMA`

```c
#define NXP_WUU_PIN_18_ANY_DMA NXP_WUU_PIN(18, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 18 的任意边沿直接存储器访问请求（Pin 18 any edge DMA）。

<a id="a3fca4746d56e2c3fb231d3f5fe2161fb"></a>

### `NXP_WUU_PIN_18_ANY_INT`

```c
#define NXP_WUU_PIN_18_ANY_INT NXP_WUU_PIN(18, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 18 的任意边沿中断（Pin 18 any edge interrupt）。

<a id="a13ba376dcc47a4fe533aecd6bf185093"></a>

### `NXP_WUU_PIN_18_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_18_ANY_TRIGGER NXP_WUU_PIN(18, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 18 的任意边沿触发输出（Pin 18 any edge trigger）。

<a id="a8567faff46474b71fc45c12ec2a3ef44"></a>

### `NXP_WUU_PIN_18_FALLING_DMA`

```c
#define NXP_WUU_PIN_18_FALLING_DMA NXP_WUU_PIN(18, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 18 的下降沿直接存储器访问请求（Pin 18 falling edge DMA）。

<a id="ac978c583bd32dc45ec87b581f422562d"></a>

### `NXP_WUU_PIN_18_FALLING_INT`

```c
#define NXP_WUU_PIN_18_FALLING_INT NXP_WUU_PIN(18, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 18 的下降沿中断（Pin 18 falling edge interrupt）。

<a id="a7adcc876c2a608ade50e2b46c02c3236"></a>

### `NXP_WUU_PIN_18_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_18_FALLING_TRIGGER NXP_WUU_PIN(18, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 18 的下降沿触发输出（Pin 18 falling edge trigger）。

<a id="ae5df884ff42594d73630a479c7ed5cd9"></a>

### `NXP_WUU_PIN_18_RISING_DMA`

```c
#define NXP_WUU_PIN_18_RISING_DMA NXP_WUU_PIN(18, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 18 的上升沿直接存储器访问请求（Pin 18 rising edge DMA）。

<a id="a506ccb796cfed8bd48999be92c41d0a5"></a>

### `NXP_WUU_PIN_18_RISING_INT`

```c
#define NXP_WUU_PIN_18_RISING_INT NXP_WUU_PIN(18, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 18 的上升沿中断（Pin 18 rising edge interrupt）。

<a id="ab4a5ea49ce2a5afe63821f4b7aa241ed"></a>

### `NXP_WUU_PIN_18_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_18_RISING_TRIGGER NXP_WUU_PIN(18, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 18 的上升沿触发输出（Pin 18 rising edge trigger）。

<a id="ac86a2430bd0204e4b742248f90f4e15c"></a>

### `NXP_WUU_PIN_19_ANY_DMA`

```c
#define NXP_WUU_PIN_19_ANY_DMA NXP_WUU_PIN(19, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 19 的任意边沿直接存储器访问请求（Pin 19 any edge DMA）。

<a id="a17c194f87dcf310e80644e23c3cf2741"></a>

### `NXP_WUU_PIN_19_ANY_INT`

```c
#define NXP_WUU_PIN_19_ANY_INT NXP_WUU_PIN(19, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 19 的任意边沿中断（Pin 19 any edge interrupt）。

<a id="a2da00e28b0cc91a12c3d3ca9dc4f0625"></a>

### `NXP_WUU_PIN_19_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_19_ANY_TRIGGER NXP_WUU_PIN(19, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 19 的任意边沿触发输出（Pin 19 any edge trigger）。

<a id="ae5cf777820d6fae0bde68e642646c5f1"></a>

### `NXP_WUU_PIN_19_FALLING_DMA`

```c
#define NXP_WUU_PIN_19_FALLING_DMA NXP_WUU_PIN(19, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 19 的下降沿直接存储器访问请求（Pin 19 falling edge DMA）。

<a id="aa150b69aa5c9806bf34267cc77b1ea68"></a>

### `NXP_WUU_PIN_19_FALLING_INT`

```c
#define NXP_WUU_PIN_19_FALLING_INT NXP_WUU_PIN(19, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 19 的下降沿中断（Pin 19 falling edge interrupt）。

<a id="a14f90ae893427011f3c797c5e28eae71"></a>

### `NXP_WUU_PIN_19_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_19_FALLING_TRIGGER NXP_WUU_PIN(19, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 19 的下降沿触发输出（Pin 19 falling edge trigger）。

<a id="ae89a87ad6d8dae7d923594b414ce2a1b"></a>

### `NXP_WUU_PIN_19_RISING_DMA`

```c
#define NXP_WUU_PIN_19_RISING_DMA NXP_WUU_PIN(19, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 19 的上升沿直接存储器访问请求（Pin 19 rising edge DMA）。

<a id="acefad14e0dd0c79ac4a8941980b26ccb"></a>

### `NXP_WUU_PIN_19_RISING_INT`

```c
#define NXP_WUU_PIN_19_RISING_INT NXP_WUU_PIN(19, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 19 的上升沿中断（Pin 19 rising edge interrupt）。

<a id="aa3f5fff1f2baf23834b71d849ae2aa36"></a>

### `NXP_WUU_PIN_19_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_19_RISING_TRIGGER NXP_WUU_PIN(19, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 19 的上升沿触发输出（Pin 19 rising edge trigger）。

<a id="a3714e4b51f69f6c81f4beef8be9c7662"></a>

### `NXP_WUU_PIN_1_ANY_DMA`

```c
#define NXP_WUU_PIN_1_ANY_DMA NXP_WUU_PIN(1, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 1 的任意边沿直接存储器访问请求（Pin 1 any edge DMA）。

<a id="a4322d9c1add84c779e93f0f6c0a72581"></a>

### `NXP_WUU_PIN_1_ANY_INT`

```c
#define NXP_WUU_PIN_1_ANY_INT NXP_WUU_PIN(1, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 1 的任意边沿中断（Pin 1 any edge interrupt）。

<a id="a155a73ef138aeaaddcaf6c3fc6f26f13"></a>

### `NXP_WUU_PIN_1_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_1_ANY_TRIGGER NXP_WUU_PIN(1, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 1 的任意边沿触发输出（Pin 1 any edge trigger）。

<a id="afd3d2a168c2bc1443b427c044bd7c23c"></a>

### `NXP_WUU_PIN_1_FALLING_DMA`

```c
#define NXP_WUU_PIN_1_FALLING_DMA NXP_WUU_PIN(1, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 1 的下降沿直接存储器访问请求（Pin 1 falling edge DMA）。

<a id="ad7874c8b597433427225dfb715310f9f"></a>

### `NXP_WUU_PIN_1_FALLING_INT`

```c
#define NXP_WUU_PIN_1_FALLING_INT NXP_WUU_PIN(1, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 1 的下降沿中断（Pin 1 falling edge interrupt）。

<a id="ae72c2cefea5ca77ea80f01eccf757ab6"></a>

### `NXP_WUU_PIN_1_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_1_FALLING_TRIGGER NXP_WUU_PIN(1, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 1 的下降沿触发输出（Pin 1 falling edge trigger）。

<a id="a545a4416464829a915fd94cd8d83adc5"></a>

### `NXP_WUU_PIN_1_RISING_DMA`

```c
#define NXP_WUU_PIN_1_RISING_DMA NXP_WUU_PIN(1, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 1 的上升沿直接存储器访问请求（Pin 1 rising edge DMA）。

<a id="af6c68e8fa486d668d8ef2d5f1d375c14"></a>

### `NXP_WUU_PIN_1_RISING_INT`

```c
#define NXP_WUU_PIN_1_RISING_INT NXP_WUU_PIN(1, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 1 的上升沿中断（Pin 1 rising edge interrupt）。

<a id="a5090f5949511fd8db1bc4221cc4da47f"></a>

### `NXP_WUU_PIN_1_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_1_RISING_TRIGGER NXP_WUU_PIN(1, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 1 的上升沿触发输出（Pin 1 rising edge trigger）。

<a id="af9b12c5aed07b9a498501108a2adfc77"></a>

### `NXP_WUU_PIN_20_ANY_DMA`

```c
#define NXP_WUU_PIN_20_ANY_DMA NXP_WUU_PIN(20, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 20 的任意边沿直接存储器访问请求（Pin 20 any edge DMA）。

<a id="a21faa14e3950d7af7105ab64f1643e25"></a>

### `NXP_WUU_PIN_20_ANY_INT`

```c
#define NXP_WUU_PIN_20_ANY_INT NXP_WUU_PIN(20, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 20 的任意边沿中断（Pin 20 any edge interrupt）。

<a id="a55df2b0445f30c848a667c73bebdd53d"></a>

### `NXP_WUU_PIN_20_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_20_ANY_TRIGGER NXP_WUU_PIN(20, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 20 的任意边沿触发输出（Pin 20 any edge trigger）。

<a id="a465dcff3b9abe6ffed79c0929a187387"></a>

### `NXP_WUU_PIN_20_FALLING_DMA`

```c
#define NXP_WUU_PIN_20_FALLING_DMA NXP_WUU_PIN(20, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 20 的下降沿直接存储器访问请求（Pin 20 falling edge DMA）。

<a id="a50d8e0138b11164b307efe9e8235d97e"></a>

### `NXP_WUU_PIN_20_FALLING_INT`

```c
#define NXP_WUU_PIN_20_FALLING_INT NXP_WUU_PIN(20, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 20 的下降沿中断（Pin 20 falling edge interrupt）。

<a id="a8b48e7713c41a96a994a5f987cc00568"></a>

### `NXP_WUU_PIN_20_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_20_FALLING_TRIGGER NXP_WUU_PIN(20, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 20 的下降沿触发输出（Pin 20 falling edge trigger）。

<a id="af44689b24c5a9f7edd05aa239d7b2bb6"></a>

### `NXP_WUU_PIN_20_RISING_DMA`

```c
#define NXP_WUU_PIN_20_RISING_DMA NXP_WUU_PIN(20, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 20 的上升沿直接存储器访问请求（Pin 20 rising edge DMA）。

<a id="a7d46cccd96904d0136a1a1f345b1cf51"></a>

### `NXP_WUU_PIN_20_RISING_INT`

```c
#define NXP_WUU_PIN_20_RISING_INT NXP_WUU_PIN(20, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 20 的上升沿中断（Pin 20 rising edge interrupt）。

<a id="aacc61ba8c492295a9222d4adfa856d68"></a>

### `NXP_WUU_PIN_20_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_20_RISING_TRIGGER NXP_WUU_PIN(20, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 20 的上升沿触发输出（Pin 20 rising edge trigger）。

<a id="a9a6d1a5da9984f594037d4835dc0ea83"></a>

### `NXP_WUU_PIN_21_ANY_DMA`

```c
#define NXP_WUU_PIN_21_ANY_DMA NXP_WUU_PIN(21, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 21 的任意边沿直接存储器访问请求（Pin 21 any edge DMA）。

<a id="ac09bc5380153996e43eff1d2fc5f5039"></a>

### `NXP_WUU_PIN_21_ANY_INT`

```c
#define NXP_WUU_PIN_21_ANY_INT NXP_WUU_PIN(21, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 21 的任意边沿中断（Pin 21 any edge interrupt）。

<a id="ae4947d1f4d99207a272cfeb4f796ccdd"></a>

### `NXP_WUU_PIN_21_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_21_ANY_TRIGGER NXP_WUU_PIN(21, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 21 的任意边沿触发输出（Pin 21 any edge trigger）。

<a id="a5b9ccb859e9534e2c5f020e8d52cb935"></a>

### `NXP_WUU_PIN_21_FALLING_DMA`

```c
#define NXP_WUU_PIN_21_FALLING_DMA NXP_WUU_PIN(21, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 21 的下降沿直接存储器访问请求（Pin 21 falling edge DMA）。

<a id="ad51871d2a3e3e25e48663c4827e096a4"></a>

### `NXP_WUU_PIN_21_FALLING_INT`

```c
#define NXP_WUU_PIN_21_FALLING_INT NXP_WUU_PIN(21, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 21 的下降沿中断（Pin 21 falling edge interrupt）。

<a id="afcda5e8e65a534d5203653460b328d3e"></a>

### `NXP_WUU_PIN_21_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_21_FALLING_TRIGGER NXP_WUU_PIN(21, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 21 的下降沿触发输出（Pin 21 falling edge trigger）。

<a id="a16e1fc6e2a38348c0c2ce7c865015363"></a>

### `NXP_WUU_PIN_21_RISING_DMA`

```c
#define NXP_WUU_PIN_21_RISING_DMA NXP_WUU_PIN(21, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 21 的上升沿直接存储器访问请求（Pin 21 rising edge DMA）。

<a id="a4e6e9c5c37d8aa2c4626ffb545d9278d"></a>

### `NXP_WUU_PIN_21_RISING_INT`

```c
#define NXP_WUU_PIN_21_RISING_INT NXP_WUU_PIN(21, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 21 的上升沿中断（Pin 21 rising edge interrupt）。

<a id="ac398816bd7222ceb960c3fe4d7830f58"></a>

### `NXP_WUU_PIN_21_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_21_RISING_TRIGGER NXP_WUU_PIN(21, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 21 的上升沿触发输出（Pin 21 rising edge trigger）。

<a id="a0afc2d32673e4af3c311f1cf82f70533"></a>

### `NXP_WUU_PIN_22_ANY_DMA`

```c
#define NXP_WUU_PIN_22_ANY_DMA NXP_WUU_PIN(22, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 22 的任意边沿直接存储器访问请求（Pin 22 any edge DMA）。

<a id="a1254db7ec52aeee3d2cd92750cc90792"></a>

### `NXP_WUU_PIN_22_ANY_INT`

```c
#define NXP_WUU_PIN_22_ANY_INT NXP_WUU_PIN(22, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 22 的任意边沿中断（Pin 22 any edge interrupt）。

<a id="a354a1e9768d6a461868675bd29ba92ed"></a>

### `NXP_WUU_PIN_22_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_22_ANY_TRIGGER NXP_WUU_PIN(22, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 22 的任意边沿触发输出（Pin 22 any edge trigger）。

<a id="af1290b944be74262979a8a961ef113c3"></a>

### `NXP_WUU_PIN_22_FALLING_DMA`

```c
#define NXP_WUU_PIN_22_FALLING_DMA NXP_WUU_PIN(22, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 22 的下降沿直接存储器访问请求（Pin 22 falling edge DMA）。

<a id="a1295040c63fd36098b23f0b23d9cb6fc"></a>

### `NXP_WUU_PIN_22_FALLING_INT`

```c
#define NXP_WUU_PIN_22_FALLING_INT NXP_WUU_PIN(22, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 22 的下降沿中断（Pin 22 falling edge interrupt）。

<a id="a970eb9293924f98fae733a5868573ebe"></a>

### `NXP_WUU_PIN_22_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_22_FALLING_TRIGGER NXP_WUU_PIN(22, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 22 的下降沿触发输出（Pin 22 falling edge trigger）。

<a id="a7e1b24e4ed605b59479563c02ac0b880"></a>

### `NXP_WUU_PIN_22_RISING_DMA`

```c
#define NXP_WUU_PIN_22_RISING_DMA NXP_WUU_PIN(22, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 22 的上升沿直接存储器访问请求（Pin 22 rising edge DMA）。

<a id="ab2c03c05bdc6f379d40f66b598d2da59"></a>

### `NXP_WUU_PIN_22_RISING_INT`

```c
#define NXP_WUU_PIN_22_RISING_INT NXP_WUU_PIN(22, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 22 的上升沿中断（Pin 22 rising edge interrupt）。

<a id="a3f2c4f4794d4a9fb4b8afa7753e4f4a6"></a>

### `NXP_WUU_PIN_22_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_22_RISING_TRIGGER NXP_WUU_PIN(22, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 22 的上升沿触发输出（Pin 22 rising edge trigger）。

<a id="acf0bb6d2f6e77565dc41da3c111eba51"></a>

### `NXP_WUU_PIN_23_ANY_DMA`

```c
#define NXP_WUU_PIN_23_ANY_DMA NXP_WUU_PIN(23, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 23 的任意边沿直接存储器访问请求（Pin 23 any edge DMA）。

<a id="a5c4237c33652de5c60d14dd48fdd0f58"></a>

### `NXP_WUU_PIN_23_ANY_INT`

```c
#define NXP_WUU_PIN_23_ANY_INT NXP_WUU_PIN(23, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 23 的任意边沿中断（Pin 23 any edge interrupt）。

<a id="a7cfb8765eb6f361a6f5e66504f4a2815"></a>

### `NXP_WUU_PIN_23_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_23_ANY_TRIGGER NXP_WUU_PIN(23, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 23 的任意边沿触发输出（Pin 23 any edge trigger）。

<a id="ab58a65207d587a3d84d5cb872c053d88"></a>

### `NXP_WUU_PIN_23_FALLING_DMA`

```c
#define NXP_WUU_PIN_23_FALLING_DMA NXP_WUU_PIN(23, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 23 的下降沿直接存储器访问请求（Pin 23 falling edge DMA）。

<a id="a8e10c62976dce2224806798f0bd6e583"></a>

### `NXP_WUU_PIN_23_FALLING_INT`

```c
#define NXP_WUU_PIN_23_FALLING_INT NXP_WUU_PIN(23, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 23 的下降沿中断（Pin 23 falling edge interrupt）。

<a id="a630d67e605e582eb0304f8cf9e0981b6"></a>

### `NXP_WUU_PIN_23_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_23_FALLING_TRIGGER NXP_WUU_PIN(23, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 23 的下降沿触发输出（Pin 23 falling edge trigger）。

<a id="ac46430498dea7d33e0ec4ef90da00ae5"></a>

### `NXP_WUU_PIN_23_RISING_DMA`

```c
#define NXP_WUU_PIN_23_RISING_DMA NXP_WUU_PIN(23, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 23 的上升沿直接存储器访问请求（Pin 23 rising edge DMA）。

<a id="a64016990a9468d96d4b8fc79f8e6bd29"></a>

### `NXP_WUU_PIN_23_RISING_INT`

```c
#define NXP_WUU_PIN_23_RISING_INT NXP_WUU_PIN(23, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 23 的上升沿中断（Pin 23 rising edge interrupt）。

<a id="ab5702a24d851ccd2e11c07a2ff755e4c"></a>

### `NXP_WUU_PIN_23_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_23_RISING_TRIGGER NXP_WUU_PIN(23, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 23 的上升沿触发输出（Pin 23 rising edge trigger）。

<a id="a5c7cd136b67cd5b7e08ceeaeea4bfb76"></a>

### `NXP_WUU_PIN_24_ANY_DMA`

```c
#define NXP_WUU_PIN_24_ANY_DMA NXP_WUU_PIN(24, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 24 的任意边沿直接存储器访问请求（Pin 24 any edge DMA）。

<a id="ac32c55886098d01cebe5cabafa6c1c68"></a>

### `NXP_WUU_PIN_24_ANY_INT`

```c
#define NXP_WUU_PIN_24_ANY_INT NXP_WUU_PIN(24, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 24 的任意边沿中断（Pin 24 any edge interrupt）。

<a id="a605894f98f993c88183710279574366e"></a>

### `NXP_WUU_PIN_24_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_24_ANY_TRIGGER NXP_WUU_PIN(24, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 24 的任意边沿触发输出（Pin 24 any edge trigger）。

<a id="aa94fb06fd5e80386cb0ee7a1dd1d29b7"></a>

### `NXP_WUU_PIN_24_FALLING_DMA`

```c
#define NXP_WUU_PIN_24_FALLING_DMA NXP_WUU_PIN(24, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 24 的下降沿直接存储器访问请求（Pin 24 falling edge DMA）。

<a id="a99f1ae94248003598c12ce11b2b2c550"></a>

### `NXP_WUU_PIN_24_FALLING_INT`

```c
#define NXP_WUU_PIN_24_FALLING_INT NXP_WUU_PIN(24, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 24 的下降沿中断（Pin 24 falling edge interrupt）。

<a id="ae8876a7cb177ac376769375ca96a364b"></a>

### `NXP_WUU_PIN_24_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_24_FALLING_TRIGGER NXP_WUU_PIN(24, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 24 的下降沿触发输出（Pin 24 falling edge trigger）。

<a id="a7751f13409941a48e903cc5a7bba0966"></a>

### `NXP_WUU_PIN_24_RISING_DMA`

```c
#define NXP_WUU_PIN_24_RISING_DMA NXP_WUU_PIN(24, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 24 的上升沿直接存储器访问请求（Pin 24 rising edge DMA）。

<a id="a1ab5e383b924a0fef3f9aed083151d6c"></a>

### `NXP_WUU_PIN_24_RISING_INT`

```c
#define NXP_WUU_PIN_24_RISING_INT NXP_WUU_PIN(24, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 24 的上升沿中断（Pin 24 rising edge interrupt）。

<a id="aa0e41affe7b3ea661e13663833f5e928"></a>

### `NXP_WUU_PIN_24_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_24_RISING_TRIGGER NXP_WUU_PIN(24, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 24 的上升沿触发输出（Pin 24 rising edge trigger）。

<a id="af17e95c7f7e74e995038066f9bc4ba6f"></a>

### `NXP_WUU_PIN_25_ANY_DMA`

```c
#define NXP_WUU_PIN_25_ANY_DMA NXP_WUU_PIN(25, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 25 的任意边沿直接存储器访问请求（Pin 25 any edge DMA）。

<a id="a139e6518f84f66824db9828f6487f9d2"></a>

### `NXP_WUU_PIN_25_ANY_INT`

```c
#define NXP_WUU_PIN_25_ANY_INT NXP_WUU_PIN(25, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 25 的任意边沿中断（Pin 25 any edge interrupt）。

<a id="afd282674c01bc2218a84cbe8b551cd04"></a>

### `NXP_WUU_PIN_25_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_25_ANY_TRIGGER NXP_WUU_PIN(25, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 25 的任意边沿触发输出（Pin 25 any edge trigger）。

<a id="a0940391b22b5d240e3734a7f9b398587"></a>

### `NXP_WUU_PIN_25_FALLING_DMA`

```c
#define NXP_WUU_PIN_25_FALLING_DMA NXP_WUU_PIN(25, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 25 的下降沿直接存储器访问请求（Pin 25 falling edge DMA）。

<a id="ac1fd771014c83ce5ef7e29a15fbdb64b"></a>

### `NXP_WUU_PIN_25_FALLING_INT`

```c
#define NXP_WUU_PIN_25_FALLING_INT NXP_WUU_PIN(25, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 25 的下降沿中断（Pin 25 falling edge interrupt）。

<a id="adc98eed33ab6fcbda8d85f1685aa974f"></a>

### `NXP_WUU_PIN_25_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_25_FALLING_TRIGGER NXP_WUU_PIN(25, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 25 的下降沿触发输出（Pin 25 falling edge trigger）。

<a id="a9587fc89dee2b403f9a1d3dc68130ccf"></a>

### `NXP_WUU_PIN_25_RISING_DMA`

```c
#define NXP_WUU_PIN_25_RISING_DMA NXP_WUU_PIN(25, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 25 的上升沿直接存储器访问请求（Pin 25 rising edge DMA）。

<a id="a0786c00ff54c6f408fcc3ff842eac328"></a>

### `NXP_WUU_PIN_25_RISING_INT`

```c
#define NXP_WUU_PIN_25_RISING_INT NXP_WUU_PIN(25, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 25 的上升沿中断（Pin 25 rising edge interrupt）。

<a id="aba6865f7ce26ae506d38900d7dc88a92"></a>

### `NXP_WUU_PIN_25_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_25_RISING_TRIGGER NXP_WUU_PIN(25, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 25 的上升沿触发输出（Pin 25 rising edge trigger）。

<a id="ad38b8b9c677732abbea0e203c4d48496"></a>

### `NXP_WUU_PIN_26_ANY_DMA`

```c
#define NXP_WUU_PIN_26_ANY_DMA NXP_WUU_PIN(26, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 26 的任意边沿直接存储器访问请求（Pin 26 any edge DMA）。

<a id="a8732cc560348b8b6a8887bd1689a1c91"></a>

### `NXP_WUU_PIN_26_ANY_INT`

```c
#define NXP_WUU_PIN_26_ANY_INT NXP_WUU_PIN(26, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 26 的任意边沿中断（Pin 26 any edge interrupt）。

<a id="a5a9f75686c4bd3072b24a7ccebe35c96"></a>

### `NXP_WUU_PIN_26_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_26_ANY_TRIGGER NXP_WUU_PIN(26, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 26 的任意边沿触发输出（Pin 26 any edge trigger）。

<a id="af2f6c44e0a4f87b095c849244d7bc591"></a>

### `NXP_WUU_PIN_26_FALLING_DMA`

```c
#define NXP_WUU_PIN_26_FALLING_DMA NXP_WUU_PIN(26, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 26 的下降沿直接存储器访问请求（Pin 26 falling edge DMA）。

<a id="a7cb27974779a15abcb6f7ef2ca584fc0"></a>

### `NXP_WUU_PIN_26_FALLING_INT`

```c
#define NXP_WUU_PIN_26_FALLING_INT NXP_WUU_PIN(26, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 26 的下降沿中断（Pin 26 falling edge interrupt）。

<a id="a6136f467e9c3045e4c2b5cb53e5f6c33"></a>

### `NXP_WUU_PIN_26_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_26_FALLING_TRIGGER NXP_WUU_PIN(26, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 26 的下降沿触发输出（Pin 26 falling edge trigger）。

<a id="a260eeba3c8c0882c045d036fc469fc5d"></a>

### `NXP_WUU_PIN_26_RISING_DMA`

```c
#define NXP_WUU_PIN_26_RISING_DMA NXP_WUU_PIN(26, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 26 的上升沿直接存储器访问请求（Pin 26 rising edge DMA）。

<a id="a4d8f9a42d5a9f22033f48d3ff3deb574"></a>

### `NXP_WUU_PIN_26_RISING_INT`

```c
#define NXP_WUU_PIN_26_RISING_INT NXP_WUU_PIN(26, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 26 的上升沿中断（Pin 26 rising edge interrupt）。

<a id="a32b96187402f13717c590b3d595b66e4"></a>

### `NXP_WUU_PIN_26_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_26_RISING_TRIGGER NXP_WUU_PIN(26, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 26 的上升沿触发输出（Pin 26 rising edge trigger）。

<a id="af2f89438834c13f535e22cfdfbcddd60"></a>

### `NXP_WUU_PIN_27_ANY_DMA`

```c
#define NXP_WUU_PIN_27_ANY_DMA NXP_WUU_PIN(27, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 27 的任意边沿直接存储器访问请求（Pin 27 any edge DMA）。

<a id="a7b69faca62fc98fddb82729372cda153"></a>

### `NXP_WUU_PIN_27_ANY_INT`

```c
#define NXP_WUU_PIN_27_ANY_INT NXP_WUU_PIN(27, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 27 的任意边沿中断（Pin 27 any edge interrupt）。

<a id="a72448223dd0baaa22f5a2e37482e8d90"></a>

### `NXP_WUU_PIN_27_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_27_ANY_TRIGGER NXP_WUU_PIN(27, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 27 的任意边沿触发输出（Pin 27 any edge trigger）。

<a id="ae5cc3af8b9457232d775a1afb3e45efa"></a>

### `NXP_WUU_PIN_27_FALLING_DMA`

```c
#define NXP_WUU_PIN_27_FALLING_DMA NXP_WUU_PIN(27, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 27 的下降沿直接存储器访问请求（Pin 27 falling edge DMA）。

<a id="ab19c0a16839e7f71715fe97e54a31cfc"></a>

### `NXP_WUU_PIN_27_FALLING_INT`

```c
#define NXP_WUU_PIN_27_FALLING_INT NXP_WUU_PIN(27, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 27 的下降沿中断（Pin 27 falling edge interrupt）。

<a id="ab5559e1f172eec039d58c1df7fd9b648"></a>

### `NXP_WUU_PIN_27_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_27_FALLING_TRIGGER NXP_WUU_PIN(27, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 27 的下降沿触发输出（Pin 27 falling edge trigger）。

<a id="a389b6e9c46ff420a8ca3a902b4743b3e"></a>

### `NXP_WUU_PIN_27_RISING_DMA`

```c
#define NXP_WUU_PIN_27_RISING_DMA NXP_WUU_PIN(27, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 27 的上升沿直接存储器访问请求（Pin 27 rising edge DMA）。

<a id="a8f087bc8cecd70c7c0d9d10bddef9f6f"></a>

### `NXP_WUU_PIN_27_RISING_INT`

```c
#define NXP_WUU_PIN_27_RISING_INT NXP_WUU_PIN(27, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 27 的上升沿中断（Pin 27 rising edge interrupt）。

<a id="ae1666594469d6bef7bf295b9c5d42f3d"></a>

### `NXP_WUU_PIN_27_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_27_RISING_TRIGGER NXP_WUU_PIN(27, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 27 的上升沿触发输出（Pin 27 rising edge trigger）。

<a id="a347c8dad3efc35f5ff3376c987713461"></a>

### `NXP_WUU_PIN_28_ANY_DMA`

```c
#define NXP_WUU_PIN_28_ANY_DMA NXP_WUU_PIN(28, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 28 的任意边沿直接存储器访问请求（Pin 28 any edge DMA）。

<a id="adfb27b752ecd7c96a9ab2fcf855e024e"></a>

### `NXP_WUU_PIN_28_ANY_INT`

```c
#define NXP_WUU_PIN_28_ANY_INT NXP_WUU_PIN(28, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 28 的任意边沿中断（Pin 28 any edge interrupt）。

<a id="a602c954cc1a534f75601d821d1059b8d"></a>

### `NXP_WUU_PIN_28_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_28_ANY_TRIGGER NXP_WUU_PIN(28, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 28 的任意边沿触发输出（Pin 28 any edge trigger）。

<a id="aa06cba2ca497e50592bef33a20e387ea"></a>

### `NXP_WUU_PIN_28_FALLING_DMA`

```c
#define NXP_WUU_PIN_28_FALLING_DMA NXP_WUU_PIN(28, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 28 的下降沿直接存储器访问请求（Pin 28 falling edge DMA）。

<a id="a90df0c72e3dc2dca3a57ea50c47e64dd"></a>

### `NXP_WUU_PIN_28_FALLING_INT`

```c
#define NXP_WUU_PIN_28_FALLING_INT NXP_WUU_PIN(28, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 28 的下降沿中断（Pin 28 falling edge interrupt）。

<a id="ad1094a23e6b230e43da3f2c40928d406"></a>

### `NXP_WUU_PIN_28_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_28_FALLING_TRIGGER NXP_WUU_PIN(28, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 28 的下降沿触发输出（Pin 28 falling edge trigger）。

<a id="ac147e54729e572ac5740a1fb2132c822"></a>

### `NXP_WUU_PIN_28_RISING_DMA`

```c
#define NXP_WUU_PIN_28_RISING_DMA NXP_WUU_PIN(28, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 28 的上升沿直接存储器访问请求（Pin 28 rising edge DMA）。

<a id="ae61a7794b5274fc6b0fddd24b3786f79"></a>

### `NXP_WUU_PIN_28_RISING_INT`

```c
#define NXP_WUU_PIN_28_RISING_INT NXP_WUU_PIN(28, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 28 的上升沿中断（Pin 28 rising edge interrupt）。

<a id="aa9397ac0890139885bc6b23615082215"></a>

### `NXP_WUU_PIN_28_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_28_RISING_TRIGGER NXP_WUU_PIN(28, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 28 的上升沿触发输出（Pin 28 rising edge trigger）。

<a id="a36a0c5f7e40f432348a1119d5772d5ec"></a>

### `NXP_WUU_PIN_29_ANY_DMA`

```c
#define NXP_WUU_PIN_29_ANY_DMA NXP_WUU_PIN(29, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 29 的任意边沿直接存储器访问请求（Pin 29 any edge DMA）。

<a id="a2294c7fcf8124f0e97f461dba7a459fe"></a>

### `NXP_WUU_PIN_29_ANY_INT`

```c
#define NXP_WUU_PIN_29_ANY_INT NXP_WUU_PIN(29, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 29 的任意边沿中断（Pin 29 any edge interrupt）。

<a id="ae938a8480eecd7aff325dbadef529fbf"></a>

### `NXP_WUU_PIN_29_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_29_ANY_TRIGGER NXP_WUU_PIN(29, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 29 的任意边沿触发输出（Pin 29 any edge trigger）。

<a id="a24c5047eedac8ea7317f21b5a187c508"></a>

### `NXP_WUU_PIN_29_FALLING_DMA`

```c
#define NXP_WUU_PIN_29_FALLING_DMA NXP_WUU_PIN(29, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 29 的下降沿直接存储器访问请求（Pin 29 falling edge DMA）。

<a id="a943872b62aef9bcb3fb1c9ffcc227535"></a>

### `NXP_WUU_PIN_29_FALLING_INT`

```c
#define NXP_WUU_PIN_29_FALLING_INT NXP_WUU_PIN(29, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 29 的下降沿中断（Pin 29 falling edge interrupt）。

<a id="abe948ad4554aaba19d1acaedc28ac9eb"></a>

### `NXP_WUU_PIN_29_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_29_FALLING_TRIGGER NXP_WUU_PIN(29, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 29 的下降沿触发输出（Pin 29 falling edge trigger）。

<a id="aa8aa9d173cb3d631d02d56fc1633f948"></a>

### `NXP_WUU_PIN_29_RISING_DMA`

```c
#define NXP_WUU_PIN_29_RISING_DMA NXP_WUU_PIN(29, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 29 的上升沿直接存储器访问请求（Pin 29 rising edge DMA）。

<a id="ae038b3a246101fa06346d4d6c409306e"></a>

### `NXP_WUU_PIN_29_RISING_INT`

```c
#define NXP_WUU_PIN_29_RISING_INT NXP_WUU_PIN(29, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 29 的上升沿中断（Pin 29 rising edge interrupt）。

<a id="a0531e427d93d586fa8d959c5d8550d56"></a>

### `NXP_WUU_PIN_29_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_29_RISING_TRIGGER NXP_WUU_PIN(29, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 29 的上升沿触发输出（Pin 29 rising edge trigger）。

<a id="a189200efbd1d8a32222b626643cc9aa0"></a>

### `NXP_WUU_PIN_2_ANY_DMA`

```c
#define NXP_WUU_PIN_2_ANY_DMA NXP_WUU_PIN(2, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 2 的任意边沿直接存储器访问请求（Pin 2 any edge DMA）。

<a id="ad3c929fd00d7ef13d4fce5bf05354d42"></a>

### `NXP_WUU_PIN_2_ANY_INT`

```c
#define NXP_WUU_PIN_2_ANY_INT NXP_WUU_PIN(2, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 2 的任意边沿中断（Pin 2 any edge interrupt）。

<a id="ae002d606053d5dfc818cc6decd0f5344"></a>

### `NXP_WUU_PIN_2_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_2_ANY_TRIGGER NXP_WUU_PIN(2, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 2 的任意边沿触发输出（Pin 2 any edge trigger）。

<a id="ad094c074f68621557b20f692c10f7852"></a>

### `NXP_WUU_PIN_2_FALLING_DMA`

```c
#define NXP_WUU_PIN_2_FALLING_DMA NXP_WUU_PIN(2, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 2 的下降沿直接存储器访问请求（Pin 2 falling edge DMA）。

<a id="a829b2582b7bda3f86b53118691bbf9ad"></a>

### `NXP_WUU_PIN_2_FALLING_INT`

```c
#define NXP_WUU_PIN_2_FALLING_INT NXP_WUU_PIN(2, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 2 的下降沿中断（Pin 2 falling edge interrupt）。

<a id="a85246cda06850b9c7470710b50fcb067"></a>

### `NXP_WUU_PIN_2_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_2_FALLING_TRIGGER NXP_WUU_PIN(2, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 2 的下降沿触发输出（Pin 2 falling edge trigger）。

<a id="a84d9e6be844a6900e828f8985fe51f02"></a>

### `NXP_WUU_PIN_2_RISING_DMA`

```c
#define NXP_WUU_PIN_2_RISING_DMA NXP_WUU_PIN(2, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 2 的上升沿直接存储器访问请求（Pin 2 rising edge DMA）。

<a id="a065e54fcd117c45abfdef2b34e012dbc"></a>

### `NXP_WUU_PIN_2_RISING_INT`

```c
#define NXP_WUU_PIN_2_RISING_INT NXP_WUU_PIN(2, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 2 的上升沿中断（Pin 2 rising edge interrupt）。

<a id="a88e4dd24b7fbf8133808822fac85d0b3"></a>

### `NXP_WUU_PIN_2_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_2_RISING_TRIGGER NXP_WUU_PIN(2, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 2 的上升沿触发输出（Pin 2 rising edge trigger）。

<a id="a3eea2af7b44504449adf6e19dce9a591"></a>

### `NXP_WUU_PIN_30_ANY_DMA`

```c
#define NXP_WUU_PIN_30_ANY_DMA NXP_WUU_PIN(30, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 30 的任意边沿直接存储器访问请求（Pin 30 any edge DMA）。

<a id="ab922f612cafced3392ec6d8809c5f8ee"></a>

### `NXP_WUU_PIN_30_ANY_INT`

```c
#define NXP_WUU_PIN_30_ANY_INT NXP_WUU_PIN(30, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 30 的任意边沿中断（Pin 30 any edge interrupt）。

<a id="ad984888d667e38c0d527da6b848554b3"></a>

### `NXP_WUU_PIN_30_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_30_ANY_TRIGGER NXP_WUU_PIN(30, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 30 的任意边沿触发输出（Pin 30 any edge trigger）。

<a id="a10f8ad477d538497b07923b2dd3d4d6a"></a>

### `NXP_WUU_PIN_30_FALLING_DMA`

```c
#define NXP_WUU_PIN_30_FALLING_DMA NXP_WUU_PIN(30, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 30 的下降沿直接存储器访问请求（Pin 30 falling edge DMA）。

<a id="a0ca83ab747500f453b0e88a918482546"></a>

### `NXP_WUU_PIN_30_FALLING_INT`

```c
#define NXP_WUU_PIN_30_FALLING_INT NXP_WUU_PIN(30, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 30 的下降沿中断（Pin 30 falling edge interrupt）。

<a id="ae457b538bc805cd2a25202457efd4ecf"></a>

### `NXP_WUU_PIN_30_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_30_FALLING_TRIGGER NXP_WUU_PIN(30, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 30 的下降沿触发输出（Pin 30 falling edge trigger）。

<a id="a656177c37d72970453a788b931f27f30"></a>

### `NXP_WUU_PIN_30_RISING_DMA`

```c
#define NXP_WUU_PIN_30_RISING_DMA NXP_WUU_PIN(30, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 30 的上升沿直接存储器访问请求（Pin 30 rising edge DMA）。

<a id="a66ccadf7c0cc89fd90f559c28efe6f8a"></a>

### `NXP_WUU_PIN_30_RISING_INT`

```c
#define NXP_WUU_PIN_30_RISING_INT NXP_WUU_PIN(30, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 30 的上升沿中断（Pin 30 rising edge interrupt）。

<a id="a99b22a9abb8a1b5cd76dad1cce2566fc"></a>

### `NXP_WUU_PIN_30_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_30_RISING_TRIGGER NXP_WUU_PIN(30, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 30 的上升沿触发输出（Pin 30 rising edge trigger）。

<a id="a517f82f1fbcdfa4e21e7053bad48adad"></a>

### `NXP_WUU_PIN_31_ANY_DMA`

```c
#define NXP_WUU_PIN_31_ANY_DMA NXP_WUU_PIN(31, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 31 的任意边沿直接存储器访问请求（Pin 31 any edge DMA）。

<a id="aa2000a701abe50eaed661369cb766a86"></a>

### `NXP_WUU_PIN_31_ANY_INT`

```c
#define NXP_WUU_PIN_31_ANY_INT NXP_WUU_PIN(31, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 31 的任意边沿中断（Pin 31 any edge interrupt）。

<a id="a532c12001131d9de5f8acecce5c095b5"></a>

### `NXP_WUU_PIN_31_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_31_ANY_TRIGGER NXP_WUU_PIN(31, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 31 的任意边沿触发输出（Pin 31 any edge trigger）。

<a id="a2bad33398fd39840a96814846ee09bf0"></a>

### `NXP_WUU_PIN_31_FALLING_DMA`

```c
#define NXP_WUU_PIN_31_FALLING_DMA NXP_WUU_PIN(31, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 31 的下降沿直接存储器访问请求（Pin 31 falling edge DMA）。

<a id="a4e442cd96c8ab316262369f3d5fdb979"></a>

### `NXP_WUU_PIN_31_FALLING_INT`

```c
#define NXP_WUU_PIN_31_FALLING_INT NXP_WUU_PIN(31, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 31 的下降沿中断（Pin 31 falling edge interrupt）。

<a id="a8f0010fbc10ba1db35c14688a9acfd25"></a>

### `NXP_WUU_PIN_31_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_31_FALLING_TRIGGER NXP_WUU_PIN(31, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 31 的下降沿触发输出（Pin 31 falling edge trigger）。

<a id="abdbc6eae346325c5bde7267425951dce"></a>

### `NXP_WUU_PIN_31_RISING_DMA`

```c
#define NXP_WUU_PIN_31_RISING_DMA NXP_WUU_PIN(31, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 31 的上升沿直接存储器访问请求（Pin 31 rising edge DMA）。

<a id="abeb326af95c992cb7a4777e80c069e11"></a>

### `NXP_WUU_PIN_31_RISING_INT`

```c
#define NXP_WUU_PIN_31_RISING_INT NXP_WUU_PIN(31, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 31 的上升沿中断（Pin 31 rising edge interrupt）。

<a id="a780acac9ae801d0fa9470d8779dfe399"></a>

### `NXP_WUU_PIN_31_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_31_RISING_TRIGGER NXP_WUU_PIN(31, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 31 的上升沿触发输出（Pin 31 rising edge trigger）。

<a id="aabbd3a817a790f26c62b6e2174fe07ca"></a>

### `NXP_WUU_PIN_3_ANY_DMA`

```c
#define NXP_WUU_PIN_3_ANY_DMA NXP_WUU_PIN(3, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 3 的任意边沿直接存储器访问请求（Pin 3 any edge DMA）。

<a id="a737c61948f5a33d352ed0f356239da0a"></a>

### `NXP_WUU_PIN_3_ANY_INT`

```c
#define NXP_WUU_PIN_3_ANY_INT NXP_WUU_PIN(3, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 3 的任意边沿中断（Pin 3 any edge interrupt）。

<a id="aa24891983beba114925065478cdb0d02"></a>

### `NXP_WUU_PIN_3_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_3_ANY_TRIGGER NXP_WUU_PIN(3, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 3 的任意边沿触发输出（Pin 3 any edge trigger）。

<a id="aec1e5d52cd412af5a559472ee40e5807"></a>

### `NXP_WUU_PIN_3_FALLING_DMA`

```c
#define NXP_WUU_PIN_3_FALLING_DMA NXP_WUU_PIN(3, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 3 的下降沿直接存储器访问请求（Pin 3 falling edge DMA）。

<a id="af7134ed647faed2cf54849fb5829bcd1"></a>

### `NXP_WUU_PIN_3_FALLING_INT`

```c
#define NXP_WUU_PIN_3_FALLING_INT NXP_WUU_PIN(3, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 3 的下降沿中断（Pin 3 falling edge interrupt）。

<a id="a8a20192b0b8972eb651043634844affa"></a>

### `NXP_WUU_PIN_3_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_3_FALLING_TRIGGER NXP_WUU_PIN(3, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 3 的下降沿触发输出（Pin 3 falling edge trigger）。

<a id="a156b3b7b038161a5757ea6945fe6f7cd"></a>

### `NXP_WUU_PIN_3_RISING_DMA`

```c
#define NXP_WUU_PIN_3_RISING_DMA NXP_WUU_PIN(3, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 3 的上升沿直接存储器访问请求（Pin 3 rising edge DMA）。

<a id="a35ae0792e0b716d46b82bab627965116"></a>

### `NXP_WUU_PIN_3_RISING_INT`

```c
#define NXP_WUU_PIN_3_RISING_INT NXP_WUU_PIN(3, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 3 的上升沿中断（Pin 3 rising edge interrupt）。

<a id="a4574d79575dabc93c3afca157e0bdeb8"></a>

### `NXP_WUU_PIN_3_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_3_RISING_TRIGGER NXP_WUU_PIN(3, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 3 的上升沿触发输出（Pin 3 rising edge trigger）。

<a id="a1de265d095d774fec9fa26820cb90e2e"></a>

### `NXP_WUU_PIN_4_ANY_DMA`

```c
#define NXP_WUU_PIN_4_ANY_DMA NXP_WUU_PIN(4, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 4 的任意边沿直接存储器访问请求（Pin 4 any edge DMA）。

<a id="a0679a44abb91b4404142fe0abc2c9f0d"></a>

### `NXP_WUU_PIN_4_ANY_INT`

```c
#define NXP_WUU_PIN_4_ANY_INT NXP_WUU_PIN(4, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 4 的任意边沿中断（Pin 4 any edge interrupt）。

<a id="a64ab721b978a687974af47dadb5c9779"></a>

### `NXP_WUU_PIN_4_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_4_ANY_TRIGGER NXP_WUU_PIN(4, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 4 的任意边沿触发输出（Pin 4 any edge trigger）。

<a id="a53c4b1d915699ee902639539954e9bca"></a>

### `NXP_WUU_PIN_4_FALLING_DMA`

```c
#define NXP_WUU_PIN_4_FALLING_DMA NXP_WUU_PIN(4, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 4 的下降沿直接存储器访问请求（Pin 4 falling edge DMA）。

<a id="a221d7a4d5e96e7c8202fe51bf630a626"></a>

### `NXP_WUU_PIN_4_FALLING_INT`

```c
#define NXP_WUU_PIN_4_FALLING_INT NXP_WUU_PIN(4, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 4 的下降沿中断（Pin 4 falling edge interrupt）。

<a id="aedfec85e539e3f2001fb0290c43ed422"></a>

### `NXP_WUU_PIN_4_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_4_FALLING_TRIGGER NXP_WUU_PIN(4, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 4 的下降沿触发输出（Pin 4 falling edge trigger）。

<a id="a0d5228f868cb0a56a5d5b74006b1223e"></a>

### `NXP_WUU_PIN_4_RISING_DMA`

```c
#define NXP_WUU_PIN_4_RISING_DMA NXP_WUU_PIN(4, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 4 的上升沿直接存储器访问请求（Pin 4 rising edge DMA）。

<a id="a03ffa3bf5c3edd6d91dff43ca2538b9b"></a>

### `NXP_WUU_PIN_4_RISING_INT`

```c
#define NXP_WUU_PIN_4_RISING_INT NXP_WUU_PIN(4, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 4 的上升沿中断（Pin 4 rising edge interrupt）。

<a id="a04b515a0005e1662a864a05ccc0e04b8"></a>

### `NXP_WUU_PIN_4_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_4_RISING_TRIGGER NXP_WUU_PIN(4, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 4 的上升沿触发输出（Pin 4 rising edge trigger）。

<a id="a5f98a8f759dbab2c7e55e9b8a3fe4efe"></a>

### `NXP_WUU_PIN_5_ANY_DMA`

```c
#define NXP_WUU_PIN_5_ANY_DMA NXP_WUU_PIN(5, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 5 的任意边沿直接存储器访问请求（Pin 5 any edge DMA）。

<a id="a26841234d383fbfee40a1f30d23882ba"></a>

### `NXP_WUU_PIN_5_ANY_INT`

```c
#define NXP_WUU_PIN_5_ANY_INT NXP_WUU_PIN(5, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 5 的任意边沿中断（Pin 5 any edge interrupt）。

<a id="a90fee494887f96b13ccaf091bc583a3e"></a>

### `NXP_WUU_PIN_5_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_5_ANY_TRIGGER NXP_WUU_PIN(5, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 5 的任意边沿触发输出（Pin 5 any edge trigger）。

<a id="aba5b3ed4b607afc26d0d16e923a2b7f2"></a>

### `NXP_WUU_PIN_5_FALLING_DMA`

```c
#define NXP_WUU_PIN_5_FALLING_DMA NXP_WUU_PIN(5, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 5 的下降沿直接存储器访问请求（Pin 5 falling edge DMA）。

<a id="a20855781ffe40aadb8909da13d175bab"></a>

### `NXP_WUU_PIN_5_FALLING_INT`

```c
#define NXP_WUU_PIN_5_FALLING_INT NXP_WUU_PIN(5, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 5 的下降沿中断（Pin 5 falling edge interrupt）。

<a id="ac00de1cc83661c503630f8add5763f62"></a>

### `NXP_WUU_PIN_5_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_5_FALLING_TRIGGER NXP_WUU_PIN(5, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 5 的下降沿触发输出（Pin 5 falling edge trigger）。

<a id="a7fdc593f1390bff7b96e0cfaa2824dbf"></a>

### `NXP_WUU_PIN_5_RISING_DMA`

```c
#define NXP_WUU_PIN_5_RISING_DMA NXP_WUU_PIN(5, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 5 的上升沿直接存储器访问请求（Pin 5 rising edge DMA）。

<a id="acaaa8970ac212cb84264eb4171684c62"></a>

### `NXP_WUU_PIN_5_RISING_INT`

```c
#define NXP_WUU_PIN_5_RISING_INT NXP_WUU_PIN(5, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 5 的上升沿中断（Pin 5 rising edge interrupt）。

<a id="a7f302101a226e9288223a3b62ed3ab24"></a>

### `NXP_WUU_PIN_5_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_5_RISING_TRIGGER NXP_WUU_PIN(5, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 5 的上升沿触发输出（Pin 5 rising edge trigger）。

<a id="af7a115cb95d28d7195cce12155a35f9e"></a>

### `NXP_WUU_PIN_6_ANY_DMA`

```c
#define NXP_WUU_PIN_6_ANY_DMA NXP_WUU_PIN(6, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 6 的任意边沿直接存储器访问请求（Pin 6 any edge DMA）。

<a id="a752d52864160dc25cc25874871dcba6c"></a>

### `NXP_WUU_PIN_6_ANY_INT`

```c
#define NXP_WUU_PIN_6_ANY_INT NXP_WUU_PIN(6, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 6 的任意边沿中断（Pin 6 any edge interrupt）。

<a id="ac1b311ddfc3000eec9df3b82cd14704b"></a>

### `NXP_WUU_PIN_6_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_6_ANY_TRIGGER NXP_WUU_PIN(6, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 6 的任意边沿触发输出（Pin 6 any edge trigger）。

<a id="a4bba8ac0ac94dc3248639b542bc4596f"></a>

### `NXP_WUU_PIN_6_FALLING_DMA`

```c
#define NXP_WUU_PIN_6_FALLING_DMA NXP_WUU_PIN(6, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 6 的下降沿直接存储器访问请求（Pin 6 falling edge DMA）。

<a id="a036c6d65349a3abf5fcebf990d9e63e0"></a>

### `NXP_WUU_PIN_6_FALLING_INT`

```c
#define NXP_WUU_PIN_6_FALLING_INT NXP_WUU_PIN(6, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 6 的下降沿中断（Pin 6 falling edge interrupt）。

<a id="acf56e5732e701ddad7f21595b13f33f6"></a>

### `NXP_WUU_PIN_6_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_6_FALLING_TRIGGER NXP_WUU_PIN(6, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 6 的下降沿触发输出（Pin 6 falling edge trigger）。

<a id="ac6f14a518aeb2d0312cde5eef8a1d27f"></a>

### `NXP_WUU_PIN_6_RISING_DMA`

```c
#define NXP_WUU_PIN_6_RISING_DMA NXP_WUU_PIN(6, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 6 的上升沿直接存储器访问请求（Pin 6 rising edge DMA）。

<a id="aedd93d9766b02eb9b9ad88240dde6602"></a>

### `NXP_WUU_PIN_6_RISING_INT`

```c
#define NXP_WUU_PIN_6_RISING_INT NXP_WUU_PIN(6, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 6 的上升沿中断（Pin 6 rising edge interrupt）。

<a id="af0749213c8d920cd41347f90891b1bd1"></a>

### `NXP_WUU_PIN_6_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_6_RISING_TRIGGER NXP_WUU_PIN(6, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 6 的上升沿触发输出（Pin 6 rising edge trigger）。

<a id="ad13c89d41a3cf9c9e971cb3a8ef4c1e4"></a>

### `NXP_WUU_PIN_7_ANY_DMA`

```c
#define NXP_WUU_PIN_7_ANY_DMA NXP_WUU_PIN(7, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 7 的任意边沿直接存储器访问请求（Pin 7 any edge DMA）。

<a id="aee7ae97ed373dbd8bc3d315260eb3e5c"></a>

### `NXP_WUU_PIN_7_ANY_INT`

```c
#define NXP_WUU_PIN_7_ANY_INT NXP_WUU_PIN(7, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 7 的任意边沿中断（Pin 7 any edge interrupt）。

<a id="abb5df8e6ff7af5e4a0a4f08e61a47d97"></a>

### `NXP_WUU_PIN_7_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_7_ANY_TRIGGER NXP_WUU_PIN(7, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 7 的任意边沿触发输出（Pin 7 any edge trigger）。

<a id="add18fd6736de55936cc29571a51754c6"></a>

### `NXP_WUU_PIN_7_FALLING_DMA`

```c
#define NXP_WUU_PIN_7_FALLING_DMA NXP_WUU_PIN(7, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 7 的下降沿直接存储器访问请求（Pin 7 falling edge DMA）。

<a id="acb5ab244dad84bb053bcf74bb6a6c81f"></a>

### `NXP_WUU_PIN_7_FALLING_INT`

```c
#define NXP_WUU_PIN_7_FALLING_INT NXP_WUU_PIN(7, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 7 的下降沿中断（Pin 7 falling edge interrupt）。

<a id="a7fabee54875e2ca9be3b5a5a03851173"></a>

### `NXP_WUU_PIN_7_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_7_FALLING_TRIGGER NXP_WUU_PIN(7, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 7 的下降沿触发输出（Pin 7 falling edge trigger）。

<a id="a50ebf181f3be451a10615450efcb251b"></a>

### `NXP_WUU_PIN_7_RISING_DMA`

```c
#define NXP_WUU_PIN_7_RISING_DMA NXP_WUU_PIN(7, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 7 的上升沿直接存储器访问请求（Pin 7 rising edge DMA）。

<a id="a8b21a3c4f017be5430eeecdc2d641cb8"></a>

### `NXP_WUU_PIN_7_RISING_INT`

```c
#define NXP_WUU_PIN_7_RISING_INT NXP_WUU_PIN(7, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 7 的上升沿中断（Pin 7 rising edge interrupt）。

<a id="ae0c98281fd53d8f03a533c7a4460700a"></a>

### `NXP_WUU_PIN_7_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_7_RISING_TRIGGER NXP_WUU_PIN(7, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 7 的上升沿触发输出（Pin 7 rising edge trigger）。

<a id="a392a466f5148cb8eb32f0b12bd38904e"></a>

### `NXP_WUU_PIN_8_ANY_DMA`

```c
#define NXP_WUU_PIN_8_ANY_DMA NXP_WUU_PIN(8, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 8 的任意边沿直接存储器访问请求（Pin 8 any edge DMA）。

<a id="ab15c905cc40563b658ec1522af9887e9"></a>

### `NXP_WUU_PIN_8_ANY_INT`

```c
#define NXP_WUU_PIN_8_ANY_INT NXP_WUU_PIN(8, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 8 的任意边沿中断（Pin 8 any edge interrupt）。

<a id="a29d76ec9b7ae3f611944b140d6fc6aa2"></a>

### `NXP_WUU_PIN_8_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_8_ANY_TRIGGER NXP_WUU_PIN(8, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 8 的任意边沿触发输出（Pin 8 any edge trigger）。

<a id="a66cb9726ac60da282bcfa7be7e041ff7"></a>

### `NXP_WUU_PIN_8_FALLING_DMA`

```c
#define NXP_WUU_PIN_8_FALLING_DMA NXP_WUU_PIN(8, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 8 的下降沿直接存储器访问请求（Pin 8 falling edge DMA）。

<a id="a1f8e0e7b12c2a3f8e0bdc60f1c219f5f"></a>

### `NXP_WUU_PIN_8_FALLING_INT`

```c
#define NXP_WUU_PIN_8_FALLING_INT NXP_WUU_PIN(8, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 8 的下降沿中断（Pin 8 falling edge interrupt）。

<a id="adb784db06fa54157da7fc09f848a8d83"></a>

### `NXP_WUU_PIN_8_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_8_FALLING_TRIGGER NXP_WUU_PIN(8, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 8 的下降沿触发输出（Pin 8 falling edge trigger）。

<a id="a8620ba95a59f4817c28b9987bddee80d"></a>

### `NXP_WUU_PIN_8_RISING_DMA`

```c
#define NXP_WUU_PIN_8_RISING_DMA NXP_WUU_PIN(8, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 8 的上升沿直接存储器访问请求（Pin 8 rising edge DMA）。

<a id="a191fa35fc706ffb26703a48fd0cdcddf"></a>

### `NXP_WUU_PIN_8_RISING_INT`

```c
#define NXP_WUU_PIN_8_RISING_INT NXP_WUU_PIN(8, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 8 的上升沿中断（Pin 8 rising edge interrupt）。

<a id="af7cf40dbc62bea416bd94ee894e978f2"></a>

### `NXP_WUU_PIN_8_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_8_RISING_TRIGGER NXP_WUU_PIN(8, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 8 的上升沿触发输出（Pin 8 rising edge trigger）。

<a id="aa9750dfe149398cc3bdb992b8fe17d0c"></a>

### `NXP_WUU_PIN_9_ANY_DMA`

```c
#define NXP_WUU_PIN_9_ANY_DMA NXP_WUU_PIN(9, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_DMA)
```

引脚 9 的任意边沿直接存储器访问请求（Pin 9 any edge DMA）。

<a id="af757f93d5d859727a7018163cb1cbbc2"></a>

### `NXP_WUU_PIN_9_ANY_INT`

```c
#define NXP_WUU_PIN_9_ANY_INT NXP_WUU_PIN(9, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_INT)
```

引脚 9 的任意边沿中断（Pin 9 any edge interrupt）。

<a id="a40b12fedf163e1e3ff5100bbcf487561"></a>

### `NXP_WUU_PIN_9_ANY_TRIGGER`

```c
#define NXP_WUU_PIN_9_ANY_TRIGGER NXP_WUU_PIN(9, NXP_WUU_EDGE_ANY, NXP_WUU_EVENT_TRIGGER)
```

引脚 9 的任意边沿触发输出（Pin 9 any edge trigger）。

<a id="a97fecb5180baa34818e5993ea876cd73"></a>

### `NXP_WUU_PIN_9_FALLING_DMA`

```c
#define NXP_WUU_PIN_9_FALLING_DMA NXP_WUU_PIN(9, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_DMA)
```

引脚 9 的下降沿直接存储器访问请求（Pin 9 falling edge DMA）。

<a id="abbb695600abf970fbbc1f69fed0ade4c"></a>

### `NXP_WUU_PIN_9_FALLING_INT`

```c
#define NXP_WUU_PIN_9_FALLING_INT NXP_WUU_PIN(9, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_INT)
```

引脚 9 的下降沿中断（Pin 9 falling edge interrupt）。

<a id="af44aba7a609b0e1fc7ac6aac9db5f5a4"></a>

### `NXP_WUU_PIN_9_FALLING_TRIGGER`

```c
#define NXP_WUU_PIN_9_FALLING_TRIGGER NXP_WUU_PIN(9, NXP_WUU_EDGE_FALLING, NXP_WUU_EVENT_TRIGGER)
```

引脚 9 的下降沿触发输出（Pin 9 falling edge trigger）。

<a id="a9e91e5cf898c0a4e722b4a7414cef455"></a>

### `NXP_WUU_PIN_9_RISING_DMA`

```c
#define NXP_WUU_PIN_9_RISING_DMA NXP_WUU_PIN(9, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_DMA)
```

引脚 9 的上升沿直接存储器访问请求（Pin 9 rising edge DMA）。

<a id="ad465da00c578d048d17f1d0383ac27b2"></a>

### `NXP_WUU_PIN_9_RISING_INT`

```c
#define NXP_WUU_PIN_9_RISING_INT NXP_WUU_PIN(9, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_INT)
```

引脚 9 的上升沿中断（Pin 9 rising edge interrupt）。

<a id="a458a8c7e2c108a7ec044d900bc3fdde2"></a>

### `NXP_WUU_PIN_9_RISING_TRIGGER`

```c
#define NXP_WUU_PIN_9_RISING_TRIGGER NXP_WUU_PIN(9, NXP_WUU_EDGE_RISING, NXP_WUU_EVENT_TRIGGER)
```

引脚 9 的上升沿触发输出（Pin 9 rising edge trigger）。

<a id="a73731f505cb4a94a4b34fd428734c70b"></a>

### `NXP_WUU_SOURCE_EDGE_POS`

```c
#define NXP_WUU_SOURCE_EDGE_POS 8
```

边沿类型字段（Edge-type Field）的位位置，仅用于 PIN 源。

<a id="a6eb529e0f845770faa06b88454ca09e5"></a>

### `NXP_WUU_SOURCE_EVENT_POS`

```c
#define NXP_WUU_SOURCE_EVENT_POS 0
```

事件类型字段（Event-type Field）的位位置。

<a id="a81cb0ae5e3e2f756c1ffa512df55cc84"></a>

### `NXP_WUU_SOURCE_INDEX_POS`

```c
#define NXP_WUU_SOURCE_INDEX_POS 16
```

索引字段（Index Field）的位位置，即引脚或模块编号所在字段。

<a id="a0507ef26fd272e9cbe32a610493c53ce"></a>

### `NXP_WUU_SOURCE_MASK`

```c
#define NXP_WUU_SOURCE_MASK 0xFF
```

覆盖编码唤醒源中一个 8 位字段的掩码（Mask）。

<a id="a890e5418a2e669f6244cd5004c68367a"></a>

### `NXP_WUU_SOURCE_TYPE_MODULE`

```c
#define NXP_WUU_SOURCE_TYPE_MODULE 1
```

源类型值（Source-type Value）：内部外设模块。

<a id="a855b0d5f35a46702544758ed3a5b6f3f"></a>

### `NXP_WUU_SOURCE_TYPE_PIN`

```c
#define NXP_WUU_SOURCE_TYPE_PIN 0
```

源类型值（Source-type Value）：外部 WUU 引脚。

<a id="a769e1ef3d9e96a6afad8ea17828cc050"></a>

### `NXP_WUU_SOURCE_TYPE_POS`

```c
#define NXP_WUU_SOURCE_TYPE_POS 24
```

编码唤醒源中源类型字段（Source-type Field）的位位置。

<a id="ad7bc71c642cc4124e11c73a88dd6aa4f"></a>

### `NXP_WUU_WAKEUP_SOURCE_DECODE`

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE ( source, pos )
```

展开值（Value）：

```c
(((source) >> (pos)) & NXP_WUU_SOURCE_MASK)
```

从编码唤醒源（Encoded Wakeup Source）中提取一个 8 位字段。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 编码后的唤醒源值（Encoded Wakeup Source Value）。 |
| `pos` | 字段位位置（Bit Position），为 `NXP_WUU_SOURCE_*_POS` 之一。 |

<a id="a4c6d253dd543e140f48eb1bca57a84af"></a>

### `NXP_WUU_WAKEUP_SOURCE_DECODE_EDGE`

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE_EDGE ( source)
```

展开值（Value）：

```c
NXP_WUU_WAKEUP_SOURCE_DECODE(source, NXP_WUU_SOURCE_EDGE_POS)
```

解码边沿类型字段（Edge-type Field），仅对 PIN 源有意义。

<a id="acc2c876066de244451ac99027f686e7a"></a>

### `NXP_WUU_WAKEUP_SOURCE_DECODE_EVENT`

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE_EVENT ( source)
```

展开值（Value）：

```c
NXP_WUU_WAKEUP_SOURCE_DECODE(source, NXP_WUU_SOURCE_EVENT_POS)
```

解码唤醒源的事件类型字段（Event-type Field）。

<a id="abfe9ad605f2bcc78b96358cf092c7274"></a>

### `NXP_WUU_WAKEUP_SOURCE_DECODE_INDEX`

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE_INDEX ( source)
```

展开值（Value）：

```c
NXP_WUU_WAKEUP_SOURCE_DECODE(source, NXP_WUU_SOURCE_INDEX_POS)
```

解码索引字段（Index Field），即引脚或模块编号。

<a id="af35ec75d34b9df3fe74f939376b4f99d"></a>

### `NXP_WUU_WAKEUP_SOURCE_DECODE_TYPE`

```c
#define NXP_WUU_WAKEUP_SOURCE_DECODE_TYPE ( source)
```

展开值（Value）：

```c
NXP_WUU_WAKEUP_SOURCE_DECODE(source, NXP_WUU_SOURCE_TYPE_POS)
```

解码唤醒源的源类型字段（Source-type Field）。

<a id="ad39e976e86b11e57096e46d781f83c17"></a>

### `NXP_WUU_WAKEUP_SOURCE_ENCODE`

```c
#define NXP_WUU_WAKEUP_SOURCE_ENCODE ( type, index, edge, event )
```

展开值（Value）：

```c
(((type) << NXP_WUU_SOURCE_TYPE_POS) | ((index) << NXP_WUU_SOURCE_INDEX_POS) |             \
 ((edge) << NXP_WUU_SOURCE_EDGE_POS) | ((event) << NXP_WUU_SOURCE_EVENT_POS))
```

将 WUU 唤醒源（Wakeup Source）编码为单个 32 位值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 源类型（Source Type），为 `NXP_WUU_SOURCE_TYPE_PIN` 或 `NXP_WUU_SOURCE_TYPE_MODULE`。 |
| `index` | 引脚或模块索引（Index）。 |
| `edge` | 边沿类型（Edge Type），为 `NXP_WUU_EDGE_*`；对于 MODULE 源忽略此值。 |
| `event` | 事件类型（Event Type），为 `NXP_WUU_EVENT_*`。 |


## 7.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_http_wifi_reference/P010_wuc_nxp_wuu.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="awuc__nxp__wuu_8h_html_a890e5418a2e669f6244cd5004c68367a"></a>
<a id="awuc__nxp__wuu_8h_html_af35ec75d34b9df3fe74f939376b4f99d"></a>
<a id="awuc__nxp__wuu_8h_html_a855b0d5f35a46702544758ed3a5b6f3f"></a>
<a id="awuc__nxp__wuu_8h_html_ad39e976e86b11e57096e46d781f83c17"></a>
<a id="awuc__nxp__wuu_8h_html_a0507ef26fd272e9cbe32a610493c53ce"></a>
<a id="awuc__nxp__wuu_8h_html_a73731f505cb4a94a4b34fd428734c70b"></a>
<a id="awuc__nxp__wuu_8h_html_ad7bc71c642cc4124e11c73a88dd6aa4f"></a>
<a id="awuc__nxp__wuu_8h_html_a6eb529e0f845770faa06b88454ca09e5"></a>
<a id="awuc__nxp__wuu_8h_html_a81cb0ae5e3e2f756c1ffa512df55cc84"></a>
<a id="awuc__nxp__wuu_8h_html_a769e1ef3d9e96a6afad8ea17828cc050"></a>

---

[上一章](P006_zephyr__usb_c__tcpci.h_文件参考.md) · [返回大纲](大纲.md)
