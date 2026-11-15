---
id: learning.zephyr-docs.api-file-reference.page-173
title: zephyr__irq.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/irq_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第173章\_zephyr\_\_irq.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

中断配置（Configuring Interrupts）的公共接口。

<a id="details"></a>

```c
#include <zephyr/arch/cpu.h>
#include <limits.h>
#include <stdbool.h>
#include <zephyr/toolchain.h>
#include <zephyr/types.h>
```

查看此文件的源码。

中断配置（Configuring Interrupts）的公共接口。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 173.1\_宏定义（Macros）

<a id="r_ga131739d1faf501a15590053817aba984"></a>

```c
#define IRQ_CONNECT(irq_p, priority_p, isr_p, isr_param_p, flags_p)
```

相关声明：[IRQ_CONNECT](../fatal_irq_reference/P007_中断服务接口.md#ga131739d1faf501a15590053817aba984)。

初始化中断处理函数（Interrupt Handler）。

<a id="r_gac6c8746ac28da6ce02b24714f4144ff3"></a>

```c
#define IRQ_DIRECT_CONNECT(irq_p, priority_p, isr_p, flags_p)
```

相关声明：[IRQ_DIRECT_CONNECT](../fatal_irq_reference/P007_中断服务接口.md#gac6c8746ac28da6ce02b24714f4144ff3)。

初始化直接中断处理函数（Direct Interrupt Handler）。

<a id="r_ga1ab99dbeb50b228001e1fca808cbaeea"></a>

```c
#define ISR_DIRECT_HEADER()
```

相关声明：[ISR_DIRECT_HEADER](../fatal_irq_reference/P007_中断服务接口.md#ga1ab99dbeb50b228001e1fca808cbaeea)。

执行中断服务例程（Interrupt Service Routine，ISR）主体之前的公共操作。

<a id="r_ga31581157c9dbacf935f0e6a8dd456335"></a>

```c
#define ISR_DIRECT_FOOTER(check_reschedule)
```

相关声明：[ISR_DIRECT_FOOTER](../fatal_irq_reference/P007_中断服务接口.md#ga31581157c9dbacf935f0e6a8dd456335)。

退出 ISR 主体之前的公共操作。

<a id="r_ga3c1327551dfca7818975e3fbf1470227"></a>

```c
#define ISR_DIRECT_PM()
```

相关声明：[ISR_DIRECT_PM](../fatal_irq_reference/P007_中断服务接口.md#ga3c1327551dfca7818975e3fbf1470227)。

执行电源管理的空闲退出逻辑（Power Management Idle Exit）。

<a id="r_gaf86866cd07fd37f381d98866f8874ebf"></a>

```c
#define ISR_DIRECT_DECLARE(name)
```

相关声明：[ISR_DIRECT_DECLARE](../fatal_irq_reference/P007_中断服务接口.md#gaf86866cd07fd37f381d98866f8874ebf)。

声明直接中断服务例程的辅助宏。

<a id="r_ga19fdde73c3b02fcca6cf1d1e67631228"></a>

```c
#define irq_lock()
```

相关声明：[irq_lock](../fatal_irq_reference/P007_中断服务接口.md#ga19fdde73c3b02fcca6cf1d1e67631228)。

锁定中断（Lock Interrupts）。

<a id="r_ga646045943b3b2a130738bcc48867bf57"></a>

```c
#define irq_unlock(key)
```

相关声明：[irq_unlock](../fatal_irq_reference/P007_中断服务接口.md#ga646045943b3b2a130738bcc48867bf57)。

解除中断锁定（Unlock Interrupts）。

<a id="r_ga7ea700ee31e4ff036c997a554dbedfeb"></a>

```c
#define irq_enable(irq)
```

相关声明：[irq_enable](../fatal_irq_reference/P007_中断服务接口.md#ga7ea700ee31e4ff036c997a554dbedfeb)。

使能一个中断请求（Interrupt Request，IRQ）。

<a id="r_ga82c3a15d812f58e0f6525f358d031e6d"></a>

```c
#define irq_disable(irq)
```

相关声明：[irq_disable](../fatal_irq_reference/P007_中断服务接口.md#ga82c3a15d812f58e0f6525f358d031e6d)。

禁用一个 IRQ。

<a id="r_ga71fef3867ba9818cf0a5baf8410a6354"></a>

```c
#define irq_is_enabled(irq)
```

相关声明：[irq_is_enabled](../fatal_irq_reference/P007_中断服务接口.md#ga71fef3867ba9818cf0a5baf8410a6354)。

取得 IRQ 的使能状态（Enable State）。

<a id="r_gade847221335f869809291f0dda33a710"></a>

```c
#define K_IRQ_ACTIVE_NONE UINT_MAX
```

相关声明：[K_IRQ_ACTIVE_NONE](../fatal_irq_reference/P007_中断服务接口.md#gade847221335f869809291f0dda33a710)。

`k_irq_get_active()` 在中断上下文之外返回的值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 173.2\_函数（Functions）

<a id="r_ga4e9915b92b09df49b99bc449f0cc31a1"></a>

```c
static int irq_connect_dynamic (unsigned int irq, unsigned int priority, void(*routine)(const void *parameter), const void *parameter, uint32_t flags)
```

相关声明：[irq_connect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#ga4e9915b92b09df49b99bc449f0cc31a1)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置动态中断（Dynamic Interrupt）。

<a id="r_gabdab7745edc1e15862e1772d8673fc00"></a>

```c
static int irq_disconnect_dynamic (unsigned int irq, unsigned int priority, void(*routine)(const void *parameter), const void *parameter, uint32_t flags)
```

相关声明：[irq_disconnect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#gabdab7745edc1e15862e1772d8673fc00)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

断开动态中断的连接。

<a id="r_gad4a27741fdbb40d4a7d1c7cea10eff03"></a>

```c
static ALWAYS_INLINE unsigned int k_irq_lock (void)
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[k_irq_lock](../fatal_irq_reference/P007_中断服务接口.md#gad4a27741fdbb40d4a7d1c7cea10eff03)。

锁定中断；这是带命名空间前缀的 `irq_lock()` 等价接口。

<a id="r_ga4a5a523c81da5c75d25c58d7702b7144"></a>

```c
static ALWAYS_INLINE void k_irq_unlock (unsigned int key)
```

相关声明：[k_irq_unlock](../fatal_irq_reference/P007_中断服务接口.md#ga4a5a523c81da5c75d25c58d7702b7144)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

解除中断锁定；这是带命名空间前缀的 `irq_unlock()` 等价接口。

<a id="r_ga502c7221c97faad1399465e21880fef1"></a>

```c
static ALWAYS_INLINE void k_irq_enable (unsigned int irq)
```

相关声明：[k_irq_enable](../fatal_irq_reference/P007_中断服务接口.md#ga502c7221c97faad1399465e21880fef1)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使能 IRQ；这是带命名空间前缀的 `irq_enable()` 等价接口。

<a id="r_ga432cfe25e5846d7a0a665043e623d3b6"></a>

```c
static ALWAYS_INLINE void k_irq_disable (unsigned int irq)
```

相关声明：[k_irq_disable](../fatal_irq_reference/P007_中断服务接口.md#ga432cfe25e5846d7a0a665043e623d3b6)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用 IRQ；这是带命名空间前缀的 `irq_disable()` 等价接口。

<a id="r_gabba768c3c87a40641982e4b0654c0d26"></a>

```c
static ALWAYS_INLINE int k_irq_is_enabled (unsigned int irq)
```

相关声明：[k_irq_is_enabled](../fatal_irq_reference/P007_中断服务接口.md#gabba768c3c87a40641982e4b0654c0d26)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

取得 IRQ 使能状态；这是带命名空间前缀的 `irq_is_enabled()` 等价接口。

<a id="r_ga2835209c4f3809b5d22fc84c1bdce935"></a>

```c
static ALWAYS_INLINE int k_irq_connect_dynamic (unsigned int irq, unsigned int priority, void(*routine)(const void *parameter), const void *parameter, uint32_t flags)
```

相关声明：[k_irq_connect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#ga2835209c4f3809b5d22fc84c1bdce935)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置动态中断；这是带命名空间前缀的 `irq_connect_dynamic()` 等价接口。

<a id="r_gae2f1cb1c6babc98ff59d9e87daccb0c5"></a>

```c
static ALWAYS_INLINE int k_irq_disconnect_dynamic (unsigned int irq, unsigned int priority, void(*routine)(const void *parameter), const void *parameter, uint32_t flags)
```

相关声明：[k_irq_disconnect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#gae2f1cb1c6babc98ff59d9e87daccb0c5)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

断开动态中断连接；这是带命名空间前缀的 `irq_disconnect_dynamic()` 等价接口。

<a id="r_gaa322248445f4914ff2093e7cadff0891"></a>

```c
static ALWAYS_INLINE void k_irq_clear_pending (unsigned int irq)
```

相关声明：[k_irq_clear_pending](../fatal_irq_reference/P007_中断服务接口.md#gaa322248445f4914ff2093e7cadff0891)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

清除 IRQ 的挂起状态（Pending State）。

<a id="r_gaa9f2e3357809d1bb734d0841cb3a9653"></a>

```c
static ALWAYS_INLINE void k_irq_set_pending (unsigned int irq)
```

相关声明：[k_irq_set_pending](../fatal_irq_reference/P007_中断服务接口.md#gaa9f2e3357809d1bb734d0841cb3a9653)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

设置 IRQ 的挂起状态。

<a id="r_ga1afce7151e12971b53f7f522493b982c"></a>

```c
static ALWAYS_INLINE bool k_irq_is_pending (unsigned int irq)
```

相关声明：[bool](P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_irq_is_pending](../fatal_irq_reference/P007_中断服务接口.md#ga1afce7151e12971b53f7f522493b982c)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

取得 IRQ 的挂起状态。

<a id="r_gaa62fbe4efebb343ed5ae494c9fcd13cb"></a>

```c
static ALWAYS_INLINE unsigned int k_irq_get_active (void)
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[k_irq_get_active](../fatal_irq_reference/P007_中断服务接口.md#gaa62fbe4efebb343ed5ae494c9fcd13cb)。

取得当前 CPU 正在服务的 IRQ。


## 173.3\_原页交叉引用（Cross References）

- [zephyr/arch/cpu.h](../api_source_supplement_reference/P009_cpu.h_源码浏览.md)
- [limits.h](../api_source_runtime_reference/P039_limits.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/irq_8h_source.html)
- [IRQ_CONNECT](../fatal_irq_reference/P007_中断服务接口.md#ga131739d1faf501a15590053817aba984)
- [IRQ_DIRECT_CONNECT](../fatal_irq_reference/P007_中断服务接口.md#gac6c8746ac28da6ce02b24714f4144ff3)
- [ISR_DIRECT_HEADER](../fatal_irq_reference/P007_中断服务接口.md#ga1ab99dbeb50b228001e1fca808cbaeea)
- [ISR_DIRECT_FOOTER](../fatal_irq_reference/P007_中断服务接口.md#ga31581157c9dbacf935f0e6a8dd456335)
- [ISR_DIRECT_PM](../fatal_irq_reference/P007_中断服务接口.md#ga3c1327551dfca7818975e3fbf1470227)
- [ISR_DIRECT_DECLARE](../fatal_irq_reference/P007_中断服务接口.md#gaf86866cd07fd37f381d98866f8874ebf)
- [irq_lock](../fatal_irq_reference/P007_中断服务接口.md#ga19fdde73c3b02fcca6cf1d1e67631228)
- [irq_unlock](../fatal_irq_reference/P007_中断服务接口.md#ga646045943b3b2a130738bcc48867bf57)
- [irq_enable](../fatal_irq_reference/P007_中断服务接口.md#ga7ea700ee31e4ff036c997a554dbedfeb)
- [irq_disable](../fatal_irq_reference/P007_中断服务接口.md#ga82c3a15d812f58e0f6525f358d031e6d)
- [irq_is_enabled](../fatal_irq_reference/P007_中断服务接口.md#ga71fef3867ba9818cf0a5baf8410a6354)
- [K_IRQ_ACTIVE_NONE](../fatal_irq_reference/P007_中断服务接口.md#gade847221335f869809291f0dda33a710)
- [k_irq_get_active()](../fatal_irq_reference/P007_中断服务接口.md#gaa62fbe4efebb343ed5ae494c9fcd13cb)
- [irq_connect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#ga4e9915b92b09df49b99bc449f0cc31a1)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [irq_disconnect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#gabdab7745edc1e15862e1772d8673fc00)
- [k_irq_lock](../fatal_irq_reference/P007_中断服务接口.md#gad4a27741fdbb40d4a7d1c7cea10eff03)
- [k_irq_unlock](../fatal_irq_reference/P007_中断服务接口.md#ga4a5a523c81da5c75d25c58d7702b7144)
- [k_irq_enable](../fatal_irq_reference/P007_中断服务接口.md#ga502c7221c97faad1399465e21880fef1)
- [k_irq_disable](../fatal_irq_reference/P007_中断服务接口.md#ga432cfe25e5846d7a0a665043e623d3b6)
- [k_irq_is_enabled](../fatal_irq_reference/P007_中断服务接口.md#gabba768c3c87a40641982e4b0654c0d26)
- [k_irq_connect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#ga2835209c4f3809b5d22fc84c1bdce935)
- [k_irq_disconnect_dynamic](../fatal_irq_reference/P007_中断服务接口.md#gae2f1cb1c6babc98ff59d9e87daccb0c5)
- [k_irq_clear_pending](../fatal_irq_reference/P007_中断服务接口.md#gaa322248445f4914ff2093e7cadff0891)
- [k_irq_set_pending](../fatal_irq_reference/P007_中断服务接口.md#gaa9f2e3357809d1bb734d0841cb3a9653)
- [bool](P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_irq_is_pending](../fatal_irq_reference/P007_中断服务接口.md#ga1afce7151e12971b53f7f522493b982c)

<a id="header-details"></a>

---

[上一章](P172_zephyr__drivers__interrupt_controller__ioapic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P174_zephyr__dt-bindings__i2c__it51xxx-i2c.h_文件参考.md)
