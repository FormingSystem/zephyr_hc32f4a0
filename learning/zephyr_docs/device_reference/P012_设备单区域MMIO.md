---
id: learning.zephyr-docs.device-reference.page-12
title: 设备单区域MMIO
kind: reference
status: maintained
domains: [zephyr, device, mmio, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__device-mmio-single.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_设备单区域MMIO

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__device-mmio-single.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是设备内存映射输入输出（Memory-Mapped Input/Output，MMIO）应用程序接口（Application Programming Interface，API）参考。先读[设备驱动模型](../hardware/P003_设备驱动模型.md)，再按[本册大纲](大纲.md)区分物理地址（Physical Address）、线性地址（Linear Address）及区域元数据（Region Metadata），并比较单区域、命名区域与顶层存储。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

适用于只需管理一个MMIO区域的驱动；这是最常见的情况。

<a id="details"></a>

适用于只需管理一个MMIO区域的驱动；这是最常见的情况。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_ga47e037f86108c8da12d8a9b9a35e6ad5"></a>

```c
#define DEVICE_MMIO_RAM mm_reg_t _mmio
```

相关声明：[DEVICE_MMIO_RAM](#ga47e037f86108c8da12d8a9b9a35e6ad5)、[mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)。

在设备的dev_data结构中声明MMIO信息的存储空间。

<a id="r_ga63f871dc2ec4c89839a1782e86e292bf"></a>

```c
#define DEVICE_MMIO_RAM_PTR(device)
```

相关声明：[DEVICE_MMIO_RAM_PTR](#ga63f871dc2ec4c89839a1782e86e292bf)、[device](P002_设备对象结构.md)。

返回指向设备MMIO地址在RAM中存储位置的指针。

<a id="r_ga1dfb620f6b3c7ee9b2bc54044d0bc875"></a>

```c
#define DEVICE_MMIO_ROM struct z_device_mmio_rom _mmio
```

相关声明：[DEVICE_MMIO_ROM](#ga1dfb620f6b3c7ee9b2bc54044d0bc875)。

在设备的config结构中声明MMIO数据的存储空间。

<a id="r_ga6246f4c8bc1542d8960d3bda99a592e5"></a>

```c
#define DEVICE_MMIO_ROM_PTR(dev)
```

相关声明：[DEVICE_MMIO_ROM_PTR](#ga6246f4c8bc1542d8960d3bda99a592e5)。

返回指向设备MMIO信息在ROM中存储位置的指针。

<a id="r_ga023516c60725f8c6d62110f74af22549"></a>

```c
#define DEVICE_MMIO_ROM_INIT(node_id)
```

相关声明：[DEVICE_MMIO_ROM_INIT](#ga023516c60725f8c6d62110f74af22549)。

初始化DEVICE_MMIO_ROM成员。

<a id="r_ga8e15770c4ec118edbefc1ef95f1ace80"></a>

```c
#define DEVICE_MMIO_MAP(dev, flags)
```

相关声明：[DEVICE_MMIO_MAP](#ga8e15770c4ec118edbefc1ef95f1ace80)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将MMIO内存映射到地址空间（Address Space）。

<a id="r_ga8cb49d87ef6dc3b017d5b68860530b63"></a>

```c
#define DEVICE_MMIO_GET(dev)
```

相关声明：[DEVICE_MMIO_GET](#ga8cb49d87ef6dc3b017d5b68860530b63)。

取得设备的MMIO地址。

## 12.2\_详细说明（Detailed Documentation）

<a id="ga8cb49d87ef6dc3b017d5b68860530b63"></a>

### `DEVICE_MMIO_GET`

```c
#define DEVICE_MMIO_GET ( dev)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
(*DEVICE_MMIO_RAM_PTR(dev))
```

取得设备的MMIO地址。

对多数微控制器，MMIO地址可以是在构建时已知的固定值，因此可将其保存在位于ROM中的device->config中。

但某些设备只能在运行时确定MMIO地址，因为它们需要映射到地址空间、通过PCI枚举（Enumeration）取得地址，或同时需要这两种操作。

此宏返回驱动MMIO区域的线性地址，适用于恰好只有一个MMIO区域的驱动。驱动初始化函数必须已经调用device_map()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备对象。 |

**返回（Returns）**：返回MMIO区域的mm_reg_t类型线性地址。

> 译注——源码核对：GET只读取已保存的地址，不建立映射或检查设备就绪。在无需RAM存储的分支中，它直接取ROM的addr，MAP为空操作；因此原文要求先调用device_map应结合需要运行时映射的配置理解。

<a id="ga8e15770c4ec118edbefc1ef95f1ace80"></a>

### `DEVICE_MMIO_MAP`

```c
#define DEVICE_MMIO_MAP ( dev, flags )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
device_map(DEVICE_MMIO_RAM_PTR(dev), \
           DEVICE_MMIO_ROM_PTR(dev)->phys_addr, \
           DEVICE_MMIO_ROM_PTR(dev)->size, \
           (flags))
```

将MMIO内存映射到地址空间（Address Space）。

本宏不用于PCIe设备；PCIe设备必须在运行时探测，应直接调用device_map()，并使用DEVICE_MMIO_RAM_PTR()作为保存目标虚拟地址的位置。

flags参数目前用于缓存模式，应取DEVICE_CACHE_*宏之一；未使用的位保留供未来扩展。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备对象实例。 |
| `flags` | 缓存模式标志。 |

> 译注——源码核对：原说明中的DEVICE_CACHE_*是命名不一致；本次kernel/mm.h实际定义K_MEM_CACHE_NONE、K_MEM_CACHE_WT和K_MEM_CACHE_WB。RAM分支从ROM取phys_addr／size后调用device_map，不执行PCIe BAR探测；没有ROM信息的PCIe驱动应自行取得BAR信息并直接调用device_map。非RAM分支为空操作。

<a id="ga47e037f86108c8da12d8a9b9a35e6ad5"></a>

### `DEVICE_MMIO_RAM`

```c
#define DEVICE_MMIO_RAM mm_reg_t _mmio
```

```c
#include <zephyr/sys/device_mmio.h>
```

在设备的dev_data结构中声明MMIO信息的存储空间。

DEVICE_MMIO_MAP()和DEVICE_MMIO_GET()宏会访问此存储空间。

根据配置，也可能完全不预留内存。本成员必须是data结构的第一个成员。

如果构建时已知物理地址，config_info中必须有对应的DEVICE_MMIO_ROM；若构建时未知，例如PCIe设备，则可以省略它。

以名为foo的驱动为例：

原始示例（Example）：

```c
struct foo_driver_data {
     DEVICE_MMIO_RAM;
     int wibble;
     ...
}
```

无需在构建时初始化此内存；初始化函数中的DEVICE_MMIO_MAP()会设置它。

可通过DEVICE_MMIO_RAM_PTR()取得指向此内存的指针。

> 译注——源码核对：需要RAM地址存储时展开为mm_reg_t _mmio，否则展开为空。单区域接口通过dev->data起始位置直接转换指针，所以必须放在运行数据结构首成员；这不是普通命名区域的布局要求。

<a id="ga63f871dc2ec4c89839a1782e86e292bf"></a>

### `DEVICE_MMIO_RAM_PTR`

```c
#define DEVICE_MMIO_RAM_PTR ( device)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
(mm_reg_t *)((device)->data)
```

返回指向设备MMIO地址在RAM中存储位置的指针。

直接使用device_map()时，可用此结果指定目标MMIO地址的保存位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `device` | 设备node_id对象。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `mm_reg_t` | 指向存储位置的指针。 |

> 译注——源码核对：原参数说明称device为node_id对象，但宏实际访问(device)->data，输入应为struct device指针而非设备树节点标识符。原返回值表写mm_reg_t，宏实际结果为mm_reg_t *；它指向保存地址的RAM位置，而不是直接返回外设地址。此宏只在DEVICE_MMIO_IS_IN_RAM下定义。

<a id="ga1dfb620f6b3c7ee9b2bc54044d0bc875"></a>

### `DEVICE_MMIO_ROM`

```c
#define DEVICE_MMIO_ROM struct z_device_mmio_rom _mmio
```

```c
#include <zephyr/sys/device_mmio.h>
```

在设备的config结构中声明MMIO数据的存储空间。

DEVICE_MMIO_MAP()和DEVICE_MMIO_GET()宏会访问此存储空间。

这里保存的内容随配置有较大差异。本成员必须是config结构的第一个成员，data中必须有对应的DEVICE_MMIO_RAM。

PCIe设备不使用此存储空间，可以将其省略。

应在构建时使用DEVICE_MMIO_ROM_INIT()，根据设备树源码（Devicetree Source，DTS）中的信息初始化它。

可通过DEVICE_MMIO_ROM_PTR()取得指向此内存的指针。

以名为foo的驱动为例：

原始示例（Example）：

```c
struct foo_config {
     DEVICE_MMIO_ROM;
     int baz;
     ...
}
```

**参阅（See Also）**：另请参阅DEVICE_MMIO_ROM_INIT()。

> 译注——源码核对：展开为struct z_device_mmio_rom _mmio。其布局依配置为phys_addr加size，或只有线性addr；单区域辅助宏把dev->config起始位置转换成该类型，所以必须放在配置结构首成员。原示例含省略号且结构末尾缺少分号，是展示布局的片段，不能整段原样编译。

<a id="ga023516c60725f8c6d62110f74af22549"></a>

### `DEVICE_MMIO_ROM_INIT`

```c
#define DEVICE_MMIO_ROM_INIT ( node_id)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
._mmio = Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)
```

初始化DEVICE_MMIO_ROM成员。

使用DTS信息，在设备config结构的一个具体实例中初始化MMIO相关信息。

以属于foo子系统的驱动为例：

原始示例（Example）：

```c
struct foo_config my_config = {
     DEVICE_MMIO_ROM_INIT(DT_DRV_INST(...)),
     .baz = 2;
     ...
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | DTS节点标识符node_id。 |

**参阅（See Also）**：另请参阅DEVICE_MMIO_ROM()。

> 译注——源码核对：该宏是结构初始化器中的指定成员片段。原示例包含省略号、初始化列表内的分号和缺少末尾分号等简写，保留以反映官网内容；实际C初始化列表需要逗号分隔成员并补齐完整声明。

<a id="ga6246f4c8bc1542d8960d3bda99a592e5"></a>

### `DEVICE_MMIO_ROM_PTR`

```c
#define DEVICE_MMIO_ROM_PTR ( dev)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
((struct z_device_mmio_rom *)((dev)->config))
```

返回指向设备MMIO信息在ROM中存储位置的指针。

如果config结构声明中省略了ROM存储成员，此宏将无法正常工作，此时不得使用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例对象。 |

**返回（Returns）**：返回指向存储位置的struct device_mmio_rom *指针。

> 译注——源码核对：原返回说明写struct device_mmio_rom *，实际类型为struct z_device_mmio_rom *。它只是对config起始地址进行转换，不证明该区域可写；config一般指向常量配置，不能据转换后的类型擅自修改ROM。

## 12.3\_源码定位与版本边界

MMIO布局和宏展开可在仓库的[device_mmio.h](../../../include/zephyr/sys/device_mmio.h)相对定位；缓存／权限标志见[kernel/mm.h](../../../include/zephyr/kernel/mm.h)，外部地址查询接口见[system_mm.h](../../../include/zephyr/drivers/mm/system_mm.h)。本批核对[官方MMIO头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/device_mmio.h)、[官方内存管理头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel/mm.h)和[官方系统内存驱动接口](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/mm/system_mm.h)，摘要见[来源记录](../SOURCES.md)。本地源码、main和latest网页不能自动视为同一版本。

> 译注——示例完整性：原页结构体与配置示例保留省略号及原始标点；它们用于说明布局和初始化器位置，不是可直接复制编译的完整源文件。命名区域在取得DEV_DATA／DEV_CFG正确类型后按成员访问，单区域宏则依赖首成员布局。

本批只做官方文档翻译与源码核对，没有运行地址映射、访问设备寄存器、构建固件或进行实板实验。

## 12.4\_原页交叉引用（Cross References）

- [mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [device](P002_设备对象结构.md)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/sys/device_mmio.h](P015_设备MMIO头文件参考.md)
- [device_map()](P011_设备MMIO管理概述.md#ga6b4a9841a5176104e1b63f7475d3d2a2)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device-mmio-single_html_ga63f871dc2ec4c89839a1782e86e292bf"></a>
<a id="agroup__device-mmio-single_html_ga6246f4c8bc1542d8960d3bda99a592e5"></a>
<a id="agroup__device-mmio_html_ga6b4a9841a5176104e1b63f7475d3d2a2"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="agroup__device-mmio-single_html_ga47e037f86108c8da12d8a9b9a35e6ad5"></a>
<a id="agroup__sys__io__apis_html_ga7bcfa789a44940bccc5b9b98642744b0"></a>
<a id="astructdevice_html"></a>
<a id="agroup__device-mmio-single_html_ga1dfb620f6b3c7ee9b2bc54044d0bc875"></a>
<a id="agroup__device-mmio-single_html_ga023516c60725f8c6d62110f74af22549"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>

---

[上一章](P011_设备MMIO管理概述.md) · [返回大纲](大纲.md) · [下一章](P013_设备命名区域MMIO.md)
