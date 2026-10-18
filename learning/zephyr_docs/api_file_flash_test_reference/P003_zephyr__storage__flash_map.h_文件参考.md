---
id: learning.zephyr-docs.api-file-flash-test-reference.page-3
title: zephyr__storage__flash_map.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_storage\_\_flash\_map.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

闪存映射（Flash Map）的公共API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <stddef.h>
#include <sys/types.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/devicetree/fixed-partitions.h>
#include <zephyr/devicetree/mapped-partition.h>
#include <zephyr/devicetree/partitions.h>
```

查看此文件的源码。

闪存映射（Flash Map）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

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

## 3.2\_宏定义（Macros）

<a id="r_ga4e63c3b898a43a210bc0298dc7b49c1e"></a>

```c
#define PARTITION_EXISTS(label)
```

相关声明：[PARTITION_EXISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga4e63c3b898a43a210bc0298dc7b49c1e)。

给定 DTS 节点标签（Node Label）对应的分区存在时，返回非零值。

<a id="r_gabb94759e5717302724f08f90f941a945"></a>

```c
#define FIXED_PARTITION_EXISTS(label)
```

相关声明：[FIXED_PARTITION_EXISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gabb94759e5717302724f08f90f941a945)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_EXISTS()。这里不能使用 __DEPRECATED_MACRO，因为它会导致使用此宏时出现编译器错误。

<a id="r_gafbc907db76aec2702eff9e5265323560"></a>

```c
#define PARTITION_ID(label)
```

相关声明：[PARTITION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gafbc907db76aec2702eff9e5265323560)。

通过分区 DTS 节点标签获取闪存区域标识符（Flash Area ID）。

<a id="r_ga60d5298007e2ee261b915a110389e76a"></a>

```c
#define FIXED_PARTITION_ID(label)
```

相关声明：[FIXED_PARTITION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga60d5298007e2ee261b915a110389e76a)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_ID()。

<a id="r_gaee5fe6581a477b83157d00155e150980"></a>

```c
#define PARTITION_OFFSET(label)
```

相关声明：[PARTITION_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaee5fe6581a477b83157d00155e150980)。

通过 DTS 节点标签获取分区偏移量（Partition Offset）。

<a id="r_ga9229bc06458c19baf093ced063a9494b"></a>

```c
#define FIXED_PARTITION_OFFSET(label)
```

相关声明：[FIXED_PARTITION_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga9229bc06458c19baf093ced063a9494b)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_OFFSET()。

<a id="r_gadfe30156a3a50c69e268075d07ef050b"></a>

```c
#define PARTITION_ADDRESS(label)
```

相关声明：[PARTITION_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gadfe30156a3a50c69e268075d07ef050b)。

通过 DTS 节点标签获取分区地址（Partition Address）。

<a id="r_ga5ac2848ccfcc1425939d76f499756551"></a>

```c
#define FIXED_PARTITION_ADDRESS(label)
```

相关声明：[FIXED_PARTITION_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga5ac2848ccfcc1425939d76f499756551)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_ADDRESS()。

<a id="r_ga8c68c5fa266dcc128ee9520c3c57807d"></a>

```c
#define PARTITION_NODE_ADDRESS(node)
```

相关声明：[PARTITION_NODE_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga8c68c5fa266dcc128ee9520c3c57807d)。

通过 DTS 节点获取分区地址（Partition Address）。

<a id="r_gaf6121895f4fdd50533762c6aa57cb319"></a>

```c
#define FIXED_PARTITION_NODE_ADDRESS(node)
```

相关声明：[FIXED_PARTITION_NODE_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaf6121895f4fdd50533762c6aa57cb319)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_ADDRESS()。

<a id="r_ga28906b4cc8b00f8e055a1d9a082dbb5e"></a>

```c
#define PARTITION_NODE_OFFSET(node)
```

相关声明：[PARTITION_NODE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga28906b4cc8b00f8e055a1d9a082dbb5e)。

通过 DTS 节点获取分区偏移量（Partition Offset）。

<a id="r_ga79092c8d0f32aeec69c6a79021d1ab38"></a>

```c
#define FIXED_PARTITION_NODE_OFFSET(label)
```

相关声明：[FIXED_PARTITION_NODE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga79092c8d0f32aeec69c6a79021d1ab38)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_OFFSET()。

<a id="r_gab5234434a7f106e4b3f2b79f2087279a"></a>

```c
#define PARTITION_SIZE(label)
```

相关声明：[PARTITION_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab5234434a7f106e4b3f2b79f2087279a)。

获取 DTS 节点标签对应的分区大小（Partition Size）。

<a id="r_ga2dbc50d9f80d7f7c597c75cbd536cd50"></a>

```c
#define FIXED_PARTITION_SIZE(label)
```

相关声明：[FIXED_PARTITION_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga2dbc50d9f80d7f7c597c75cbd536cd50)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_SIZE()。

<a id="r_gabaa4ff45d7ec2c57616b9fb721c0c45c"></a>

```c
#define PARTITION_NODE_SIZE(node)
```

相关声明：[PARTITION_NODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gabaa4ff45d7ec2c57616b9fb721c0c45c)。

获取 DTS 节点对应的固定分区大小（Fixed-partition Size）。

<a id="r_ga526459438c6de09abb727585d22b7004"></a>

```c
#define FIXED_PARTITION_NODE_SIZE(node)
```

相关声明：[FIXED_PARTITION_NODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga526459438c6de09abb727585d22b7004)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_SIZE()。

<a id="r_gacca3f32100a4e46cb7da21ea8bf0782c"></a>

```c
#define FLASH_AREA_DEVICE(label)
```

相关声明：[FLASH_AREA_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gacca3f32100a4e46cb7da21ea8bf0782c)。

获取区域／分区所在设备的设备指针（Device Pointer）。

<a id="r_ga565f24a138c217bdbe8f42afe8b664e0"></a>

```c
#define PARTITION_DEVICE(label)
```

相关声明：[PARTITION_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga565f24a138c217bdbe8f42afe8b664e0)。

获取区域／分区所在设备的设备指针（Device Pointer）。

<a id="r_ga3c92b6797feb183da38b8b57e77f2d17"></a>

```c
#define FIXED_PARTITION_DEVICE(label)
```

相关声明：[FIXED_PARTITION_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga3c92b6797feb183da38b8b57e77f2d17)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_DEVICE()。

<a id="r_ga8986be787a0c4d7c35ef835ce91290de"></a>

```c
#define PARTITION_NODE_DEVICE(node)
```

相关声明：[PARTITION_NODE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga8986be787a0c4d7c35ef835ce91290de)。

获取区域／分区所在设备的设备指针（Device Pointer）。

<a id="r_gad64fb220f82870acce62661bfa94991a"></a>

```c
#define FIXED_PARTITION_NODE_DEVICE(node)
```

相关声明：[FIXED_PARTITION_NODE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gad64fb220f82870acce62661bfa94991a)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_DEVICE()。

<a id="r_ga583ab6d0092ce23df436e42c1eeeb6e2"></a>

```c
#define PARTITION_MTD(label)
```

相关声明：[PARTITION_MTD](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga583ab6d0092ce23df436e42c1eeeb6e2)。

获取区域／分区所在闪存控制器的节点标识符（Node Identifier）。

<a id="r_gaf933ac3bd33006357c8dc0c3b3f5878f"></a>

```c
#define FIXED_PARTITION_MTD(label)
```

相关声明：[FIXED_PARTITION_MTD](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaf933ac3bd33006357c8dc0c3b3f5878f)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_OFFSET()。

<a id="r_gac6c6b41211ee9bdb154cefdb46214615"></a>

```c
#define PARTITION_NODE_MTD(node)
```

相关声明：[PARTITION_NODE_MTD](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gac6c6b41211ee9bdb154cefdb46214615)。

获取区域／分区所在闪存控制器的节点标识符（Node Identifier）。

<a id="r_ga891d6e60a927f4b5660bcb2966e9bd2b"></a>

```c
#define FIXED_PARTITION_NODE_MTD(node)
```

相关声明：[FIXED_PARTITION_NODE_MTD](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga891d6e60a927f4b5660bcb2966e9bd2b)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_NODE_MTD()。

<a id="r_ga87e1dd8007998ca22d83bf23a9c4a150"></a>

```c
#define PARTITION(label)
```

相关声明：[PARTITION](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga87e1dd8007998ca22d83bf23a9c4a150)。

通过分区标签（Partition Label）获取 flash_area 对象的指针。

<a id="r_ga5682b688b50fd2cac3c6c8045e64107e"></a>

```c
#define FIXED_PARTITION(label)
```

相关声明：[FIXED_PARTITION](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga5682b688b50fd2cac3c6c8045e64107e)。

已弃用的宏（Deprecated Macro），请改用 PARTITION()。

<a id="r_ga8f3f3ac80d3858626f05c60aaaec48f7"></a>

```c
#define PARTITION_BY_NODE(node)
```

相关声明：[PARTITION_BY_NODE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga8f3f3ac80d3858626f05c60aaaec48f7)。

通过 DTS 中的分区节点（Partition Node）获取 flash_area 对象的指针。

<a id="r_gab51fb05a2cd0666b892d90ccbc9de342"></a>

```c
#define FIXED_PARTITION_BY_NODE(node)
```

相关声明：[FIXED_PARTITION_BY_NODE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab51fb05a2cd0666b892d90ccbc9de342)。

已弃用的宏（Deprecated Macro），请改用 PARTITION_OFFSET()。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_gab9d0b43faefa1f25805e7def82819f2c"></a>

```c
typedef void(* flash_area_cb_t) (const struct flash_area *fa, void *user_data)
```

相关声明：[flash_area_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab9d0b43faefa1f25805e7def82819f2c)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

闪存映射遍历回调（Flash Map Iteration Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_ga6fe2593210688eb85e03bea5f96ea2f7"></a>

```c
int flash_area_open (uint8_t id, const struct flash_area **fa)
```

相关声明：[flash_area_open](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga6fe2593210688eb85e03bea5f96ea2f7)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

从 flash_map 获取分区的闪存区域（Flash Area）。

<a id="r_ga826350cb9176f58fecead9998b79756f"></a>

```c
static void flash_area_close (__unused const struct flash_area *fa)
```

相关声明：[flash_area_close](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga826350cb9176f58fecead9998b79756f)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

关闭 flash_area。

<a id="r_ga7adf79769378ed468df6d3ffef5e02a9"></a>

```c
static ALWAYS_INLINE bool flash_area_device_is_ready (const struct flash_area *fa)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[flash_area_device_is_ready](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga7adf79769378ed468df6d3ffef5e02a9)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

