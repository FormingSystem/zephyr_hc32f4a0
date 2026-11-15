---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-22
title: zephyr__sw_isr_table.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sw__isr__table_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_sw\_isr\_table.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sw__isr__table_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

由软件管理的中断服务程序（ISR）表。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/types.h>
#include <zephyr/toolchain.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

软件管理的中断服务例程表（Software-managed ISR Table）。用于软件管理 ISR 表的数据类型，每个 ISR 均具有一个参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.1\_宏定义（Macros）

<a id="r_a9b130c84dbe718bcb89f7a83eb3a1d04"></a>

```c
#define INTC_BASE_ISR_TBL_OFFSET(node_id)
```

相关声明：[INTC_BASE_ISR_TBL_OFFSET](#a9b130c84dbe718bcb89f7a83eb3a1d04)。

获取中断控制器节点的层级基准 ISR 表偏移量（Level Base ISR Table Offset）。

<a id="r_a810f9314f0a6d8a902593d0521660176"></a>

```c
#define INTC_INST_ISR_TBL_OFFSET(inst)
```

相关声明：[INTC_INST_ISR_TBL_OFFSET](#a810f9314f0a6d8a902593d0521660176)。

获取某个中断控制器实例的软件 ISR 表偏移量（SW ISR Table Offset）。

<a id="r_a433c2b13315bd1fa93057a48b3b30122"></a>

```c
#define INTC_CHILD_ISR_TBL_OFFSET(node_id)
```

相关声明：[INTC_CHILD_ISR_TBL_OFFSET](#a433c2b13315bd1fa93057a48b3b30122)。

获取子中断控制器（Child Interrupt Controller）的软件 ISR 表偏移量。

<a id="r_aaa922e8bad35d8f5a25d889cd14fd915"></a>

```c
#define IRQ_PARENT_ENTRY_DEFINE(_name, _dev, _irq, _offset, _level)
```

相关声明：[IRQ_PARENT_ENTRY_DEFINE](#aaa922e8bad35d8f5a25d889cd14fd915)。

向软件 ISR 表注册中断控制器（Interrupt Controller）。

<a id="r_a1376eec61303fcd20e7656175ddbaf19"></a>

```c
#define ISR_FLAG_DIRECT BIT(0)
```

相关声明：[ISR_FLAG_DIRECT](#a1376eec61303fcd20e7656175ddbaf19)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

此中断直接放入向量表（Vector Table）。

<a id="r_af36594d0586be77420bfe6eaf9f96a2c"></a>

```c
#define IRQ_TABLE_SIZE (CONFIG_NUM_IRQS - CONFIG_GEN_IRQ_START_VECTOR)
```

相关声明：[IRQ_TABLE_SIZE](#af36594d0586be77420bfe6eaf9f96a2c)。

## 22.2\_详细说明（Detailed Documentation）

<a id="a9b130c84dbe718bcb89f7a83eb3a1d04"></a>

### `INTC_BASE_ISR_TBL_OFFSET`

```c
#define INTC_BASE_ISR_TBL_OFFSET ( node_id)
```

展开值（Value）：

```c
Z_SW_ISR_TBL_KCONFIG_BY_ALVL(DT_INTC_GET_AGGREGATOR_LEVEL(node_id))
```

获取中断控制器节点的层级基准 ISR 表偏移量（Level Base ISR Table Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 中断控制器的节点标识符（Node Identifier）。 |

**返回（Returns）**：返回值：若 `node_id` 是二级汇聚控制器（Second Level Aggregator），返回 `CONFIG_2ND_LVL_ISR_TBL_OFFSET`；若是三级汇聚控制器，返回 `CONFIG_3RD_LVL_ISR_TBL_OFFSET`。

<a id="a433c2b13315bd1fa93057a48b3b30122"></a>

### `INTC_CHILD_ISR_TBL_OFFSET`

```c
#define INTC_CHILD_ISR_TBL_OFFSET ( node_id)
```

展开值（Value）：

```c
(INTC_BASE_ISR_TBL_OFFSET(node_id) +                                                       \
 (DT_NODE_CHILD_IDX(node_id) * CONFIG_MAX_IRQ_PER_AGGREGATOR))
```

获取子中断控制器（Child Interrupt Controller）的软件 ISR 表偏移量。

此宏是 `INTC_INST_ISR_TBL_OFFSET` 的另一种形式，供作为主中断控制器设备子节点的伪中断控制器设备（Pseudo Interrupt Controller Devices）使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 子中断控制器的节点标识符（Node Identifier）。 |

**返回（Returns）**：返回值：子中断控制器的软件 ISR 表偏移量（Software ISR Table Offset）。

<a id="a810f9314f0a6d8a902593d0521660176"></a>

### `INTC_INST_ISR_TBL_OFFSET`

```c
#define INTC_INST_ISR_TBL_OFFSET ( inst)
```

展开值（Value）：

```c
(INTC_BASE_ISR_TBL_OFFSET(DT_DRV_INST(inst)) + (inst * CONFIG_MAX_IRQ_PER_AGGREGATOR))
```

获取某个中断控制器实例的软件 ISR 表偏移量（SW ISR Table Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | `DT_DRV_COMPAT` 中断控制器驱动实例编号（Instance Number）。 |

**返回（Returns）**：返回值：中断控制器的软件 ISR 表偏移量（Software ISR Table Offset）。

<a id="aaa922e8bad35d8f5a25d889cd14fd915"></a>

### `IRQ_PARENT_ENTRY_DEFINE`

```c
#define IRQ_PARENT_ENTRY_DEFINE ( _name, _dev, _irq, _offset, _level )
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE_ALTERNATE(intc_table, _irq_parent_entry, _name) = {   \
        .dev = _dev,                                                                       \
        .level = _level,                                                                   \
        .irq = _irq,                                                                       \
        .offset = _offset,                                                                 \
}
```

向软件 ISR 表注册中断控制器（Interrupt Controller）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 中断控制器名称（Name），必须唯一。 |
| `_dev` | 指向中断控制器设备实例（Device Instance）的指针。 |
| `_irq` | 中断控制器的中断请求（IRQ）编号。 |
| `_offset` | 中断控制器的软件 ISR 表偏移量（Software ISR Table Offset）。 |
| `_level` | 中断控制器的汇聚层级（Aggregator Level）。 |

<a id="af36594d0586be77420bfe6eaf9f96a2c"></a>

### `IRQ_TABLE_SIZE`

```c
#define IRQ_TABLE_SIZE (CONFIG_NUM_IRQS - CONFIG_GEN_IRQ_START_VECTOR)
```

<a id="a1376eec61303fcd20e7656175ddbaf19"></a>

### `ISR_FLAG_DIRECT`

```c
#define ISR_FLAG_DIRECT BIT(0)
```

此中断直接放入向量表（Vector Table）。


## 22.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_interrupt_modem_reference/P011_sw_isr_table.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [DT_INTC_GET_AGGREGATOR_LEVEL](../dt_irq_reference/P002_设备树中断控制器宏.md#ga4eebef2c5e75d6a6c87d0cea03ac1bee)
- [DT_NODE_CHILD_IDX](../dt_identity_reference/P001_设备树节点标识宏.md#ga34452788d4fed1fce3e6650d61246866)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [STRUCT_SECTION_ITERABLE_ALTERNATE](../iterable_reference/P001_可遍历段公共接口.md#gae08ef16db3e04967fdca69a19ca4c70b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-interrupt__controller_html_ga4eebef2c5e75d6a6c87d0cea03ac1bee"></a>
<a id="agroup__devicetree-generic-id_html_ga34452788d4fed1fce3e6650d61246866"></a>
<a id="asw__isr__table_8h_html_a9b130c84dbe718bcb89f7a83eb3a1d04"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__iterable__section__apis_html_gae08ef16db3e04967fdca69a19ca4c70b"></a>

---

[上一章](P021_zephyr__arch__pmu.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__xen__sched.h_文件参考.md)
