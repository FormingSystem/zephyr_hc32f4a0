---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-5
title: 闪存区域接口（flash area Interface）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_闪存区域接口（flash area Interface）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对闪存分区/区域及其驱动的抽象。

<a id="details"></a>

对闪存分区／区域及其驱动的抽象（Flash Partitions/Areas Abstraction）。起始版本（Since）：1.11。接口版本（Version）：1.1.1。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_flash_5Farea"></a>

```c
struct flash_area
```

相关声明：[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

闪存分区（Flash Partition）。

<a id="r_flash_5Fsector"></a>

```c
struct flash_sector
```

相关声明：[flash_sector](../system_service_model_reference/P033_flash_sector_结构体.md)。

用于传递闪存扇区边界（Flash Sector Boundaries）的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga4e63c3b898a43a210bc0298dc7b49c1e"></a>

```c
#define PARTITION_EXISTS(label)
```

相关声明：[PARTITION_EXISTS](#ga4e63c3b898a43a210bc0298dc7b49c1e)。

给定 DTS 节点标签（Node Label）对应的分区存在时，返回非零值。

<a id="r_gabb94759e5717302724f08f90f941a945"></a>

```c
#define FIXED_PARTITION_EXISTS(label)
```

相关声明：[FIXED_PARTITION_EXISTS](#gabb94759e5717302724f08f90f941a945)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_EXISTS()。这里不能使用 __DEPRECATED_MACRO，因为它会导致使用此宏时出现编译器错误。

<a id="r_gafbc907db76aec2702eff9e5265323560"></a>

```c
#define PARTITION_ID(label)
```

相关声明：[PARTITION_ID](#gafbc907db76aec2702eff9e5265323560)。

通过分区 DTS 节点标签获取闪存区域标识符（Flash Area ID）。

<a id="r_ga60d5298007e2ee261b915a110389e76a"></a>

```c
#define FIXED_PARTITION_ID(label)
```

相关声明：[FIXED_PARTITION_ID](#ga60d5298007e2ee261b915a110389e76a)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_ID()。

<a id="r_gaee5fe6581a477b83157d00155e150980"></a>

```c
#define PARTITION_OFFSET(label)
```

相关声明：[PARTITION_OFFSET](#gaee5fe6581a477b83157d00155e150980)。

通过 DTS 节点标签获取分区偏移量（Partition Offset）。

<a id="r_ga9229bc06458c19baf093ced063a9494b"></a>

```c
#define FIXED_PARTITION_OFFSET(label)
```

相关声明：[FIXED_PARTITION_OFFSET](#ga9229bc06458c19baf093ced063a9494b)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_OFFSET()。

<a id="r_gadfe30156a3a50c69e268075d07ef050b"></a>

```c
#define PARTITION_ADDRESS(label)
```

相关声明：[PARTITION_ADDRESS](#gadfe30156a3a50c69e268075d07ef050b)。

通过 DTS 节点标签获取分区地址（Partition Address）。

<a id="r_ga5ac2848ccfcc1425939d76f499756551"></a>

```c
#define FIXED_PARTITION_ADDRESS(label)
```

相关声明：[FIXED_PARTITION_ADDRESS](#ga5ac2848ccfcc1425939d76f499756551)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_ADDRESS()。

<a id="r_ga8c68c5fa266dcc128ee9520c3c57807d"></a>

```c
#define PARTITION_NODE_ADDRESS(node)
```

相关声明：[PARTITION_NODE_ADDRESS](#ga8c68c5fa266dcc128ee9520c3c57807d)。

通过 DTS 节点获取分区地址（Partition Address）。

<a id="r_gaf6121895f4fdd50533762c6aa57cb319"></a>

```c
#define FIXED_PARTITION_NODE_ADDRESS(node)
```

相关声明：[FIXED_PARTITION_NODE_ADDRESS](#gaf6121895f4fdd50533762c6aa57cb319)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_ADDRESS()。

<a id="r_ga28906b4cc8b00f8e055a1d9a082dbb5e"></a>

```c
#define PARTITION_NODE_OFFSET(node)
```

相关声明：[PARTITION_NODE_OFFSET](#ga28906b4cc8b00f8e055a1d9a082dbb5e)。

通过 DTS 节点获取分区偏移量（Partition Offset）。

<a id="r_ga79092c8d0f32aeec69c6a79021d1ab38"></a>

```c
#define FIXED_PARTITION_NODE_OFFSET(label)
```

相关声明：[FIXED_PARTITION_NODE_OFFSET](#ga79092c8d0f32aeec69c6a79021d1ab38)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_OFFSET()。

<a id="r_gab5234434a7f106e4b3f2b79f2087279a"></a>

```c
#define PARTITION_SIZE(label)
```

相关声明：[PARTITION_SIZE](#gab5234434a7f106e4b3f2b79f2087279a)。

获取 DTS 节点标签对应的分区大小（Partition Size）。

<a id="r_ga2dbc50d9f80d7f7c597c75cbd536cd50"></a>

```c
#define FIXED_PARTITION_SIZE(label)
```

相关声明：[FIXED_PARTITION_SIZE](#ga2dbc50d9f80d7f7c597c75cbd536cd50)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_SIZE()。

<a id="r_gabaa4ff45d7ec2c57616b9fb721c0c45c"></a>

```c
#define PARTITION_NODE_SIZE(node)
```

相关声明：[PARTITION_NODE_SIZE](#gabaa4ff45d7ec2c57616b9fb721c0c45c)。

获取 DTS 节点对应的固定分区大小（Fixed-partition Size）。

<a id="r_ga526459438c6de09abb727585d22b7004"></a>

```c
#define FIXED_PARTITION_NODE_SIZE(node)
```

相关声明：[FIXED_PARTITION_NODE_SIZE](#ga526459438c6de09abb727585d22b7004)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_SIZE()。

<a id="r_gacca3f32100a4e46cb7da21ea8bf0782c"></a>

```c
#define FLASH_AREA_DEVICE(label)
```

相关声明：[FLASH_AREA_DEVICE](#gacca3f32100a4e46cb7da21ea8bf0782c)。

获取区域／分区所在设备的设备指针（Device Pointer）。

<a id="r_ga565f24a138c217bdbe8f42afe8b664e0"></a>

```c
#define PARTITION_DEVICE(label)
```

相关声明：[PARTITION_DEVICE](#ga565f24a138c217bdbe8f42afe8b664e0)。

获取区域／分区所在设备的设备指针（Device Pointer）。

<a id="r_ga3c92b6797feb183da38b8b57e77f2d17"></a>

```c
#define FIXED_PARTITION_DEVICE(label)
```

相关声明：[FIXED_PARTITION_DEVICE](#ga3c92b6797feb183da38b8b57e77f2d17)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_DEVICE()。

<a id="r_ga8986be787a0c4d7c35ef835ce91290de"></a>

```c
#define PARTITION_NODE_DEVICE(node)
```

相关声明：[PARTITION_NODE_DEVICE](#ga8986be787a0c4d7c35ef835ce91290de)。

获取区域／分区所在设备的设备指针（Device Pointer）。

<a id="r_gad64fb220f82870acce62661bfa94991a"></a>

```c
#define FIXED_PARTITION_NODE_DEVICE(node)
```

相关声明：[FIXED_PARTITION_NODE_DEVICE](#gad64fb220f82870acce62661bfa94991a)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_DEVICE()。

<a id="r_ga583ab6d0092ce23df436e42c1eeeb6e2"></a>

```c
#define PARTITION_MTD(label)
```

相关声明：[PARTITION_MTD](#ga583ab6d0092ce23df436e42c1eeeb6e2)。

获取区域／分区所在闪存控制器的节点标识符（Node Identifier）。

<a id="r_gaf933ac3bd33006357c8dc0c3b3f5878f"></a>

```c
#define FIXED_PARTITION_MTD(label)
```

相关声明：[FIXED_PARTITION_MTD](#gaf933ac3bd33006357c8dc0c3b3f5878f)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_OFFSET()。

<a id="r_gac6c6b41211ee9bdb154cefdb46214615"></a>

```c
#define PARTITION_NODE_MTD(node)
```

相关声明：[PARTITION_NODE_MTD](#gac6c6b41211ee9bdb154cefdb46214615)。

获取区域／分区所在闪存控制器的节点标识符（Node Identifier）。

<a id="r_ga891d6e60a927f4b5660bcb2966e9bd2b"></a>

```c
#define FIXED_PARTITION_NODE_MTD(node)
```

相关声明：[FIXED_PARTITION_NODE_MTD](#ga891d6e60a927f4b5660bcb2966e9bd2b)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_MTD()。

<a id="r_ga87e1dd8007998ca22d83bf23a9c4a150"></a>

```c
#define PARTITION(label)
```

相关声明：[PARTITION](#ga87e1dd8007998ca22d83bf23a9c4a150)。

通过分区标签（Partition Label）获取 flash_area 对象的指针。

<a id="r_ga5682b688b50fd2cac3c6c8045e64107e"></a>

```c
#define FIXED_PARTITION(label)
```

相关声明：[FIXED_PARTITION](#ga5682b688b50fd2cac3c6c8045e64107e)。

已弃用的宏（Deprecated Macro），请改用 PARTITION()。

<a id="r_ga8f3f3ac80d3858626f05c60aaaec48f7"></a>

```c
#define PARTITION_BY_NODE(node)
```

相关声明：[PARTITION_BY_NODE](#ga8f3f3ac80d3858626f05c60aaaec48f7)。

通过 DTS 中的分区节点（Partition Node）获取 flash_area 对象的指针。

<a id="r_gab51fb05a2cd0666b892d90ccbc9de342"></a>

```c
#define FIXED_PARTITION_BY_NODE(node)
```

相关声明：[FIXED_PARTITION_BY_NODE](#gab51fb05a2cd0666b892d90ccbc9de342)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_OFFSET()。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_gab9d0b43faefa1f25805e7def82819f2c"></a>

```c
typedef void(* flash_area_cb_t) (const struct flash_area *fa, void *user_data)
```

相关声明：[flash_area_cb_t](#gab9d0b43faefa1f25805e7def82819f2c)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

闪存映射遍历回调（Flash Map Iteration Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_ga6fe2593210688eb85e03bea5f96ea2f7"></a>

```c
int flash_area_open (uint8_t id, const struct flash_area **fa)
```

相关声明：[flash_area_open](#ga6fe2593210688eb85e03bea5f96ea2f7)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

从 flash_map 获取分区的闪存区域（Flash Area）。

<a id="r_ga826350cb9176f58fecead9998b79756f"></a>

```c
static void flash_area_close (__unused const struct flash_area *fa)
```

相关声明：[flash_area_close](#ga826350cb9176f58fecead9998b79756f)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

关闭 flash_area。

<a id="r_ga7adf79769378ed468df6d3ffef5e02a9"></a>

```c
static ALWAYS_INLINE bool flash_area_device_is_ready (const struct flash_area *fa)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[flash_area_device_is_ready](#ga7adf79769378ed468df6d3ffef5e02a9)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

验证分配给闪存区域（Flash Area）的设备是否已就绪可用。

<a id="r_ga7c55704b0c0061a4715470676114b127"></a>

```c
int flash_area_read (const struct flash_area *fa, off_t off, void *dst, size_t len)
```

相关声明：[flash_area_read](#ga7c55704b0c0061a4715470676114b127)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

读取闪存区域数据（Flash Area Data）。

<a id="r_gaa56052f8d6bf4f6966752bc21f5cceb8"></a>

```c
int flash_area_write (const struct flash_area *fa, off_t off, const void *src, size_t len)
```

相关声明：[flash_area_write](#gaa56052f8d6bf4f6966752bc21f5cceb8)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

向闪存区域（Flash Area）写入数据。

<a id="r_gaa50bb1b455a9004f9c24e4af9fd74cd7"></a>

```c
int flash_area_copy (const struct flash_area *src_fa, off_t src_off, const struct flash_area *dst_fa, off_t dst_off, off_t len, uint8_t *buf, size_t buf_size)
```

相关声明：[flash_area_copy](#gaa50bb1b455a9004f9c24e4af9fd74cd7)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将闪存内容从一个闪存区域（Flash Area）复制到另一个区域。

<a id="r_gacc5cbff19d23773115f3334f862814d2"></a>

```c
int flash_area_erase (const struct flash_area *fa, off_t off, size_t len)
```

相关声明：[flash_area_erase](#gacc5cbff19d23773115f3334f862814d2)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

擦除闪存区域（Erase Flash Area）。

<a id="r_gafd097d05f5bfe91695bc7793e82cabcd"></a>

```c
int flash_area_flatten (const struct flash_area *fa, off_t off, size_t len)
```

相关声明：[flash_area_flatten](#gafd097d05f5bfe91695bc7793e82cabcd)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

擦除闪存区域，或使用擦除值（Erase-value）填充。

<a id="r_ga13b7294e84544373e97b8c0274859f6e"></a>

```c
uint32_t flash_area_align (const struct flash_area *fa)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flash_area_align](#ga13b7294e84544373e97b8c0274859f6e)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

获取闪存区域的写块大小（Write Block Size）。

<a id="r_ga5c89e0be6c41058beb1c3f87a0c9c94f"></a>

```c
int flash_area_get_sectors (int fa_id, uint32_t *count, struct flash_sector *sectors)
```

相关声明：[flash_area_get_sectors](#ga5c89e0be6c41058beb1c3f87a0c9c94f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flash_sector](../system_service_model_reference/P033_flash_sector_结构体.md)。

获取区域内扇区（Sectors）的信息。

<a id="r_ga12064d388369a504b571e9776201f688"></a>

```c
int flash_area_sectors (const struct flash_area *fa, uint32_t *count, struct flash_sector *sectors)
```

相关声明：[flash_area_sectors](#ga12064d388369a504b571e9776201f688)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flash_sector](../system_service_model_reference/P033_flash_sector_结构体.md)。

获取区域内扇区（Sectors）的信息。

<a id="r_ga34e74955153f8576acdbff1a524f2d37"></a>

```c
void flash_area_foreach (flash_area_cb_t user_cb, void *user_data)
```

相关声明：[flash_area_foreach](#ga34e74955153f8576acdbff1a524f2d37)、[flash_area_cb_t](#gab9d0b43faefa1f25805e7def82819f2c)。

遍历闪存映射（Flash Map）。

<a id="r_ga557d5fd981b0d52d0eb483ab218c497c"></a>

```c
int flash_area_has_driver (const struct flash_area *fa)
```

相关声明：[flash_area_has_driver](#ga557d5fd981b0d52d0eb483ab218c497c)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

检查系统中是否有支持给定闪存区域（Flash Area）的闪存驱动。

<a id="r_ga868a47161b33c99629df600c1d7d9d43"></a>

```c
static const struct device * flash_area_get_device (const struct flash_area *fa)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[flash_area_get_device](#ga868a47161b33c99629df600c1d7d9d43)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

获取给定闪存区域（Flash Area）的驱动。

<a id="r_ga91e8c75b636b6f300207128df8b0ca9a"></a>

```c
static const char * flash_area_label (const struct flash_area *fa)
```

相关声明：[flash_area_label](#ga91e8c75b636b6f300207128df8b0ca9a)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

从设备树（Device Tree）获取 label 属性。

<a id="r_ga1f16d59cecb25c5143c6a923b3b2f466"></a>

```c
uint8_t flash_area_erased_val (const struct flash_area *fa)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flash_area_erased_val](#ga1f16d59cecb25c5143c6a923b3b2f466)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

获取访问任意已擦除闪存字节时应读到的值（Erased Flash Value）。

## 5.5\_详细说明（Detailed Documentation）

<a id="ga5682b688b50fd2cac3c6c8045e64107e"></a>

### `FIXED_PARTITION`

```c
#define FIXED_PARTITION ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION(label) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION()。

<a id="ga5ac2848ccfcc1425939d76f499756551"></a>

### `FIXED_PARTITION_ADDRESS`

```c
#define FIXED_PARTITION_ADDRESS ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_ADDRESS(label) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_ADDRESS()。

<a id="gab51fb05a2cd0666b892d90ccbc9de342"></a>

### `FIXED_PARTITION_BY_NODE`

```c
#define FIXED_PARTITION_BY_NODE ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_BY_NODE(node) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_OFFSET()。

<a id="ga3c92b6797feb183da38b8b57e77f2d17"></a>

### `FIXED_PARTITION_DEVICE`

```c
#define FIXED_PARTITION_DEVICE ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_DEVICE(label) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_DEVICE()。

<a id="gabb94759e5717302724f08f90f941a945"></a>

### `FIXED_PARTITION_EXISTS`

```c
#define FIXED_PARTITION_EXISTS ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_EXISTS(label)
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_EXISTS()。这里不能使用 __DEPRECATED_MACRO，因为它会导致使用此宏时出现编译器错误。

<a id="ga60d5298007e2ee261b915a110389e76a"></a>

### `FIXED_PARTITION_ID`

```c
#define FIXED_PARTITION_ID ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_ID(label) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_ID()。

<a id="gaf933ac3bd33006357c8dc0c3b3f5878f"></a>

### `FIXED_PARTITION_MTD`

```c
#define FIXED_PARTITION_MTD ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_MTD(label) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_OFFSET()。

<a id="gaf6121895f4fdd50533762c6aa57cb319"></a>

### `FIXED_PARTITION_NODE_ADDRESS`

```c
#define FIXED_PARTITION_NODE_ADDRESS ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_NODE_ADDRESS(node) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_ADDRESS()。

<a id="gad64fb220f82870acce62661bfa94991a"></a>

### `FIXED_PARTITION_NODE_DEVICE`

```c
#define FIXED_PARTITION_NODE_DEVICE ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_NODE_DEVICE(node) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_DEVICE()。

<a id="ga891d6e60a927f4b5660bcb2966e9bd2b"></a>

### `FIXED_PARTITION_NODE_MTD`

```c
#define FIXED_PARTITION_NODE_MTD ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_NODE_MTD(node) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_MTD()。

<a id="ga79092c8d0f32aeec69c6a79021d1ab38"></a>

### `FIXED_PARTITION_NODE_OFFSET`

```c
#define FIXED_PARTITION_NODE_OFFSET ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_NODE_OFFSET(label) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_OFFSET()。

<a id="ga526459438c6de09abb727585d22b7004"></a>

### `FIXED_PARTITION_NODE_SIZE`

```c
#define FIXED_PARTITION_NODE_SIZE ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_NODE_SIZE(node) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_SIZE()。

<a id="ga9229bc06458c19baf093ced063a9494b"></a>

### `FIXED_PARTITION_OFFSET`

```c
#define FIXED_PARTITION_OFFSET ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_OFFSET(label) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_OFFSET()。

<a id="ga2dbc50d9f80d7f7c597c75cbd536cd50"></a>

### `FIXED_PARTITION_SIZE`

```c
#define FIXED_PARTITION_SIZE ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_SIZE(label) __DEPRECATED_MACRO
```

已弃用的宏（Deprecated Macro），请改用 PARTITION_SIZE()。

<a id="gacca3f32100a4e46cb7da21ea8bf0782c"></a>

### `FLASH_AREA_DEVICE`

```c
#define FLASH_AREA_DEVICE ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_COMPAT(DT_NODELABEL(label), zephyr_mapped_partition),   \
            (DEVICE_DT_GET(DT_MTD_FROM_MAPPED_PARTITION(                        \
                                DT_NODE_BY_MAPPED_PARTITION_LABEL(label)))),    \
            (DEVICE_DT_GET(DT_MTD_FROM_FIXED_PARTITION(                         \
                                DT_NODE_BY_FIXED_PARTITION_LABEL(label)))))
```

获取区域／分区所在设备的设备指针（Device Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `label` | 分区的设备树节点标签（DTS Node Label）。 |

**返回（Returns）**：返回值（Returns）：`const struct device` 类型的指针。

<a id="ga87e1dd8007998ca22d83bf23a9c4a150"></a>

### `PARTITION`

```c
#define PARTITION ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_BY_NODE(DT_NODELABEL(label))
```

通过分区标签（Partition Label）获取 flash_area 对象的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `label` | 分区的设备树节点标签（DTS Node Label）。 |

**返回（Returns）**：返回值（Returns）：指向表示该分区的 `flash_area` 类型对象的指针。

<a id="gadfe30156a3a50c69e268075d07ef050b"></a>

### `PARTITION_ADDRESS`

```c
#define PARTITION_ADDRESS ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_NODE_ADDRESS(DT_NODELABEL(label))
```

通过 DTS 节点标签获取分区地址（Partition Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `label` | 分区的设备树节点标签（DTS Node Label）。 |

**返回（Returns）**：返回值（Returns）：该分区在设备树（DTS）中定义的地址（Address）。

<a id="ga8f3f3ac80d3858626f05c60aaaec48f7"></a>

### `PARTITION_BY_NODE`

```c
#define PARTITION_BY_NODE ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),  \
            (MAPPED_PARTITION_1(node)),                         \
            (FIXED_PARTITION_1(node)))
```

通过 DTS 中的分区节点（Partition Node）获取 flash_area 对象的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 分区的设备树节点（DTS Node）。 |

**返回（Returns）**：返回值（Returns）：指向表示该分区的 `flash_area` 类型对象的指针。

<a id="ga565f24a138c217bdbe8f42afe8b664e0"></a>

### `PARTITION_DEVICE`

```c
#define PARTITION_DEVICE ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_NODE_DEVICE(DT_NODELABEL(label))
```

获取区域／分区所在设备的设备指针（Device Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `label` | 分区的设备树节点标签（DTS Node Label）。 |

**返回（Returns）**：返回值（Returns）：指向设备（Device）的指针。

<a id="ga4e63c3b898a43a210bc0298dc7b49c1e"></a>

### `PARTITION_EXISTS`

```c
#define PARTITION_EXISTS ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
DT_PARTITION_EXISTS(DT_NODELABEL(label))
```

给定 DTS 节点标签（Node Label）对应的分区存在时，返回非零值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `label` | 设备树节点标签（DTS Node Label）。 |

**返回（Returns）**：返回值（Returns）：分区节点（Partition Node）存在且已启用时为非零；节点不存在、未启用或不是分区时为 0。

<a id="gafbc907db76aec2702eff9e5265323560"></a>

### `PARTITION_ID`

```c
#define PARTITION_ID ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_COMPAT(DT_NODELABEL(label), zephyr_mapped_partition),   \
            (DT_MAPPED_PARTITION_ID(DT_NODELABEL(label))),                      \
            (DT_FIXED_PARTITION_ID(DT_NODELABEL(label))))
```

通过分区 DTS 节点标签获取闪存区域标识符（Flash Area ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `label` | 分区的设备树节点标签（DTS Node Label）。 |

**返回（Returns）**：返回值（Returns）：闪存区域标识符（Flash Area ID）。

<a id="ga583ab6d0092ce23df436e42c1eeeb6e2"></a>

### `PARTITION_MTD`

```c
#define PARTITION_MTD ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_NODE_MTD(DT_NODELABEL(label))
```

获取区域／分区所在闪存控制器的节点标识符（Node Identifier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `label` | 分区的设备树节点标签（DTS Node Label）。 |

**返回（Returns）**：返回值（Returns）：指向设备（Device）的指针。

<a id="ga8c68c5fa266dcc128ee9520c3c57807d"></a>

### `PARTITION_NODE_ADDRESS`

```c
#define PARTITION_NODE_ADDRESS ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),          \
            (DT_MAPPED_PARTITION_ADDR(node)),                           \
            (COND_CODE_1(DT_FIXED_SUBPARTITION_EXISTS(node),            \
                         (DT_FIXED_SUBPARTITION_ADDR(node)),            \
                         (DT_FIXED_PARTITION_ADDR(node)))))
```

通过 DTS 节点获取分区地址（Partition Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 分区的设备树节点（DTS Node）。 |

**返回（Returns）**：返回值（Returns）：该分区在设备树（DTS）中定义的地址（Address）。

<a id="ga8986be787a0c4d7c35ef835ce91290de"></a>

### `PARTITION_NODE_DEVICE`

```c
#define PARTITION_NODE_DEVICE ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),                  \
            (DEVICE_DT_GET(DT_MTD_FROM_MAPPED_PARTITION(node))),                \
            (DEVICE_DT_GET(COND_CODE_1(DT_FIXED_SUBPARTITION_EXISTS(node),      \
                           (DT_MTD_FROM_FIXED_SUBPARTITION(node)),              \
                           (DT_MTD_FROM_FIXED_PARTITION(node))))))
```

获取区域／分区所在设备的设备指针（Device Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 分区的设备树节点（DTS Node）。 |

**返回（Returns）**：返回值（Returns）：指向设备（Device）的指针。

<a id="gac6c6b41211ee9bdb154cefdb46214615"></a>

### `PARTITION_NODE_MTD`

```c
#define PARTITION_NODE_MTD ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),          \
            (DT_MTD_FROM_MAPPED_PARTITION(node)),                       \
            (COND_CODE_1(DT_FIXED_SUBPARTITION_EXISTS(node),            \
                         (DT_MTD_FROM_FIXED_SUBPARTITION(node)),        \
                         (DT_MTD_FROM_FIXED_PARTITION(node)))))
```

获取区域／分区所在闪存控制器的节点标识符（Node Identifier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 分区的设备树节点（DTS Node）。 |

**返回（Returns）**：返回值（Returns）：指向设备（Device）的指针。

<a id="ga28906b4cc8b00f8e055a1d9a082dbb5e"></a>

### `PARTITION_NODE_OFFSET`

```c
#define PARTITION_NODE_OFFSET ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
COND_CASE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),                          \
            (DT_MAPPED_PARTITION_OFFSET(node)),                                         \
            DT_FIXED_SUBPARTITION_EXISTS(node),                                         \
            (DT_PROP_BY_IDX(DT_PARENT(node), reg, 0) + DT_PROP_BY_IDX(node, reg, 0)),   \
            ((DT_PROP_BY_IDX(node, reg, 0))))
```

通过 DTS 节点获取分区偏移量（Partition Offset）。

注意（Note）：仅适用于顶层 `fixed-partitions` 节点、顶层 `fixed-subpartitions` 节点，或一层 `fixed-subpartitions` 节点内部的 `fixed-partitions` 节点；不支持多层 `fixed-subpartitions` 嵌套，但适用于所有 `zephyr,mapped-partition` 节点实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 分区的设备树节点（DTS Node）。 |

**返回（Returns）**：返回值（Returns）：该分区在设备树（DTS）中定义的偏移量（Offset）。

<a id="gabaa4ff45d7ec2c57616b9fb721c0c45c"></a>

### `PARTITION_NODE_SIZE`

```c
#define PARTITION_NODE_SIZE ( node)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
DT_REG_SIZE(node)
```

获取 DTS 节点对应的固定分区大小（Fixed-partition Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 分区的设备树节点（DTS Node）。 |

**返回（Returns）**：返回值（Returns）：该分区在设备树（DTS）中定义的大小（Size）。

<a id="gaee5fe6581a477b83157d00155e150980"></a>

### `PARTITION_OFFSET`

```c
#define PARTITION_OFFSET ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
PARTITION_NODE_OFFSET(DT_NODELABEL(label))
```

通过 DTS 节点标签获取分区偏移量（Partition Offset）。

注意（Note）：仅适用于顶层 `fixed-partitions` 节点、顶层 `fixed-subpartitions` 节点，或一层 `fixed-subpartitions` 节点内部的 `fixed-partitions` 节点；不支持多层 `fixed-subpartitions` 嵌套，但适用于所有 `zephyr,mapped-partition` 节点实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `label` | 分区的设备树节点标签（DTS Node Label）。 |

**返回（Returns）**：返回值（Returns）：该分区在设备树（DTS）中定义的偏移量（Offset）。

<a id="gab5234434a7f106e4b3f2b79f2087279a"></a>

### `PARTITION_SIZE`

```c
#define PARTITION_SIZE ( label)
```

```c
#include <zephyr/storage/flash_map.h>
```

展开值（Value）：

```c
DT_REG_SIZE(DT_NODELABEL(label))
```

获取 DTS 节点标签对应的分区大小（Partition Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `label` | 设备树节点标签（DTS Node Label）。 |

**返回（Returns）**：返回值（Returns）：该分区在设备树（DTS）中定义的大小（Size）。

<a id="gab9d0b43faefa1f25805e7def82819f2c"></a>

### `flash_area_cb_t`

```c
typedef void(* flash_area_cb_t) (const struct flash_area *fa, void *user_data)
```

```c
#include <zephyr/storage/flash_map.h>
```

闪存映射遍历回调（Flash Map Iteration Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fa` | 闪存区域（Flash Area）。 |
| `user_data` | 用户提供的数据（User Supplied Data）。 |

<a id="ga13b7294e84544373e97b8c0274859f6e"></a>

### `flash_area_align()`

```c
uint32_t flash_area_align ( const struct flash_area * fa)
```

```c
#include <zephyr/storage/flash_map.h>
```

获取闪存区域的写块大小（Write Block Size）。

目前，写入块大小（Write Block Size）可能被视为读取块大小（Read Block Size），尽管大多数驱动支持非对齐读取（Unaligned Readout）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 闪存区域（Flash Area）。 |

**返回（Returns）**：返回值（Returns）：闪存写入的对齐限制（Alignment Restriction），以字节（B）为单位。

<a id="ga826350cb9176f58fecead9998b79756f"></a>

### `flash_area_close()`

```c
void flash_area_close ( __unused const struct flash_area * fa)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/storage/flash_map.h>
```

关闭 flash_area。

保留供未来使用，并用于兼容外部项目。目前是空操作（NOP）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 要关闭的闪存区域（Flash Area）。 |

<a id="gaa50bb1b455a9004f9c24e4af9fd74cd7"></a>

### `flash_area_copy()`

```c
int flash_area_copy ( const struct flash_area * src_fa, off_t src_off, const struct flash_area * dst_fa, off_t dst_off, off_t len, uint8_t * buf, size_t buf_size )
```

```c
#include <zephyr/storage/flash_map.h>
```

将闪存内容从一个闪存区域（Flash Area）复制到另一个区域。

将数据复制到闪存区域（Flash Area）。在发出复制请求之前，通过断言检查区域边界（Area Boundaries）。

更多信息参见 `flash_copy()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src_fa` | 源闪存区域（Source Flash Area）。 |
| `[in] src_off` | 相对于源闪存区域起始位置的偏移量（Offset）。 |
| `[in] dst_fa` | 目标闪存区域（Destination Flash Area）。 |
| `[in] dst_off` | 相对于目标闪存区域起始位置的偏移量（Offset）。 |
| `[in] len` | 要复制的字节数（Number of Bytes）。 |
| `[out] buf` | 指向大小为 `buf_size` 的缓冲区的指针。 |
| `[in] buf_size` | `buf` 所指向缓冲区的大小。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="ga7adf79769378ed468df6d3ffef5e02a9"></a>

### `flash_area_device_is_ready()`

```c
ALWAYS_INLINE bool flash_area_device_is_ready ( const struct flash_area * fa)
```

声明属性：`static`。

```c
#include <zephyr/storage/flash_map.h>
```

验证分配给闪存区域（Flash Area）的设备是否已就绪可用。

指示提供的闪存区域（Flash Area）是否具有一个已知处于可供闪存映射 API（Flash Map API）使用状态的设备。

可用于通过 `PARTITION()` 获得的 `struct flash_area` 指针。该状态至少意味着设备已成功初始化（Initialized）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fa` | 指向待检查 `flash_area` 对象的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 设备已就绪、可供使用。 |
| `false` | 设备尚未就绪（Not Ready），传入的闪存区域指针为 `NULL`，或闪存区域对象内部的设备指针为 `NULL` 时。 |

<a id="gacc5cbff19d23773115f3334f862814d2"></a>

### `flash_area_erase()`

```c
int flash_area_erase ( const struct flash_area * fa, off_t off, size_t len )
```

```c
#include <zephyr/storage/flash_map.h>
```

擦除闪存区域（Erase Flash Area）。

擦除给定闪存区域范围（Flash Area Range）。在发出擦除请求前，通过断言检查区域边界。本 API 的擦除块对齐（Erase-block Alignment）和大小限制，与其封装的闪存驱动相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 闪存区域（Flash Area）。 |
| `[in] off` | 相对于闪存区域起始位置的偏移量（Offset）。 |
| `[in] len` | 要擦除的字节数（Number of Bytes）。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="ga1f16d59cecb25c5143c6a923b3b2f466"></a>

### `flash_area_erased_val()`

```c
uint8_t flash_area_erased_val ( const struct flash_area * fa)
```

```c
#include <zephyr/storage/flash_map.h>
```

获取访问任意已擦除闪存字节时应读到的值（Erased Flash Value）。

本 API 与 MCUboot 移植层（Porting Layer）兼容。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fa` | 闪存区域（Flash Area）。 |

**返回（Returns）**：返回值（Returns）：已擦除存储器的字节值（Erased Memory Byte Value）。

<a id="gafd097d05f5bfe91695bc7793e82cabcd"></a>

### `flash_area_flatten()`

```c
int flash_area_flatten ( const struct flash_area * fa, off_t off, size_t len )
```

```c
#include <zephyr/storage/flash_map.h>
```

擦除闪存区域，或使用擦除值（Erase-value）填充。

对于需要编程—擦除（Program-Erase）的设备，本函数的行为与 `flash_area_erase` 完全相同。对于 RAM 型非易失性设备（RAM Non-volatile Device），若驱动提供擦除回调则调用该回调，否则用驱动定义的擦除值（Erase Value）填充给定范围。本函数只应供此类代码使用：尚未直接支持无须擦除的设备，并且依赖设备在某些操作前已被擦除。注意，对无须擦除的设备模拟擦除（Emulated Erase）是通过写入实现的，会影响设备耐久性（Endurance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 闪存区域（Flash Area）。 |
| `[in] off` | 相对于闪存区域起始位置的偏移量（Offset）。 |
| `[in] len` | 要擦除的字节数（Number of Bytes）。 |

**参阅（See Also）**：另请参见（See Also）：`flash_area_erase()`、`flash_flatten()`。

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="ga34e74955153f8576acdbff1a524f2d37"></a>

### `flash_area_foreach()`

```c
void flash_area_foreach ( flash_area_cb_t user_cb, void * user_data )
```

```c
#include <zephyr/storage/flash_map.h>
```

遍历闪存映射（Flash Map）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `user_cb` | 用户回调（User Callback） |
| `user_data` | 用户提供的数据（User Supplied Data）。 |

<a id="ga868a47161b33c99629df600c1d7d9d43"></a>

### `flash_area_get_device()`

```c
const struct device * flash_area_get_device ( const struct flash_area * fa)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/storage/flash_map.h>
```

获取给定闪存区域（Flash Area）的驱动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 闪存区域（Flash Area）。 |

**返回（Returns）**：返回值（Returns）：设备驱动（Device Driver）。

<a id="ga5c89e0be6c41058beb1c3f87a0c9c94f"></a>

### `flash_area_get_sectors()`

```c
int flash_area_get_sectors ( int fa_id, uint32_t * count, struct flash_sector * sectors )
```

```c
#include <zephyr/storage/flash_map.h>
```

获取区域内扇区（Sectors）的信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa_id` | 给定的闪存区域标识符（Flash Area ID）。 |
| `[in,out] count` | 输入时为扇区数组容量（Sector Capacity），输出时为获取到的扇区数（Number of Sectors Retrieved）。 |
| `[out] sectors` | 用于存储扇区数据（Sector Data）的缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，失败时为负 `errno` 错误码。特别地，如果 `flash_area` 内的闪存页数超过数组容量，则返回 `-ENOMEM`。

<a id="ga557d5fd981b0d52d0eb483ab218c497c"></a>

### `flash_area_has_driver()`

```c
int flash_area_has_driver ( const struct flash_area * fa)
```

```c
#include <zephyr/storage/flash_map.h>
```

检查系统中是否有支持给定闪存区域（Flash Area）的闪存驱动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 闪存区域（Flash Area）。 |

**返回（Returns）**：返回值（Returns）：成功时为 1；没有匹配驱动时为 `-ENODEV`。

<a id="ga91e8c75b636b6f300207128df8b0ca9a"></a>

### `flash_area_label()`

```c
const char * flash_area_label ( const struct flash_area * fa)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/storage/flash_map.h>
```

从设备树（Device Tree）获取 label 属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 闪存区域（Flash Area）。 |

**返回（Returns）**：返回值（Returns）：已定义 `label` 属性时返回该属性，否则为 `NULL`。

<a id="ga6fe2593210688eb85e03bea5f96ea2f7"></a>

### `flash_area_open()`

```c
int flash_area_open ( uint8_t id, const struct flash_area ** fa )
```

```c
#include <zephyr/storage/flash_map.h>
```

从 flash_map 获取分区的闪存区域（Flash Area）。

本函数从 `flash_map` 中获取给定分区对应的 `flash_area`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] id` | 闪存分区标识符（Flash Partition ID）。 |
| `[out] fa` | 用于接收 `flash_area` 引用的指针。如果 ID 未知，输出时该指针为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；`flash_map` 不可用时为 `-EACCES`；ID 未知时为 `-ENOENT`；区域未关联驱动时为 `-ENODEV`。

<a id="ga7c55704b0c0061a4715470676114b127"></a>

### `flash_area_read()`

```c
int flash_area_read ( const struct flash_area * fa, off_t off, void * dst, size_t len )
```

```c
#include <zephyr/storage/flash_map.h>
```

读取闪存区域数据（Flash Area Data）。

从闪存区域（Flash Area）读取数据。发出读取请求前，通过断言检查读取范围。本 API 的读取块对齐（Read-block Alignment）和大小限制，与其封装的闪存驱动相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 闪存区域（Flash Area）。 |
| `[in] off` | 相对于闪存区域起始位置的读取偏移量（Read Offset）。 |
| `[out] dst` | 用于保存所读数据的缓冲区。 |
| `[in] len` | 要读取的字节数。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="ga12064d388369a504b571e9776201f688"></a>

### `flash_area_sectors()`

```c
int flash_area_sectors ( const struct flash_area * fa, uint32_t * count, struct flash_sector * sectors )
```

```c
#include <zephyr/storage/flash_map.h>
```

获取区域内扇区（Sectors）的信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 指向闪存区域对象（Flash Area Object）的指针。 |
| `[in,out] count` | 输入时为扇区数组容量（Sector Capacity），输出时为获取到的扇区数（Number of Sectors Retrieved）。 |
| `[out] sectors` | 用于存储扇区数据（Sector Data）的缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，失败时为负 `errno` 错误码。特别地，如果 `flash_area` 内的闪存页数超过数组容量，则返回 `-ENOMEM`。

<a id="gaa56052f8d6bf4f6966752bc21f5cceb8"></a>

### `flash_area_write()`

```c
int flash_area_write ( const struct flash_area * fa, off_t off, const void * src, size_t len )
```

```c
#include <zephyr/storage/flash_map.h>
```

向闪存区域（Flash Area）写入数据。

向闪存区域（Flash Area）写入数据。发出写入请求前，通过断言检查写入范围。本 API 的写入块对齐（Write-block Alignment）和大小限制，与其封装的闪存驱动相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] fa` | 闪存区域（Flash Area）。 |
| `[in] off` | 相对于闪存区域起始位置的写入偏移量（Write Offset）。 |
| `[in] src` | 包含待写数据的缓冲区（Buffer）。 |
| `[in] len` | 要写入的字节数。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。


## 5.6\_原页交叉引用（Cross References）

- [flash_area](../system_service_model_reference/P027_flash_area_结构体.md)
- [flash_sector](../system_service_model_reference/P033_flash_sector_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)
- [zephyr/storage/flash_map.h](../api_file_flash_test_reference/P003_zephyr__storage__flash_map.h_文件参考.md)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_NODE_HAS_COMPAT](../dt_identity_reference/P002_设备树存在性与状态宏.md#gad8912ba5db980713e72257472ded3ced)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_MTD_FROM_MAPPED_PARTITION](../dt_partition_reference/P005_设备树映射分区宏.md#ga441462089e44e9ea3eb0a7af3473b37a)
- [DT_NODE_BY_MAPPED_PARTITION_LABEL](../dt_partition_reference/P005_设备树映射分区宏.md#ga4ba9b127634652b98df9e0a08f7c8ff0)
- [DT_MTD_FROM_FIXED_PARTITION](../dt_partition_reference/P002_设备树固定分区宏.md#ga3484bb9a0cd8c2a4d971989dc58c194e)
- [DT_NODE_BY_FIXED_PARTITION_LABEL](../dt_partition_reference/P002_设备树固定分区宏.md#gafcd93790974c48b10dd1170d14c49bf9)
- [DT_PARTITION_EXISTS](../dt_partition_reference/P001_设备树通用分区宏.md#gaaa77bff50edd953502a952620b3568ed)
- [DT_MAPPED_PARTITION_ID](../dt_partition_reference/P005_设备树映射分区宏.md#gab01469f6210d92885917931c35e3f868)
- [DT_FIXED_PARTITION_ID](../dt_partition_reference/P002_设备树固定分区宏.md#gaf3b448e91dff79ece4d67ef833088ac9)
- [DT_MAPPED_PARTITION_ADDR](../dt_partition_reference/P005_设备树映射分区宏.md#ga677f55ce5ad2e0519f699d8867f36aa1)
- [DT_FIXED_SUBPARTITION_EXISTS](../dt_partition_reference/P002_设备树固定分区宏.md#ga14a8091e4a46de4314c5bbacc0451726)
- [DT_FIXED_SUBPARTITION_ADDR](../dt_partition_reference/P002_设备树固定分区宏.md#gac3fb38b3219320d67f24f02518eb29c1)
- [DT_FIXED_PARTITION_ADDR](../dt_partition_reference/P002_设备树固定分区宏.md#gac8be7ec2cddde3f76f0f096bd3c63546)
- [DT_MTD_FROM_FIXED_SUBPARTITION](../dt_partition_reference/P002_设备树固定分区宏.md#ga9e6ffb2c5a623d9e49333302f8e1a834)
- [COND_CASE_1](../util_reference/P001_通用工具公共接口.md#ga0325a11d188ce0d7f2fddc4b74947478)
- [DT_MAPPED_PARTITION_OFFSET](../dt_partition_reference/P005_设备树映射分区宏.md#ga36c4868e32a9b8d4f6d0f01c30723c06)
- [DT_PROP_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga52ad691ea4cae633ca702020e939d461)
- [DT_PARENT](../dt_identity_reference/P001_设备树节点标识宏.md#ga3ac56d491510275ee1321446796ab63b)
- [DT_REG_SIZE](../dt_reg_reference/P001_设备树寄存器属性宏.md#gad223efc6c77d008e55c3588953e85bfb)
- [flash_copy()](../flash_reference/P001_Flash公共接口.md#ga847407358a20d3d5918d8ef11657ce2b)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [flash_flatten()](../flash_reference/P001_Flash公共接口.md#ga11eda0cdc7be12636a90d2e8c7264e4a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__flash__area__api_html_ga87e1dd8007998ca22d83bf23a9c4a150"></a>
<a id="agroup__flash__area__api_html_gadfe30156a3a50c69e268075d07ef050b"></a>
<a id="agroup__flash__area__api_html_ga8f3f3ac80d3858626f05c60aaaec48f7"></a>
<a id="agroup__flash__area__api_html_ga565f24a138c217bdbe8f42afe8b664e0"></a>
<a id="agroup__flash__area__api_html_ga4e63c3b898a43a210bc0298dc7b49c1e"></a>
<a id="agroup__flash__area__api_html_gafbc907db76aec2702eff9e5265323560"></a>
<a id="agroup__flash__area__api_html_ga583ab6d0092ce23df436e42c1eeeb6e2"></a>
<a id="agroup__flash__area__api_html_ga8c68c5fa266dcc128ee9520c3c57807d"></a>
<a id="agroup__flash__area__api_html_ga8986be787a0c4d7c35ef835ce91290de"></a>
<a id="agroup__flash__area__api_html_gac6c6b41211ee9bdb154cefdb46214615"></a>
<a id="agroup__flash__area__api_html_ga28906b4cc8b00f8e055a1d9a082dbb5e"></a>
<a id="agroup__flash__area__api_html_gabaa4ff45d7ec2c57616b9fb721c0c45c"></a>
<a id="agroup__flash__area__api_html_gaee5fe6581a477b83157d00155e150980"></a>
<a id="agroup__flash__area__api_html_gab5234434a7f106e4b3f2b79f2087279a"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-fixed-partition_html_ga3484bb9a0cd8c2a4d971989dc58c194e"></a>
<a id="agroup__devicetree-fixed-partition_html_gafcd93790974c48b10dd1170d14c49bf9"></a>
<a id="agroup__devicetree-generic-exist_html_gad8912ba5db980713e72257472ded3ced"></a>
<a id="agroup__devicetree-generic-id_html_gab7d23294a6bf7fd44a98b48ec47d8a79"></a>
<a id="agroup__devicetree-mapped-partition_html_ga441462089e44e9ea3eb0a7af3473b37a"></a>
<a id="agroup__devicetree-mapped-partition_html_ga4ba9b127634652b98df9e0a08f7c8ff0"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__devicetree-partition_html_gaaa77bff50edd953502a952620b3568ed"></a>
<a id="agroup__devicetree-fixed-partition_html_gaf3b448e91dff79ece4d67ef833088ac9"></a>
<a id="agroup__devicetree-mapped-partition_html_gab01469f6210d92885917931c35e3f868"></a>
<a id="agroup__devicetree-fixed-partition_html_ga14a8091e4a46de4314c5bbacc0451726"></a>
<a id="agroup__devicetree-fixed-partition_html_gac3fb38b3219320d67f24f02518eb29c1"></a>
<a id="agroup__devicetree-fixed-partition_html_gac8be7ec2cddde3f76f0f096bd3c63546"></a>
<a id="agroup__devicetree-mapped-partition_html_ga677f55ce5ad2e0519f699d8867f36aa1"></a>
<a id="agroup__devicetree-fixed-partition_html_ga9e6ffb2c5a623d9e49333302f8e1a834"></a>
<a id="agroup__devicetree-generic-id_html_ga3ac56d491510275ee1321446796ab63b"></a>
<a id="agroup__devicetree-generic-prop_html_ga52ad691ea4cae633ca702020e939d461"></a>
<a id="agroup__devicetree-mapped-partition_html_ga36c4868e32a9b8d4f6d0f01c30723c06"></a>
<a id="agroup__sys-util_html_ga0325a11d188ce0d7f2fddc4b74947478"></a>
<a id="agroup__devicetree-reg-prop_html_gad223efc6c77d008e55c3588953e85bfb"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_连接管理器连接性 API（Connectivity API）.md) · [返回大纲](大纲.md) · [下一章](P006_SMP 传输（SMP transport）.md)
