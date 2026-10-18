---
id: learning.zephyr-docs.flash-reference.page-18
title: Flash模拟器参数
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__simulator__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_Flash模拟器参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__simulator__params.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是Flash与EEPROM存储驱动应用程序接口（Application Programming Interface，API）参考。Flash部分配合[Flash概述](../hardware/P012_Flash闪存.md)，EEPROM部分配合[EEPROM公共接口](../hardware/P040_EEPROM接口参考.md)阅读；模拟器（Simulator）、伪函数（Fake Function）与I²C目标设备（Target Device）分别说明，不能互相当作实板验证。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

Flash 模拟器参数结构体（Parameters Structure）。

```c
#include <zephyr/drivers/flash/flash_simulator.h>
```

<a id="details"></a>

Flash 模拟器参数结构体。这是保存模拟器参数的辅助结构，供能够改变模拟器驱动行为的回调使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a4c9c5d6c1a9876044e05457353e0bb46"></a>

```c
size_t memory_size
```

相关声明：[memory_size](#a4c9c5d6c1a9876044e05457353e0bb46)。

存储空间总大小。

<a id="r_a4159a11d6b52a5afc8a98eda6a1f6de6"></a>

```c
size_t base_offset
```

相关声明：[base_offset](#a4159a11d6b52a5afc8a98eda6a1f6de6)。

Flash 模拟器的基准偏移（Base Offset）。

<a id="r_a84d687fd28d14b59019ee0e881c1ff0e"></a>

```c
size_t erase_unit
```

相关声明：[erase_unit](#a84d687fd28d14b59019ee0e881c1ff0e)。

擦除单元（Erase Unit）的大小。

<a id="r_a7a4c60e8a1d7f3c4761cc8d58e2d1fc1"></a>

```c
size_t prog_unit
```

相关声明：[prog_unit](#a7a4c60e8a1d7f3c4761cc8d58e2d1fc1)。

编程单元（Program Unit）的大小。

<a id="r_ab30c470b8f3638bba19ee5dae2bddb68"></a>

```c
bool explicit_erase
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[explicit_erase](#ab30c470b8f3638bba19ee5dae2bddb68)。

是否要求显式擦除（Explicit Erase）。

<a id="r_a36ce56491f38836e9cf3f797cf6117e2"></a>

```c
uint8_t erase_value
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[erase_value](#a36ce56491f38836e9cf3f797cf6117e2)。

用于表示已擦除存储内容的值。

## 18.2\_详细说明（Detailed Documentation）

<a id="a4159a11d6b52a5afc8a98eda6a1f6de6"></a>

### `base_offset`

```c
size_t flash_simulator_params::base_offset
```

Flash 模拟器的基准偏移（Base Offset）。

> 译注——源码核对：本字段由设备树中的存储区域起始地址生成；当前模拟器读写范围按0～memory_size检查，底层RAM按设备内offset索引。不要仅因为存在base_offset，就把它无条件加到传给flash_read、flash_write或flash_erase的偏移上。

<a id="a84d687fd28d14b59019ee0e881c1ff0e"></a>

### `erase_unit`

```c
size_t flash_simulator_params::erase_unit
```

擦除单元（Erase Unit）的大小。

<a id="a36ce56491f38836e9cf3f797cf6117e2"></a>

### `erase_value`

```c
uint8_t flash_simulator_params::erase_value
```

用于表示已擦除存储内容的值。

<a id="ab30c470b8f3638bba19ee5dae2bddb68"></a>

### `explicit_erase`

```c
bool flash_simulator_params::explicit_erase
```

是否要求显式擦除（Explicit Erase）。

<a id="a4c9c5d6c1a9876044e05457353e0bb46"></a>

### `memory_size`

```c
size_t flash_simulator_params::memory_size
```

存储空间总大小。

<a id="a7a4c60e8a1d7f3c4761cc8d58e2d1fc1"></a>

### `prog_unit`

```c
size_t flash_simulator_params::prog_unit
```

编程单元（Program Unit）的大小。

## 18.3\_源码定位与使用边界

本组包含[模拟器API](P017_Flash模拟器接口.md)、[参数](P018_Flash模拟器参数.md)、[回调结构](P019_Flash模拟器回调.md)及[头文件源码](P020_Flash模拟器头文件源码.md)。源码跟踪：[flash_simulator.h](../../../include/zephyr/drivers/flash/flash_simulator.h)和[flash_simulator.c](../../../drivers/flash/flash_simulator.c)。译注核对的官方[头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash/flash_simulator.h)与[驱动实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_simulator.c)分别记录摘要；本地版本可能不同。

各页官方来源及源码摘要见[来源记录](../SOURCES.md)。本批仅翻译和核对代码，没有运行模拟测试、构建、擦写存储或执行实板通信。

## 18.4\_原页交叉引用（Cross References）

- [zephyr/drivers/flash/flash_simulator.h](P020_Flash模拟器头文件源码.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_Flash模拟器接口.md) · [返回大纲](大纲.md) · [下一章](P019_Flash模拟器回调.md)
