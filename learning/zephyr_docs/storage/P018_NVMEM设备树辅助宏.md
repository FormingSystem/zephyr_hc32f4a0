---
id: learning.zephyr-docs.storage.nvmemextra-0
title: NVMEM设备树辅助宏
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-nvmem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第18章\_NVMEM设备树辅助宏

原文：[group__devicetree-nvmem](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-nvmem.html)。读取日期：2026-10-13，`latest`。

本页提供**非易失性存储器（Non-Volatile Memory，NVMEM）**的设备树（Devicetree）支持，公共头文件为 [`zephyr/devicetree/nvmem.h`](../memory_retention_reference/P002_NVMEM设备树头文件参考.md)。这些宏处理节点引用与属性，不执行运行时存储读写。

## 18.1\_节点、名称与实例参数

下文 `node_id` 为设备树节点标识，`idx` 为 `nvmem-cells` 属性中的逻辑索引；`name` 来自 `nvmem-cell-names`，在宏参数中写成小写加下划线的形式。**节点引用（Phandle）**指向数据单元节点，`nvmem-cells` 是节点引用及其说明单元数组（Phandle Array）。

实例参数 `inst` 是驱动兼容类型 `DT_DRV_COMPAT` 的实例编号，辅助宏 [`DT_DRV_INST`](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1) 把它转换为节点标识。示例中的 [`DT_NODELABEL`](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79) 宏按节点标签取标识。[`DT_PROP_LEN`](../dt_property_reference/P001_设备树属性读取宏.md#gaa7f5afcedd1f54be79a5337e8e28a5b6) 取得属性元素数量，[`DT_PROP_HAS_IDX`](../dt_property_reference/P001_设备树属性读取宏.md#ga479dfc704087eea7e7c5af42ae98576c)/[`DT_PROP_HAS_NAME`](../dt_property_reference/P001_设备树属性读取宏.md#gae46c100aecd299eaea51e033890d9a58) 检查索引/名称是否存在，[`DT_PHANDLE_BY_IDX`](../dt_property_reference/P001_设备树属性读取宏.md#ga8ff163c240878a988d29d727671671de)/[`DT_PHANDLE_BY_NAME`](../dt_property_reference/P001_设备树属性读取宏.md#ga65c90d2d96255b8569c5b869b637c2fd) 取得索引/名称指向的节点，[`DT_GPARENT`](../dt_identity_reference/P001_设备树节点标识宏.md#gaa4eccf276a426cbbc6e440d72b692753) 取得祖父节点。

## 18.2\_实例的数据单元数量与第零项

<a id="gac38526df0e386dfe22539e26b0a8eccf"></a>

`DT_INST_NUM_NVMEM_CELLS(inst)` 接收 `DT_DRV_COMPAT` 实例编号，返回其 `nvmem-cells` 属性中的元素数量，等价于 `DT_NUM_NVMEM_CELLS(DT_DRV_INST(inst))`。

```c
DT_NUM_NVMEM_CELLS(DT_DRV_INST(inst))
```

<a id="gad4d8e5a98af8a27e11c315ae91f48b61"></a>

`DT_INST_NVMEM_CELL(inst)` 接收实例编号，返回其 `nvmem-cells` 索引 0 处的数据单元节点标识，等价于 `DT_INST_NVMEM_CELL_BY_IDX(inst, 0)`；普通节点对应宏为 [`DT_NVMEM_CELL()`](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-nvmem.html#gad53d706e576954c8e8dd2739cc99d306)。

```c
DT_INST_NVMEM_CELL_BY_IDX(inst, 0)
```

## 18.3\_实例按索引或名称取得节点

<a id="ga1584c2c0238d1b25a50ad7f031401b29"></a>

`DT_INST_NVMEM_CELL_BY_IDX(inst, idx)` 的参数为驱动实例编号和 `nvmem-cells` 属性逻辑索引，返回索引 `idx` 引用的 NVMEM 数据单元节点标识。

```c
DT_NVMEM_CELL_BY_IDX(DT_DRV_INST(inst), idx)
```

译注：原页交叉引用写为 `DT_NVMEM_CELL_CTLR_BY_IDX()`，但本页没有定义此名称；上面的实际定义调用 [`DT_NVMEM_CELL_BY_IDX()`](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-nvmem.html#gadc09f069ab5823011bccfd2b87604330)，这里保留原引用差异。

<a id="gabeadd3a51084b52bd8a4b02d45ea025a"></a>

`DT_INST_NVMEM_CELL_BY_NAME(inst, name)` 的参数为实例编号，以及由 `nvmem-cell-names` 转换成小写下划线形式的名称。返回该名称引用的数据单元节点标识，对应普通节点宏 [`DT_NVMEM_CELL_BY_NAME()`](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-nvmem.html#ga42848d5418cfed0c5c003ba7484584b7)。

```c
DT_NVMEM_CELL_BY_NAME(DT_DRV_INST(inst), name)
```

译注：上述两个实例宏的原概述使用了“controller phandle”措辞，返回值说明和定义指向的是数据单元节点。要找数据单元所属的存储设备，使用后面的 [`DT_MTD_FROM_NVMEM_CELL`](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-nvmem.html#gaf664c3e960ba047489fbc10eab6113e4)。

## 18.4\_实例的存在性检查

<a id="ga30989613f7ad97d47a8f620a17f08db9"></a>

`DT_INST_NVMEM_CELLS_HAS_IDX(inst, idx)` 检查驱动实例是否具有 `nvmem-cells` 属性中的指定索引。`inst` 对应的实例可以有也可以没有此属性；`idx` 是要检查的索引。存在时展开为 `1`，否则为 `0`，等价于 `DT_NVMEM_CELLS_HAS_IDX(DT_DRV_INST(inst), idx)`。

```c
DT_NVMEM_CELLS_HAS_IDX(DT_DRV_INST(inst), idx)
```

<a id="gaf984c322b72e49e75401d655126ab728"></a>

`DT_INST_NVMEM_CELLS_HAS_NAME(inst, name)` 检查驱动实例是否具有包含给定名称的 `nvmem-cell-names` 属性。实例可以有也可以没有此属性；`name` 为小写下划线形式的名称。名称存在返回 `1`，否则返回 `0`，等价于 `DT_NVMEM_CELLS_HAS_NAME(DT_DRV_INST(inst), name)`。

```c
DT_NVMEM_CELLS_HAS_NAME(DT_DRV_INST(inst), name)
```

## 18.5\_取得数据单元所属的存储设备

<a id="gaf664c3e960ba047489fbc10eab6113e4"></a>

`DT_MTD_FROM_NVMEM_CELL(node_id)` 的参数是 NVMEM 数据单元节点标识，返回包含它的**存储技术设备（Memory Technology Device，MTD）**节点标识，即其存储控制器节点。

```c
DT_GPARENT(node_id)
```

官方设备树片段：

```dts
mac_eeprom: mac_eeprom@2 {
   nvmem-layout {
           compatible = "fixed-layout";
           #address-cells = <1>;
           #size-cells = <1>;

           mac_address: mac_address@fa {
                   reg = <0xfa 0x06>;
                   #nvmem-cell-cells = <0>;
           };
   };
};

eth: ethernet {
   nvmem-cells = <&mac_address>;
   nvmem-cell-names = "mac-address";
};
```

官方用法从以太网使用者的第零个数据单元找到 `mac_eeprom` 存储节点：

```c
DT_MTD_FROM_NVMEM_CELL(DT_NVMEM_CELL(DT_NODELABEL(eth))) // DT_NODELABEL(mac_eeprom)
```

## 18.6\_普通节点的数据单元数量

<a id="gac87acacf5e5d6f0ed57d910b09e2578a"></a>

`DT_NUM_NVMEM_CELLS(node_id)` 接收具有 `nvmem-cells` 属性的节点标识，返回该属性元素数量。

```c
DT_PROP_LEN(node_id, nvmem_cells)
```

官方设备树片段：

```dts
eth: ethernet {
   nvmem-cells = <&mac_address>;
   nvmem-cell-names = "mac-address";
};
```

官方用法，结果为一个元素：

```c
DT_NUM_NVMEM_CELLS(DT_NODELABEL(eth)) // 1
```

## 18.7\_普通节点的第零个数据单元

<a id="gad53d706e576954c8e8dd2739cc99d306"></a>

`DT_NVMEM_CELL(node_id)` 接收具有 `nvmem-cells` 属性的节点标识，返回索引 0 处的 NVMEM 数据单元节点标识。它等价于 `DT_NVMEM_CELL_BY_IDX(node_id, 0)`。

```c
DT_NVMEM_CELL_BY_IDX(node_id, 0)
```

## 18.8\_按索引取得数据单元节点

<a id="gadc09f069ab5823011bccfd2b87604330"></a>

`DT_NVMEM_CELL_BY_IDX(node_id, idx)` 的 `node_id` 必须具有 `nvmem-cells` 属性，`idx` 是属性中的索引；返回该索引的数据单元节点标识。

```c
DT_PHANDLE_BY_IDX(node_id, nvmem_cells, idx)
```

官方设备树片段：

```dts
mac_eeprom: mac_eeprom@2 {
   nvmem-layout {
           compatible = "fixed-layout";
           #address-cells = <1>;
           #size-cells = <1>;

           mac_address: mac_address@fa {
                   reg = <0xfa 0x06>;
                   #nvmem-cell-cells = <0>;
           };
   };
};

eth: ethernet {
   nvmem-cells = <&mac_address>;
   nvmem-cell-names = "mac-address";
};
```

官方用法，结果为 `mac_address` 节点标识：

```c
DT_NVMEM_CELL_BY_IDX(DT_NODELABEL(eth), 0) // DT_NODELABEL(mac_address)
```

## 18.9\_按名称取得数据单元节点

<a id="ga42848d5418cfed0c5c003ba7484584b7"></a>

`DT_NVMEM_CELL_BY_NAME(node_id, name)` 的 `node_id` 必须具有 `nvmem-cells` 属性，`name` 是 `nvmem-cell-names` 指定名称的小写下划线形式；返回该名称对应的数据单元节点标识。

```c
DT_PHANDLE_BY_NAME(node_id, nvmem_cells, name)
```

官方设备树片段：

```dts
mac_eeprom: mac_eeprom@2 {
   nvmem-layout {
           compatible = "fixed-layout";
           #address-cells = <1>;
           #size-cells = <1>;

           mac_address: mac_address@fa {
                   reg = <0xfa 0x06>;
                   #nvmem-cell-cells = <0>;
           };
   };
};

eth: ethernet {
   nvmem-cells = <&mac_address>;
   nvmem-cell-names = "mac-address";
};
```

官方用法，设备树名称 `mac-address` 在宏参数中写为 `mac_address`：

```c
DT_NVMEM_CELL_BY_NAME(DT_NODELABEL(eth), mac_address) // DT_NODELABEL(mac_address)
```

## 18.10\_检查索引是否存在

<a id="ga477ec6b0fcb8dfeed591ae17ee26ce4a"></a>

`DT_NVMEM_CELLS_HAS_IDX(node_id, idx)` 检查节点的 `nvmem-cells` 节点引用数组是否具有指定索引。节点可以有也可以没有这个属性；有效索引展开为 `1`，否则为 `0`。

```c
DT_PROP_HAS_IDX(node_id, nvmem_cells, idx)
```

官方设备树片段：

```dts
eth: ethernet {
   nvmem-cells = <&mac_address>;
   nvmem-cell-names = "mac-address";
};
```

官方用法显示索引 0 存在，索引 1 不存在：

```c
DT_NVMEM_CELLS_HAS_IDX(DT_NODELABEL(eth), 0) // 1
DT_NVMEM_CELLS_HAS_IDX(DT_NODELABEL(eth), 1) // 0
```

## 18.11\_检查名称是否存在

<a id="ga75c4f7ef73d6802dec48be9a9a042811"></a>

`DT_NVMEM_CELLS_HAS_NAME(node_id, name)` 检查节点的 `nvmem-cell-names` 数组是否包含指定名称。节点可以有也可以没有这个属性；`name` 用小写加下划线表示。名称存在展开为 `1`，否则为 `0`。

```c
DT_PROP_HAS_NAME(node_id, nvmem_cells, name)
```

官方设备树片段：

```dts
eth: ethernet {
   nvmem-cells = <&mac_address>;
   nvmem-cell-names = "mac-address";
};
```

官方用法显示 `mac_address` 存在，测试名称 `bogus` 不存在：

```c
DT_NVMEM_CELLS_HAS_NAME(DT_NODELABEL(eth), mac_address) // 1
DT_NVMEM_CELLS_HAS_NAME(DT_NODELABEL(eth), bogus)       // 0
```

译注：该宏原页返回值一句写作“index exists”，但概述、定义和示例均检查名称；这里按名称存在性说明，并指出原文措辞差异。


---

[上一章：设置运行时接口](P017_设置运行时接口.md) · [下一章：NVMEM数据单元结构](P019_NVMEM数据单元结构.md) · [返回大纲](大纲.md)
