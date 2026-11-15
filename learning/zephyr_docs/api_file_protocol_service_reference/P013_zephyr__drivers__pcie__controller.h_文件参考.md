---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-13
title: zephyr__drivers__pcie__controller.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2controller_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_drivers\_\_pcie\_\_controller.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2controller_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe控制器（Controllers）驱动的公共API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/drivers/pcie/pcie.h>
```

查看此文件的源码。

PCIe控制器（Controllers）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_pcie_5Fctrl_5Fdriver_5Fapi"></a>

```c
struct pcie_ctrl_driver_api
```

相关声明：[pcie_ctrl_driver_api](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md)。

驱动操作（Driver Operations）：PCIe控制器（Controller）驱动操作。

<a id="r_pcie_5Fctrl_5Fconfig"></a>

```c
struct pcie_ctrl_config
```

相关声明：[pcie_ctrl_config](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md)。

描述支持PCI Express控制器API（Controller API）的设备的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.2\_宏定义（Macros）

<a id="r_ga91525130b94b07187633abd1e017aa61"></a>

```c
#define PCIE_RANGE_FORMAT(node_id, idx)
```

相关声明：[PCIE_RANGE_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga91525130b94b07187633abd1e017aa61)。

根据设备树（Devicetree）填充 `pcie_ctrl_config.ranges` 表条目。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 13.3\_类型定义（Typedefs）

<a id="r_gac3d0f7e90bcc30996ce23324d2d7356a"></a>

```c
typedef uint32_t(* pcie_ctrl_conf_read_t) (const struct device *dev, pcie_bdf_t bdf, unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_ctrl_conf_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gac3d0f7e90bcc30996ce23324d2d7356a)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

从端点配置空间（Endpoint Configuration Space）读取 32 位字（Word）时调用的函数。

<a id="r_ga3241acc7de4af2b73cf3f47a25349109"></a>

```c
typedef void(* pcie_ctrl_conf_write_t) (const struct device *dev, pcie_bdf_t bdf, unsigned int reg, uint32_t data)
```

相关声明：[pcie_ctrl_conf_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga3241acc7de4af2b73cf3f47a25349109)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向端点配置空间（Endpoint Configuration Space）写入 32 位字（Word）时调用的函数。

<a id="r_ga62ce18e7495256c148168b773eabd37d"></a>

```c
typedef bool(* pcie_ctrl_region_allocate_t) (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t bar_size, uintptr_t *bar_bus_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_allocate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga62ce18e7495256c148168b773eabd37d)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

为端点基地址寄存器（Base Address Register，BAR）分配内存区域子集（Memory Region Subset）时调用的函数。

<a id="r_gaa9d5bd27c841e36f65e65dec0b057e9a"></a>

```c
typedef bool(* pcie_ctrl_region_get_allocate_base_t) (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t align, uintptr_t *bar_base_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_get_allocate_base_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gaa9d5bd27c841e36f65e65dec0b057e9a)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

获取为端点基地址寄存器（BAR）分配的内存区域子集当前分配基地址（Allocation Base）时调用的函数。

<a id="r_gab144356b1c3ec3754aae0008634f2d2f"></a>

