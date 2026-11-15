---
id: learning.zephyr-docs.hardware.backend-3
title: EEPROM驱动后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第49章\_EEPROM驱动后端接口

原文：[group__eeprom__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface__backend.html)。读取日期：2026-10-13，`latest`。

<a id="details"></a>
<a id="doc-typedef-members"></a>
<a id="header-details"></a>
<a id="header-doc-typedef-members"></a>
<a id="header-nested-classes"></a>
<a id="header-typedef-members"></a>
<a id="nested-classes"></a>
<a id="r_eeprom_5Fdriver_5Fapi"></a>
<a id="typedef-members"></a>

## 49.1\_EEPROM驱动后端

本组提供实现 **电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）**驱动所需的 **应用程序编程接口（Application Programming Interface，API）**类型、回调签名及辅助内容。官方头文件为 `zephyr/drivers/eeprom.h`。

`struct eeprom_driver_api` 是EEPROM驱动操作结构，见[结构参考](P054_EEPROM驱动操作结构.md)。下面的 **回调函数（Callback Function）**类型分别定义驱动读取、写入及容量查询操作。

## 49.2\_读写操作类型

<a id="gaa12f5fdb02e73a608d5fdf128b14b4be"></a>
<a id="r_gaa12f5fdb02e73a608d5fdf128b14b4be"></a>
<a id="gaee46582bce50cf50cc0293d006ca2ba8"></a>
<a id="r_gaee46582bce50cf50cc0293d006ca2ba8"></a>

```c
typedef int (*eeprom_api_read)(const struct device *dev, off_t offset,
                              void *data, size_t len);
typedef int (*eeprom_api_write)(const struct device *dev, off_t offset,
                               const void *data, size_t len);
```

[`eeprom_api_read`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface__backend.html#gaa12f5fdb02e73a608d5fdf128b14b4be) 在读取EEPROM时调用，参数说明见 [`eeprom_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface.html#ga92b92c8fb721f1b94038a20443d46e52)；[`eeprom_api_write`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface__backend.html#gaee46582bce50cf50cc0293d006ca2ba8) 在写入EEPROM时调用，参数说明见 [`eeprom_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface.html#ga1973e8982de88f53e49154dc73461e56)。

两者的 `dev` 都是设备指针，`offset` 是起始偏移，`len` 是字节数。读取的 `data` 用于接收数据；写入的 `data` 指向待写数据，因此声明带有 `const`。公共接口成功返回0、失败返回负错误码，完整说明见[EEPROM接口参考](P040_EEPROM接口参考.md)。

## 49.3\_容量查询类型

[`eeprom_api_size`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface__backend.html#gabbf1d1f66944f2297c68686a7db080ac) 在获取EEPROM容量时调用：

<a id="gabbf1d1f66944f2297c68686a7db080ac"></a>
<a id="r_gabbf1d1f66944f2297c68686a7db080ac"></a>

```c
typedef size_t (*eeprom_api_size)(const struct device *dev);
```

它接收设备指针 `dev`；原文将参数说明指向 [`eeprom_get_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface.html#ga27a1f50af8916f9291dad4a63796a707)。返回类型是 `size_t`，表示字节容量，与读写回调的操作状态不同。

对应的完整[头文件参考](../flash_reference/P021_EEPROM公共头文件参考.md)和[源码浏览译文](../flash_reference/P022_EEPROM公共头文件源码.md)已补齐，类型、条件声明和调用转发可继续对照。

[上一章：熵源驱动后端接口](P048_熵源驱动后端接口.md) · [下一章：CAN收发器驱动后端接口](P050_CAN收发器驱动后端接口.md) · [返回大纲](大纲.md)
