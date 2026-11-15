---
id: learning.zephyr-docs.flash-reference.page-23
title: 伪EEPROM头文件参考
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/eeprom__fake_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_伪EEPROM头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/eeprom__fake_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是Flash与EEPROM存储驱动应用程序接口（Application Programming Interface，API）参考。Flash部分配合[Flash概述](../hardware/P012_Flash闪存.md)，EEPROM部分配合[EEPROM公共接口](../hardware/P040_EEPROM接口参考.md)阅读；模拟器（Simulator）、伪函数（Fake Function）与I²C目标设备（Target Device）分别说明，不能互相当作实板验证。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

伪 EEPROM（Fake EEPROM）驱动的 API 函数。

<a id="details"></a>

```c
#include <zephyr/drivers/eeprom.h>
#include <zephyr/fff.h>
```

查看此文件的源码。入口：[源码浏览译文](P024_伪EEPROM头文件源码.md)。

伪 EEPROM（Fake EEPROM）驱动的 API 函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.1\_函数（Functions）

<a id="r_ga6238da3c648ca23d4be16853feee071d"></a>

```c
int fake_eeprom_read (const struct device *, off_t, void *, size_t)
```

相关声明：[fake_eeprom_read](../hardware/P051_伪EEPROM接口.md#ga6238da3c648ca23d4be16853feee071d)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

驱动操作 `eeprom_driver_api::read` 的伪实现（Fake Implementation）。

<a id="r_ga2484447bd0c4d5d43a56fd42a893de61"></a>

```c
int fake_eeprom_write (const struct device *, off_t, const void *, size_t)
```

相关声明：[fake_eeprom_write](../hardware/P051_伪EEPROM接口.md#ga2484447bd0c4d5d43a56fd42a893de61)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

驱动操作 `eeprom_driver_api::write` 的伪实现（Fake Implementation）。

<a id="r_ga0afb1c3d28fe1f0883c7a7c744edc5d8"></a>

```c
size_t fake_eeprom_size (const struct device *)
```

相关声明：[fake_eeprom_size](../hardware/P051_伪EEPROM接口.md#ga0afb1c3d28fe1f0883c7a7c744edc5d8)、[device](../device_reference/P002_设备对象结构.md)。

驱动操作 `eeprom_driver_api::size` 的伪实现（Fake Implementation）。

## 23.2\_源码定位与使用边界

伪函数框架（Fake Function Framework，FFF）用于记录调用并提供可配置行为；完整用法见[伪EEPROM接口](../hardware/P051_伪EEPROM接口.md)，声明宏见[源码浏览译文](P024_伪EEPROM头文件源码.md)。本地跟踪：[eeprom_fake.h](../../../include/zephyr/drivers/eeprom/eeprom_fake.h)、[eeprom_fake.c](../../../drivers/eeprom/eeprom_fake.c)。

> 译注——默认行为与边界：本次官方eeprom_fake.c为read与size安装默认custom_fake，并在启用CONFIG_ZTEST时于每个测试前重装。read只检查len是否大于设备树size，然后填零；未检查offset、offset+len或data有效性。write默认只提供FFF返回值和调用记录，不维护可读回的存储内容。测试边界错误、持久内容或多设备差异时，应提供自己的custom_fake，不把伪函数成功当作真实存储访问成功。

各页官方来源及源码摘要见[来源记录](../SOURCES.md)。本批仅翻译和核对代码，没有运行模拟测试、构建、擦写存储或执行实板通信。

## 23.3\_原页交叉引用（Cross References）

- [zephyr/drivers/eeprom.h](P022_EEPROM公共头文件源码.md)
- [查看此文件源码](P024_伪EEPROM头文件源码.md)
- [fake_eeprom_read](../hardware/P051_伪EEPROM接口.md#ga6238da3c648ca23d4be16853feee071d)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [eeprom_driver_api::read](../hardware/P054_EEPROM驱动操作结构.md#a821724b35926882a1a732f1fb541b965)
- [fake_eeprom_write](../hardware/P051_伪EEPROM接口.md#ga2484447bd0c4d5d43a56fd42a893de61)
- [eeprom_driver_api::write](../hardware/P054_EEPROM驱动操作结构.md#ade546770dc302ecb149a8631bbf5b5cb)
- [fake_eeprom_size](../hardware/P051_伪EEPROM接口.md#ga0afb1c3d28fe1f0883c7a7c744edc5d8)
- [eeprom_driver_api::size](../hardware/P054_EEPROM驱动操作结构.md#a82ef001ad60f95fabb37235a40974854)

<a id="header-details"></a>

---

[上一章](P022_EEPROM公共头文件源码.md) · [返回大纲](大纲.md) · [下一章](P024_伪EEPROM头文件源码.md)
