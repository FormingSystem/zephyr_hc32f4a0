---
id: learning.zephyr-docs.api-file-reference.page-480
title: zephyr__drivers__interrupt_controller__sysapic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sysapic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第480章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_sysapic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sysapic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/interrupt_controller/loapic.h>
#include <zephyr/types.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 480.1\_宏定义（Macros）

<a id="r_afffc88f34c930a5af21baadb445f9c71"></a>

```c
#define IRQ_TRIGGER_EDGE IOAPIC_EDGE
```

相关声明：[IRQ_TRIGGER_EDGE](#afffc88f34c930a5af21baadb445f9c71)、[IOAPIC_EDGE](P172_zephyr__drivers__interrupt_controller__ioapic.h_文件参考.md#a1d4cfd6f7d4aba0bc773e4d53333bb1d)。

<a id="r_afa859e1b2648a338573252756f6df69b"></a>

```c
#define IRQ_TRIGGER_LEVEL IOAPIC_LEVEL
```

相关声明：[IRQ_TRIGGER_LEVEL](#afa859e1b2648a338573252756f6df69b)、[IOAPIC_LEVEL](P172_zephyr__drivers__interrupt_controller__ioapic.h_文件参考.md#afee8dca23363d2f9b785a21f6b5c4080)。

<a id="r_a1f706a68a6c632a0a3ad761eaa0092ee"></a>

```c
#define IRQ_POLARITY_HIGH IOAPIC_HIGH
```

相关声明：[IRQ_POLARITY_HIGH](#a1f706a68a6c632a0a3ad761eaa0092ee)、[IOAPIC_HIGH](P172_zephyr__drivers__interrupt_controller__ioapic.h_文件参考.md#a1677a4eb3aab3bea022e9ea2bf547888)。

<a id="r_a90a856442e76f43799d24ca853d8a04b"></a>

```c
#define IRQ_POLARITY_LOW IOAPIC_LOW
```

相关声明：[IRQ_POLARITY_LOW](#a90a856442e76f43799d24ca853d8a04b)、[IOAPIC_LOW](P172_zephyr__drivers__interrupt_controller__ioapic.h_文件参考.md#a23ec31db6b36b64ad0d04c3caf2815f2)。

<a id="r_ad0fac43b50900ad4e2b2d1e1876fc36d"></a>

```c
#define LOAPIC_IRQ_COUNT 6 /* Default to LOAPIC_TIMER to LOAPIC_ERROR */
```

相关声明：[LOAPIC_IRQ_COUNT](#ad0fac43b50900ad4e2b2d1e1876fc36d)、[LOAPIC_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#ad2c049f84d86360481bf39f1c769d33a)、[LOAPIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#ab7911822a48695ea33abe3321623fe98)。

## 480.2\_详细说明（Detailed Documentation）

<a id="a1f706a68a6c632a0a3ad761eaa0092ee"></a>

### `IRQ_POLARITY_HIGH`

```c
#define IRQ_POLARITY_HIGH IOAPIC_HIGH
```

<a id="a90a856442e76f43799d24ca853d8a04b"></a>

### `IRQ_POLARITY_LOW`

```c
#define IRQ_POLARITY_LOW IOAPIC_LOW
```

<a id="afffc88f34c930a5af21baadb445f9c71"></a>

### `IRQ_TRIGGER_EDGE`

```c
#define IRQ_TRIGGER_EDGE IOAPIC_EDGE
```

<a id="afa859e1b2648a338573252756f6df69b"></a>

### `IRQ_TRIGGER_LEVEL`

```c
#define IRQ_TRIGGER_LEVEL IOAPIC_LEVEL
```

<a id="ad0fac43b50900ad4e2b2d1e1876fc36d"></a>

### `LOAPIC_IRQ_COUNT`

```c
#define LOAPIC_IRQ_COUNT 6 /* Default to LOAPIC_TIMER to LOAPIC_ERROR */
```


## 480.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/loapic.h](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P220_sysapic.h_源码浏览.md)
- [IOAPIC_EDGE](P172_zephyr__drivers__interrupt_controller__ioapic.h_文件参考.md#a1d4cfd6f7d4aba0bc773e4d53333bb1d)
- [IOAPIC_LEVEL](P172_zephyr__drivers__interrupt_controller__ioapic.h_文件参考.md#afee8dca23363d2f9b785a21f6b5c4080)
- [IOAPIC_HIGH](P172_zephyr__drivers__interrupt_controller__ioapic.h_文件参考.md#a1677a4eb3aab3bea022e9ea2bf547888)
- [IOAPIC_LOW](P172_zephyr__drivers__interrupt_controller__ioapic.h_文件参考.md#a23ec31db6b36b64ad0d04c3caf2815f2)
- [LOAPIC_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#ad2c049f84d86360481bf39f1c769d33a)
- [LOAPIC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#ab7911822a48695ea33abe3321623fe98)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P479_zephyr__posix__sys__dirent.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P481_zephyr__posix__sys__sysconf.h_文件参考.md)
