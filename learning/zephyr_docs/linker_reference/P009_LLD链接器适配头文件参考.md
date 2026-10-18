---
id: learning.zephyr-docs.linker-reference.page-9
title: LLD链接器适配头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-lld_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_LLD链接器适配头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-lld_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)区分设备树区域生成、工具链适配、只读检测与链接符号。源码跟踪译注与官方原文分开标示。

LLVM LLD 链接器定义（LLVM LLD Linker Definitions）。

<a id="details"></a>

```c
#include <zephyr/linker/linker-tool-gcc.h>
```

查看此文件的源码。

LLVM LLD 链接器定义（LLVM LLD Linker Definitions）。

此头文件定义了链接脚本使用 LLD 链接器时所需的宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

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

## 9.2\_详细说明（Detailed Documentation）

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

使用 LLD 链接时，此宏等价于 `SECTION_PROLOGUE()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 输出段的名称（Output Section Name）。 |
| `options` | 段选项（Section Options），也可留空。 |
| `align` | 对齐指令，例如 `SUBALIGN()`；可留空。 |

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

向 LLD 提供 `--omagic`（`-N`）选项后，指定区域中只有第一个输出段的 LMA 会对齐，随后加上 VMA 地址之间的差值（若为第一个段，该差值为 0）。默认情况下，不使用 `--omagic` 时，LLD 会将每个段的 LMA 与 VMA 对齐到相同值。这样，每个段的 LMA 与 VMA 之差保持恒定，从而模拟 GNU LD 的 `ALIGN_WITH_INPUT` 选项，满足 XIP 系统的需要。

原文指出，`--omagic` 标志定义在 `cmake/linker/lld/target_baremetal.cmake` 中。

> 译注——本次官方源码中已找不到此路径；当前 LLD 标志文件继承通用 LD 标志文件，后者的 baremetal 属性中配置 `-N`，详见源码跟踪译注。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 输出段的名称（Output Section Name）。 |
| `options` | 段选项，例如 `(NOLOAD)`，也可留空。 |
| `align` | 对齐指令，例如 `SUBALIGN()`；可留空。 |

## 9.3\_源码定位与版本边界

相对源码定位：[设备树区域](../../../include/zephyr/linker/devicetree_regions.h)、[只读检测](../../../include/zephyr/linker/utils.h)、[适配选择](../../../include/zephyr/linker/linker-tool.h)、[GCC](../../../include/zephyr/linker/linker-tool-gcc.h)、[LLD](../../../include/zephyr/linker/linker-tool-lld.h)、[MWDT](../../../include/zephyr/linker/linker-tool-mwdt.h)、[devnull](../../../include/zephyr/linker/linker-devnull.h)、[链接符号](../../../include/zephyr/linker/linker-defs.h)、[区域绑定](../../../dts/bindings/base/zephyr,memory-region.yaml)、[LLD构建入口](../../../cmake/linker/lld/target.cmake)、[LLD标志](../../../cmake/linker/lld/linker_flags.cmake)、[通用LD标志](../../../cmake/linker/ld/linker_flags.cmake)、[日志段](../../../include/zephyr/linker/common-rom/common-rom-logging.ld)、[内存管理](../../../include/zephyr/kernel/mm.h)和[虚拟内核条件](../../../include/zephyr/kernel/internal/mm.h)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：继承与覆写：LLD头文件先包含GCC宏集，再#undef并重定义SECTION_PROLOGUE与SECTION_DATA_PROLOGUE；数据段开头最终同样展开为name options : align。其他区域放置宏来自GCC适配，因此阅读LLD页时也需参考GCC条件分支。

> 译注——源码核对：旧路径说明：原注释中的cmake/linker/lld/target_baremetal.cmake在本次官方读取时返回404。当前cmake/linker/lld/linker_flags.cmake包含cmake/linker/ld/linker_flags.cmake，后者在baremetal属性中配置-N。原文保留，当前文件相对链接与摘要列在来源记录；这不是要求读者创建那个旧文件。

> 译注——源码核对：两类地址：虚拟内存地址（Virtual Memory Address，VMA）表示段的运行地址，装载内存地址（Load Memory Address，LMA）表示装载镜像位置。GROUP_DATA_LINK_IN在XIP或K_MEM_IS_VM_KERNEL分支生成> vregion AT > lregion，普通分支只指定vregion。宏描述布局，不执行启动复制；需要由启动代码消费相应符号。

> 译注——源码核对：版本边界：本批记录八份链接器头文件、设备树绑定、三份链接器CMake文件、日志链接片段及两份内存管理头文件，共十五份官方源码摘要。八个源码浏览页的非注释代码与本次读取的原始头文件逐项核对；滚动main、latest与本仓库参照版本不自动等同。本次未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 9.4\_原页交叉引用（Cross References）

- [zephyr/linker/linker-tool-gcc.h](P008_GNU链接器适配头文件源码.md)
- [查看此文件的源码](P010_LLD链接器适配头文件源码.md)
- [SECTION_PROLOGUE](P007_GNU链接器适配头文件参考.md#a784c696b95848c5f070e257a50fbe23a)
- [SUBALIGN()](P011_MWDT链接器适配头文件参考.md#aeec277ba79a2ce60397be71ac2efbe33)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="alinker-tool-gcc_8h_html_a784c696b95848c5f070e257a50fbe23a"></a>

---

[上一章](P008_GNU链接器适配头文件源码.md) · [返回大纲](大纲.md) · [下一章](P010_LLD链接器适配头文件源码.md)
