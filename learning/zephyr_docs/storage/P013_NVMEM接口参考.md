---
id: learning.zephyr-docs.storage.storageapi-0
title: NVMEM接口参考
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第13章\_NVMEM接口参考

原文：[group__nvmem__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html)。读取日期：2026-10-13，`latest`。

本页为**非易失性存储器（Non-Volatile Memory，NVMEM）**数据单元应用程序编程接口（Application Programming Interface，API），自 Zephyr 4.3 提供，接口版本为 0.1.0。公共头文件是 [`zephyr/nvmem.h`](P020_NVMEM公共头文件.md)。数据单元由 [`struct nvmem_cell`](P019_NVMEM数据单元结构.md) 表示，设备树相关辅助功能见 [NVMEM设备树辅助宏](P018_NVMEM设备树辅助宏.md)。

## 13.1\_初始化宏的参数约定

以下宏产生**静态初始化器（Static Initializer）**，用于初始化 `struct nvmem_cell` 结构体。`node_id` 为设备树节点标识；除 [`NVMEM_CELL_INIT`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#ga5ba7831633e9309fec2b9008c9dd4498) 直接接收数据单元节点外，其他普通宏接收包含或可能包含 `nvmem-cells` 属性的使用者节点。

索引参数 `idx` 是 `nvmem-cells` 属性中的逻辑索引；名称参数 `name` 来自节点的 `nvmem-cell-names`，写成小写加下划线形式。带实例号的宏使用 `inst`，它是 `DT_DRV_COMPAT` 对应驱动兼容类型的实例编号。`default_value` 是无法取得对应条目时展开的回退值（Fallback Value）。

原例中的 [`DT_NODELABEL`](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79) 宏按节点标签取节点标识，[`DEVICE_DT_GET`](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7) 宏取得设备指针。其他 `DT_*` 标识是设备树辅助宏；原始定义和用法均保留，便于与设备树展开结果对照。

## 13.2\_按索引取得数据单元

`NVMEM_CELL_GET_BY_IDX(node_id, idx)` 根据设备树使用者节点及索引，返回对应属性条目的 `struct nvmem_cell` 静态初始化器。`node_id` 必须具有 `nvmem-cells` 属性。

官方宏定义：

```c
NVMEM_CELL_INIT(DT_NVMEM_CELL_BY_IDX(node_id, idx))
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

对应使用示例：

```c
const struct nvmem_cell cell =
   NVMEM_CELL_GET_BY_IDX(DT_NODELABEL(eth), 0);

// Initializes 'cell' to:
// {
// .dev = DEVICE_DT_GET(DT_NODELABEL(mac_eeprom)),
// .offset = 0xfa,
// .size = 6,
// .read_only = false,
// }
```

示例中的 `cell` 是结构体变量：设备指向 `mac_eeprom`，偏移为 `0xfa`，大小为 6 字节，只读标志为 `false`。相关实例形式是 [`NVMEM_CELL_INST_GET_BY_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#gab35104744a5bc8759bada64f49c789a3)。

## 13.3\_按索引取得或使用回退值

`NVMEM_CELL_GET_BY_IDX_OR(node_id, idx, default_value)` 的 `node_id` 可以指向可能具有 `nvmem-cells` 属性的节点，`idx` 为属性逻辑索引，`default_value` 为回退展开值。返回对应数据单元的静态初始化器；原文说明节点或属性不存在时返回回退值。

原文描述：节点有 `nvmem-cells` 属性时展开为 `NVMEM_CELL_GET_BY_IDX(node_id, idx)`，这种情况下不展开 `default_value`；否则展开为回退值。官方定义如下。译注：条件宏 `COND_CODE_1` 根据检查结果选择展开分支，`DT_PROP_HAS_IDX` 与 `DT_PROP_HAS_NAME` 分别检查索引和名称是否存在。

```c
COND_CODE_1(DT_PROP_HAS_IDX(node_id, nvmem_cells, idx),                                    \
            (NVMEM_CELL_GET_BY_IDX(node_id, idx)),                                         \
            (default_value))
```

译注：定义实际通过 [`DT_PROP_HAS_IDX`](../dt_property_reference/P001_设备树属性读取宏.md#ga479dfc704087eea7e7c5af42ae98576c) 检查指定索引是否存在，条件比说明中的“有该属性”更具体。应按定义理解：指定索引存在才取得条目，否则使用回退值。对应实例宏为 [`NVMEM_CELL_INST_GET_BY_IDX_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#ga2187065079caf2bcdbe45843d579cfa4)。

## 13.4\_按名称取得数据单元

`NVMEM_CELL_GET_BY_NAME(node_id, name)` 根据使用者节点及名称，返回对应条目的静态初始化器。节点必须具有 `nvmem-cells`，名称取自 `nvmem-cell-names` 并转换为小写加下划线形式。

官方宏定义：

```c
NVMEM_CELL_INIT(DT_NVMEM_CELL_BY_NAME(node_id, name))
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

对应使用示例：

```c
const struct nvmem_cell cell =
   NVMEM_CELL_GET_BY_NAME(DT_NODELABEL(eth), mac_address);

// Initializes 'cell' to:
// {
// .dev = DEVICE_DT_GET(DT_NODELABEL(mac_eeprom)),
// .offset = 0xfa,
// .size = 6,
// .read_only = false,
// }
```

这里设备树中的 `mac-address` 对应 C 宏参数 `mac_address`，结构体结果与前面的按索引示例一致。相关实例形式是 [`NVMEM_CELL_INST_GET_BY_NAME`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#gad6e7abf1c54353696ec0d87763c71a5e)。

## 13.5\_按名称取得或使用回退值

`NVMEM_CELL_GET_BY_NAME_OR(node_id, name, default_value)` 接收可能具有 `nvmem-cells` 属性的节点、由 `nvmem-cell-names` 转成小写下划线形式的名称，以及回退展开值。返回对应条目的静态初始化器；原文说明节点或属性不存在时使用回退值。

原文描述：有 `nvmem-cells` 属性时展开为 `NVMEM_CELL_GET_BY_NAME(node_id, name)`，并且不展开 `default_value`；否则展开为回退值。官方定义如下。译注：条件宏 `COND_CODE_1` 根据检查结果选择展开分支，`DT_PROP_HAS_IDX` 与 `DT_PROP_HAS_NAME` 分别检查索引和名称是否存在。

```c
COND_CODE_1(DT_PROP_HAS_NAME(node_id, nvmem_cells, name),                                  \
            (NVMEM_CELL_GET_BY_NAME(node_id, name)),                                       \
            (default_value))
```

译注：定义实际使用 [`DT_PROP_HAS_NAME`](../dt_property_reference/P001_设备树属性读取宏.md#gae46c100aecd299eaea51e033890d9a58) 检查指定名称是否存在，应按这个更具体的条件判断是否走回退分支。相关实例形式为 [`NVMEM_CELL_INST_GET_BY_NAME_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#gaa7df326a030b03274d3e3d451a819768)。

## 13.6\_直接从数据单元节点初始化

`NVMEM_CELL_INIT(node_id)` 的参数是 NVMEM 数据单元节点标识，返回 `struct nvmem_cell` 静态初始化器。它是供其他 `NVMEM_CELL_GET` 宏初始化结构体时使用的辅助宏。

官方定义如下。译注：`DT_MTD_FROM_NVMEM_CELL` 宏取得数据单元所属存储设备的节点，`DT_REG_ADDR` 与 `DT_REG_SIZE` 宏读取其 `reg` 地址和大小，`DT_PROP` 宏取得指定属性；这里用于取得只读属性。

```c
{                                                                                          \
        .dev = DEVICE_DT_GET(DT_MTD_FROM_NVMEM_CELL(node_id)),                             \
        .offset = DT_REG_ADDR(node_id),                                                    \
        .size = DT_REG_SIZE(node_id),                                                      \
        .read_only = DT_PROP(node_id, read_only),                                          \
}
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
```

对应使用示例：

```c
const struct nvmem_cell cell = NVMEM_CELL_INIT(DT_NODELABEL(mac_address));

// Initializes 'cell' to:
// {
// .dev = DEVICE_DT_GET(DT_NODELABEL(mac_eeprom)),
// .offset = 0xfa,
// .size = 6,
// .read_only = false,
// }
```

初始化器的字段分别为设备 `dev`、偏移 `offset`、大小 `size` 和只读状态 `read_only`。

## 13.7\_驱动实例的索引形式

`NVMEM_CELL_INST_GET_BY_IDX(inst, idx)` 从 `DT_DRV_COMPAT` 驱动实例中按索引取得数据单元静态初始化器。`inst` 为实例编号，`idx` 为其 `nvmem-cells` 的逻辑索引。返回值是对应属性条目的初始化器，与 [`NVMEM_CELL_GET_BY_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#ga2d8ded7e090878d8dee0e2a4c3daac7b) 对应。

```c
NVMEM_CELL_GET_BY_IDX(DT_DRV_INST(inst), idx)
```

`NVMEM_CELL_INST_GET_BY_IDX_OR(inst, idx, default_value)` 增加回退展开值参数；返回条目初始化器，或在相应节点/属性条件不满足时返回 `default_value`。它委托给上一节已说明条件的普通索引回退宏。

```c
NVMEM_CELL_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)
```

## 13.8\_驱动实例的名称形式

`NVMEM_CELL_INST_GET_BY_NAME(inst, name)` 从 `DT_DRV_COMPAT` 实例中按名称取得数据单元静态初始化器。`inst` 为实例编号，`name` 是其 `nvmem-cell-names` 中小写加下划线形式的名称。返回对应条目的初始化器，与 [`NVMEM_CELL_GET_BY_NAME`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#ga6ba5137ac2ca250c769b32506d2eddae) 对应。

```c
NVMEM_CELL_GET_BY_NAME(DT_DRV_INST(inst), name)
```

`NVMEM_CELL_INST_GET_BY_NAME_OR(inst, name, default_value)` 还接受回退展开值；返回对应初始化器，或在相应节点/属性条件不满足时返回 `default_value`。它委托给普通名称回退宏，名称检查条件与前文一致。

```c
NVMEM_CELL_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)
```

## 13.9\_就绪与只读检查

两个函数均为静态内联函数（Static Inline Function），公共头文件仍为 `zephyr/nvmem.h`。注意它们对空指针的要求不同：

```c
static inline bool nvmem_cell_is_read_only(const struct nvmem_cell *cell);
static inline bool nvmem_cell_is_ready(const struct nvmem_cell *cell);
```

<a id="gac8abd20a158e3c304c73d6cb7e8cc50a"></a>

[`nvmem_cell_is_read_only()`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#gac8abd20a158e3c304c73d6cb7e8cc50a) 的 `cell` 是待检查数据单元，**不能为 `NULL`**；只读时返回 `true`，否则返回 `false`。

<a id="ga614cac8acc913cb2f7b62c2f0d625421"></a>

[`nvmem_cell_is_ready()`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#ga614cac8acc913cb2f7b62c2f0d625421) 的 `cell` **可以为 `NULL`**；数据单元已就绪可用时返回 `true`，否则返回 `false`。

## 13.10\_按字节读写数据

以下函数仅在启用 Kconfig 配置项 [`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM) 时可用。`off` 是数据单元内部的字节偏移，必须小于数据单元大小；`len` 是字节数量，`off + len` 不得超过数据单元大小。

