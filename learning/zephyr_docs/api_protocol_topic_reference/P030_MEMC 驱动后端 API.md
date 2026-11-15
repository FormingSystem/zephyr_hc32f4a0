---
id: learning.zephyr-docs.api-protocol-topic-reference.page-30
title: MEMC 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_MEMC 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现内存控制器（MEMC）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 30.1\_数据结构（Data Structures）

<a id="r_memc_5Fdriver_5Fapi"></a>

```c
struct memc_driver_api
```

相关声明：[memc_driver_api](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md)。

驱动操作（Driver Operations）：内存控制器（MEMC）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 30.2\_类型定义（Typedefs）

<a id="r_ga1e7138177b931238a4f09a58bf4c765a"></a>

```c
typedef int(* memc_api_read) (const struct device *dev, uint32_t addr, uint8_t *data, size_t len)
```

相关声明：[memc_api_read](#ga1e7138177b931238a4f09a58bf4c765a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取外部存储器的回调 API。

<a id="r_gac495599a886be46a47dc22f6aaedcfb8"></a>

```c
typedef int(* memc_api_write) (const struct device *dev, uint32_t addr, const uint8_t *data, size_t len)
```

相关声明：[memc_api_write](#gac495599a886be46a47dc22f6aaedcfb8)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入外部存储器的回调 API。

<a id="r_ga2c33e74e81bbc4aaaef0a577737ebdcb"></a>

```c
typedef int(* memc_api_get_size) (const struct device *dev, uint64_t *size)
```

相关声明：[memc_api_get_size](#ga2c33e74e81bbc4aaaef0a577737ebdcb)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取外部存储器大小的回调 API。

<a id="r_gada700c92c23e9a59eea6012594e8866d"></a>

```c
typedef int(* memc_api_read_id) (const struct device *dev, uint8_t *id, size_t len)
```

相关声明：[memc_api_read_id](#gada700c92c23e9a59eea6012594e8866d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取外部存储器 ID 的回调 API。

<a id="r_ga0311584e35d2ad24e92bb9999ca76510"></a>

```c
typedef void *(* memc_api_get_mem_base) (const struct device *dev)
```

相关声明：[memc_api_get_mem_base](#ga0311584e35d2ad24e92bb9999ca76510)、[device](../device_reference/P002_设备对象结构.md)。

获取外部存储器基地址的回调 API。

## 30.3\_详细说明（Detailed Documentation）

<a id="ga0311584e35d2ad24e92bb9999ca76510"></a>

### `memc_api_get_mem_base`

```c
typedef void *(* memc_api_get_mem_base) (const struct device *dev)
```

```c
#include <zephyr/drivers/memc.h>
```

获取外部存储器基地址的回调 API。

参数说明参见 `memc_get_mem_base()`。

<a id="ga2c33e74e81bbc4aaaef0a577737ebdcb"></a>

### `memc_api_get_size`

```c
typedef int(* memc_api_get_size) (const struct device *dev, uint64_t *size)
```

```c
#include <zephyr/drivers/memc.h>
```

获取外部存储器大小的回调 API。

参数说明参见 `memc_get_size()`。

<a id="ga1e7138177b931238a4f09a58bf4c765a"></a>

### `memc_api_read`

```c
typedef int(* memc_api_read) (const struct device *dev, uint32_t addr, uint8_t *data, size_t len)
```

```c
#include <zephyr/drivers/memc.h>
```

读取外部存储器的回调 API。

参数说明参见 `memc_read()`。

<a id="gada700c92c23e9a59eea6012594e8866d"></a>

### `memc_api_read_id`

```c
typedef int(* memc_api_read_id) (const struct device *dev, uint8_t *id, size_t len)
```

```c
#include <zephyr/drivers/memc.h>
```

读取外部存储器 ID 的回调 API。

参数说明参见 `memc_read_id()`。

<a id="gac495599a886be46a47dc22f6aaedcfb8"></a>

### `memc_api_write`

```c
typedef int(* memc_api_write) (const struct device *dev, uint32_t addr, const uint8_t *data, size_t len)
```

```c
#include <zephyr/drivers/memc.h>
```

写入外部存储器的回调 API。

参数说明参见 `memc_write()`。


## 30.4\_原页交叉引用（Cross References）

- [memc_driver_api](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [zephyr/drivers/memc.h](../peripheral_bus_storage_header_reference/P014_zephyr__drivers__memc.h_头文件参考.md)
- [memc_get_mem_base()](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#gac48976493664e5c68c5b6a90ae8dd960)
- [memc_get_size()](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga02bca9fd387ac26841394a73d51dbe7e)
- [memc_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga7b766a76f3bffe8b89eafb93c4f16cae)
- [memc_read_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#gaf797d9df098f75ce12e69223f759364b)
- [memc_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga8c08116a54ccb2765822ba20ba77ed39)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P029_MFD BD8LB600FS 接口.md) · [返回大纲](大纲.md) · [下一章](P031_MFD Infineon MXCRYPTO 接口.md)
