---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-19
title: zephyr__drivers__interrupt_controller__intc_infineon_aurix.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_infineon\_aurix.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon AURIX中断路由器（Interrupt Router，IR）的公共API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
```

查看此文件的源码。

Infineon AURIX 中断路由器（Interrupt Router，IR）的公共 API。AURIX 中断子系统由两个协作模块组成：中断路由器 IR 在 CPU 与 DMA 之间仲裁挂起的服务请求（Service Requests），并驱动各中断源的优先级比较器；服务请求控制寄存器（Service Request Control，SRC）则每个中断源一个，包含各源的使能、优先级、路由和挂起位。本头文件提供精简的底层辅助接口，供 Zephyr TriCore IRQ 适配代码配置、启用、查询和触发单个中断源。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.1\_宏定义（Macros）

<a id="r_a264604390750815174ab7cc81f785830"></a>

```c
#define IR_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, infineon_aurix_ir), 0)
```

相关声明：[IR_BASE](#a264604390750815174ab7cc81f785830)、[DT_REG_ADDR_BY_IDX](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac540b00bb12d0662f6aefe6ac0cff243)、[DT_INST](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)。

AURIX 中断路由器（IR）内存映射 I/O（MMIO）模块的基地址。

<a id="r_a27fb6fedeab6a38c8720873255443abd"></a>

```c
#define SRC_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, infineon_aurix_ir), 1)
```

相关声明：[SRC_BASE](#a27fb6fedeab6a38c8720873255443abd)、[DT_REG_ADDR_BY_IDX](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac540b00bb12d0662f6aefe6ac0cff243)、[DT_INST](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)。

AURIX 服务请求控制（SRC）内存映射 I/O（MMIO）模块的基地址。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.2\_函数（Functions）

<a id="r_a3ba347e14b314f2afdfb87deddf79d1d"></a>

```c
void intc_aurix_ir_irq_config (unsigned int irq, unsigned int priority, unsigned int flags)
```

相关声明：[intc_aurix_ir_irq_config](#a3ba347e14b314f2afdfb87deddf79d1d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置 AURIX 中断源（Interrupt Source）。

<a id="r_a1d7882c67c41d5106e60c9ac2d34da59"></a>

```c
void intc_aurix_ir_irq_enable (unsigned int irq)
```

相关声明：[intc_aurix_ir_irq_enable](#a1d7882c67c41d5106e60c9ac2d34da59)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

启用 AURIX 中断源（Interrupt Source）。

<a id="r_afd28b85ed701604b62abba1f7b6839cf"></a>

```c
void intc_aurix_ir_irq_disable (unsigned int irq)
```

相关声明：[intc_aurix_ir_irq_disable](#afd28b85ed701604b62abba1f7b6839cf)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用 AURIX 中断源（Interrupt Source）。

<a id="r_a50e9bab548376d645b0a6f72e84a29a1"></a>

```c
bool intc_aurix_ir_irq_is_enabled (unsigned int irq)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[intc_aurix_ir_irq_is_enabled](#a50e9bab548376d645b0a6f72e84a29a1)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

查询 AURIX 中断源（Interrupt Source）是否已启用。

<a id="r_ac58092370a3f7087417edc786a804b60"></a>

```c
bool intc_aurix_ir_irq_is_pending (unsigned int irq)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[intc_aurix_ir_irq_is_pending](#ac58092370a3f7087417edc786a804b60)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

查询 AURIX 中断源是否有挂起请求（Pending Request）。

<a id="r_a6e85af7d5a690b0470ba750359ec008c"></a>

```c
void intc_aurix_ir_irq_clear_pending (unsigned int irq)
```

相关声明：[intc_aurix_ir_irq_clear_pending](#a6e85af7d5a690b0470ba750359ec008c)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

清除 AURIX 中断源上的挂起请求（Pending Request）。

<a id="r_a431de8a889dcd8691221a2ec3f7cda89"></a>

```c
void intc_aurix_ir_irq_raise (unsigned int irq)
```

相关声明：[intc_aurix_ir_irq_raise](#a431de8a889dcd8691221a2ec3f7cda89)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

按 IRQ 编号触发 AURIX 中断源（Interrupt Source）。

<a id="r_a6c512b4b26dfda0b434b10332f6b5373"></a>

```c
unsigned int intc_aurix_ir_get_active (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[intc_aurix_ir_get_active](#a6c512b4b26dfda0b434b10332f6b5373)。

返回当前活动的 IRQ 编号。

<a id="r_a0b02c47eb40443d9cceec818a1b7bb93"></a>

```c
void intc_aurix_ir_src_raise (uintptr_t src)
```

相关声明：[intc_aurix_ir_src_raise](#a0b02c47eb40443d9cceec818a1b7bb93)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

按 SRC 寄存器地址触发 AURIX 中断源（Interrupt Source）。

## 19.3\_详细说明（Detailed Documentation）

<a id="a264604390750815174ab7cc81f785830"></a>

### `IR_BASE`

```c
#define IR_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, infineon_aurix_ir), 0)
```

AURIX 中断路由器（IR）内存映射 I/O（MMIO）模块的基地址。

<a id="a27fb6fedeab6a38c8720873255443abd"></a>

### `SRC_BASE`

```c
#define SRC_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, infineon_aurix_ir), 1)
```

AURIX 服务请求控制（SRC）内存映射 I/O（MMIO）模块的基地址。

<a id="a6c512b4b26dfda0b434b10332f6b5373"></a>

### `intc_aurix_ir_get_active()`

```c
unsigned int intc_aurix_ir_get_active ( void )
```

返回当前活动的 IRQ 编号。

读取 CPU 在进入中断时锁存的、当前正在处理的中断标识符（Identifier）。

**返回（Returns）**：返回值（Returns）：当前活动的 Zephyr 编码 IRQ 编号。

<a id="a6e85af7d5a690b0470ba750359ec008c"></a>

### `intc_aurix_ir_irq_clear_pending()`

```c
void intc_aurix_ir_irq_clear_pending ( unsigned int irq)
```

清除 AURIX 中断源上的挂起请求（Pending Request）。

写入对应 SRC 寄存器的 CLRR 位，以清除 SRR 而不影响其他字段。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 编码的 IRQ 编号。 |

<a id="a3ba347e14b314f2afdfb87deddf79d1d"></a>

### `intc_aurix_ir_irq_config()`

```c
void intc_aurix_ir_irq_config ( unsigned int irq, unsigned int priority, unsigned int flags )
```

配置 AURIX 中断源（Interrupt Source）。

将给定优先级和 SoC 支持的标志（如服务类型／路由）写入该中断源的 SRC 寄存器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 编码的 IRQ 编号。 |
| `priority` | 要写入 SRPN 的中断优先级（Interrupt Priority）值。 |
| `flags` | 由实现定义的标志（Implementation-defined Flags），通常为 TOS 字段。 |

<a id="afd28b85ed701604b62abba1f7b6839cf"></a>

### `intc_aurix_ir_irq_disable()`

```c
void intc_aurix_ir_irq_disable ( unsigned int irq)
```

禁用 AURIX 中断源（Interrupt Source）。

清除对应 SRC 寄存器的 SRE 位，保留该中断源中的挂起请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 编码的 IRQ 编号。 |

<a id="a1d7882c67c41d5106e60c9ac2d34da59"></a>

### `intc_aurix_ir_irq_enable()`

```c
void intc_aurix_ir_irq_enable ( unsigned int irq)
```

启用 AURIX 中断源（Interrupt Source）。

设置对应 SRC 寄存器的 SRE 位，使该中断源可以请求服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 编码的 IRQ 编号。 |

<a id="a50e9bab548376d645b0a6f72e84a29a1"></a>

### `intc_aurix_ir_irq_is_enabled()`

```c
bool intc_aurix_ir_irq_is_enabled ( unsigned int irq)
```

查询 AURIX 中断源（Interrupt Source）是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 编码的 IRQ 编号。 |

**返回（Returns）**：返回值（Returns）：该中断源的 SRE 位已设置时返回 true，否则返回 false。

<a id="ac58092370a3f7087417edc786a804b60"></a>

### `intc_aurix_ir_irq_is_pending()`

```c
bool intc_aurix_ir_irq_is_pending ( unsigned int irq)
```

查询 AURIX 中断源是否有挂起请求（Pending Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 编码的 IRQ 编号。 |

**返回（Returns）**：返回值（Returns）：该中断源的 SRR 位已设置时返回 true，否则返回 false。

<a id="a431de8a889dcd8691221a2ec3f7cda89"></a>

### `intc_aurix_ir_irq_raise()`

```c
void intc_aurix_ir_irq_raise ( unsigned int irq)
```

按 IRQ 编号触发 AURIX 中断源（Interrupt Source）。

设置对应 SRC 寄存器的 SETR 位，从软件请求服务。适用于自检（Self-test）和软件触发的处理器间中断（IPIs）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 编码的 IRQ 编号。 |

<a id="a0b02c47eb40443d9cceec818a1b7bb93"></a>

### `intc_aurix_ir_src_raise()`

```c
void intc_aurix_ir_src_raise ( uintptr_t src)
```

按 SRC 寄存器地址触发 AURIX 中断源（Interrupt Source）。

intc_aurix_ir_irq_raise 的变体，通过 SRC 寄存器的绝对地址而非 IRQ 编号指定中断源。适用于已持有 SRC 指针的调用位置，例如驱动内部的软件事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 中断源 SRC 寄存器的绝对地址（Absolute Address）。 |


## 19.4\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P095_intc_infineon_aurix.h_源码浏览.md)
- [DT_REG_ADDR_BY_IDX](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac540b00bb12d0662f6aefe6ac0cff243)
- [DT_INST](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__sd__mmc.h_文件参考.md)
