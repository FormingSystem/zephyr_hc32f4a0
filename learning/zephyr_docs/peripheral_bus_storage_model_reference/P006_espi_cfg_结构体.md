---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-6
title: espi_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_espi\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

增强型串行外设接口（eSPI）的总线配置参数。

```c
#include <zephyr/drivers/espi.h>
```

<a id="details"></a>

增强型串行外设接口（eSPI）的总线配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a75175c60a31c3a88c83772b99c2a5c34"></a>

```c
enum espi_io_mode io_caps
```

相关声明：[espi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0)、[io_caps](#a75175c60a31c3a88c83772b99c2a5c34)。

支持的 I/O 模式。

<a id="r_abb24c88ecc977d8116973d44a7e7cb94"></a>

```c
enum espi_channel channel_caps
```

相关声明：[espi_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gafaa3f7d54503c901ab23bd79a7f8a755)、[channel_caps](#abb24c88ecc977d8116973d44a7e7cb94)。

支持的通道。

<a id="r_aed88dd6fc8028a7c281260e7fa29ce21"></a>

```c
uint8_t max_freq
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_freq](#aed88dd6fc8028a7c281260e7fa29ce21)。

支持的最高频率，单位为 MHz。

## 6.2\_详细说明（Detailed Documentation）

<a id="abb24c88ecc977d8116973d44a7e7cb94"></a>

### `channel_caps`

```c
enum espi_channel espi_cfg::channel_caps
```

支持的通道。

<a id="a75175c60a31c3a88c83772b99c2a5c34"></a>

### `io_caps`

```c
enum espi_io_mode espi_cfg::io_caps
```

支持的 I/O 模式。

<a id="aed88dd6fc8028a7c281260e7fa29ce21"></a>

### `max_freq`

```c
uint8_t espi_cfg::max_freq
```

支持的最高频率，单位为 MHz。

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi.h](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)
- [espi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0)
- [espi_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gafaa3f7d54503c901ab23bd79a7f8a755)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_disk_operations_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_espi_driver_api_结构体.md)
