---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-1
title: ccs811_configver_type_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structccs811__configver__type.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_ccs811\_configver\_type\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structccs811__configver__type.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

获取CCS811静态状态的信息。

```c
#include <zephyr/drivers/sensor/ccs811.h>
```

<a id="details"></a>

获取 CCS811 静态状态信息，包括配置的工作模式以及硬件和固件版本。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a78d15d9b7695cc7dd4251cecd573a18a"></a>

```c
uint16_t fw_boot_version
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fw_boot_version](#a78d15d9b7695cc7dd4251cecd573a18a)。

<a id="r_add87f032fef47ad3c4b6415a9aeb829d"></a>

```c
uint16_t fw_app_version
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fw_app_version](#add87f032fef47ad3c4b6415a9aeb829d)。

<a id="r_ad76906d24bd14e63dd7a4c1628fd81cc"></a>

```c
uint8_t hw_version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hw_version](#ad76906d24bd14e63dd7a4c1628fd81cc)。

<a id="r_aa8dad67bbdd286a54749e421967d228d"></a>

```c
uint8_t mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode](#aa8dad67bbdd286a54749e421967d228d)。

## 1.2\_详细说明（Detailed Documentation）

<a id="add87f032fef47ad3c4b6415a9aeb829d"></a>

### `fw_app_version`

```c
uint16_t ccs811_configver_type::fw_app_version
```

<a id="a78d15d9b7695cc7dd4251cecd573a18a"></a>

### `fw_boot_version`

```c
uint16_t ccs811_configver_type::fw_boot_version
```

<a id="ad76906d24bd14e63dd7a4c1628fd81cc"></a>

### `hw_version`

```c
uint8_t ccs811_configver_type::hw_version
```

<a id="aa8dad67bbdd286a54749e421967d228d"></a>

### `mode`

```c
uint8_t ccs811_configver_type::mode
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor/ccs811.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor/ccs811.h](https://docs.zephyrproject.org/latest/doxygen/html/ccs811_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_ccs811_result_type_结构体.md)
