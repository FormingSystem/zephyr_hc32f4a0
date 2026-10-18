---
id: learning.zephyr-docs.api-file-display-chat-reference.page-15
title: zephyr__irq_multilevel.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_irq\_multilevel.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/irq__multilevel_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多级中断（Multi-Level Interrupts）的公共接口。

<a id="details"></a>

```c
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/util.h>
#include <zephyr/types.h>
```

查看此文件的源码。

多级中断（Multi-Level Interrupts）的公共接口。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.1\_宏定义（Macros）

<a id="r_a9a94c2cecb8c8d3394c1ff5ed3cc4db3"></a>

```c
#define IRQ_TO_L2(irq)
```

相关声明：[IRQ_TO_L2](#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)。

将 irq 从第 1 级格式转换为第 2 级格式的预处理器宏（Preprocessor Macro）。

<a id="r_a1aa1eaa367e7c8baa250900de4eb0daf"></a>

```c
#define IRQ_TO_L3(irq)
```

相关声明：[IRQ_TO_L3](#a1aa1eaa367e7c8baa250900de4eb0daf)。

将 irq 从第 1 级格式转换为第 3 级格式的预处理器宏（Preprocessor Macro）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.2\_函数（Functions）

<a id="r_a45afd68784e71521606e489d965b1c13"></a>

```c
static unsigned int irq_get_level (unsigned int irq)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_get_level](#a45afd68784e71521606e489d965b1c13)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

返回 IRQ 层级（IRQ Level）。此例程返回所提供中断的层级编号。

<a id="r_a4022e57572b3bffb694bf25eef090cec"></a>

```c
static unsigned int irq_from_level_2 (unsigned int irq)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_from_level_2](#a4022e57572b3bffb694bf25eef090cec)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

返回第 2 级中断编号（Interrupt Number）。

<a id="r_a79eb4433215c271fa61b9352855f93ca"></a>

```c
static unsigned int irq_to_level_2 (unsigned int irq)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_to_level_2](#a79eb4433215c271fa61b9352855f93ca)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

将 irq 从第 1 级格式转换为第 2 级格式。

<a id="r_ab1a4c5a542e4ad472dba609829c34bc4"></a>

```c
static unsigned int irq_parent_level_2 (unsigned int irq)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_parent_level_2](#ab1a4c5a542e4ad472dba609829c34bc4)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

返回第 2 级原始 IRQ 编号的父 IRQ（Parent IRQ）。

<a id="r_a401e5249731398fdec30f8e51437f2fb"></a>

```c
static unsigned int irq_from_level_3 (unsigned int irq)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_from_level_3](#a401e5249731398fdec30f8e51437f2fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

返回第 3 级中断编号（Interrupt Number）。

<a id="r_a3b8df71a84ac972b89eb37684dcc7072"></a>

```c
static unsigned int irq_to_level_3 (unsigned int irq)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_to_level_3](#a3b8df71a84ac972b89eb37684dcc7072)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

将 irq 从第 1 级格式转换为第 3 级格式。

<a id="r_ae11c8cb9a832a5a8f514a52a12f133c4"></a>

```c
static unsigned int irq_parent_level_3 (unsigned int irq)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_parent_level_3](#ae11c8cb9a832a5a8f514a52a12f133c4)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

返回第 3 级原始 IRQ 编号的父 IRQ（Parent IRQ）。

<a id="r_a07a9a77e0d09a05f81d73da2d3f3388a"></a>

```c
static unsigned int irq_from_level (unsigned int irq, unsigned int level)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_from_level](#a07a9a77e0d09a05f81d73da2d3f3388a)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

返回给定层级的中断编号（Interrupt Number）。

<a id="r_ae91094e0be680803d7bd79739029e390"></a>

```c
static unsigned int irq_to_level (unsigned int irq, unsigned int level)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_to_level](#ae91094e0be680803d7bd79739029e390)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

将 irq 从第 1 级格式转换为给定层级的格式。

<a id="r_a8f22ab28ed1da7312fcd716eea59e400"></a>

```c
static unsigned int irq_parent_level (unsigned int irq, unsigned int level)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_parent_level](#a8f22ab28ed1da7312fcd716eea59e400)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

返回给定层级原始 IRQ 编号的父 IRQ（Parent IRQ）。

<a id="r_a9fb52147e972ee981050b47758dca73d"></a>

```c
static unsigned int irq_get_intc_irq (unsigned int irq)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_get_intc_irq](#a9fb52147e972ee981050b47758dca73d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

返回给定 IRQ 编号的父中断控制器 IRQ（Parent Interrupt Controller IRQ）。

<a id="r_a4b5e1b801ea817b0432a5c5e74f6bff7"></a>

```c
static unsigned int irq_increment (unsigned int irq, unsigned int val)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[irq_increment](#a4b5e1b801ea817b0432a5c5e74f6bff7)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

将多级编码（Multilevel-encoded）的 irq 增加 val。

## 15.3\_详细说明（Detailed Documentation）

<a id="a9a94c2cecb8c8d3394c1ff5ed3cc4db3"></a>

### `IRQ_TO_L2`

```c
#define IRQ_TO_L2 ( irq)
```

展开值（Value）：

```c
FIELD_PREP(Z_IRQ_L2_MASK, (irq) + 1U)
```

将 irq 从第 1 级格式转换为第 2 级格式的预处理器宏（Preprocessor Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

返回（Returns）：第 2 级 IRQ 编号。

<a id="a1aa1eaa367e7c8baa250900de4eb0daf"></a>

### `IRQ_TO_L3`

```c
#define IRQ_TO_L3 ( irq)
```

展开值（Value）：

```c
FIELD_PREP(Z_IRQ_L3_MASK, (irq) + 1U)
```

将 irq 从第 1 级格式转换为第 3 级格式的预处理器宏（Preprocessor Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

返回（Returns）：第 3 级 IRQ 编号。

<a id="a07a9a77e0d09a05f81d73da2d3f3388a"></a>

### `irq_from_level()`

```c
unsigned int irq_from_level ( unsigned int irq, unsigned int level )
```

声明属性：`inline`、`static`。

返回给定层级的中断编号（Interrupt Number）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |
| `level` | IRQ 层级（IRQ Level）。 |

返回（Returns）：该层级中的 IRQ 编号。

<a id="a4022e57572b3bffb694bf25eef090cec"></a>

### `irq_from_level_2()`

```c
unsigned int irq_from_level_2 ( unsigned int irq)
```

声明属性：`inline`、`static`。

返回第 2 级中断编号（Interrupt Number）。

此例程返回传入的 Zephyr IRQ 编号对应的第 2 级 IRQ 编号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

返回（Returns）：第 2 级 IRQ 编号。

<a id="a401e5249731398fdec30f8e51437f2fb"></a>

### `irq_from_level_3()`

```c
unsigned int irq_from_level_3 ( unsigned int irq)
```

声明属性：`inline`、`static`。

返回第 3 级中断编号（Interrupt Number）。

此例程返回传入的 Zephyr IRQ 编号对应的第 3 级 IRQ 编号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

返回（Returns）：第 3 级 IRQ 编号。

<a id="a9fb52147e972ee981050b47758dca73d"></a>

### `irq_get_intc_irq()`

```c
unsigned int irq_get_intc_irq ( unsigned int irq)
```

声明属性：`inline`、`static`。

返回给定 IRQ 编号的父中断控制器 IRQ（Parent Interrupt Controller IRQ）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

返回（Returns）：中断控制器（Interrupt Controller）的 IRQ。

<a id="a45afd68784e71521606e489d965b1c13"></a>

### `irq_get_level()`

```c
unsigned int irq_get_level ( unsigned int irq)
```

声明属性：`inline`、`static`。

返回 IRQ 层级（IRQ Level）。此例程返回所提供中断的层级编号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

返回（Returns）：IRQ 为第 1 级时返回 1，第 2 级时返回 2，第 3 级时返回 3。

<a id="a4b5e1b801ea817b0432a5c5e74f6bff7"></a>

### `irq_increment()`

```c
unsigned int irq_increment ( unsigned int irq, unsigned int val )
```

声明属性：`inline`、`static`。

将多级编码（Multilevel-encoded）的 irq 增加 val。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |
| `val` | 增量（Amount to Increment）。 |

返回（Returns）：增加 val 后的 irq。

<a id="a8f22ab28ed1da7312fcd716eea59e400"></a>

### `irq_parent_level()`

```c
unsigned int irq_parent_level ( unsigned int irq, unsigned int level )
```

声明属性：`inline`、`static`。

返回给定层级原始 IRQ 编号的父 IRQ（Parent IRQ）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |
| `level` | IRQ 层级（IRQ Level）。 |

返回（Returns）：给定层级的父 IRQ（IRQ Parent）。

<a id="ab1a4c5a542e4ad472dba609829c34bc4"></a>

### `irq_parent_level_2()`

```c
unsigned int irq_parent_level_2 ( unsigned int irq)
```

声明属性：`inline`、`static`。

返回第 2 级原始 IRQ 编号的父 IRQ（Parent IRQ）。

第 2 级中断的父中断（Parent）位于第 1 个字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

返回（Returns）：第 2 级 IRQ 的父 IRQ。

<a id="ae11c8cb9a832a5a8f514a52a12f133c4"></a>

### `irq_parent_level_3()`

```c
unsigned int irq_parent_level_3 ( unsigned int irq)
```

声明属性：`inline`、`static`。

返回第 3 级原始 IRQ 编号的父 IRQ（Parent IRQ）。

第 3 级中断的父中断（Parent）位于第 2 个字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

返回（Returns）：第 3 级 IRQ 的父 IRQ。

<a id="ae91094e0be680803d7bd79739029e390"></a>

### `irq_to_level()`

```c
unsigned int irq_to_level ( unsigned int irq, unsigned int level )
```

声明属性：`inline`、`static`。

将 irq 从第 1 级格式转换为给定层级的格式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |
| `level` | IRQ 层级（IRQ Level）。 |

返回（Returns）：转换为该层级格式的 IRQ 编号。

<a id="a79eb4433215c271fa61b9352855f93ca"></a>

### `irq_to_level_2()`

```c
unsigned int irq_to_level_2 ( unsigned int irq)
```

声明属性：`inline`、`static`。

将 irq 从第 1 级格式转换为第 2 级格式。

此例程将输入值转换为第 2 级 IRQ 编号格式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

**说明（Note）**：注意（Note）：大于或等于 0xFF 的值无效。

返回（Returns）：第 2 级 IRQ 编号。

<a id="a3b8df71a84ac972b89eb37684dcc7072"></a>

### `irq_to_level_3()`

```c
unsigned int irq_to_level_3 ( unsigned int irq)
```

声明属性：`inline`、`static`。

将 irq 从第 1 级格式转换为第 3 级格式。

此例程将输入值转换为第 3 级 IRQ 编号格式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用 Zephyr 格式的 IRQ 编号（IRQ Number）。 |

**说明（Note）**：注意（Note）：大于或等于 0xFF 的值无效。

返回（Returns）：第 3 级 IRQ 编号。


## 15.4\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P021_irq_multilevel.h_源码浏览.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_zephyr__input__input_crsf.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__canbus__isotp.h_文件参考.md)
