---
id: learning.zephyr-docs.flash-reference.page-19
title: Flash模拟器回调
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__simulator__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_Flash模拟器回调

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__simulator__cb.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是Flash与EEPROM存储驱动应用程序接口（Application Programming Interface，API）参考。Flash部分配合[Flash概述](../hardware/P012_Flash闪存.md)，EEPROM部分配合[EEPROM公共接口](../hardware/P040_EEPROM接口参考.md)阅读；模拟器（Simulator）、伪函数（Fake Function）与I²C目标设备（Target Device）分别说明，不能互相当作实板验证。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

Flash 模拟器回调结构体（Callbacks Structure）。

```c
#include <zephyr/drivers/flash/flash_simulator.h>
```

<a id="details"></a>

Flash 模拟器回调结构体，保存模拟器操作所用的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a62ae850896b86b36cd5c478c8bfc614b"></a>

```c
flash_simulator_write_byte_cb_t write_byte
```

相关声明：[flash_simulator_write_byte_cb_t](P017_Flash模拟器接口.md#a860ecc612edda863f4f86ec690bec979)、[write_byte](#a62ae850896b86b36cd5c478c8bfc614b)。

单字节写入回调。

<a id="r_a70774e9972fe53c2c6fd13cfb0797de1"></a>

```c
flash_simulator_erase_unit_cb_t erase_unit
```

相关声明：[flash_simulator_erase_unit_cb_t](P017_Flash模拟器接口.md#a24b9919bf5776683d1890c46ed961bd5)、[erase_unit](#a70774e9972fe53c2c6fd13cfb0797de1)。

单元擦除回调。

## 19.2\_详细说明（Detailed Documentation）

<a id="a70774e9972fe53c2c6fd13cfb0797de1"></a>

### `erase_unit`

```c
flash_simulator_erase_unit_cb_t flash_simulator_cb::erase_unit
```

单元擦除回调。

<a id="a62ae850896b86b36cd5c478c8bfc614b"></a>

### `write_byte`

```c
flash_simulator_write_byte_cb_t flash_simulator_cb::write_byte
```

单字节写入回调。

## 19.3\_源码定位与使用边界

本组包含[模拟器API](P017_Flash模拟器接口.md)、[参数](P018_Flash模拟器参数.md)、[回调结构](P019_Flash模拟器回调.md)及[头文件源码](P020_Flash模拟器头文件源码.md)。源码跟踪：[flash_simulator.h](../../../include/zephyr/drivers/flash/flash_simulator.h)和[flash_simulator.c](../../../drivers/flash/flash_simulator.c)。译注核对的官方[头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash/flash_simulator.h)与[驱动实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_simulator.c)分别记录摘要；本地版本可能不同。

各页官方来源及源码摘要见[来源记录](../SOURCES.md)。本批仅翻译和核对代码，没有运行模拟测试、构建、擦写存储或执行实板通信。

## 19.4\_原页交叉引用（Cross References）

- [zephyr/drivers/flash/flash_simulator.h](P020_Flash模拟器头文件源码.md)
- [flash_simulator_write_byte_cb_t](P017_Flash模拟器接口.md#a860ecc612edda863f4f86ec690bec979)
- [flash_simulator_erase_unit_cb_t](P017_Flash模拟器接口.md#a24b9919bf5776683d1890c46ed961bd5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_Flash模拟器参数.md) · [返回大纲](大纲.md) · [下一章](P020_Flash模拟器头文件源码.md)
