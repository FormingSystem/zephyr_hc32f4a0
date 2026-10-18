---
id: learning.zephyr-docs.linker-reference.page-7
title: GNU链接器适配头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-gcc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_GNU链接器适配头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-gcc_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)区分设备树区域生成、工具链适配、只读检测与链接符号。源码跟踪译注与官方原文分开标示。

GCC 工具链的链接器定义（GCC Toolchain Linker Definitions）。

<a id="details"></a>

```c
#include <zephyr/kernel/mm.h>
```

查看此文件的源码。

GCC 工具链的链接器定义（GCC Toolchain Linker Definitions）。

此头文件定义了链接脚本使用 GCC 链接器时所需的宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_a7461001a81999ec4da41a0f1027c4bbd"></a>

```c
#define GROUP_START(where)
```

相关声明：[GROUP_START](#a7461001a81999ec4da41a0f1027c4bbd)。

<a id="r_ab29c47f59ee5a5456a5f81a9050b1a47"></a>

```c
#define GROUP_END(where)
```

相关声明：[GROUP_END](#ab29c47f59ee5a5456a5f81a9050b1a47)。

<a id="r_a9250789b7dcbb7afd371010fb3a6031d"></a>

```c
#define GROUP_LINK_IN(where)
```

相关声明：[GROUP_LINK_IN](#a9250789b7dcbb7afd371010fb3a6031d)。

将内存段放置到指定内存区域。

<a id="r_a0cf8819559a7d33944b47130f478e116"></a>

```c
#define GROUP_ROM_LINK_IN(vregion, lregion)
```

相关声明：[GROUP_ROM_LINK_IN](#a0cf8819559a7d33944b47130f478e116)。

为只读段指定内存放置位置。

<a id="r_a639d450cbafa51e8937d90df449b797f"></a>

```c
#define GROUP_DATA_LINK_IN(vregion, lregion)
```

相关声明：[GROUP_DATA_LINK_IN](#a639d450cbafa51e8937d90df449b797f)。

为需要装载的可读写段指定内存放置位置。

<a id="r_a6784ceba92d50f9785cfd130b4341dae"></a>

```c
#define GROUP_NOLOAD_LINK_IN(vregion, lregion)
```

相关声明：[GROUP_NOLOAD_LINK_IN](#a6784ceba92d50f9785cfd130b4341dae)。

为不装载的可读写段指定内存放置位置；通常只用于 BSS 和 noinit。

<a id="r_a784c696b95848c5f070e257a50fbe23a"></a>

```c
#define SECTION_PROLOGUE(name, options, align)
```

相关声明：[SECTION_PROLOGUE](#a784c696b95848c5f070e257a50fbe23a)。

`SECTION_PROLOGUE()` 宏用于定义一个段的开头。

<a id="r_a0d8981d3817b2563846735c90d50240c"></a>

```c
#define SECTION_DATA_PROLOGUE(name, options, align)
```

相关声明：[SECTION_DATA_PROLOGUE](#a0d8981d3817b2563846735c90d50240c)。

与 `SECTION_PROLOGUE()` 类似，但在原地执行（Execute In Place，XIP）平台上，虚拟地址与装载地址不同的数据段必须使用此宏。

<a id="r_aa5f3d8dcfb378cdbf899467c01494a6f"></a>

```c
#define COMMON_SYMBOLS *(COMMON)
```

相关声明：[COMMON_SYMBOLS](#aa5f3d8dcfb378cdbf899467c01494a6f)。

## 7.2\_详细说明（Detailed Documentation）

<a id="aa5f3d8dcfb378cdbf899467c01494a6f"></a>

### `COMMON_SYMBOLS`

```c
#define COMMON_SYMBOLS *(COMMON)
```

<a id="a639d450cbafa51e8937d90df449b797f"></a>

### `GROUP_DATA_LINK_IN`

```c
#define GROUP_DATA_LINK_IN ( vregion, lregion )
```

展开值（Value）：

```c
> vregion
```

为需要装载的可读写段指定内存放置位置。

用于 XIP 平台上必须在启动时复制的已初始化数据段。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vregion` | 输出虚拟内存地址（Virtual Memory Address，VMA）。 |
| `lregion` | 输出装载内存地址（Load Memory Address，LMA）；仅在启用 CONFIG_MMU 且 VMA 不等于 LMA，或启用 CONFIG_XIP 时使用。 |

<a id="ab29c47f59ee5a5456a5f81a9050b1a47"></a>

### `GROUP_END`

```c
#define GROUP_END ( where)
```

<a id="a9250789b7dcbb7afd371010fb3a6031d"></a>

### `GROUP_LINK_IN`

```c
#define GROUP_LINK_IN ( where)
```

展开值（Value）：

```c
> where
```

将内存段放置到指定内存区域。

`GROUP_LINK_IN()` 宏位于段描述的末尾，用于告知链接器将该段放入 `where` 参数指定的内存区域。

对于启用 CONFIG_MMU 且 CONFIG_KERNEL_VM_BASE 与 DT_CHOSEN_SRAM_ADDR 不同的系统，此宏有意不定义，因为所有段都必须同时明确 LMA 与 VMA 目标，分别对应物理位置和虚拟位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `where` | 目标内存区域（Destination Memory Area）。 |

<a id="a6784ceba92d50f9785cfd130b4341dae"></a>

### `GROUP_NOLOAD_LINK_IN`

```c
#define GROUP_NOLOAD_LINK_IN ( vregion, lregion )
```

展开值（Value）：

```c
> vregion
```

为不装载的可读写段指定内存放置位置；通常只用于 BSS 和 noinit。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vregion` | 输出虚拟内存地址（Virtual Memory Address，VMA）。 |
| `lregion` | 输出 LMA；仅在启用 CONFIG_MMU 且 VMA 不等于 LMA 时使用，此时对应物理位置。 |

<a id="a0cf8819559a7d33944b47130f478e116"></a>

### `GROUP_ROM_LINK_IN`

```c
#define GROUP_ROM_LINK_IN ( vregion, lregion )
```

展开值（Value）：

```c
> lregion
```

为只读段指定内存放置位置。

`GROUP_ROM_LINK_IN()` 宏位于段描述的末尾，用于告知链接器这是一个只读段，其物理位置由 `lregion` 参数指定。

如果启用 CONFIG_XIP，`lregion` 区域就是闪存（Flash Memory）。

如果启用 CONFIG_MMU，`vregion` 参数用于确定此段在虚拟内存映射中的位置；否则忽略该参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vregion` | 输出 VMA；仅在启用 CONFIG_MMU 且 LMA 不等于 VMA 时使用。 |
| `lregion` | 输出 LMA。 |

<a id="a7461001a81999ec4da41a0f1027c4bbd"></a>

### `GROUP_START`

```c
#define GROUP_START ( where)
```

<a id="a0d8981d3817b2563846735c90d50240c"></a>

### `SECTION_DATA_PROLOGUE`

```c
#define SECTION_DATA_PROLOGUE ( name, options, align )
```

展开值（Value）：

```c
SECTION_PROLOGUE(name, options, align)
```

与 `SECTION_PROLOGUE()` 类似，但在原地执行（Execute In Place，XIP）平台上，虚拟地址与装载地址不同的数据段必须使用此宏。

也就是说，程序启动时会将这些段复制到 RAM。这种段还必须使用 `GROUP_DATA_LINK_IN` 指定正确的输出装载地址。

在非 XIP 系统上，此宏等价于 `SECTION_PROLOGUE()`；在 XIP 系统上，它隐含指定 `ALIGN_WITH_INPUT`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 输出段的名称（Output Section Name）。 |
| `options` | 段选项（Section Options），也可留空。 |
| `align` | 对齐指令（Alignment Directives），例如 `SUBALIGN()`；不允许直接使用 `ALIGN()`。可留空。 |

<a id="a784c696b95848c5f070e257a50fbe23a"></a>

### `SECTION_PROLOGUE`

```c
#define SECTION_PROLOGUE ( name, options, align )
```

展开值（Value）：

```c
name options : align
```

`SECTION_PROLOGUE()` 宏用于定义一个段的开头。

在 VMA 不等于 LMA 的 MMU 系统上，隐含指定 `ALIGN_WITH_INPUT`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 输出段的名称（Output Section Name）。 |
| `options` | 段选项，例如 `(NOLOAD)`，也可留空。 |
| `align` | 对齐指令（Alignment Directives），例如 `SUBALIGN()`；不允许直接使用 `ALIGN()`。可留空。 |

## 7.3\_源码定位与版本边界

相对源码定位：[设备树区域](../../../include/zephyr/linker/devicetree_regions.h)、[只读检测](../../../include/zephyr/linker/utils.h)、[适配选择](../../../include/zephyr/linker/linker-tool.h)、[GCC](../../../include/zephyr/linker/linker-tool-gcc.h)、[LLD](../../../include/zephyr/linker/linker-tool-lld.h)、[MWDT](../../../include/zephyr/linker/linker-tool-mwdt.h)、[devnull](../../../include/zephyr/linker/linker-devnull.h)、[链接符号](../../../include/zephyr/linker/linker-defs.h)、[区域绑定](../../../dts/bindings/base/zephyr,memory-region.yaml)、[LLD构建入口](../../../cmake/linker/lld/target.cmake)、[LLD标志](../../../cmake/linker/lld/linker_flags.cmake)、[通用LD标志](../../../cmake/linker/ld/linker_flags.cmake)、[日志段](../../../include/zephyr/linker/common-rom/common-rom-logging.ld)、[内存管理](../../../include/zephyr/kernel/mm.h)和[虚拟内核条件](../../../include/zephyr/kernel/internal/mm.h)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：两类地址：虚拟内存地址（Virtual Memory Address，VMA）表示段的运行地址，装载内存地址（Load Memory Address，LMA）表示装载镜像位置。GROUP_DATA_LINK_IN在XIP或K_MEM_IS_VM_KERNEL分支生成> vregion AT > lregion，普通分支只指定vregion。宏描述布局，不执行启动复制；需要由启动代码消费相应符号。

> 译注——源码核对：虚拟内核条件：实际GNU宏判断K_MEM_IS_VM_KERNEL。kernel/internal/mm.h在K_MEM_VIRT_OFFSET非0时定义它，并拒绝同时启用XIP；不要把只启用CONFIG_MMU与地址存在偏移混为一谈。此分支不定义单参数GROUP_LINK_IN，要求明确VMA与LMA；CONFIG_ARCH_POSIX分支的区域放置宏为空。

> 译注——源码核对：NOLOAD与对齐：GROUP_NOLOAD_LINK_IN在虚拟内核分支指定vregion和lregion，在XIP分支使用> vregion AT > vregion，其他分支只指定vregion。GCC的SECTION_DATA_PROLOGUE在XIP下输出ALIGN_WITH_INPUT且未引用传入align实参；非XIP下转交SECTION_PROLOGUE。应核对实际分支，不能认为每种适配都以相同方式使用三个参数。

> 译注——源码核对：版本边界：本批记录八份链接器头文件、设备树绑定、三份链接器CMake文件、日志链接片段及两份内存管理头文件，共十五份官方源码摘要。八个源码浏览页的非注释代码与本次读取的原始头文件逐项核对；滚动main、latest与本仓库参照版本不自动等同。本次未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 7.4\_原页交叉引用（Cross References）

- [zephyr/kernel/mm.h](https://docs.zephyrproject.org/latest/doxygen/html/mm_8h_source.html)
- [查看此文件的源码](P008_GNU链接器适配头文件源码.md)
- [SUBALIGN()](P011_MWDT链接器适配头文件参考.md#aeec277ba79a2ce60397be71ac2efbe33)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="alinker-tool-gcc_8h_html_a784c696b95848c5f070e257a50fbe23a"></a>

---

[上一章](P006_链接器工具选择头文件源码.md) · [返回大纲](大纲.md) · [下一章](P008_GNU链接器适配头文件源码.md)
