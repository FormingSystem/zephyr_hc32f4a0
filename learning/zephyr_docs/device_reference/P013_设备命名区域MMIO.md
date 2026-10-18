---
id: learning.zephyr-docs.device-reference.page-13
title: 设备命名区域MMIO
kind: reference
status: maintained
domains: [zephyr, device, mmio, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__device-mmio-named.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_设备命名区域MMIO

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__device-mmio-named.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是设备内存映射输入输出（Memory-Mapped Input/Output，MMIO）应用程序接口（Application Programming Interface，API）参考。先读[设备驱动模型](../hardware/P003_设备驱动模型.md)，再按[本册大纲](大纲.md)区分物理地址（Physical Address）、线性地址（Linear Address）及区域元数据（Region Metadata），并比较单区域、命名区域与顶层存储。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

适用于需要管理多个MMIO区域，并按名称引用各区域的驱动。

<a id="details"></a>

适用于需要管理多个MMIO区域，并按名称引用各区域的驱动。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="r_ga92b6570b0f7bd370bbdfbc4e474151e4"></a>

```c
#define DEVICE_MMIO_NAMED_RAM(name)
```

相关声明：[DEVICE_MMIO_NAMED_RAM](#ga92b6570b0f7bd370bbdfbc4e474151e4)。

在设备的dev_data结构中声明MMIO数据的存储空间。

<a id="r_ga42737f178f205bd90d4e523ae5d67a09"></a>

```c
#define DEVICE_MMIO_NAMED_RAM_PTR(dev, name)
```

相关声明：[DEVICE_MMIO_NAMED_RAM_PTR](#ga42737f178f205bd90d4e523ae5d67a09)。

返回指向设备命名MMIO地址在RAM中存储位置的指针。

<a id="r_gae3ad012160f657451a3f47487510bffb"></a>

```c
#define DEVICE_MMIO_NAMED_ROM(name)
```

相关声明：[DEVICE_MMIO_NAMED_ROM](#gae3ad012160f657451a3f47487510bffb)。

在设备的config结构中声明MMIO数据的存储空间。

<a id="r_ga7f018db0d820b72a782759a4b674de94"></a>

```c
#define DEVICE_MMIO_NAMED_ROM_PTR(dev, name)
```

相关声明：[DEVICE_MMIO_NAMED_ROM_PTR](#ga7f018db0d820b72a782759a4b674de94)。

返回指向设备MMIO信息在ROM中存储位置的指针。

<a id="r_ga727a1946d2a315af720706a9c9e80465"></a>

```c
#define DEVICE_MMIO_NAMED_ROM_INIT(name, node_id)
```

相关声明：[DEVICE_MMIO_NAMED_ROM_INIT](#ga727a1946d2a315af720706a9c9e80465)。

初始化一个命名的DEVICE_MMIO_NAMED_ROM成员。

<a id="r_gada46ff611e373bdb26a9473ec7cb0380"></a>

```c
#define DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME(name, node_id)
```

相关声明：[DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME](#gada46ff611e373bdb26a9473ec7cb0380)。

使用具名的设备树reg项，初始化一个命名的DEVICE_MMIO_NAMED_ROM成员。

<a id="r_ga1059bb0020656ce6597e29c7dd6680c1"></a>

```c
#define DEVICE_MMIO_NAMED_MAP(dev, name, flags)
```

相关声明：[DEVICE_MMIO_NAMED_MAP](#ga1059bb0020656ce6597e29c7dd6680c1)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

为命名MMIO区域设置内存。

<a id="r_ga5ca4b0cf0637f475b5da3b1ec0a7c995"></a>

```c
#define DEVICE_MMIO_NAMED_GET(dev, name)
```

相关声明：[DEVICE_MMIO_NAMED_GET](#ga5ca4b0cf0637f475b5da3b1ec0a7c995)。

取得设备的命名MMIO地址。

## 13.2\_详细说明（Detailed Documentation）

<a id="ga5ca4b0cf0637f475b5da3b1ec0a7c995"></a>

### `DEVICE_MMIO_NAMED_GET`

```c
#define DEVICE_MMIO_NAMED_GET ( dev, name )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
(*DEVICE_MMIO_NAMED_RAM_PTR((dev), name))
```

取得设备的命名MMIO地址。

此宏从设备对象所关联数据结构中的适当位置，取得命名区域的MMIO基地址。

适用于具有多个MMIO区域的驱动。

此宏要求在本地定义DEV_DATA和DEV_CFG宏，它们应返回指向该驱动专用dev_data和config结构、且类型正确的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备对象。 |
| `name` | MMIO信息成员名称，与DEVICE_MMIO_NAMED_RAM／DEVICE_MMIO_NAMED_ROM声明的名称对应。 |

**参阅（See Also）**：另请参阅DEVICE_MMIO_GET。

**返回（Returns）**：返回MMIO区域的mm_reg_t类型线性地址。

<a id="ga1059bb0020656ce6597e29c7dd6680c1"></a>

### `DEVICE_MMIO_NAMED_MAP`

```c
#define DEVICE_MMIO_NAMED_MAP ( dev, name, flags )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
device_map(DEVICE_MMIO_NAMED_RAM_PTR((dev), name), \
           (DEVICE_MMIO_NAMED_ROM_PTR((dev), name)->phys_addr), \
           (DEVICE_MMIO_NAMED_ROM_PTR((dev), name)->size), \
           (flags))
```

为命名MMIO区域设置内存。

执行必要的PCI探测和／或MMU虚拟内存映射，使DEVICE_MMIO_GET(name)能够返回适用于该MMIO区域的线性内存地址。

如果目标硬件不需要这些操作，本宏展开为空操作。

应从驱动初始化函数中调用本宏，每个需要映射的MMIO区域调用一次。

此宏要求在本地定义DEV_DATA和DEV_CFG宏，它们应返回指向该驱动专用dev_data和config结构、且类型正确的指针。

flags参数目前用于缓存模式，应取DEVICE_CACHE_*宏之一；未使用的位保留供未来扩展。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备对象。 |
| `name` | MMIO信息成员名称，与DEVICE_MMIO_NAMED_RAM／DEVICE_MMIO_NAMED_ROM声明的名称对应。 |
| `flags` | DEVICE_CACHE_*缓存模式之一。 |

> 译注——源码核对：原文声称执行PCI探测，并写DEVICE_MMIO_GET(name)；当前展开只把具名RAM地址保存位置及ROM中的phys_addr／size传给device_map，不做PCI探测。对应取地址宏应为DEVICE_MMIO_NAMED_GET(dev, name)。flags的实际缓存常量使用K_MEM_CACHE_*；需要本地DEV_DATA／DEV_CFG类型转换宏，且不能省略本操作会访问的ROM成员。

<a id="ga92b6570b0f7bd370bbdfbc4e474151e4"></a>

### `DEVICE_MMIO_NAMED_RAM`

```c
#define DEVICE_MMIO_NAMED_RAM ( name)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
mm_reg_t name
```

在设备的dev_data结构中声明MMIO数据的存储空间。

DEVICE_MMIO_NAMED_MAP()和DEVICE_MMIO_NAMED_GET()宏会访问此存储空间。

根据配置，也可能完全不预留内存。可以声明多个命名区域。

如果构建时已知物理地址，config中必须有对应的DEVICE_MMIO_ROM；若构建时未知，例如PCIe设备，则可以省略它。

以名为foo的驱动为例：

原始示例（Example）：

```c
struct foo_driver_data {
     int blarg;
     DEVICE_MMIO_NAMED_RAM(corge);
     DEVICE_MMIO_NAMED_RAM(grault);
     int wibble;
     ...
}
```

无需在构建时初始化此内存；初始化函数中的DEVICE_MMIO_NAMED_MAP()会设置它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 在dev_data中用于保存该信息的成员名称。 |

> 译注——源码核对：与单区域宏不同，命名区域通过DEV_DATA(dev)->name访问，不要求放在结构首部。原文提到相应DEVICE_MMIO_ROM时应结合这里的具名形式理解，配置成员应使用对应的DEVICE_MMIO_NAMED_ROM(name)。省略ROM后不可继续调用依赖它的NAMED_MAP。

<a id="ga42737f178f205bd90d4e523ae5d67a09"></a>

### `DEVICE_MMIO_NAMED_RAM_PTR`

```c
#define DEVICE_MMIO_NAMED_RAM_PTR ( dev, name )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
(&(DEV_DATA(dev)->name))
```

返回指向设备命名MMIO地址在RAM中存储位置的指针。

此宏要求在本地定义DEV_DATA宏，它应返回指向该驱动专用dev_data结构、且类型正确的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例对象。 |
| `name` | dev_data中的成员名称。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `mm_reg_t` | 指向存储位置的指针。 |

> 译注——源码核对：结果是取成员地址，即指向mm_reg_t存储的指针；原返回值表仅写mm_reg_t并不表示返回一个地址值。此宏只在DEVICE_MMIO_IS_IN_RAM下定义，依赖DEV_DATA返回正确的驱动数据指针。

<a id="gae3ad012160f657451a3f47487510bffb"></a>

### `DEVICE_MMIO_NAMED_ROM`

```c
#define DEVICE_MMIO_NAMED_ROM ( name)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
struct z_device_mmio_rom name
```

在设备的config结构中声明MMIO数据的存储空间。

DEVICE_MMIO_NAMED_MAP()和DEVICE_MMIO_NAMED_GET()宏会访问此存储空间。

这里保存的内容随配置有较大差异。可以声明多个命名区域，dev_data结构中必须存在相应条目。

PCIe设备不使用此存储空间，可以将其省略。

使用此成员时，必须在构建时通过DEVICE_MMIO_NAMED_ROM_INIT()，根据DTS信息初始化它。

可通过DEVICE_MMIO_NAMED_ROM_PTR()取得指向此内存的指针。

以名为foo的驱动为例：

原始示例（Example）：

```c
struct foo_config {
     int bar;
     DEVICE_MMIO_NAMED_ROM(corge);
     DEVICE_MMIO_NAMED_ROM(grault);
     int baz;
     ...
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 在config中用于保存该信息的成员名称。 |

**参阅（See Also）**：另请参阅DEVICE_MMIO_NAMED_ROM_INIT()。

<a id="ga727a1946d2a315af720706a9c9e80465"></a>

### `DEVICE_MMIO_NAMED_ROM_INIT`

```c
#define DEVICE_MMIO_NAMED_ROM_INIT ( name, node_id )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
.name = Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)
```

初始化一个命名的DEVICE_MMIO_NAMED_ROM成员。

使用DTS信息，在设备config结构的一个具体实例中初始化MMIO相关信息。

以属于foo子系统的一个驱动实例为例，它具有corge和grault两个命名区域：

原始示例（Example）：

```c
struct foo_config my_config = {
     bar = 7;
     DEVICE_MMIO_NAMED_ROM_INIT(corge, DT_DRV_INST(...));
     DEVICE_MMIO_NAMED_ROM_INIT(grault, DT_DRV_INST(...));
     baz = 2;
     ...
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | config中该MMIO区域的成员名称。 |
| `node_id` | DTS节点标识符。 |

**参阅（See Also）**：另请参阅DEVICE_MMIO_NAMED_ROM()。

> 译注——源码核对：name只指定C结构成员；底层初始化器仍读取node_id的第一个reg项。若同一node_id用于corge和grault，两者会得到同一首项地址／大小，成员名不同不会自动选取不同寄存器区域。需要按reg-names选择时使用BY_NAME版本。原C示例中的bar = 7、baz = 2及分号是原文简写，真实指定初始化器应使用.bar、.baz和逗号。

<a id="gada46ff611e373bdb26a9473ec7cb0380"></a>

### `DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME`

```c
#define DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME ( name, node_id )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
.name = Z_DEVICE_MMIO_NAMED_ROM_INITIALIZER(name, node_id)
```

使用具名的设备树reg项，初始化一个命名的DEVICE_MMIO_NAMED_ROM成员。

与DEVICE_MMIO_NAMED_ROM_INIT相同，但大小及地址取自具名的设备树reg项。

以属于foo子系统的一个驱动实例为例，设备树为它定义chip和dale两个区域：

原始示例（Example）：

```dts
foo@E5000000 {
     reg = <0xE5000000 0x1000>, <0xE6000000 0x1000>;
     reg-names = "chip", "dale";
     ...
};
```

原始示例（Example）：

```c
struct foo_config my_config = {
     bar = 7;
     DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME(chip, DT_DRV_INST(...));
     DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME(dale, DT_DRV_INST(...));
     baz = 2;
     ...
}
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | config中该MMIO区域的成员名称，同时也是设备树中相应reg项的名称。 |
| `node_id` | DTS节点标识符。 |

**参阅（See Also）**：另请参阅DEVICE_MMIO_NAMED_ROM_INIT()。

> 译注——源码核对：name同时用于C成员和DT_REG_ADDR_BY_NAME／DT_REG_SIZE_BY_NAME查找，后者按reg-names选择对应reg项；不是创建名为name的新DT属性。保留原DTS与C示例，C示例中的成员指定和分隔符简写不能直接照搬为完整可编译程序。

<a id="ga7f018db0d820b72a782759a4b674de94"></a>

### `DEVICE_MMIO_NAMED_ROM_PTR`

```c
#define DEVICE_MMIO_NAMED_ROM_PTR ( dev, name )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
(&(DEV_CFG(dev)->name))
```

返回指向设备MMIO信息在ROM中存储位置的指针。

此宏要求在本地定义DEV_CFG宏，它应返回指向该驱动专用config结构、且类型正确的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备实例对象。 |
| `name` | config中的成员名称。 |

**返回（Returns）**：返回指向存储位置的struct device_mmio_rom *指针。

> 译注——源码核对：该宏取DEV_CFG(dev)->name的地址；实际成员类型来自struct z_device_mmio_rom，而非原返回说明中的struct device_mmio_rom。指针的const属性还取决于DEV_CFG的返回类型。

## 13.3\_源码定位与版本边界

MMIO布局和宏展开可在仓库的[device_mmio.h](../../../include/zephyr/sys/device_mmio.h)相对定位；缓存／权限标志见[kernel/mm.h](../../../include/zephyr/kernel/mm.h)，外部地址查询接口见[system_mm.h](../../../include/zephyr/drivers/mm/system_mm.h)。本批核对[官方MMIO头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/device_mmio.h)、[官方内存管理头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel/mm.h)和[官方系统内存驱动接口](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/mm/system_mm.h)，摘要见[来源记录](../SOURCES.md)。本地源码、main和latest网页不能自动视为同一版本。

> 译注——示例完整性：原页结构体与配置示例保留省略号及原始标点；它们用于说明布局和初始化器位置，不是可直接复制编译的完整源文件。命名区域在取得DEV_DATA／DEV_CFG正确类型后按成员访问，单区域宏则依赖首成员布局。

本批只做官方文档翻译与源码核对，没有运行地址映射、访问设备寄存器、构建固件或进行实板实验。

## 13.4\_原页交叉引用（Cross References）

- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/sys/device_mmio.h](P015_设备MMIO头文件参考.md)
- [DEVICE_MMIO_GET](P012_设备单区域MMIO.md#ga8cb49d87ef6dc3b017d5b68860530b63)
- [mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [device_map](P011_设备MMIO管理概述.md#ga6b4a9841a5176104e1b63f7475d3d2a2)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device-mmio-named_html_ga42737f178f205bd90d4e523ae5d67a09"></a>
<a id="agroup__device-mmio-named_html_ga7f018db0d820b72a782759a4b674de94"></a>
<a id="agroup__device-mmio_html_ga6b4a9841a5176104e1b63f7475d3d2a2"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="agroup__sys__io__apis_html_ga7bcfa789a44940bccc5b9b98642744b0"></a>
<a id="agroup__device-mmio-named_html_ga92b6570b0f7bd370bbdfbc4e474151e4"></a>
<a id="agroup__device-mmio-named_html_gae3ad012160f657451a3f47487510bffb"></a>
<a id="agroup__device-mmio-named_html_ga727a1946d2a315af720706a9c9e80465"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__device-mmio-named_html_gada46ff611e373bdb26a9473ec7cb0380"></a>

---

[上一章](P012_设备单区域MMIO.md) · [返回大纲](大纲.md) · [下一章](P014_顶层MMIO区域.md)
