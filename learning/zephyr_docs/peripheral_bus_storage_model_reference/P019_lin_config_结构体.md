---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-19
title: lin_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlin__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_lin\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlin__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

局部互连网络（LIN）的配置结构。

```c
#include <zephyr/drivers/lin.h>
```

<a id="details"></a>

局部互连网络（LIN）的配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_ad8c36401d16e91a9f15a93733e42c8b9"></a>

```c
enum lin_mode mode
```

相关声明：[lin_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga4d80ed442a8a83985c6ba3658f96fd16)、[mode](#ad8c36401d16e91a9f15a93733e42c8b9)。

LIN 工作模式（Operation mode）。

<a id="r_aa61435f08c254683bced69fade50b775"></a>

```c
uint32_t baudrate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[baudrate](#aa61435f08c254683bced69fade50b775)。

LIN 波特率（Baud rate）。

<a id="r_a1ea39425c06334cab01e224eba5e6aea"></a>

```c
size_t break_len
```

相关声明：[break_len](#a1ea39425c06334cab01e224eba5e6aea)。

LIN 间隔场（Break field）的位长度。

<a id="r_a8474d3f259ecb76b0f10ace0f78ae360"></a>

```c
size_t break_delimiter_len
```

相关声明：[break_delimiter_len](#a8474d3f259ecb76b0f10ace0f78ae360)。

LIN 间隔定界符（Break delimiter）的位长度。

<a id="r_a54077348c405316ba557ef0068a5a245"></a>

```c
lin_config_flags_t flags
```

相关声明：[lin_config_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga560c00e1f3b7990836a06c83ab0eca43)、[flags](#a54077348c405316ba557ef0068a5a245)。

LIN 标志。

## 19.2\_详细说明（Detailed Documentation）

<a id="aa61435f08c254683bced69fade50b775"></a>

### `baudrate`

```c
uint32_t lin_config::baudrate
```

LIN 波特率（Baud rate）。

<a id="a8474d3f259ecb76b0f10ace0f78ae360"></a>

### `break_delimiter_len`

```c
size_t lin_config::break_delimiter_len
```

LIN 间隔定界符（Break delimiter）的位长度。

<a id="a1ea39425c06334cab01e224eba5e6aea"></a>

### `break_len`

```c
size_t lin_config::break_len
```

LIN 间隔场（Break field）的位长度。

<a id="a54077348c405316ba557ef0068a5a245"></a>

### `flags`

```c
lin_config_flags_t lin_config::flags
```

LIN 标志。

<a id="ad8c36401d16e91a9f15a93733e42c8b9"></a>

### `mode`

```c
enum lin_mode lin_config::mode
```

LIN 工作模式（Operation mode）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lin.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lin.h](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html)
- [lin_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga4d80ed442a8a83985c6ba3658f96fd16)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [lin_config_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga560c00e1f3b7990836a06c83ab0eca43)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_fpga_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_lin_driver_api_结构体.md)
