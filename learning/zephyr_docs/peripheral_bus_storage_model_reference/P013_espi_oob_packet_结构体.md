---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-13
title: espi_oob_packet_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__oob__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_espi\_oob\_packet\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__oob__packet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

eSPI带外事务（Out-of-Band Transaction）的数据包格式。

```c
#include <zephyr/drivers/espi.h>
```

<a id="details"></a>

eSPI 带外事务数据包格式（Out-of-band transaction packet format）。对于发送（Tx）数据包，eSPI 驱动的客户端应指定 OOB 载荷数据及其字节数。对于接收（Rx）数据包，客户端应指明可接收的最大字节数，eSPI 驱动则应以实际接收或可用的数据长度更新长度字段。注意：所有情况下，`len` 均不包含 3 字节 OOB 头部的大小。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a0b19890b5e63ecbd1b95eef57fd9263f"></a>

```c
uint8_t * buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#a0b19890b5e63ecbd1b95eef57fd9263f)。

指向数据缓冲区的指针。

<a id="r_adf45a10c88a171df8e7138929958b346"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#adf45a10c88a171df8e7138929958b346)。

数据的字节数，不包括 3 字节的 OOB 头部。

## 13.2\_详细说明（Detailed Documentation）

<a id="a0b19890b5e63ecbd1b95eef57fd9263f"></a>

### `buf`

```c
uint8_t* espi_oob_packet::buf
```

指向数据缓冲区的指针。

<a id="adf45a10c88a171df8e7138929958b346"></a>

### `len`

```c
uint16_t espi_oob_packet::len
```

数据的字节数，不包括 3 字节的 OOB 头部。

接收时，由驱动将此值更新为实际大小。

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi.h](https://docs.zephyrproject.org/latest/doxygen/html/espi_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_espi_flash_packet_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_espi_request_packet_结构体.md)
