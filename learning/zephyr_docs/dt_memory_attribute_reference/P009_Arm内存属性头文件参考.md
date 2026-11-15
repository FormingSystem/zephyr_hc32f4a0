---
id: learning.zephyr-docs.dt-memory-attribute-reference.page-9
title: Arm内存属性头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/memory-attr-arm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_Arm内存属性头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/memory-attr-arm_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)区分通用、软件和架构专用内存属性，再选择对应接口。源码跟踪译注与官方原文分开标示。

Arm 内存保护单元（Memory Protection Unit，MPU）的内存属性设备树绑定定义，属于旧式定义（Legacy）。

<a id="details"></a>

```c
#include <zephyr/sys/util_macro.h>
#include <zephyr/dt-bindings/memory-attr/memory-attr.h>
```

查看此文件的源码。

Arm 内存保护单元（Memory Protection Unit，MPU）的内存属性设备树绑定定义，属于旧式定义（Legacy）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="r_gac9237bf43ea0801606a72bb1aa408952"></a>

```c
#define DT_MEM_ARM_GET(x)
```

相关声明：[DT_MEM_ARM_GET](P018_Arm_MPU内存类型宏.md#gac9237bf43ea0801606a72bb1aa408952)。

从完整的 `zephyr,memory-attr` 值中提取 Arm MPU 专用位。

<a id="r_gab3669734951faa3f55f85db9fe005daa"></a>

```c
#define DT_MEM_ARM_MPU_RAM DT_MEM_ARM(ATTR_MPU_RAM)
```

相关声明：[DT_MEM_ARM_MPU_RAM](P018_Arm_MPU内存类型宏.md#gab3669734951faa3f55f85db9fe005daa)。

标准可缓存 RAM 区域（Standard Cacheable RAM Region）。

<a id="r_gaf60fb9c11ef84238647855f52a338904"></a>

```c
#define DT_MEM_ARM_MPU_RAM_NOCACHE DT_MEM_ARM(ATTR_MPU_RAM_NOCACHE)
```

相关声明：[DT_MEM_ARM_MPU_RAM_NOCACHE](P018_Arm_MPU内存类型宏.md#gaf60fb9c11ef84238647855f52a338904)。

不可缓存 RAM 区域（Non-cacheable RAM Region）。

<a id="r_ga2bc421f5582d90604dc95b796a475221"></a>

```c
#define DT_MEM_ARM_MPU_FLASH DT_MEM_ARM(ATTR_MPU_FLASH)
```

相关声明：[DT_MEM_ARM_MPU_FLASH](P018_Arm_MPU内存类型宏.md#ga2bc421f5582d90604dc95b796a475221)。

闪存／只读存储器区域（Flash／ROM Memory Region）。

<a id="r_ga7b0f983bdde1aab0cf703006aa79c363"></a>

```c
#define DT_MEM_ARM_MPU_PPB DT_MEM_ARM(ATTR_MPU_PPB)
```

相关声明：[DT_MEM_ARM_MPU_PPB](P018_Arm_MPU内存类型宏.md#ga7b0f983bdde1aab0cf703006aa79c363)。

私有外设总线区域（Private Peripheral Bus Region，PPB）。

<a id="r_ga21a8d85ff9c329bb4ebd9f9f4a9b2e9c"></a>

```c
#define DT_MEM_ARM_MPU_IO DT_MEM_ARM(ATTR_MPU_IO)
```

相关声明：[DT_MEM_ARM_MPU_IO](P018_Arm_MPU内存类型宏.md#ga21a8d85ff9c329bb4ebd9f9f4a9b2e9c)。

输入输出／外设内存区域（I/O／Peripheral Memory Region）。

<a id="r_gadd7dd0c9f14a8696d1827d3d5bfbb263"></a>

```c
#define DT_MEM_ARM_MPU_EXTMEM DT_MEM_ARM(ATTR_MPU_EXTMEM)
```

相关声明：[DT_MEM_ARM_MPU_EXTMEM](P018_Arm_MPU内存类型宏.md#gadd7dd0c9f14a8696d1827d3d5bfbb263)。

外部内存区域（External Memory Region）。

<a id="r_gaee3d2c7c52a670df6d18fb7f336cbe9c"></a>

```c
#define DT_MEM_ARM_MPU_RAM_PXN DT_MEM_ARM(ATTR_MPU_RAM_PXN)
```

相关声明：[DT_MEM_ARM_MPU_RAM_PXN](P018_Arm_MPU内存类型宏.md#gaee3d2c7c52a670df6d18fb7f336cbe9c)。

具有特权级禁止执行属性（Privileged Execute Never，PXN）的 RAM 区域。

<a id="r_gae7b7d40900362bf93216c050d60f82f7"></a>

```c
#define DT_MEM_ARM_MPU_DEVICE DT_MEM_ARM(ATTR_MPU_DEVICE)
```

相关声明：[DT_MEM_ARM_MPU_DEVICE](P018_Arm_MPU内存类型宏.md#gae7b7d40900362bf93216c050d60f82f7)。

设备内存区域（Device Memory Region）。

<a id="r_gaba3890ac15f70b2e240410baa1dc317c"></a>

```c
#define DT_MEM_ARM_MPU_RAM_WT DT_MEM_ARM(ATTR_MPU_RAM_WT)
```

相关声明：[DT_MEM_ARM_MPU_RAM_WT](P018_Arm_MPU内存类型宏.md#gaba3890ac15f70b2e240410baa1dc317c)。

采用写直达策略的可缓存 RAM 区域（Write-through Cacheable RAM Region）。

<a id="r_gab24037ec20705fdf979d453046cd979a"></a>

```c
#define DT_MEM_ARM_MPU_UNKNOWN DT_MEM_ARCH_ATTR_UNKNOWN
```

相关声明：[DT_MEM_ARM_MPU_UNKNOWN](P018_Arm_MPU内存类型宏.md#gab24037ec20705fdf979d453046cd979a)、[DT_MEM_ARCH_ATTR_UNKNOWN](P003_架构专用内存属性宏.md#gaaefc7bf33d8fa6d5151338cd23b84474)。

未知或不受支持的 Arm MPU 内存类型。

## 9.2\_源码定位与版本边界

相对源码定位：[通用定义](../../../include/zephyr/dt-bindings/memory-attr/memory-attr.h)、[软件定义](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-sw.h)、[Arm](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h)、[Arm64](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-arm64.h)、[RISC-V](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-riscv.h)、[Xtensa](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-xtensa.h)、[内存属性接口](../../../include/zephyr/mem_mgmt/mem_attr.h)、[内存属性实现](../../../subsys/mem_mgmt/mem_attr.c)、[属性堆接口](../../../include/zephyr/mem_mgmt/mem_attr_heap.h)和[属性堆实现](../../../subsys/mem_mgmt/mem_attr_heap.c)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：三类字段：zephyr,memory-attr使用32位属性值，通用字段为位15:0，软件字段为位19:16，架构字段为位31:20。通用、软件及架构的UNKNOWN分别占位15、19、31；UNKNOWN是一个显式标志，不能把0或未设置某一位一概解释为UNKNOWN。各字段的掩码（Mask）和移位量（Shift）见通用头文件源码。

> 译注——源码核对：提取后仍在原位：本册各GET宏均执行按位与，没有右移。例如DT_MEM_SW_GET(DT_MEM_SW_ALLOC_DMA)仍为BIT(18)，不是原始低位常量ATTR_SW_ALLOC_DMA的BIT(2)。DT_MEM_ARM、DT_MEM_ARM64、DT_MEM_RISCV和DT_MEM_XTENSA等内部编码宏将低位属性移入架构字段；不要把已经编码的DT_MEM_*常量再次移位。

> 译注——源码核对：声明与消费：这些绑定头文件定义属性编码，实际处理取决于启用的子系统和架构代码。subsys/mem_mgmt/mem_attr.c从状态为okay且具有zephyr,memory-attr的节点生成区域表，记录名称、第0个reg的地址与大小及完整属性值。属性声明本身不会分配内存、启用缓存、建立内存管理单元（Memory Management Unit，MMU）映射或赋予硬件原本不具备的DMA能力。

> 译注——源码核对：旧式MPU编码：Arm头文件中的RAM、RAM_NOCACHE、FLASH、PPB、IO、EXTMEM、RAM_PXN、DEVICE和RAM_WT编码移入架构字段。本页仅描述Zephyr设备树编码，不是直接可写入MPU寄存器的硬件位。官方注释明确禁止继续扩展这套旧式类型，新的MPU区域类型应使用通用内存属性；保留现有定义不等于建议新代码继续增加此类常量。

> 译注——源码核对：版本边界：本批记录六份绑定头文件及内存属性／属性堆的两个公共头文件、两份实现文件，共十份官方源码摘要。六个源码浏览页的非注释代码与本次读取的对应原始头文件一致；滚动main、latest和本仓库参照源码不自动视为同版本。本次未编译示例、配置MPU／MMU、建立内存堆或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 9.3\_原页交叉引用（Cross References）

- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/dt-bindings/memory-attr/memory-attr.h](P006_通用内存属性头文件源码.md)
- [查看此文件的源码](P010_Arm内存属性头文件源码.md)
- [DT_MEM_ARM_GET](P018_Arm_MPU内存类型宏.md#gac9237bf43ea0801606a72bb1aa408952)
- [DT_MEM_ARM_MPU_RAM](P018_Arm_MPU内存类型宏.md#gab3669734951faa3f55f85db9fe005daa)
- [DT_MEM_ARM_MPU_RAM_NOCACHE](P018_Arm_MPU内存类型宏.md#gaf60fb9c11ef84238647855f52a338904)
- [DT_MEM_ARM_MPU_FLASH](P018_Arm_MPU内存类型宏.md#ga2bc421f5582d90604dc95b796a475221)
- [DT_MEM_ARM_MPU_PPB](P018_Arm_MPU内存类型宏.md#ga7b0f983bdde1aab0cf703006aa79c363)
- [DT_MEM_ARM_MPU_IO](P018_Arm_MPU内存类型宏.md#ga21a8d85ff9c329bb4ebd9f9f4a9b2e9c)
- [DT_MEM_ARM_MPU_EXTMEM](P018_Arm_MPU内存类型宏.md#gadd7dd0c9f14a8696d1827d3d5bfbb263)
- [DT_MEM_ARM_MPU_RAM_PXN](P018_Arm_MPU内存类型宏.md#gaee3d2c7c52a670df6d18fb7f336cbe9c)
- [DT_MEM_ARM_MPU_DEVICE](P018_Arm_MPU内存类型宏.md#gae7b7d40900362bf93216c050d60f82f7)
- [DT_MEM_ARM_MPU_RAM_WT](P018_Arm_MPU内存类型宏.md#gaba3890ac15f70b2e240410baa1dc317c)
- [DT_MEM_ARM_MPU_UNKNOWN](P018_Arm_MPU内存类型宏.md#gab24037ec20705fdf979d453046cd979a)
- [DT_MEM_ARCH_ATTR_UNKNOWN](P003_架构专用内存属性宏.md#gaaefc7bf33d8fa6d5151338cd23b84474)

<a id="header-details"></a>

---

[上一章](P008_软件内存属性头文件源码.md) · [返回大纲](大纲.md) · [下一章](P010_Arm内存属性头文件源码.md)
