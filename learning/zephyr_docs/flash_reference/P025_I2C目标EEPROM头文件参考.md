---
id: learning.zephyr-docs.flash-reference.page-25
title: I2C目标EEPROM头文件参考
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/i2c_2target_2eeprom_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_I2C目标EEPROM头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/i2c_2target_2eeprom_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是Flash与EEPROM存储驱动应用程序接口（Application Programming Interface，API）参考。Flash部分配合[Flash概述](../hardware/P012_Flash闪存.md)，EEPROM部分配合[EEPROM公共接口](../hardware/P040_EEPROM接口参考.md)阅读；模拟器（Simulator）、伪函数（Fake Function）与I²C目标设备（Target Device）分别说明，不能互相当作实板验证。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

集成电路间总线（Inter-Integrated Circuit，I²C）EEPROM 目标驱动（Target Driver）的公共 API。

<a id="details"></a>

```c
#include <stddef.h>
#include <sys/types.h>
```

查看此文件的源码。入口：[源码浏览译文](P026_I2C目标EEPROM头文件源码.md)。

集成电路间总线（Inter-Integrated Circuit，I²C）EEPROM 目标驱动（Target Driver）的公共 API。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 25.1\_类型定义（Typedefs）

<a id="r_ga769f4b319013956d58fdc56d378519aa"></a>

```c
typedef void(* eeprom_target_changed_handler_t) (const struct device *dev, void *user_data)
```

相关声明：[eeprom_target_changed_handler_t](../hardware/P313_I2CEEPROM目标接口.md#ga769f4b319013956d58fdc56d378519aa)、[device](../device_reference/P002_设备对象结构.md)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.2\_函数（Functions）

<a id="r_gaab87512e92f7f50b93019c5f9255c4a7"></a>

```c
void eeprom_target_set_changed_callback (const struct device *dev, eeprom_target_changed_handler_t handler, void *user_data)
```

相关声明：[eeprom_target_set_changed_callback](../hardware/P313_I2CEEPROM目标接口.md#gaab87512e92f7f50b93019c5f9255c4a7)、[device](../device_reference/P002_设备对象结构.md)、[eeprom_target_changed_handler_t](../hardware/P313_I2CEEPROM目标接口.md#ga769f4b319013956d58fdc56d378519aa)。

设置 EEPROM 内容变更回调处理函数。

<a id="r_ga3da67a267034e3b90c1a7c84588c3839"></a>

```c
size_t eeprom_target_get_size (const struct device *dev)
```

相关声明：[eeprom_target_get_size](../hardware/P313_I2CEEPROM目标接口.md#ga3da67a267034e3b90c1a7c84588c3839)、[device](../device_reference/P002_设备对象结构.md)。

取得虚拟 EEPROM（Virtual EEPROM）的大小。

<a id="r_ga1543dbc12e26df856eac01b1a686d7c5"></a>

```c
int eeprom_target_read_data (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[eeprom_target_read_data](../hardware/P313_I2CEEPROM目标接口.md#ga1543dbc12e26df856eac01b1a686d7c5)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

从虚拟 EEPROM 读取数据。

<a id="r_gad562c9ac13d3fa7a7b43c1d8ba415f11"></a>

```c
int eeprom_target_write_data (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[eeprom_target_write_data](../hardware/P313_I2CEEPROM目标接口.md#gad562c9ac13d3fa7a7b43c1d8ba415f11)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

向虚拟 EEPROM 写入数据。

<a id="r_ga8c2d7c18fcec4ce2241850f031966a89"></a>

```c
static int eeprom_target_program (const struct device *dev, const uint8_t *eeprom_data, unsigned int length)
```

相关声明：[eeprom_target_program](../hardware/P313_I2CEEPROM目标接口.md#ga8c2d7c18fcec4ce2241850f031966a89)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

对虚拟 EEPROM 的存储内容编程。

<a id="r_ga72b88bc1df1ec097ed677f94e9dad875"></a>

```c
static int eeprom_target_read (const struct device *dev, uint8_t *eeprom_data, unsigned int offset)
```

相关声明：[eeprom_target_read](../hardware/P313_I2CEEPROM目标接口.md#ga72b88bc1df1ec097ed677f94e9dad875)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

读取虚拟 EEPROM 存储空间中的单个字节。

<a id="r_ga802f5d779e9a837a81b8b617037dfce8"></a>

```c
int eeprom_target_set_addr (const struct device *dev, uint8_t addr)
```

相关声明：[eeprom_target_set_addr](../hardware/P313_I2CEEPROM目标接口.md#ga802f5d779e9a837a81b8b617037dfce8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在运行时修改 EEPROM 目标设备的地址。

## 25.3\_源码定位与使用边界

本页提供I²C EEPROM目标设备（Target Device）的头文件摘要，完整调用语义见[I2C目标EEPROM接口](../hardware/P313_I2CEEPROM目标接口.md)及[源码浏览译文](P026_I2C目标EEPROM头文件源码.md)。本地跟踪：[目标头文件](../../../include/zephyr/drivers/i2c/target/eeprom.h)与[eeprom_target.c](../../../drivers/i2c/target/eeprom_target.c)。

> 译注——旧包装与运行时地址：eeprom_target_program已弃用，转发到offset为0的eeprom_target_write_data；eeprom_target_read则转发到指定偏移、长度为1的eeprom_target_read_data。当前eeprom_target_set_addr实现受CONFIG_I2C_EEPROM_TARGET_RUNTIME_ADDR控制；头文件中的无条件声明不保证所有构建均提供该实现。该驱动表示本机作为I²C目标端，不等于通过控制器接口访问外部EEPROM。

各页官方来源及源码摘要见[来源记录](../SOURCES.md)。本批仅翻译和核对代码，没有运行模拟测试、构建、擦写存储或执行实板通信。

## 25.4\_原页交叉引用（Cross References）

- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h_source.html)
- [查看此文件源码](P026_I2C目标EEPROM头文件源码.md)
- [eeprom_target_changed_handler_t](../hardware/P313_I2CEEPROM目标接口.md#ga769f4b319013956d58fdc56d378519aa)
- [device](../device_reference/P002_设备对象结构.md)
- [eeprom_target_set_changed_callback](../hardware/P313_I2CEEPROM目标接口.md#gaab87512e92f7f50b93019c5f9255c4a7)
- [eeprom_target_get_size](../hardware/P313_I2CEEPROM目标接口.md#ga3da67a267034e3b90c1a7c84588c3839)
- [eeprom_target_read_data](../hardware/P313_I2CEEPROM目标接口.md#ga1543dbc12e26df856eac01b1a686d7c5)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [eeprom_target_write_data](../hardware/P313_I2CEEPROM目标接口.md#gad562c9ac13d3fa7a7b43c1d8ba415f11)
- [eeprom_target_program](../hardware/P313_I2CEEPROM目标接口.md#ga8c2d7c18fcec4ce2241850f031966a89)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [eeprom_target_read](../hardware/P313_I2CEEPROM目标接口.md#ga72b88bc1df1ec097ed677f94e9dad875)
- [eeprom_target_set_addr](../hardware/P313_I2CEEPROM目标接口.md#ga802f5d779e9a837a81b8b617037dfce8)

<a id="header-details"></a>

---

[上一章](P024_伪EEPROM头文件源码.md) · [返回大纲](大纲.md) · [下一章](P026_I2C目标EEPROM头文件源码.md)