验证分配给闪存区域（Flash Area）的设备是否已就绪可用。

<a id="r_ga7c55704b0c0061a4715470676114b127"></a>

```c
int flash_area_read (const struct flash_area *fa, off_t off, void *dst, size_t len)
```

相关声明：[flash_area_read](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga7c55704b0c0061a4715470676114b127)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

读取闪存区域数据（Flash Area Data）。

<a id="r_gaa56052f8d6bf4f6966752bc21f5cceb8"></a>

```c
int flash_area_write (const struct flash_area *fa, off_t off, const void *src, size_t len)
```

相关声明：[flash_area_write](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaa56052f8d6bf4f6966752bc21f5cceb8)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

向闪存区域（Flash Area）写入数据。

<a id="r_gaa50bb1b455a9004f9c24e4af9fd74cd7"></a>

```c
int flash_area_copy (const struct flash_area *src_fa, off_t src_off, const struct flash_area *dst_fa, off_t dst_off, off_t len, uint8_t *buf, size_t buf_size)
```

相关声明：[flash_area_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaa50bb1b455a9004f9c24e4af9fd74cd7)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将闪存内容从一个闪存区域（Flash Area）复制到另一个区域。

<a id="r_gacc5cbff19d23773115f3334f862814d2"></a>

```c
int flash_area_erase (const struct flash_area *fa, off_t off, size_t len)
```

