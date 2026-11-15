---
id: learning.zephyr-docs.dma-reference.page-8
title: DMA设备树宏
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-dmas.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_DMA设备树宏

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-dmas.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_gac74e56d90f8abe4bb0b53acddb618a3a"></a>

```c
#define DT_DMAS_CTLR_BY_IDX(node_id, idx)
```

相关声明：[DT_DMAS_CTLR_BY_IDX](#gac74e56d90f8abe4bb0b53acddb618a3a)。

按索引从dmas属性取得DMA控制器的节点标识符（Node Identifier）。

<a id="r_ga8c148fc826dee34f5e4601f4a7aa9f55"></a>

```c
#define DT_DMAS_CTLR_BY_NAME(node_id, name)
```

相关声明：[DT_DMAS_CTLR_BY_NAME](#ga8c148fc826dee34f5e4601f4a7aa9f55)。

按名称从dmas属性取得DMA控制器的节点标识符（Node Identifier）。

<a id="r_ga09a22a0e5133dc7514680c16373f6ad3"></a>

```c
#define DT_DMAS_CTLR(node_id)
```

相关声明：[DT_DMAS_CTLR](#ga09a22a0e5133dc7514680c16373f6ad3)。

等价于DT_DMAS_CTLR_BY_IDX(node_id, 0)。

<a id="r_ga5dbb1f22a0098a3493fd6f4cef9985a9"></a>

```c
#define DT_INST_DMAS_CTLR_BY_IDX(inst, idx)
```

相关声明：[DT_INST_DMAS_CTLR_BY_IDX](#ga5dbb1f22a0098a3493fd6f4cef9985a9)。

按索引从DT_DRV_COMPAT对应实例的dmas属性取得DMA控制器的节点标识符。

<a id="r_gad098f0b51ee1f629c1259ca346f49303"></a>

```c
#define DT_INST_DMAS_CTLR_BY_NAME(inst, name)
```

相关声明：[DT_INST_DMAS_CTLR_BY_NAME](#gad098f0b51ee1f629c1259ca346f49303)。

按名称从DT_DRV_COMPAT对应实例的dmas属性取得DMA控制器的节点标识符。

<a id="r_ga32025fb8590eec09adaff23db1138e75"></a>

```c
#define DT_INST_DMAS_CTLR(inst)
```

相关声明：[DT_INST_DMAS_CTLR](#ga32025fb8590eec09adaff23db1138e75)。

等价于DT_INST_DMAS_CTLR_BY_IDX(inst, 0)。

<a id="r_ga8aff7a91d19482964b8b56cb558c1b59"></a>

```c
#define DT_DMAS_CELL_BY_IDX(node_id, idx, cell)
```

相关声明：[DT_DMAS_CELL_BY_IDX](#ga8aff7a91d19482964b8b56cb558c1b59)。

按索引取得DMA说明符（Specifier）中的单元（Cell）值。

<a id="r_gad4e1a8f22b8943328df2a3f8f2a149b7"></a>

```c
#define DT_INST_DMAS_CELL_BY_IDX(inst, idx, cell)
```

相关声明：[DT_INST_DMAS_CELL_BY_IDX](#gad4e1a8f22b8943328df2a3f8f2a149b7)。

按索引取得DT_DRV_COMPAT对应实例的DMA说明符中的单元值。

<a id="r_ga1b80ae7fee6bcc9aa2ad03435e70dd14"></a>

```c
#define DT_DMAS_CELL_BY_NAME(node_id, name, cell)
```

相关声明：[DT_DMAS_CELL_BY_NAME](#ga1b80ae7fee6bcc9aa2ad03435e70dd14)。

按名称取得DMA说明符中的单元值。

<a id="r_ga2843380c317657cd5f50cdacb9e93939"></a>

```c
#define DT_DMAS_CELL_BY_NAME_OR(node_id, name, cell, default_value)
```

相关声明：[DT_DMAS_CELL_BY_NAME_OR](#ga2843380c317657cd5f50cdacb9e93939)。

与DT_DMAS_CELL_BY_NAME()类似，但可回退到default_value。

<a id="r_ga2cc0124a66cf3b9f1c4c506b7f978d30"></a>

```c
#define DT_INST_DMAS_CELL_BY_NAME(inst, name, cell)
```

相关声明：[DT_INST_DMAS_CELL_BY_NAME](#ga2cc0124a66cf3b9f1c4c506b7f978d30)。

按名称取得DT_DRV_COMPAT对应实例的DMA说明符中的单元值。

<a id="r_gab789e18935628f40d80f3b64ca5cbe80"></a>

```c
#define DT_DMAS_HAS_IDX(node_id, idx)
```

相关声明：[DT_DMAS_HAS_IDX](#gab789e18935628f40d80f3b64ca5cbe80)。

索引idx对dmas属性是否有效？

<a id="r_gaff634d5b2a342c73f001a5ee64b70829"></a>

```c
#define DT_INST_DMAS_HAS_IDX(inst, idx)
```

相关声明：[DT_INST_DMAS_HAS_IDX](#gaff634d5b2a342c73f001a5ee64b70829)。

索引idx对DT_DRV_COMPAT对应实例的dmas属性是否有效？

<a id="r_ga865adb5b82c63e7f63451b96cd5a6404"></a>

```c
#define DT_DMAS_HAS_NAME(node_id, name)
```

相关声明：[DT_DMAS_HAS_NAME](#ga865adb5b82c63e7f63451b96cd5a6404)。

dmas属性是否具有指定名称的元素？

<a id="r_gad60c155da3d850a61365ca7d12dc1813"></a>

```c
#define DT_INST_DMAS_HAS_NAME(inst, name)
```

相关声明：[DT_INST_DMAS_HAS_NAME](#gad60c155da3d850a61365ca7d12dc1813)。

DT_DRV_COMPAT对应实例的dmas属性是否具有指定名称的元素？

## 8.2\_详细说明（Detailed Documentation）

<a id="ga8aff7a91d19482964b8b56cb558c1b59"></a>

### `DT_DMAS_CELL_BY_IDX`

```c
#define DT_DMAS_CELL_BY_IDX ( node_id, idx, cell )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_PHA_BY_IDX(node_id, dmas, idx, cell)
```

按索引取得DMA说明符（Specifier）中的单元（Cell）值。

设备树（Devicetree）片段示例：

```dts
dma1: dma@... {
        compatible = "vnd,dma";
        #dma-cells = <2>;
};

dma2: dma@... {
        compatible = "vnd,dma";
        #dma-cells = <2>;
};

n: node {
    dmas = <&dma1 1 0x400>,
           <&dma2 6 0x404>;
};
```

兼容标识（Compatible）vnd,dma的绑定（Binding）片段：

```yaml
dma-cells:
  - channel
  - config
```

用法示例：

```c
DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 0, channel) // 1
DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 1, channel) // 6
DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 0, config) // 0x400
DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 1, config) // 0x404
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有dmas属性的节点的标识符。 |
| `idx` | dmas属性中的逻辑索引（Logical Index）。 |
| `cell` | 采用小写字母与下划线形式的单元名称。 |

**返回（Returns）**：返回索引idx处的单元值。

**参阅（See Also）**：另请参阅DT_PHA_BY_IDX()。

> 译注——源码核对：idx选择一个DMA说明符，cell选择该说明符中的具名单元。原例vnd,dma绑定规定channel、config两个单元，故索引1的channel是6、config是0x404；这些名称与含义来自控制器绑定，不能推广成所有DMA控制器的固定布局。

<a id="ga1b80ae7fee6bcc9aa2ad03435e70dd14"></a>

### `DT_DMAS_CELL_BY_NAME`

```c
#define DT_DMAS_CELL_BY_NAME ( node_id, name, cell )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_PHA_BY_NAME(node_id, dmas, name, cell)
```

按名称取得DMA说明符中的单元值。

设备树（Devicetree）片段示例：

```dts
dma1: dma@... {
        compatible = "vnd,dma";
        #dma-cells = <2>;
};

dma2: dma@... {
        compatible = "vnd,dma";
        #dma-cells = <2>;
};

n: node {
    dmas = <&dma1 1 0x400>,
           <&dma2 6 0x404>;
    dma-names = "tx", "rx";
};
```

兼容标识（Compatible）vnd,dma的绑定（Binding）片段：

```yaml
dma-cells:
  - channel
  - config
```

用法示例：

```c
DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), tx, channel) // 1
DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), rx, channel) // 6
DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), tx, config) // 0x400
DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), rx, config) // 0x404
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有dmas属性的节点的标识符。 |
| `name` | dmas元素的名称，由节点的dma-names属性定义，以小写字母与下划线形式传入。 |
| `cell` | 采用小写字母与下划线形式的单元名称。 |

**返回（Returns）**：返回指定名称元素的说明符中的单元值。

**参阅（See Also）**：另请参阅DT_PHA_BY_NAME()。

<a id="ga2843380c317657cd5f50cdacb9e93939"></a>

### `DT_DMAS_CELL_BY_NAME_OR`

```c
#define DT_DMAS_CELL_BY_NAME_OR ( node_id, name, cell, default_value )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_PHA_BY_NAME_OR(node_id, dmas, name, cell, default_value)
```

与DT_DMAS_CELL_BY_NAME()类似，但可回退到default_value。

如果该值存在，则展开为DT_DMAS_CELL_BY_NAME(node_id, name, cell)，此时不展开default_value参数。

否则展开为default_value。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有dmas属性的节点的标识符。 |
| `name` | dmas元素的名称，由节点的dma-names属性定义，以小写字母与下划线形式传入。 |
| `cell` | 采用小写字母与下划线形式的单元名称。 |
| `default_value` | 回退时展开得到的值。 |

**返回（Returns）**：返回该单元的值或default_value。

**参阅（See Also）**：另请参阅DT_PHA_BY_NAME_OR()。

> 译注——源码核对：本次底层DT_PHA_BY_NAME_OR转发到DT_PROP_OR，按生成的具名单元是否存在选择值或default_value。它提供预处理期回退，不执行运行时异常处理，也不会自动创建DMA通道或修复无效绑定。

<a id="ga09a22a0e5133dc7514680c16373f6ad3"></a>

### `DT_DMAS_CTLR`

```c
#define DT_DMAS_CTLR ( node_id)
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_DMAS_CTLR_BY_IDX(node_id, 0)
```

等价于DT_DMAS_CTLR_BY_IDX(node_id, 0)。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有dmas属性的节点的标识符。 |

**返回（Returns）**：返回节点dmas属性中索引0处的DMA控制器节点标识符。

**参阅（See Also）**：另请参阅DT_DMAS_CTLR_BY_IDX()。

<a id="gac74e56d90f8abe4bb0b53acddb618a3a"></a>

### `DT_DMAS_CTLR_BY_IDX`

```c
#define DT_DMAS_CTLR_BY_IDX ( node_id, idx )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_PHANDLE_BY_IDX(node_id, dmas, idx)
```

按索引从dmas属性取得DMA控制器的节点标识符（Node Identifier）。

设备树（Devicetree）片段示例：

```dts
dma1: dma@... { ... };

dma2: dma@... { ... };

n: node {
    dmas = <&dma1 1 2 0x400 0x3>,
            <&dma2 6 3 0x404 0x5>;
};
```

用法示例：

```c
DT_DMAS_CTLR_BY_IDX(DT_NODELABEL(n), 0) // DT_NODELABEL(dma1)
DT_DMAS_CTLR_BY_IDX(DT_NODELABEL(n), 1) // DT_NODELABEL(dma2)
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有dmas属性的节点的标识符。 |
| `idx` | dmas属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回索引idx处所引用DMA控制器的节点标识符。

**参阅（See Also）**：另请参阅DT_PROP_BY_PHANDLE_IDX()。

> 译注——源码核对：idx是dmas属性中的元素序号，不是DMA硬件通道号。宏返回节点标识符，不是const struct device *，也不是控制器寄存器地址；取得设备对象还需通过DEVICE_DT_GET等设备模型接口，并按使用场景检查就绪状态。

<a id="ga8c148fc826dee34f5e4601f4a7aa9f55"></a>

### `DT_DMAS_CTLR_BY_NAME`

```c
#define DT_DMAS_CTLR_BY_NAME ( node_id, name )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_PHANDLE_BY_NAME(node_id, dmas, name)
```

按名称从dmas属性取得DMA控制器的节点标识符（Node Identifier）。

设备树（Devicetree）片段示例：

```dts
dma1: dma@... { ... };

dma2: dma@... { ... };

n: node {
    dmas = <&dma1 1 2 0x400 0x3>,
            <&dma2 6 3 0x404 0x5>;
    dma-names = "tx", "rx";
};
```

用法示例：

```c
DT_DMAS_CTLR_BY_NAME(DT_NODELABEL(n), tx) // DT_NODELABEL(dma1)
DT_DMAS_CTLR_BY_NAME(DT_NODELABEL(n), rx) // DT_NODELABEL(dma2)
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有dmas属性的节点的标识符。 |
| `name` | dmas元素的名称，由节点的dma-names属性定义，以小写字母与下划线形式传入。 |

**返回（Returns）**：返回指定名称元素中DMA控制器的节点标识符。

**参阅（See Also）**：另请参阅DT_PHANDLE_BY_NAME()。

> 译注——源码核对：name按dma-names选取对应dmas元素，例如tx或rx，不是带引号的C字符串。设备树名称转换成宏参数时使用小写与下划线形式。返回的仍是控制器节点标识符。

<a id="gab789e18935628f40d80f3b64ca5cbe80"></a>

### `DT_DMAS_HAS_IDX`

```c
#define DT_DMAS_HAS_IDX ( node_id, idx )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
IS_ENABLED(DT_CAT4(node_id, _P_dmas_IDX_, idx, _EXISTS))
```

索引idx对dmas属性是否有效？

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有dmas属性的节点的标识符。 |
| `idx` | dmas属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：若dmas属性包含索引idx，则返回1，否则返回0。

> 译注——源码核对：这是对生成的dmas元素存在标志的预处理期检查；返回1不证明DMA控制器已就绪、驱动已启用、通道空闲或目标硬件支持所需传输。

<a id="ga865adb5b82c63e7f63451b96cd5a6404"></a>

### `DT_DMAS_HAS_NAME`

```c
#define DT_DMAS_HAS_NAME ( node_id, name )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_PROP_HAS_NAME(node_id, dmas, name)
```

dmas属性是否具有指定名称的元素？

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有dmas属性的节点的标识符。 |
| `name` | dmas元素的名称，由节点的dma-names属性定义，以小写字母与下划线形式传入。 |

**返回（Returns）**：若dmas属性包含指定名称的元素，则返回1，否则返回0。

> 译注——源码核对：只判断dmas是否存在指定名称元素，不保证其中任意cell名称有效。读取具名单元仍应遵循对应控制器绑定。

<a id="gad4e1a8f22b8943328df2a3f8f2a149b7"></a>

### `DT_INST_DMAS_CELL_BY_IDX`

```c
#define DT_INST_DMAS_CELL_BY_IDX ( inst, idx, cell )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_PHA_BY_IDX(DT_DRV_INST(inst), dmas, idx, cell)
```

按索引取得DT_DRV_COMPAT对应实例的DMA说明符中的单元值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT对应的实例编号（Instance Number）。 |
| `idx` | dmas属性中的逻辑索引（Logical Index）。 |
| `cell` | 采用小写字母与下划线形式的单元名称。 |

**返回（Returns）**：返回索引idx处的单元值。

**参阅（See Also）**：另请参阅DT_DMAS_CELL_BY_IDX()。

<a id="ga2cc0124a66cf3b9f1c4c506b7f978d30"></a>

### `DT_INST_DMAS_CELL_BY_NAME`

```c
#define DT_INST_DMAS_CELL_BY_NAME ( inst, name, cell )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_DMAS_CELL_BY_NAME(DT_DRV_INST(inst), name, cell)
```

按名称取得DT_DRV_COMPAT对应实例的DMA说明符中的单元值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT对应的实例编号（Instance Number）。 |
| `name` | dmas元素的名称，由节点的dma-names属性定义，以小写字母与下划线形式传入。 |
| `cell` | 采用小写字母与下划线形式的单元名称。 |

**返回（Returns）**：返回指定名称元素的说明符中的单元值。

**参阅（See Also）**：另请参阅DT_DMAS_CELL_BY_NAME()。

<a id="ga32025fb8590eec09adaff23db1138e75"></a>

### `DT_INST_DMAS_CTLR`

```c
#define DT_INST_DMAS_CTLR ( inst)
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_INST_DMAS_CTLR_BY_IDX(inst, 0)
```

等价于DT_INST_DMAS_CTLR_BY_IDX(inst, 0)。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT对应的实例编号（Instance Number）。 |

**返回（Returns）**：返回实例dmas属性中索引0处的DMA控制器节点标识符。

**参阅（See Also）**：另请参阅DT_DMAS_CTLR_BY_IDX()。

<a id="ga5dbb1f22a0098a3493fd6f4cef9985a9"></a>

### `DT_INST_DMAS_CTLR_BY_IDX`

```c
#define DT_INST_DMAS_CTLR_BY_IDX ( inst, idx )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_DMAS_CTLR_BY_IDX(DT_DRV_INST(inst), idx)
```

按索引从DT_DRV_COMPAT对应实例的dmas属性取得DMA控制器的节点标识符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT对应的实例编号（Instance Number）。 |
| `idx` | dmas属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回索引idx处所引用DMA控制器的节点标识符。

**参阅（See Also）**：另请参阅DT_DMAS_CTLR_BY_IDX()。

<a id="gad098f0b51ee1f629c1259ca346f49303"></a>

### `DT_INST_DMAS_CTLR_BY_NAME`

```c
#define DT_INST_DMAS_CTLR_BY_NAME ( inst, name )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_DMAS_CTLR_BY_NAME(DT_DRV_INST(inst), name)
```

按名称从DT_DRV_COMPAT对应实例的dmas属性取得DMA控制器的节点标识符。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT对应的实例编号（Instance Number）。 |
| `name` | dmas元素的名称，由节点的dma-names属性定义，以小写字母与下划线形式传入。 |

**返回（Returns）**：返回指定名称元素中DMA控制器的节点标识符。

**参阅（See Also）**：另请参阅DT_DMAS_CTLR_BY_NAME()。

<a id="gaff634d5b2a342c73f001a5ee64b70829"></a>

### `DT_INST_DMAS_HAS_IDX`

```c
#define DT_INST_DMAS_HAS_IDX ( inst, idx )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_DMAS_HAS_IDX(DT_DRV_INST(inst), idx)
```

索引idx对DT_DRV_COMPAT对应实例的dmas属性是否有效？

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT对应的实例编号（Instance Number）。 |
| `idx` | dmas属性中的逻辑索引（Logical Index）。 |

**返回（Returns）**：若dmas属性在索引idx处具有说明符，则返回1，否则返回0。

<a id="gad60c155da3d850a61365ca7d12dc1813"></a>

### `DT_INST_DMAS_HAS_NAME`

```c
#define DT_INST_DMAS_HAS_NAME ( inst, name )
```

```c
#include <zephyr/devicetree/dma.h>
```

展开值（Value）：

```c
DT_DMAS_HAS_NAME(DT_DRV_INST(inst), name)
```

DT_DRV_COMPAT对应实例的dmas属性是否具有指定名称的元素？

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT对应的实例编号（Instance Number）。 |
| `name` | dmas元素的名称，由节点的dma-names属性定义，以小写字母与下划线形式传入。 |

**返回（Returns）**：若dmas属性包含指定名称的元素，则返回1，否则返回0。

## 8.3\_源码定位与配置边界

设备树宏定义在[devicetree/dma.h](../../../include/zephyr/devicetree/dma.h)，底层句柄数组（Phandle Array）访问由[devicetree.h](../../../include/zephyr/devicetree.h)提供。先用CTLR系列宏确定控制器节点，再按绑定中的cell名称取值；本文保留的示例只有占位节点地址，展示宏展开关系，不能直接当作完整板级设备树。

> 译注——读取配置不等于启动传输：这些宏在预处理期读取构建生成的设备树信息。DT_INST_系列将inst映射到DT_DRV_INST(inst)，该编号属于DT_DRV_COMPAT设备实例，不是通道号；实际申请、配置和启动仍分别使用[DMA公共接口](P001_DMA公共接口.md)。控制器绑定中的channel等值与通道申请策略是否直接对应，应以驱动约定为准。

头文件概览见[P011](P011_DMA设备树头文件参考.md)，可见源码见[P012](P012_DMA设备树头文件源码.md)。本次核对的[DMA宏头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree/dma.h)与[底层设备树头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/devicetree.h)分别记录摘要。

各页官方HTML及源码摘要见[来源记录](../SOURCES.md)。本地源码、main和latest不能自动视为同一版本；本批只翻译和核对，不编译设备树、运行DMA或进行实板验证。

## 8.4\_原页交叉引用（Cross References）

- [zephyr/devicetree/dma.h](P011_DMA设备树头文件参考.md)
- [DT_PHA_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga118b63fd22c20ef940ac2fa073c126ed)
- [DT_PHA_BY_NAME](../dt_property_reference/P001_设备树属性读取宏.md#gae469615356a867c49416da15bdc44a26)
- [DT_PHA_BY_NAME_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga79cda6ca70cc1e27b034ad096d4f4401)
- [DT_PHANDLE_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga8ff163c240878a988d29d727671671de)
- [DT_PROP_BY_PHANDLE_IDX()](../dt_property_reference/P001_设备树属性读取宏.md#gaeba973992914d493cff5506ecf86a00d)
- [DT_PHANDLE_BY_NAME](../dt_property_reference/P001_设备树属性读取宏.md#ga65c90d2d96255b8569c5b869b637c2fd)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [DT_PROP_HAS_NAME](../dt_property_reference/P001_设备树属性读取宏.md#gae46c100aecd299eaea51e033890d9a58)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)

<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-prop_html_ga118b63fd22c20ef940ac2fa073c126ed"></a>
<a id="agroup__devicetree-generic-prop_html_gae469615356a867c49416da15bdc44a26"></a>
<a id="agroup__devicetree-generic-prop_html_ga79cda6ca70cc1e27b034ad096d4f4401"></a>
<a id="agroup__devicetree-dmas_html_gac74e56d90f8abe4bb0b53acddb618a3a"></a>
<a id="agroup__devicetree-generic-prop_html_ga8ff163c240878a988d29d727671671de"></a>
<a id="agroup__devicetree-generic-prop_html_ga65c90d2d96255b8569c5b869b637c2fd"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__devicetree-generic-prop_html_gae46c100aecd299eaea51e033890d9a58"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__devicetree-dmas_html_ga1b80ae7fee6bcc9aa2ad03435e70dd14"></a>
<a id="agroup__devicetree-dmas_html_ga5dbb1f22a0098a3493fd6f4cef9985a9"></a>
<a id="agroup__devicetree-dmas_html_ga8c148fc826dee34f5e4601f4a7aa9f55"></a>
<a id="agroup__devicetree-dmas_html_gab789e18935628f40d80f3b64ca5cbe80"></a>
<a id="agroup__devicetree-dmas_html_ga865adb5b82c63e7f63451b96cd5a6404"></a>

---

[上一章](P007_DMA驱动操作结构.md) · [返回大纲](大纲.md) · [下一章](P009_DMA驱动头文件参考.md)
