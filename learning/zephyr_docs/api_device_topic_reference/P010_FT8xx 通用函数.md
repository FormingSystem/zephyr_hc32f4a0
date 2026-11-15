---
id: learning.zephyr-docs.api-device-topic-reference.page-10
title: FT8xx 通用函数
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_FT8xx 通用函数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FT8xx 内存读写函数。

<a id="details"></a>

FT8xx 内存读写函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.1\_函数（Functions）

<a id="r_ga2c8c5d06b09549ab041bbff4612b4620"></a>

```c
void ft8xx_wr8 (const struct device *dev, uint32_t address, uint8_t data)
```

相关声明：[ft8xx_wr8](#ga2c8c5d06b09549ab041bbff4612b4620)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 FT8xx 存储器写入 1 字节（8 位）。

<a id="r_gaa6d306b1e2701e0de415c64d33e575a4"></a>

```c
void ft8xx_wr16 (const struct device *dev, uint32_t address, uint16_t data)
```

相关声明：[ft8xx_wr16](#gaa6d306b1e2701e0de415c64d33e575a4)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 FT8xx 存储器写入 2 字节（16 位）。

<a id="r_gada8d996d58f0f46f3f56534ee0da4c68"></a>

```c
void ft8xx_wr32 (const struct device *dev, uint32_t address, uint32_t data)
```

相关声明：[ft8xx_wr32](#gada8d996d58f0f46f3f56534ee0da4c68)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 FT8xx 存储器写入 4 字节（32 位）。

<a id="r_gab8235ed0c0f7373628457fcf64e15fbd"></a>

```c
uint8_t ft8xx_rd8 (const struct device *dev, uint32_t address)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ft8xx_rd8](#gab8235ed0c0f7373628457fcf64e15fbd)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 FT8xx 存储器读取 1 字节（8 位）。

<a id="r_ga743c2d25f728451e98417b2ebcc9c722"></a>

```c
uint16_t ft8xx_rd16 (const struct device *dev, uint32_t address)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[ft8xx_rd16](#ga743c2d25f728451e98417b2ebcc9c722)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 FT8xx 存储器读取 2 字节（16 位）。

<a id="r_gaed670a8410224f8f3970fad86705f513"></a>

```c
uint32_t ft8xx_rd32 (const struct device *dev, uint32_t address)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[ft8xx_rd32](#gaed670a8410224f8f3970fad86705f513)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 FT8xx 存储器读取 4 字节（32 位）。

## 10.2\_详细说明（Detailed Documentation）

<a id="ga743c2d25f728451e98417b2ebcc9c722"></a>

### `ft8xx_rd16()`

```c
uint16_t ft8xx_rd16 ( const struct device * dev, uint32_t address )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_common.h>
```

从 FT8xx 存储器读取 2 字节（16 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `address` | 要读取的内存地址（memory address）。 |

**返回（Returns）**：返回值：从内存读取的值。

<a id="gaed670a8410224f8f3970fad86705f513"></a>

### `ft8xx_rd32()`

```c
uint32_t ft8xx_rd32 ( const struct device * dev, uint32_t address )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_common.h>
```

从 FT8xx 存储器读取 4 字节（32 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `address` | 要读取的内存地址（memory address）。 |

**返回（Returns）**：返回值：从内存读取的值。

<a id="gab8235ed0c0f7373628457fcf64e15fbd"></a>

### `ft8xx_rd8()`

```c
uint8_t ft8xx_rd8 ( const struct device * dev, uint32_t address )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_common.h>
```

从 FT8xx 存储器读取 1 字节（8 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `address` | 要读取的内存地址（memory address）。 |

**返回（Returns）**：返回值：从内存读取的值。

<a id="gaa6d306b1e2701e0de415c64d33e575a4"></a>

### `ft8xx_wr16()`

```c
void ft8xx_wr16 ( const struct device * dev, uint32_t address, uint16_t data )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_common.h>
```

向 FT8xx 存储器写入 2 字节（16 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `address` | 要写入的内存地址。 |
| `data` | 要写入的值。 |

<a id="gada8d996d58f0f46f3f56534ee0da4c68"></a>

### `ft8xx_wr32()`

```c
void ft8xx_wr32 ( const struct device * dev, uint32_t address, uint32_t data )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_common.h>
```

向 FT8xx 存储器写入 4 字节（32 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `address` | 要写入的内存地址。 |
| `data` | 要写入的值。 |

<a id="ga2c8c5d06b09549ab041bbff4612b4620"></a>

### `ft8xx_wr8()`

```c
void ft8xx_wr8 ( const struct device * dev, uint32_t address, uint8_t data )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_common.h>
```

向 FT8xx 存储器写入 1 字节（8 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `address` | 要写入的内存地址。 |
| `data` | 待写入的字节（Byte）。 |


## 10.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/drivers/misc/ft8xx/ft8xx_common.h](../api_file_management_reference/P017_zephyr__drivers__misc__ft8xx__ft8xx_common.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_FPGA 驱动后端 API（Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P011_INA2XX API主题.md)
