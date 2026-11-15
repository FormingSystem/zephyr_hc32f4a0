---
id: learning.zephyr-docs.device-reference.page-14
title: 顶层MMIO区域
kind: reference
status: maintained
domains: [zephyr, device, mmio, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__device-mmio-toplevel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_顶层MMIO区域

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__device-mmio-toplevel.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是设备内存映射输入输出（Memory-Mapped Input/Output，MMIO）应用程序接口（Application Programming Interface，API）参考。先读[设备驱动模型](../hardware/P003_设备驱动模型.md)，再按[本册大纲](大纲.md)区分物理地址（Physical Address）、线性地址（Linear Address）及区域元数据（Region Metadata），并比较单区域、命名区域与顶层存储。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

适用于不使用Zephyr驱动模型、也不将struct device与驱动实例关联的驱动。

<a id="details"></a>

适用于不使用Zephyr驱动模型、也不将struct device与驱动实例关联的驱动。改为使用顶层存储（Top-Level Storage），可具有全局作用域或static文件作用域。这通常适用于中断控制器和定时器驱动。目前这组宏对PCIe设备的支持不完善；这类设备应使用Zephyr驱动模型，或通过device_map()手动管理内存。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.1\_宏定义（Macros）

<a id="r_gad60e6840b8a9c18c19693da0028c2488"></a>

```c
#define DEVICE_MMIO_TOPLEVEL(name, node_id)
```

相关声明：[DEVICE_MMIO_TOPLEVEL](#gad60e6840b8a9c18c19693da0028c2488)。

声明具有全局作用域的顶层MMIO信息存储。

<a id="r_ga8a712886defe59972f4cf00bb2266f95"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_DECLARE(name)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_DECLARE](#ga8a712886defe59972f4cf00bb2266f95)。

提供对顶层MMIO区域的extern引用。

<a id="r_ga80456633db67dbb23d32e2ae7cc93512"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_STATIC(name, node_id)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_STATIC](#ga80456633db67dbb23d32e2ae7cc93512)。

声明具有static文件作用域的顶层MMIO信息存储。

<a id="r_ga746bfe0c817dbd60f1c1f60d47f1560e"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_RAM_PTR(name)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_RAM_PTR](#ga746bfe0c817dbd60f1c1f60d47f1560e)。

返回指向设备顶层MMIO地址在RAM中存储位置的指针。

<a id="r_ga2877cda5f9780ecff45a4abe150e2504"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_ROM_PTR(name)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_ROM_PTR](#ga2877cda5f9780ecff45a4abe150e2504)。

返回指向顶层MMIO区域在ROM中存储位置的指针。

<a id="r_ga6533dfab1e1bab2a11654abf4231379b"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_MAP(name, flags)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_MAP](#ga6533dfab1e1bab2a11654abf4231379b)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

为驱动的MMIO区域设置内存。

<a id="r_gaad7ad99277cf2be684bd70c46d358338"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_GET(name)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_GET](#gaad7ad99277cf2be684bd70c46d358338)。

取得以顶层方式声明的设备MMIO地址。

## 14.2\_详细说明（Detailed Documentation）

<a id="gad60e6840b8a9c18c19693da0028c2488"></a>

### `DEVICE_MMIO_TOPLEVEL`

```c
#define DEVICE_MMIO_TOPLEVEL ( name, node_id )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
\
mm_reg_t Z_TOPLEVEL_RAM_NAME(name); \
\
const struct z_device_mmio_rom Z_TOPLEVEL_ROM_NAME(name) = \
        Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)
```

声明具有全局作用域的顶层MMIO信息存储。

适用于不采用Zephyr驱动模型中“config／dev_data关联到struct device”组织方式的驱动。

改为在驱动C文件顶层声明。声明具有全局作用域，其他C文件可以通过DEVICE_MMIO_TOPLEVEL_DECLARE引用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 基础符号名称。 |
| `node_id` | 该区域的设备树节点标识符。 |

<a id="ga8a712886defe59972f4cf00bb2266f95"></a>

### `DEVICE_MMIO_TOPLEVEL_DECLARE`

```c
#define DEVICE_MMIO_TOPLEVEL_DECLARE ( name)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
extern mm_reg_t Z_TOPLEVEL_RAM_NAME(name); \
extern const struct z_device_mmio_rom Z_TOPLEVEL_ROM_NAME(name)
```

提供对顶层MMIO区域的extern引用。

如果需要从其他C文件引用通过DEVICE_MMIO_DEFINE定义的顶层MMIO区域，本宏提供所需的extern声明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 顶层MMIO区域名称。 |

**参阅（See Also）**：另请参阅DEVICE_MMIO_TOPLEVEL。

> 译注——源码核对：原文提到DEVICE_MMIO_DEFINE，但本头文件实际配套定义宏是DEVICE_MMIO_TOPLEVEL。DECLARE只生成extern声明；其他C文件还需要且只能有相应定义，不能用它访问另一个文件中TOPLEVEL_STATIC定义的内部链接对象。

<a id="gaad7ad99277cf2be684bd70c46d358338"></a>

### `DEVICE_MMIO_TOPLEVEL_GET`

```c
#define DEVICE_MMIO_TOPLEVEL_GET ( name)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
((mm_reg_t)Z_TOPLEVEL_RAM_NAME(name))
```

取得以顶层方式声明的设备MMIO地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 顶层MMIO区域名称。 |

**参阅（See Also）**：另请参阅DEVICE_MMIO_GET。

**返回（Returns）**：返回MMIO区域的mm_reg_t类型线性地址。

> 译注——源码核对：只读取顶层对象中已保存的线性地址，不触发映射、设备初始化或硬件探测。需要映射的配置应先完成TOPLEVEL_MAP。

<a id="ga6533dfab1e1bab2a11654abf4231379b"></a>

### `DEVICE_MMIO_TOPLEVEL_MAP`

```c
#define DEVICE_MMIO_TOPLEVEL_MAP ( name, flags )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
device_map(&Z_TOPLEVEL_RAM_NAME(name), \
           Z_TOPLEVEL_ROM_NAME(name).phys_addr, \
           Z_TOPLEVEL_ROM_NAME(name).size, (flags))
```

为驱动的MMIO区域设置内存。

执行必要的MMU虚拟内存映射，使DEVICE_MMIO_GET()能够返回适用于该MMIO区域的线性内存地址。

如果目标硬件不需要这些操作，本宏展开为空操作。

应从驱动初始化函数中调用一次。

flags参数目前用于缓存模式，应取DEVICE_CACHE_*宏之一；未使用的位保留供未来扩展。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 顶层MMIO区域名称。 |
| `flags` | DEVICE_CACHE_*缓存模式之一。 |

> 译注——源码核对：对应的取地址宏是DEVICE_MMIO_TOPLEVEL_GET(name)，原文中的DEVICE_MMIO_GET()属于单区域设备接口。当前宏从顶层ROM对象取物理地址及大小调用device_map；非RAM分支为空操作。缓存模式使用K_MEM_CACHE_*。

<a id="ga746bfe0c817dbd60f1c1f60d47f1560e"></a>

### `DEVICE_MMIO_TOPLEVEL_RAM_PTR`

```c
#define DEVICE_MMIO_TOPLEVEL_RAM_PTR ( name)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
&Z_TOPLEVEL_RAM_NAME(name)
```

返回指向设备顶层MMIO地址在RAM中存储位置的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 顶层MMIO区域名称。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `mm_reg_t` | 指向存储位置的指针。 |

> 译注——源码核对：宏结果为保存线性地址的mm_reg_t对象的地址，即mm_reg_t *；原返回值表只写mm_reg_t。此宏仅在DEVICE_MMIO_IS_IN_RAM下定义。

<a id="ga2877cda5f9780ecff45a4abe150e2504"></a>

### `DEVICE_MMIO_TOPLEVEL_ROM_PTR`

```c
#define DEVICE_MMIO_TOPLEVEL_ROM_PTR ( name)
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
&Z_TOPLEVEL_ROM_NAME(name)
```

返回指向顶层MMIO区域在ROM中存储位置的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | MMIO区域名称。 |

**返回（Returns）**：返回指向存储位置的struct device_mmio_rom *指针。

> 译注——源码核对：实际返回const struct z_device_mmio_rom *，不是原说明中的struct device_mmio_rom *；顶层ROM对象由定义宏声明为const。

<a id="ga80456633db67dbb23d32e2ae7cc93512"></a>

### `DEVICE_MMIO_TOPLEVEL_STATIC`

```c
#define DEVICE_MMIO_TOPLEVEL_STATIC ( name, node_id )
```

```c
#include <zephyr/sys/device_mmio.h>
```

展开值（Value）：

```c
\
static mm_reg_t Z_TOPLEVEL_RAM_NAME(name); \
\
static const struct z_device_mmio_rom Z_TOPLEVEL_ROM_NAME(name) = \
        Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)
```

声明具有static文件作用域的顶层MMIO信息存储。

适用于不采用Zephyr驱动模型中“config／dev_data关联到struct device”组织方式的驱动。

改为在驱动C文件顶层声明，声明具有static文件作用域。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 顶层MMIO区域名称。 |
| `node_id` | 该区域的设备树节点标识符。 |

## 14.3\_源码定位与版本边界

MMIO布局和宏展开可在仓库的[device_mmio.h](../../../include/zephyr/sys/device_mmio.h)相对定位；缓存／权限标志见[kernel/mm.h](../../../include/zephyr/kernel/mm.h)，外部地址查询接口见[system_mm.h](../../../include/zephyr/drivers/mm/system_mm.h)。本批核对[官方MMIO头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/device_mmio.h)、[官方内存管理头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel/mm.h)和[官方系统内存驱动接口](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/mm/system_mm.h)，摘要见[来源记录](../SOURCES.md)。本地源码、main和latest网页不能自动视为同一版本。

本批只做官方文档翻译与源码核对，没有运行地址映射、访问设备寄存器、构建固件或进行实板实验。

## 14.4\_原页交叉引用（Cross References）

- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [device_map()](P011_设备MMIO管理概述.md#ga6b4a9841a5176104e1b63f7475d3d2a2)
- [zephyr/sys/device_mmio.h](P015_设备MMIO头文件参考.md)
- [mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [DEVICE_MMIO_GET](P012_设备单区域MMIO.md#ga8cb49d87ef6dc3b017d5b68860530b63)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys__io__apis_html_ga7bcfa789a44940bccc5b9b98642744b0"></a>
<a id="agroup__device-mmio_html_ga6b4a9841a5176104e1b63f7475d3d2a2"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>

---

[上一章](P013_设备命名区域MMIO.md) · [返回大纲](大纲.md) · [下一章](P015_设备MMIO头文件参考.md)