<a id="ga5db94733cecfd4b46dd87ee07128d58d"></a>

<a id="gaef749ffc4b49e2e37b489fab2d8fa6b4"></a>

```c
int nvmem_cell_read(const struct nvmem_cell *cell, void *data,
                    off_t off, size_t len);
int nvmem_cell_write(const struct nvmem_cell *cell, const void *data,
                     off_t off, size_t len);
```

读取函数的 `cell` 是数据来源，输出参数 `data` 指向至少能容纳 `len` 字节的缓冲区。写入函数的 `cell` 是目标且不得只读，输入参数 `data` 指向至少包含 `len` 字节待写数据的缓冲区。

两个函数返回底层设备 API 的调用结果。原页明确列出的错误如下：

| 返回值 | 含义 | 适用函数 |
| --- | --- | --- |
| `-EINVAL` | 偏移或长度参数无效 | 读取与写入 |
| `-ENODEV` | 控制器设备未就绪 | 读取与写入 |
| `-ENXIO` | 没有可用的运行时设备 API | 读取与写入 |
| `-EROFS` | 试图向只读 NVMEM 数据单元写入 | 写入 |

## 13.11\_按字节序读取整数

**大端字节序（Big Endian，BE）**与**小端字节序（Little Endian，LE）**决定存储数据的字节顺序。下列静态内联函数从数据单元读取指定宽度的值，并把结果转换为**主机字节序（Host Endian）**。

