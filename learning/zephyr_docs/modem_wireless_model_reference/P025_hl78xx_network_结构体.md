---
id: learning.zephyr-docs.modem-wireless-model-reference.page-25
title: hl78xx_network_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__network.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_hl78xx\_network\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__network.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蜂窝网络（Cellular Network）结构。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

蜂窝网络（Cellular network）结构体，配置蜂窝网络技术和频段选择。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a0ef743013b5287ef8edd1c7414da2a81"></a>

```c
enum hl78xx_cell_rat_mode technology
```

相关声明：[hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)、[technology](#a0ef743013b5287ef8edd1c7414da2a81)。

蜂窝网络接入技术（Cellular access technology）。

<a id="r_a2c956f3333c56c34a197c5f3336030bb"></a>

```c
uint16_t * bands
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bands](#a2c956f3333c56c34a197c5f3336030bb)。

要启用的频段列表。

<a id="r_adac6d7a38cd259a908d3e6f8b8ef9961"></a>

```c
uint16_t size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[size](#adac6d7a38cd259a908d3e6f8b8ef9961)。

`bands` 数组的大小。

## 25.2\_详细说明（Detailed Documentation）

<a id="a2c956f3333c56c34a197c5f3336030bb"></a>

### `bands`

```c
uint16_t* hl78xx_network::bands
```

要启用的频段列表。

要启用的频段列表，频段由指定的蜂窝接入技术定义。如果未提供列表，则启用所有支持的频段。

<a id="adac6d7a38cd259a908d3e6f8b8ef9961"></a>

### `size`

```c
uint16_t hl78xx_network::size
```

`bands` 数组的大小。

<a id="a0ef743013b5287ef8edd1c7414da2a81"></a>

### `technology`

```c
enum hl78xx_cell_rat_mode hl78xx_network::technology
```

蜂窝网络接入技术（Cellular access technology）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_hl78xx_gnss_nmea_aux_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_hl78xx_network_info_结构体.md)
