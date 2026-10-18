---
id: learning.zephyr-docs.dt-memory-attribute-reference.page-19
title: Arm64_MMU内存类型宏
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__binding__mem__attr__arm64.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_Arm64\_MMU内存类型宏

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__binding__mem__attr__arm64.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)区分通用、软件和架构专用内存属性，再选择对应接口。源码跟踪译注与官方原文分开标示。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_memory-attr-arm64_2Eh"></a>

```c
file memory-attr-arm64.h
```

相关声明：[memory-attr-arm64.h](P011_Arm64内存属性头文件参考.md)。

设备树使用的 Arm64 专用内存属性定义（ARM64-specific Memory Attribute Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.2\_宏定义（Macros）

<a id="r_ga967162f16b8b8eff8d8cd02177df4b28"></a>

```c
#define DT_MEM_ARM64_GET(x)
```

相关声明：[DT_MEM_ARM64_GET](#ga967162f16b8b8eff8d8cd02177df4b28)。

从完整的 `zephyr,memory-attr` 值中提取 Arm64 专用位。

<a id="r_gabc7103064d41c7ad5585889318f47457"></a>

```c
#define DT_MEM_ARM64_MMU_NORMAL_NC (0)
```

相关声明：[DT_MEM_ARM64_MMU_NORMAL_NC](#gabc7103064d41c7ad5585889318f47457)。

普通、不可缓存内存（Normal Non-cacheable Memory）。

<a id="r_ga4216fccf33e85298201bbecfba1058d5"></a>

```c
#define DT_MEM_ARM64_MMU_NORMAL_WT (DT_MEM_CACHEABLE)
```

相关声明：[DT_MEM_ARM64_MMU_NORMAL_WT](#ga4216fccf33e85298201bbecfba1058d5)、[DT_MEM_CACHEABLE](P002_通用内存属性宏.md#ga74b1e3dceed92cf63ed018e971c89573)。

采用写直达策略的普通可缓存内存（Normal Write-through Cacheable Memory）。

<a id="r_ga2f7e2582fbfc8bbf777c050cc8c87b72"></a>

```c
#define DT_MEM_ARM64_MMU_NORMAL
```

相关声明：[DT_MEM_ARM64_MMU_NORMAL](#ga2f7e2582fbfc8bbf777c050cc8c87b72)。

采用写回策略的普通可缓存内存（Normal Write-back Cacheable Memory）。

<a id="r_ga80dbfd80717fd17cccbf23a8ff09eb09"></a>

```c
#define DT_MEM_ARM64_MMU_UNKNOWN DT_MEM_ARCH_ATTR_UNKNOWN
```

相关声明：[DT_MEM_ARM64_MMU_UNKNOWN](#ga80dbfd80717fd17cccbf23a8ff09eb09)、[DT_MEM_ARCH_ATTR_UNKNOWN](P003_架构专用内存属性宏.md#gaaefc7bf33d8fa6d5151338cd23b84474)。

表示未知或不受支持内存类型的设备树值。

## 19.3\_详细说明（Detailed Documentation）

<a id="ga967162f16b8b8eff8d8cd02177df4b28"></a>

### `DT_MEM_ARM64_GET`

```c
#define DT_MEM_ARM64_GET ( x)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-arm64.h>
```

展开值（Value）：

```c
((x) & DT_MEM_ARM64_MASK)
```

从完整的 `zephyr,memory-attr` 值中提取 Arm64 专用位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 从中提取 Arm64 专用内存属性位的值。 |

返回（Returns）：Arm64 专用内存属性位。

<a id="ga2f7e2582fbfc8bbf777c050cc8c87b72"></a>

### `DT_MEM_ARM64_MMU_NORMAL`

```c
#define DT_MEM_ARM64_MMU_NORMAL
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-arm64.h>
```

展开值（Value）：

```c
(DT_MEM_CACHEABLE | \
DT_MEM_ARM64(ATTR_ARM64_CACHE_WB))
```

采用写回策略的普通可缓存内存（Normal Write-back Cacheable Memory）。

<a id="gabc7103064d41c7ad5585889318f47457"></a>

### `DT_MEM_ARM64_MMU_NORMAL_NC`

```c
#define DT_MEM_ARM64_MMU_NORMAL_NC (0)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-arm64.h>
```

普通、不可缓存内存（Normal Non-cacheable Memory）。

<a id="ga4216fccf33e85298201bbecfba1058d5"></a>

### `DT_MEM_ARM64_MMU_NORMAL_WT`

```c
#define DT_MEM_ARM64_MMU_NORMAL_WT (DT_MEM_CACHEABLE)
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-arm64.h>
```

采用写直达策略的普通可缓存内存（Normal Write-through Cacheable Memory）。

<a id="ga80dbfd80717fd17cccbf23a8ff09eb09"></a>

### `DT_MEM_ARM64_MMU_UNKNOWN`

```c
#define DT_MEM_ARM64_MMU_UNKNOWN DT_MEM_ARCH_ATTR_UNKNOWN
```

```c
#include <zephyr/dt-bindings/memory-attr/memory-attr-arm64.h>
```

表示未知或不受支持内存类型的设备树值。

## 19.4\_源码定位与版本边界

相对源码定位：[通用定义](../../../include/zephyr/dt-bindings/memory-attr/memory-attr.h)、[软件定义](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-sw.h)、[Arm](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-arm.h)、[Arm64](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-arm64.h)、[RISC-V](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-riscv.h)、[Xtensa](../../../include/zephyr/dt-bindings/memory-attr/memory-attr-xtensa.h)、[内存属性接口](../../../include/zephyr/mem_mgmt/mem_attr.h)、[内存属性实现](../../../subsys/mem_mgmt/mem_attr.c)、[属性堆接口](../../../include/zephyr/mem_mgmt/mem_attr_heap.h)和[属性堆实现](../../../subsys/mem_mgmt/mem_attr_heap.c)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：三类字段：zephyr,memory-attr使用32位属性值，通用字段为位15:0，软件字段为位19:16，架构字段为位31:20。通用、软件及架构的UNKNOWN分别占位15、19、31；UNKNOWN是一个显式标志，不能把0或未设置某一位一概解释为UNKNOWN。各字段的掩码（Mask）和移位量（Shift）见通用头文件源码。

> 译注——源码核对：提取后仍在原位：本册各GET宏均执行按位与，没有右移。例如DT_MEM_SW_GET(DT_MEM_SW_ALLOC_DMA)仍为BIT(18)，不是原始低位常量ATTR_SW_ALLOC_DMA的BIT(2)。DT_MEM_ARM、DT_MEM_ARM64、DT_MEM_RISCV和DT_MEM_XTENSA等内部编码宏将低位属性移入架构字段；不要把已经编码的DT_MEM_*常量再次移位。

> 译注——源码核对：声明与消费：这些绑定头文件定义属性编码，实际处理取决于启用的子系统和架构代码。subsys/mem_mgmt/mem_attr.c从状态为okay且具有zephyr,memory-attr的节点生成区域表，记录名称、第0个reg的地址与大小及完整属性值。属性声明本身不会分配内存、启用缓存、建立内存管理单元（Memory Management Unit，MMU）映射或赋予硬件原本不具备的DMA能力。

> 译注——源码核对：组合编码与零值：DT_MEM_ARM64_MMU_NORMAL_NC为0；NORMAL_WT只含通用DT_MEM_CACHEABLE；NORMAL同时含DT_MEM_CACHEABLE与架构字段中的写回位。它们不是三个独立的一位枚举。DT_MEM_ARM64_GET会去掉通用字段，因此对NORMAL_WT提取架构字段得到0，对NORMAL_NC也得到0；不能只靠这个结果区分二者，应结合完整值的通用字段。

> 译注——源码核对：写回与未知：ATTR_ARM64_CACHE_WB是移位前的位1，编码后位于完整属性的位21，只有同时具备DT_MEM_CACHEABLE时其写回（Write-back）策略才有意义。DT_MEM_ARM64_MMU_UNKNOWN使用架构UNKNOWN位31，与NORMAL_NC的0不同。正常内存类型（Normal Memory）的声明不单独建立MMU映射。

> 译注——源码核对：版本边界：本批记录六份绑定头文件及内存属性／属性堆的两个公共头文件、两份实现文件，共十份官方源码摘要。六个源码浏览页的非注释代码与本次读取的对应原始头文件一致；滚动main、latest和本仓库参照源码不自动视为同版本。本次未编译示例、配置MPU／MMU、建立内存堆或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 19.5\_原页交叉引用（Cross References）

- [memory-attr-arm64.h](P011_Arm64内存属性头文件参考.md)
- [DT_MEM_CACHEABLE](P002_通用内存属性宏.md#ga74b1e3dceed92cf63ed018e971c89573)
- [DT_MEM_ARCH_ATTR_UNKNOWN](P003_架构专用内存属性宏.md#gaaefc7bf33d8fa6d5151338cd23b84474)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__dt__memory__attr__generic_html_ga74b1e3dceed92cf63ed018e971c89573"></a>

---

[上一章](P018_Arm_MPU内存类型宏.md) · [返回大纲](大纲.md) · [下一章](P020_RISC_V内存类型宏.md)
