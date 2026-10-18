---
id: learning.zephyr-docs.flash-reference.page-9
title: Flash公共头文件参考
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flash_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_Flash公共头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/flash_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是闪存（Flash）应用程序接口（Application Programming Interface，API）参考。先读[Flash概述](../hardware/P012_Flash闪存.md)理解设备偏移，再按[本册大纲](大纲.md)区分应用接口、驱动后端（Driver Backend）、页布局（Page Layout）和扩展操作。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

Flash 驱动应用程序接口（Application Programming Interface，API）的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/types.h>
#include <stddef.h>
#include <sys/types.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/flash.h>
```

查看此文件的源码。入口：[源码浏览译文](P010_Flash公共头文件源码.md)。

Flash 驱动应用程序接口（Application Programming Interface，API）的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_flash_5Fpages_5Flayout"></a>

```c
struct flash_pages_layout
```

相关声明：[flash_pages_layout](P006_Flash页布局结构.md)。

描述一段大小相同的闪存页序列。

<a id="r_flash_5Fparameters"></a>

```c
struct flash_parameters
```

相关声明：[flash_parameters](P004_Flash存储参数结构.md)。

闪存参数（Flash Memory Parameters）。

<a id="r_flash_5Fdriver_5Fapi"></a>

```c
struct flash_driver_api
```

相关声明：[flash_driver_api](P007_Flash驱动操作结构.md)。

驱动操作（Driver Operations）：Flash 驱动的操作集合。

<a id="r_flash_5Fpages_5Finfo"></a>

```c
struct flash_pages_info
```

相关声明：[flash_pages_info](P005_Flash页信息结构.md)。

闪存页的信息（Flash Page Information）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_ga760f7d79cb9f23bc0326abfea85808aa"></a>

```c
#define FLASH_ERASE_C_EXPLICIT 0x01
```

相关声明：[FLASH_ERASE_C_EXPLICIT](P001_Flash公共接口.md#ga760f7d79cb9f23bc0326abfea85808aa)。

用于普通 Flash：写入任意数据前需要擦除时设置此标志。

<a id="r_ga82adeb566049cfbbced1c50db5d17760"></a>

```c
#define FLASH_ERASE_CAPS_UNSET (int)-1
```

相关声明：[FLASH_ERASE_CAPS_UNSET](P001_Flash公共接口.md#ga82adeb566049cfbbced1c50db5d17760)。

保留供使用者初始化变量；该变量之后用于保存能力信息（Capabilities）。

<a id="r_ga37f63f7c484ae89c9a133fbe2616a8ea"></a>

```c
#define FLASH_ERASE_C_SUPPORTED 0x02
```

相关声明：[FLASH_ERASE_C_SUPPORTED](P001_Flash公共接口.md#ga37f63f7c484ae89c9a133fbe2616a8ea)。

保留，尚未使用。

<a id="r_gaf0257b23bbe071c5b1e0294e7d31fca4"></a>

```c
#define FLASH_ERASE_C_VAL_BIT 0x04
```

相关声明：[FLASH_ERASE_C_VAL_BIT](P001_Flash公共接口.md#gaf0257b23bbe071c5b1e0294e7d31fca4)。

保留，尚未使用。

<a id="r_ga6dc21974c3db6b5b7a69cdfb170b2c06"></a>

```c
#define FLASH_ERASE_UNIFORM_PAGE 0x08
```

相关声明：[FLASH_ERASE_UNIFORM_PAGE](P001_Flash公共接口.md#ga6dc21974c3db6b5b7a69cdfb170b2c06)。

保留，尚未使用。

<a id="r_ga67418b2d5cbbec83463dce3d426162e3"></a>

```c
#define FLASH_EX_OP_VENDOR_BASE 0x8000
```

相关声明：[FLASH_EX_OP_VENDOR_BASE](P001_Flash公共接口.md#ga67418b2d5cbbec83463dce3d426162e3)。

厂商专用扩展操作码范围的起始值。

<a id="r_gafc0aa899b7ea452d048d8ee67d2e6f06"></a>

```c
#define FLASH_EX_OP_IS_VENDOR(c)
```

相关声明：[FLASH_EX_OP_IS_VENDOR](P001_Flash公共接口.md#gafc0aa899b7ea452d048d8ee67d2e6f06)。

检查扩展操作码是否属于厂商专用范围。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.3\_类型定义（Typedefs）

<a id="r_ga358404d040b7ef30c8d24106e97bc290"></a>

```c
typedef int(* flash_api_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[flash_api_read](P002_Flash驱动后端接口.md#ga358404d040b7ef30c8d24106e97bc290)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

闪存读取实现的处理函数类型。

<a id="r_gaf6b0c3aa2b6514ac8936aa0c7fda96ba"></a>

```c
typedef int(* flash_api_write) (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[flash_api_write](P002_Flash驱动后端接口.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

闪存写入实现的处理函数类型。

<a id="r_ga2178a2338e652396ba9811ca449f4cb5"></a>

```c
typedef int(* flash_api_erase) (const struct device *dev, off_t offset, size_t size)
```

相关声明：[flash_api_erase](P002_Flash驱动后端接口.md#ga2178a2338e652396ba9811ca449f4cb5)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

闪存擦除实现的处理函数类型。

<a id="r_ga97ab6540136589aaafbe049cf4302285"></a>

```c
typedef int(* flash_api_get_size) (const struct device *dev, uint64_t *size)
```

相关声明：[flash_api_get_size](P002_Flash驱动后端接口.md#ga97ab6540136589aaafbe049cf4302285)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

取得以字节为单位的设备容量。

<a id="r_ga2dee3874cb1be4ef4dab599963c30e70"></a>

```c
typedef const struct flash_parameters *(* flash_api_get_parameters) (const struct device *dev)
```

相关声明：[flash_parameters](P004_Flash存储参数结构.md)、[flash_api_get_parameters](P002_Flash驱动后端接口.md#ga2dee3874cb1be4ef4dab599963c30e70)、[device](../device_reference/P002_设备对象结构.md)。

取得设备参数。

<a id="r_ga7576411536217c9ec3e167e7a5ca82a5"></a>

```c
typedef void(* flash_api_pages_layout) (const struct device *dev, const struct flash_pages_layout **layout, size_t *layout_size)
```

相关声明：[flash_api_pages_layout](P002_Flash驱动后端接口.md#ga7576411536217c9ec3e167e7a5ca82a5)、[device](../device_reference/P002_设备对象结构.md)、[flash_pages_layout](P006_Flash页布局结构.md)。

取得闪存设备的布局（Layout）。

<a id="r_gac7b802015885044df6a1872513b89ab5"></a>

```c
typedef int(* flash_api_sfdp_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[flash_api_sfdp_read](P002_Flash驱动后端接口.md#gac7b802015885044df6a1872513b89ab5)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

从串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）区域读取数据。

<a id="r_ga088369ef7593aa7c1fbe4cdad6e5b994"></a>

```c
typedef int(* flash_api_read_jedec_id) (const struct device *dev, uint8_t *id)
```

相关声明：[flash_api_read_jedec_id](P002_Flash驱动后端接口.md#ga088369ef7593aa7c1fbe4cdad6e5b994)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取设备的 JEDEC 标识。

<a id="r_gacff972cc16c1afa0a85e3118eff0afb2"></a>

```c
typedef int(* flash_api_ex_op) (const struct device *dev, uint16_t code, const uintptr_t in, void *out)
```

相关声明：[flash_api_ex_op](P002_Flash驱动后端接口.md#gacff972cc16c1afa0a85e3118eff0afb2)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)。

执行扩展操作。

<a id="r_ga41bfc5eb05a8e73873763c36f3e1ec6f"></a>

```c
typedef bool(* flash_page_cb) (const struct flash_pages_info *info, void *data)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[flash_page_cb](P001_Flash公共接口.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)、[flash_pages_info](P005_Flash页信息结构.md)。

遍历设备上各闪存页时使用的回调（Callback）类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.4\_枚举（Enumerations）

<a id="r_gae401e7b13d22a0f405e8d2ca0ef33c51"></a>

```c
enum flash_ex_op_types { FLASH_EX_OP_RESET = 0 , FLASH_EX_OP_IS_BAD_BLOCK = 1 , FLASH_EX_OP_MARK_BAD_BLOCK = 2 }
```

相关声明：[flash_ex_op_types](P001_Flash公共接口.md#gae401e7b13d22a0f405e8d2ca0ef33c51)、[FLASH_EX_OP_RESET](P001_Flash公共接口.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd)、[FLASH_EX_OP_IS_BAD_BLOCK](P001_Flash公共接口.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a56ea1df211a928c8bd2ade61df9cce34)、[FLASH_EX_OP_MARK_BAD_BLOCK](P001_Flash公共接口.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a22b688ac088aead1f989ecb656fc7342)。

额外闪存操作的枚举（Enumeration）。

<a id="r_ga8eeb7135fbe276e7c287d895a91c6116"></a>

```c
enum flash_block_status { FLASH_BLOCK_GOOD = 0 , FLASH_BLOCK_BAD = 1 }
```

相关声明：[flash_block_status](P001_Flash公共接口.md#ga8eeb7135fbe276e7c287d895a91c6116)、[FLASH_BLOCK_GOOD](P001_Flash公共接口.md#gga8eeb7135fbe276e7c287d895a91c6116a1974162ef10f5b83bb8428e3c7c513c7)、[FLASH_BLOCK_BAD](P001_Flash公共接口.md#gga8eeb7135fbe276e7c287d895a91c6116a398def014a3982b35e4557f93bfa44bb)。

闪存块状态（Block Status）的枚举。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.5\_函数（Functions）

<a id="r_gabc73e8888dcb8f4f79cd80b8d02a6a2c"></a>

```c
static int flash_params_get_erase_cap (const struct flash_parameters *p)
```

相关声明：[flash_params_get_erase_cap](P001_Flash公共接口.md#gabc73e8888dcb8f4f79cd80b8d02a6a2c)、[flash_parameters](P004_Flash存储参数结构.md)。

解析 `flash_parameters`，取得擦除能力（Erase Capabilities）。

<a id="r_ga1649b22ba5c5974060b4a3c44a0e44e2"></a>

```c
static bool flash_params_erase_value_readable (const struct flash_parameters *p)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[flash_params_erase_value_readable](P001_Flash公共接口.md#ga1649b22ba5c5974060b4a3c44a0e44e2)、[flash_parameters](P004_Flash存储参数结构.md)。

检查已擦除区域是否能读回擦除值（Erase Value）。

<a id="r_gaa7c9382796aad64da0da683f54600b5f"></a>

```c
int flash_read (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[flash_read](P001_Flash公共接口.md#gaa7c9382796aad64da0da683f54600b5f)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

从闪存读取数据。

<a id="r_ga76d7880cc5e18ca40237736d3bd94324"></a>

```c
int flash_write (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[flash_write](P001_Flash公共接口.md#ga76d7880cc5e18ca40237736d3bd94324)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

将缓冲区内容写入闪存。

<a id="r_ga05f9c8b0c1ff7273f71797e7ff799c95"></a>

```c
int flash_erase (const struct device *dev, off_t offset, size_t size)
```

相关声明：[flash_erase](P001_Flash公共接口.md#ga05f9c8b0c1ff7273f71797e7ff799c95)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

擦除部分或全部闪存。

<a id="r_ga471edb53a2b1abe3dff0f4e2d216521e"></a>

```c
int flash_get_size (const struct device *dev, uint64_t *size)
```

相关声明：[flash_get_size](P001_Flash公共接口.md#ga471edb53a2b1abe3dff0f4e2d216521e)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

取得以字节为单位的设备容量。

<a id="r_ga022838332e905b0111d5136dd963889b"></a>

```c
int flash_fill (const struct device *dev, uint8_t val, off_t offset, size_t size)
```

相关声明：[flash_fill](P001_Flash公共接口.md#ga022838332e905b0111d5136dd963889b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

用指定值填充设备的选定范围。

<a id="r_ga11eda0cdc7be12636a90d2e8c7264e4a"></a>

```c
int flash_flatten (const struct device *dev, off_t offset, size_t size)
```

相关声明：[flash_flatten](P001_Flash公共接口.md#ga11eda0cdc7be12636a90d2e8c7264e4a)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

擦除部分或全部闪存，或将该区域填平为统一值。

<a id="r_gafc959b0363eb27d6a3237e4288d60979"></a>

```c
int flash_get_page_info_by_offs (const struct device *dev, off_t offset, struct flash_pages_info *info)
```

相关声明：[flash_get_page_info_by_offs](P001_Flash公共接口.md#gafc959b0363eb27d6a3237e4288d60979)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[flash_pages_info](P005_Flash页信息结构.md)。

取得指定闪存偏移所处页的大小和起始偏移。

<a id="r_gaae733082fa92f80261d5895d3f81a98b"></a>

```c
int flash_get_page_info_by_idx (const struct device *dev, uint32_t page_index, struct flash_pages_info *info)
```

相关声明：[flash_get_page_info_by_idx](P001_Flash公共接口.md#gaae733082fa92f80261d5895d3f81a98b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flash_pages_info](P005_Flash页信息结构.md)。

取得指定索引的闪存页大小和起始偏移。

<a id="r_gaf750fe20c02758be7e37f36d2d16345e"></a>

```c
size_t flash_get_page_count (const struct device *dev)
```

相关声明：[flash_get_page_count](P001_Flash公共接口.md#gaf750fe20c02758be7e37f36d2d16345e)、[device](../device_reference/P002_设备对象结构.md)。

取得闪存页总数。

<a id="r_ga275f2346e88b5e4d050dae426f0953fe"></a>

```c
void flash_page_foreach (const struct device *dev, flash_page_cb cb, void *data)
```

相关声明：[flash_page_foreach](P001_Flash公共接口.md#ga275f2346e88b5e4d050dae426f0953fe)、[device](../device_reference/P002_设备对象结构.md)、[flash_page_cb](P001_Flash公共接口.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)。

遍历设备上的所有闪存页。

<a id="r_ga8e9b921299bfb059bf72445a2ffa5a97"></a>

```c
int flash_sfdp_read (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[flash_sfdp_read](P001_Flash公共接口.md#ga8e9b921299bfb059bf72445a2ffa5a97)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

从串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）区域读取数据。

<a id="r_gadb273ed317e1088b57adcac3385f50a7"></a>

```c
int flash_read_jedec_id (const struct device *dev, uint8_t *id)
```

相关声明：[flash_read_jedec_id](P001_Flash公共接口.md#gadb273ed317e1088b57adcac3385f50a7)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从兼容的闪存设备读取 JEDEC 标识（JEDEC ID）。

<a id="r_gaadfb323bc1b4efa39e7bc0a048c472a6"></a>

```c
size_t flash_get_write_block_size (const struct device *dev)
```

相关声明：[flash_get_write_block_size](P001_Flash公共接口.md#gaadfb323bc1b4efa39e7bc0a048c472a6)、[device](../device_reference/P002_设备对象结构.md)。

取得驱动支持的最小写入块大小（Minimum Write Block Size）。

<a id="r_ga07b516708224b7a69a5169ef9c5c26e3"></a>

```c
const struct flash_parameters * flash_get_parameters (const struct device *dev)
```

相关声明：[flash_parameters](P004_Flash存储参数结构.md)、[flash_get_parameters](P001_Flash公共接口.md#ga07b516708224b7a69a5169ef9c5c26e3)、[device](../device_reference/P002_设备对象结构.md)。

取得指向 `flash_parameters` 结构体的指针。

<a id="r_ga5571fbed2babb0036255d7a4d5e66f6c"></a>

```c
int flash_ex_op (const struct device *dev, uint16_t code, const uintptr_t in, void *out)
```

相关声明：[flash_ex_op](P001_Flash公共接口.md#ga5571fbed2babb0036255d7a4d5e66f6c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)。

在指定设备上执行闪存扩展操作（Extended Operation）。

<a id="r_ga847407358a20d3d5918d8ef11657ce2b"></a>

```c
int flash_copy (const struct device *src_dev, off_t src_offset, const struct device *dst_dev, off_t dst_offset, off_t size, uint8_t *buf, size_t buf_size)
```

相关声明：[flash_copy](P001_Flash公共接口.md#ga847407358a20d3d5918d8ef11657ce2b)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将闪存内容从一个设备复制到另一个设备。

## 9.6\_源码定位与操作边界

本页列出flash.h的公开参考摘要；[公共接口](P001_Flash公共接口.md)、[驱动后端](P002_Flash驱动后端接口.md)与[源码浏览译文](P010_Flash公共头文件源码.md)分别提供调用条件、驱动职责及可见代码。仓库相对定位为[flash.h](../../../include/zephyr/drivers/flash.h)，本次源码依据见[来源记录](../SOURCES.md)。

> 译注——展示范围：本页列出九个后端操作类型，而官方源码浏览页还包含CONFIG_FLASH_HAS_DRIVER_FILL条件下的flash_api_fill和fill成员；二者并非足以证明源码版本不同。去掉注释和展示空白后，本次浏览页与读取的main头文件代码一致。按实际编译配置判断成员是否存在，不把API摘要当作完整条件编译布局。

本批仅翻译和核对官方源码，未构建、烧录、读写标识页或执行存储擦除；上游链接的main会滚动更新。

## 9.7\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件源码](P010_Flash公共头文件源码.md)
- [flash_pages_layout](P006_Flash页布局结构.md)
- [flash_parameters](P004_Flash存储参数结构.md)
- [flash_driver_api](P007_Flash驱动操作结构.md)
- [flash_pages_info](P005_Flash页信息结构.md)
- [FLASH_ERASE_C_EXPLICIT](P001_Flash公共接口.md#ga760f7d79cb9f23bc0326abfea85808aa)
- [FLASH_ERASE_CAPS_UNSET](P001_Flash公共接口.md#ga82adeb566049cfbbced1c50db5d17760)
- [FLASH_ERASE_C_SUPPORTED](P001_Flash公共接口.md#ga37f63f7c484ae89c9a133fbe2616a8ea)
- [FLASH_ERASE_C_VAL_BIT](P001_Flash公共接口.md#gaf0257b23bbe071c5b1e0294e7d31fca4)
- [FLASH_ERASE_UNIFORM_PAGE](P001_Flash公共接口.md#ga6dc21974c3db6b5b7a69cdfb170b2c06)
- [FLASH_EX_OP_VENDOR_BASE](P001_Flash公共接口.md#ga67418b2d5cbbec83463dce3d426162e3)
- [FLASH_EX_OP_IS_VENDOR](P001_Flash公共接口.md#gafc0aa899b7ea452d048d8ee67d2e6f06)
- [flash_api_read](P002_Flash驱动后端接口.md#ga358404d040b7ef30c8d24106e97bc290)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [flash_api_write](P002_Flash驱动后端接口.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)
- [flash_api_erase](P002_Flash驱动后端接口.md#ga2178a2338e652396ba9811ca449f4cb5)
- [flash_api_get_size](P002_Flash驱动后端接口.md#ga97ab6540136589aaafbe049cf4302285)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [flash_api_get_parameters](P002_Flash驱动后端接口.md#ga2dee3874cb1be4ef4dab599963c30e70)
- [flash_api_pages_layout](P002_Flash驱动后端接口.md#ga7576411536217c9ec3e167e7a5ca82a5)
- [flash_api_sfdp_read](P002_Flash驱动后端接口.md#gac7b802015885044df6a1872513b89ab5)
- [flash_api_read_jedec_id](P002_Flash驱动后端接口.md#ga088369ef7593aa7c1fbe4cdad6e5b994)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flash_api_ex_op](P002_Flash驱动后端接口.md#gacff972cc16c1afa0a85e3118eff0afb2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [flash_page_cb](P001_Flash公共接口.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)
- [flash_ex_op_types](P001_Flash公共接口.md#gae401e7b13d22a0f405e8d2ca0ef33c51)
- [FLASH_EX_OP_RESET](P001_Flash公共接口.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd)
- [FLASH_EX_OP_IS_BAD_BLOCK](P001_Flash公共接口.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a56ea1df211a928c8bd2ade61df9cce34)
- [FLASH_EX_OP_MARK_BAD_BLOCK](P001_Flash公共接口.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a22b688ac088aead1f989ecb656fc7342)
- [flash_block_status](P001_Flash公共接口.md#ga8eeb7135fbe276e7c287d895a91c6116)
- [FLASH_BLOCK_GOOD](P001_Flash公共接口.md#gga8eeb7135fbe276e7c287d895a91c6116a1974162ef10f5b83bb8428e3c7c513c7)
- [FLASH_BLOCK_BAD](P001_Flash公共接口.md#gga8eeb7135fbe276e7c287d895a91c6116a398def014a3982b35e4557f93bfa44bb)
- [flash_params_get_erase_cap](P001_Flash公共接口.md#gabc73e8888dcb8f4f79cd80b8d02a6a2c)
- [flash_params_erase_value_readable](P001_Flash公共接口.md#ga1649b22ba5c5974060b4a3c44a0e44e2)
- [flash_read](P001_Flash公共接口.md#gaa7c9382796aad64da0da683f54600b5f)
- [flash_write](P001_Flash公共接口.md#ga76d7880cc5e18ca40237736d3bd94324)
- [flash_erase](P001_Flash公共接口.md#ga05f9c8b0c1ff7273f71797e7ff799c95)
- [flash_get_size](P001_Flash公共接口.md#ga471edb53a2b1abe3dff0f4e2d216521e)
- [flash_fill](P001_Flash公共接口.md#ga022838332e905b0111d5136dd963889b)
- [flash_flatten](P001_Flash公共接口.md#ga11eda0cdc7be12636a90d2e8c7264e4a)
- [flash_get_page_info_by_offs](P001_Flash公共接口.md#gafc959b0363eb27d6a3237e4288d60979)
- [flash_get_page_info_by_idx](P001_Flash公共接口.md#gaae733082fa92f80261d5895d3f81a98b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flash_get_page_count](P001_Flash公共接口.md#gaf750fe20c02758be7e37f36d2d16345e)
- [flash_page_foreach](P001_Flash公共接口.md#ga275f2346e88b5e4d050dae426f0953fe)
- [flash_sfdp_read](P001_Flash公共接口.md#ga8e9b921299bfb059bf72445a2ffa5a97)
- [flash_read_jedec_id](P001_Flash公共接口.md#gadb273ed317e1088b57adcac3385f50a7)
- [flash_get_write_block_size](P001_Flash公共接口.md#gaadfb323bc1b4efa39e7bc0a048c472a6)
- [flash_get_parameters](P001_Flash公共接口.md#ga07b516708224b7a69a5169ef9c5c26e3)
- [flash_ex_op](P001_Flash公共接口.md#ga5571fbed2babb0036255d7a4d5e66f6c)
- [flash_copy](P001_Flash公共接口.md#ga847407358a20d3d5918d8ef11657ce2b)

<a id="header-details"></a>

---

[上一章](P008_Flash扩展操作目录.md) · [返回大纲](大纲.md) · [下一章](P010_Flash公共头文件源码.md)
