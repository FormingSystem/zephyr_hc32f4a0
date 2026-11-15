---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-80
title: sdhc_data_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_sdhc\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD主控制器（Host Controller）的数据结构。

```c
#include <zephyr/drivers/sdhc.h>
```

<a id="details"></a>

SD 主机控制器数据结构体（Data structure）。此结构体用于向 SD 主机控制器发送数据传输请求，控制器随后将请求发送给 SD 设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 80.1\_数据成员（Data Fields）

<a id="r_aad1e8462d94b4243c981147eab6c962d"></a>

```c
unsigned int block_addr
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[block_addr](#aad1e8462d94b4243c981147eab6c962d)。

开始读取的块。

<a id="r_a20b0ca14adadcdb8d3681240faf5e7b6"></a>

```c
unsigned int block_size
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[block_size](#a20b0ca14adadcdb8d3681240faf5e7b6)。

块大小（Block Size）。

<a id="r_a47b378d455167bb8d7d05d2f058977fa"></a>

```c
unsigned int blocks
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[blocks](#a47b378d455167bb8d7d05d2f058977fa)。

块数。

<a id="r_ae68f1e7f1fbff14c24bd42fa300f9e15"></a>

```c
unsigned int bytes_xfered
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[bytes_xfered](#ae68f1e7f1fbff14c24bd42fa300f9e15)。

填入 SDHC 已发送的字节数。

<a id="r_a4f7ca31c9cee1ace999a46cce75b9f65"></a>

```c
bool is_sg_data
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_sg_data](#a4f7ca31c9cee1ace999a46cce75b9f65)。

是否为使用 `net_buf` 数据结构的分散/聚集（Scatter-gather）数据。

<a id="r_a0f656d093a5cdf3bd09ffee279ad452d"></a>

```c
void * data
```

相关声明：[data](#a0f656d093a5cdf3bd09ffee279ad452d)。

要发送或接收的数据。

<a id="r_afcf3942de27cd164b6da8dfefa864a8a"></a>

```c
int timeout_ms
```

相关声明：[timeout_ms](#afcf3942de27cd164b6da8dfefa864a8a)。

数据超时，单位为毫秒。

## 80.2\_详细说明（Detailed Documentation）

<a id="aad1e8462d94b4243c981147eab6c962d"></a>

### `block_addr`

```c
unsigned int sdhc_data::block_addr
```

开始读取的块。

<a id="a20b0ca14adadcdb8d3681240faf5e7b6"></a>

### `block_size`

```c
unsigned int sdhc_data::block_size
```

块大小（Block Size）。

<a id="a47b378d455167bb8d7d05d2f058977fa"></a>

### `blocks`

```c
unsigned int sdhc_data::blocks
```

块数。

<a id="ae68f1e7f1fbff14c24bd42fa300f9e15"></a>

### `bytes_xfered`

```c
unsigned int sdhc_data::bytes_xfered
```

填入 SDHC 已发送的字节数。

<a id="a0f656d093a5cdf3bd09ffee279ad452d"></a>

### `data`

```c
void* sdhc_data::data
```

要发送或接收的数据。

<a id="a4f7ca31c9cee1ace999a46cce75b9f65"></a>

### `is_sg_data`

```c
bool sdhc_data::is_sg_data
```

是否为使用 `net_buf` 数据结构的分散/聚集（Scatter-gather）数据。

<a id="afcf3942de27cd164b6da8dfefa864a8a"></a>

### `timeout_ms`

```c
int sdhc_data::timeout_ms
```

数据超时，单位为毫秒。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sdhc.h`

## 80.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sdhc.h](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P079_sdhc_command_结构体.md) · [返回大纲](大纲.md) · [下一章](P081_sdhc_driver_api_结构体.md)
