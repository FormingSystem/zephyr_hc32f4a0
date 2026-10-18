---
id: learning.zephyr-docs.flash-reference.page-21
title: EEPROM公共头文件参考
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/eeprom_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_EEPROM公共头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/eeprom_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是Flash与EEPROM存储驱动应用程序接口（Application Programming Interface，API）参考。Flash部分配合[Flash概述](../hardware/P012_Flash闪存.md)，EEPROM部分配合[EEPROM公共接口](../hardware/P040_EEPROM接口参考.md)阅读；模拟器（Simulator）、伪函数（Fake Function）与I²C目标设备（Target Device）分别说明，不能互相当作实板验证。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

电可擦可编程只读存储器（Electrically Erasable Programmable Read-only Memory，EEPROM）驱动 API 的主头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <stddef.h>
#include <sys/types.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/eeprom.h>
```

查看此文件的源码。入口：[源码浏览译文](P022_EEPROM公共头文件源码.md)。

电可擦可编程只读存储器（Electrically Erasable Programmable Read-only Memory，EEPROM）驱动 API 的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_eeprom_5Fdriver_5Fapi"></a>

```c
struct eeprom_driver_api
```

相关声明：[eeprom_driver_api](../hardware/P054_EEPROM驱动操作结构.md)。

驱动操作（Driver Operations）：EEPROM 驱动的操作集合。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 21.2\_类型定义（Typedefs）

<a id="r_gaa12f5fdb02e73a608d5fdf128b14b4be"></a>

```c
typedef int(* eeprom_api_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[eeprom_api_read](../hardware/P049_EEPROM驱动后端接口.md#gaa12f5fdb02e73a608d5fdf128b14b4be)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

从 EEPROM 读取时调用的回调 API。

<a id="r_gaee46582bce50cf50cc0293d006ca2ba8"></a>

```c
typedef int(* eeprom_api_write) (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[eeprom_api_write](../hardware/P049_EEPROM驱动后端接口.md#gaee46582bce50cf50cc0293d006ca2ba8)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

向 EEPROM 写入时调用的回调 API。

<a id="r_gabbf1d1f66944f2297c68686a7db080ac"></a>

```c
typedef size_t(* eeprom_api_size) (const struct device *dev)
```

相关声明：[eeprom_api_size](../hardware/P049_EEPROM驱动后端接口.md#gabbf1d1f66944f2297c68686a7db080ac)、[device](../device_reference/P002_设备对象结构.md)。

取得 EEPROM 容量时调用的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.3\_函数（Functions）

<a id="r_ga92b92c8fb721f1b94038a20443d46e52"></a>

```c
int eeprom_read (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[eeprom_read](../hardware/P040_EEPROM接口参考.md#ga92b92c8fb721f1b94038a20443d46e52)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

从 EEPROM 读取数据。

<a id="r_ga1973e8982de88f53e49154dc73461e56"></a>

```c
int eeprom_write (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[eeprom_write](../hardware/P040_EEPROM接口参考.md#ga1973e8982de88f53e49154dc73461e56)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

向 EEPROM 写入数据。

<a id="r_ga27a1f50af8916f9291dad4a63796a707"></a>

```c
size_t eeprom_get_size (const struct device *dev)
```

相关声明：[eeprom_get_size](../hardware/P040_EEPROM接口参考.md#ga27a1f50af8916f9291dad4a63796a707)、[device](../device_reference/P002_设备对象结构.md)。

取得 EEPROM 容量，单位为字节。

## 21.4\_源码定位与使用边界

此页保留官方头文件摘要，完整参数与返回值见[EEPROM公共API](../hardware/P040_EEPROM接口参考.md)、[驱动后端](../hardware/P049_EEPROM驱动后端接口.md)和[驱动操作结构](../hardware/P054_EEPROM驱动操作结构.md)。可继续查看[源码浏览译文](P022_EEPROM公共头文件源码.md)，或相对定位到仓库的[eeprom.h](../../../include/zephyr/drivers/eeprom.h)。

> 译注——转发层：头文件中的三个z_impl_eeprom_*包装通过DEVICE_API_GET取得驱动操作表，再调用read、write或size。具体范围校验由相应驱动负责；不能把头文件存在这些声明理解为调用时自动完成所有参数检查。

各页官方来源及源码摘要见[来源记录](../SOURCES.md)。本批仅翻译和核对代码，没有运行模拟测试、构建、擦写存储或执行实板通信。

## 21.5\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件源码](P022_EEPROM公共头文件源码.md)
- [eeprom_driver_api](../hardware/P054_EEPROM驱动操作结构.md)
- [eeprom_api_read](../hardware/P049_EEPROM驱动后端接口.md#gaa12f5fdb02e73a608d5fdf128b14b4be)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [eeprom_api_write](../hardware/P049_EEPROM驱动后端接口.md#gaee46582bce50cf50cc0293d006ca2ba8)
- [eeprom_api_size](../hardware/P049_EEPROM驱动后端接口.md#gabbf1d1f66944f2297c68686a7db080ac)
- [eeprom_read](../hardware/P040_EEPROM接口参考.md#ga92b92c8fb721f1b94038a20443d46e52)
- [eeprom_write](../hardware/P040_EEPROM接口参考.md#ga1973e8982de88f53e49154dc73461e56)
- [eeprom_get_size](../hardware/P040_EEPROM接口参考.md#ga27a1f50af8916f9291dad4a63796a707)

<a id="header-details"></a>

---

[上一章](P020_Flash模拟器头文件源码.md) · [返回大纲](大纲.md) · [下一章](P022_EEPROM公共头文件源码.md)
