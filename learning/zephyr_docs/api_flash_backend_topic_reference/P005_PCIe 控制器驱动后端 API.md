---
id: learning.zephyr-docs.api-flash-backend-topic-reference.page-5
title: PCIe 控制器驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_PCIe 控制器驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

此组包含实现 PCIe 控制器驱动（Controller Driver）所需的 API 类型定义、回调签名（Callback Signatures）及其他辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_pcie_5Fctrl_5Fdriver_5Fapi"></a>

```c
struct pcie_ctrl_driver_api
```

相关声明：[pcie_ctrl_driver_api](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md)。

驱动操作（Driver Operations）：PCIe控制器（Controller）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.2\_类型定义（Typedefs）

<a id="r_gac3d0f7e90bcc30996ce23324d2d7356a"></a>

```c
typedef uint32_t(* pcie_ctrl_conf_read_t) (const struct device *dev, pcie_bdf_t bdf, unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_ctrl_conf_read_t](#gac3d0f7e90bcc30996ce23324d2d7356a)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

从端点配置空间（Endpoint Configuration Space）读取 32 位字（Word）时调用的函数。

<a id="r_ga3241acc7de4af2b73cf3f47a25349109"></a>

```c
typedef void(* pcie_ctrl_conf_write_t) (const struct device *dev, pcie_bdf_t bdf, unsigned int reg, uint32_t data)
```

相关声明：[pcie_ctrl_conf_write_t](#ga3241acc7de4af2b73cf3f47a25349109)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向端点配置空间（Endpoint Configuration Space）写入 32 位字（Word）时调用的函数。

<a id="r_ga62ce18e7495256c148168b773eabd37d"></a>

```c
typedef bool(* pcie_ctrl_region_allocate_t) (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t bar_size, uintptr_t *bar_bus_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_allocate_t](#ga62ce18e7495256c148168b773eabd37d)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

为端点基地址寄存器（Base Address Register，BAR）分配内存区域子集（Memory Region Subset）时调用的函数。

<a id="r_gaa9d5bd27c841e36f65e65dec0b057e9a"></a>

```c
typedef bool(* pcie_ctrl_region_get_allocate_base_t) (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t align, uintptr_t *bar_base_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_get_allocate_base_t](#gaa9d5bd27c841e36f65e65dec0b057e9a)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

获取为端点基地址寄存器（BAR）分配的内存区域子集当前分配基地址（Allocation Base）时调用的函数。

<a id="r_gab144356b1c3ec3754aae0008634f2d2f"></a>

```c
typedef bool(* pcie_ctrl_region_translate_t) (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, uintptr_t bar_bus_addr, uintptr_t *bar_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_translate_t](#gab144356b1c3ec3754aae0008634f2d2f)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

将端点基地址寄存器（BAR）的总线地址（Bus-centric Address）转换为物理地址（Physical Address）时调用的函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_gaa16b59c39f273a654b72d9e209f3ba2e"></a>

```c
uint32_t pcie_generic_ctrl_conf_read (mm_reg_t cfg_addr, pcie_bdf_t bdf, unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_generic_ctrl_conf_read](#gaa16b59c39f273a654b72d9e209f3ba2e)、[mm_reg_t](../device_reference/P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

从内存映射端点（Memory-mapped Endpoint）的配置空间读取 32 位字（Word）。

<a id="r_ga709ecedbd0585b4eb17fc2f5923a8f61"></a>

```c
void pcie_generic_ctrl_conf_write (mm_reg_t cfg_addr, pcie_bdf_t bdf, unsigned int reg, uint32_t data)
```

相关声明：[pcie_generic_ctrl_conf_write](#ga709ecedbd0585b4eb17fc2f5923a8f61)、[mm_reg_t](../device_reference/P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向内存映射端点（Memory-mapped Endpoint）的配置空间写入 32 位字（Word）。

<a id="r_ga75910ea4255a740b57e35a596a90b7bb"></a>

```c
void pcie_generic_ctrl_enumerate (const struct device *dev, pcie_bdf_t bdf_start)
```

相关声明：[pcie_generic_ctrl_enumerate](#ga75910ea4255a740b57e35a596a90b7bb)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

开始 PCIe 端点枚举（Endpoints Enumeration）。

## 5.4\_详细说明（Detailed Documentation）

<a id="gac3d0f7e90bcc30996ce23324d2d7356a"></a>

### `pcie_ctrl_conf_read_t`

```c
typedef uint32_t(* pcie_ctrl_conf_read_t) (const struct device *dev, pcie_bdf_t bdf, unsigned int reg)
```

```c
#include <zephyr/drivers/pcie/controller.h>
```

从端点配置空间（Endpoint Configuration Space）读取 32 位字（Word）时调用的函数。

使用 PCI Express 控制器配置空间访问方式（Configuration Space Access Method），从端点配置空间读取一个 32 位字（Word）。访问方式可以是 I/O 端口、内存映射或自定义方法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PCI Express 控制器设备指针（Controller Device Pointer）。 |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `reg` | 配置字索引（Configuration Word Index），不是地址。 |

**返回（Returns）**：返回值：读出的字（Word）；端点或该字不存在时为 `0xFFFFFFFFU`。

<a id="ga3241acc7de4af2b73cf3f47a25349109"></a>

### `pcie_ctrl_conf_write_t`

```c
typedef void(* pcie_ctrl_conf_write_t) (const struct device *dev, pcie_bdf_t bdf, unsigned int reg, uint32_t data)
```

```c
#include <zephyr/drivers/pcie/controller.h>
```

向端点配置空间（Endpoint Configuration Space）写入 32 位字（Word）时调用的函数。

使用 PCI Express 控制器配置空间访问方式（Configuration Space Access Method），向端点配置空间写入一个 32 位字（Word）。访问方式可以是 I/O 端口、内存映射或自定义方法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PCI Express 控制器设备指针（Controller Device Pointer）。 |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `reg` | 配置字索引（Configuration Word Index），不是地址。 |
| `data` | 要写入的值（Value）。 |

<a id="ga62ce18e7495256c148168b773eabd37d"></a>

### `pcie_ctrl_region_allocate_t`

```c
typedef bool(* pcie_ctrl_region_allocate_t) (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t bar_size, uintptr_t *bar_bus_addr)
```

```c
#include <zephyr/drivers/pcie/controller.h>
```

为端点基地址寄存器（Base Address Register，BAR）分配内存区域子集（Memory Region Subset）时调用的函数。

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

<a id="gaa9d5bd27c841e36f65e65dec0b057e9a"></a>

### `pcie_ctrl_region_get_allocate_base_t`

```c
typedef bool(* pcie_ctrl_region_get_allocate_base_t) (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t align, uintptr_t *bar_base_addr)
```

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

<a id="gab144356b1c3ec3754aae0008634f2d2f"></a>

### `pcie_ctrl_region_translate_t`

```c
typedef bool(* pcie_ctrl_region_translate_t) (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, uintptr_t bar_bus_addr, uintptr_t *bar_addr)
```

```c
#include <zephyr/drivers/pcie/controller.h>
```

将端点基地址寄存器（BAR）的总线地址（Bus-centric Address）转换为物理地址（Physical Address）时调用的函数。

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

<a id="gaa16b59c39f273a654b72d9e209f3ba2e"></a>

### `pcie_generic_ctrl_conf_read()`

```c
uint32_t pcie_generic_ctrl_conf_read ( mm_reg_t cfg_addr, pcie_bdf_t bdf, unsigned int reg )
```

```c
#include <zephyr/drivers/pcie/controller.h>
```

从内存映射端点（Memory-mapped Endpoint）的配置空间读取 32 位字（Word）。

使用内存映射配置空间访问方式（Memory-Mapped Configuration Space Access Method），从端点配置空间读取一个 32 位字。此方式称为 PCI 控制访问方法（CAM）或 PCIe 扩展控制访问方法（ECAM）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cfg_addr` | 内存映射配置空间（Memory-Mapped Configuration Space）的逻辑地址。 |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `reg` | 配置字索引（Configuration Word Index），不是地址。 |

**返回（Returns）**：返回值：读出的字（Word）；端点或该字不存在时为 `0xFFFFFFFFU`。

<a id="ga709ecedbd0585b4eb17fc2f5923a8f61"></a>

### `pcie_generic_ctrl_conf_write()`

```c
void pcie_generic_ctrl_conf_write ( mm_reg_t cfg_addr, pcie_bdf_t bdf, unsigned int reg, uint32_t data )
```

```c
#include <zephyr/drivers/pcie/controller.h>
```

向内存映射端点（Memory-mapped Endpoint）的配置空间写入 32 位字（Word）。

使用内存映射配置空间访问方式（Memory-Mapped Configuration Space Access Method），向端点配置空间写入一个 32 位字。此方式称为 PCI 控制访问方法（CAM）或 PCIe 扩展控制访问方法（ECAM）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cfg_addr` | 内存映射配置空间（Memory-Mapped Configuration Space）的逻辑地址。 |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `reg` | 配置字索引（Configuration Word Index），不是地址。 |
| `data` | 要写入的值（Value）。 |

<a id="ga75910ea4255a740b57e35a596a90b7bb"></a>

### `pcie_generic_ctrl_enumerate()`

```c
void pcie_generic_ctrl_enumerate ( const struct device * dev, pcie_bdf_t bdf_start )
```

```c
#include <zephyr/drivers/pcie/controller.h>
```

开始 PCIe 端点枚举（Endpoints Enumeration）。

从指定总线编号开始枚举 PCIe 端点（Endpoint Enumeration）。在非 x86 架构上，或固件未设置 PCIe 总线层级（Bus Hierarchy）时，必须枚举 PCIe 总线系统，以配置端点的基址寄存器（BARs）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PCI Express 控制器设备指针（Controller Device Pointer）。 |
| `bdf_start` | PCI(e) 起始端点（Start Endpoint），开始枚举时仅使用 `bus` 和 `dev`。 |


## 5.5\_原页交叉引用（Cross References）

- [pcie_ctrl_driver_api](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [mm_reg_t](../device_reference/P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [zephyr/drivers/pcie/controller.h](../api_file_protocol_service_reference/P013_zephyr__drivers__pcie__controller.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_以太网过滤条件（Ethernet Filter Conditions）.md) · [返回大纲](大纲.md) · [下一章](P006_时钟协议（Clock Protocol）.md)
