---
id: learning.zephyr-docs.flash-reference.page-1
title: Flash公共接口
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__flash__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Flash公共接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__interface.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是闪存（Flash）应用程序接口（Application Programming Interface，API）参考。先读[Flash概述](../hardware/P012_Flash闪存.md)理解设备偏移，再按[本册大纲](大纲.md)区分应用接口、驱动后端（Driver Backend）、页布局（Page Layout）和扩展操作。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

闪存控制器（Flash Memory Controller）的接口。

<a id="details"></a>

闪存控制器（Flash Memory Controller）的接口。自 Zephyr 1.2 引入；接口版本为 1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_flash_5Fex_5Fop"></a>

相关声明：[扩展操作（Extended Operations）](P008_Flash扩展操作目录.md)。

闪存驱动的厂商专用扩展操作（Vendor-specific Extended Operations）。

<a id="r_flash_5Finterface_5Fbackend"></a>

相关声明：[Flash 驱动后端接口（Backend API）](P002_Flash驱动后端接口.md)。



<a id="r_flash_5Finternal_5Finterface"></a>

相关声明：[Flash 内部接口（Internal Interfaces）](P003_Flash内部接口.md)。

闪存控制器的内部接口（Internal Interfaces）。

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_flash_2Eh"></a>

```c
file flash.h
```

相关声明：[flash.h](P009_Flash公共头文件参考.md)。

Flash 驱动应用程序接口（Application Programming Interface，API）的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.3\_数据结构（Data Structures）

<a id="r_flash_5Fparameters"></a>

```c
struct flash_parameters
```

相关声明：[flash_parameters](P004_Flash存储参数结构.md)。

闪存参数（Flash Memory Parameters）。

<a id="r_flash_5Fpages_5Finfo"></a>

```c
struct flash_pages_info
```

相关声明：[flash_pages_info](P005_Flash页信息结构.md)。

闪存页的信息（Flash Page Information）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.4\_宏定义（Macros）

<a id="r_ga760f7d79cb9f23bc0326abfea85808aa"></a>

```c
#define FLASH_ERASE_C_EXPLICIT 0x01
```

