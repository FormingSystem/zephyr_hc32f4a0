---
id: learning.zephyr-docs.dt-memory-attribute-reference.page-20
title: RISC_V内存类型宏
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__binding__mem__attr__riscv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_RISC\_V内存类型宏

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__binding__mem__attr__riscv.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)区分通用、软件和架构专用内存属性，再选择对应接口。源码跟踪译注与官方原文分开标示。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 20.1\_文件（Files）

<a id="r_memory-attr-riscv_2Eh"></a>

```c
file memory-attr-riscv.h
```

相关声明：[memory-attr-riscv.h](P013_RISC_V内存属性头文件参考.md)。

RISC-V 内存属性设备树绑定定义（Memory Attribute DT Binding Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.2\_宏定义（Macros）

<a id="r_gafea331be5ba6698753abd1a1a1d958eb"></a>

```c
#define DT_MEM_RISCV_GET(x)
```

相关声明：[DT_MEM_RISCV_GET](#gafea331be5ba6698753abd1a1a1d958eb)。

从完整的 `zephyr,memory-attr` 值中提取 RISC-V 专用位。

<a id="r_ga4c67437419601ee8c81b9c34f39122c4"></a>

```c
#define DT_MEM_RISCV_TYPE_MAIN DT_MEM_RISCV(ATTR_RISCV_TYPE_MAIN)
```

相关声明：[DT_MEM_RISCV_TYPE_MAIN](#ga4c67437419601ee8c81b9c34f39122c4)。

主存／动态随机存取存储器类型（Main／DRAM Memory Type）。

<a id="r_ga30903aee0dabbf6f15c8526834b11f11"></a>

```c
#define DT_MEM_RISCV_TYPE_IO DT_MEM_RISCV(ATTR_RISCV_TYPE_IO)
```

相关声明：[DT_MEM_RISCV_TYPE_IO](#ga30903aee0dabbf6f15c8526834b11f11)。

输入输出内存类型（I/O Memory Type）。

<a id="r_ga874f08e7b73df8f1aa49adfbfbc8fae3"></a>

```c
#define DT_MEM_RISCV_TYPE_IO_R DT_MEM_RISCV(ATTR_RISCV_TYPE_IO_R)
```

相关声明：[DT_MEM_RISCV_TYPE_IO_R](#ga874f08e7b73df8f1aa49adfbfbc8fae3)。

具有读取属性（Read Attribute）的 I/O 内存。

<a id="r_ga5ba95a48993ccd4ba834d02a4464318f"></a>

```c
#define DT_MEM_RISCV_TYPE_IO_W DT_MEM_RISCV(ATTR_RISCV_TYPE_IO_W)
```

相关声明：[DT_MEM_RISCV_TYPE_IO_W](#ga5ba95a48993ccd4ba834d02a4464318f)。

具有写入属性（Write Attribute）的 I/O 内存。

<a id="r_ga0e515e7457b354aa38f0ccaac00fabde"></a>

```c
#define DT_MEM_RISCV_TYPE_IO_X DT_MEM_RISCV(ATTR_RISCV_TYPE_IO_X)
```

相关声明：[DT_MEM_RISCV_TYPE_IO_X](#ga0e515e7457b354aa38f0ccaac00fabde)。

具有执行属性（Execute Attribute）的 I/O 内存。

<a id="r_ga938f9f8b108f8e1230726bf3cbadbe99"></a>

```c
#define DT_MEM_RISCV_TYPE_EMPTY DT_MEM_RISCV(ATTR_RISCV_TYPE_EMPTY)
```

相关声明：[DT_MEM_RISCV_TYPE_EMPTY](#ga938f9f8b108f8e1230726bf3cbadbe99)。

空的或保留的内存类型（Empty or Reserved Memory Type）。

<a id="r_gafe6b3c00217e837092384b2baf36d613"></a>

```c
#define DT_MEM_RISCV_AMO_SWAP DT_MEM_RISCV(ATTR_RISCV_AMO_SWAP)
```

相关声明：[DT_MEM_RISCV_AMO_SWAP](#gafe6b3c00217e837092384b2baf36d613)。

支持原子内存操作中的交换操作（AMO Swap Operations）。

<a id="r_ga1b28fc152f2c96c3236e2e4c37c8fbb2"></a>

```c
#define DT_MEM_RISCV_AMO_LOGICAL DT_MEM_RISCV(ATTR_RISCV_AMO_LOGICAL)
```

相关声明：[DT_MEM_RISCV_AMO_LOGICAL](#ga1b28fc152f2c96c3236e2e4c37c8fbb2)。

支持原子内存操作中的逻辑操作（AMO Logical Operations）。

<a id="r_gadafec66eb70663372088154a2703012e"></a>

```c
#define DT_MEM_RISCV_AMO_ARITHMETIC DT_MEM_RISCV(ATTR_RISCV_AMO_ARITHMETIC)
```

相关声明：[DT_MEM_RISCV_AMO_ARITHMETIC](#gadafec66eb70663372088154a2703012e)。

支持原子内存操作中的算术操作（AMO Arithmetic Operations）。

<a id="r_ga2be0609b3bc135633711554e840e512a"></a>

```c
#define DT_MEM_RISCV_IO_IDEMPOTENT_READ DT_MEM_RISCV(ATTR_RISCV_IO_IDEMPOTENT_READ)
```

相关声明：[DT_MEM_RISCV_IO_IDEMPOTENT_READ](#ga2be0609b3bc135633711554e840e512a)。

具有幂等读取属性（Idempotent Read Attribute）的 I/O 内存。

<a id="r_ga1b04dd65a2a5bf184b0965a352cba49f"></a>

```c
#define DT_MEM_RISCV_IO_IDEMPOTENT_WRITE DT_MEM_RISCV(ATTR_RISCV_IO_IDEMPOTENT_WRITE)
```

相关声明：[DT_MEM_RISCV_IO_IDEMPOTENT_WRITE](#ga1b04dd65a2a5bf184b0965a352cba49f)。

具有幂等写入属性（Idempotent Write Attribute）的 I/O 内存。

<a id="r_gae008d2f860df3c52c9a02e97757f4168"></a>

```c
#define DT_MEM_RISCV_UNKNOWN DT_MEM_ARCH_ATTR_UNKNOWN
```

相关声明：[DT_MEM_RISCV_UNKNOWN](#gae008d2f860df3c52c9a02e97757f4168)、[DT_MEM_ARCH_ATTR_UNKNOWN](P003_架构专用内存属性宏.md#gaaefc7bf33d8fa6d5151338cd23b84474)。

未知或不受支持的 RISC-V 内存类型。

## 20.3\_详细说明（Detailed Documentation）

<a id="gadafec66eb70663372088154a2703012e"></a>

### `DT_MEM_RISCV_AMO_ARITHMETIC`

```c
#define DT_MEM_RISCV_AMO_ARITHMETIC DT_MEM_RISCV(ATTR_RISCV_AMO_ARITHMETIC)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

支持原子内存操作中的算术操作（AMO Arithmetic Operations）。

<a id="ga1b28fc152f2c96c3236e2e4c37c8fbb2"></a>

### `DT_MEM_RISCV_AMO_LOGICAL`

```c
#define DT_MEM_RISCV_AMO_LOGICAL DT_MEM_RISCV(ATTR_RISCV_AMO_LOGICAL)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

支持原子内存操作中的逻辑操作（AMO Logical Operations）。

<a id="gafe6b3c00217e837092384b2baf36d613"></a>

### `DT_MEM_RISCV_AMO_SWAP`

```c
#define DT_MEM_RISCV_AMO_SWAP DT_MEM_RISCV(ATTR_RISCV_AMO_SWAP)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

支持原子内存操作中的交换操作（AMO Swap Operations）。

<a id="gafea331be5ba6698753abd1a1a1d958eb"></a>

### `DT_MEM_RISCV_GET`

```c
#define DT_MEM_RISCV_GET ( x)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

展开值（Value）：

```c
((x) & DT_MEM_RISCV_MASK)
```

从完整的 `zephyr,memory-attr` 值中提取 RISC-V 专用位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 从中提取 RISC-V 专用内存属性位的值。 |

返回（Returns）：RISC-V 专用内存属性位。

<a id="ga2be0609b3bc135633711554e840e512a"></a>

### `DT_MEM_RISCV_IO_IDEMPOTENT_READ`

```c
#define DT_MEM_RISCV_IO_IDEMPOTENT_READ DT_MEM_RISCV(ATTR_RISCV_IO_IDEMPOTENT_READ)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

具有幂等读取属性（Idempotent Read Attribute）的 I/O 内存。

<a id="ga1b04dd65a2a5bf184b0965a352cba49f"></a>

### `DT_MEM_RISCV_IO_IDEMPOTENT_WRITE`

```c
#define DT_MEM_RISCV_IO_IDEMPOTENT_WRITE DT_MEM_RISCV(ATTR_RISCV_IO_IDEMPOTENT_WRITE)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

具有幂等写入属性（Idempotent Write Attribute）的 I/O 内存。

<a id="ga938f9f8b108f8e1230726bf3cbadbe99"></a>

### `DT_MEM_RISCV_TYPE_EMPTY`

```c
#define DT_MEM_RISCV_TYPE_EMPTY DT_MEM_RISCV(ATTR_RISCV_TYPE_EMPTY)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

空的或保留的内存类型（Empty or Reserved Memory Type）。

<a id="ga30903aee0dabbf6f15c8526834b11f11"></a>

### `DT_MEM_RISCV_TYPE_IO`

```c
#define DT_MEM_RISCV_TYPE_IO DT_MEM_RISCV(ATTR_RISCV_TYPE_IO)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

输入输出内存类型（I/O Memory Type）。

<a id="ga874f08e7b73df8f1aa49adfbfbc8fae3"></a>

### `DT_MEM_RISCV_TYPE_IO_R`

```c
#define DT_MEM_RISCV_TYPE_IO_R DT_MEM_RISCV(ATTR_RISCV_TYPE_IO_R)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

具有读取属性（Read Attribute）的 I/O 内存。

<a id="ga5ba95a48993ccd4ba834d02a4464318f"></a>

### `DT_MEM_RISCV_TYPE_IO_W`

```c
#define DT_MEM_RISCV_TYPE_IO_W DT_MEM_RISCV(ATTR_RISCV_TYPE_IO_W)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

具有写入属性（Write Attribute）的 I/O 内存。

<a id="ga0e515e7457b354aa38f0ccaac00fabde"></a>

### `DT_MEM_RISCV_TYPE_IO_X`

```c
#define DT_MEM_RISCV_TYPE_IO_X DT_MEM_RISCV(ATTR_RISCV_TYPE_IO_X)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

具有执行属性（Execute Attribute）的 I/O 内存。

<a id="ga4c67437419601ee8c81b9c34f39122c4"></a>

### `DT_MEM_RISCV_TYPE_MAIN`

```c
#define DT_MEM_RISCV_TYPE_MAIN DT_MEM_RISCV(ATTR_RISCV_TYPE_MAIN)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

主存／动态随机存取存储器类型（Main／DRAM Memory Type）。

<a id="gae008d2f860df3c52c9a02e97757f4168"></a>

### `DT_MEM_RISCV_UNKNOWN`

```c
#define DT_MEM_RISCV_UNKNOWN DT_MEM_ARCH_ATTR_UNKNOWN
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-riscv.h>
```

未知或不受支持的 RISC-V 内存类型。

## 20.4\_源码定位与版本边界

相对源码定位：[通用定义](../../../include/zephyr/dt-bindings/memory-attr/memory-attr.h)、[软件定义](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-sw.h)、[Arm](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h)、[Arm64](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-arm64.h)、[RISC-V](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-riscv.h)、[Xtensa](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-xtensa.h)、[内存属性接口](../../../include/zephyr/mem_mgmt/mem_attr.h)、[内存属性实现](../../../subsys/mem_mgmt/mem_attr.c)、[属性堆接口](../../../include/zephyr/mem_mgmt/mem_attr_heap.h)和[属性堆实现](../../../subsys/mem_mgmt/mem_attr_heap.c)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：三类字段：zephyr,memory-attr使用32位属性值，通用字段为位15:0，软件字段为位19:16，架构字段为位31:20。通用、软件及架构的UNKNOWN分别占位15、19、31；UNKNOWN是一个显式标志，不能把0或未设置某一位一概解释为UNKNOWN。各字段的掩码（Mask）和移位量（Shift）见通用头文件源码。

> 译注——源码核对：提取后仍在原位：本册各GET宏均执行按位与，没有右移。例如DT_MEM_SW_GET(DT_MEM_SW_ALLOC_DMA)仍为BIT(18)，不是原始低位常量ATTR_SW_ALLOC_DMA的BIT(2)。DT_MEM_ARM、DT_MEM_ARM64、DT_MEM_RISCV和DT_MEM_XTENSA等内部编码宏将低位属性移入架构字段；不要把已经编码的DT_MEM_*常量再次移位。

> 译注——源码核对：声明与消费：这些绑定头文件定义属性编码，实际处理取决于启用的子系统和架构代码。subsys/mem_mgmt/mem_attr.c从状态为okay且具有zephyr,memory-attr的节点生成区域表，记录名称、第0个reg的地址与大小及完整属性值。属性声明本身不会分配内存、启用缓存、建立内存管理单元（Memory Management Unit，MMU）映射或赋予硬件原本不具备的DMA能力。

> 译注——源码核对：类型与操作能力：RISC-V字段分别描述主存、I/O、空／保留类型，I/O读写执行、原子内存操作（Atomic Memory Operation，AMO）及幂等访问能力。每个常量只是移入架构字段的编码，不会执行原子操作或授予访问权限。幂等读取／写入是对重复访问特性的声明，不能用这些标志将具有副作用的外设寄存器变成幂等寄存器。

> 译注——源码核对：版本边界：本批记录六份绑定头文件及内存属性／属性堆的两个公共头文件、两份实现文件，共十份官方源码摘要。六个源码浏览页的非注释代码与本次读取的对应原始头文件一致；滚动main、latest和本仓库参照源码不自动视为同版本。本次未编译示例、配置MPU／MMU、建立内存堆或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 20.5\_原页交叉引用（Cross References）

- [memory-attr-riscv.h](P013_RISC_V内存属性头文件参考.md)
- [DT_MEM_ARCH_ATTR_UNKNOWN](P003_架构专用内存属性宏.md#gaaefc7bf33d8fa6d5151338cd23b84474)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P019_Arm64_MMU内存类型宏.md) · [返回大纲](大纲.md) · [下一章](P021_Xtensa内存类型宏.md)