```c
typedef bool(* pcie_ctrl_region_translate_t) (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, uintptr_t bar_bus_addr, uintptr_t *bar_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_translate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gab144356b1c3ec3754aae0008634f2d2f)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

将端点基地址寄存器（BAR）的总线地址（Bus-centric Address）转换为物理地址（Physical Address）时调用的函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_gaa16b59c39f273a654b72d9e209f3ba2e"></a>

```c
uint32_t pcie_generic_ctrl_conf_read (mm_reg_t cfg_addr, pcie_bdf_t bdf, unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_generic_ctrl_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gaa16b59c39f273a654b72d9e209f3ba2e)、[mm_reg_t](../device_reference/P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

从内存映射端点（Memory-mapped Endpoint）的配置空间读取 32 位字（Word）。

<a id="r_ga709ecedbd0585b4eb17fc2f5923a8f61"></a>

```c
void pcie_generic_ctrl_conf_write (mm_reg_t cfg_addr, pcie_bdf_t bdf, unsigned int reg, uint32_t data)
```

相关声明：[pcie_generic_ctrl_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga709ecedbd0585b4eb17fc2f5923a8f61)、[mm_reg_t](../device_reference/P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向内存映射端点（Memory-mapped Endpoint）的配置空间写入 32 位字（Word）。

<a id="r_ga75910ea4255a740b57e35a596a90b7bb"></a>

```c
void pcie_generic_ctrl_enumerate (const struct device *dev, pcie_bdf_t bdf_start)
```

相关声明：[pcie_generic_ctrl_enumerate](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga75910ea4255a740b57e35a596a90b7bb)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

开始 PCIe 端点枚举（Endpoints Enumeration）。

<a id="r_ga1d978b8075191d6e571349684c731a43"></a>

```c
static uint32_t pcie_ctrl_conf_read (const struct device *dev, pcie_bdf_t bdf, unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_ctrl_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga1d978b8075191d6e571349684c731a43)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

从端点配置空间（Endpoint Configuration Space）读取 32 位字（Word）。

<a id="r_ga5cfe01762e5af8dc0cc5fbd550ff7e74"></a>

```c
static void pcie_ctrl_conf_write (const struct device *dev, pcie_bdf_t bdf, unsigned int reg, uint32_t data)
```

相关声明：[pcie_ctrl_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga5cfe01762e5af8dc0cc5fbd550ff7e74)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向端点配置空间（Endpoint Configuration Space）写入 32 位字（Word）。

<a id="r_ga1de030e2e8b07509d75de5a348297f42"></a>

```c
static bool pcie_ctrl_region_allocate (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t bar_size, uintptr_t *bar_bus_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_allocate](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga1de030e2e8b07509d75de5a348297f42)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

为端点基地址寄存器（BAR）分配内存区域子集（Memory Region Subset）。

<a id="r_gae7c109ca138adfd906fef5b6f3dca385"></a>

```c
static bool pcie_ctrl_region_get_allocate_base (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, size_t align, uintptr_t *bar_base_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_get_allocate_base](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#gae7c109ca138adfd906fef5b6f3dca385)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

获取为端点基地址寄存器（BAR）分配的内存区域子集当前分配基地址（Allocation Base）时调用的函数。

<a id="r_gae6fa104ea2cc85912ebb1cfe0a1a3ddf"></a>

```c
static bool pcie_ctrl_region_translate (const struct device *dev, pcie_bdf_t bdf, bool mem, bool mem64, uintptr_t bar_bus_addr, uintptr_t *bar_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ctrl_region_translate](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#gae6fa104ea2cc85912ebb1cfe0a1a3ddf)、[device](../device_reference/P002_设备对象结构.md)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

将端点基地址寄存器（BAR）的总线地址（Bus-centric Address）转换为物理地址（Physical Address）。

<a id="r_ga69493e7da12c4c2d95f506ecf86e7dfe"></a>

```c
static uint8_t pcie_ctrl_msi_device_setup (const struct device *dev, unsigned int priority, msi_vector_t *vectors, uint8_t n_vector)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pcie_ctrl_msi_device_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga69493e7da12c4c2d95f506ecf86e7dfe)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[msi_vector_t](../api_vector_pipeline_topic_reference/P025_PCIe 主机消息信号中断（MSI）接口.md#ga9ede6a7a472ee62f0975256a1b5f1231)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

配置给定 PCI 端点（Endpoint），使其生成消息信号中断（Message Signaled Interrupts，MSIs）。


## 13.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/pcie/pcie.h](../api_source_pcie_hid_reference/P001_pcie.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P169_controller.h_源码浏览.md)
- [pcie_ctrl_driver_api](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md)
- [pcie_ctrl_config](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md)
- [PCIE_RANGE_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga91525130b94b07187633abd1e017aa61)
- [pcie_ctrl_config.ranges](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a1a59bec03927f2c6b5fd0aed8c36e6b4)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pcie_ctrl_conf_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gac3d0f7e90bcc30996ce23324d2d7356a)
- [device](../device_reference/P002_设备对象结构.md)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [pcie_ctrl_conf_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga3241acc7de4af2b73cf3f47a25349109)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [pcie_ctrl_region_allocate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga62ce18e7495256c148168b773eabd37d)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [pcie_ctrl_region_get_allocate_base_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gaa9d5bd27c841e36f65e65dec0b057e9a)
- [pcie_ctrl_region_translate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gab144356b1c3ec3754aae0008634f2d2f)
- [pcie_generic_ctrl_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gaa16b59c39f273a654b72d9e209f3ba2e)
- [mm_reg_t](../device_reference/P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [pcie_generic_ctrl_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga709ecedbd0585b4eb17fc2f5923a8f61)
- [pcie_generic_ctrl_enumerate](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga75910ea4255a740b57e35a596a90b7bb)
- [pcie_ctrl_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga1d978b8075191d6e571349684c731a43)
- [pcie_ctrl_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga5cfe01762e5af8dc0cc5fbd550ff7e74)
- [pcie_ctrl_region_allocate](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga1de030e2e8b07509d75de5a348297f42)
- [pcie_ctrl_region_get_allocate_base](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#gae7c109ca138adfd906fef5b6f3dca385)
- [pcie_ctrl_region_translate](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#gae6fa104ea2cc85912ebb1cfe0a1a3ddf)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pcie_ctrl_msi_device_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga69493e7da12c4c2d95f506ecf86e7dfe)
- [msi_vector_t](../api_vector_pipeline_topic_reference/P025_PCIe 主机消息信号中断（MSI）接口.md#ga9ede6a7a472ee62f0975256a1b5f1231)

<a id="header-details"></a>

---

[上一章](P012_zephyr__drivers__mspi__devicetree.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__mgmt__fota_http.h_文件参考.md)