相关声明：[FLASH_ERASE_C_EXPLICIT](#ga760f7d79cb9f23bc0326abfea85808aa)。

用于普通 Flash：写入任意数据前需要擦除时设置此标志。

<a id="r_ga82adeb566049cfbbced1c50db5d17760"></a>

```c
#define FLASH_ERASE_CAPS_UNSET (int)-1
```

相关声明：[FLASH_ERASE_CAPS_UNSET](#ga82adeb566049cfbbced1c50db5d17760)。

保留供使用者初始化变量；该变量之后用于保存能力信息（Capabilities）。

<a id="r_ga37f63f7c484ae89c9a133fbe2616a8ea"></a>

```c
#define FLASH_ERASE_C_SUPPORTED 0x02
```

相关声明：[FLASH_ERASE_C_SUPPORTED](#ga37f63f7c484ae89c9a133fbe2616a8ea)。

保留，尚未使用。

<a id="r_gaf0257b23bbe071c5b1e0294e7d31fca4"></a>

```c
#define FLASH_ERASE_C_VAL_BIT 0x04
```

相关声明：[FLASH_ERASE_C_VAL_BIT](#gaf0257b23bbe071c5b1e0294e7d31fca4)。

保留，尚未使用。

<a id="r_ga6dc21974c3db6b5b7a69cdfb170b2c06"></a>

```c
#define FLASH_ERASE_UNIFORM_PAGE 0x08
```

相关声明：[FLASH_ERASE_UNIFORM_PAGE](#ga6dc21974c3db6b5b7a69cdfb170b2c06)。

保留，尚未使用。

<a id="r_ga67418b2d5cbbec83463dce3d426162e3"></a>

```c
#define FLASH_EX_OP_VENDOR_BASE 0x8000
```

相关声明：[FLASH_EX_OP_VENDOR_BASE](#ga67418b2d5cbbec83463dce3d426162e3)。

厂商专用扩展操作码范围的起始值。

<a id="r_gafc0aa899b7ea452d048d8ee67d2e6f06"></a>

```c
#define FLASH_EX_OP_IS_VENDOR(c)
```

相关声明：[FLASH_EX_OP_IS_VENDOR](#gafc0aa899b7ea452d048d8ee67d2e6f06)。

检查扩展操作码是否属于厂商专用范围。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.5\_类型定义（Typedefs）

<a id="r_ga41bfc5eb05a8e73873763c36f3e1ec6f"></a>

```c
typedef bool(* flash_page_cb) (const struct flash_pages_info *info, void *data)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[flash_page_cb](#ga41bfc5eb05a8e73873763c36f3e1ec6f)、[flash_pages_info](P005_Flash页信息结构.md)。

遍历设备上各闪存页时使用的回调（Callback）类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.6\_枚举（Enumerations）

<a id="r_gae401e7b13d22a0f405e8d2ca0ef33c51"></a>

```c
enum flash_ex_op_types { FLASH_EX_OP_RESET = 0 , FLASH_EX_OP_IS_BAD_BLOCK = 1 , FLASH_EX_OP_MARK_BAD_BLOCK = 2 }
```

相关声明：[flash_ex_op_types](#gae401e7b13d22a0f405e8d2ca0ef33c51)、[FLASH_EX_OP_RESET](#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd)、[FLASH_EX_OP_IS_BAD_BLOCK](#ggae401e7b13d22a0f405e8d2ca0ef33c51a56ea1df211a928c8bd2ade61df9cce34)、[FLASH_EX_OP_MARK_BAD_BLOCK](#ggae401e7b13d22a0f405e8d2ca0ef33c51a22b688ac088aead1f989ecb656fc7342)。

额外闪存操作的枚举（Enumeration）。

<a id="r_ga8eeb7135fbe276e7c287d895a91c6116"></a>

```c
enum flash_block_status { FLASH_BLOCK_GOOD = 0 , FLASH_BLOCK_BAD = 1 }
```

相关声明：[flash_block_status](#ga8eeb7135fbe276e7c287d895a91c6116)、[FLASH_BLOCK_GOOD](#gga8eeb7135fbe276e7c287d895a91c6116a1974162ef10f5b83bb8428e3c7c513c7)、[FLASH_BLOCK_BAD](#gga8eeb7135fbe276e7c287d895a91c6116a398def014a3982b35e4557f93bfa44bb)。

闪存块状态（Block Status）的枚举。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.7\_函数（Functions）

<a id="r_gabc73e8888dcb8f4f79cd80b8d02a6a2c"></a>

```c
static int flash_params_get_erase_cap (const struct flash_parameters *p)
```

相关声明：[flash_params_get_erase_cap](#gabc73e8888dcb8f4f79cd80b8d02a6a2c)、[flash_parameters](P004_Flash存储参数结构.md)。

解析 `flash_parameters`，取得擦除能力（Erase Capabilities）。

<a id="r_ga1649b22ba5c5974060b4a3c44a0e44e2"></a>

```c
static bool flash_params_erase_value_readable (const struct flash_parameters *p)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[flash_params_erase_value_readable](#ga1649b22ba5c5974060b4a3c44a0e44e2)、[flash_parameters](P004_Flash存储参数结构.md)。

检查已擦除区域是否能读回擦除值（Erase Value）。

<a id="r_gaa7c9382796aad64da0da683f54600b5f"></a>

```c
int flash_read (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[flash_read](#gaa7c9382796aad64da0da683f54600b5f)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

从闪存读取数据。

<a id="r_ga76d7880cc5e18ca40237736d3bd94324"></a>

```c
int flash_write (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[flash_write](#ga76d7880cc5e18ca40237736d3bd94324)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

将缓冲区内容写入闪存。

<a id="r_ga05f9c8b0c1ff7273f71797e7ff799c95"></a>

```c
int flash_erase (const struct device *dev, off_t offset, size_t size)
```

相关声明：[flash_erase](#ga05f9c8b0c1ff7273f71797e7ff799c95)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

擦除部分或全部闪存。

<a id="r_ga471edb53a2b1abe3dff0f4e2d216521e"></a>

```c
int flash_get_size (const struct device *dev, uint64_t *size)
```

相关声明：[flash_get_size](#ga471edb53a2b1abe3dff0f4e2d216521e)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

取得以字节为单位的设备容量。

<a id="r_ga022838332e905b0111d5136dd963889b"></a>

```c
int flash_fill (const struct device *dev, uint8_t val, off_t offset, size_t size)
```

相关声明：[flash_fill](#ga022838332e905b0111d5136dd963889b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

用指定值填充设备的选定范围。

<a id="r_ga11eda0cdc7be12636a90d2e8c7264e4a"></a>

```c
int flash_flatten (const struct device *dev, off_t offset, size_t size)
```

相关声明：[flash_flatten](#ga11eda0cdc7be12636a90d2e8c7264e4a)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

擦除部分或全部闪存，或将该区域填平为统一值。

<a id="r_gafc959b0363eb27d6a3237e4288d60979"></a>

```c
int flash_get_page_info_by_offs (const struct device *dev, off_t offset, struct flash_pages_info *info)
```

相关声明：[flash_get_page_info_by_offs](#gafc959b0363eb27d6a3237e4288d60979)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[flash_pages_info](P005_Flash页信息结构.md)。

取得指定闪存偏移所处页的大小和起始偏移。

<a id="r_gaae733082fa92f80261d5895d3f81a98b"></a>

```c
int flash_get_page_info_by_idx (const struct device *dev, uint32_t page_index, struct flash_pages_info *info)
```

相关声明：[flash_get_page_info_by_idx](#gaae733082fa92f80261d5895d3f81a98b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flash_pages_info](P005_Flash页信息结构.md)。

取得指定索引的闪存页大小和起始偏移。

<a id="r_gaf750fe20c02758be7e37f36d2d16345e"></a>

```c
size_t flash_get_page_count (const struct device *dev)
```

相关声明：[flash_get_page_count](#gaf750fe20c02758be7e37f36d2d16345e)、[device](../device_reference/P002_设备对象结构.md)。

取得闪存页总数。

<a id="r_ga275f2346e88b5e4d050dae426f0953fe"></a>

```c
void flash_page_foreach (const struct device *dev, flash_page_cb cb, void *data)
```

相关声明：[flash_page_foreach](#ga275f2346e88b5e4d050dae426f0953fe)、[device](../device_reference/P002_设备对象结构.md)、[flash_page_cb](#ga41bfc5eb05a8e73873763c36f3e1ec6f)。

遍历设备上的所有闪存页。

<a id="r_ga8e9b921299bfb059bf72445a2ffa5a97"></a>

```c
int flash_sfdp_read (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[flash_sfdp_read](#ga8e9b921299bfb059bf72445a2ffa5a97)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

从串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）区域读取数据。

<a id="r_gadb273ed317e1088b57adcac3385f50a7"></a>

```c
int flash_read_jedec_id (const struct device *dev, uint8_t *id)
```

相关声明：[flash_read_jedec_id](#gadb273ed317e1088b57adcac3385f50a7)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从兼容的闪存设备读取 JEDEC 标识（JEDEC ID）。

<a id="r_gaadfb323bc1b4efa39e7bc0a048c472a6"></a>

```c
size_t flash_get_write_block_size (const struct device *dev)
```

相关声明：[flash_get_write_block_size](#gaadfb323bc1b4efa39e7bc0a048c472a6)、[device](../device_reference/P002_设备对象结构.md)。

取得驱动支持的最小写入块大小（Minimum Write Block Size）。

<a id="r_ga07b516708224b7a69a5169ef9c5c26e3"></a>

```c
const struct flash_parameters * flash_get_parameters (const struct device *dev)
```

相关声明：[flash_parameters](P004_Flash存储参数结构.md)、[flash_get_parameters](#ga07b516708224b7a69a5169ef9c5c26e3)、[device](../device_reference/P002_设备对象结构.md)。

取得指向 `flash_parameters` 结构体的指针。

<a id="r_ga5571fbed2babb0036255d7a4d5e66f6c"></a>

```c
int flash_ex_op (const struct device *dev, uint16_t code, const uintptr_t in, void *out)
```

相关声明：[flash_ex_op](#ga5571fbed2babb0036255d7a4d5e66f6c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)。

在指定设备上执行闪存扩展操作（Extended Operation）。

<a id="r_ga847407358a20d3d5918d8ef11657ce2b"></a>

```c
int flash_copy (const struct device *src_dev, off_t src_offset, const struct device *dst_dev, off_t dst_offset, off_t size, uint8_t *buf, size_t buf_size)
```

相关声明：[flash_copy](#ga847407358a20d3d5918d8ef11657ce2b)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将闪存内容从一个设备复制到另一个设备。

## 1.8\_详细说明（Detailed Documentation）

<a id="ga760f7d79cb9f23bc0326abfea85808aa"></a>

### `FLASH_ERASE_C_EXPLICIT`

```c
#define FLASH_ERASE_C_EXPLICIT 0x01
```

```c
#include <zephyr/drivers/flash.h>
```

用于普通 Flash：写入任意数据前需要擦除时设置此标志。

<a id="ga37f63f7c484ae89c9a133fbe2616a8ea"></a>

### `FLASH_ERASE_C_SUPPORTED`

```c
#define FLASH_ERASE_C_SUPPORTED 0x02
```

```c
#include <zephyr/drivers/flash.h>
```

保留，尚未使用。

<a id="gaf0257b23bbe071c5b1e0294e7d31fca4"></a>

### `FLASH_ERASE_C_VAL_BIT`

```c
#define FLASH_ERASE_C_VAL_BIT 0x04
```

```c
#include <zephyr/drivers/flash.h>
```

保留，尚未使用。

<a id="ga82adeb566049cfbbced1c50db5d17760"></a>

### `FLASH_ERASE_CAPS_UNSET`

```c
#define FLASH_ERASE_CAPS_UNSET (int)-1
```

```c
#include <zephyr/drivers/flash.h>
```

保留供使用者初始化变量；该变量之后用于保存能力信息（Capabilities）。

<a id="ga6dc21974c3db6b5b7a69cdfb170b2c06"></a>

### `FLASH_ERASE_UNIFORM_PAGE`

```c
#define FLASH_ERASE_UNIFORM_PAGE 0x08
```

```c
#include <zephyr/drivers/flash.h>
```

保留，尚未使用。

<a id="gafc0aa899b7ea452d048d8ee67d2e6f06"></a>

### `FLASH_EX_OP_IS_VENDOR`

```c
#define FLASH_EX_OP_IS_VENDOR ( c)
```

```c
#include <zephyr/drivers/flash.h>
```

展开值（Value）：

```c
((c) & FLASH_EX_OP_VENDOR_BASE)
```

检查扩展操作码是否属于厂商专用范围。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `c` | 扩展操作码。 |

**返回（Returns）**：操作码在厂商专用范围内时返回非零值，否则返回 0。

<a id="ga67418b2d5cbbec83463dce3d426162e3"></a>

### `FLASH_EX_OP_VENDOR_BASE`

```c
#define FLASH_EX_OP_VENDOR_BASE 0x8000
```

```c
#include <zephyr/drivers/flash.h>
```

厂商专用扩展操作码范围的起始值。

<a id="ga41bfc5eb05a8e73873763c36f3e1ec6f"></a>

### `flash_page_cb`

```c
typedef bool(* flash_page_cb) (const struct flash_pages_info *info, void *data)
```

```c
#include <zephyr/drivers/flash.h>
```

遍历设备上各闪存页时使用的回调（Callback）类型。

回调应返回 `true` 继续遍历，返回 `false` 停止遍历。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `info` | 当前页的信息。 |
| `data` | 提供给回调的私有数据（Private Data）。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_PAGE_LAYOUT` 时可用。

**返回（Returns）**：返回 `true` 继续遍历，返回 `false` 停止遍历。

**参阅（See Also）**：参见 `flash_page_foreach()`。

<a id="ga8eeb7135fbe276e7c287d895a91c6116"></a>

### `flash_block_status`

```c
enum flash_block_status
```

```c
#include <zephyr/drivers/flash.h>
```

闪存块状态（Block Status）的枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_BLOCK_GOOD` | 该块功能正常。 |
| `FLASH_BLOCK_BAD` | 该块已被标记为坏块（Bad Block）。 |

<a id="gae401e7b13d22a0f405e8d2ca0ef33c51"></a>

### `flash_ex_op_types`

```c
enum flash_ex_op_types
```

```c
#include <zephyr/drivers/flash.h>
```

额外闪存操作的枚举（Enumeration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_EX_OP_RESET` | 复位闪存设备。 |
| `FLASH_EX_OP_IS_BAD_BLOCK` | 检查某个块是否已标记为坏块。输入为指向块地址的指针（`off_t *`）；输出通过 `enum flash_block_status *` 返回 `flash_block_status`。 |
| `FLASH_EX_OP_MARK_BAD_BLOCK` | 将某个块标记为坏块。输入为指向块地址的指针（`off_t *`），没有输出。 |

<a id="ga847407358a20d3d5918d8ef11657ce2b"></a>

### `flash_copy()`

```c
int flash_copy ( const struct device * src_dev, off_t src_offset, const struct device * dst_dev, off_t dst_offset, off_t size, uint8_t * buf, size_t buf_size )
```

```c
#include <zephyr/drivers/flash.h>
```

将闪存内容从一个设备复制到另一个设备。

将一个位置的闪存区域复制到另一个位置。源设备与目标设备可以相同，也可以不同。但如果是同一设备，且源、目标内存区域相互重叠而又不完全相同，本函数会失败。

调用者必须提供大小合适的缓冲区；若设备需要预先擦除，还必须确保目标区域已擦除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` src_dev` | 源闪存设备。 |
| ` dst_dev` | 目标闪存设备。 |
| ` src_offset` | 源闪存设备内的偏移。 |
| ` dst_offset` | 目标闪存设备内的偏移。 |
| ` size` | 待复制区域的大小，单位为字节。 |
| `[out] buf` | 指向大小为 `buf_size` 的缓冲区的指针。 |
| ` buf_size` | `buf` 所指向缓冲区的大小。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 参数无效。 |
| `-EIO` | 发生输入输出（Input/Output，I/O）错误。 |
| `-ENODEV` | `src_dev` 或 `dst_dev` 尚未就绪。 |

**说明（Note）**：如果源设备与目标设备相同，且源偏移与目标偏移也相同，本函数成功返回，不执行任何复制。

> 译注——源码核对：本次核对的 flash_util.c 要求 buf_size 不小于目标写入块大小，且是其整数倍；同设备同偏移的快速成功也在基础参数检查之后。该源码在末尾剩余字节少于写入块时，将读写长度提升到至少一个写入块，并用该长度执行 flash_read 和 flash_write，因此可能访问请求 size 之外的字节；复制长度不是块大小整数倍时必须核对目标版本及区域边界，不能仅凭函数名假定它严格只访问 size 字节。此处记录源码行为，未执行擦写。

<a id="ga05f9c8b0c1ff7273f71797e7ff799c95"></a>

### `flash_erase()`

```c
int flash_erase ( const struct device * dev, off_t offset, size_t size )
```

```c
#include <zephyr/drivers/flash.h>
```

擦除部分或全部闪存。

可接受的擦除大小和偏移受具体硬件的页大小、偏移倍数要求约束。请检查底层子驱动实现的 API；例如，在闪存驱动支持时，可使用 `flash_get_page_info_by_offs()` 查询。

必要的擦除保护管理由驱动的擦除实现自行完成。

本函数只应用于真正需要显式擦除（Explicit Erase）的设备。如果代码依赖在某些操作前将设备设为擦除值，又需要兼容显式擦除设备和非易失性 RAM 设备，应改用 `flash_flatten`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |
| `offset` | 擦除区域的起始偏移。 |
| `size` | 待擦除区域的大小。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

**参阅（See Also）**：参见 `flash_flatten()`、`flash_get_page_info_by_offs()` 和 `flash_get_page_info_by_idx()`。

<a id="ga5571fbed2babb0036255d7a4d5e66f6c"></a>

### `flash_ex_op()`

```c
int flash_ex_op ( const struct device * dev, uint16_t code, const uintptr_t in, void * out )
```

```c
#include <zephyr/drivers/flash.h>
```

在指定设备上执行闪存扩展操作（Extended Operation）。

除了写入、擦除等标准操作，闪存控制器还可能支持写保护（Write Protection）、读出保护（Readout Protection）等附加功能。这些功能并非每个控制器都有，各控制器的实现方式也可能不同。

为每项控制器功能单独增加一个 Flash API 并不合适：某项功能可能只在少数控制器上存在，或者同一个 API 无法表达所有控制器对该功能的不同实现。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |
| `code` | 将在设备上执行的操作。 |
| `in` | 指向操作所需输入数据的指针；操作不需要输入数据时可以为 `NULL`。 |
| `out` | 指向操作输出数据的指针；操作不产生输出时可以为 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 指定设备不支持扩展操作。 |
| `-ENOSYS` | Kconfig 中未启用扩展操作支持。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_EX_OP_ENABLED` 时可用。

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误值。

> 译注——源码核对：参数原型中的 in 是 uintptr_t 整数类型，原文则按“输入指针”描述其用途；传递结构体地址时需按具体操作约定转成 uintptr_t，无输入时使用 0。仅启用 CONFIG_FLASH_EX_OP_ENABLED 不代表驱动支持每一种操作，应检查返回码与厂商扩展定义。

<a id="ga022838332e905b0111d5136dd963889b"></a>

### `flash_fill()`

```c
int flash_fill ( const struct device * dev, uint8_t val, off_t offset, size_t size )
```

```c
#include <zephyr/drivers/flash.h>
```

用指定值填充设备的选定范围。

此辅助函数用指定值填充设备上的指定范围。范围的偏移和大小都必须按设备的写入块大小对齐（Alignment）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |
| `val` | 用于填充该范围的值。 |
| `offset` | 待填充范围的偏移。 |
| `size` | 范围大小。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

> 译注——源码核对：当前 main 分支还支持 CONFIG_FLASH_HAS_DRIVER_FILL 下的驱动 fill 回调，否则根据 CONFIG_FLASH_FILL_GENERIC_IMPLEMENTATION 使用分块写入回退；没有可用实现时返回 -ENOTSUP。官方源码浏览页也包含此条件声明；API参考未列出该回调属于展示范围差异，不能仅据此判断版本不同。完整条件见[源码浏览译文](P010_Flash公共头文件源码.md)。

<a id="ga11eda0cdc7be12636a90d2e8c7264e4a"></a>

### `flash_flatten()`

```c
int flash_flatten ( const struct device * dev, off_t offset, size_t size )
```

```c
#include <zephyr/drivers/flash.h>
```

擦除部分或全部闪存，或将该区域填平为统一值。

如果设备属于显式擦除类型，或驱动提供了擦除回调，就调用设备的擦除回调，行为与 `flash_erase` 相同。如果设备不要求显式擦除——可能完全无需擦除，也可能自动擦除或写入时擦除——且未提供擦除回调，则用设备的 `erase_value` 填充选定区域来模拟擦除。

按页组织且需要显式擦除的设备受擦除页偏移和大小约束；没有这类要求的设备可以放宽限制。因此，用户代码必须自行保证参数正确：不满足这些约束时，按页擦除设备返回 `-EINVAL`，非显式擦除设备却可能成功。当前对非易失性 RAM 设备模拟擦除页，是为了让依赖分页设备的代码平滑迁移；这完全是软件约束。

一般而言，如果既有代码必须先擦除设备才能执行后续动作，可将 `flash_erase` 调用替换为本函数。如果代码能直接使用非易失性 RAM 设备、无需模拟擦除，则更适合为 Flash 等按页擦除设备设置单独执行分支，仅在该分支调用 `flash_erase`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |
| `offset` | 擦除区域的起始偏移。 |
| `size` | 待擦除区域的大小。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

**参阅（See Also）**：参见 `flash_erase()`。

> 译注——源码核对：上文按网页快照保留“显式擦除或提供回调”的描述。但本次核对的 main 分支 flash_util.c 只有在启用 CONFIG_FLASH_HAS_EXPLICIT_ERASE、能力包含 FLASH_ERASE_C_EXPLICIT 且 erase 非空时才调用擦除回调；否则在 CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE 分支调用 flash_fill，未启用该分支则返回 -ENOSYS。不能单凭 erase 指针存在推断此版本会调用它。

<a id="gaf750fe20c02758be7e37f36d2d16345e"></a>

### `flash_get_page_count()`

```c
size_t flash_get_page_count ( const struct device * dev)
```

```c
#include <zephyr/drivers/flash.h>
```

取得闪存页总数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_PAGE_LAYOUT` 时可用。

**返回（Returns）**：返回闪存页数量。

<a id="gaae733082fa92f80261d5895d3f81a98b"></a>

### `flash_get_page_info_by_idx()`

```c
int flash_get_page_info_by_idx ( const struct device * dev, uint32_t page_index, struct flash_pages_info * info )
```

```c
#include <zephyr/drivers/flash.h>
```

取得指定索引的闪存页大小和起始偏移。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |
| `page_index` | 页索引（Page Index），从 0 开始计数。 |
| `info` | 待填充的页信息结构体。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_PAGE_LAYOUT` 时可用。

**返回（Returns）**：成功返回 0；指定索引的页不存在时返回 `-EINVAL`。

<a id="gafc959b0363eb27d6a3237e4288d60979"></a>

### `flash_get_page_info_by_offs()`

```c
int flash_get_page_info_by_offs ( const struct device * dev, off_t offset, struct flash_pages_info * info )
```

```c
#include <zephyr/drivers/flash.h>
```

取得指定闪存偏移所处页的大小和起始偏移。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |
| `offset` | 位于该页内的偏移。 |
| `info` | 待填充的页信息结构体。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_PAGE_LAYOUT` 时可用。

**返回（Returns）**：成功返回 0；指定偏移对应的页不存在时返回 `-EINVAL`。

> 译注——源码核对：offset 是相对于该 Flash 设备起点的偏移，只需落在目标页内；不是从该页起点重新计数的偏移，也不是 CPU 内存映射绝对地址。返回的 start_offset 则是该页相对于设备起点的偏移，详见页信息结构。

<a id="ga07b516708224b7a69a5169ef9c5c26e3"></a>

### `flash_get_parameters()`

```c
const struct flash_parameters * flash_get_parameters ( const struct device * dev)
```

```c
#include <zephyr/drivers/flash.h>
```

取得指向 `flash_parameters` 结构体的指针。

无论该结构体定义在 RAM 还是 Flash 中，返回指针所指向的内容都应视为在整个运行期间保持不变。开发者可以缓存该指针，也可以复制结构体内容。

**返回（Returns）**：返回指向该设备特性对应的 `flash_parameters` 结构体的指针。

<a id="ga471edb53a2b1abe3dff0f4e2d216521e"></a>

### `flash_get_size()`

```c
int flash_get_size ( const struct device * dev, uint64_t * size )
```

```c
#include <zephyr/drivers/flash.h>
```

取得以字节为单位的设备容量。

取得设备的总逻辑容量，单位为字节。并非所有设备都支持返回容量，尤其是页布局不均匀或采用存储体（Bank）的设备；此时函数返回 `-ENOTSUP`，用户必须依靠 `CONFIG_FLASH_PAGE_LAYOUT` 启用的 Flash 页布局函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 闪存设备。 |
| `[out] size` | 设备容量，单位为字节。 |

**返回（Returns）**：成功返回 0，出错时返回负的 errno 错误码。

<a id="gaadfb323bc1b4efa39e7bc0a048c472a6"></a>

### `flash_get_write_block_size()`

```c
size_t flash_get_write_block_size ( const struct device * dev)
```

```c
#include <zephyr/drivers/flash.h>
```

取得驱动支持的最小写入块大小（Minimum Write Block Size）。

驱动可能实现写入修改算法（Write-modify Algorithm），因此它支持的写入块大小可能与底层存储器的实际写入块大小不同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |

**返回（Returns）**：返回写入块大小，单位为字节。

<a id="ga275f2346e88b5e4d050dae426f0953fe"></a>

### `flash_page_foreach()`

```c
void flash_page_foreach ( const struct device * dev, flash_page_cb cb, void * data )
```

```c
#include <zephyr/drivers/flash.h>
```

遍历设备上的所有闪存页。

本函数按起始偏移递增的顺序遍历指定设备的全部闪存页。每一页都会调用给定回调，将该页的信息和私有数据对象传给回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 待遍历其各页的设备。 |
| `cb` | 为每个闪存页调用的回调。 |
| `data` | 回调函数的私有数据。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_PAGE_LAYOUT` 时可用。

> 译注——源码核对：核对的 flash_page_layout.c 使用局部 page_info 对象逐页调用回调；如果要在回调结束后保留页信息，应复制字段，不能仅保存 info 指针并假定它长期有效。

<a id="ga1649b22ba5c5974060b4a3c44a0e44e2"></a>

### `flash_params_erase_value_readable()`

```c
bool flash_params_erase_value_readable ( const struct flash_parameters * p)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/flash.h>
```

检查已擦除区域是否能读回擦除值（Erase Value）。

对读取时会转换内容的设备，典型情况是透明解密（Transparent Decryption），本函数返回 `false`：已擦除区域读回的值并非 `flash_parameters.erase_value`。此时存储系统应依赖驱动报告的擦除状态，而不是通过读回擦除值判断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `p` | 指向 `flash_parameters` 类型对象的指针。 |

**返回（Returns）**：已擦除区域能读回 `erase_value` 时返回 `true`，否则返回 `false`。

<a id="gabc73e8888dcb8f4f79cd80b8d02a6a2c"></a>

### `flash_params_get_erase_cap()`

```c
int flash_params_get_erase_cap ( const struct flash_parameters * p)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/flash.h>
```

解析 `flash_parameters`，取得擦除能力（Erase Capabilities）。

解析 `flash_parameters` 对象，返回擦除能力的组合；设备没有擦除能力时返回 0。注意，擦除能力是否可用有时取决于驱动选项：即使硬件提供某项能力，若驱动禁用或未实现该能力，函数仍可能返回 0。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `p` | 指向 `flash_parameters` 类型对象的指针。 |

**返回（Returns）**：返回 0，或 `FLASH_ERASE_C_` 系列能力标志的组合。

<a id="gaa7c9382796aad64da0da683f54600b5f"></a>

### `flash_read()`

```c
int flash_read ( const struct device * dev, off_t offset, void * data, size_t len )
```

```c
#include <zephyr/drivers/flash.h>
```

从闪存读取数据。

所有闪存驱动都支持读取，读取偏移、读取大小及目标地址均无额外对齐限制。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |
| `offset` | 要读取的偏移，以字节对齐。 |
| `data` | 保存读取数据的缓冲区。 |
| `len` | 要读取的字节数。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="gadb273ed317e1088b57adcac3385f50a7"></a>

### `flash_read_jedec_id()`

```c
int flash_read_jedec_id ( const struct device * dev, uint8_t * id )
```

```c
#include <zephyr/drivers/flash.h>
```

从兼容的闪存设备读取 JEDEC 标识（JEDEC ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要从中读取标识的设备。 |
| `id` | 指向至少 3 字节缓冲区的指针，用于保存标识。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 闪存驱动不支持此函数。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_JESD216_API` 时可用。

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误值。

<a id="ga8e9b921299bfb059bf72445a2ffa5a97"></a>

### `flash_sfdp_read()`

```c
int flash_sfdp_read ( const struct device * dev, off_t offset, void * data, size_t len )
```

```c
#include <zephyr/drivers/flash.h>
```

从串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）区域读取数据。

从兼容 JEDEC JESD216 标准的串行闪存设备读取数据；该标准规定了闪存特性的编码方式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要从中读取参数的设备。 |
| `offset` | SFDP 区域中待读取数据的地址。 |
| `data` | 存放读取数据的位置。 |
| `len` | 要读取的数据字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 闪存驱动不支持访问 SFDP。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_FLASH_JESD216_API` 时可用。

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误值。

<a id="ga76d7880cc5e18ca40237736d3bd94324"></a>

### `flash_write()`

```c
int flash_write ( const struct device * dev, off_t offset, const void * data, size_t len )
```

```c
#include <zephyr/drivers/flash.h>
```

将缓冲区内容写入闪存。

所有闪存驱动都支持位于随机存取存储器（Random Access Memory，RAM）或片上系统（System on Chip，SoC）闪存中的源缓冲区，源地址无额外对齐限制。写入大小和偏移必须是驱动所支持最小写入块大小的整数倍。

必要的写保护管理由驱动的写入实现自行完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |
| `offset` | 写入起始偏移。 |
| `data` | 要写入的数据。 |
| `len` | 要写入的字节数。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

## 1.9\_源码定位与版本边界

这些接口定义在 [flash.h](../../../include/zephyr/drivers/flash.h)，辅助操作与页遍历分别见 [flash_util.c](../../../drivers/flash/flash_util.c) 和 [flash_page_layout.c](../../../drivers/flash/flash_page_layout.c)。仓库相对链接供跟踪，不能自动视为与网页同版本。译注核对了本次读取的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash.h)、[辅助实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_util.c)与[页布局实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_page_layout.c)，三份源码摘要单独记录；main 和 latest 都会滚动更新。本批只翻译和核对源码，没有构建、擦写存储或实板验证。

## 1.10\_原页交叉引用（Cross References）

- [扩展操作（Extended Operations）](P008_Flash扩展操作目录.md)
- [Flash 驱动后端接口（Backend API）](P002_Flash驱动后端接口.md)
- [Flash 内部接口（Internal Interfaces）](P003_Flash内部接口.md)
- [flash.h](P009_Flash公共头文件参考.md)
- [flash_parameters](P004_Flash存储参数结构.md)
- [flash_pages_info](P005_Flash页信息结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [CONFIG_FLASH_PAGE_LAYOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_PAGE_LAYOUT)
- [CONFIG_FLASH_EX_OP_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_EX_OP_ENABLED)
- [flash_parameters.erase_value](P004_Flash存储参数结构.md#a218b0cbc797572ce096d0d6f55475ff9)
- [CONFIG_FLASH_JESD216_API](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_JESD216_API)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__flash__interface_html_ga67418b2d5cbbec83463dce3d426162e3"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8eeb7135fbe276e7c287d895a91c6116a1974162ef10f5b83bb8428e3c7c513c7"></a>
<a id="gga8eeb7135fbe276e7c287d895a91c6116a398def014a3982b35e4557f93bfa44bb"></a>
<a id="ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd"></a>
<a id="ggae401e7b13d22a0f405e8d2ca0ef33c51a56ea1df211a928c8bd2ade61df9cce34"></a>
<a id="ggae401e7b13d22a0f405e8d2ca0ef33c51a22b688ac088aead1f989ecb656fc7342"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_Flash驱动后端接口.md)
