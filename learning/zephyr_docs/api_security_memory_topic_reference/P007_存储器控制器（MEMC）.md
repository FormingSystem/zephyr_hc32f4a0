---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-7
title: 存储器控制器（MEMC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_存储器控制器（MEMC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

存储器控制器（Memory Controller，MEMC）接口。

<a id="details"></a>

内存控制器（Memory Controllers，MEMC）接口。**引入版本（Since）：**4.5。**版本（Version）：**0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 7.1\_主题（Topics）

<a id="r_memc_5Finterface_5Fbackend"></a>

相关声明：[MEMC 驱动后端 API](../api_protocol_topic_reference/P030_MEMC 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 7.2\_文件（Files）

<a id="r_memc_2Eh"></a>

```c
file memc.h
```

相关声明：[memc.h](../peripheral_bus_storage_header_reference/P014_zephyr__drivers__memc.h_头文件参考.md)。

内存控制器（Memory Controller，MEMC）驱动API的主头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_ga7b766a76f3bffe8b89eafb93c4f16cae"></a>

```c
int memc_read (const struct device *dev, uint32_t addr, uint8_t *data, size_t len)
```

相关声明：[memc_read](#ga7b766a76f3bffe8b89eafb93c4f16cae)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从外部存储器读取数据。

<a id="r_ga8c08116a54ccb2765822ba20ba77ed39"></a>

```c
int memc_write (const struct device *dev, uint32_t addr, const uint8_t *data, size_t len)
```

相关声明：[memc_write](#ga8c08116a54ccb2765822ba20ba77ed39)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向外部存储器写入数据。

<a id="r_gac48976493664e5c68c5b6a90ae8dd960"></a>

```c
static void * memc_get_mem_base (const struct device *dev)
```

相关声明：[memc_get_mem_base](#gac48976493664e5c68c5b6a90ae8dd960)、[device](../device_reference/P002_设备对象结构.md)。

获取存储控制器（MEMC）设备的内存映射基地址。

<a id="r_ga02bca9fd387ac26841394a73d51dbe7e"></a>

```c
int memc_get_size (const struct device *dev, uint64_t *size)
```

相关声明：[memc_get_size](#ga02bca9fd387ac26841394a73d51dbe7e)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取外部存储器的大小。

<a id="r_gaf797d9df098f75ce12e69223f759364b"></a>

```c
int memc_read_id (const struct device *dev, uint8_t *id, size_t len)
```

相关声明：[memc_read_id](#gaf797d9df098f75ce12e69223f759364b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取外部存储器的 ID。

## 7.4\_详细说明（Detailed Documentation）

<a id="gac48976493664e5c68c5b6a90ae8dd960"></a>

### `memc_get_mem_base()`

```c
void * memc_get_mem_base ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/memc.h>
```

获取存储控制器（MEMC）设备的内存映射基地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 内存控制器（MEMC）设备。 |

**说明（Note）**：**注意（Note）：**本函数仅在内核模式（Kernel Mode）可用，不是系统调用（Syscall）。返回指针是内核空间地址，不能直接从用户空间使用。若要可移植地访问，应使用 `memc_read()`／`memc_write()`。

**返回（Returns）**：**返回值（Returns）：**映射基地址（Mapped Base Address）的指针；若不是内存映射设备，或设备未实现 memc API，则为 `NULL`。

<a id="ga02bca9fd387ac26841394a73d51dbe7e"></a>

### `memc_get_size()`

```c
int memc_get_size ( const struct device * dev, uint64_t * size )
```

```c
#include <zephyr/drivers/memc.h>
```

获取外部存储器的大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 内存控制器（MEMC）设备。 |
| `size` | 指向保存大小的变量的指针，大小以字节为单位。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 设备未实现 memc API 或可选回调时。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga7b766a76f3bffe8b89eafb93c4f16cae"></a>

### `memc_read()`

```c
int memc_read ( const struct device * dev, uint32_t addr, uint8_t * data, size_t len )
```

```c
#include <zephyr/drivers/memc.h>
```

从外部存储器读取数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 内存控制器（MEMC）设备。 |
| `addr` | 相对于基地址、要读取的位置的字节偏移量（Byte Offset）。 |
| `data` | 用于保存所读数据的缓冲区。 |
| `len` | 要读取的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 设备未实现 memc API，或 `get_mem_base` 和 `read` 均未实现时。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gaf797d9df098f75ce12e69223f759364b"></a>

### `memc_read_id()`

```c
int memc_read_id ( const struct device * dev, uint8_t * id, size_t len )
```

```c
#include <zephyr/drivers/memc.h>
```

读取外部存储器的 ID。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 内存控制器（MEMC）设备。 |
| `id` | 保存设备标识（ID）的缓冲区，大小取决于设备，通常为 2–4 字节。 |
| `len` | 要读取的字节数。若设备标识（Device ID）较短，驱动返回的字节数可以少于请求值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 设备未实现 memc API 或可选回调时。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga8c08116a54ccb2765822ba20ba77ed39"></a>

### `memc_write()`

```c
int memc_write ( const struct device * dev, uint32_t addr, const uint8_t * data, size_t len )
```

```c
#include <zephyr/drivers/memc.h>
```

向外部存储器写入数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 内存控制器（MEMC）设备。 |
| `addr` | 相对于基地址、要写入的位置的字节偏移量（Byte Offset）。 |
| `data` | 包含待写入数据的缓冲区（Buffer）。 |
| `len` | 要写入的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 设备未实现 memc API，或 `get_mem_base` 和 `write` 均未实现时。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。


## 7.5\_原页交叉引用（Cross References）

- [MEMC 驱动后端 API](../api_protocol_topic_reference/P030_MEMC 驱动后端 API.md)
- [memc.h](../peripheral_bus_storage_header_reference/P014_zephyr__drivers__memc.h_头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_管理数据输入_输出（MDIO）.md) · [返回大纲](大纲.md) · [下一章](P008_对象（Objects）.md)
