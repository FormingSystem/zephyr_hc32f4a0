---
id: learning.zephyr-docs.api-file-network-device-reference.page-22
title: zephyr__drivers__mfd__mc146818.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mc146818_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_drivers\_\_mfd\_\_mc146818.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mc146818_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.1\_函数（Functions）

<a id="r_aa465a8868cbc23916b99326fa0353fe7"></a>

```c
uint8_t mfd_mc146818_std_read (const struct device *dev, uint8_t offset)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mfd_mc146818_std_read](#aa465a8868cbc23916b99326fa0353fe7)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取标准存储体（Standard Memory Bank）中指定偏移处的值。

<a id="r_ac6c5fc17f16874d9759ba5fd77d62447"></a>

```c
void mfd_mc146818_std_write (const struct device *dev, uint8_t offset, uint8_t value)
```

相关声明：[mfd_mc146818_std_write](#ac6c5fc17f16874d9759ba5fd77d62447)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入标准存储体（Standard Memory Bank）中指定偏移处的值。

<a id="r_a590a63a3683f3cd8d6bb523fee99f660"></a>

```c
uint8_t mfd_mc146818_ext_read (const struct device *dev, uint8_t offset)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mfd_mc146818_ext_read](#a590a63a3683f3cd8d6bb523fee99f660)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取扩展存储体（Extended Memory Bank）中指定偏移处的值。

<a id="r_af22b2a52764840a0be1382ed61257aa8"></a>

```c
void mfd_mc146818_ext_write (const struct device *dev, uint8_t offset, uint8_t value)
```

相关声明：[mfd_mc146818_ext_write](#af22b2a52764840a0be1382ed61257aa8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入扩展存储体（Extended Memory Bank）中指定偏移处的值。

## 22.2\_详细说明（Detailed Documentation）

<a id="a590a63a3683f3cd8d6bb523fee99f660"></a>

### `mfd_mc146818_ext_read()`

```c
uint8_t mfd_mc146818_ext_read ( const struct device * dev, uint8_t offset )
```

读取扩展存储体（Extended Memory Bank）中指定偏移处的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MC146818 多功能设备（MFD）。 |
| `offset` | 要读取的内存偏移（Memory Offset）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 位于该偏移处的值。 |

<a id="af22b2a52764840a0be1382ed61257aa8"></a>

### `mfd_mc146818_ext_write()`

```c
void mfd_mc146818_ext_write ( const struct device * dev, uint8_t offset, uint8_t value )
```

写入扩展存储体（Extended Memory Bank）中指定偏移处的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MC146818 多功能设备（MFD）。 |
| `offset` | 要写入的内存偏移（Memory Offset）。 |
| `value` | 要写入该偏移处的值。 |

<a id="aa465a8868cbc23916b99326fa0353fe7"></a>

### `mfd_mc146818_std_read()`

```c
uint8_t mfd_mc146818_std_read ( const struct device * dev, uint8_t offset )
```

读取标准存储体（Standard Memory Bank）中指定偏移处的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MC146818 多功能设备（MFD）。 |
| `offset` | 要读取的内存偏移（Memory Offset）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 位于该偏移处的值。 |

<a id="ac6c5fc17f16874d9759ba5fd77d62447"></a>

### `mfd_mc146818_std_write()`

```c
void mfd_mc146818_std_write ( const struct device * dev, uint8_t offset, uint8_t value )
```

写入标准存储体（Standard Memory Bank）中指定偏移处的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | MC146818 多功能设备（MFD）。 |
| `offset` | 要写入的内存偏移（Memory Offset）。 |
| `value` | 要写入该偏移处的值。 |


## 22.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P488_mc146818.h_源码浏览.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P021_zephyr__drivers__sensor__max32664c.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__mgmt__mcumgr__mgmt__mgmt.h_文件参考.md)
