---
id: learning.zephyr-docs.device-reference.page-11
title: 设备MMIO管理概述
kind: reference
status: maintained
domains: [zephyr, device, mmio, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__device-mmio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_设备MMIO管理概述

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__device-mmio.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是设备内存映射输入输出（Memory-Mapped Input/Output，MMIO）应用程序接口（Application Programming Interface，API）参考。先读[设备驱动模型](../hardware/P003_设备驱动模型.md)，再按[本册大纲](大纲.md)区分物理地址（Physical Address）、线性地址（Linear Address）及区域元数据（Region Metadata），并比较单区域、命名区域与顶层存储。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

用于在RAM或ROM中适当管理驱动内存映射输入输出（Memory-Mapped Input/Output，MMIO）区域的定义与辅助宏。

<a id="details"></a>

用于在RAM或ROM中适当管理驱动内存映射输入输出（Memory-Mapped Input/Output，MMIO）区域的定义与辅助宏。多数驱动只需包含device.h；但架构层驱动代码使用DEVICE_MMIO_TOPLEVEL系列宏时，可能需要单独包含本头文件，因为主device.h依赖kernel.h，包含它可能造成头文件依赖循环（Header Dependency Cycle）。

<a id="header-groups"></a>
<a id="groups"></a>

## 11.1\_主题（Topics）

<a id="r_device-mmio-named"></a>

相关声明：[命名MMIO区域宏（Named Regions）](P013_设备命名区域MMIO.md)。

适用于需要管理多个MMIO区域，并按名称引用各区域的驱动。

<a id="r_device-mmio-single"></a>

相关声明：[单个MMIO区域宏（Single Region）](P012_设备单区域MMIO.md)。

适用于只需管理一个MMIO区域的驱动；这是最常见的情况。

<a id="r_device-mmio-toplevel"></a>

相关声明：[顶层MMIO区域宏（Top-Level Regions）](P014_顶层MMIO区域.md)。

适用于不使用Zephyr驱动模型、也不将struct device与驱动实例关联的驱动。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_gabdae30483b01d470c357571e088dc51a"></a>

```c
#define DEVICE_MMIO_IS_IN_RAM
```

相关声明：[DEVICE_MMIO_IS_IN_RAM](#gabdae30483b01d470c357571e088dc51a)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.3\_函数（Functions）

<a id="r_ga6b4a9841a5176104e1b63f7475d3d2a2"></a>

```c
static __boot_func void device_map (mm_reg_t *virt_addr, uintptr_t phys_addr, size_t size, uint32_t flags)
```

相关声明：[device_map](#ga6b4a9841a5176104e1b63f7475d3d2a2)、[mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)、[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

设置用于设备MMIO访问的线性地址（Linear Address）。

<a id="r_ga16070be695cec4ebc01915a3dbc1adf8"></a>

```c
static __boot_func void device_unmap (mm_reg_t virt_addr, size_t size)
```

相关声明：[device_unmap](#ga16070be695cec4ebc01915a3dbc1adf8)、[mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)。

撤销用于设备MMIO访问的线性地址。

## 11.4\_详细说明（Detailed Documentation）

<a id="gabdae30483b01d470c357571e088dc51a"></a>

### `DEVICE_MMIO_IS_IN_RAM`

```c
#define DEVICE_MMIO_IS_IN_RAM
```

```c
#include <zephyr/sys/device_mmio.h>
```

> 译注——源码核对：当前头文件在CONFIG_MMU、CONFIG_PCIE或CONFIG_EXTERNAL_ADDRESS_TRANSLATION任一启用时定义该宏，不只考虑MMU／PCIe。它是全系统配置选择，而不是对某个设备是否属于PCIe的运行时判断；所需RAM用于保存可访问地址，不是把外设寄存器内容复制到RAM。

<a id="ga6b4a9841a5176104e1b63f7475d3d2a2"></a>

### `device_map()`

```c
__boot_func void device_map ( mm_reg_t * virt_addr, uintptr_t phys_addr, size_t size, uint32_t flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/device_mmio.h>
```

设置用于设备MMIO访问的线性地址（Linear Address）。

此函数将virt_addr参数所指向的位置设为该MMIO区域正确的线性地址。

启用内存管理单元（Memory Management Unit，MMU）时，可能会在页表（Page Table）中创建映射。

通常只需为flags参数设置缓存模式（Caching Mode）。映射得到的线性地址允许监督者模式（Supervisor Mode）读写访问。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] virt_addr` | 保存输出线性地址的位置；多数用户应使用某个DEVICE_MMIO_RAM_PTR()的结果。 |
| `[in] phys_addr` | MMIO区域的物理基地址（Physical Base Address）。 |
| `[in] size` | MMIO区域大小。 |
| `[in] flags` | 缓存模式及访问标志，参见K_MEM_CACHE_*和K_MEM_PERM_*宏。 |

**参阅（See Also）**：另请参阅k_map()。

> 译注——源码核对：当前MMU分支调用k_mem_map_phys_bare，并在传入flags上增加K_MEM_PERM_RW；CONFIG_KERNEL_DIRECT_MAP启用时还增加K_MEM_DIRECT_MAP。它不会主动清除调用方传入的K_MEM_PERM_USER。无MMU时，外部地址转换分支调用sys_mm_drv_page_phys_get，否则直接赋值。该函数返回void，不向调用方提供成功／失败状态；原文参阅k_map()，而本快照的实际调用名称是k_mem_map_phys_bare。

<a id="ga16070be695cec4ebc01915a3dbc1adf8"></a>

### `device_unmap()`

```c
__boot_func void device_unmap ( mm_reg_t virt_addr, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/device_mmio.h>
```

撤销用于设备MMIO访问的线性地址。

启用MMU时，可以从页表中移除映射。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `virt_addr` | 由device_map取得的线性地址。 |
| `size` | MMIO区域大小。 |

> 译注——源码核对：当前仅CONFIG_MMU分支调用k_mem_unmap_phys_bare；其他分支为空操作。参数按值传递，因此即使移除页表映射，也不会把调用者RAM中保存的地址清零，更不会自动停止外设或释放其其他资源。

## 11.5\_源码定位与版本边界

MMIO布局和宏展开可在仓库的[device_mmio.h](../../../include/zephyr/sys/device_mmio.h)相对定位；缓存／权限标志见[kernel/mm.h](../../../include/zephyr/kernel/mm.h)，外部地址查询接口见[system_mm.h](../../../include/zephyr/drivers/mm/system_mm.h)。本批核对[官方MMIO头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/device_mmio.h)、[官方内存管理头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel/mm.h)和[官方系统内存驱动接口](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/mm/system_mm.h)，摘要见[来源记录](../SOURCES.md)。本地源码、main和latest网页不能自动视为同一版本。

> 译注——外部地址转换：当前无MMU且启用CONFIG_EXTERNAL_ADDRESS_TRANSLATION时，device_map把名为phys_addr的参数传给sys_mm_drv_page_phys_get的virt参数，并将输出写入virt_addr位置，且不检查该函数返回值。system_mm.h将这个接口定义为查询已映射虚拟页对应的物理地址，并要求页对齐。这里如实记录两个接口的当前命名与方向差异；不能仅按device_map参数名推断该分支一定在建立物理到虚拟的新映射，须结合所用版本和目标系统内存驱动核对。

本批只做官方文档翻译与源码核对，没有运行地址映射、访问设备寄存器、构建固件或进行实板实验。

## 11.6\_原页交叉引用（Cross References）

- [命名MMIO区域宏（Named Regions）](P013_设备命名区域MMIO.md)
- [单个MMIO区域宏（Single Region）](P012_设备单区域MMIO.md)
- [顶层MMIO区域宏（Top-Level Regions）](P014_顶层MMIO区域.md)
- [mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/sys/device_mmio.h](P015_设备MMIO头文件参考.md)
- [DEVICE_MMIO_RAM_PTR()](P012_设备单区域MMIO.md#ga63f871dc2ec4c89839a1782e86e292bf)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_系统初始化头文件源码.md) · [返回大纲](大纲.md) · [下一章](P012_设备单区域MMIO.md)
