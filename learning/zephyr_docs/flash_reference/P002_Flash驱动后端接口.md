---
id: learning.zephyr-docs.flash-reference.page-2
title: Flash驱动后端接口
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__flash__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Flash驱动后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__interface__backend.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是闪存（Flash）应用程序接口（Application Programming Interface，API）参考。先读[Flash概述](../hardware/P012_Flash闪存.md)理解设备偏移，再按[本册大纲](大纲.md)区分应用接口、驱动后端（Driver Backend）、页布局（Page Layout）和扩展操作。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

<a id="details"></a>

本组包含实现 Flash 驱动所需的 API 类型定义、回调签名和其他辅助声明。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_flash_5Fdriver_5Fapi"></a>

```c
struct flash_driver_api
```

相关声明：[flash_driver_api](P007_Flash驱动操作结构.md)。

驱动操作（Driver Operations）：Flash 驱动的操作集合。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.2\_类型定义（Typedefs）

<a id="r_ga358404d040b7ef30c8d24106e97bc290"></a>

```c
typedef int(* flash_api_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[flash_api_read](#ga358404d040b7ef30c8d24106e97bc290)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

闪存读取实现的处理函数类型。

<a id="r_gaf6b0c3aa2b6514ac8936aa0c7fda96ba"></a>

```c
typedef int(* flash_api_write) (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[flash_api_write](#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

闪存写入实现的处理函数类型。

<a id="r_ga2178a2338e652396ba9811ca449f4cb5"></a>

```c
typedef int(* flash_api_erase) (const struct device *dev, off_t offset, size_t size)
```

相关声明：[flash_api_erase](#ga2178a2338e652396ba9811ca449f4cb5)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

闪存擦除实现的处理函数类型。

<a id="r_ga97ab6540136589aaafbe049cf4302285"></a>

```c
typedef int(* flash_api_get_size) (const struct device *dev, uint64_t *size)
```

相关声明：[flash_api_get_size](#ga97ab6540136589aaafbe049cf4302285)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

取得以字节为单位的设备容量。

<a id="r_ga2dee3874cb1be4ef4dab599963c30e70"></a>

```c
typedef const struct flash_parameters *(* flash_api_get_parameters) (const struct device *dev)
```

相关声明：[flash_parameters](P004_Flash存储参数结构.md)、[flash_api_get_parameters](#ga2dee3874cb1be4ef4dab599963c30e70)、[device](../device_reference/P002_设备对象结构.md)。

取得设备参数。

<a id="r_ga7576411536217c9ec3e167e7a5ca82a5"></a>

```c
typedef void(* flash_api_pages_layout) (const struct device *dev, const struct flash_pages_layout **layout, size_t *layout_size)
```

相关声明：[flash_api_pages_layout](#ga7576411536217c9ec3e167e7a5ca82a5)、[device](../device_reference/P002_设备对象结构.md)、[flash_pages_layout](P006_Flash页布局结构.md)。

取得闪存设备的布局（Layout）。

<a id="r_gac7b802015885044df6a1872513b89ab5"></a>

```c
typedef int(* flash_api_sfdp_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[flash_api_sfdp_read](#gac7b802015885044df6a1872513b89ab5)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

从串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）区域读取数据。

<a id="r_ga088369ef7593aa7c1fbe4cdad6e5b994"></a>

```c
typedef int(* flash_api_read_jedec_id) (const struct device *dev, uint8_t *id)
```

相关声明：[flash_api_read_jedec_id](#ga088369ef7593aa7c1fbe4cdad6e5b994)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取设备的 JEDEC 标识。

<a id="r_gacff972cc16c1afa0a85e3118eff0afb2"></a>

```c
typedef int(* flash_api_ex_op) (const struct device *dev, uint16_t code, const uintptr_t in, void *out)
```

相关声明：[flash_api_ex_op](#gacff972cc16c1afa0a85e3118eff0afb2)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)。

执行扩展操作。

## 2.3\_详细说明（Detailed Documentation）

<a id="ga2178a2338e652396ba9811ca449f4cb5"></a>

### `flash_api_erase`

```c
typedef int(* flash_api_erase) (const struct device *dev, off_t offset, size_t size)
```

```c
#include <zephyr/drivers/flash.h>
```

闪存擦除实现的处理函数类型。

对于设计上不需要擦除的非易失性 RAM 设备，此回调是可选的。如果回调能提高设备效率，或者设备支持驱动擦除实现可以利用的内部填充操作，也可以提供此回调。

**说明（Note）**：必要的擦除保护管理必须由驱动完成。无论操作成功还是失败，驱动都必须确保操作结束后的擦除保护状态与操作开始时一致。

<a id="gacff972cc16c1afa0a85e3118eff0afb2"></a>

### `flash_api_ex_op`

```c
typedef int(* flash_api_ex_op) (const struct device *dev, uint16_t code, const uintptr_t in, void *out)
```

```c
#include <zephyr/drivers/flash.h>
```

执行扩展操作。

参数说明见 `flash_ex_op()`。

<a id="ga2dee3874cb1be4ef4dab599963c30e70"></a>

### `flash_api_get_parameters`

```c
typedef const struct flash_parameters *(* flash_api_get_parameters) (const struct device *dev)
```

```c
#include <zephyr/drivers/flash.h>
```

取得设备参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 闪存设备。 |

**返回（Returns）**：返回指向保存设备参数的 Flash 参数结构体的指针。

<a id="ga97ab6540136589aaafbe049cf4302285"></a>

### `flash_api_get_size`

```c
typedef int(* flash_api_get_size) (const struct device *dev, uint64_t *size)
```

```c
#include <zephyr/drivers/flash.h>
```

取得以字节为单位的设备容量。

返回设备总逻辑容量，单位为字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 闪存设备。 |
| `[out] size` | 设备容量，单位为字节。 |

**返回（Returns）**：成功返回 0，出错时返回负的 errno 错误码。

<a id="ga7576411536217c9ec3e167e7a5ca82a5"></a>

### `flash_api_pages_layout`

```c
typedef void(* flash_api_pages_layout) (const struct device *dev, const struct flash_pages_layout **layout, size_t *layout_size)
```

```c
#include <zephyr/drivers/flash.h>
```

取得闪存设备的布局（Layout）。

Flash 设备布局是对设备各页的游程编码（Run-length Encoding）描述。这里的“页”指闪存设备上最小的可擦除区域。

对于所有页大小一致的闪存，返回长度为 1 的数组，由该元素说明页大小及存储器中的页数量。

对于页大小不一致的闪存，返回包含多个元素的数组，每个元素描述一组大小相同的页。数组元素顺序表示这些页组在设备上的排列顺序。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要查询布局的闪存设备。 |
| `layout` | 通过此参数返回 Flash 布局。 |
| `layout_size` | 返回布局数组的元素数量。 |

> 译注——源码核对：layout_size 是布局数组元素数量，不是总页数。总页数为各元素 pages_count 之和；页大小描述擦除粒度，不应与最小写入块大小或串行器件的编程页大小混用。

<a id="ga358404d040b7ef30c8d24106e97bc290"></a>

### `flash_api_read`

```c
typedef int(* flash_api_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

```c
#include <zephyr/drivers/flash.h>
```

闪存读取实现的处理函数类型。

为使不同实现的行为一致，应先检查 `len` 是否等于 0；若为 0，立即返回 0；仅在非零时继续校验数据目标指针。

**返回（Returns）**：成功或 `len` 为零时返回 0；页偏移不存在或数据目标为 `NULL` 时返回 `-EINVAL`。

**说明（Note）**：必要的读取保护管理必须由驱动完成。

<a id="ga088369ef7593aa7c1fbe4cdad6e5b994"></a>

### `flash_api_read_jedec_id`

```c
typedef int(* flash_api_read_jedec_id) (const struct device *dev, uint8_t *id)
```

```c
#include <zephyr/drivers/flash.h>
```

读取设备的 JEDEC 标识。

参数说明见 `flash_read_jedec_id()`。

<a id="gac7b802015885044df6a1872513b89ab5"></a>

### `flash_api_sfdp_read`

```c
typedef int(* flash_api_sfdp_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

```c
#include <zephyr/drivers/flash.h>
```

从串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）区域读取数据。

参数说明见 `flash_sfdp_read()`。

<a id="gaf6b0c3aa2b6514ac8936aa0c7fda96ba"></a>

### `flash_api_write`

```c
typedef int(* flash_api_write) (const struct device *dev, off_t offset, const void *data, size_t len)
```

```c
#include <zephyr/drivers/flash.h>
```

闪存写入实现的处理函数类型。

**说明（Note）**：必要的写保护管理必须由驱动完成。无论操作成功还是失败，驱动都必须确保操作结束后的写保护状态与操作开始时一致。

## 2.4\_源码定位与版本边界

这些接口定义在 [flash.h](../../../include/zephyr/drivers/flash.h)，辅助操作与页遍历分别见 [flash_util.c](../../../drivers/flash/flash_util.c) 和 [flash_page_layout.c](../../../drivers/flash/flash_page_layout.c)。仓库相对链接供跟踪，不能自动视为与网页同版本。译注核对了本次读取的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash.h)、[辅助实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_util.c)与[页布局实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_page_layout.c)，三份源码摘要单独记录；main 和 latest 都会滚动更新。本批只翻译和核对源码，没有构建、擦写存储或实板验证。

> 译注——条件声明与展示：本次API网页列出九个后端操作类型和九个驱动成员；[官方源码浏览译文](P010_Flash公共头文件源码.md)同时包含CONFIG_FLASH_HAS_DRIVER_FILL条件下的flash_api_fill与fill。去掉注释和展示空白后，该源码页与本次读取的main头文件代码一致，因此不能将API摘要未展示fill归因于版本不同。应按实际编译配置判断成员是否存在。

## 2.5\_原页交叉引用（Cross References）

- [flash_driver_api](P007_Flash驱动操作结构.md)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [flash_parameters](P004_Flash存储参数结构.md)
- [flash_pages_layout](P006_Flash页布局结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [zephyr/drivers/flash.h](P009_Flash公共头文件参考.md)
- [flash_ex_op()](P001_Flash公共接口.md#ga5571fbed2babb0036255d7a4d5e66f6c)
- [flash_read_jedec_id()](P001_Flash公共接口.md#gadb273ed317e1088b57adcac3385f50a7)
- [flash_sfdp_read()](P001_Flash公共接口.md#ga8e9b921299bfb059bf72445a2ffa5a97)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P001_Flash公共接口.md) · [返回大纲](大纲.md) · [下一章](P003_Flash内部接口.md)
