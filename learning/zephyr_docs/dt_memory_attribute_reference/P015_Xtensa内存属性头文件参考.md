---
id: learning.zephyr-docs.dt-memory-attribute-reference.page-15
title: Xtensa内存属性头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/memory-attr-xtensa_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_Xtensa内存属性头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/memory-attr-xtensa_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)区分通用、软件和架构专用内存属性，再选择对应接口。源码跟踪译注与官方原文分开标示。

Xtensa 内存属性设备树绑定定义（Memory Attribute DT Binding Definitions）。

<a id="details"></a>

```c
#include <zephyr/sys/util_macro.h>
#include <zephyr/dt-bindings/memory-attr/memory-attr.h>
```

查看此文件的源码。

Xtensa 内存属性设备树绑定定义（Memory Attribute DT Binding Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.1\_宏定义（Macros）

<a id="r_gaebb8ec5798ba120fd7f2c020a81349f4"></a>

```c
#define DT_MEM_XTENSA_GET(x)
```

相关声明：[DT_MEM_XTENSA_GET](P021_Xtensa内存类型宏.md#gaebb8ec5798ba120fd7f2c020a81349f4)。

从完整的 `zephyr,memory-attr` 值中提取 Xtensa 专用位。

<a id="r_gaa9a1851e86f36be439f024af0d998ee4"></a>

```c
#define DT_MEM_XTENSA_INSTR_ROM DT_MEM_XTENSA(ATTR_XTENSA_INSTR_ROM)
```

相关声明：[DT_MEM_XTENSA_INSTR_ROM](P021_Xtensa内存类型宏.md#gaa9a1851e86f36be439f024af0d998ee4)。

指令只读存储器类型（Instruction ROM Memory Type）。

<a id="r_ga2566e023ccb0cb9529bc9b1d710d27c3"></a>

```c
#define DT_MEM_XTENSA_INSTR_RAM DT_MEM_XTENSA(ATTR_XTENSA_INSTR_RAM)
```

相关声明：[DT_MEM_XTENSA_INSTR_RAM](P021_Xtensa内存类型宏.md#ga2566e023ccb0cb9529bc9b1d710d27c3)。

指令随机存取存储器类型（Instruction RAM Memory Type）。

<a id="r_ga94f99c060768b249c055eb88bf551de8"></a>

```c
#define DT_MEM_XTENSA_DATA_ROM DT_MEM_XTENSA(ATTR_XTENSA_DATA_ROM)
```

相关声明：[DT_MEM_XTENSA_DATA_ROM](P021_Xtensa内存类型宏.md#ga94f99c060768b249c055eb88bf551de8)。

数据只读存储器类型（Data ROM Memory Type）。

<a id="r_ga3b64411ba4c118b0ef9058e3f8c9ebc8"></a>

```c
#define DT_MEM_XTENSA_DATA_RAM DT_MEM_XTENSA(ATTR_XTENSA_DATA_RAM)
```

相关声明：[DT_MEM_XTENSA_DATA_RAM](P021_Xtensa内存类型宏.md#ga3b64411ba4c118b0ef9058e3f8c9ebc8)。

数据随机存取存储器类型（Data RAM Memory Type）。

<a id="r_ga9e63ac329fa36ad194865c40695bad09"></a>

```c
#define DT_MEM_XTENSA_XLMI DT_MEM_XTENSA(ATTR_XTENSA_XLMI)
```

相关声明：[DT_MEM_XTENSA_XLMI](P021_Xtensa内存类型宏.md#ga9e63ac329fa36ad194865c40695bad09)。

Xtensa 本地内存接口类型（Xtensa Local Memory Interface，XLMI）。

<a id="r_ga272c0689cf885783d2c25598d9506eae"></a>

```c
#define DT_MEM_XTENSA_UNKNOWN DT_MEM_ARCH_ATTR_UNKNOWN
```

相关声明：[DT_MEM_XTENSA_UNKNOWN](P021_Xtensa内存类型宏.md#ga272c0689cf885783d2c25598d9506eae)、[DT_MEM_ARCH_ATTR_UNKNOWN](P003_架构专用内存属性宏.md#gaaefc7bf33d8fa6d5151338cd23b84474)。

未知或不受支持的 Xtensa 内存类型。

## 15.2\_源码定位与版本边界

相对源码定位：[通用定义](../../../include/zephyr/dt-bindings/memory-attr/memory-attr.h)、[软件定义](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-sw.h)、[Arm](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h)、[Arm64](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-arm64.h)、[RISC-V](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-riscv.h)、[Xtensa](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-xtensa.h)、[内存属性接口](../../../include/zephyr/mem_mgmt/mem_attr.h)、[内存属性实现](../../../subsys/mem_mgmt/mem_attr.c)、[属性堆接口](../../../include/zephyr/mem_mgmt/mem_attr_heap.h)和[属性堆实现](../../../subsys/mem_mgmt/mem_attr_heap.c)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：三类字段：zephyr,memory-attr使用32位属性值，通用字段为位15:0，软件字段为位19:16，架构字段为位31:20。通用、软件及架构的UNKNOWN分别占位15、19、31；UNKNOWN是一个显式标志，不能把0或未设置某一位一概解释为UNKNOWN。各字段的掩码（Mask）和移位量（Shift）见通用头文件源码。

> 译注——源码核对：提取后仍在原位：本册各GET宏均执行按位与，没有右移。例如DT_MEM_SW_GET(DT_MEM_SW_ALLOC_DMA)仍为BIT(18)，不是原始低位常量ATTR_SW_ALLOC_DMA的BIT(2)。DT_MEM_ARM、DT_MEM_ARM64、DT_MEM_RISCV和DT_MEM_XTENSA等内部编码宏将低位属性移入架构字段；不要把已经编码的DT_MEM_*常量再次移位。

> 译注——源码核对：声明与消费：这些绑定头文件定义属性编码，实际处理取决于启用的子系统和架构代码。subsys/mem_mgmt/mem_attr.c从状态为okay且具有zephyr,memory-attr的节点生成区域表，记录名称、第0个reg的地址与大小及完整属性值。属性声明本身不会分配内存、启用缓存、建立内存管理单元（Memory Management Unit，MMU）映射或赋予硬件原本不具备的DMA能力。

> 译注——源码核对：架构名称空间：Xtensa的指令ROM、指令RAM、数据ROM、数据RAM和XLMI使用架构字段中的对应位；同一位在Arm、Arm64和RISC-V头文件中可能有其他含义。这些架构类型不能混合为一个跨架构属性枚举，消费方必须与目标架构一致。

> 译注——源码核对：版本边界：本批记录六份绑定头文件及内存属性／属性堆的两个公共头文件、两份实现文件，共十份官方源码摘要。六个源码浏览页的非注释代码与本次读取的对应原始头文件一致；滚动main、latest和本仓库参照源码不自动视为同版本。本次未编译示例、配置MPU／MMU、建立内存堆或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 15.3\_原页交叉引用（Cross References）

- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/dt-bindings/memory-attr/memory-attr.h](P006_通用内存属性头文件源码.md)
- [查看此文件的源码](P016_Xtensa内存属性头文件源码.md)
- [DT_MEM_XTENSA_GET](P021_Xtensa内存类型宏.md#gaebb8ec5798ba120fd7f2c020a81349f4)
- [DT_MEM_XTENSA_INSTR_ROM](P021_Xtensa内存类型宏.md#gaa9a1851e86f36be439f024af0d998ee4)
- [DT_MEM_XTENSA_INSTR_RAM](P021_Xtensa内存类型宏.md#ga2566e023ccb0cb9529bc9b1d710d27c3)
- [DT_MEM_XTENSA_DATA_ROM](P021_Xtensa内存类型宏.md#ga94f99c060768b249c055eb88bf551de8)
- [DT_MEM_XTENSA_DATA_RAM](P021_Xtensa内存类型宏.md#ga3b64411ba4c118b0ef9058e3f8c9ebc8)
- [DT_MEM_XTENSA_XLMI](P021_Xtensa内存类型宏.md#ga9e63ac329fa36ad194865c40695bad09)
- [DT_MEM_XTENSA_UNKNOWN](P021_Xtensa内存类型宏.md#ga272c0689cf885783d2c25598d9506eae)
- [DT_MEM_ARCH_ATTR_UNKNOWN](P003_架构专用内存属性宏.md#gaaefc7bf33d8fa6d5151338cd23b84474)

<a id="header-details"></a>

---

[上一章](P014_RISC_V内存属性头文件源码.md) · [返回大纲](大纲.md) · [下一章](P016_Xtensa内存属性头文件源码.md)