相关声明：[flash_area_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gacc5cbff19d23773115f3334f862814d2)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

擦除闪存区域（Erase Flash Area）。

<a id="r_gafd097d05f5bfe91695bc7793e82cabcd"></a>

```c
int flash_area_flatten (const struct flash_area *fa, off_t off, size_t len)
```

相关声明：[flash_area_flatten](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gafd097d05f5bfe91695bc7793e82cabcd)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

擦除闪存区域，或使用擦除值（Erase-value）填充。

<a id="r_ga13b7294e84544373e97b8c0274859f6e"></a>

```c
uint32_t flash_area_align (const struct flash_area *fa)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flash_area_align](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga13b7294e84544373e97b8c0274859f6e)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

获取闪存区域的写块大小（Write Block Size）。

<a id="r_ga5c89e0be6c41058beb1c3f87a0c9c94f"></a>

```c
int flash_area_get_sectors (int fa_id, uint32_t *count, struct flash_sector *sectors)
```

相关声明：[flash_area_get_sectors](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga5c89e0be6c41058beb1c3f87a0c9c94f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flash_sector](../system_service_model_reference/P033_flash_sector_结构体.md)。

获取区域内扇区（Sectors）的信息。

<a id="r_ga12064d388369a504b571e9776201f688"></a>

```c
int flash_area_sectors (const struct flash_area *fa, uint32_t *count, struct flash_sector *sectors)
```

相关声明：[flash_area_sectors](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga12064d388369a504b571e9776201f688)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flash_sector](../system_service_model_reference/P033_flash_sector_结构体.md)。

获取区域内扇区（Sectors）的信息。

<a id="r_ga34e74955153f8576acdbff1a524f2d37"></a>

```c
void flash_area_foreach (flash_area_cb_t user_cb, void *user_data)
```

相关声明：[flash_area_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga34e74955153f8576acdbff1a524f2d37)、[flash_area_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab9d0b43faefa1f25805e7def82819f2c)。

遍历闪存映射（Flash Map）。

<a id="r_ga557d5fd981b0d52d0eb483ab218c497c"></a>

```c
int flash_area_has_driver (const struct flash_area *fa)
```

相关声明：[flash_area_has_driver](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga557d5fd981b0d52d0eb483ab218c497c)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

检查系统中是否有支持给定闪存区域（Flash Area）的闪存驱动。

<a id="r_ga868a47161b33c99629df600c1d7d9d43"></a>

```c
static const struct device * flash_area_get_device (const struct flash_area *fa)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[flash_area_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga868a47161b33c99629df600c1d7d9d43)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

