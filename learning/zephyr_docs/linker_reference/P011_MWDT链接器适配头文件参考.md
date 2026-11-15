---
id: learning.zephyr-docs.linker-reference.page-11
title: MWDT链接器适配头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-mwdt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_MWDT链接器适配头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/linker-tool-mwdt_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)区分设备树区域生成、工具链适配、只读检测与链接符号。源码跟踪译注与官方原文分开标示。

MetaWare（原文拼作 Metware）工具链的链接器定义。

查看此文件的源码。

<a id="details"></a>

MetaWare（原文拼作 Metware）工具链的链接器定义。

此头文件定义了链接脚本使用 MetaWare 链接器时所需的宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_a0a3e46fec8345ab664843141b78b82a3"></a>

```c
#define ASSERT(x, y)
```

相关声明：[ASSERT](#a0a3e46fec8345ab664843141b78b82a3)。

<a id="r_aeec277ba79a2ce60397be71ac2efbe33"></a>

```c
#define SUBALIGN(x)
```

相关声明：[SUBALIGN](#aeec277ba79a2ce60397be71ac2efbe33)。

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

<a id="r_a0cf8819559a7d33944b47130f478e116"></a>

```c
#define GROUP_ROM_LINK_IN(vregion, lregion)
```

相关声明：[GROUP_ROM_LINK_IN](#a0cf8819559a7d33944b47130f478e116)。

`GROUP_ROM_LINK_IN()` 宏位于段描述的末尾，用于告知链接器这是一个只读段，其物理位置由 `region` 参数指定。

> 译注——当前宏的参数名是 `vregion` 与 `lregion`，展开使用的是 `lregion`；原说明中的 region 未区分这两个参数。

<a id="r_a639d450cbafa51e8937d90df449b797f"></a>

```c
#define GROUP_DATA_LINK_IN(vregion, lregion)
```

相关声明：[GROUP_DATA_LINK_IN](#a639d450cbafa51e8937d90df449b797f)。

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

<a id="r_a0d8981d3817b2563846735c90d50240c"></a>

```c
#define SECTION_DATA_PROLOGUE(name, options, align)
```

相关声明：[SECTION_DATA_PROLOGUE](#a0d8981d3817b2563846735c90d50240c)。

<a id="r_afd4796dcd7496f1463f849165f7e2779"></a>

```c
#define SORT_BY_NAME(x)
```

相关声明：[SORT_BY_NAME](#afd4796dcd7496f1463f849165f7e2779)。

## 11.2\_详细说明（Detailed Documentation）

<a id="a0a3e46fec8345ab664843141b78b82a3"></a>

### `ASSERT`

```c
#define ASSERT ( x, y )
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

<a id="a0cf8819559a7d33944b47130f478e116"></a>

### `GROUP_ROM_LINK_IN`

```c
#define GROUP_ROM_LINK_IN ( vregion, lregion )
```

展开值（Value）：

```c
> lregion
```

`GROUP_ROM_LINK_IN()` 宏位于段描述的末尾，用于告知链接器这是一个只读段，其物理位置由 `region` 参数指定。

> 译注——当前宏的参数名是 `vregion` 与 `lregion`，展开使用的是 `lregion`；原说明中的 region 未区分这两个参数。

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
name options : align
```

<a id="a784c696b95848c5f070e257a50fbe23a"></a>

### `SECTION_PROLOGUE`

```c
#define SECTION_PROLOGUE ( name, options, align )
```

展开值（Value）：

```c
name options : align
```

<a id="afd4796dcd7496f1463f849165f7e2779"></a>

### `SORT_BY_NAME`

```c
#define SORT_BY_NAME ( x)
```

展开值（Value）：

```c
SORT(x)
```

<a id="aeec277ba79a2ce60397be71ac2efbe33"></a>

### `SUBALIGN`

```c
#define SUBALIGN ( x)
```

展开值（Value）：

```c
ALIGN(x)
```

## 11.3\_源码定位与版本边界

相对源码定位：[设备树区域](../../../include/zephyr/linker/devicetree_regions.h)、[只读检测](../../../include/zephyr/linker/utils.h)、[适配选择](../../../include/zephyr/linker/linker-tool.h)、[GCC](../../../include/zephyr/linker/linker-tool-gcc.h)、[LLD](../../../include/zephyr/linker/linker-tool-lld.h)、[MWDT](../../../include/zephyr/linker/linker-tool-mwdt.h)、[devnull](../../../include/zephyr/linker/linker-devnull.h)、[链接符号](../../../include/zephyr/linker/linker-defs.h)、[区域绑定](../../../dts/bindings/base/zephyr,memory-region.yaml)、[LLD构建入口](../../../cmake/linker/lld/target.cmake)、[LLD标志](../../../cmake/linker/lld/linker_flags.cmake)、[通用LD标志](../../../cmake/linker/ld/linker_flags.cmake)、[日志段](../../../include/zephyr/linker/common-rom/common-rom-logging.ld)、[内存管理](../../../include/zephyr/kernel/mm.h)和[虚拟内核条件](../../../include/zephyr/kernel/internal/mm.h)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：适配差异：MWDT将ASSERT展开为空、将SUBALIGN(x)映射为ALIGN(x)，GROUP_START／END也为空；不能把源码出现ASSERT当作该工具链实际执行了断言。GROUP_ROM_LINK_IN使用lregion而忽略vregion；原描述写作region，译注明确实际参数。原页面Metware拼写保留说明，工具链通常称MetaWare。

> 译注——源码核对：原注释旧名称：SECTION_DATA_PROLOGUE的源码注释要求配合GROUP_LINK_IN_LMA，但本头文件实际定义的是GROUP_DATA_LINK_IN。XIP下数据段开头附带ALIGN(8)，并由GROUP_DATA_LINK_IN生成运行区域和装载区域关系。原注释关于GNU ld放置指令会延续影响后续段的描述照译，不把它当成每种链接器的统一语义保证。

> 译注——源码核对：版本边界：本批记录八份链接器头文件、设备树绑定、三份链接器CMake文件、日志链接片段及两份内存管理头文件，共十五份官方源码摘要。八个源码浏览页的非注释代码与本次读取的原始头文件逐项核对；滚动main、latest与本仓库参照版本不自动等同。本次未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 11.4\_原页交叉引用（Cross References）

- [查看此文件的源码](P012_MWDT链接器适配头文件源码.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P010_LLD链接器适配头文件源码.md) · [返回大纲](大纲.md) · [下一章](P012_MWDT链接器适配头文件源码.md)