所有读取函数的 `cell` 指定来源数据单元；输出参数 `val` 指向用于保存主机字节序结果的变量；`off` 为单元内开始读取的字节偏移。成功返回 `0`，失败返回负错误码。48 位数值通过 [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) 变量返回。

<a id="ga3929245cba736565c5d7f746b09147a4"></a>

<a id="ga405e1697ca3ff9c8f33a3fea5dc8ffdb"></a>

<a id="ga4fac111617d3a2a2affab26d239c91ea"></a>

<a id="ga8d0acdfeb984292616d0a5c8b90c37be"></a>

<a id="gabf0dc8224abaeec54537c84b4bf0aa9b"></a>

<a id="gacce8148eeac974048659efea2be2d9bf"></a>

<a id="gae0974ff5106a37609d218340aad758ff"></a>

<a id="gaf61422106876ef0995d0e5e6ebda6bd5"></a>

```c
static inline int nvmem_cell_read_be16(const struct nvmem_cell *cell, uint16_t *val, off_t off);
static inline int nvmem_cell_read_be32(const struct nvmem_cell *cell, uint32_t *val, off_t off);
static inline int nvmem_cell_read_be48(const struct nvmem_cell *cell, uint64_t *val, off_t off);
static inline int nvmem_cell_read_be64(const struct nvmem_cell *cell, uint64_t *val, off_t off);
static inline int nvmem_cell_read_le16(const struct nvmem_cell *cell, uint16_t *val, off_t off);
static inline int nvmem_cell_read_le32(const struct nvmem_cell *cell, uint32_t *val, off_t off);
static inline int nvmem_cell_read_le48(const struct nvmem_cell *cell, uint64_t *val, off_t off);
static inline int nvmem_cell_read_le64(const struct nvmem_cell *cell, uint64_t *val, off_t off);
```

