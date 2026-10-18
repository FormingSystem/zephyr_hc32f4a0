---
id: learning.zephyr-docs.memory-retention-reference.page-2
title: NVMEM设备树头文件参考
kind: reference
status: maintained
domains: [zephyr, storage, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2nvmem_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_NVMEM设备树头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2nvmem_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：按[本册大纲](大纲.md)区分NVMEM数据单元、保留内存驱动与数据保留服务，再结合已有公共接口阅读本册源码。源码跟踪译注与官方原文分开标示。

非易失性存储器（Non-Volatile Memory，NVMEM）的公共设备树（Devicetree）头文件。

查看此文件的源码。

<a id="details"></a>

非易失性存储器（Non-Volatile Memory，NVMEM）的公共设备树（Devicetree）头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga477ec6b0fcb8dfeed591ae17ee26ce4a"></a>

```c
#define DT_NVMEM_CELLS_HAS_IDX(node_id, idx)
```

相关声明：[DT_NVMEM_CELLS_HAS_IDX](../storage/P018_NVMEM设备树辅助宏.md#ga477ec6b0fcb8dfeed591ae17ee26ce4a)。

检查节点的nvmem-cells节点引用数组（Phandle Array）属性是否存在指定索引。

<a id="r_ga75c4f7ef73d6802dec48be9a9a042811"></a>

```c
#define DT_NVMEM_CELLS_HAS_NAME(node_id, name)
```

相关声明：[DT_NVMEM_CELLS_HAS_NAME](../storage/P018_NVMEM设备树辅助宏.md#ga75c4f7ef73d6802dec48be9a9a042811)。

检查节点的nvmem-cell-names数组属性是否包含指定名称。

<a id="r_gac87acacf5e5d6f0ed57d910b09e2578a"></a>

```c
#define DT_NUM_NVMEM_CELLS(node_id)
```

相关声明：[DT_NUM_NVMEM_CELLS](../storage/P018_NVMEM设备树辅助宏.md#gac87acacf5e5d6f0ed57d910b09e2578a)。

获取nvmem-cells属性中的元素数量。

<a id="r_gadc09f069ab5823011bccfd2b87604330"></a>

```c
#define DT_NVMEM_CELL_BY_IDX(node_id, idx)
```

相关声明：[DT_NVMEM_CELL_BY_IDX](../storage/P018_NVMEM设备树辅助宏.md#gadc09f069ab5823011bccfd2b87604330)。

按索引从nvmem-cells属性获取NVMEM数据单元（Cell）的节点标识符（Node Identifier）。

<a id="r_gad53d706e576954c8e8dd2739cc99d306"></a>

```c
#define DT_NVMEM_CELL(node_id)
```

相关声明：[DT_NVMEM_CELL](../storage/P018_NVMEM设备树辅助宏.md#gad53d706e576954c8e8dd2739cc99d306)。

获取索引0处NVMEM数据单元的节点标识符。

<a id="r_ga42848d5418cfed0c5c003ba7484584b7"></a>

```c
#define DT_NVMEM_CELL_BY_NAME(node_id, name)
```

相关声明：[DT_NVMEM_CELL_BY_NAME](../storage/P018_NVMEM设备树辅助宏.md#ga42848d5418cfed0c5c003ba7484584b7)。

按名称从nvmem-cells属性获取NVMEM数据单元的节点标识符。

<a id="r_ga30989613f7ad97d47a8f620a17f08db9"></a>

```c
#define DT_INST_NVMEM_CELLS_HAS_IDX(inst, idx)
```

相关声明：[DT_INST_NVMEM_CELLS_HAS_IDX](../storage/P018_NVMEM设备树辅助宏.md#ga30989613f7ad97d47a8f620a17f08db9)。

检查DT_DRV_COMPAT实例的nvmem-cells属性是否存在指定索引。

<a id="r_gaf984c322b72e49e75401d655126ab728"></a>

```c
#define DT_INST_NVMEM_CELLS_HAS_NAME(inst, name)
```

相关声明：[DT_INST_NVMEM_CELLS_HAS_NAME](../storage/P018_NVMEM设备树辅助宏.md#gaf984c322b72e49e75401d655126ab728)。

检查DT_DRV_COMPAT实例的nvmem-cell-names属性是否包含指定名称。

<a id="r_gac38526df0e386dfe22539e26b0a8eccf"></a>

```c
#define DT_INST_NUM_NVMEM_CELLS(inst)
```

相关声明：[DT_INST_NUM_NVMEM_CELLS](../storage/P018_NVMEM设备树辅助宏.md#gac38526df0e386dfe22539e26b0a8eccf)。

获取DT_DRV_COMPAT实例的nvmem-cells属性中的元素数量。

<a id="r_ga1584c2c0238d1b25a50ad7f031401b29"></a>

```c
#define DT_INST_NVMEM_CELL_BY_IDX(inst, idx)
```

相关声明：[DT_INST_NVMEM_CELL_BY_IDX](../storage/P018_NVMEM设备树辅助宏.md#ga1584c2c0238d1b25a50ad7f031401b29)。

按索引从nvmem-cells节点引用数组属性获取控制器节点引用（Controller Phandle）的节点标识符。

<a id="r_gad4d8e5a98af8a27e11c315ae91f48b61"></a>

```c
#define DT_INST_NVMEM_CELL(inst)
```

相关声明：[DT_INST_NVMEM_CELL](../storage/P018_NVMEM设备树辅助宏.md#gad4d8e5a98af8a27e11c315ae91f48b61)。

获取DT_DRV_COMPAT实例索引0处NVMEM数据单元的节点标识符。

<a id="r_gabeadd3a51084b52bd8a4b02d45ea025a"></a>

```c
#define DT_INST_NVMEM_CELL_BY_NAME(inst, name)
```

相关声明：[DT_INST_NVMEM_CELL_BY_NAME](../storage/P018_NVMEM设备树辅助宏.md#gabeadd3a51084b52bd8a4b02d45ea025a)。

按名称从nvmem-cells节点引用数组属性获取控制器节点引用（Controller Phandle）的节点标识符。

<a id="r_gaf664c3e960ba047489fbc10eab6113e4"></a>

```c
#define DT_MTD_FROM_NVMEM_CELL(node_id)
```

相关声明：[DT_MTD_FROM_NVMEM_CELL](../storage/P018_NVMEM设备树辅助宏.md#gaf664c3e960ba047489fbc10eab6113e4)。

获取NVMEM数据单元所属存储控制器（Memory Controller）的节点标识符。

## 2.2\_源码定位与版本边界

本册包含NVMEM公共头文件源码、设备树头文件参考与源码、保留内存及数据保留服务源码，以及官方Nordic保留扩展源码。相对定位：[NVMEM设备树宏](../../../include/zephyr/devicetree/nvmem.h)、[NVMEM接口](../../../include/zephyr/nvmem.h)和[读写分派](../../../subsys/nvmem/nvmem.c)；完整原始文件摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：阅读关系：详细宏参数和原始设备树示例见[已有设备树辅助宏](../storage/P018_NVMEM设备树辅助宏.md)。本页补齐头文件参考，源码页保留完整展开式；这些宏在编译阶段处理节点标识和属性，不在运行时读取存储数据。

> 译注——源码核对：节点与控制器：原文两个DT_INST_NVMEM_CELL_BY_*摘要使用controller phandle措辞，但实际展开调用DT_NVMEM_CELL_BY_*，取得的是数据单元节点。要取得底层存储控制器，DT_MTD_FROM_NVMEM_CELL使用DT_GPARENT取得祖父节点；它依赖既定设备树层级，不是递归搜索任意祖先。

> 译注——源码核对：索引和名称：idx是nvmem-cells属性中的逻辑索引，不是存储字节偏移；name是由nvmem-cell-names形成的标识符形式，不是运行时字符串。DT_INST_*把inst交给DT_DRV_INST，依赖当前驱动的DT_DRV_COMPAT定义。第零项辅助宏不检查数组非空，NUM宏也不自动在属性缺失时返回0；使用方应先核对属性与所需索引／名称存在。

本次验证范围为文档与源码对照，未编译或执行存储写入、掉电、低功耗、非法参数及实板实验。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的源码](P003_NVMEM设备树头文件源码.md)
- [DT_NVMEM_CELLS_HAS_IDX](../storage/P018_NVMEM设备树辅助宏.md#ga477ec6b0fcb8dfeed591ae17ee26ce4a)
- [DT_NVMEM_CELLS_HAS_NAME](../storage/P018_NVMEM设备树辅助宏.md#ga75c4f7ef73d6802dec48be9a9a042811)
- [DT_NUM_NVMEM_CELLS](../storage/P018_NVMEM设备树辅助宏.md#gac87acacf5e5d6f0ed57d910b09e2578a)
- [DT_NVMEM_CELL_BY_IDX](../storage/P018_NVMEM设备树辅助宏.md#gadc09f069ab5823011bccfd2b87604330)
- [DT_NVMEM_CELL](../storage/P018_NVMEM设备树辅助宏.md#gad53d706e576954c8e8dd2739cc99d306)
- [DT_NVMEM_CELL_BY_NAME](../storage/P018_NVMEM设备树辅助宏.md#ga42848d5418cfed0c5c003ba7484584b7)
- [DT_INST_NVMEM_CELLS_HAS_IDX](../storage/P018_NVMEM设备树辅助宏.md#ga30989613f7ad97d47a8f620a17f08db9)
- [DT_INST_NVMEM_CELLS_HAS_NAME](../storage/P018_NVMEM设备树辅助宏.md#gaf984c322b72e49e75401d655126ab728)
- [DT_INST_NUM_NVMEM_CELLS](../storage/P018_NVMEM设备树辅助宏.md#gac38526df0e386dfe22539e26b0a8eccf)
- [DT_INST_NVMEM_CELL_BY_IDX](../storage/P018_NVMEM设备树辅助宏.md#ga1584c2c0238d1b25a50ad7f031401b29)
- [DT_INST_NVMEM_CELL](../storage/P018_NVMEM设备树辅助宏.md#gad4d8e5a98af8a27e11c315ae91f48b61)
- [DT_INST_NVMEM_CELL_BY_NAME](../storage/P018_NVMEM设备树辅助宏.md#gabeadd3a51084b52bd8a4b02d45ea025a)
- [DT_MTD_FROM_NVMEM_CELL](../storage/P018_NVMEM设备树辅助宏.md#gaf664c3e960ba047489fbc10eab6113e4)

<a id="header-details"></a>

---

[上一章](P001_NVMEM公共头文件源码.md) · [返回大纲](大纲.md) · [下一章](P003_NVMEM设备树头文件源码.md)
