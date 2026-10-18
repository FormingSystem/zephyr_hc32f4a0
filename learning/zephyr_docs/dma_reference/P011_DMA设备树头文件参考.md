---
id: learning.zephyr-docs.dma-reference.page-11
title: DMA设备树头文件参考
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_DMA设备树头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2dma_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

DMA设备树宏公共API头文件。

[查看此文件的源码。](P012_DMA设备树头文件源码.md)

<a id="details"></a>

DMA设备树宏公共API头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_gac74e56d90f8abe4bb0b53acddb618a3a"></a>

```c
#define DT_DMAS_CTLR_BY_IDX(node_id, idx)
```

相关声明：[DT_DMAS_CTLR_BY_IDX](P008_DMA设备树宏.md#gac74e56d90f8abe4bb0b53acddb618a3a)。

按索引从dmas属性取得DMA控制器的节点标识符（Node Identifier）。

<a id="r_ga8c148fc826dee34f5e4601f4a7aa9f55"></a>

```c
#define DT_DMAS_CTLR_BY_NAME(node_id, name)
```

相关声明：[DT_DMAS_CTLR_BY_NAME](P008_DMA设备树宏.md#ga8c148fc826dee34f5e4601f4a7aa9f55)。

按名称从dmas属性取得DMA控制器的节点标识符（Node Identifier）。

<a id="r_ga09a22a0e5133dc7514680c16373f6ad3"></a>

```c
#define DT_DMAS_CTLR(node_id)
```

相关声明：[DT_DMAS_CTLR](P008_DMA设备树宏.md#ga09a22a0e5133dc7514680c16373f6ad3)。

等价于DT_DMAS_CTLR_BY_IDX(node_id, 0)。

<a id="r_ga5dbb1f22a0098a3493fd6f4cef9985a9"></a>

```c
#define DT_INST_DMAS_CTLR_BY_IDX(inst, idx)
```

相关声明：[DT_INST_DMAS_CTLR_BY_IDX](P008_DMA设备树宏.md#ga5dbb1f22a0098a3493fd6f4cef9985a9)。

按索引从DT_DRV_COMPAT对应实例的dmas属性取得DMA控制器的节点标识符。

<a id="r_gad098f0b51ee1f629c1259ca346f49303"></a>

```c
#define DT_INST_DMAS_CTLR_BY_NAME(inst, name)
```

相关声明：[DT_INST_DMAS_CTLR_BY_NAME](P008_DMA设备树宏.md#gad098f0b51ee1f629c1259ca346f49303)。

按名称从DT_DRV_COMPAT对应实例的dmas属性取得DMA控制器的节点标识符。

<a id="r_ga32025fb8590eec09adaff23db1138e75"></a>

```c
#define DT_INST_DMAS_CTLR(inst)
```

相关声明：[DT_INST_DMAS_CTLR](P008_DMA设备树宏.md#ga32025fb8590eec09adaff23db1138e75)。

等价于DT_INST_DMAS_CTLR_BY_IDX(inst, 0)。

<a id="r_ga8aff7a91d19482964b8b56cb558c1b59"></a>

```c
#define DT_DMAS_CELL_BY_IDX(node_id, idx, cell)
```

相关声明：[DT_DMAS_CELL_BY_IDX](P008_DMA设备树宏.md#ga8aff7a91d19482964b8b56cb558c1b59)。

按索引取得DMA说明符（Specifier）中的单元（Cell）值。

<a id="r_gad4e1a8f22b8943328df2a3f8f2a149b7"></a>

```c
#define DT_INST_DMAS_CELL_BY_IDX(inst, idx, cell)
```

相关声明：[DT_INST_DMAS_CELL_BY_IDX](P008_DMA设备树宏.md#gad4e1a8f22b8943328df2a3f8f2a149b7)。

按索引取得DT_DRV_COMPAT对应实例的DMA说明符中的单元值。

<a id="r_ga1b80ae7fee6bcc9aa2ad03435e70dd14"></a>

```c
#define DT_DMAS_CELL_BY_NAME(node_id, name, cell)
```

相关声明：[DT_DMAS_CELL_BY_NAME](P008_DMA设备树宏.md#ga1b80ae7fee6bcc9aa2ad03435e70dd14)。

按名称取得DMA说明符中的单元值。

<a id="r_ga2843380c317657cd5f50cdacb9e93939"></a>

```c
#define DT_DMAS_CELL_BY_NAME_OR(node_id, name, cell, default_value)
```

相关声明：[DT_DMAS_CELL_BY_NAME_OR](P008_DMA设备树宏.md#ga2843380c317657cd5f50cdacb9e93939)。

与DT_DMAS_CELL_BY_NAME()类似，但可回退到default_value。

<a id="r_ga2cc0124a66cf3b9f1c4c506b7f978d30"></a>

```c
#define DT_INST_DMAS_CELL_BY_NAME(inst, name, cell)
```

相关声明：[DT_INST_DMAS_CELL_BY_NAME](P008_DMA设备树宏.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)。

按名称取得DT_DRV_COMPAT对应实例的DMA说明符中的单元值。

<a id="r_gab789e18935628f40d80f3b64ca5cbe80"></a>

```c
#define DT_DMAS_HAS_IDX(node_id, idx)
```

相关声明：[DT_DMAS_HAS_IDX](P008_DMA设备树宏.md#gab789e18935628f40d80f3b64ca5cbe80)。

索引idx对dmas属性是否有效？

<a id="r_gaff634d5b2a342c73f001a5ee64b70829"></a>

```c
#define DT_INST_DMAS_HAS_IDX(inst, idx)
```

相关声明：[DT_INST_DMAS_HAS_IDX](P008_DMA设备树宏.md#gaff634d5b2a342c73f001a5ee64b70829)。

索引idx对DT_DRV_COMPAT对应实例的dmas属性是否有效？

<a id="r_ga865adb5b82c63e7f63451b96cd5a6404"></a>

```c
#define DT_DMAS_HAS_NAME(node_id, name)
```

相关声明：[DT_DMAS_HAS_NAME](P008_DMA设备树宏.md#ga865adb5b82c63e7f63451b96cd5a6404)。

dmas属性是否具有指定名称的元素？

<a id="r_gad60c155da3d850a61365ca7d12dc1813"></a>

```c
#define DT_INST_DMAS_HAS_NAME(inst, name)
```

相关声明：[DT_INST_DMAS_HAS_NAME](P008_DMA设备树宏.md#gad60c155da3d850a61365ca7d12dc1813)。

DT_DRV_COMPAT对应实例的dmas属性是否具有指定名称的元素？

## 11.2\_源码定位与配置边界

本页汇总15个DMA设备树宏；完整参数、示例和展开值见[DMA设备树宏](P008_DMA设备树宏.md)，可见代码见[头文件源码](P012_DMA设备树头文件源码.md)。仓库相对定位：[devicetree/dma.h](../../../include/zephyr/devicetree/dma.h)。

各页官方HTML及源码摘要见[来源记录](../SOURCES.md)。本地源码、main和latest不能自动视为同一版本；本批只翻译和核对，不编译设备树、运行DMA或进行实板验证。

## 11.3\_原页交叉引用（Cross References）

- [Go to the source code of this file.](P012_DMA设备树头文件源码.md)
- [DT_DMAS_CTLR_BY_IDX](P008_DMA设备树宏.md#gac74e56d90f8abe4bb0b53acddb618a3a)
- [DT_DMAS_CTLR_BY_NAME](P008_DMA设备树宏.md#ga8c148fc826dee34f5e4601f4a7aa9f55)
- [DT_DMAS_CTLR](P008_DMA设备树宏.md#ga09a22a0e5133dc7514680c16373f6ad3)
- [DT_INST_DMAS_CTLR_BY_IDX](P008_DMA设备树宏.md#ga5dbb1f22a0098a3493fd6f4cef9985a9)
- [DT_INST_DMAS_CTLR_BY_NAME](P008_DMA设备树宏.md#gad098f0b51ee1f629c1259ca346f49303)
- [DT_INST_DMAS_CTLR](P008_DMA设备树宏.md#ga32025fb8590eec09adaff23db1138e75)
- [DT_DMAS_CELL_BY_IDX](P008_DMA设备树宏.md#ga8aff7a91d19482964b8b56cb558c1b59)
- [DT_INST_DMAS_CELL_BY_IDX](P008_DMA设备树宏.md#gad4e1a8f22b8943328df2a3f8f2a149b7)
- [DT_DMAS_CELL_BY_NAME](P008_DMA设备树宏.md#ga1b80ae7fee6bcc9aa2ad03435e70dd14)
- [DT_DMAS_CELL_BY_NAME_OR](P008_DMA设备树宏.md#ga2843380c317657cd5f50cdacb9e93939)
- [DT_INST_DMAS_CELL_BY_NAME](P008_DMA设备树宏.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)
- [DT_DMAS_HAS_IDX](P008_DMA设备树宏.md#gab789e18935628f40d80f3b64ca5cbe80)
- [DT_INST_DMAS_HAS_IDX](P008_DMA设备树宏.md#gaff634d5b2a342c73f001a5ee64b70829)
- [DT_DMAS_HAS_NAME](P008_DMA设备树宏.md#ga865adb5b82c63e7f63451b96cd5a6404)
- [DT_INST_DMAS_HAS_NAME](P008_DMA设备树宏.md#gad60c155da3d850a61365ca7d12dc1813)

<a id="header-details"></a>

---

[上一章](P010_DMA驱动头文件源码.md) · [返回大纲](大纲.md) · [下一章](P012_DMA设备树头文件源码.md)
