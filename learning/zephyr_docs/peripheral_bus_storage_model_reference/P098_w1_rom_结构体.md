---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-98
title: w1_rom_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structw1__rom.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_w1\_rom\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structw1__rom.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

W1_rom结构。

```c
#include <zephyr/drivers/w1.h>
```

<a id="details"></a>

W1_rom结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 98.1\_数据成员（Data Fields）

<a id="r_adc7f4f9fca172392b11864a17424a14c"></a>

```c
uint8_t family
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[family](#adc7f4f9fca172392b11864a17424a14c)。

用于标识从设备类型的 1-Wire 家族代码（Family code）。

<a id="r_a134ee6d6e5e5eb711caf59449d11732e"></a>

```c
uint8_t serial [6]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[serial](#a134ee6d6e5e5eb711caf59449d11732e)。

序列号（Serial）与家族代码共同组成唯一的 56 位 ID。

<a id="r_a73d85d7ce0ef671027c910b9b7a54165"></a>

```c
uint8_t crc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[crc](#a73d85d7ce0ef671027c910b9b7a54165)。

56 位唯一 ID 的 8 位校验和（Checksum）。

## 98.2\_详细说明（Detailed Documentation）

<a id="a73d85d7ce0ef671027c910b9b7a54165"></a>

### `crc`

```c
uint8_t w1_rom::crc
```

56 位唯一 ID 的 8 位校验和（Checksum）。

<a id="adc7f4f9fca172392b11864a17424a14c"></a>

### `family`

```c
uint8_t w1_rom::family
```

用于标识从设备类型的 1-Wire 家族代码（Family code）。

部分家族代码列于[1-Wire 软件资源指南：设备说明](https://www.analog.com/en/resources/technical-articles/1wire-software-resource-guide-device-description.html)；其他代码见对应设备的数据手册。

<a id="a134ee6d6e5e5eb711caf59449d11732e"></a>

### `serial`

```c
uint8_t w1_rom::serial[6]
```

序列号（Serial）与家族代码共同组成唯一的 56 位 ID。

本数据类型文档由以下文件生成：

- `zephyr/drivers/w1.h`

## 98.3\_原页交叉引用（Cross References）

- [w1_rom](P098_w1_rom_结构体.md)
- [zephyr/drivers/w1.h](https://docs.zephyrproject.org/latest/doxygen/html/w1_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [https://www.analog.com/en/resources/technical-articles/1wire-software-resource-guide-device-description.html](https://www.analog.com/en/resources/technical-articles/1wire-software-resource-guide-device-description.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P097_w1_master_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P099_w1_slave_config_结构体.md)
