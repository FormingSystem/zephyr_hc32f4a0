---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-8
title: PCIe 控制器（PCIe Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_PCIe 控制器（PCIe Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe 控制器接口。

<a id="details"></a>

PCIe 控制器接口。

<a id="header-groups"></a>
<a id="groups"></a>

## 8.1\_主题（Topics）

<a id="r_pcie_5Fcontroller_5Finterface_5Fbackend"></a>

相关声明：[PCIe 控制器驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html)。

<a id="header-files"></a>
<a id="files"></a>

## 8.2\_文件（Files）

<a id="r_controller_2Eh"></a>

```c
file controller.h
```

相关声明：[controller.h](../api_file_protocol_service_reference/P013_zephyr__drivers__pcie__controller.h_文件参考.md)。

PCIe控制器（Controllers）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.3\_数据结构（Data Structures）

<a id="r_pcie_5Fctrl_5Fconfig"></a>

```c
struct pcie_ctrl_config
```

相关声明：[pcie_ctrl_config](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md)。

描述支持PCI Express控制器API（Controller API）的设备的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.4\_宏定义（Macros）

<a id="r_ga91525130b94b07187633abd1e017aa61"></a>

```c
#define PCIE_RANGE_FORMAT(node_id, idx)
```

相关声明：[PCIE_RANGE_FORMAT](#ga91525130b94b07187633abd1e017aa61)。

根据设备树（Devicetree）填充 `pcie_ctrl_config.ranges` 表条目。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.5\_函数（Functions）

<a id="r_ga1d978b8075191d6e571349684c731a43"></a>

```c
static uint32_t pcie_ctrl_conf_read (const struct device *dev, pcie_bdf_t bdf, unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_ctrl_conf_read](#ga1d978b8075191d6e571349684c731a43)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

从端点配置空间（Endpoint Configuration Space）读取 32 位字（Word）。

<a id="r_ga5cfe01762e5af8dc0cc5fbd550ff7e74"></a>

```c
static void pcie_ctrl_conf_write (const struct device *dev, pcie_bdf_t bdf, unsigned int reg, uint32_t data)
```

相关声明：[pcie_ctrl_conf_write](#ga5cfe01762e5af8dc0cc5fbd550ff7e74)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向端点配置空间（Endpoint Configuration Space）写入 32 位字（Word）。

<a id="r_ga1de030e2e8b07509d75de5a348297f42"></a>

```c
static bool pcie_ctrl_region_allocate (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t bar_size, uintptr_t *bar_bus_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_allocate](#ga1de030e2e8b07509d75de5a348297f42)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

为端点基地址寄存器（BAR）分配内存区域子集（Memory Region Subset）。

<a id="r_gae7c109ca138adfd906fef5b6f3dca385"></a>

```c
static bool pcie_ctrl_region_get_allocate_base (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t align, uintptr_t *bar_base_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_get_allocate_base](#gae7c109ca138adfd906fef5b6f3dca385)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

获取为端点基地址寄存器（BAR）分配的内存区域子集当前分配基地址（Allocation Base）时调用的函数。

<a id="r_gae6fa104ea2cc85912ebb1cfe0a1a3ddf"></a>

```c
static bool pcie_ctrl_region_translate (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, uintptr_t bar_bus_addr, uintptr_t *bar_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_translate](#gae6fa104ea2cc85912ebb1cfe0a1a3ddf)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

将端点基地址寄存器（BAR）的总线地址（Bus-centric Address）转换为物理地址（Physical Address）。

<a id="r_ga69493e7da12c4c2d95f506ecf86e7dfe"></a>

```c
static uint8_t pcie_ctrl_msi_device_setup (const struct device *dev, unsigned int priority, msi_vector_t *vectors, uint8_t n_vector)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pcie_ctrl_msi_device_setup](#ga69493e7da12c4c2d95f506ecf86e7dfe)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[msi_vector_t](../api_vector_pipeline_topic_reference/P025_PCIe 主机消息信号中断（MSI）接口.md#ga9ede6a7a472ee62f0975256a1b5f1231)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

配置给定 PCI 端点（Endpoint），使其生成消息信号中断（Message Signaled Interrupts，MSIs）。

## 8.6\_详细说明（Detailed Documentation）

<a id="ga91525130b94b07187633abd1e017aa61"></a>

### `PCIE_RANGE_FORMAT`

```c
#define PCIE_RANGE_FORMAT ( node_id, idx )
```

```c
#include <zephyr/drivers/pcie/controller.h>
```

展开值（Value）：

```c
{                                                                                       \
        .flags = DT_RANGES_CHILD_BUS_FLAGS_BY_IDX(node_id, idx),                        \
        .pcie_bus_addr = DT_RANGES_CHILD_BUS_ADDRESS_BY_IDX(node_id, idx),              \
        .host_map_addr = DT_RANGES_PARENT_BUS_ADDRESS_BY_IDX(node_id, idx),             \
        .map_length = DT_RANGES_LENGTH_BY_IDX(node_id, idx),                            \
},
```

根据设备树（Devicetree）填充 `pcie_ctrl_config.ranges` 表条目。

旨在与 `DT_FOREACH_RANGE` 配合使用，根据控制器的 `ranges` 属性填充整个表。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | PCIe 控制器的设备树节点标识符（Devicetree Node Identifier）。 |
| `idx` | `ranges` 属性中的条目索引（Entry Index）。 |

<a id="ga1d978b8075191d6e571349684c731a43"></a>

### `pcie_ctrl_conf_read()`

```c
uint32_t pcie_ctrl_conf_read ( const struct device * dev, pcie_bdf_t bdf, unsigned int reg )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/pcie/controller.h>
```

从端点配置空间（Endpoint Configuration Space）读取 32 位字（Word）。

使用 PCI Express 控制器配置空间访问方式（Configuration Space Access Method），从端点配置空间读取一个 32 位字（Word）。访问方式可以是 I/O 端口、内存映射或自定义方法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PCI Express 控制器设备指针（Controller Device Pointer）。 |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `reg` | 配置字索引（Configuration Word Index），不是地址。 |

**返回（Returns）**：返回值：读出的字（Word）；端点或该字不存在时为 `0xFFFFFFFFU`。

<a id="ga5cfe01762e5af8dc0cc5fbd550ff7e74"></a>

### `pcie_ctrl_conf_write()`

```c
void pcie_ctrl_conf_write ( const struct device * dev, pcie_bdf_t bdf, unsigned int reg, uint32_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/pcie/controller.h>
```

向端点配置空间（Endpoint Configuration Space）写入 32 位字（Word）。

使用 PCI Express 控制器配置空间访问方式（Configuration Space Access Method），向端点配置空间写入一个 32 位字（Word）。访问方式可以是 I/O 端口、内存映射或自定义方法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PCI Express 控制器设备指针（Controller Device Pointer）。 |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `reg` | 配置字索引（Configuration Word Index），不是地址。 |
| `data` | 要写入的值（Value）。 |

<a id="ga69493e7da12c4c2d95f506ecf86e7dfe"></a>

### `pcie_ctrl_msi_device_setup()`

```c
uint8_t pcie_ctrl_msi_device_setup ( const struct device * dev, unsigned int priority, msi_vector_t * vectors, uint8_t n_vector )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/pcie/controller.h>
```

配置给定 PCI 端点（Endpoint），使其生成消息信号中断（Message Signaled Interrupts，MSIs）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PCI Express 控制器设备指针（Controller Device Pointer）。 |
| `priority` | 消息信号中断优先级（MSI Priority）。 |
| `vectors` | 已分配向量（Vector）的数组。 |
| `n_vector` | 向量数组（Vector Array）的大小。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_PCIE_MSI`。

**返回（Returns）**：返回值：已分配的中断向量数量（Number of Vectors）。

<a id="ga1de030e2e8b07509d75de5a348297f42"></a>

### `pcie_ctrl_region_allocate()`

```c
bool pcie_ctrl_region_allocate ( const struct device * dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t bar_size, uintptr_t * bar_bus_addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/pcie/controller.h>
```

为端点基地址寄存器（BAR）分配内存区域子集（Memory Region Subset）。

枚举 PCIe 端点（Endpoints）时，Type 0 端点可通过 I/O 类型或内存类型的基址寄存器（BARs）请求最多 6 个内存区域。

若 PCI Express 控制器存在相应内存区域且仍有可用空间，此调用就在这些区域中分配所需区域。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PCI Express 控制器设备指针（Controller Device Pointer）。 |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `mem` | 基址寄存器（BAR）为内存类型时为 `true`。 |
| `mem64` | 基址寄存器（BAR）为 64 位内存类型时为 `true`。 |
| `bar_size` | 硬件返回的基址寄存器（BAR）所需区域大小，单位为字节。 |
| `bar_bus_addr` | 已分配、用于写入 BAR 寄存器的总线侧地址（Bus-centric Address）。 |

**返回（Returns）**：返回值：可以分配时为 `true`，分配失败时为 `false`。

<a id="gae7c109ca138adfd906fef5b6f3dca385"></a>

### `pcie_ctrl_region_get_allocate_base()`

```c
bool pcie_ctrl_region_get_allocate_base ( const struct device * dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t align, uintptr_t * bar_base_addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/pcie/controller.h>
```

获取为端点基地址寄存器（BAR）分配的内存区域子集当前分配基地址（Allocation Base）时调用的函数。

枚举 PCIe 端点（Endpoints）时，Type 1 桥接端点需要一个覆盖桥后总线全部端点所分配内存的地址范围（Memory Range）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PCI Express 控制器设备指针（Controller Device Pointer）。 |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `mem` | 基址寄存器（BAR）为内存类型时为 `true`。 |
| `mem64` | 基址寄存器（BAR）为 64 位内存类型时为 `true`。 |
| `align` | 对齐（Alignment）时需要考虑的大小。 |
| `bar_base_addr` | 总线侧地址分配基址（Bus-centric Address Allocation Base）。 |

**返回（Returns）**：返回值：可以分配时为 `true`，分配失败时为 `false`。

<a id="gae6fa104ea2cc85912ebb1cfe0a1a3ddf"></a>

### `pcie_ctrl_region_translate()`

```c
bool pcie_ctrl_region_translate ( const struct device * dev, pcie_bdf_t bdf, bool mem, bool mem64, uintptr_t bar_bus_addr, uintptr_t * bar_addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/pcie/controller.h>
```

将端点基地址寄存器（BAR）的总线地址（Bus-centric Address）转换为物理地址（Physical Address）。

枚举 PCIe 端点（Endpoints）时，Type 0 端点可通过 I/O 类型或内存类型的基址寄存器（BARs）请求最多 6 个内存区域。

设置在 BAR 寄存器中的总线侧地址（Bus-centric Address）不一定能由 CPU 直接访问，因此必须使用 PCI Express 控制器的内存区域转换范围（Translation Ranges）进行转换，才能由 CPU 映射。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PCI Express 控制器设备指针（Controller Device Pointer）。 |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `mem` | 基址寄存器（BAR）为内存类型时为 `true`。 |
| `mem64` | 基址寄存器（BAR）为 64 位内存类型时为 `true`。 |
| `bar_bus_addr` | 写入 BAR 寄存器的总线侧地址（Bus-centric Address）。 |
| `bar_addr` | 由总线侧地址转换得到的 CPU 侧地址（CPU-centric Address）。 |

**返回（Returns）**：返回值：可以转换时为 `true`，转换失败时为 `false`。


## 8.7\_原页交叉引用（Cross References）

- [PCIe 控制器驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html)
- [controller.h](../api_file_protocol_service_reference/P013_zephyr__drivers__pcie__controller.h_文件参考.md)
- [pcie_ctrl_config](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md)
- [pcie_ctrl_config.ranges](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a1a59bec03927f2c6b5fd0aed8c36e6b4)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [msi_vector_t](../api_vector_pipeline_topic_reference/P025_PCIe 主机消息信号中断（MSI）接口.md#ga9ede6a7a472ee62f0975256a1b5f1231)
- [DT_RANGES_CHILD_BUS_FLAGS_BY_IDX](../dt_reg_reference/P002_设备树地址范围映射宏.md#ga32a9c873d3ec1f5d7922c38eaafd1af8)
- [DT_RANGES_CHILD_BUS_ADDRESS_BY_IDX](../dt_reg_reference/P002_设备树地址范围映射宏.md#ga449940559213086b15151ec00e46607d)
- [DT_RANGES_PARENT_BUS_ADDRESS_BY_IDX](../dt_reg_reference/P002_设备树地址范围映射宏.md#ga48d493ad616438ace2396c0312a242ba)
- [DT_RANGES_LENGTH_BY_IDX](../dt_reg_reference/P002_设备树地址范围映射宏.md#ga52677a5bc86f9132a09b6bc37153afb2)
- [CONFIG_PCIE_MSI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MSI)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-ranges-prop_html_ga32a9c873d3ec1f5d7922c38eaafd1af8"></a>
<a id="agroup__devicetree-ranges-prop_html_ga449940559213086b15151ec00e46607d"></a>
<a id="agroup__devicetree-ranges-prop_html_ga48d493ad616438ace2396c0312a242ba"></a>
<a id="agroup__devicetree-ranges-prop_html_ga52677a5bc86f9132a09b6bc37153afb2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_网络分组过滤器 API（Network Packet Filter API）.md) · [返回大纲](大纲.md) · [下一章](P009_引脚控制协议（Pin Control Protocol）.md)