函数名称中的 `be` 表示读取大端存储值，`le` 表示读取小端存储值；末尾的 `16`、`32`、`48`、`64` 表示所读取值的位数。

## 13.12\_按字节序写入整数

下列静态内联函数把主机字节序的整数，按名称指定的大端或小端形式写入数据单元。`cell` 指定目标，`val` 是主机字节序的待写值，`off` 是单元内开始写入的字节偏移。成功返回 `0`，失败返回负错误码。48 位写入的参数类型为 [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

<a id="ga1c119e9ad5817f47a6b99aaebc492da8"></a>

<a id="ga2ff30423cff4e064ab22cc13ff2fd60a"></a>

<a id="ga377f8afd53d1d84e630de96a3620c13a"></a>

<a id="ga43e38af86b79d9ae5d9933e95fbbb134"></a>

<a id="ga495e06601cfc7d7f41d3b16a58476b67"></a>

<a id="ga5846faeb71b80da68044229de943833b"></a>

<a id="ga8e4eca68269a125baa5ae1bd6813a50a"></a>

<a id="gac882709f9a2f8dcd4f48119cc73db3bd"></a>

```c
static inline int nvmem_cell_write_be16(const struct nvmem_cell *cell, uint16_t val, off_t off);
static inline int nvmem_cell_write_be32(const struct nvmem_cell *cell, uint32_t val, off_t off);
static inline int nvmem_cell_write_be48(const struct nvmem_cell *cell, uint64_t val, off_t off);
static inline int nvmem_cell_write_be64(const struct nvmem_cell *cell, uint64_t val, off_t off);
static inline int nvmem_cell_write_le16(const struct nvmem_cell *cell, uint16_t val, off_t off);
static inline int nvmem_cell_write_le32(const struct nvmem_cell *cell, uint32_t val, off_t off);
static inline int nvmem_cell_write_le48(const struct nvmem_cell *cell, uint64_t val, off_t off);
static inline int nvmem_cell_write_le64(const struct nvmem_cell *cell, uint64_t val, off_t off);
```

函数名称中的 `be`、`le` 和末尾位数含义与读取函数一致；参数 `val` 直接传值，不是读取接口使用的输出指针。


---

[上一章：存储服务入口](P012_存储服务入口.md) · [下一章：数据保留接口参考](P014_数据保留接口参考.md) · [返回大纲](大纲.md)
