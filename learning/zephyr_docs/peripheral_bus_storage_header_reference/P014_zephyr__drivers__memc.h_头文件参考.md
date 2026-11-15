---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-14
title: zephyr__drivers__memc.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/memc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_drivers\_\_memc.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/memc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内存控制器（Memory Controller，MEMC）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>
#include <string.h>
#include <zephyr/syscalls/memc.h>
```

查看此文件的源码。

内存控制器（Memory Controller，MEMC）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_memc_5Fdriver_5Fapi"></a>

```c
struct memc_driver_api
```

相关声明：[memc_driver_api](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md)。

驱动操作（Driver Operations）：内存控制器（MEMC）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 14.2\_类型定义（Typedefs）

<a id="r_ga1e7138177b931238a4f09a58bf4c765a"></a>

```c
typedef int(* memc_api_read) (const struct device *dev, uint32_t addr, uint8_t *data, size_t len)
```

相关声明：[memc_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga1e7138177b931238a4f09a58bf4c765a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取外部存储器的回调 API。

<a id="r_gac495599a886be46a47dc22f6aaedcfb8"></a>

```c
typedef int(* memc_api_write) (const struct device *dev, uint32_t addr, const uint8_t *data, size_t len)
```

相关声明：[memc_api_write](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gac495599a886be46a47dc22f6aaedcfb8)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入外部存储器的回调 API。

<a id="r_ga2c33e74e81bbc4aaaef0a577737ebdcb"></a>

```c
typedef int(* memc_api_get_size) (const struct device *dev, uint64_t *size)
```

相关声明：[memc_api_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga2c33e74e81bbc4aaaef0a577737ebdcb)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

获取外部存储器大小的回调 API。

<a id="r_gada700c92c23e9a59eea6012594e8866d"></a>

```c
typedef int(* memc_api_read_id) (const struct device *dev, uint8_t *id, size_t len)
```

相关声明：[memc_api_read_id](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gada700c92c23e9a59eea6012594e8866d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取外部存储器 ID 的回调 API。

<a id="r_ga0311584e35d2ad24e92bb9999ca76510"></a>

```c
typedef void *(* memc_api_get_mem_base) (const struct device *dev)
```

相关声明：[memc_api_get_mem_base](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga0311584e35d2ad24e92bb9999ca76510)、[device](../device_reference/P002_设备对象结构.md)。

获取外部存储器基地址的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.3\_函数（Functions）

<a id="r_ga7b766a76f3bffe8b89eafb93c4f16cae"></a>

```c
int memc_read (const struct device *dev, uint32_t addr, uint8_t *data, size_t len)
```

相关声明：[memc_read](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga7b766a76f3bffe8b89eafb93c4f16cae)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从外部存储器读取数据。

<a id="r_ga8c08116a54ccb2765822ba20ba77ed39"></a>

```c
int memc_write (const struct device *dev, uint32_t addr, const uint8_t *data, size_t len)
```

相关声明：[memc_write](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga8c08116a54ccb2765822ba20ba77ed39)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向外部存储器写入数据。

<a id="r_gac48976493664e5c68c5b6a90ae8dd960"></a>

```c
static void * memc_get_mem_base (const struct device *dev)
```

相关声明：[memc_get_mem_base](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#gac48976493664e5c68c5b6a90ae8dd960)、[device](../device_reference/P002_设备对象结构.md)。

获取存储控制器（MEMC）设备的内存映射基地址。

<a id="r_ga02bca9fd387ac26841394a73d51dbe7e"></a>

```c
int memc_get_size (const struct device *dev, uint64_t *size)
```

相关声明：[memc_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga02bca9fd387ac26841394a73d51dbe7e)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

获取外部存储器的大小。

<a id="r_gaf797d9df098f75ce12e69223f759364b"></a>

```c
int memc_read_id (const struct device *dev, uint8_t *id, size_t len)
```

相关声明：[memc_read_id](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#gaf797d9df098f75ce12e69223f759364b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取外部存储器的 ID。


## 14.4\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/memc_8h_source.html)
- [memc_driver_api](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md)
- [memc_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga1e7138177b931238a4f09a58bf4c765a)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [memc_api_write](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gac495599a886be46a47dc22f6aaedcfb8)
- [memc_api_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga2c33e74e81bbc4aaaef0a577737ebdcb)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [memc_api_read_id](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gada700c92c23e9a59eea6012594e8866d)
- [memc_api_get_mem_base](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga0311584e35d2ad24e92bb9999ca76510)
- [memc_read](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga7b766a76f3bffe8b89eafb93c4f16cae)
- [memc_write](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga8c08116a54ccb2765822ba20ba77ed39)
- [memc_get_mem_base](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#gac48976493664e5c68c5b6a90ae8dd960)
- [memc_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga02bca9fd387ac26841394a73d51dbe7e)
- [memc_read_id](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#gaf797d9df098f75ce12e69223f759364b)

<a id="header-details"></a>

---

[上一章](P013_zephyr__pmci__mctp__mctp_usb.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__sd__sd_spec.h_头文件参考.md)