获取给定闪存区域（Flash Area）的驱动。

<a id="r_ga91e8c75b636b6f300207128df8b0ca9a"></a>

```c
static const char * flash_area_label (const struct flash_area *fa)
```

相关声明：[flash_area_label](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga91e8c75b636b6f300207128df8b0ca9a)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

从设备树（Device Tree）获取 label 属性。

<a id="r_ga1f16d59cecb25c5143c6a923b3b2f466"></a>

```c
uint8_t flash_area_erased_val (const struct flash_area *fa)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flash_area_erased_val](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga1f16d59cecb25c5143c6a923b3b2f466)、[flash_area](../system_service_model_reference/P027_flash_area_结构体.md)。

获取访问任意已擦除闪存字节时应读到的值（Erased Flash Value）。


## 3.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/devicetree/fixed-partitions.h](../dt_partition_reference/P004_设备树固定分区头文件源码.md)
- [zephyr/devicetree/mapped-partition.h](../dt_partition_reference/P007_设备树映射分区头文件源码.md)
- [zephyr/devicetree/partitions.h](../dt_partition_reference/P009_设备树通用分区头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P020_flash_map.h_源码浏览.md)
- [flash_area](../system_service_model_reference/P027_flash_area_结构体.md)
- [flash_sector](../system_service_model_reference/P033_flash_sector_结构体.md)
- [PARTITION_EXISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga4e63c3b898a43a210bc0298dc7b49c1e)
- [FIXED_PARTITION_EXISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gabb94759e5717302724f08f90f941a945)
- [PARTITION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gafbc907db76aec2702eff9e5265323560)
- [FIXED_PARTITION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga60d5298007e2ee261b915a110389e76a)
- [PARTITION_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaee5fe6581a477b83157d00155e150980)
- [FIXED_PARTITION_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga9229bc06458c19baf093ced063a9494b)
- [PARTITION_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gadfe30156a3a50c69e268075d07ef050b)
- [FIXED_PARTITION_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga5ac2848ccfcc1425939d76f499756551)
- [PARTITION_NODE_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga8c68c5fa266dcc128ee9520c3c57807d)
- [FIXED_PARTITION_NODE_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaf6121895f4fdd50533762c6aa57cb319)
- [PARTITION_NODE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga28906b4cc8b00f8e055a1d9a082dbb5e)
- [FIXED_PARTITION_NODE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga79092c8d0f32aeec69c6a79021d1ab38)
- [PARTITION_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab5234434a7f106e4b3f2b79f2087279a)
- [FIXED_PARTITION_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga2dbc50d9f80d7f7c597c75cbd536cd50)
- [PARTITION_NODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gabaa4ff45d7ec2c57616b9fb721c0c45c)
- [FIXED_PARTITION_NODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga526459438c6de09abb727585d22b7004)
- [FLASH_AREA_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gacca3f32100a4e46cb7da21ea8bf0782c)
- [PARTITION_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga565f24a138c217bdbe8f42afe8b664e0)
- [FIXED_PARTITION_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga3c92b6797feb183da38b8b57e77f2d17)
- [PARTITION_NODE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga8986be787a0c4d7c35ef835ce91290de)
- [FIXED_PARTITION_NODE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gad64fb220f82870acce62661bfa94991a)
- [PARTITION_MTD](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga583ab6d0092ce23df436e42c1eeeb6e2)
- [FIXED_PARTITION_MTD](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaf933ac3bd33006357c8dc0c3b3f5878f)
- [PARTITION_NODE_MTD](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gac6c6b41211ee9bdb154cefdb46214615)
- [FIXED_PARTITION_NODE_MTD](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga891d6e60a927f4b5660bcb2966e9bd2b)
- [PARTITION](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga87e1dd8007998ca22d83bf23a9c4a150)
- [FIXED_PARTITION](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga5682b688b50fd2cac3c6c8045e64107e)
- [PARTITION_BY_NODE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga8f3f3ac80d3858626f05c60aaaec48f7)
- [FIXED_PARTITION_BY_NODE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab51fb05a2cd0666b892d90ccbc9de342)
- [flash_area_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab9d0b43faefa1f25805e7def82819f2c)
- [flash_area_open](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga6fe2593210688eb85e03bea5f96ea2f7)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flash_area_close](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga826350cb9176f58fecead9998b79756f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [flash_area_device_is_ready](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga7adf79769378ed468df6d3ffef5e02a9)
- [flash_area_read](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga7c55704b0c0061a4715470676114b127)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [flash_area_write](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaa56052f8d6bf4f6966752bc21f5cceb8)
- [flash_area_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaa50bb1b455a9004f9c24e4af9fd74cd7)
- [flash_area_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gacc5cbff19d23773115f3334f862814d2)
- [flash_area_flatten](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gafd097d05f5bfe91695bc7793e82cabcd)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [flash_area_align](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga13b7294e84544373e97b8c0274859f6e)
- [flash_area_get_sectors](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga5c89e0be6c41058beb1c3f87a0c9c94f)
- [flash_area_sectors](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga12064d388369a504b571e9776201f688)
- [flash_area_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga34e74955153f8576acdbff1a524f2d37)
- [flash_area_has_driver](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga557d5fd981b0d52d0eb483ab218c497c)
- [device](../device_reference/P002_设备对象结构.md)
- [flash_area_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga868a47161b33c99629df600c1d7d9d43)
- [flash_area_label](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga91e8c75b636b6f300207128df8b0ca9a)
- [flash_area_erased_val](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga1f16d59cecb25c5143c6a923b3b2f466)

<a id="header-details"></a>

---

[上一章](P002_zephyr__authentication__fido2__fido2_types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__bluetooth__classic__hfp_hf.h_文件参考.md)
