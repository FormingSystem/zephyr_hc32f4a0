---
id: learning.zephyr-docs.device-reference.page-15
title: 设备MMIO头文件参考
kind: reference
status: maintained
domains: [zephyr, device, mmio, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/device__mmio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_设备MMIO头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/device__mmio_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是设备内存映射输入输出（Memory-Mapped Input/Output，MMIO）应用程序接口（Application Programming Interface，API）参考。先读[设备驱动模型](../hardware/P003_设备驱动模型.md)，再按[本册大纲](大纲.md)区分物理地址（Physical Address）、线性地址（Linear Address）及区域元数据（Region Metadata），并比较单区域、命名区域与顶层存储。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

```c
#include <zephyr/toolchain.h>
#include <zephyr/linker/sections.h>
#include <stdint.h>
#include <stddef.h>
#include <zephyr/kernel/mm.h>
#include <zephyr/sys/sys_io.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.1\_宏定义（Macros）

<a id="r_gabdae30483b01d470c357571e088dc51a"></a>

```c
#define DEVICE_MMIO_IS_IN_RAM
```

相关声明：[DEVICE_MMIO_IS_IN_RAM](P011_设备MMIO管理概述.md#gabdae30483b01d470c357571e088dc51a)。

<a id="r_ga47e037f86108c8da12d8a9b9a35e6ad5"></a>

```c
#define DEVICE_MMIO_RAM mm_reg_t _mmio
```

相关声明：[DEVICE_MMIO_RAM](P012_设备单区域MMIO.md#ga47e037f86108c8da12d8a9b9a35e6ad5)、[mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)。

在设备的dev_data结构中声明MMIO信息的存储空间。

<a id="r_ga63f871dc2ec4c89839a1782e86e292bf"></a>

```c
#define DEVICE_MMIO_RAM_PTR(device)
```

相关声明：[DEVICE_MMIO_RAM_PTR](P012_设备单区域MMIO.md#ga63f871dc2ec4c89839a1782e86e292bf)、[device](P002_设备对象结构.md)。

返回指向设备MMIO地址在RAM中存储位置的指针。

<a id="r_ga1dfb620f6b3c7ee9b2bc54044d0bc875"></a>

```c
#define DEVICE_MMIO_ROM struct z_device_mmio_rom _mmio
```

相关声明：[DEVICE_MMIO_ROM](P012_设备单区域MMIO.md#ga1dfb620f6b3c7ee9b2bc54044d0bc875)。

在设备的config结构中声明MMIO数据的存储空间。

<a id="r_ga6246f4c8bc1542d8960d3bda99a592e5"></a>

```c
#define DEVICE_MMIO_ROM_PTR(dev)
```

相关声明：[DEVICE_MMIO_ROM_PTR](P012_设备单区域MMIO.md#ga6246f4c8bc1542d8960d3bda99a592e5)。

返回指向设备MMIO信息在ROM中存储位置的指针。

<a id="r_ga023516c60725f8c6d62110f74af22549"></a>

```c
#define DEVICE_MMIO_ROM_INIT(node_id)
```

相关声明：[DEVICE_MMIO_ROM_INIT](P012_设备单区域MMIO.md#ga023516c60725f8c6d62110f74af22549)。

初始化DEVICE_MMIO_ROM成员。

<a id="r_ga8e15770c4ec118edbefc1ef95f1ace80"></a>

```c
#define DEVICE_MMIO_MAP(dev, flags)
```

相关声明：[DEVICE_MMIO_MAP](P012_设备单区域MMIO.md#ga8e15770c4ec118edbefc1ef95f1ace80)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将MMIO内存映射到地址空间（Address Space）。

<a id="r_ga8cb49d87ef6dc3b017d5b68860530b63"></a>

```c
#define DEVICE_MMIO_GET(dev)
```

相关声明：[DEVICE_MMIO_GET](P012_设备单区域MMIO.md#ga8cb49d87ef6dc3b017d5b68860530b63)。

取得设备的MMIO地址。

<a id="r_ga92b6570b0f7bd370bbdfbc4e474151e4"></a>

```c
#define DEVICE_MMIO_NAMED_RAM(name)
```

相关声明：[DEVICE_MMIO_NAMED_RAM](P013_设备命名区域MMIO.md#ga92b6570b0f7bd370bbdfbc4e474151e4)。

在设备的dev_data结构中声明MMIO数据的存储空间。

<a id="r_ga42737f178f205bd90d4e523ae5d67a09"></a>

```c
#define DEVICE_MMIO_NAMED_RAM_PTR(dev, name)
```

相关声明：[DEVICE_MMIO_NAMED_RAM_PTR](P013_设备命名区域MMIO.md#ga42737f178f205bd90d4e523ae5d67a09)。

返回指向设备命名MMIO地址在RAM中存储位置的指针。

<a id="r_gae3ad012160f657451a3f47487510bffb"></a>

```c
#define DEVICE_MMIO_NAMED_ROM(name)
```

相关声明：[DEVICE_MMIO_NAMED_ROM](P013_设备命名区域MMIO.md#gae3ad012160f657451a3f47487510bffb)。

在设备的config结构中声明MMIO数据的存储空间。

<a id="r_ga7f018db0d820b72a782759a4b674de94"></a>

```c
#define DEVICE_MMIO_NAMED_ROM_PTR(dev, name)
```

相关声明：[DEVICE_MMIO_NAMED_ROM_PTR](P013_设备命名区域MMIO.md#ga7f018db0d820b72a782759a4b674de94)。

返回指向设备MMIO信息在ROM中存储位置的指针。

<a id="r_ga727a1946d2a315af720706a9c9e80465"></a>

```c
#define DEVICE_MMIO_NAMED_ROM_INIT(name, node_id)
```

相关声明：[DEVICE_MMIO_NAMED_ROM_INIT](P013_设备命名区域MMIO.md#ga727a1946d2a315af720706a9c9e80465)。

初始化一个命名的DEVICE_MMIO_NAMED_ROM成员。

<a id="r_gada46ff611e373bdb26a9473ec7cb0380"></a>

```c
#define DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME(name, node_id)
```

相关声明：[DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME](P013_设备命名区域MMIO.md#gada46ff611e373bdb26a9473ec7cb0380)。

使用具名的设备树reg项，初始化一个命名的DEVICE_MMIO_NAMED_ROM成员。

<a id="r_ga1059bb0020656ce6597e29c7dd6680c1"></a>

```c
#define DEVICE_MMIO_NAMED_MAP(dev, name, flags)
```

相关声明：[DEVICE_MMIO_NAMED_MAP](P013_设备命名区域MMIO.md#ga1059bb0020656ce6597e29c7dd6680c1)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

为命名MMIO区域设置内存。

<a id="r_ga5ca4b0cf0637f475b5da3b1ec0a7c995"></a>

```c
#define DEVICE_MMIO_NAMED_GET(dev, name)
```

相关声明：[DEVICE_MMIO_NAMED_GET](P013_设备命名区域MMIO.md#ga5ca4b0cf0637f475b5da3b1ec0a7c995)。

取得设备的命名MMIO地址。

<a id="r_gad60e6840b8a9c18c19693da0028c2488"></a>

```c
#define DEVICE_MMIO_TOPLEVEL(name, node_id)
```

相关声明：[DEVICE_MMIO_TOPLEVEL](P014_顶层MMIO区域.md#gad60e6840b8a9c18c19693da0028c2488)。

声明具有全局作用域的顶层MMIO信息存储。

<a id="r_ga8a712886defe59972f4cf00bb2266f95"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_DECLARE(name)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_DECLARE](P014_顶层MMIO区域.md#ga8a712886defe59972f4cf00bb2266f95)。

提供对顶层MMIO区域的extern引用。

<a id="r_ga80456633db67dbb23d32e2ae7cc93512"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_STATIC(name, node_id)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_STATIC](P014_顶层MMIO区域.md#ga80456633db67dbb23d32e2ae7cc93512)。

声明具有static文件作用域的顶层MMIO信息存储。

<a id="r_ga746bfe0c817dbd60f1c1f60d47f1560e"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_RAM_PTR(name)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_RAM_PTR](P014_顶层MMIO区域.md#ga746bfe0c817dbd60f1c1f60d47f1560e)。

返回指向设备顶层MMIO地址在RAM中存储位置的指针。

<a id="r_ga2877cda5f9780ecff45a4abe150e2504"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_ROM_PTR(name)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_ROM_PTR](P014_顶层MMIO区域.md#ga2877cda5f9780ecff45a4abe150e2504)。

返回指向顶层MMIO区域在ROM中存储位置的指针。

<a id="r_ga6533dfab1e1bab2a11654abf4231379b"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_MAP(name, flags)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_MAP](P014_顶层MMIO区域.md#ga6533dfab1e1bab2a11654abf4231379b)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

为驱动的MMIO区域设置内存。

<a id="r_gaad7ad99277cf2be684bd70c46d358338"></a>

```c
#define DEVICE_MMIO_TOPLEVEL_GET(name)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_GET](P014_顶层MMIO区域.md#gaad7ad99277cf2be684bd70c46d358338)。

取得以顶层方式声明的设备MMIO地址。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.2\_函数（Functions）

<a id="r_ga6b4a9841a5176104e1b63f7475d3d2a2"></a>

```c
static __boot_func void device_map (mm_reg_t *virt_addr, uintptr_t phys_addr, size_t size, uint32_t flags)
```

相关声明：[device_map](P011_设备MMIO管理概述.md#ga6b4a9841a5176104e1b63f7475d3d2a2)、[mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)、[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

设置用于设备MMIO访问的线性地址（Linear Address）。

<a id="r_ga16070be695cec4ebc01915a3dbc1adf8"></a>

```c
static __boot_func void device_unmap (mm_reg_t virt_addr, size_t size)
```

相关声明：[device_unmap](P011_设备MMIO管理概述.md#ga16070be695cec4ebc01915a3dbc1adf8)、[mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)。

撤销用于设备MMIO访问的线性地址。

## 15.3\_源码定位与版本边界

MMIO布局和宏展开可在仓库的[device_mmio.h](../../../include/zephyr/sys/device_mmio.h)相对定位；缓存／权限标志见[kernel/mm.h](../../../include/zephyr/kernel/mm.h)，外部地址查询接口见[system_mm.h](../../../include/zephyr/drivers/mm/system_mm.h)。本批核对[官方MMIO头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/device_mmio.h)、[官方内存管理头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/kernel/mm.h)和[官方系统内存驱动接口](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/mm/system_mm.h)，摘要见[来源记录](../SOURCES.md)。本地源码、main和latest网页不能自动视为同一版本。

> 译注——参考页覆盖：本页保留官方头文件的概览与摘要；宏的完整参数、示例和条件分支说明分别见[概述](P011_设备MMIO管理概述.md)、[单区域](P012_设备单区域MMIO.md)、[命名区域](P013_设备命名区域MMIO.md)和[顶层区域](P014_顶层MMIO区域.md)，完整可见代码见[源码页](P016_设备MMIO头文件源码.md)。

本批只做官方文档翻译与源码核对，没有运行地址映射、访问设备寄存器、构建固件或进行实板实验。

## 15.4\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [zephyr/linker/sections.h](https://docs.zephyrproject.org/latest/doxygen/html/sections_8h_source.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/kernel/mm.h](https://docs.zephyrproject.org/latest/doxygen/html/mm_8h_source.html)
- [zephyr/sys/sys_io.h](P022_系统IO头文件源码.md)
- [查看此文件的源码](P016_设备MMIO头文件源码.md)
- [DEVICE_MMIO_IS_IN_RAM](P011_设备MMIO管理概述.md#gabdae30483b01d470c357571e088dc51a)
- [DEVICE_MMIO_RAM](P012_设备单区域MMIO.md#ga47e037f86108c8da12d8a9b9a35e6ad5)
- [mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [DEVICE_MMIO_RAM_PTR](P012_设备单区域MMIO.md#ga63f871dc2ec4c89839a1782e86e292bf)
- [device](P002_设备对象结构.md)
- [DEVICE_MMIO_ROM](P012_设备单区域MMIO.md#ga1dfb620f6b3c7ee9b2bc54044d0bc875)
- [DEVICE_MMIO_ROM_PTR](P012_设备单区域MMIO.md#ga6246f4c8bc1542d8960d3bda99a592e5)
- [DEVICE_MMIO_ROM_INIT](P012_设备单区域MMIO.md#ga023516c60725f8c6d62110f74af22549)
- [DEVICE_MMIO_MAP](P012_设备单区域MMIO.md#ga8e15770c4ec118edbefc1ef95f1ace80)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [DEVICE_MMIO_GET](P012_设备单区域MMIO.md#ga8cb49d87ef6dc3b017d5b68860530b63)
- [DEVICE_MMIO_NAMED_RAM](P013_设备命名区域MMIO.md#ga92b6570b0f7bd370bbdfbc4e474151e4)
- [DEVICE_MMIO_NAMED_RAM_PTR](P013_设备命名区域MMIO.md#ga42737f178f205bd90d4e523ae5d67a09)
- [DEVICE_MMIO_NAMED_ROM](P013_设备命名区域MMIO.md#gae3ad012160f657451a3f47487510bffb)
- [DEVICE_MMIO_NAMED_ROM_PTR](P013_设备命名区域MMIO.md#ga7f018db0d820b72a782759a4b674de94)
- [DEVICE_MMIO_NAMED_ROM_INIT](P013_设备命名区域MMIO.md#ga727a1946d2a315af720706a9c9e80465)
- [DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME](P013_设备命名区域MMIO.md#gada46ff611e373bdb26a9473ec7cb0380)
- [DEVICE_MMIO_NAMED_MAP](P013_设备命名区域MMIO.md#ga1059bb0020656ce6597e29c7dd6680c1)
- [DEVICE_MMIO_NAMED_GET](P013_设备命名区域MMIO.md#ga5ca4b0cf0637f475b5da3b1ec0a7c995)
- [DEVICE_MMIO_TOPLEVEL](P014_顶层MMIO区域.md#gad60e6840b8a9c18c19693da0028c2488)
- [DEVICE_MMIO_TOPLEVEL_DECLARE](P014_顶层MMIO区域.md#ga8a712886defe59972f4cf00bb2266f95)
- [DEVICE_MMIO_TOPLEVEL_STATIC](P014_顶层MMIO区域.md#ga80456633db67dbb23d32e2ae7cc93512)
- [DEVICE_MMIO_TOPLEVEL_RAM_PTR](P014_顶层MMIO区域.md#ga746bfe0c817dbd60f1c1f60d47f1560e)
- [DEVICE_MMIO_TOPLEVEL_ROM_PTR](P014_顶层MMIO区域.md#ga2877cda5f9780ecff45a4abe150e2504)
- [DEVICE_MMIO_TOPLEVEL_MAP](P014_顶层MMIO区域.md#ga6533dfab1e1bab2a11654abf4231379b)
- [DEVICE_MMIO_TOPLEVEL_GET](P014_顶层MMIO区域.md#gaad7ad99277cf2be684bd70c46d358338)
- [device_map](P011_设备MMIO管理概述.md#ga6b4a9841a5176104e1b63f7475d3d2a2)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [device_unmap](P011_设备MMIO管理概述.md#ga16070be695cec4ebc01915a3dbc1adf8)

---

[上一章](P014_顶层MMIO区域.md) · [返回大纲](大纲.md) · [下一章](P016_设备MMIO头文件源码.md)
